![All brushes](contact.png)

# Brush Lab — 147 brushes · 3 Nov 2026 at 19:41

Every sheet: 1500 × 600, ten strokes in a 5 × 2 grid — 1. light line · 2. heavy line · 3. pressure swell · 4. fast wave · 5. slow wave · 6. spiral · 7. loop · 8. tilted · 9. over the wet one · 10. long, no reload (cell 8 holds «tilted» and «over the wet one» crossed). The CPU reference of Mamay's paint engine; the wet layer settles 20 s at the end.

Columns: **covered** = share of the cell with paint right after the stroke → after settling; **width** = painted area of the stroke ÷ its length (px); **dark** = mean darkness of the painted pixels above the paper's own grain (0 = paper, 1 = black); **spread** = how far wet paint went beyond the stroke (1.0 = stayed); **ms** = the stroke on the CPU; long stroke: paint in each quarter of its length (it should run out: wet → streaks → dry tail).

## Ink Line
Ink · 12 px · 23.2 s

![Ink Line](Ink-Line.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 1 % → 4 % | 4.3 px | 0.55 | 2.44 | 55 |
| heavy line | 5 % → 6 % | 15.7 px | 0.68 | 1.13 | 52 |
| pressure swell | 3 % → 4 % | 11.3 px | 0.64 | 1.40 | 48 |
| fast wave | 10 % → 11 % | 11.2 px | 0.59 | 1.11 | 104 |
| slow wave | 8 % → 10 % | 9.6 px | 0.57 | 1.16 | 117 |
| spiral | 14 % → 15 % | 8.9 px | 0.50 | 1.07 | 181 |
| loop | 8 % → 9 % | 10.6 px | 0.61 | 1.16 | 94 |
| tilted | 5 % → 5 % | 14.4 px | 0.65 | 1.05 | 43 |
| over the wet one | 10 % → 11 % | 12.5 px | 0.65 | 1.15 | 43 |
| long, no reload | 18 % → 17 % | 8.1 px | 0.47 | 0.96 | 242 | quarters: 0.22 → 0.09 → 0.04 → 0.02

Numbers say: light vs heavy: width 4.3 → 15.7 px, dark 0.55 → 0.68; wet paint spreads well beyond the stroke.

## Dense Ink
Ink · 14 px · 23.3 s

![Dense Ink](Dense-Ink.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 5 % → 7 % | 15.2 px | 0.72 | 1.26 | 98 |
| heavy line | 7 % → 7 % | 19.1 px | 0.73 | 1.09 | 65 |
| pressure swell | 5 % → 6 % | 17.9 px | 0.72 | 1.17 | 32 |
| fast wave | 13 % → 13 % | 15.3 px | 0.69 | 1.01 | 128 |
| slow wave | 12 % → 12 % | 13.6 px | 0.67 | 1.04 | 107 |
| spiral | 18 % → 15 % | 12.2 px | 0.65 | 0.80 | 210 |
| loop | 11 % → 12 % | 14.8 px | 0.69 | 1.08 | 99 |
| tilted | 5 % → 6 % | 14.6 px | 0.72 | 1.07 | 56 |
| over the wet one | 12 % → 13 % | 17.7 px | 0.72 | 1.11 | 50 |
| long, no reload | 23 % → 15 % | 10.1 px | 0.64 | 0.66 | 298 | quarters: 0.30 → 0.12 → 0.04 → 0.02

Numbers say: light vs heavy: width 15.2 → 19.1 px, dark 0.72 → 0.73.

## Transparent Wash
Watercolor · 22 px · 23.9 s

![Transparent Wash](Transparent-Wash.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 2 % → 5 % | 6.9 px | 0.27 | 2.25 | 68 |
| heavy line | 7 % → 9 % | 20.4 px | 0.27 | 1.22 | 49 |
| pressure swell | 4 % → 6 % | 15.2 px | 0.28 | 1.54 | 21 |
| fast wave | 14 % → 16 % | 16.1 px | 0.20 | 1.17 | 128 |
| slow wave | 12 % → 15 % | 13.7 px | 0.21 | 1.28 | 148 |
| spiral | 18 % → 22 % | 11.9 px | 0.16 | 1.23 | 168 |
| loop | 11 % → 13 % | 14.5 px | 0.22 | 1.20 | 82 |
| tilted | 8 % → 8 % | 21.1 px | 0.24 | 1.06 | 49 |
| over the wet one | 13 % → 16 % | 16.4 px | 0.24 | 1.18 | 40 |
| long, no reload | 26 % → 32 % | 11.6 px | 0.13 | 1.22 | 278 | quarters: 0.11 → 0.04 → 0.02 → 0.01

Numbers say: light vs heavy: width 6.9 → 20.4 px, dark 0.27 → 0.27; wet paint spreads well beyond the stroke.

## Dry Brush
Gouache · 24 px · 19.6 s

![Dry Brush](Dry-Brush.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 5 % → 0 % | 14.0 px | 0.65 | 0.09 | 141 |
| heavy line | 6 % → 0 % | 18.6 px | 0.65 | 0.02 | 85 |
| pressure swell | 5 % → 0 % | 18.2 px | 0.65 | 0.08 | 50 |
| fast wave | 6 % → 1 % | 7.3 px | 0.65 | 0.08 | 126 |
| slow wave | 7 % → 0 % | 8.1 px | 0.65 | 0.06 | 208 |
| spiral | 7 % → 0 % | 4.6 px | 0.65 | 0.07 | 235 |
| loop | 10 % → 0 % | 12.4 px | 0.65 | 0.04 | 126 |
| tilted | 4 % → 3 % | 10.6 px | 0.65 | 0.88 | 61 |
| over the wet one | 9 % → 1 % | 14.5 px | 0.65 | 0.12 | 58 |
| long, no reload | 6 % → 1 % | 2.9 px | 0.65 | 0.14 | 294 | quarters: 0.12 → 0.00 → 0.00 → 0.00

Numbers say: light vs heavy: width 14.0 → 18.6 px, dark 0.65 → 0.65.

## Wax Crayon
Wax · 8 px · 8.9 s

![Wax Crayon](Wax-Crayon.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 1 % → 1 % | 2.5 px | 0.71 | 1.00 | 66 |
| heavy line | 1 % → 1 % | 3.9 px | 0.69 | 1.00 | 14 |
| pressure swell | 1 % → 1 % | 3.3 px | 0.70 | 1.00 | 12 |
| fast wave | 3 % → 3 % | 3.5 px | 0.69 | 1.00 | 27 |
| slow wave | 3 % → 3 % | 3.4 px | 0.70 | 1.00 | 46 |
| spiral | 5 % → 5 % | 3.3 px | 0.70 | 1.00 | 72 |
| loop | 3 % → 3 % | 3.3 px | 0.70 | 1.00 | 32 |
| tilted | 2 % → 2 % | 5.6 px | 0.68 | 1.00 | 19 |
| over the wet one | 3 % → 3 % | 3.6 px | 0.68 | 1.00 | 15 |
| long, no reload | 7 % → 7 % | 3.3 px | 0.70 | 1.00 | 109 | quarters: 0.06 → 0.06 → 0.06 → 0.06

Numbers say: light vs heavy: width 2.5 → 3.9 px, dark 0.71 → 0.69; the long stroke does not run out of paint.

## Oil Pastel
Wax · 12 px · 9.0 s

![Oil Pastel](Oil-Pastel.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 1 % → 1 % | 4.0 px | 0.68 | 1.00 | 66 |
| heavy line | 2 % → 2 % | 6.5 px | 0.68 | 1.00 | 22 |
| pressure swell | 2 % → 2 % | 5.7 px | 0.69 | 1.00 | 14 |
| fast wave | 5 % → 5 % | 5.7 px | 0.68 | 1.00 | 50 |
| slow wave | 5 % → 5 % | 5.5 px | 0.68 | 1.00 | 32 |
| spiral | 8 % → 8 % | 5.5 px | 0.68 | 1.00 | 106 |
| loop | 4 % → 4 % | 5.6 px | 0.68 | 1.00 | 43 |
| tilted | 2 % → 2 % | 6.8 px | 0.68 | 1.00 | 28 |
| over the wet one | 5 % → 5 % | 5.8 px | 0.68 | 1.00 | 20 |
| long, no reload | 13 % → 13 % | 5.6 px | 0.68 | 1.00 | 129 | quarters: 0.10 → 0.09 → 0.10 → 0.10

Numbers say: light vs heavy: width 4.0 → 6.5 px, dark 0.68 → 0.68; the long stroke does not run out of paint.

## Charcoal
Charcoal · 5 px · 8.9 s

![Charcoal](Charcoal.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 1 % → 1 % | 2.0 px | 0.74 | 1.00 | 68 |
| heavy line | 1 % → 1 % | 3.0 px | 0.74 | 1.00 | 7 |
| pressure swell | 1 % → 1 % | 2.7 px | 0.74 | 1.00 | 9 |
| fast wave | 2 % → 2 % | 2.7 px | 0.73 | 1.00 | 21 |
| slow wave | 2 % → 2 % | 2.6 px | 0.74 | 1.00 | 38 |
| spiral | 4 % → 4 % | 2.5 px | 0.74 | 1.00 | 68 |
| loop | 2 % → 2 % | 2.6 px | 0.74 | 1.00 | 28 |
| tilted | 2 % → 2 % | 4.3 px | 0.72 | 1.00 | 16 |
| over the wet one | 2 % → 2 % | 2.4 px | 0.72 | 1.00 | 15 |
| long, no reload | 6 % → 6 % | 2.7 px | 0.73 | 1.00 | 91 | quarters: 0.05 → 0.05 → 0.05 → 0.05

Numbers say: light vs heavy: width 2.0 → 3.0 px, dark 0.74 → 0.74; the long stroke does not run out of paint.

## Impasto
Heavy acrylic · 22 px · 13.2 s

![Impasto](Impasto.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 8 % → 8 % | 24.1 px | 0.71 | 0.93 | 133 |
| heavy line | 10 % → 9 % | 28.8 px | 0.70 | 0.94 | 69 |
| pressure swell | 7 % → 7 % | 28.1 px | 0.72 | 0.94 | 49 |
| fast wave | 20 % → 13 % | 23.5 px | 0.71 | 0.64 | 137 |
| slow wave | 21 % → 14 % | 24.5 px | 0.71 | 0.66 | 193 |
| spiral | 30 % → 14 % | 20.0 px | 0.71 | 0.46 | 226 |
| loop | 18 % → 14 % | 23.9 px | 0.71 | 0.77 | 99 |
| tilted | 8 % → 8 % | 21.8 px | 0.70 | 1.00 | 66 |
| over the wet one | 17 % → 15 % | 25.4 px | 0.70 | 0.91 | 63 |
| long, no reload | 34 % → 14 % | 15.2 px | 0.71 | 0.41 | 326 | quarters: 0.38 → 0.21 → 0.10 → 0.03

Numbers say: light vs heavy: width 24.1 → 28.8 px, dark 0.71 → 0.70.

## Oil Round
Oil · 18 px · 15.9 s

![Oil Round](Oil-Round.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 2 % → 2 % | 7.2 px | 0.75 | 1.00 | 154 |
| heavy line | 7 % → 7 % | 19.3 px | 0.73 | 1.00 | 67 |
| pressure swell | 4 % → 4 % | 13.7 px | 0.72 | 1.00 | 30 |
| fast wave | 11 % → 11 % | 12.7 px | 0.65 | 1.00 | 136 |
| slow wave | 8 % → 8 % | 9.0 px | 0.57 | 1.00 | 158 |
| spiral | 10 % → 10 % | 6.6 px | 0.50 | 1.00 | 175 |
| loop | 5 % → 5 % | 7.1 px | 0.45 | 1.00 | 100 |
| tilted | 4 % → 4 % | 10.1 px | 0.52 | 1.00 | 49 |
| over the wet one | 6 % → 6 % | 7.4 px | 0.52 | 1.00 | 45 |
| long, no reload | 15 % → 15 % | 6.8 px | 0.42 | 1.00 | 304 | quarters: 0.08 → 0.08 → 0.07 → 0.06

Numbers say: light vs heavy: width 7.2 → 19.3 px, dark 0.75 → 0.73.

## Palette Knife
Oil · 20 px · 15.7 s

![Palette Knife](Palette-Knife.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 8 % → 8 % | 21.9 px | 0.67 | 1.00 | 102 |
| heavy line | 8 % → 8 % | 22.5 px | 0.73 | 1.00 | 14 |
| pressure swell | 6 % → 6 % | 22.4 px | 0.74 | 1.00 | 11 |
| fast wave | 17 % → 17 % | 19.3 px | 0.49 | 1.00 | 23 |
| slow wave | 17 % → 17 % | 19.9 px | 0.43 | 1.00 | 47 |
| spiral | 18 % → 18 % | 11.7 px | 0.45 | 1.00 | 43 |
| loop | 16 % → 16 % | 21.0 px | 0.58 | 1.00 | 21 |
| tilted | 5 % → 5 % | 15.0 px | 0.72 | 1.00 | 13 |
| over the wet one | 13 % → 13 % | 21.0 px | 0.72 | 1.00 | 12 |
| long, no reload | 17 % → 17 % | 7.5 px | 0.47 | 1.00 | 58 | quarters: 0.29 → 0.05 → 0.00 → 0.00

Numbers say: light vs heavy: width 21.9 → 22.5 px, dark 0.67 → 0.73; pressure barely changes the width.

## Water
Watercolor · 20 px · 33.0 s · over bands of wet oil paint and oil pastel in turn (it works on paint already there: look at what it does to the bands; covered counts the bands too)

![Water](Water.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 25 % → 27 % | 73.8 px | 0.80 | 1.06 | 28 |
| heavy line | 24 % → 25 % | 69.8 px | 0.81 | 1.04 | 51 |
| pressure swell | 24 % → 25 % | 89.6 px | 0.81 | 1.03 | 31 |
| fast wave | 24 % → 26 % | 27.7 px | 0.81 | 1.07 | 100 |
| slow wave | 24 % → 25 % | 27.7 px | 0.81 | 1.06 | 128 |
| spiral | 24 % → 26 % | 15.9 px | 0.81 | 1.07 | 161 |
| loop | 24 % → 25 % | 31.1 px | 0.81 | 1.03 | 81 |
| tilted | 24 % → 24 % | 67.0 px | 0.81 | 1.00 | 54 |
| over the wet one | 24 % → 25 % | 0.0 px | 0.81 | 1.06 | 42 |
| long, no reload | 24 % → 26 % | 10.7 px | 0.81 | 1.08 | 233 | quarters: 0.21 → 0.27 → 0.18 → 0.27

Numbers say: light vs heavy: width 73.8 → 69.8 px, dark 0.80 → 0.81; pressure barely changes the width; the long stroke does not run out of paint.

## Blender
Pastel · 16 px · 18.8 s · over bands of wet oil paint and oil pastel in turn (it works on paint already there: look at what it does to the bands; covered counts the bands too)

![Blender](Blender.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 24 % → 24 % | 70.7 px | 0.81 | 1.00 | 21 |
| heavy line | 25 % → 25 % | 72.1 px | 0.80 | 1.00 | 28 |
| pressure swell | 24 % → 24 % | 91.3 px | 0.81 | 1.00 | 19 |
| fast wave | 26 % → 26 % | 30.0 px | 0.79 | 1.00 | 69 |
| slow wave | 26 % → 26 % | 29.9 px | 0.80 | 1.00 | 72 |
| spiral | 28 % → 28 % | 18.7 px | 0.77 | 1.00 | 104 |
| loop | 25 % → 25 % | 32.9 px | 0.80 | 1.00 | 50 |
| tilted | 25 % → 25 % | 70.1 px | 0.79 | 1.00 | 37 |
| over the wet one | 26 % → 26 % | 1.8 px | 0.79 | 1.00 | 19 |
| long, no reload | 30 % → 30 % | 13.7 px | 0.76 | 1.00 | 166 | quarters: 0.20 → 0.28 → 0.23 → 0.30

Numbers say: light vs heavy: width 70.7 → 72.1 px, dark 0.81 → 0.80; pressure barely changes the width; the long stroke does not run out of paint.

## Eraser
Eraser · 16 px · 18.0 s · over bands of wet oil paint and oil pastel in turn (it works on paint already there: look at what it does to the bands; covered counts the bands too)

![Eraser](Eraser.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 24 % → 24 % | 69.5 px | 0.82 | 1.00 | 25 |
| heavy line | 23 % → 23 % | 67.9 px | 0.82 | 1.00 | 30 |
| pressure swell | 23 % → 23 % | 87.3 px | 0.82 | 1.00 | 21 |
| fast wave | 22 % → 22 % | 25.7 px | 0.82 | 1.00 | 62 |
| slow wave | 22 % → 22 % | 25.7 px | 0.82 | 1.00 | 79 |
| spiral | 22 % → 22 % | 14.4 px | 0.82 | 1.00 | 96 |
| loop | 22 % → 22 % | 28.6 px | 0.82 | 1.00 | 46 |
| tilted | 23 % → 23 % | 65.1 px | 0.82 | 1.00 | 36 |
| over the wet one | 23 % → 23 % | 0.0 px | 0.82 | 1.00 | 20 |
| long, no reload | 20 % → 20 % | 8.9 px | 0.82 | 1.00 | 117 | quarters: 0.15 → 0.20 → 0.15 → 0.20

Numbers say: light vs heavy: width 69.5 → 67.9 px, dark 0.82 → 0.82; pressure barely changes the width; the long stroke does not run out of paint.

## Fan
Gouache · 30 px · 27.3 s

![Fan](Fan.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 9 % → 3 % | 25.7 px | 0.63 | 0.37 | 25 |
| heavy line | 11 % → 4 % | 31.0 px | 0.63 | 0.39 | 48 |
| pressure swell | 8 % → 5 % | 31.7 px | 0.63 | 0.55 | 23 |
| fast wave | 18 % → 5 % | 20.3 px | 0.63 | 0.26 | 91 |
| slow wave | 18 % → 5 % | 21.1 px | 0.63 | 0.25 | 155 |
| spiral | 24 % → 5 % | 15.8 px | 0.63 | 0.20 | 154 |
| loop | 17 % → 5 % | 22.7 px | 0.63 | 0.29 | 84 |
| tilted | 5 % → 6 % | 15.1 px | 0.63 | 1.05 | 29 |
| over the wet one | 16 % → 8 % | 29.8 px | 0.63 | 0.50 | 42 |
| long, no reload | 23 % → 5 % | 10.1 px | 0.63 | 0.22 | 218 | quarters: 0.29 → 0.07 → 0.01 → 0.00

Numbers say: light vs heavy: width 25.7 → 31.0 px, dark 0.63 → 0.63.

## Sponge
Gouache · 30 px · 27.0 s

![Sponge](Sponge.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 4 % → 0 % | 11.4 px | 0.62 | 0.12 | 30 |
| heavy line | 12 % → 2 % | 35.4 px | 0.62 | 0.14 | 58 |
| pressure swell | 7 % → 2 % | 27.9 px | 0.62 | 0.27 | 35 |
| fast wave | 20 % → 4 % | 23.2 px | 0.62 | 0.19 | 115 |
| slow wave | 21 % → 4 % | 23.7 px | 0.62 | 0.18 | 205 |
| spiral | 28 % → 4 % | 18.3 px | 0.62 | 0.14 | 168 |
| loop | 18 % → 5 % | 23.0 px | 0.62 | 0.29 | 98 |
| tilted | 7 % → 7 % | 18.2 px | 0.62 | 1.04 | 88 |
| over the wet one | 16 % → 6 % | 27.8 px | 0.62 | 0.37 | 47 |
| long, no reload | 29 % → 5 % | 12.9 px | 0.62 | 0.17 | 266 | quarters: 0.29 → 0.13 → 0.07 → 0.04

Numbers say: light vs heavy: width 11.4 → 35.4 px, dark 0.62 → 0.62.

## Ink — sumi brush
Watercolor · 22 px · 26.9 s

![Ink — sumi brush](Ink-sumi-brush.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 8 % → 9 % | 23.8 px | 0.77 | 1.13 | 54 |
| heavy line | 13 % → 13 % | 38.0 px | 0.72 | 1.01 | 66 |
| pressure swell | 9 % → 10 % | 34.5 px | 0.75 | 1.05 | 41 |
| fast wave | 27 % → 28 % | 31.7 px | 0.58 | 1.03 | 159 |
| slow wave | 25 % → 26 % | 29.0 px | 0.61 | 1.05 | 229 |
| spiral | 37 % → 38 % | 24.3 px | 0.51 | 1.03 | 261 |
| loop | 22 % → 22 % | 28.2 px | 0.66 | 1.03 | 123 |
| tilted | 9 % → 9 % | 24.7 px | 0.73 | 1.03 | 81 |
| over the wet one | 20 % → 21 % | 31.1 px | 0.73 | 1.03 | 67 |
| long, no reload | 42 % → 43 % | 18.9 px | 0.46 | 1.02 | 355 | quarters: 0.47 → 0.23 → 0.11 → 0.06

Numbers say: light vs heavy: width 23.8 → 38.0 px, dark 0.77 → 0.72.

## Ink — wash
Watercolor · 40 px · 30.2 s

![Ink — wash](Ink-wash.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 13 % → 13 % | 36.5 px | 0.17 | 1.04 | 66 |
| heavy line | 18 % → 19 % | 53.5 px | 0.13 | 1.04 | 79 |
| pressure swell | 12 % → 13 % | 46.6 px | 0.16 | 1.05 | 56 |
| fast wave | 40 % → 42 % | 45.9 px | 0.12 | 1.06 | 190 |
| slow wave | 38 % → 40 % | 43.6 px | 0.17 | 1.06 | 307 |
| spiral | 58 % → 62 % | 38.5 px | 0.12 | 1.06 | 322 |
| loop | 33 % → 34 % | 42.9 px | 0.15 | 1.03 | 169 |
| tilted | 14 % → 14 % | 38.1 px | 0.17 | 1.03 | 98 |
| over the wet one | 29 % → 31 % | 43.2 px | 0.17 | 1.06 | 83 |
| long, no reload | 66 % → 75 % | 29.8 px | 0.12 | 1.12 | 456 | quarters: 0.16 → 0.11 → 0.07 → 0.04

Numbers say: light vs heavy: width 36.5 → 53.5 px, dark 0.17 → 0.13.

## Ink — dry brush
Ink · 30 px · 22.7 s

![Ink — dry brush](Ink-dry-brush.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 9 % → 7 % | 25.2 px | 0.81 | 0.79 | 76 |
| heavy line | 10 % → 8 % | 29.6 px | 0.80 | 0.76 | 110 |
| pressure swell | 7 % → 6 % | 27.9 px | 0.81 | 0.85 | 63 |
| fast wave | 21 % → 8 % | 24.2 px | 0.79 | 0.40 | 208 |
| slow wave | 18 % → 7 % | 20.3 px | 0.79 | 0.39 | 361 |
| spiral | 24 % → 8 % | 15.6 px | 0.78 | 0.34 | 347 |
| loop | 19 % → 8 % | 24.3 px | 0.78 | 0.45 | 182 |
| tilted | 8 % → 8 % | 22.2 px | 0.78 | 1.02 | 113 |
| over the wet one | 17 % → 14 % | 25.9 px | 0.78 | 0.81 | 86 |
| long, no reload | 20 % → 8 % | 9.1 px | 0.79 | 0.41 | 497 | quarters: 0.32 → 0.02 → 0.00 → 0.00

Numbers say: light vs heavy: width 25.2 → 29.6 px, dark 0.81 → 0.80.

## Ink — nib
Watercolor · 5 px · 21.8 s

![Ink — nib](Ink-nib.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 2 % → 5 % | 5.4 px | 0.86 | 2.45 | 23 |
| heavy line | 2 % → 5 % | 6.4 px | 0.86 | 2.33 | 25 |
| pressure swell | 2 % → 4 % | 6.2 px | 0.86 | 2.52 | 21 |
| fast wave | 5 % → 8 % | 5.8 px | 0.82 | 1.65 | 54 |
| slow wave | 5 % → 8 % | 5.6 px | 0.82 | 1.73 | 61 |
| spiral | 7 % → 11 % | 4.8 px | 0.75 | 1.45 | 76 |
| loop | 4 % → 8 % | 5.6 px | 0.84 | 1.75 | 56 |
| tilted | 4 % → 4 % | 10.1 px | 0.85 | 1.04 | 25 |
| over the wet one | 6 % → 9 % | 6.3 px | 0.85 | 1.61 | 21 |
| long, no reload | 9 % → 12 % | 4.0 px | 0.70 | 1.37 | 134 | quarters: 0.23 → 0.08 → 0.04 → 0.02

Numbers say: light vs heavy: width 5.4 → 6.4 px, dark 0.86 → 0.86; wet paint spreads well beyond the stroke.

## 0.45 · Dry brush
Gouache · 34 px · 23.9 s

![0.45 · Dry brush](0-45-Dry-brush.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 10 % → 3 % | 29.4 px | 0.67 | 0.29 | 96 |
| heavy line | 11 % → 3 % | 31.6 px | 0.67 | 0.30 | 106 |
| pressure swell | 8 % → 3 % | 31.5 px | 0.67 | 0.41 | 92 |
| fast wave | 19 % → 3 % | 22.5 px | 0.67 | 0.18 | 259 |
| slow wave | 20 % → 4 % | 23.2 px | 0.67 | 0.18 | 453 |
| spiral | 21 % → 3 % | 14.1 px | 0.67 | 0.16 | 476 |
| loop | 20 % → 4 % | 26.1 px | 0.67 | 0.20 | 254 |
| tilted | 9 % → 8 % | 24.0 px | 0.67 | 0.98 | 164 |
| over the wet one | 19 % → 6 % | 28.2 px | 0.67 | 0.34 | 118 |
| long, no reload | 20 % → 4 % | 9.1 px | 0.67 | 0.19 | 649 | quarters: 0.36 → 0.10 → 0.00 → 0.00

Numbers say: light vs heavy: width 29.4 → 31.6 px, dark 0.67 → 0.67; pressure barely changes the width.

## Dry pastel
Pastel · 26 px · 10.0 s

![Dry pastel](Dry-pastel.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 3 % → 3 % | 8.3 px | 0.38 | 1.00 | 24 |
| heavy line | 5 % → 5 % | 13.2 px | 0.39 | 1.00 | 30 |
| pressure swell | 3 % → 3 % | 11.7 px | 0.38 | 1.00 | 26 |
| fast wave | 10 % → 10 % | 11.9 px | 0.39 | 1.00 | 72 |
| slow wave | 10 % → 10 % | 11.3 px | 0.39 | 1.00 | 132 |
| spiral | 15 % → 15 % | 9.6 px | 0.39 | 1.00 | 129 |
| loop | 7 % → 7 % | 9.4 px | 0.39 | 1.00 | 72 |
| tilted | 3 % → 3 % | 8.3 px | 0.38 | 1.00 | 39 |
| over the wet one | 7 % → 7 % | 11.1 px | 0.38 | 1.00 | 34 |
| long, no reload | 18 % → 18 % | 8.2 px | 0.39 | 1.00 | 188 | quarters: 0.08 → 0.08 → 0.08 → 0.07

Numbers say: light vs heavy: width 8.3 → 13.2 px, dark 0.38 → 0.39; the long stroke does not run out of paint.

## 0.45 · Charcoal
Charcoal · 18 px · 9.4 s

![0.45 · Charcoal](0-45-Charcoal.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 2 % → 2 % | 6.5 px | 0.80 | 1.00 | 14 |
| heavy line | 3 % → 3 % | 9.2 px | 0.80 | 1.00 | 10 |
| pressure swell | 2 % → 2 % | 8.8 px | 0.80 | 1.00 | 9 |
| fast wave | 7 % → 7 % | 8.5 px | 0.80 | 1.00 | 44 |
| slow wave | 7 % → 7 % | 8.0 px | 0.80 | 1.00 | 57 |
| spiral | 12 % → 12 % | 7.9 px | 0.80 | 1.00 | 69 |
| loop | 6 % → 6 % | 8.1 px | 0.80 | 1.00 | 37 |
| tilted | 3 % → 3 % | 7.5 px | 0.80 | 1.00 | 23 |
| over the wet one | 6 % → 6 % | 7.9 px | 0.80 | 1.00 | 10 |
| long, no reload | 17 % → 17 % | 7.8 px | 0.80 | 1.00 | 83 | quarters: 0.15 → 0.16 → 0.15 → 0.16

Numbers say: light vs heavy: width 6.5 → 9.2 px, dark 0.80 → 0.80; the long stroke does not run out of paint.

## Watercolour — wash
Watercolor · 50 px · 32.9 s

![Watercolour — wash](Watercolour-wash.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 15 % → 16 % | 43.3 px | 0.03 | 1.05 | 87 |
| heavy line | 21 % → 22 % | 62.1 px | 0.03 | 1.04 | 106 |
| pressure swell | 14 % → 15 % | 54.3 px | 0.03 | 1.04 | 83 |
| fast wave | 47 % → 49 % | 53.8 px | 0.02 | 1.04 | 270 |
| slow wave | 45 % → 46 % | 52.0 px | 0.04 | 1.03 | 437 |
| spiral | 64 % → 66 % | 42.5 px | 0.03 | 1.03 | 438 |
| loop | 39 % → 40 % | 50.3 px | 0.03 | 1.02 | 233 |
| tilted | 17 % → 17 % | 47.3 px | 0.04 | 1.03 | 154 |
| over the wet one | 35 % → 36 % | 49.0 px | 0.04 | 1.04 | 104 |
| long, no reload | 79 % → 84 % | 35.5 px | 0.03 | 1.06 | 631 | quarters: 0.04 → 0.03 → 0.02 → 0.01

Numbers say: light vs heavy: width 43.3 → 62.1 px, dark 0.03 → 0.03.

## Watercolour — wet-in-wet
Watercolor · 44 px · 30.8 s

![Watercolour — wet-in-wet](Watercolour-wet-in-wet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 13 % → 13 % | 36.6 px | 0.07 | 1.05 | 92 |
| heavy line | 18 % → 19 % | 52.4 px | 0.06 | 1.04 | 107 |
| pressure swell | 12 % → 12 % | 44.9 px | 0.07 | 1.04 | 66 |
| fast wave | 40 % → 41 % | 45.9 px | 0.05 | 1.04 | 204 |
| slow wave | 39 % → 40 % | 45.0 px | 0.08 | 1.03 | 357 |
| spiral | 62 % → 63 % | 40.8 px | 0.06 | 1.02 | 365 |
| loop | 33 % → 34 % | 43.2 px | 0.07 | 1.03 | 179 |
| tilted | 14 % → 15 % | 39.1 px | 0.08 | 1.04 | 124 |
| over the wet one | 29 % → 31 % | 42.0 px | 0.08 | 1.05 | 89 |
| long, no reload | 75 % → 78 % | 33.6 px | 0.06 | 1.04 | 532 | quarters: 0.07 → 0.06 → 0.04 → 0.03

Numbers say: light vs heavy: width 36.6 → 52.4 px, dark 0.07 → 0.06.

## Watercolour — glaze
Watercolor · 38 px · 29.4 s

![Watercolour — glaze](Watercolour-glaze.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 12 % → 13 % | 35.2 px | 0.03 | 1.05 | 75 |
| heavy line | 18 % → 19 % | 52.2 px | 0.02 | 1.06 | 78 |
| pressure swell | 12 % → 13 % | 44.6 px | 0.02 | 1.07 | 53 |
| fast wave | 37 % → 40 % | 42.4 px | 0.02 | 1.08 | 194 |
| slow wave | 35 % → 37 % | 40.2 px | 0.02 | 1.08 | 321 |
| spiral | 54 % → 59 % | 35.9 px | 0.02 | 1.09 | 347 |
| loop | 32 % → 33 % | 40.8 px | 0.02 | 1.05 | 161 |
| tilted | 13 % → 14 % | 37.0 px | 0.03 | 1.03 | 108 |
| over the wet one | 28 % → 30 % | 41.7 px | 0.03 | 1.06 | 82 |
| long, no reload | 60 % → 69 % | 26.8 px | 0.02 | 1.15 | 472 | quarters: 0.02 → 0.01 → 0.01 → 0.00

Numbers say: light vs heavy: width 35.2 → 52.2 px, dark 0.03 → 0.02.

## Watercolour — granulating
Watercolor · 44 px · 30.9 s

![Watercolour — granulating](Watercolour-granulating.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 14 % → 14 % | 40.5 px | 0.05 | 1.03 | 78 |
| heavy line | 20 % → 21 % | 59.2 px | 0.04 | 1.02 | 105 |
| pressure swell | 14 % → 14 % | 51.3 px | 0.05 | 1.02 | 71 |
| fast wave | 44 % → 45 % | 50.3 px | 0.04 | 1.04 | 236 |
| slow wave | 40 % → 42 % | 46.0 px | 0.06 | 1.06 | 396 |
| spiral | 59 % → 63 % | 38.7 px | 0.04 | 1.07 | 382 |
| loop | 36 % → 37 % | 46.9 px | 0.05 | 1.02 | 206 |
| tilted | 15 % → 16 % | 43.1 px | 0.06 | 1.03 | 130 |
| over the wet one | 32 % → 33 % | 46.6 px | 0.06 | 1.04 | 130 |
| long, no reload | 68 % → 76 % | 30.3 px | 0.04 | 1.12 | 551 | quarters: 0.06 → 0.04 → 0.02 → 0.02

Numbers say: light vs heavy: width 40.5 → 59.2 px, dark 0.05 → 0.04.

## Watercolour — dry brush
Watercolor · 36 px · 25.1 s

![Watercolour — dry brush](Watercolour-dry-brush.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 9 % → 9 % | 24.9 px | 0.07 | 1.09 | 84 |
| heavy line | 13 % → 13 % | 36.7 px | 0.06 | 0.99 | 102 |
| pressure swell | 10 % → 10 % | 36.4 px | 0.06 | 1.04 | 69 |
| fast wave | 24 % → 19 % | 27.3 px | 0.05 | 0.82 | 323 |
| slow wave | 22 % → 17 % | 25.2 px | 0.05 | 0.78 | 399 |
| spiral | 29 % → 20 % | 19.3 px | 0.05 | 0.67 | 377 |
| loop | 19 % → 18 % | 24.6 px | 0.05 | 0.94 | 186 |
| tilted | 9 % → 10 % | 24.3 px | 0.06 | 1.10 | 121 |
| over the wet one | 20 % → 20 % | 31.7 px | 0.06 | 0.99 | 95 |
| long, no reload | 28 % → 19 % | 12.4 px | 0.05 | 0.70 | 578 | quarters: 0.03 → 0.01 → 0.00 → 0.00

Numbers say: light vs heavy: width 24.9 → 36.7 px, dark 0.07 → 0.06.

## Gouache
Gouache · 30 px · 24.3 s

![Gouache](Gouache.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 8 % → 5 % | 24.4 px | 0.28 | 0.64 | 75 |
| heavy line | 14 % → 6 % | 39.7 px | 0.28 | 0.47 | 80 |
| pressure swell | 10 % → 6 % | 38.6 px | 0.28 | 0.60 | 56 |
| fast wave | 28 % → 7 % | 32.2 px | 0.28 | 0.25 | 188 |
| slow wave | 27 % → 8 % | 31.4 px | 0.28 | 0.29 | 281 |
| spiral | 38 % → 8 % | 24.8 px | 0.27 | 0.22 | 325 |
| loop | 22 % → 8 % | 28.6 px | 0.28 | 0.35 | 166 |
| tilted | 9 % → 9 % | 23.8 px | 0.27 | 1.01 | 112 |
| over the wet one | 20 % → 13 % | 31.1 px | 0.27 | 0.66 | 81 |
| long, no reload | 40 % → 9 % | 17.9 px | 0.27 | 0.24 | 469 | quarters: 0.01 → 0.01 → 0.02 → 0.02

Numbers say: light vs heavy: width 24.4 → 39.7 px, dark 0.28 → 0.28; the long stroke does not run out of paint.

## Oil — alla prima
Oil · 30 px · 17.5 s

![Oil — alla prima](Oil-alla-prima.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 9 % → 9 % | 27.6 px | 0.51 | 1.00 | 82 |
| heavy line | 10 % → 10 % | 30.3 px | 0.51 | 1.00 | 80 |
| pressure swell | 8 % → 8 % | 29.8 px | 0.53 | 1.00 | 64 |
| fast wave | 24 % → 24 % | 28.1 px | 0.51 | 1.00 | 207 |
| slow wave | 26 % → 26 % | 29.5 px | 0.51 | 1.00 | 355 |
| spiral | 40 % → 40 % | 26.4 px | 0.50 | 1.00 | 378 |
| loop | 21 % → 21 % | 27.6 px | 0.52 | 1.00 | 194 |
| tilted | 11 % → 11 % | 30.4 px | 0.51 | 1.00 | 96 |
| over the wet one | 20 % → 20 % | 26.5 px | 0.51 | 1.00 | 91 |
| long, no reload | 49 % → 49 % | 22.0 px | 0.50 | 1.00 | 523 | quarters: 0.32 → 0.28 → 0.25 → 0.22

Numbers say: light vs heavy: width 27.6 → 30.3 px, dark 0.51 → 0.51; pressure barely changes the width.

## Oil — impasto
Oil · 34 px · 18.3 s

![Oil — impasto](Oil-impasto.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 12 % → 12 % | 33.4 px | 0.25 | 1.00 | 110 |
| heavy line | 12 % → 12 % | 36.3 px | 0.25 | 1.00 | 101 |
| pressure swell | 10 % → 10 % | 35.9 px | 0.26 | 1.00 | 75 |
| fast wave | 30 % → 30 % | 35.1 px | 0.25 | 1.00 | 259 |
| slow wave | 31 % → 31 % | 35.7 px | 0.25 | 1.00 | 444 |
| spiral | 52 % → 52 % | 34.0 px | 0.23 | 1.00 | 479 |
| loop | 26 % → 26 % | 33.7 px | 0.24 | 1.00 | 247 |
| tilted | 12 % → 12 % | 32.8 px | 0.26 | 1.00 | 134 |
| over the wet one | 23 % → 23 % | 31.9 px | 0.26 | 1.00 | 95 |
| long, no reload | 60 % → 60 % | 26.9 px | 0.22 | 1.00 | 725 | quarters: 0.18 → 0.16 → 0.13 → 0.10

Numbers say: light vs heavy: width 33.4 → 36.3 px, dark 0.25 → 0.25; pressure barely changes the width.

## Oil — glaze
Oil · 40 px · 14.9 s

![Oil — glaze](Oil-glaze.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 9 % → 9 % | 25.4 px | 0.50 | 1.00 | 94 |
| heavy line | 13 % → 13 % | 36.3 px | 0.49 | 1.00 | 111 |
| pressure swell | 9 % → 9 % | 35.3 px | 0.50 | 1.00 | 77 |
| fast wave | 26 % → 26 % | 30.1 px | 0.48 | 1.00 | 268 |
| slow wave | 29 % → 29 % | 33.7 px | 0.49 | 1.00 | 449 |
| spiral | 44 % → 44 % | 29.0 px | 0.49 | 1.00 | 440 |
| loop | 23 % → 23 % | 30.2 px | 0.50 | 1.00 | 272 |
| tilted | 10 % → 10 % | 28.9 px | 0.50 | 1.00 | 137 |
| over the wet one | 22 % → 22 % | 31.6 px | 0.50 | 1.00 | 98 |
| long, no reload | 51 % → 51 % | 22.7 px | 0.49 | 1.00 | 621 | quarters: 0.33 → 0.29 → 0.26 → 0.22

Numbers say: light vs heavy: width 25.4 → 36.3 px, dark 0.50 → 0.49.

## Oil — scumble
Oil · 36 px · 19.0 s

![Oil — scumble](Oil-scumble.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 11 % → 11 % | 33.1 px | 0.27 | 1.00 | 103 |
| heavy line | 12 % → 12 % | 36.1 px | 0.27 | 1.00 | 122 |
| pressure swell | 9 % → 9 % | 35.5 px | 0.28 | 1.00 | 104 |
| fast wave | 26 % → 26 % | 29.6 px | 0.19 | 1.00 | 322 |
| slow wave | 27 % → 27 % | 30.9 px | 0.18 | 1.00 | 515 |
| spiral | 41 % → 41 % | 27.1 px | 0.13 | 1.00 | 517 |
| loop | 24 % → 24 % | 30.6 px | 0.20 | 1.00 | 268 |
| tilted | 11 % → 11 % | 30.4 px | 0.25 | 1.00 | 148 |
| over the wet one | 22 % → 22 % | 31.4 px | 0.25 | 1.00 | 125 |
| long, no reload | 45 % → 45 % | 20.3 px | 0.12 | 1.00 | 739 | quarters: 0.00 → 0.00 → 0.00 → 0.00

Numbers say: light vs heavy: width 33.1 → 36.1 px, dark 0.27 → 0.27; pressure barely changes the width.

## Acrylic — heavy body
Heavy acrylic · 30 px · 13.9 s

![Acrylic — heavy body](Acrylic-heavy-body.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 10 % → 9 % | 28.9 px | 0.51 | 0.91 | 76 |
| heavy line | 11 % → 10 % | 31.1 px | 0.51 | 0.93 | 88 |
| pressure swell | 8 % → 8 % | 30.7 px | 0.53 | 0.94 | 74 |
| fast wave | 23 % → 15 % | 26.5 px | 0.52 | 0.64 | 237 |
| slow wave | 24 % → 16 % | 27.7 px | 0.51 | 0.65 | 359 |
| spiral | 35 % → 15 % | 23.3 px | 0.51 | 0.43 | 362 |
| loop | 21 % → 16 % | 26.9 px | 0.51 | 0.76 | 188 |
| tilted | 9 % → 9 % | 24.9 px | 0.52 | 0.99 | 112 |
| over the wet one | 19 % → 17 % | 27.7 px | 0.52 | 0.89 | 90 |
| long, no reload | 39 % → 16 % | 17.3 px | 0.51 | 0.41 | 539 | quarters: 0.29 → 0.20 → 0.12 → 0.04

Numbers say: light vs heavy: width 28.9 → 31.1 px, dark 0.51 → 0.51; pressure barely changes the width.

## Acrylic — fluid
Watercolor · 36 px · 29.5 s

![Acrylic — fluid](Acrylic-fluid.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 12 % → 12 % | 34.3 px | 0.08 | 1.02 | 71 |
| heavy line | 18 % → 18 % | 51.6 px | 0.07 | 1.01 | 78 |
| pressure swell | 12 % → 12 % | 44.8 px | 0.08 | 1.01 | 63 |
| fast wave | 37 % → 38 % | 42.6 px | 0.07 | 1.02 | 203 |
| slow wave | 34 % → 35 % | 39.2 px | 0.07 | 1.03 | 324 |
| spiral | 52 % → 53 % | 34.2 px | 0.07 | 1.03 | 321 |
| loop | 30 % → 31 % | 39.4 px | 0.07 | 1.02 | 174 |
| tilted | 12 % → 12 % | 32.6 px | 0.08 | 1.04 | 104 |
| over the wet one | 27 % → 28 % | 43.2 px | 0.08 | 1.02 | 88 |
| long, no reload | 56 % → 58 % | 25.3 px | 0.06 | 1.04 | 465 | quarters: 0.06 → 0.05 → 0.03 → 0.02

Numbers say: light vs heavy: width 34.3 → 51.6 px, dark 0.08 → 0.07.

## Acrylic — palette knife
Heavy acrylic · 42 px · 18.0 s

![Acrylic — palette knife](Acrylic-palette-knife.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 15 % → 15 % | 44.0 px | 0.36 | 0.98 | 27 |
| heavy line | 15 % → 15 % | 44.2 px | 0.38 | 0.97 | 23 |
| pressure swell | 12 % → 12 % | 43.5 px | 0.40 | 0.99 | 11 |
| fast wave | 36 % → 20 % | 41.9 px | 0.35 | 0.56 | 63 |
| slow wave | 37 % → 21 % | 42.6 px | 0.35 | 0.57 | 96 |
| spiral | 50 % → 18 % | 32.8 px | 0.35 | 0.37 | 102 |
| loop | 32 % → 24 % | 41.2 px | 0.34 | 0.75 | 49 |
| tilted | 12 % → 12 % | 33.6 px | 0.37 | 1.00 | 21 |
| over the wet one | 26 % → 25 % | 39.7 px | 0.37 | 0.97 | 22 |
| long, no reload | 57 % → 21 % | 25.7 px | 0.33 | 0.36 | 141 | quarters: 0.00 → 0.00 → 0.00 → 0.01

Numbers say: light vs heavy: width 44.0 → 44.2 px, dark 0.36 → 0.38; pressure barely changes the width; the long stroke does not run out of paint.

## Finger on oil
Oil · 30 px · 13.0 s

![Finger on oil](Finger-on-oil.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 8 % → 8 % | 23.7 px | 0.40 | 1.00 | 55 |
| heavy line | 13 % → 13 % | 36.5 px | 0.38 | 1.00 | 77 |
| pressure swell | 9 % → 9 % | 33.3 px | 0.41 | 1.00 | 50 |
| fast wave | 22 % → 22 % | 26.0 px | 0.35 | 1.00 | 141 |
| slow wave | 24 % → 24 % | 27.8 px | 0.35 | 1.00 | 211 |
| spiral | 36 % → 36 % | 23.5 px | 0.27 | 1.00 | 221 |
| loop | 21 % → 21 % | 27.3 px | 0.36 | 1.00 | 105 |
| tilted | 9 % → 9 % | 26.4 px | 0.39 | 1.00 | 85 |
| over the wet one | 20 % → 20 % | 29.3 px | 0.39 | 1.00 | 55 |
| long, no reload | 36 % → 36 % | 16.3 px | 0.26 | 1.00 | 314 | quarters: 0.23 → 0.11 → 0.05 → 0.02

Numbers say: light vs heavy: width 23.7 → 36.5 px, dark 0.40 → 0.38.

## Palette knife — oil
Oil · 44 px · 18.3 s

![Palette knife — oil](Palette-knife-oil.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 16 % → 16 % | 45.6 px | 0.33 | 1.00 | 27 |
| heavy line | 16 % → 16 % | 46.3 px | 0.36 | 1.00 | 16 |
| pressure swell | 12 % → 12 % | 45.2 px | 0.35 | 1.00 | 14 |
| fast wave | 39 % → 39 % | 44.9 px | 0.31 | 1.00 | 44 |
| slow wave | 39 % → 39 % | 45.4 px | 0.32 | 1.00 | 94 |
| spiral | 62 % → 62 % | 40.9 px | 0.26 | 1.00 | 100 |
| loop | 34 % → 34 % | 43.8 px | 0.33 | 1.00 | 46 |
| tilted | 13 % → 13 % | 36.6 px | 0.35 | 1.00 | 21 |
| over the wet one | 28 % → 28 % | 40.8 px | 0.35 | 1.00 | 17 |
| long, no reload | 74 % → 74 % | 33.1 px | 0.24 | 1.00 | 136 | quarters: 0.00 → 0.00 → 0.00 → 0.00

Numbers say: light vs heavy: width 45.6 → 46.3 px, dark 0.33 → 0.36; pressure barely changes the width.

## 0.45 · Sponge
Watercolor · 46 px · 29.2 s

![0.45 · Sponge](0-45-Sponge.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 23 % → 15 % | 66.4 px | 0.02 | 0.67 | 47 |
| heavy line | 28 % → 23 % | 81.1 px | 0.02 | 0.81 | 69 |
| pressure swell | 20 % → 16 % | 76.7 px | 0.03 | 0.76 | 45 |
| fast wave | 46 % → 32 % | 53.0 px | 0.03 | 0.70 | 142 |
| slow wave | 53 % → 46 % | 60.7 px | 0.04 | 0.87 | 298 |
| spiral | 65 % → 53 % | 42.6 px | 0.04 | 0.82 | 265 |
| loop | 46 % → 40 % | 60.1 px | 0.04 | 0.86 | 142 |
| tilted | 16 % → 17 % | 43.8 px | 0.05 | 1.07 | 97 |
| over the wet one | 40 % → 35 % | 67.3 px | 0.05 | 0.89 | 62 |
| long, no reload | 74 % → 65 % | 33.2 px | 0.04 | 0.88 | 398 | quarters: 0.05 → 0.04 → 0.03 → 0.02

Numbers say: light vs heavy: width 66.4 → 81.1 px, dark 0.02 → 0.02.

## 0.45 · Eraser
Eraser · 30 px · 18.7 s · over bands of wet oil paint and oil pastel in turn (it works on paint already there: look at what it does to the bands; covered counts the bands too)

![0.45 · Eraser](0-45-Eraser.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 24 % → 24 % | 69.2 px | 0.82 | 1.00 | 45 |
| heavy line | 23 % → 23 % | 67.4 px | 0.81 | 1.00 | 41 |
| pressure swell | 23 % → 23 % | 86.7 px | 0.82 | 1.00 | 25 |
| fast wave | 21 % → 21 % | 24.7 px | 0.81 | 1.00 | 120 |
| slow wave | 20 % → 20 % | 23.5 px | 0.82 | 1.00 | 212 |
| spiral | 20 % → 20 % | 13.5 px | 0.79 | 1.00 | 194 |
| loop | 21 % → 21 % | 27.8 px | 0.80 | 1.00 | 110 |
| tilted | 23 % → 23 % | 64.8 px | 0.81 | 1.00 | 61 |
| over the wet one | 22 % → 22 % | 0.0 px | 0.81 | 1.00 | 44 |
| long, no reload | 17 % → 17 % | 7.5 px | 0.79 | 1.00 | 271 | quarters: 0.13 → 0.16 → 0.13 → 0.17

Numbers say: light vs heavy: width 69.2 → 67.4 px, dark 0.82 → 0.81; pressure barely changes the width; the long stroke does not run out of paint.

## Lift wet paint
Eraser · 30 px · 18.3 s · over bands of wet oil paint and oil pastel in turn (it works on paint already there: look at what it does to the bands; covered counts the bands too)

![Lift wet paint](Lift-wet-paint.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 24 % → 24 % | 70.1 px | 0.82 | 1.00 | 28 |
| heavy line | 24 % → 24 % | 69.8 px | 0.82 | 1.00 | 35 |
| pressure swell | 24 % → 24 % | 89.5 px | 0.82 | 1.00 | 29 |
| fast wave | 24 % → 24 % | 27.7 px | 0.82 | 1.00 | 102 |
| slow wave | 24 % → 24 % | 27.7 px | 0.82 | 1.00 | 157 |
| spiral | 24 % → 24 % | 15.9 px | 0.82 | 1.00 | 143 |
| loop | 24 % → 24 % | 31.1 px | 0.82 | 1.00 | 71 |
| tilted | 24 % → 24 % | 66.8 px | 0.82 | 1.00 | 47 |
| over the wet one | 24 % → 24 % | 0.0 px | 0.82 | 1.00 | 41 |
| long, no reload | 24 % → 24 % | 10.7 px | 0.82 | 1.00 | 243 | quarters: 0.18 → 0.24 → 0.17 → 0.24

Numbers say: light vs heavy: width 70.1 → 69.8 px, dark 0.82 → 0.82; pressure barely changes the width; the long stroke does not run out of paint.

## Sgraffito
Eraser · 10 px · 18.5 s · over bands of wet oil paint and oil pastel in turn (it works on paint already there: look at what it does to the bands; covered counts the bands too)

![Sgraffito](Sgraffito.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 24 % → 24 % | 69.5 px | 0.81 | 1.00 | 9 |
| heavy line | 24 % → 24 % | 69.5 px | 0.82 | 1.00 | 5 |
| pressure swell | 24 % → 24 % | 89.5 px | 0.82 | 1.00 | 6 |
| fast wave | 24 % → 24 % | 27.4 px | 0.82 | 1.00 | 22 |
| slow wave | 24 % → 24 % | 27.4 px | 0.81 | 1.00 | 25 |
| spiral | 24 % → 24 % | 15.7 px | 0.81 | 1.00 | 37 |
| loop | 24 % → 24 % | 30.9 px | 0.82 | 1.00 | 16 |
| tilted | 24 % → 24 % | 66.6 px | 0.82 | 1.00 | 4 |
| over the wet one | 24 % → 24 % | 0.0 px | 0.82 | 1.00 | 9 |
| long, no reload | 24 % → 24 % | 10.6 px | 0.82 | 1.00 | 44 | quarters: 0.17 → 0.24 → 0.17 → 0.24

Numbers say: light vs heavy: width 69.5 → 69.5 px, dark 0.81 → 0.82; pressure barely changes the width; the long stroke does not run out of paint.

## Brush Artist · Refs · #01 Henry Ward peach cloud
Gouache · 44 px · 32.6 s

![Brush Artist · Refs · #01 Henry Ward peach cloud](Brush-Artist-Refs-01-Henry-Ward-peach-cloud.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 15 % → 12 % | 42.2 px | 0.32 | 0.80 | 131 |
| heavy line | 16 % → 13 % | 45.5 px | 0.32 | 0.84 | 170 |
| pressure swell | 12 % → 10 % | 44.0 px | 0.32 | 0.87 | 94 |
| fast wave | 37 % → 18 % | 43.1 px | 0.32 | 0.48 | 365 |
| slow wave | 37 % → 18 % | 43.1 px | 0.32 | 0.48 | 638 |
| spiral | 59 % → 19 % | 39.1 px | 0.32 | 0.32 | 634 |
| loop | 32 % → 19 % | 41.3 px | 0.32 | 0.60 | 325 |
| tilted | 13 % → 13 % | 36.7 px | 0.32 | 0.99 | 160 |
| over the wet one | 27 % → 23 % | 38.9 px | 0.32 | 0.85 | 150 |
| long, no reload | 69 % → 20 % | 30.8 px | 0.32 | 0.29 | 842 | quarters: 0.01 → 0.01 → 0.01 → 0.02

Numbers say: light vs heavy: width 42.2 → 45.5 px, dark 0.32 → 0.32; pressure barely changes the width; the long stroke does not run out of paint.

## Brush Artist · Refs · #02 Henry Ward cream strokes
Gouache · 46 px · 31.2 s

![Brush Artist · Refs · #02 Henry Ward cream strokes](Brush-Artist-Refs-02-Henry-Ward-cream-strokes.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 14 % → 13 % | 40.8 px | 0.41 | 0.90 | 129 |
| heavy line | 15 % → 14 % | 43.9 px | 0.41 | 0.92 | 136 |
| pressure swell | 11 % → 11 % | 42.8 px | 0.41 | 0.94 | 109 |
| fast wave | 36 % → 18 % | 41.0 px | 0.40 | 0.50 | 425 |
| slow wave | 36 % → 18 % | 41.1 px | 0.40 | 0.49 | 627 |
| spiral | 58 % → 19 % | 38.1 px | 0.40 | 0.33 | 655 |
| loop | 31 % → 20 % | 39.7 px | 0.40 | 0.64 | 325 |
| tilted | 13 % → 13 % | 36.9 px | 0.41 | 0.99 | 168 |
| over the wet one | 27 % → 23 % | 37.9 px | 0.41 | 0.86 | 159 |
| long, no reload | 67 % → 21 % | 30.1 px | 0.40 | 0.31 | 947 | quarters: 0.01 → 0.01 → 0.01 → 0.02

Numbers say: light vs heavy: width 40.8 → 43.9 px, dark 0.41 → 0.41; pressure barely changes the width; the long stroke does not run out of paint.

## Brush Artist · Refs · #03 Henry Ward navy contours
Heavy acrylic · 22 px · 13.4 s

![Brush Artist · Refs · #03 Henry Ward navy contours](Brush-Artist-Refs-03-Henry-Ward-navy-contours.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 7 % → 7 % | 21.5 px | 0.70 | 0.94 | 65 |
| heavy line | 8 % → 8 % | 23.4 px | 0.70 | 0.95 | 78 |
| pressure swell | 6 % → 6 % | 23.2 px | 0.73 | 0.94 | 55 |
| fast wave | 19 % → 12 % | 21.8 px | 0.72 | 0.66 | 181 |
| slow wave | 19 % → 13 % | 22.4 px | 0.72 | 0.69 | 264 |
| spiral | 30 % → 13 % | 19.5 px | 0.72 | 0.45 | 303 |
| loop | 17 % → 13 % | 21.4 px | 0.72 | 0.81 | 153 |
| tilted | 8 % → 8 % | 22.6 px | 0.71 | 1.00 | 83 |
| over the wet one | 16 % → 14 % | 21.2 px | 0.71 | 0.89 | 69 |
| long, no reload | 34 % → 14 % | 15.1 px | 0.72 | 0.40 | 407 | quarters: 0.35 → 0.29 → 0.20 → 0.08

Numbers say: light vs heavy: width 21.5 → 23.4 px, dark 0.70 → 0.70; pressure barely changes the width.

## Brush Artist · Refs · #04 Henry Ward grey cloud
Gouache · 50 px · 31.4 s

![Brush Artist · Refs · #04 Henry Ward grey cloud](Brush-Artist-Refs-04-Henry-Ward-grey-cloud.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 16 % → 14 % | 46.7 px | 0.31 | 0.85 | 155 |
| heavy line | 17 % → 15 % | 50.2 px | 0.31 | 0.89 | 158 |
| pressure swell | 13 % → 12 % | 48.7 px | 0.31 | 0.91 | 108 |
| fast wave | 40 % → 20 % | 46.5 px | 0.31 | 0.50 | 384 |
| slow wave | 40 % → 20 % | 46.5 px | 0.31 | 0.49 | 655 |
| spiral | 61 % → 21 % | 40.0 px | 0.31 | 0.34 | 708 |
| loop | 35 % → 22 % | 45.2 px | 0.31 | 0.64 | 344 |
| tilted | 14 % → 14 % | 40.0 px | 0.31 | 0.99 | 186 |
| over the wet one | 30 % → 26 % | 42.8 px | 0.31 | 0.87 | 157 |
| long, no reload | 73 % → 23 % | 32.7 px | 0.31 | 0.31 | 963 | quarters: 0.01 → 0.01 → 0.01 → 0.02

Numbers say: light vs heavy: width 46.7 → 50.2 px, dark 0.31 → 0.31; pressure barely changes the width; the long stroke does not run out of paint.

## Brush Artist · Refs · #05 Henry Ward green in rust loops
Heavy acrylic · 20 px · 12.7 s

![Brush Artist · Refs · #05 Henry Ward green in rust loops](Brush-Artist-Refs-05-Henry-Ward-green-in-rust-loops.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 7 % → 6 % | 19.5 px | 0.55 | 0.94 | 72 |
| heavy line | 7 % → 7 % | 21.2 px | 0.55 | 0.94 | 63 |
| pressure swell | 6 % → 5 % | 21.5 px | 0.57 | 0.92 | 57 |
| fast wave | 17 % → 11 % | 19.7 px | 0.56 | 0.64 | 177 |
| slow wave | 18 % → 12 % | 20.3 px | 0.56 | 0.66 | 309 |
| spiral | 27 % → 12 % | 17.9 px | 0.55 | 0.42 | 345 |
| loop | 15 % → 12 % | 19.5 px | 0.55 | 0.80 | 166 |
| tilted | 8 % → 8 % | 21.7 px | 0.56 | 1.00 | 72 |
| over the wet one | 15 % → 13 % | 19.1 px | 0.56 | 0.87 | 65 |
| long, no reload | 30 % → 12 % | 13.4 px | 0.56 | 0.39 | 399 | quarters: 0.25 → 0.18 → 0.10 → 0.02

Numbers say: light vs heavy: width 19.5 → 21.2 px, dark 0.55 → 0.55; pressure barely changes the width.

## Brush Artist · Refs · #06 Henry Ward scrubbed grey
Gouache · 50 px · 31.7 s

![Brush Artist · Refs · #06 Henry Ward scrubbed grey](Brush-Artist-Refs-06-Henry-Ward-scrubbed-grey.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 16 % → 14 % | 46.7 px | 0.33 | 0.85 | 143 |
| heavy line | 17 % → 15 % | 50.2 px | 0.33 | 0.89 | 189 |
| pressure swell | 13 % → 12 % | 48.7 px | 0.33 | 0.91 | 105 |
| fast wave | 40 % → 20 % | 46.5 px | 0.33 | 0.50 | 396 |
| slow wave | 40 % → 20 % | 46.5 px | 0.33 | 0.49 | 657 |
| spiral | 61 % → 21 % | 40.0 px | 0.33 | 0.34 | 675 |
| loop | 35 % → 22 % | 45.2 px | 0.32 | 0.64 | 357 |
| tilted | 14 % → 14 % | 40.0 px | 0.33 | 0.99 | 183 |
| over the wet one | 30 % → 26 % | 42.8 px | 0.33 | 0.87 | 174 |
| long, no reload | 73 % → 23 % | 32.7 px | 0.32 | 0.31 | 992 | quarters: 0.01 → 0.01 → 0.01 → 0.02

Numbers say: light vs heavy: width 46.7 → 50.2 px, dark 0.33 → 0.33; pressure barely changes the width; the long stroke does not run out of paint.

## Brush Artist · Refs · #07 Henry Ward blue L + black zigzag
Heavy acrylic · 34 px · 15.2 s

![Brush Artist · Refs · #07 Henry Ward blue L + black zigzag](Brush-Artist-Refs-07-Henry-Ward-blue-L-black-zigzag.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 11 % → 11 % | 33.1 px | 0.57 | 0.93 | 102 |
| heavy line | 12 % → 11 % | 35.7 px | 0.57 | 0.93 | 88 |
| pressure swell | 9 % → 9 % | 35.2 px | 0.59 | 0.94 | 67 |
| fast wave | 29 % → 20 % | 33.6 px | 0.59 | 0.69 | 252 |
| slow wave | 30 % → 21 % | 34.1 px | 0.58 | 0.73 | 409 |
| spiral | 47 % → 22 % | 31.3 px | 0.58 | 0.46 | 426 |
| loop | 25 % → 21 % | 32.7 px | 0.58 | 0.82 | 215 |
| tilted | 11 % → 11 % | 29.8 px | 0.58 | 1.00 | 116 |
| over the wet one | 22 % → 20 % | 31.7 px | 0.58 | 0.91 | 98 |
| long, no reload | 53 % → 22 % | 23.8 px | 0.59 | 0.42 | 544 | quarters: 0.40 → 0.32 → 0.21 → 0.10

Numbers say: light vs heavy: width 33.1 → 35.7 px, dark 0.57 → 0.57; pressure barely changes the width.

## Brush Artist · Refs · #08 Henry Ward olive bands
Gouache · 34 px · 22.8 s

![Brush Artist · Refs · #08 Henry Ward olive bands](Brush-Artist-Refs-08-Henry-Ward-olive-bands.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 8 % → 2 % | 24.7 px | 0.57 | 0.27 | 83 |
| heavy line | 12 % → 3 % | 33.9 px | 0.57 | 0.22 | 136 |
| pressure swell | 8 % → 3 % | 30.8 px | 0.57 | 0.38 | 76 |
| fast wave | 25 % → 4 % | 29.2 px | 0.57 | 0.15 | 256 |
| slow wave | 25 % → 4 % | 28.9 px | 0.57 | 0.15 | 390 |
| spiral | 39 % → 4 % | 25.7 px | 0.57 | 0.10 | 415 |
| loop | 22 % → 5 % | 28.8 px | 0.57 | 0.21 | 224 |
| tilted | 10 % → 10 % | 28.6 px | 0.57 | 0.98 | 114 |
| over the wet one | 20 % → 8 % | 28.3 px | 0.57 | 0.40 | 101 |
| long, no reload | 45 % → 6 % | 20.0 px | 0.57 | 0.13 | 622 | quarters: 0.35 → 0.27 → 0.17 → 0.08

Numbers say: light vs heavy: width 24.7 → 33.9 px, dark 0.57 → 0.57.

## Brush Artist · Refs · #09 Henry Ward white loops
Gouache · 46 px · 31.4 s

![Brush Artist · Refs · #09 Henry Ward white loops](Brush-Artist-Refs-09-Henry-Ward-white-loops.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 14 % → 13 % | 40.8 px | 0.43 | 0.90 | 130 |
| heavy line | 15 % → 14 % | 43.9 px | 0.43 | 0.92 | 143 |
| pressure swell | 11 % → 11 % | 42.8 px | 0.44 | 0.94 | 111 |
| fast wave | 36 % → 18 % | 41.0 px | 0.43 | 0.50 | 350 |
| slow wave | 36 % → 18 % | 41.1 px | 0.43 | 0.49 | 633 |
| spiral | 58 % → 19 % | 38.1 px | 0.42 | 0.33 | 615 |
| loop | 31 % → 20 % | 39.7 px | 0.42 | 0.64 | 314 |
| tilted | 13 % → 13 % | 36.9 px | 0.43 | 0.99 | 174 |
| over the wet one | 27 % → 23 % | 37.9 px | 0.43 | 0.86 | 168 |
| long, no reload | 67 % → 21 % | 30.1 px | 0.42 | 0.31 | 873 | quarters: 0.01 → 0.01 → 0.01 → 0.02

Numbers say: light vs heavy: width 40.8 → 43.9 px, dark 0.43 → 0.43; pressure barely changes the width; the long stroke does not run out of paint.

## Brush Artist · Refs · #10 Henry Ward maroon loops
Heavy acrylic · 30 px · 14.0 s

![Brush Artist · Refs · #10 Henry Ward maroon loops](Brush-Artist-Refs-10-Henry-Ward-maroon-loops.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 10 % → 9 % | 28.0 px | 0.70 | 0.94 | 74 |
| heavy line | 10 % → 10 % | 30.2 px | 0.69 | 0.95 | 82 |
| pressure swell | 8 % → 8 % | 30.0 px | 0.73 | 0.94 | 57 |
| fast wave | 24 % → 17 % | 28.3 px | 0.73 | 0.71 | 200 |
| slow wave | 25 % → 18 % | 29.0 px | 0.73 | 0.73 | 354 |
| spiral | 39 % → 18 % | 26.0 px | 0.72 | 0.47 | 358 |
| loop | 21 % → 18 % | 27.6 px | 0.72 | 0.85 | 212 |
| tilted | 10 % → 10 % | 27.9 px | 0.72 | 1.00 | 110 |
| over the wet one | 20 % → 18 % | 26.8 px | 0.72 | 0.91 | 85 |
| long, no reload | 46 % → 18 % | 20.6 px | 0.73 | 0.40 | 511 | quarters: 0.44 → 0.38 → 0.31 → 0.22

Numbers say: light vs heavy: width 28.0 → 30.2 px, dark 0.70 → 0.69; pressure barely changes the width.

## Brush Artist · Refs · #11 Henry Ward purple spun balls
Heavy acrylic · 36 px · 15.3 s

![Brush Artist · Refs · #11 Henry Ward purple spun balls](Brush-Artist-Refs-11-Henry-Ward-purple-spun-balls.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 12 % → 11 % | 34.1 px | 0.70 | 0.96 | 94 |
| heavy line | 13 % → 12 % | 36.6 px | 0.70 | 0.96 | 102 |
| pressure swell | 10 % → 9 % | 36.2 px | 0.74 | 0.95 | 75 |
| fast wave | 30 % → 23 % | 34.6 px | 0.73 | 0.75 | 243 |
| slow wave | 30 % → 24 % | 35.0 px | 0.73 | 0.79 | 449 |
| spiral | 49 % → 25 % | 32.3 px | 0.73 | 0.50 | 427 |
| loop | 26 % → 23 % | 33.4 px | 0.73 | 0.88 | 238 |
| tilted | 11 % → 11 % | 31.2 px | 0.72 | 1.00 | 128 |
| over the wet one | 23 % → 21 % | 32.1 px | 0.72 | 0.93 | 107 |
| long, no reload | 55 % → 24 % | 24.8 px | 0.73 | 0.44 | 628 | quarters: 0.51 → 0.46 → 0.39 → 0.28

Numbers say: light vs heavy: width 34.1 → 36.6 px, dark 0.70 → 0.70; pressure barely changes the width.

## Brush Artist · Refs · #12 Henry Ward black-olive cage
Gouache · 28 px · 21.7 s

![Brush Artist · Refs · #12 Henry Ward black-olive cage](Brush-Artist-Refs-12-Henry-Ward-black-olive-cage.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 7 % → 3 % | 20.9 px | 0.61 | 0.35 | 56 |
| heavy line | 9 % → 4 % | 26.1 px | 0.61 | 0.41 | 110 |
| pressure swell | 6 % → 4 % | 23.9 px | 0.61 | 0.61 | 72 |
| fast wave | 20 % → 4 % | 23.7 px | 0.61 | 0.19 | 214 |
| slow wave | 20 % → 4 % | 23.3 px | 0.61 | 0.21 | 324 |
| spiral | 32 % → 4 % | 21.4 px | 0.61 | 0.14 | 324 |
| loop | 18 % → 5 % | 22.8 px | 0.61 | 0.28 | 164 |
| tilted | 9 % → 9 % | 25.4 px | 0.61 | 0.98 | 88 |
| over the wet one | 17 % → 8 % | 21.8 px | 0.61 | 0.46 | 85 |
| long, no reload | 39 % → 6 % | 17.6 px | 0.61 | 0.15 | 510 | quarters: 0.31 → 0.26 → 0.19 → 0.10

Numbers say: light vs heavy: width 20.9 → 26.1 px, dark 0.61 → 0.61.

## Brush Artist · Refs · #13 Henry Ward blue streaky form
Gouache · 50 px · 31.5 s

![Brush Artist · Refs · #13 Henry Ward blue streaky form](Brush-Artist-Refs-13-Henry-Ward-blue-streaky-form.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 16 % → 14 % | 46.7 px | 0.33 | 0.85 | 143 |
| heavy line | 17 % → 15 % | 50.2 px | 0.33 | 0.89 | 158 |
| pressure swell | 13 % → 12 % | 48.7 px | 0.33 | 0.91 | 101 |
| fast wave | 40 % → 20 % | 46.5 px | 0.33 | 0.50 | 402 |
| slow wave | 40 % → 20 % | 46.5 px | 0.33 | 0.49 | 683 |
| spiral | 61 % → 21 % | 40.0 px | 0.32 | 0.34 | 651 |
| loop | 35 % → 22 % | 45.2 px | 0.32 | 0.64 | 350 |
| tilted | 14 % → 14 % | 40.0 px | 0.33 | 0.99 | 185 |
| over the wet one | 30 % → 26 % | 42.8 px | 0.33 | 0.87 | 158 |
| long, no reload | 73 % → 23 % | 32.7 px | 0.32 | 0.31 | 961 | quarters: 0.01 → 0.01 → 0.01 → 0.02

Numbers say: light vs heavy: width 46.7 → 50.2 px, dark 0.33 → 0.33; pressure barely changes the width; the long stroke does not run out of paint.

## Brush Artist · Refs · #14 Henry Ward olive totem
Heavy acrylic · 48 px · 17.8 s

![Brush Artist · Refs · #14 Henry Ward olive totem](Brush-Artist-Refs-14-Henry-Ward-olive-totem.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 15 % → 15 % | 44.8 px | 0.31 | 0.94 | 130 |
| heavy line | 16 % → 16 % | 47.7 px | 0.31 | 0.95 | 145 |
| pressure swell | 13 % → 12 % | 47.0 px | 0.32 | 0.95 | 102 |
| fast wave | 38 % → 30 % | 43.9 px | 0.30 | 0.79 | 347 |
| slow wave | 39 % → 31 % | 44.5 px | 0.30 | 0.81 | 577 |
| spiral | 58 % → 32 % | 38.1 px | 0.30 | 0.55 | 615 |
| loop | 33 % → 29 % | 42.6 px | 0.30 | 0.89 | 320 |
| tilted | 13 % → 13 % | 37.5 px | 0.31 | 1.00 | 182 |
| over the wet one | 28 % → 26 % | 41.1 px | 0.31 | 0.93 | 156 |
| long, no reload | 67 % → 33 % | 30.3 px | 0.30 | 0.49 | 862 | quarters: 0.25 → 0.18 → 0.10 → 0.03

Numbers say: light vs heavy: width 44.8 → 47.7 px, dark 0.31 → 0.31; pressure barely changes the width.

## Brush Artist · Refs · #15 Ultramarine brush script
Ink · 6 px · 21.1 s

![Brush Artist · Refs · #15 Ultramarine brush script](Brush-Artist-Refs-15-Ultramarine-brush-script.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 1 % → 4 % | 2.8 px | 0.53 | 3.61 | 28 |
| heavy line | 7 % → 7 % | 21.0 px | 0.61 | 0.99 | 55 |
| pressure swell | 4 % → 5 % | 15.1 px | 0.66 | 1.16 | 33 |
| fast wave | 12 % → 10 % | 14.2 px | 0.55 | 0.82 | 100 |
| slow wave | 10 % → 9 % | 11.5 px | 0.54 | 0.93 | 97 |
| spiral | 15 % → 10 % | 9.9 px | 0.52 | 0.66 | 156 |
| loop | 9 % → 9 % | 12.2 px | 0.54 | 0.99 | 88 |
| tilted | 3 % → 3 % | 9.2 px | 0.64 | 1.05 | 39 |
| over the wet one | 9 % → 9 % | 15.0 px | 0.64 | 1.07 | 42 |
| long, no reload | 22 % → 10 % | 9.8 px | 0.51 | 0.47 | 251 | quarters: 0.19 → 0.06 → 0.02 → 0.00

Numbers say: light vs heavy: width 2.8 → 21.0 px, dark 0.53 → 0.61; wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #18 Blue oil-stick scribbles
Pastel · 10 px · 9.0 s

![Brush Artist · Refs · #18 Blue oil-stick scribbles](Brush-Artist-Refs-18-Blue-oil-stick-scribbles.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 1 % → 1 % | 2.9 px | 0.52 | 1.00 | 11 |
| heavy line | 2 % → 2 % | 5.5 px | 0.53 | 1.00 | 23 |
| pressure swell | 1 % → 1 % | 5.0 px | 0.53 | 1.00 | 15 |
| fast wave | 4 % → 4 % | 4.8 px | 0.53 | 1.00 | 62 |
| slow wave | 4 % → 4 % | 4.4 px | 0.53 | 1.00 | 53 |
| spiral | 7 % → 7 % | 4.5 px | 0.52 | 1.00 | 87 |
| loop | 3 % → 3 % | 4.5 px | 0.52 | 1.00 | 45 |
| tilted | 2 % → 2 % | 4.7 px | 0.53 | 1.00 | 24 |
| over the wet one | 3 % → 3 % | 4.7 px | 0.53 | 1.00 | 20 |
| long, no reload | 10 % → 10 % | 4.4 px | 0.53 | 1.00 | 127 | quarters: 0.06 → 0.06 → 0.06 → 0.06

Numbers say: light vs heavy: width 2.9 → 5.5 px, dark 0.52 → 0.53; the long stroke does not run out of paint.

## Brush Artist · Refs · #20 Orange-red crayon scribble
Pastel · 14 px · 9.2 s

![Brush Artist · Refs · #20 Orange-red crayon scribble](Brush-Artist-Refs-20-Orange-red-crayon-scribble.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 1 % → 1 % | 4.0 px | 0.53 | 1.00 | 18 |
| heavy line | 3 % → 3 % | 8.0 px | 0.53 | 1.00 | 21 |
| pressure swell | 2 % → 2 % | 7.6 px | 0.53 | 1.00 | 14 |
| fast wave | 6 % → 6 % | 7.2 px | 0.53 | 1.00 | 52 |
| slow wave | 6 % → 6 % | 6.6 px | 0.53 | 1.00 | 62 |
| spiral | 9 % → 9 % | 6.2 px | 0.53 | 1.00 | 95 |
| loop | 5 % → 5 % | 6.2 px | 0.53 | 1.00 | 50 |
| tilted | 2 % → 2 % | 5.6 px | 0.53 | 1.00 | 40 |
| over the wet one | 4 % → 4 % | 6.6 px | 0.53 | 1.00 | 23 |
| long, no reload | 13 % → 13 % | 5.7 px | 0.53 | 1.00 | 132 | quarters: 0.07 → 0.07 → 0.08 → 0.08

Numbers say: light vs heavy: width 4.0 → 8.0 px, dark 0.53 → 0.53; the long stroke does not run out of paint.

## Brush Artist · Refs · #21 Gritty black contours
Gouache · 12 px · 18.9 s

![Brush Artist · Refs · #21 Gritty black contours](Brush-Artist-Refs-21-Gritty-black-contours.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 3 % → 0 % | 8.8 px | 0.79 | 0.12 | 46 |
| heavy line | 4 % → 0 % | 11.9 px | 0.79 | 0.10 | 93 |
| pressure swell | 3 % → 0 % | 11.6 px | 0.79 | 0.15 | 61 |
| fast wave | 7 % → 1 % | 8.5 px | 0.79 | 0.10 | 178 |
| slow wave | 8 % → 1 % | 9.0 px | 0.79 | 0.09 | 178 |
| spiral | 9 % → 1 % | 6.0 px | 0.79 | 0.10 | 309 |
| loop | 8 % → 1 % | 9.9 px | 0.79 | 0.09 | 154 |
| tilted | 4 % → 4 % | 10.8 px | 0.79 | 0.90 | 92 |
| over the wet one | 7 % → 1 % | 9.7 px | 0.79 | 0.17 | 87 |
| long, no reload | 7 % → 1 % | 3.3 px | 0.79 | 0.12 | 427 | quarters: 0.20 → 0.07 → 0.00 → 0.00

Numbers say: light vs heavy: width 8.8 → 11.9 px, dark 0.79 → 0.79.

## Brush Artist · Refs · #22 Bold black brush poster
Ink · 20 px · 24.9 s

![Brush Artist · Refs · #22 Bold black brush poster](Brush-Artist-Refs-22-Bold-black-brush-poster.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 3 % → 5 % | 9.5 px | 0.79 | 1.63 | 29 |
| heavy line | 15 % → 15 % | 44.6 px | 0.88 | 0.99 | 80 |
| pressure swell | 9 % → 9 % | 31.9 px | 0.87 | 1.04 | 43 |
| fast wave | 27 % → 26 % | 31.2 px | 0.87 | 0.98 | 142 |
| slow wave | 22 % → 21 % | 25.2 px | 0.87 | 0.98 | 191 |
| spiral | 34 % → 32 % | 22.2 px | 0.87 | 0.94 | 241 |
| loop | 20 % → 20 % | 26.2 px | 0.88 | 1.00 | 121 |
| tilted | 8 % → 8 % | 22.7 px | 0.88 | 1.01 | 59 |
| over the wet one | 19 % → 19 % | 30.5 px | 0.88 | 1.00 | 53 |
| long, no reload | 45 % → 38 % | 20.2 px | 0.86 | 0.84 | 359 | quarters: 0.54 → 0.45 → 0.35 → 0.27

Numbers say: light vs heavy: width 9.5 → 44.6 px, dark 0.79 → 0.88; wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #23 Dry white on orange + black line
Gouache · 50 px · 23.4 s

![Brush Artist · Refs · #23 Dry white on orange + black line](Brush-Artist-Refs-23-Dry-white-on-orange-black-line.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 12 % → 2 % | 35.1 px | 0.39 | 0.13 | 82 |
| heavy line | 16 % → 2 % | 46.9 px | 0.39 | 0.11 | 226 |
| pressure swell | 11 % → 2 % | 42.6 px | 0.39 | 0.19 | 111 |
| fast wave | 34 % → 3 % | 39.7 px | 0.39 | 0.09 | 374 |
| slow wave | 34 % → 3 % | 39.0 px | 0.39 | 0.10 | 579 |
| spiral | 49 % → 4 % | 32.6 px | 0.38 | 0.07 | 593 |
| loop | 30 % → 4 % | 39.1 px | 0.38 | 0.12 | 319 |
| tilted | 13 % → 12 % | 34.9 px | 0.38 | 0.98 | 178 |
| over the wet one | 26 % → 7 % | 38.0 px | 0.38 | 0.27 | 150 |
| long, no reload | 58 % → 5 % | 26.1 px | 0.38 | 0.09 | 927 | quarters: 0.02 → 0.02 → 0.03 → 0.04

Numbers say: light vs heavy: width 35.1 → 46.9 px, dark 0.39 → 0.39; the long stroke does not run out of paint.

## Brush Artist · Refs · #24 Picasso flat oil
Oil · 34 px · 18.2 s

![Brush Artist · Refs · #24 Picasso flat oil](Brush-Artist-Refs-24-Picasso-flat-oil.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 11 % → 11 % | 32.2 px | 0.39 | 1.00 | 106 |
| heavy line | 12 % → 12 % | 35.0 px | 0.39 | 1.00 | 120 |
| pressure swell | 9 % → 9 % | 34.4 px | 0.41 | 1.00 | 81 |
| fast wave | 30 % → 30 % | 34.2 px | 0.41 | 1.00 | 274 |
| slow wave | 30 % → 30 % | 34.9 px | 0.41 | 1.00 | 523 |
| spiral | 51 % → 51 % | 33.7 px | 0.40 | 1.00 | 499 |
| loop | 25 % → 25 % | 32.6 px | 0.41 | 1.00 | 255 |
| tilted | 11 % → 11 % | 32.0 px | 0.41 | 1.00 | 128 |
| over the wet one | 22 % → 22 % | 30.7 px | 0.41 | 1.00 | 118 |
| long, no reload | 61 % → 61 % | 27.6 px | 0.39 | 1.00 | 702 | quarters: 0.28 → 0.28 → 0.26 → 0.24

Numbers say: light vs heavy: width 32.2 → 35.0 px, dark 0.39 → 0.39; pressure barely changes the width.

## Brush Artist · Refs · #25 Yellow heavy flat stroke
Heavy acrylic · 110 px · 31.9 s

![Brush Artist · Refs · #25 Yellow heavy flat stroke](Brush-Artist-Refs-25-Yellow-heavy-flat-stroke.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 35 % → 36 % | 101.3 px | 0.30 | 1.02 | 346 |
| heavy line | 36 % → 35 % | 105.0 px | 0.30 | 0.97 | 401 |
| pressure swell | 28 % → 29 % | 105.4 px | 0.30 | 1.04 | 259 |
| fast wave | 72 % → 76 % | 83.8 px | 0.30 | 1.05 | 947 |
| slow wave | 73 % → 72 % | 84.7 px | 0.29 | 0.98 | 1686 |
| spiral | 86 % → 83 % | 56.7 px | 0.28 | 0.97 | 1746 |
| loop | 65 % → 64 % | 83.6 px | 0.30 | 0.99 | 867 |
| tilted | 26 % → 26 % | 71.5 px | 0.30 | 1.00 | 485 |
| over the wet one | 55 % → 54 % | 83.1 px | 0.30 | 0.97 | 397 |
| long, no reload | 98 % → 97 % | 44.1 px | 0.29 | 0.99 | 2374 | quarters: 0.00 → 0.00 → 0.00 → 0.00

Numbers say: light vs heavy: width 101.3 → 105.0 px, dark 0.30 → 0.30; pressure barely changes the width; the long stroke does not run out of paint.

## Brush Artist · Refs · #27 Orange impasto swatch
Heavy acrylic · 60 px · 24.1 s

![Brush Artist · Refs · #27 Orange impasto swatch](Brush-Artist-Refs-27-Orange-impasto-swatch.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 20 % → 19 % | 56.7 px | 0.35 | 0.97 | 170 |
| heavy line | 20 % → 20 % | 59.3 px | 0.35 | 0.97 | 194 |
| pressure swell | 16 % → 15 % | 59.6 px | 0.36 | 0.97 | 116 |
| fast wave | 48 % → 46 % | 55.0 px | 0.35 | 0.98 | 428 |
| slow wave | 48 % → 47 % | 55.8 px | 0.36 | 0.98 | 756 |
| spiral | 69 % → 62 % | 45.5 px | 0.35 | 0.91 | 738 |
| loop | 42 % → 40 % | 53.8 px | 0.35 | 0.97 | 375 |
| tilted | 16 % → 16 % | 44.0 px | 0.36 | 1.00 | 211 |
| over the wet one | 34 % → 33 % | 50.6 px | 0.36 | 0.97 | 184 |
| long, no reload | 85 % → 75 % | 38.1 px | 0.35 | 0.88 | 1070 | quarters: 0.33 → 0.31 → 0.29 → 0.26

Numbers say: light vs heavy: width 56.7 → 59.3 px, dark 0.35 → 0.35; pressure barely changes the width.

## Brush Artist · Refs · #28 Miles Davis black lines
Ink · 22 px · 26.1 s

![Brush Artist · Refs · #28 Miles Davis black lines](Brush-Artist-Refs-28-Miles-Davis-black-lines.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 4 % → 6 % | 12.2 px | 0.81 | 1.48 | 35 |
| heavy line | 17 % → 17 % | 49.1 px | 0.88 | 0.99 | 84 |
| pressure swell | 10 % → 10 % | 35.9 px | 0.87 | 1.03 | 54 |
| fast wave | 30 % → 30 % | 35.0 px | 0.87 | 0.98 | 134 |
| slow wave | 25 % → 25 % | 28.5 px | 0.87 | 0.99 | 271 |
| spiral | 38 % → 37 % | 25.3 px | 0.87 | 0.96 | 220 |
| loop | 23 % → 23 % | 29.4 px | 0.88 | 1.00 | 123 |
| tilted | 9 % → 9 % | 25.0 px | 0.88 | 1.01 | 48 |
| over the wet one | 21 % → 21 % | 34.1 px | 0.88 | 1.00 | 51 |
| long, no reload | 51 % → 43 % | 22.7 px | 0.86 | 0.85 | 329 | quarters: 0.59 → 0.51 → 0.40 → 0.31

Numbers say: light vs heavy: width 12.2 → 49.1 px, dark 0.81 → 0.88.

## Brush Artist · Refs · #29 Shrigley magenta asterisk
Watercolor · 70 px · 29.1 s

![Brush Artist · Refs · #29 Shrigley magenta asterisk](Brush-Artist-Refs-29-Shrigley-magenta-asterisk.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 10 % → 13 % | 28.0 px | 0.65 | 1.36 | 62 |
| heavy line | 17 % → 18 % | 50.3 px | 0.64 | 1.03 | 118 |
| pressure swell | 11 % → 12 % | 41.1 px | 0.65 | 1.13 | 76 |
| fast wave | 38 % → 38 % | 43.7 px | 0.64 | 1.00 | 253 |
| slow wave | 35 % → 39 % | 41.0 px | 0.65 | 1.10 | 414 |
| spiral | 61 % → 61 % | 40.0 px | 0.64 | 1.01 | 379 |
| loop | 31 % → 32 % | 40.2 px | 0.65 | 1.03 | 217 |
| tilted | 18 % → 18 % | 49.0 px | 0.65 | 1.00 | 188 |
| over the wet one | 31 % → 34 % | 38.4 px | 0.65 | 1.07 | 100 |
| long, no reload | 75 % → 75 % | 33.5 px | 0.64 | 1.00 | 614 | quarters: 0.55 → 0.53 → 0.52 → 0.49

Numbers say: light vs heavy: width 28.0 → 50.3 px, dark 0.65 → 0.64; the long stroke does not run out of paint.

## Brush Artist · Refs · #30 Red gouache face patch
Gouache · 60 px · 34.3 s

![Brush Artist · Refs · #30 Red gouache face patch](Brush-Artist-Refs-30-Red-gouache-face-patch.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 16 % → 15 % | 46.9 px | 0.49 | 0.91 | 158 |
| heavy line | 25 % → 20 % | 73.8 px | 0.49 | 0.80 | 216 |
| pressure swell | 19 % → 17 % | 72.6 px | 0.49 | 0.86 | 134 |
| fast wave | 48 % → 28 % | 55.1 px | 0.49 | 0.58 | 387 |
| slow wave | 48 % → 28 % | 55.3 px | 0.49 | 0.59 | 659 |
| spiral | 59 % → 28 % | 39.1 px | 0.49 | 0.48 | 643 |
| loop | 40 % → 29 % | 51.3 px | 0.49 | 0.74 | 332 |
| tilted | 16 % → 16 % | 45.7 px | 0.49 | 1.01 | 215 |
| over the wet one | 36 % → 32 % | 55.3 px | 0.49 | 0.88 | 165 |
| long, no reload | 67 % → 30 % | 30.0 px | 0.49 | 0.45 | 946 | quarters: 0.43 → 0.38 → 0.32 → 0.26

Numbers say: light vs heavy: width 46.9 → 73.8 px, dark 0.49 → 0.49.

## Brush Artist · Refs · #31 Warhol blotted line
Ink · 6 px · 20.0 s

![Brush Artist · Refs · #31 Warhol blotted line](Brush-Artist-Refs-31-Warhol-blotted-line.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 1 % → 3 % | 2.6 px | 0.75 | 3.30 | 25 |
| heavy line | 7 % → 7 % | 20.6 px | 0.83 | 0.97 | 53 |
| pressure swell | 4 % → 4 % | 14.8 px | 0.84 | 1.12 | 30 |
| fast wave | 12 % → 9 % | 13.8 px | 0.82 | 0.77 | 90 |
| slow wave | 10 % → 8 % | 11.2 px | 0.80 | 0.85 | 96 |
| spiral | 15 % → 9 % | 9.7 px | 0.80 | 0.58 | 153 |
| loop | 9 % → 9 % | 11.9 px | 0.80 | 0.94 | 93 |
| tilted | 3 % → 3 % | 8.6 px | 0.84 | 1.04 | 33 |
| over the wet one | 8 % → 8 % | 14.5 px | 0.84 | 1.02 | 38 |
| long, no reload | 21 % → 9 % | 9.6 px | 0.78 | 0.43 | 237 | quarters: 0.25 → 0.13 → 0.05 → 0.01

Numbers say: light vs heavy: width 2.6 → 20.6 px, dark 0.75 → 0.83; wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #32 Thick orange swipes
Heavy acrylic · 90 px · 28.1 s

![Brush Artist · Refs · #32 Thick orange swipes](Brush-Artist-Refs-32-Thick-orange-swipes.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 29 % → 29 % | 82.9 px | 0.38 | 1.00 | 258 |
| heavy line | 30 % → 29 % | 86.3 px | 0.38 | 0.97 | 280 |
| pressure swell | 23 % → 23 % | 86.5 px | 0.38 | 1.01 | 223 |
| fast wave | 63 % → 65 % | 73.1 px | 0.38 | 1.03 | 827 |
| slow wave | 64 % → 63 % | 73.5 px | 0.39 | 0.98 | 1253 |
| spiral | 79 % → 77 % | 52.2 px | 0.38 | 0.98 | 1223 |
| loop | 57 % → 56 % | 73.4 px | 0.38 | 0.99 | 633 |
| tilted | 21 % → 21 % | 59.3 px | 0.38 | 1.00 | 329 |
| over the wet one | 47 % → 45 % | 70.7 px | 0.38 | 0.97 | 280 |
| long, no reload | 95 % → 93 % | 42.7 px | 0.38 | 0.98 | 1783 | quarters: 0.38 → 0.38 → 0.37 → 0.35

Numbers say: light vs heavy: width 82.9 → 86.3 px, dark 0.38 → 0.38; pressure barely changes the width; the long stroke does not run out of paint.

## Brush Artist · Refs · #33 Red wet-in-wet band
Watercolor · 80 px · 34.0 s

![Brush Artist · Refs · #33 Red wet-in-wet band](Brush-Artist-Refs-33-Red-wet-in-wet-band.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 19 % → 19 % | 55.6 px | 0.66 | 1.02 | 96 |
| heavy line | 29 % → 28 % | 83.7 px | 0.65 | 0.96 | 193 |
| pressure swell | 19 % → 19 % | 71.5 px | 0.68 | 1.01 | 114 |
| fast wave | 58 % → 58 % | 67.4 px | 0.66 | 0.99 | 376 |
| slow wave | 57 % → 56 % | 65.5 px | 0.68 | 1.00 | 638 |
| spiral | 75 % → 74 % | 49.5 px | 0.67 | 0.98 | 612 |
| loop | 51 % → 50 % | 66.3 px | 0.67 | 0.98 | 305 |
| tilted | 24 % → 24 % | 66.1 px | 0.66 | 1.00 | 243 |
| over the wet one | 47 % → 48 % | 64.9 px | 0.66 | 1.02 | 144 |
| long, no reload | 95 % → 94 % | 42.4 px | 0.68 | 0.99 | 929 | quarters: 0.67 → 0.67 → 0.67 → 0.62

Numbers say: light vs heavy: width 55.6 → 83.7 px, dark 0.66 → 0.65; the long stroke does not run out of paint.

## Brush Artist · Refs · #34 Magenta oil patches
Oil · 60 px · 22.1 s

![Brush Artist · Refs · #34 Magenta oil patches](Brush-Artist-Refs-34-Magenta-oil-patches.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 19 % → 19 % | 55.6 px | 0.59 | 1.00 | 178 |
| heavy line | 21 % → 21 % | 59.7 px | 0.59 | 1.00 | 209 |
| pressure swell | 16 % → 16 % | 58.8 px | 0.62 | 1.01 | 152 |
| fast wave | 48 % → 49 % | 55.4 px | 0.62 | 1.02 | 520 |
| slow wave | 48 % → 48 % | 55.8 px | 0.62 | 1.00 | 896 |
| spiral | 70 % → 70 % | 46.3 px | 0.62 | 1.00 | 876 |
| loop | 42 % → 42 % | 54.2 px | 0.62 | 1.00 | 454 |
| tilted | 17 % → 17 % | 46.8 px | 0.62 | 1.00 | 237 |
| over the wet one | 35 % → 35 % | 50.0 px | 0.62 | 1.00 | 200 |
| long, no reload | 86 % → 86 % | 38.7 px | 0.62 | 1.00 | 1309 | quarters: 0.59 → 0.58 → 0.57 → 0.52

Numbers say: light vs heavy: width 55.6 → 59.7 px, dark 0.59 → 0.59; pressure barely changes the width; the long stroke does not run out of paint.

## Brush Artist · Refs · #35 Red band with runs
Watercolor · 70 px · 32.5 s

![Brush Artist · Refs · #35 Red band with runs](Brush-Artist-Refs-35-Red-band-with-runs.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 17 % → 18 % | 48.3 px | 0.59 | 1.06 | 79 |
| heavy line | 25 % → 25 % | 73.9 px | 0.58 | 0.97 | 160 |
| pressure swell | 17 % → 17 % | 63.0 px | 0.60 | 1.01 | 102 |
| fast wave | 54 % → 53 % | 61.8 px | 0.58 | 0.98 | 319 |
| slow wave | 52 % → 52 % | 59.8 px | 0.60 | 1.01 | 528 |
| spiral | 72 % → 71 % | 47.3 px | 0.60 | 0.99 | 531 |
| loop | 46 % → 46 % | 60.2 px | 0.59 | 0.99 | 281 |
| tilted | 21 % → 21 % | 57.5 px | 0.59 | 1.01 | 190 |
| over the wet one | 42 % → 43 % | 59.8 px | 0.59 | 1.03 | 216 |
| long, no reload | 92 % → 91 % | 41.1 px | 0.60 | 0.99 | 794 | quarters: 0.58 → 0.59 → 0.57 → 0.54

Numbers say: light vs heavy: width 48.3 → 73.9 px, dark 0.59 → 0.58; the long stroke does not run out of paint.

## Brush Artist · Refs · #36 Magenta letters flat brush
Gouache · 36 px · 30.1 s

![Brush Artist · Refs · #36 Magenta letters flat brush](Brush-Artist-Refs-36-Magenta-letters-flat-brush.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 10 % → 10 % | 29.0 px | 0.45 | 0.98 | 77 |
| heavy line | 17 % → 14 % | 49.1 px | 0.45 | 0.85 | 92 |
| pressure swell | 13 % → 12 % | 49.4 px | 0.45 | 0.89 | 68 |
| fast wave | 35 % → 19 % | 40.3 px | 0.45 | 0.54 | 202 |
| slow wave | 35 % → 19 % | 39.9 px | 0.45 | 0.54 | 374 |
| spiral | 46 % → 19 % | 30.4 px | 0.45 | 0.42 | 416 |
| loop | 27 % → 20 % | 35.3 px | 0.45 | 0.72 | 174 |
| tilted | 11 % → 11 % | 29.8 px | 0.45 | 1.00 | 106 |
| over the wet one | 24 % → 22 % | 38.1 px | 0.45 | 0.92 | 89 |
| long, no reload | 46 % → 19 % | 20.8 px | 0.45 | 0.40 | 550 | quarters: 0.29 → 0.25 → 0.22 → 0.18

Numbers say: light vs heavy: width 29.0 → 49.1 px, dark 0.45 → 0.45.

## Brush Artist · Refs · #37 Oil still life dabs
Oil · 40 px · 18.8 s

![Brush Artist · Refs · #37 Oil still life dabs](Brush-Artist-Refs-37-Oil-still-life-dabs.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 13 % → 13 % | 37.9 px | 0.39 | 1.00 | 193 |
| heavy line | 14 % → 14 % | 41.1 px | 0.38 | 1.00 | 128 |
| pressure swell | 11 % → 11 % | 40.2 px | 0.40 | 1.00 | 100 |
| fast wave | 34 % → 34 % | 39.8 px | 0.40 | 1.00 | 348 |
| slow wave | 35 % → 35 % | 40.2 px | 0.39 | 1.00 | 593 |
| spiral | 59 % → 59 % | 38.7 px | 0.38 | 1.00 | 588 |
| loop | 29 % → 29 % | 37.8 px | 0.39 | 1.00 | 296 |
| tilted | 13 % → 13 % | 35.8 px | 0.39 | 1.00 | 158 |
| over the wet one | 26 % → 26 % | 35.6 px | 0.39 | 1.00 | 134 |
| long, no reload | 69 % → 69 % | 30.9 px | 0.37 | 1.00 | 835 | quarters: 0.31 → 0.30 → 0.28 → 0.24

Numbers say: light vs heavy: width 37.9 → 41.1 px, dark 0.39 → 0.38; pressure barely changes the width.

## Brush Artist · Refs · #38 Sanguine drawing
Pastel · 6 px · 8.6 s

![Brush Artist · Refs · #38 Sanguine drawing](Brush-Artist-Refs-38-Sanguine-drawing.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 1 % → 1 % | 2.0 px | 0.61 | 1.00 | 9 |
| heavy line | 1 % → 1 % | 3.5 px | 0.62 | 1.00 | 14 |
| pressure swell | 1 % → 1 % | 3.3 px | 0.62 | 1.00 | 7 |
| fast wave | 3 % → 3 % | 3.2 px | 0.61 | 1.00 | 39 |
| slow wave | 3 % → 3 % | 3.0 px | 0.61 | 1.00 | 29 |
| spiral | 4 % → 4 % | 2.9 px | 0.61 | 1.00 | 57 |
| loop | 2 % → 2 % | 3.0 px | 0.61 | 1.00 | 31 |
| tilted | 1 % → 1 % | 3.4 px | 0.62 | 1.00 | 24 |
| over the wet one | 2 % → 2 % | 2.9 px | 0.62 | 1.00 | 15 |
| long, no reload | 7 % → 7 % | 3.0 px | 0.61 | 1.00 | 116 | quarters: 0.04 → 0.05 → 0.05 → 0.05

Numbers say: light vs heavy: width 2.0 → 3.5 px, dark 0.61 → 0.62; the long stroke does not run out of paint.

## Brush Artist · Refs · #39 Very thick impasto
Heavy acrylic · 60 px · 20.8 s

![Brush Artist · Refs · #39 Very thick impasto](Brush-Artist-Refs-39-Very-thick-impasto.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 20 % → 19 % | 56.8 px | 0.61 | 0.97 | 159 |
| heavy line | 20 % → 20 % | 59.4 px | 0.61 | 0.97 | 169 |
| pressure swell | 16 % → 15 % | 59.6 px | 0.62 | 0.97 | 125 |
| fast wave | 48 % → 47 % | 55.2 px | 0.62 | 0.98 | 444 |
| slow wave | 48 % → 47 % | 56.0 px | 0.62 | 0.98 | 771 |
| spiral | 69 % → 65 % | 45.6 px | 0.62 | 0.93 | 724 |
| loop | 42 % → 41 % | 54.0 px | 0.62 | 0.97 | 380 |
| tilted | 16 % → 16 % | 44.0 px | 0.62 | 1.00 | 209 |
| over the wet one | 34 % → 33 % | 50.7 px | 0.62 | 0.97 | 181 |
| long, no reload | 85 % → 79 % | 38.3 px | 0.62 | 0.93 | 1119 | quarters: 0.58 → 0.57 → 0.55 → 0.52

Numbers say: light vs heavy: width 56.8 → 59.4 px, dark 0.61 → 0.61; pressure barely changes the width; the long stroke does not run out of paint.

## Brush Artist · Refs · #40 Watercolour blooms
Watercolor · 90 px · 35.8 s

![Brush Artist · Refs · #40 Watercolour blooms](Brush-Artist-Refs-40-Watercolour-blooms.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 22 % → 22 % | 63.3 px | 0.14 | 0.99 | 119 |
| heavy line | 33 % → 31 % | 94.9 px | 0.14 | 0.94 | 231 |
| pressure swell | 22 % → 23 % | 84.1 px | 0.15 | 1.00 | 137 |
| fast wave | 64 % → 64 % | 73.9 px | 0.13 | 1.00 | 442 |
| slow wave | 62 % → 61 % | 72.1 px | 0.19 | 0.98 | 734 |
| spiral | 79 % → 77 % | 52.0 px | 0.17 | 0.98 | 749 |
| loop | 56 % → 54 % | 72.4 px | 0.16 | 0.97 | 390 |
| tilted | 26 % → 26 % | 72.5 px | 0.17 | 1.00 | 273 |
| over the wet one | 52 % → 53 % | 72.0 px | 0.17 | 1.02 | 185 |
| long, no reload | 97 % → 96 % | 43.4 px | 0.17 | 0.99 | 1109 | quarters: 0.21 → 0.19 → 0.16 → 0.13

Numbers say: light vs heavy: width 63.3 → 94.9 px, dark 0.14 → 0.14.

## Brush Artist · Refs · #41 Coloured pencil hatching
Pastel · 4 px · 8.4 s

![Brush Artist · Refs · #41 Coloured pencil hatching](Brush-Artist-Refs-41-Coloured-pencil-hatching.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 1 % → 1 % | 1.6 px | 0.42 | 1.00 | 7 |
| heavy line | 1 % → 1 % | 2.6 px | 0.43 | 1.00 | 11 |
| pressure swell | 1 % → 1 % | 2.1 px | 0.43 | 1.00 | 9 |
| fast wave | 2 % → 2 % | 2.2 px | 0.42 | 1.00 | 24 |
| slow wave | 2 % → 2 % | 2.1 px | 0.43 | 1.00 | 29 |
| spiral | 3 % → 3 % | 2.1 px | 0.43 | 1.00 | 45 |
| loop | 2 % → 2 % | 2.2 px | 0.43 | 1.00 | 26 |
| tilted | 1 % → 1 % | 3.0 px | 0.42 | 1.00 | 13 |
| over the wet one | 2 % → 2 % | 2.2 px | 0.42 | 1.00 | 11 |
| long, no reload | 5 % → 5 % | 2.3 px | 0.43 | 1.00 | 77 | quarters: 0.02 → 0.02 → 0.02 → 0.03

Numbers say: light vs heavy: width 1.6 → 2.6 px, dark 0.42 → 0.43; the long stroke does not run out of paint.

## Brush Artist · Refs · #42 Oil pastel shaggy
Pastel · 18 px · 9.2 s

![Brush Artist · Refs · #42 Oil pastel shaggy](Brush-Artist-Refs-42-Oil-pastel-shaggy.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 2 % → 2 % | 5.1 px | 0.35 | 1.00 | 17 |
| heavy line | 4 % → 4 % | 10.7 px | 0.36 | 1.00 | 25 |
| pressure swell | 3 % → 3 % | 9.5 px | 0.36 | 1.00 | 22 |
| fast wave | 8 % → 8 % | 9.0 px | 0.36 | 1.00 | 62 |
| slow wave | 7 % → 7 % | 8.2 px | 0.36 | 1.00 | 80 |
| spiral | 12 % → 12 % | 7.7 px | 0.36 | 1.00 | 109 |
| loop | 6 % → 6 % | 7.9 px | 0.36 | 1.00 | 49 |
| tilted | 2 % → 2 % | 6.9 px | 0.36 | 1.00 | 29 |
| over the wet one | 6 % → 6 % | 8.5 px | 0.36 | 1.00 | 22 |
| long, no reload | 15 % → 15 % | 6.9 px | 0.36 | 1.00 | 139 | quarters: 0.00 → 0.00 → 0.00 → 0.00

Numbers say: light vs heavy: width 5.1 → 10.7 px, dark 0.35 → 0.36; the long stroke does not run out of paint.

## Brush Artist · Refs · #43 Dragged black ink blocks
Gouache · 70 px · 28.7 s

![Brush Artist · Refs · #43 Dragged black ink blocks](Brush-Artist-Refs-43-Dragged-black-ink-blocks.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 19 % → 5 % | 54.9 px | 0.57 | 0.28 | 112 |
| heavy line | 24 % → 9 % | 69.0 px | 0.57 | 0.38 | 303 |
| pressure swell | 17 % → 9 % | 63.4 px | 0.57 | 0.53 | 172 |
| fast wave | 51 % → 11 % | 58.7 px | 0.57 | 0.21 | 569 |
| slow wave | 50 % → 10 % | 58.1 px | 0.57 | 0.20 | 893 |
| spiral | 65 % → 14 % | 42.6 px | 0.57 | 0.22 | 867 |
| loop | 45 % → 12 % | 58.1 px | 0.57 | 0.27 | 462 |
| tilted | 17 % → 16 % | 46.4 px | 0.57 | 0.98 | 318 |
| over the wet one | 37 % → 20 % | 55.6 px | 0.57 | 0.56 | 224 |
| long, no reload | 82 % → 17 % | 36.6 px | 0.57 | 0.21 | 1319 | quarters: 0.54 → 0.52 → 0.47 → 0.40

Numbers say: light vs heavy: width 54.9 → 69.0 px, dark 0.57 → 0.57.

## Brush Artist · Refs · #44 Blue looping ribbon
Oil · 80 px · 24.9 s

![Brush Artist · Refs · #44 Blue looping ribbon](Brush-Artist-Refs-44-Blue-looping-ribbon.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 26 % → 27 % | 74.8 px | 0.71 | 1.04 | 252 |
| heavy line | 27 % → 27 % | 79.6 px | 0.71 | 1.00 | 274 |
| pressure swell | 21 % → 21 % | 78.1 px | 0.72 | 1.03 | 199 |
| fast wave | 61 % → 64 % | 70.3 px | 0.73 | 1.05 | 735 |
| slow wave | 61 % → 61 % | 70.0 px | 0.73 | 1.00 | 1250 |
| spiral | 78 % → 78 % | 51.3 px | 0.73 | 1.00 | 1264 |
| loop | 54 % → 54 % | 69.7 px | 0.72 | 1.00 | 614 |
| tilted | 20 % → 20 % | 57.2 px | 0.71 | 1.00 | 360 |
| over the wet one | 44 % → 44 % | 64.9 px | 0.71 | 1.00 | 288 |
| long, no reload | 96 % → 96 % | 42.8 px | 0.73 | 1.00 | 1790 | quarters: 0.72 → 0.72 → 0.72 → 0.69

Numbers say: light vs heavy: width 74.8 → 79.6 px, dark 0.71 → 0.71; pressure barely changes the width; the long stroke does not run out of paint.

## Brush Artist · Refs · #45 Soft pastel pepper
Pastel · 40 px · 9.6 s

![Brush Artist · Refs · #45 Soft pastel pepper](Brush-Artist-Refs-45-Soft-pastel-pepper.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 4 % → 4 % | 11.3 px | 0.53 | 1.00 | 41 |
| heavy line | 8 % → 8 % | 23.0 px | 0.53 | 1.00 | 47 |
| pressure swell | 5 % → 5 % | 19.5 px | 0.53 | 1.00 | 35 |
| fast wave | 17 % → 17 % | 19.4 px | 0.53 | 1.00 | 116 |
| slow wave | 15 % → 15 % | 17.1 px | 0.53 | 1.00 | 192 |
| spiral | 25 % → 25 % | 16.3 px | 0.53 | 1.00 | 203 |
| loop | 12 % → 12 % | 16.1 px | 0.53 | 1.00 | 101 |
| tilted | 5 % → 5 % | 12.8 px | 0.53 | 1.00 | 51 |
| over the wet one | 11 % → 11 % | 17.7 px | 0.53 | 1.00 | 49 |
| long, no reload | 30 % → 30 % | 13.6 px | 0.53 | 1.00 | 284 | quarters: 0.18 → 0.18 → 0.18 → 0.18

Numbers say: light vs heavy: width 11.3 → 23.0 px, dark 0.53 → 0.53; the long stroke does not run out of paint.

## Brush Artist · Refs · #46 Red-brown ink lips
Watercolor · 70 px · 32.8 s

![Brush Artist · Refs · #46 Red-brown ink lips](Brush-Artist-Refs-46-Red-brown-ink-lips.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 17 % → 17 % | 48.3 px | 0.74 | 1.04 | 88 |
| heavy line | 25 % → 25 % | 73.9 px | 0.72 | 0.97 | 169 |
| pressure swell | 17 % → 17 % | 63.0 px | 0.75 | 1.00 | 100 |
| fast wave | 54 % → 53 % | 61.8 px | 0.73 | 0.99 | 314 |
| slow wave | 52 % → 52 % | 59.8 px | 0.74 | 1.01 | 516 |
| spiral | 72 % → 71 % | 47.3 px | 0.74 | 0.99 | 515 |
| loop | 46 % → 46 % | 60.2 px | 0.74 | 0.99 | 263 |
| tilted | 21 % → 21 % | 57.5 px | 0.73 | 1.01 | 180 |
| over the wet one | 42 % → 43 % | 59.8 px | 0.73 | 1.03 | 125 |
| long, no reload | 92 % → 91 % | 41.1 px | 0.74 | 0.99 | 763 | quarters: 0.71 → 0.72 → 0.71 → 0.67

Numbers say: light vs heavy: width 48.3 → 73.9 px, dark 0.74 → 0.72; the long stroke does not run out of paint.

## Brush Artist · Refs · #47 Pink knife slabs
Heavy acrylic · 90 px · 25.9 s

![Brush Artist · Refs · #47 Pink knife slabs](Brush-Artist-Refs-47-Pink-knife-slabs.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 28 % → 27 % | 81.0 px | 0.28 | 0.97 | 196 |
| heavy line | 29 % → 28 % | 83.4 px | 0.28 | 0.97 | 216 |
| pressure swell | 22 % → 22 % | 83.4 px | 0.28 | 1.01 | 145 |
| fast wave | 61 % → 60 % | 70.1 px | 0.27 | 0.98 | 516 |
| slow wave | 61 % → 59 % | 70.9 px | 0.26 | 0.96 | 908 |
| spiral | 76 % → 58 % | 50.0 px | 0.26 | 0.76 | 910 |
| loop | 55 % → 54 % | 71.7 px | 0.27 | 0.97 | 480 |
| tilted | 21 % → 21 % | 59.3 px | 0.28 | 1.00 | 258 |
| over the wet one | 46 % → 44 % | 67.9 px | 0.28 | 0.96 | 224 |
| long, no reload | 92 % → 76 % | 41.3 px | 0.26 | 0.83 | 1376 | quarters: 0.00 → 0.00 → 0.00 → 0.00

Numbers say: light vs heavy: width 81.0 → 83.4 px, dark 0.28 → 0.28; pressure barely changes the width; the long stroke does not run out of paint.

## Brush Artist · Refs · #48 Black bands with drips
Gouache · 70 px · 38.9 s

![Brush Artist · Refs · #48 Black bands with drips](Brush-Artist-Refs-48-Black-bands-with-drips.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 19 % → 18 % | 54.6 px | 0.69 | 0.93 | 170 |
| heavy line | 29 % → 24 % | 83.0 px | 0.69 | 0.84 | 236 |
| pressure swell | 23 % → 21 % | 86.1 px | 0.69 | 0.92 | 153 |
| fast wave | 53 % → 36 % | 61.8 px | 0.69 | 0.68 | 478 |
| slow wave | 53 % → 36 % | 61.7 px | 0.69 | 0.67 | 816 |
| spiral | 64 % → 35 % | 41.9 px | 0.69 | 0.55 | 826 |
| loop | 45 % → 36 % | 57.8 px | 0.69 | 0.81 | 410 |
| tilted | 19 % → 19 % | 52.3 px | 0.69 | 1.00 | 246 |
| over the wet one | 41 % → 38 % | 62.4 px | 0.69 | 0.92 | 197 |
| long, no reload | 74 % → 37 % | 33.3 px | 0.69 | 0.50 | 1162 | quarters: 0.64 → 0.61 → 0.54 → 0.45

Numbers say: light vs heavy: width 54.6 → 83.0 px, dark 0.69 → 0.69.

## Brush Artist · Refs · #49 Magenta letters round brush
Ink · 30 px · 28.2 s

![Brush Artist · Refs · #49 Magenta letters round brush](Brush-Artist-Refs-49-Magenta-letters-round-brush.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 6 % → 8 % | 17.5 px | 0.50 | 1.28 | 36 |
| heavy line | 21 % → 21 % | 62.0 px | 0.51 | 0.99 | 98 |
| pressure swell | 12 % → 13 % | 46.3 px | 0.52 | 1.01 | 66 |
| fast wave | 38 % → 38 % | 44.3 px | 0.51 | 0.99 | 188 |
| slow wave | 32 % → 31 % | 36.4 px | 0.51 | 0.99 | 278 |
| spiral | 50 % → 48 % | 32.8 px | 0.51 | 0.97 | 292 |
| loop | 29 % → 29 % | 37.6 px | 0.51 | 1.00 | 135 |
| tilted | 11 % → 11 % | 30.7 px | 0.52 | 1.01 | 73 |
| over the wet one | 26 % → 26 % | 42.1 px | 0.52 | 1.01 | 68 |
| long, no reload | 61 % → 56 % | 27.5 px | 0.51 | 0.92 | 412 | quarters: 0.41 → 0.36 → 0.30 → 0.25

Numbers say: light vs heavy: width 17.5 → 62.0 px, dark 0.50 → 0.51.

## Brush Artist · Refs · #50 Thick swipes on photo
Heavy acrylic · 40 px · 16.4 s

![Brush Artist · Refs · #50 Thick swipes on photo](Brush-Artist-Refs-50-Thick-swipes-on-photo.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 13 % → 13 % | 38.0 px | 0.25 | 0.96 | 108 |
| heavy line | 14 % → 13 % | 40.1 px | 0.25 | 0.96 | 108 |
| pressure swell | 11 % → 10 % | 40.1 px | 0.25 | 0.95 | 82 |
| fast wave | 33 % → 31 % | 38.3 px | 0.25 | 0.93 | 274 |
| slow wave | 34 % → 32 % | 39.1 px | 0.25 | 0.95 | 476 |
| spiral | 58 % → 47 % | 38.5 px | 0.24 | 0.80 | 472 |
| loop | 28 % → 27 % | 36.8 px | 0.26 | 0.95 | 250 |
| tilted | 12 % → 12 % | 34.0 px | 0.25 | 1.00 | 115 |
| over the wet one | 25 % → 24 % | 35.2 px | 0.25 | 0.95 | 108 |
| long, no reload | 66 % → 46 % | 29.5 px | 0.24 | 0.70 | 724 | quarters: 0.00 → 0.00 → 0.00 → 0.00

Numbers say: light vs heavy: width 38.0 → 40.1 px, dark 0.25 → 0.25; pressure barely changes the width; the long stroke does not run out of paint.

## Brush Artist · Ink — wash
Watercolor · 38 px · 29.2 s

![Brush Artist · Ink — wash](Brush-Artist-Ink-wash.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 11 % → 11 % | 31.6 px | 0.38 | 1.03 | 58 |
| heavy line | 19 % → 19 % | 54.3 px | 0.32 | 1.03 | 92 |
| pressure swell | 12 % → 12 % | 45.1 px | 0.36 | 1.04 | 64 |
| fast wave | 39 % → 41 % | 44.7 px | 0.30 | 1.05 | 182 |
| slow wave | 37 % → 38 % | 42.6 px | 0.37 | 1.04 | 308 |
| spiral | 57 % → 60 % | 37.9 px | 0.30 | 1.04 | 312 |
| loop | 32 % → 33 % | 41.8 px | 0.34 | 1.02 | 162 |
| tilted | 13 % → 14 % | 36.8 px | 0.38 | 1.04 | 95 |
| over the wet one | 29 % → 30 % | 42.8 px | 0.38 | 1.04 | 79 |
| long, no reload | 65 % → 70 % | 29.2 px | 0.29 | 1.08 | 450 | quarters: 0.33 → 0.26 → 0.18 → 0.11

Numbers say: light vs heavy: width 31.6 → 54.3 px, dark 0.38 → 0.32.

## Brush Artist · Ink — brush line
Ink · 16 px · 24.2 s

![Brush Artist · Ink — brush line](Brush-Artist-Ink-brush-line.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 3 % → 5 % | 7.7 px | 0.78 | 1.80 | 39 |
| heavy line | 13 % → 13 % | 39.0 px | 0.88 | 0.99 | 74 |
| pressure swell | 8 % → 8 % | 28.4 px | 0.87 | 1.05 | 43 |
| fast wave | 24 % → 23 % | 27.6 px | 0.87 | 0.96 | 136 |
| slow wave | 19 % → 19 % | 22.5 px | 0.87 | 0.97 | 156 |
| spiral | 30 % → 27 % | 19.9 px | 0.86 | 0.90 | 248 |
| loop | 18 % → 18 % | 23.4 px | 0.88 | 1.00 | 107 |
| tilted | 7 % → 7 % | 20.1 px | 0.88 | 1.01 | 57 |
| over the wet one | 17 % → 17 % | 26.8 px | 0.88 | 1.00 | 52 |
| long, no reload | 42 % → 31 % | 18.8 px | 0.85 | 0.73 | 342 | quarters: 0.49 → 0.40 → 0.30 → 0.21

Numbers say: light vs heavy: width 7.7 → 39.0 px, dark 0.78 → 0.88; wet paint spreads well beyond the stroke.

## Brush Artist · Ink — dry brush
Gouache · 30 px · 20.3 s

![Brush Artist · Ink — dry brush](Brush-Artist-Ink-dry-brush.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 7 % → 1 % | 21.8 px | 0.71 | 0.11 | 59 |
| heavy line | 10 % → 1 % | 27.7 px | 0.71 | 0.10 | 128 |
| pressure swell | 7 % → 2 % | 25.5 px | 0.71 | 0.23 | 72 |
| fast wave | 21 % → 2 % | 24.2 px | 0.71 | 0.09 | 211 |
| slow wave | 21 % → 2 % | 23.9 px | 0.71 | 0.08 | 352 |
| spiral | 31 % → 2 % | 20.6 px | 0.71 | 0.06 | 324 |
| loop | 18 % → 2 % | 23.9 px | 0.71 | 0.13 | 184 |
| tilted | 9 % → 8 % | 24.1 px | 0.71 | 0.96 | 102 |
| over the wet one | 17 % → 4 % | 22.8 px | 0.71 | 0.24 | 92 |
| long, no reload | 31 % → 3 % | 14.0 px | 0.71 | 0.09 | 513 | quarters: 0.38 → 0.32 → 0.22 → 0.09

Numbers say: light vs heavy: width 21.8 → 27.7 px, dark 0.71 → 0.71.

## Brush Artist · Watercolour — blue
Watercolor · 40 px · 25.7 s

![Brush Artist · Watercolour — blue](Brush-Artist-Watercolour-blue.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 6 % → 10 % | 16.7 px | 0.25 | 1.70 | 27 |
| heavy line | 11 % → 12 % | 31.5 px | 0.25 | 1.13 | 60 |
| pressure swell | 7 % → 9 % | 25.4 px | 0.26 | 1.32 | 37 |
| fast wave | 24 % → 25 % | 27.8 px | 0.24 | 1.05 | 128 |
| slow wave | 22 % → 27 % | 25.9 px | 0.26 | 1.22 | 210 |
| spiral | 38 % → 41 % | 25.1 px | 0.22 | 1.08 | 212 |
| loop | 20 % → 22 % | 25.3 px | 0.26 | 1.13 | 108 |
| tilted | 12 % → 12 % | 33.3 px | 0.26 | 1.00 | 85 |
| over the wet one | 21 % → 24 % | 24.7 px | 0.26 | 1.15 | 52 |
| long, no reload | 51 % → 54 % | 23.0 px | 0.22 | 1.04 | 310 | quarters: 0.18 → 0.14 → 0.11 → 0.08

Numbers say: light vs heavy: width 16.7 → 31.5 px, dark 0.25 → 0.25; wet paint spreads well beyond the stroke.

## Brush Artist · Watercolour — violet
Watercolor · 40 px · 25.3 s

![Brush Artist · Watercolour — violet](Brush-Artist-Watercolour-violet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 6 % → 10 % | 16.7 px | 0.40 | 1.70 | 25 |
| heavy line | 11 % → 12 % | 31.5 px | 0.40 | 1.13 | 63 |
| pressure swell | 7 % → 9 % | 25.4 px | 0.41 | 1.32 | 38 |
| fast wave | 24 % → 25 % | 27.8 px | 0.38 | 1.05 | 125 |
| slow wave | 22 % → 27 % | 25.9 px | 0.40 | 1.22 | 202 |
| spiral | 38 % → 41 % | 25.1 px | 0.36 | 1.08 | 206 |
| loop | 20 % → 22 % | 25.3 px | 0.40 | 1.13 | 111 |
| tilted | 12 % → 12 % | 33.3 px | 0.40 | 1.00 | 80 |
| over the wet one | 21 % → 24 % | 24.7 px | 0.40 | 1.15 | 53 |
| long, no reload | 51 % → 54 % | 23.0 px | 0.34 | 1.04 | 299 | quarters: 0.28 → 0.22 → 0.17 → 0.14

Numbers say: light vs heavy: width 16.7 → 31.5 px, dark 0.40 → 0.40; wet paint spreads well beyond the stroke.

## Brush Artist · Watercolour — teal
Watercolor · 40 px · 25.4 s

![Brush Artist · Watercolour — teal](Brush-Artist-Watercolour-teal.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 6 % → 10 % | 16.7 px | 0.16 | 1.70 | 27 |
| heavy line | 11 % → 12 % | 31.5 px | 0.16 | 1.13 | 67 |
| pressure swell | 7 % → 9 % | 25.4 px | 0.17 | 1.32 | 33 |
| fast wave | 24 % → 25 % | 27.8 px | 0.15 | 1.05 | 130 |
| slow wave | 22 % → 27 % | 25.9 px | 0.17 | 1.22 | 218 |
| spiral | 38 % → 41 % | 25.1 px | 0.15 | 1.08 | 195 |
| loop | 20 % → 22 % | 25.3 px | 0.16 | 1.13 | 119 |
| tilted | 12 % → 12 % | 33.3 px | 0.16 | 1.00 | 84 |
| over the wet one | 21 % → 24 % | 24.7 px | 0.16 | 1.15 | 50 |
| long, no reload | 51 % → 54 % | 23.0 px | 0.14 | 1.04 | 332 | quarters: 0.11 → 0.09 → 0.07 → 0.06

Numbers say: light vs heavy: width 16.7 → 31.5 px, dark 0.16 → 0.16; wet paint spreads well beyond the stroke.

## Brush Artist · Gouache
Gouache · 30 px · 29.4 s

![Brush Artist · Gouache](Brush-Artist-Gouache.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 8 % → 8 % | 24.4 px | 0.27 | 0.97 | 67 |
| heavy line | 15 % → 11 % | 42.8 px | 0.27 | 0.78 | 78 |
| pressure swell | 11 % → 9 % | 41.0 px | 0.27 | 0.84 | 64 |
| fast wave | 30 % → 13 % | 34.4 px | 0.26 | 0.45 | 178 |
| slow wave | 29 % → 14 % | 33.9 px | 0.26 | 0.46 | 317 |
| spiral | 40 % → 14 % | 26.6 px | 0.26 | 0.35 | 300 |
| loop | 23 % → 15 % | 30.4 px | 0.26 | 0.62 | 164 |
| tilted | 10 % → 10 % | 27.1 px | 0.26 | 1.01 | 86 |
| over the wet one | 21 % → 19 % | 32.8 px | 0.26 | 0.89 | 71 |
| long, no reload | 43 % → 15 % | 19.1 px | 0.26 | 0.35 | 441 | quarters: 0.01 → 0.01 → 0.01 → 0.01

Numbers say: light vs heavy: width 24.4 → 42.8 px, dark 0.27 → 0.27; the long stroke does not run out of paint.

## Brush Artist · Oil — bristle
Oil · 30 px · 17.1 s

![Brush Artist · Oil — bristle](Brush-Artist-Oil-bristle.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 9 % → 9 % | 26.2 px | 0.54 | 1.00 | 99 |
| heavy line | 10 % → 10 % | 28.5 px | 0.54 | 1.00 | 104 |
| pressure swell | 8 % → 8 % | 28.2 px | 0.55 | 1.00 | 89 |
| fast wave | 24 % → 24 % | 27.3 px | 0.55 | 1.00 | 276 |
| slow wave | 24 % → 24 % | 28.2 px | 0.55 | 1.00 | 416 |
| spiral | 39 % → 39 % | 25.6 px | 0.54 | 1.00 | 421 |
| loop | 20 % → 20 % | 26.2 px | 0.54 | 1.00 | 224 |
| tilted | 11 % → 11 % | 29.9 px | 0.54 | 1.00 | 130 |
| over the wet one | 20 % → 20 % | 25.2 px | 0.54 | 1.00 | 106 |
| long, no reload | 50 % → 50 % | 22.4 px | 0.54 | 1.00 | 647 | quarters: 0.32 → 0.30 → 0.29 → 0.28

Numbers say: light vs heavy: width 26.2 → 28.5 px, dark 0.54 → 0.54; pressure barely changes the width; the long stroke does not run out of paint.

## Brush Artist · Charcoal — stick
Charcoal · 28 px · 9.3 s

![Brush Artist · Charcoal — stick](Brush-Artist-Charcoal-stick.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 3 % → 3 % | 8.4 px | 0.85 | 1.00 | 15 |
| heavy line | 6 % → 6 % | 17.8 px | 0.85 | 1.00 | 17 |
| pressure swell | 4 % → 4 % | 13.9 px | 0.85 | 1.00 | 11 |
| fast wave | 12 % → 12 % | 14.0 px | 0.85 | 1.00 | 47 |
| slow wave | 11 % → 11 % | 12.5 px | 0.85 | 1.00 | 116 |
| spiral | 19 % → 19 % | 12.7 px | 0.85 | 1.00 | 79 |
| loop | 10 % → 10 % | 12.8 px | 0.85 | 1.00 | 35 |
| tilted | 4 % → 4 % | 10.9 px | 0.85 | 1.00 | 32 |
| over the wet one | 9 % → 9 % | 13.5 px | 0.85 | 1.00 | 19 |
| long, no reload | 27 % → 27 % | 12.2 px | 0.85 | 1.00 | 98 | quarters: 0.26 → 0.25 → 0.26 → 0.27

Numbers say: light vs heavy: width 8.4 → 17.8 px, dark 0.85 → 0.85; the long stroke does not run out of paint.

## Brush Artist · Charcoal — stick B
Charcoal · 36 px · 9.6 s

![Brush Artist · Charcoal — stick B](Brush-Artist-Charcoal-stick-B.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 4 % → 4 % | 10.5 px | 0.85 | 1.00 | 21 |
| heavy line | 7 % → 7 % | 21.1 px | 0.85 | 1.00 | 28 |
| pressure swell | 4 % → 4 % | 16.5 px | 0.85 | 1.00 | 14 |
| fast wave | 15 % → 15 % | 16.8 px | 0.85 | 1.00 | 61 |
| slow wave | 13 % → 13 % | 14.7 px | 0.85 | 1.00 | 94 |
| spiral | 23 % → 23 % | 15.0 px | 0.85 | 1.00 | 112 |
| loop | 11 % → 11 % | 14.8 px | 0.85 | 1.00 | 57 |
| tilted | 4 % → 4 % | 12.3 px | 0.85 | 1.00 | 32 |
| over the wet one | 10 % → 10 % | 15.9 px | 0.85 | 1.00 | 29 |
| long, no reload | 31 % → 31 % | 13.9 px | 0.85 | 1.00 | 140 | quarters: 0.30 → 0.28 → 0.29 → 0.30

Numbers say: light vs heavy: width 10.5 → 21.1 px, dark 0.85 → 0.85; the long stroke does not run out of paint.

## Brush Artist · Charcoal — stick C
Charcoal · 22 px · 9.1 s

![Brush Artist · Charcoal — stick C](Brush-Artist-Charcoal-stick-C.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 2 % → 2 % | 6.9 px | 0.85 | 1.00 | 10 |
| heavy line | 5 % → 5 % | 15.3 px | 0.85 | 1.00 | 11 |
| pressure swell | 3 % → 3 % | 12.2 px | 0.85 | 1.00 | 18 |
| fast wave | 10 % → 10 % | 12.1 px | 0.85 | 1.00 | 26 |
| slow wave | 9 % → 9 % | 10.8 px | 0.85 | 1.00 | 57 |
| spiral | 17 % → 17 % | 11.0 px | 0.85 | 1.00 | 62 |
| loop | 9 % → 9 % | 11.4 px | 0.85 | 1.00 | 29 |
| tilted | 4 % → 4 % | 9.9 px | 0.85 | 1.00 | 22 |
| over the wet one | 8 % → 8 % | 11.7 px | 0.85 | 1.00 | 18 |
| long, no reload | 24 % → 24 % | 11.0 px | 0.85 | 1.00 | 97 | quarters: 0.24 → 0.22 → 0.23 → 0.24

Numbers say: light vs heavy: width 6.9 → 15.3 px, dark 0.85 → 0.85; the long stroke does not run out of paint.

## Brush Artist · Refs · #01 Henry Ward peach cloud — own sheet
own sheet 600 × 600 · Gouache · 44 px · 14.0 s

![Brush Artist · Refs · #01 Henry Ward peach cloud — own sheet](Brush-Artist-Refs-01-Henry-Ward-peach-cloud-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 35 % → 47 % | 45.1 px | 0.59 | 1.34 | 147 |
| stroke 2 | 41 % → 63 % | 66.0 px | 0.59 | 1.53 | 135 |
| stroke 3 | 45 % → 73 % | 58.9 px | 0.59 | 1.62 | 133 |
| stroke 4 | 49 % → 69 % | 79.3 px | 0.59 | 1.40 | 148 |
| stroke 5 | 41 % → 67 % | 55.6 px | 0.59 | 1.63 | 147 |
| stroke 6 | 49 % → 53 % | 72.2 px | 0.59 | 1.09 | 137 |
| stroke 7 | 32 % → 59 % | 44.9 px | 0.60 | 1.83 | 139 |
| stroke 8 | 37 % → 62 % | 48.3 px | 0.60 | 1.66 | 138 |
| stroke 9 | 46 % → 68 % | 57.4 px | 0.60 | 1.48 | 161 |
| stroke 10 | 51 % → 74 % | 64.5 px | 0.60 | 1.44 | 165 |
| stroke 11 | 53 % → 77 % | 73.0 px | 0.60 | 1.44 | 161 |
| stroke 12 | 62 % → 88 % | 84.2 px | 0.60 | 1.43 | 132 |
| stroke 13 | 61 % → 85 % | 81.0 px | 0.60 | 1.39 | 157 |
| stroke 14 | 60 % → 85 % | 77.5 px | 0.60 | 1.42 | 160 |
| stroke 15 | 67 % → 86 % | 90.7 px | 0.60 | 1.29 | 160 |
| stroke 16 | 72 % → 89 % | 101.2 px | 0.60 | 1.24 | 145 |
| stroke 17 | 69 % → 86 % | 85.7 px | 0.60 | 1.24 | 169 |
| stroke 18 | 70 % → 86 % | 92.9 px | 0.60 | 1.22 | 150 |
| stroke 19 | 73 % → 86 % | 91.2 px | 0.60 | 1.17 | 146 |
| stroke 20 | 73 % → 83 % | 96.6 px | 0.59 | 1.14 | 147 |
| stroke 21 | 73 % → 78 % | 98.4 px | 0.59 | 1.06 | 155 |
| stroke 22 | 76 % → 80 % | 101.9 px | 0.59 | 1.05 | 154 |
| stroke 23 | 75 % → 75 % | 95.6 px | 0.59 | 1.01 | 158 |
| stroke 24 | 80 % → 79 % | 107.3 px | 0.59 | 1.00 | 155 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #02 Henry Ward cream strokes — own sheet
own sheet 600 × 600 · Gouache · 46 px · 9.0 s

![Brush Artist · Refs · #02 Henry Ward cream strokes — own sheet](Brush-Artist-Refs-02-Henry-Ward-cream-strokes-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 33 % → 37 % | 42.9 px | 0.71 | 1.12 | 186 |
| stroke 2 | 37 % → 35 % | 52.2 px | 0.71 | 0.96 | 213 |
| stroke 3 | 31 % → 40 % | 43.5 px | 0.71 | 1.27 | 205 |
| stroke 4 | 38 % → 56 % | 52.3 px | 0.72 | 1.48 | 222 |
| stroke 5 | 55 % → 53 % | 71.7 px | 0.72 | 0.96 | 216 |
| stroke 6 | 35 % → 49 % | 42.9 px | 0.71 | 1.37 | 209 |
| stroke 7 | 49 % → 46 % | 62.4 px | 0.71 | 0.95 | 197 |

## Brush Artist · Refs · #03 Henry Ward navy contours — own sheet
own sheet 600 × 600 · Heavy acrylic · 22 px · 2.6 s

![Brush Artist · Refs · #03 Henry Ward navy contours — own sheet](Brush-Artist-Refs-03-Henry-Ward-navy-contours-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 15 % → 20 % | 23.1 px | 0.69 | 1.28 | 112 |
| stroke 2 | 28 % → 30 % | 26.3 px | 0.69 | 1.09 | 97 |
| stroke 3 | 28 % → 28 % | 29.4 px | 0.70 | 0.99 | 114 |
| stroke 4 | 26 % → 24 % | 45.9 px | 0.69 | 0.92 | 149 |

## Brush Artist · Refs · #04 Henry Ward grey cloud — own sheet
own sheet 600 × 600 · Gouache · 50 px · 13.3 s

![Brush Artist · Refs · #04 Henry Ward grey cloud — own sheet](Brush-Artist-Refs-04-Henry-Ward-grey-cloud-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 32 % → 59 % | 48.9 px | 0.40 | 1.81 | 194 |
| stroke 2 | 38 % → 63 % | 57.9 px | 0.40 | 1.67 | 201 |
| stroke 3 | 59 % → 81 % | 80.6 px | 0.40 | 1.39 | 214 |
| stroke 4 | 58 % → 83 % | 87.2 px | 0.40 | 1.42 | 214 |
| stroke 5 | 61 % → 86 % | 90.5 px | 0.40 | 1.41 | 210 |
| stroke 6 | 61 % → 89 % | 97.9 px | 0.40 | 1.46 | 172 |
| stroke 7 | 60 % → 84 % | 88.1 px | 0.40 | 1.40 | 222 |
| stroke 8 | 57 % → 84 % | 85.6 px | 0.40 | 1.49 | 229 |
| stroke 9 | 60 % → 86 % | 88.4 px | 0.40 | 1.44 | 210 |
| stroke 10 | 61 % → 88 % | 98.0 px | 0.40 | 1.44 | 212 |
| stroke 11 | 61 % → 86 % | 83.0 px | 0.40 | 1.40 | 207 |
| stroke 12 | 62 % → 86 % | 94.5 px | 0.40 | 1.38 | 206 |
| stroke 13 | 61 % → 86 % | 84.2 px | 0.40 | 1.39 | 204 |
| stroke 14 | 60 % → 84 % | 93.1 px | 0.40 | 1.39 | 210 |
| stroke 15 | 60 % → 83 % | 87.9 px | 0.40 | 1.39 | 207 |
| stroke 16 | 61 % → 84 % | 95.9 px | 0.40 | 1.38 | 238 |
| stroke 17 | 60 % → 84 % | 83.8 px | 0.40 | 1.41 | 202 |
| stroke 18 | 61 % → 84 % | 96.5 px | 0.40 | 1.38 | 197 |
| stroke 19 | 60 % → 62 % | 89.4 px | 0.40 | 1.03 | 199 |
| stroke 20 | 61 % → 60 % | 99.3 px | 0.40 | 0.98 | 200 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #05 Henry Ward green in rust loops — own sheet
own sheet 600 × 600 · Heavy acrylic · 20 px · 2.3 s

![Brush Artist · Refs · #05 Henry Ward green in rust loops — own sheet](Brush-Artist-Refs-05-Henry-Ward-green-in-rust-loops-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 16 % → 24 % | 20.9 px | 0.02 | 1.48 | 106 |
| stroke 2 | 15 % → 13 % | 22.7 px | 0.03 | 0.90 | 145 |
| stroke 3 | 25 % → 24 % | 37.1 px | 0.02 | 0.94 | 111 |

## Brush Artist · Refs · #06 Henry Ward scrubbed grey — own sheet
own sheet 600 × 600 · Gouache · 50 px · 14.7 s

![Brush Artist · Refs · #06 Henry Ward scrubbed grey — own sheet](Brush-Artist-Refs-06-Henry-Ward-scrubbed-grey-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 34 % → 58 % | 48.6 px | 0.40 | 1.70 | 213 |
| stroke 2 | 41 % → 65 % | 64.3 px | 0.40 | 1.57 | 214 |
| stroke 3 | 58 % → 89 % | 85.6 px | 0.40 | 1.52 | 190 |
| stroke 4 | 58 % → 88 % | 92.7 px | 0.40 | 1.51 | 204 |
| stroke 5 | 56 % → 86 % | 83.8 px | 0.40 | 1.54 | 205 |
| stroke 6 | 60 % → 86 % | 92.9 px | 0.40 | 1.44 | 224 |
| stroke 7 | 61 % → 84 % | 88.3 px | 0.40 | 1.39 | 226 |
| stroke 8 | 62 % → 88 % | 98.0 px | 0.40 | 1.43 | 200 |
| stroke 9 | 60 % → 89 % | 88.3 px | 0.40 | 1.47 | 205 |
| stroke 10 | 59 % → 89 % | 95.3 px | 0.40 | 1.50 | 197 |
| stroke 11 | 59 % → 84 % | 85.7 px | 0.40 | 1.42 | 219 |
| stroke 12 | 58 % → 83 % | 93.2 px | 0.40 | 1.43 | 214 |
| stroke 13 | 58 % → 83 % | 82.8 px | 0.40 | 1.44 | 213 |
| stroke 14 | 56 % → 84 % | 84.7 px | 0.40 | 1.49 | 211 |
| stroke 15 | 58 % → 84 % | 82.8 px | 0.40 | 1.46 | 216 |
| stroke 16 | 62 % → 90 % | 96.4 px | 0.40 | 1.44 | 187 |
| stroke 17 | 61 % → 86 % | 88.4 px | 0.40 | 1.42 | 210 |
| stroke 18 | 61 % → 85 % | 95.3 px | 0.40 | 1.39 | 219 |
| stroke 19 | 57 % → 85 % | 86.8 px | 0.40 | 1.49 | 264 |
| stroke 20 | 58 % → 84 % | 93.2 px | 0.40 | 1.45 | 211 |
| stroke 21 | 58 % → 67 % | 84.2 px | 0.40 | 1.17 | 214 |
| stroke 22 | 62 % → 61 % | 98.0 px | 0.40 | 0.99 | 187 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #07 Henry Ward blue L + black zigzag — own sheet
own sheet 600 × 600 · Heavy acrylic · 34 px · 1.8 s

![Brush Artist · Refs · #07 Henry Ward blue L + black zigzag — own sheet](Brush-Artist-Refs-07-Henry-Ward-blue-L-black-zigzag-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 30 % → 31 % | 35.6 px | 0.59 | 1.05 | 108 |
| stroke 2 | 31 % → 29 % | 38.6 px | 0.59 | 0.94 | 86 |

## Brush Artist · Refs · #08 Henry Ward olive bands — own sheet
own sheet 600 × 600 · Gouache · 34 px · 5.3 s

![Brush Artist · Refs · #08 Henry Ward olive bands — own sheet](Brush-Artist-Refs-08-Henry-Ward-olive-bands-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 33 % → 19 % | 32.3 px | 0.57 | 0.58 | 161 |
| stroke 2 | 37 % → 20 % | 44.3 px | 0.57 | 0.53 | 150 |
| stroke 3 | 30 % → 23 % | 32.4 px | 0.57 | 0.75 | 169 |
| stroke 4 | 38 % → 37 % | 44.3 px | 0.57 | 0.98 | 164 |
| stroke 5 | 50 % → 35 % | 52.4 px | 0.57 | 0.71 | 160 |
| stroke 6 | 36 % → 22 % | 32.2 px | 0.57 | 0.61 | 156 |

## Brush Artist · Refs · #09 Henry Ward white loops — own sheet
own sheet 600 × 600 · Gouache · 46 px · 8.4 s

![Brush Artist · Refs · #09 Henry Ward white loops — own sheet](Brush-Artist-Refs-09-Henry-Ward-white-loops-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 50 % → 49 % | 15.7 px | 0.16 | 0.98 | 966 |
| stroke 2 | 53 % → 48 % | 36.9 px | 0.16 | 0.92 | 1005 |
| stroke 3 | 60 % → 53 % | 34.7 px | 0.17 | 0.89 | 945 |

## Brush Artist · Refs · #10 Henry Ward maroon loops — own sheet
own sheet 600 × 600 · Heavy acrylic · 30 px · 3.0 s

![Brush Artist · Refs · #10 Henry Ward maroon loops — own sheet](Brush-Artist-Refs-10-Henry-Ward-maroon-loops-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 16 % → 33 % | 28.6 px | 0.72 | 2.07 | 205 |
| stroke 2 | 29 % → 47 % | 46.0 px | 0.72 | 1.60 | 147 |
| stroke 3 | 40 % → 50 % | 54.7 px | 0.72 | 1.24 | 147 |
| stroke 4 | 45 % → 43 % | 64.1 px | 0.72 | 0.96 | 108 |
| stroke 5 | 41 % → 38 % | 70.6 px | 0.72 | 0.93 | 138 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #11 Henry Ward purple spun balls — own sheet
own sheet 600 × 600 · Heavy acrylic · 36 px · 2.6 s

![Brush Artist · Refs · #11 Henry Ward purple spun balls — own sheet](Brush-Artist-Refs-11-Henry-Ward-purple-spun-balls-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 45 % → 54 % | 26.5 px | 0.68 | 1.19 | 230 |
| stroke 2 | 53 % → 63 % | 31.1 px | 0.68 | 1.19 | 217 |
| stroke 3 | 55 % → 53 % | 32.4 px | 0.68 | 0.97 | 226 |

## Brush Artist · Refs · #12 Henry Ward black-olive cage — own sheet
own sheet 600 × 600 · Gouache · 28 px · 5.5 s

![Brush Artist · Refs · #12 Henry Ward black-olive cage — own sheet](Brush-Artist-Refs-12-Henry-Ward-black-olive-cage-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 18 % → 22 % | 24.3 px | 0.59 | 1.24 | 197 |
| stroke 2 | 16 % → 26 % | 27.7 px | 0.59 | 1.61 | 163 |
| stroke 3 | 34 % → 34 % | 40.4 px | 0.59 | 1.01 | 203 |
| stroke 4 | 34 % → 34 % | 42.8 px | 0.59 | 1.03 | 109 |
| stroke 5 | 34 % → 21 % | 43.1 px | 0.59 | 0.60 | 159 |
| stroke 6 | 52 % → 37 % | 67.3 px | 0.59 | 0.72 | 191 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #13 Henry Ward blue streaky form — own sheet
own sheet 600 × 600 · Gouache · 50 px · 14.1 s

![Brush Artist · Refs · #13 Henry Ward blue streaky form — own sheet](Brush-Artist-Refs-13-Henry-Ward-blue-streaky-form-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 34 % → 63 % | 48.7 px | 0.05 | 1.86 | 194 |
| stroke 2 | 42 % → 66 % | 67.0 px | 0.05 | 1.58 | 206 |
| stroke 3 | 60 % → 86 % | 84.5 px | 0.05 | 1.44 | 193 |
| stroke 4 | 59 % → 89 % | 97.5 px | 0.05 | 1.49 | 213 |
| stroke 5 | 60 % → 86 % | 86.3 px | 0.05 | 1.43 | 220 |
| stroke 6 | 56 % → 82 % | 85.8 px | 0.06 | 1.47 | 219 |
| stroke 7 | 61 % → 85 % | 91.6 px | 0.05 | 1.39 | 217 |
| stroke 8 | 62 % → 85 % | 96.1 px | 0.05 | 1.37 | 217 |
| stroke 9 | 62 % → 87 % | 94.2 px | 0.05 | 1.41 | 197 |
| stroke 10 | 63 % → 88 % | 102.2 px | 0.05 | 1.40 | 201 |
| stroke 11 | 58 % → 86 % | 87.0 px | 0.05 | 1.48 | 267 |
| stroke 12 | 57 % → 81 % | 90.8 px | 0.05 | 1.42 | 217 |
| stroke 13 | 61 % → 87 % | 89.2 px | 0.06 | 1.44 | 183 |
| stroke 14 | 54 % → 82 % | 83.5 px | 0.05 | 1.53 | 209 |
| stroke 15 | 57 % → 83 % | 81.6 px | 0.05 | 1.46 | 216 |
| stroke 16 | 56 % → 84 % | 90.2 px | 0.05 | 1.51 | 207 |
| stroke 17 | 61 % → 84 % | 93.2 px | 0.06 | 1.39 | 209 |
| stroke 18 | 61 % → 82 % | 95.0 px | 0.06 | 1.35 | 215 |
| stroke 19 | 67 % → 79 % | 84.1 px | 0.06 | 1.18 | 207 |
| stroke 20 | 78 % → 77 % | 92.8 px | 0.06 | 0.99 | 205 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #14 Henry Ward olive totem — own sheet
own sheet 600 × 600 · Heavy acrylic · 48 px · 6.4 s

![Brush Artist · Refs · #14 Henry Ward olive totem — own sheet](Brush-Artist-Refs-14-Henry-Ward-olive-totem-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 31 % → 50 % | 46.9 px | 0.38 | 1.58 | 124 |
| stroke 2 | 36 % → 62 % | 64.3 px | 0.38 | 1.71 | 112 |
| stroke 3 | 54 % → 76 % | 79.7 px | 0.38 | 1.42 | 131 |
| stroke 4 | 50 % → 73 % | 88.4 px | 0.38 | 1.46 | 122 |
| stroke 5 | 56 % → 78 % | 83.2 px | 0.38 | 1.39 | 126 |
| stroke 6 | 54 % → 81 % | 96.5 px | 0.38 | 1.50 | 133 |
| stroke 7 | 52 % → 75 % | 74.2 px | 0.38 | 1.45 | 125 |
| stroke 8 | 51 % → 77 % | 90.4 px | 0.38 | 1.53 | 132 |
| stroke 9 | 56 % → 81 % | 82.9 px | 0.38 | 1.44 | 126 |
| stroke 10 | 56 % → 78 % | 94.7 px | 0.38 | 1.40 | 131 |
| stroke 11 | 57 % → 79 % | 90.0 px | 0.38 | 1.38 | 131 |
| stroke 12 | 53 % → 80 % | 90.4 px | 0.38 | 1.53 | 133 |
| stroke 13 | 55 % → 83 % | 82.0 px | 0.38 | 1.51 | 115 |
| stroke 14 | 52 % → 76 % | 86.9 px | 0.38 | 1.48 | 146 |
| stroke 15 | 58 % → 82 % | 85.5 px | 0.38 | 1.41 | 124 |
| stroke 16 | 54 % → 80 % | 89.8 px | 0.38 | 1.47 | 127 |
| stroke 17 | 53 % → 78 % | 77.7 px | 0.38 | 1.45 | 133 |
| stroke 18 | 57 % → 84 % | 100.3 px | 0.38 | 1.47 | 165 |
| stroke 19 | 57 % → 80 % | 86.5 px | 0.38 | 1.41 | 122 |
| stroke 20 | 55 % → 76 % | 95.2 px | 0.38 | 1.40 | 133 |
| stroke 21 | 52 % → 67 % | 83.7 px | 0.37 | 1.30 | 125 |
| stroke 22 | 60 % → 59 % | 94.0 px | 0.37 | 0.98 | 127 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #15 Ultramarine brush script — own sheet
own sheet 600 × 600 · Ink · 6 px · 7.4 s

![Brush Artist · Refs · #15 Ultramarine brush script — own sheet](Brush-Artist-Refs-15-Ultramarine-brush-script-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 53 % → 59 % | 10.6 px | 0.71 | 1.12 | 33 |
| stroke 2 | 53 % → 59 % | 10.4 px | 0.68 | 1.10 | 57 |
| stroke 3 | 54 % → 61 % | 10.8 px | 0.70 | 1.13 | 36 |
| stroke 4 | 54 % → 59 % | 10.3 px | 0.65 | 1.09 | 60 |
| stroke 5 | 51 % → 55 % | 10.2 px | 0.66 | 1.08 | 57 |
| stroke 6 | 50 % → 57 % | 11.1 px | 0.72 | 1.13 | 29 |
| stroke 7 | 52 % → 57 % | 10.1 px | 0.66 | 1.10 | 63 |
| stroke 8 | 52 % → 59 % | 10.9 px | 0.70 | 1.12 | 43 |
| stroke 9 | 52 % → 57 % | 10.6 px | 0.68 | 1.10 | 52 |
| stroke 10 | 50 % → 55 % | 10.7 px | 0.70 | 1.10 | 43 |
| stroke 11 | 55 % → 61 % | 10.8 px | 0.70 | 1.11 | 40 |
| stroke 12 | 52 % → 57 % | 10.2 px | 0.65 | 1.08 | 67 |
| stroke 13 | 51 % → 56 % | 10.2 px | 0.66 | 1.09 | 64 |
| stroke 14 | 50 % → 57 % | 10.9 px | 0.72 | 1.14 | 22 |
| stroke 15 | 51 % → 58 % | 11.1 px | 0.72 | 1.14 | 24 |
| stroke 16 | 52 % → 58 % | 10.8 px | 0.70 | 1.10 | 39 |
| stroke 17 | 50 % → 56 % | 10.8 px | 0.72 | 1.13 | 31 |
| stroke 18 | 52 % → 58 % | 10.8 px | 0.70 | 1.11 | 36 |
| stroke 19 | 49 % → 56 % | 11.3 px | 0.72 | 1.14 | 30 |
| stroke 20 | 50 % → 56 % | 11.2 px | 0.73 | 1.13 | 30 |
| stroke 21 | 54 % → 58 % | 10.2 px | 0.66 | 1.07 | 53 |
| stroke 22 | 60 % → 65 % | 8.2 px | 0.68 | 1.10 | 53 |
| stroke 23 | 52 % → 58 % | 10.6 px | 0.69 | 1.11 | 51 |
| stroke 24 | 50 % → 56 % | 10.9 px | 0.72 | 1.13 | 29 |
| stroke 25 | 53 % → 58 % | 10.5 px | 0.68 | 1.08 | 58 |
| stroke 26 | 54 % → 59 % | 10.1 px | 0.65 | 1.09 | 60 |

## Brush Artist · Refs · #18 Blue oil-stick scribbles — own sheet
own sheet 600 × 600 · Pastel · 10 px · 2.8 s

![Brush Artist · Refs · #18 Blue oil-stick scribbles — own sheet](Brush-Artist-Refs-18-Blue-oil-stick-scribbles-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 18 % → 37 % | 3.8 px | 0.49 | 2.02 | 137 |
| stroke 2 | 16 % → 40 % | 3.6 px | 0.49 | 2.52 | 141 |
| stroke 3 | 18 % → 29 % | 5.8 px | 0.49 | 1.59 | 137 |
| stroke 4 | 17 % → 32 % | 7.8 px | 0.49 | 1.90 | 147 |
| stroke 5 | 32 % → 37 % | 7.8 px | 0.49 | 1.15 | 133 |
| stroke 6 | 30 % → 30 % | 9.2 px | 0.49 | 1.02 | 115 |
| stroke 7 | 28 % → 35 % | 7.5 px | 0.49 | 1.26 | 121 |
| stroke 8 | 33 % → 33 % | 16.3 px | 0.49 | 1.00 | 126 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #20 Orange-red crayon scribble — own sheet
own sheet 600 × 600 · Pastel · 14 px · 2.6 s

![Brush Artist · Refs · #20 Orange-red crayon scribble — own sheet](Brush-Artist-Refs-20-Orange-red-crayon-scribble-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 9 % → 20 % | 5.5 px | 0.59 | 2.30 | 236 |
| stroke 2 | 10 % → 25 % | 6.5 px | 0.59 | 2.49 | 155 |
| stroke 3 | 15 % → 25 % | 8.3 px | 0.59 | 1.61 | 139 |
| stroke 4 | 28 % → 35 % | 8.3 px | 0.59 | 1.25 | 142 |
| stroke 5 | 32 % → 32 % | 7.0 px | 0.59 | 1.00 | 141 |
| stroke 6 | 24 % → 24 % | 16.1 px | 0.59 | 1.00 | 147 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #21 Gritty black contours — own sheet
own sheet 600 × 600 · Gouache · 12 px · 4.0 s

![Brush Artist · Refs · #21 Gritty black contours — own sheet](Brush-Artist-Refs-21-Gritty-black-contours-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 12 % → 9 % | 10.6 px | 0.36 | 0.74 | 135 |
| stroke 2 | 10 % → 6 % | 14.1 px | 0.36 | 0.62 | 165 |
| stroke 3 | 18 % → 5 % | 12.5 px | 0.36 | 0.28 | 104 |
| stroke 4 | 19 % → 9 % | 18.4 px | 0.36 | 0.47 | 112 |
| stroke 5 | 19 % → 10 % | 17.9 px | 0.36 | 0.50 | 78 |

## Brush Artist · Refs · #22 Bold black brush poster — own sheet
own sheet 600 × 600 · Ink · 20 px · 4.7 s

![Brush Artist · Refs · #22 Bold black brush poster — own sheet](Brush-Artist-Refs-22-Bold-black-brush-poster-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 34 % → 37 % | 36.3 px | 0.94 | 1.10 | 102 |
| stroke 2 | 55 % → 66 % | 36.9 px | 0.95 | 1.21 | 24 |
| stroke 3 | 49 % → 49 % | 40.5 px | 0.94 | 1.00 | 49 |
| stroke 4 | 36 % → 43 % | 45.3 px | 0.94 | 1.20 | 47 |
| stroke 5 | 35 % → 35 % | 40.5 px | 0.94 | 1.00 | 85 |

## Brush Artist · Refs · #23 Dry white on orange + black line — own sheet
own sheet 600 × 600 · Gouache · 50 px · 9.3 s

![Brush Artist · Refs · #23 Dry white on orange + black line — own sheet](Brush-Artist-Refs-23-Dry-white-on-orange-black-line-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 26 % → 47 % | 44.0 px | 0.44 | 1.79 | 139 |
| stroke 2 | 31 % → 48 % | 53.3 px | 0.44 | 1.54 | 159 |
| stroke 3 | 50 % → 68 % | 81.7 px | 0.44 | 1.35 | 152 |
| stroke 4 | 48 % → 64 % | 87.6 px | 0.44 | 1.34 | 158 |
| stroke 5 | 50 % → 53 % | 76.7 px | 0.44 | 1.06 | 139 |
| stroke 6 | 49 % → 58 % | 93.3 px | 0.44 | 1.19 | 150 |
| stroke 7 | 39 % → 56 % | 66.4 px | 0.44 | 1.42 | 143 |
| stroke 8 | 41 % → 53 % | 74.2 px | 0.44 | 1.29 | 150 |
| stroke 9 | 51 % → 66 % | 83.2 px | 0.44 | 1.30 | 146 |
| stroke 10 | 54 % → 70 % | 96.3 px | 0.44 | 1.30 | 144 |
| stroke 11 | 49 % → 68 % | 80.7 px | 0.43 | 1.39 | 159 |
| stroke 12 | 49 % → 64 % | 88.4 px | 0.43 | 1.30 | 159 |
| stroke 13 | 52 % → 62 % | 84.2 px | 0.43 | 1.19 | 151 |
| stroke 14 | 48 % → 61 % | 89.7 px | 0.43 | 1.26 | 153 |
| stroke 15 | 49 % → 65 % | 78.9 px | 0.44 | 1.33 | 135 |
| stroke 16 | 46 % → 61 % | 84.9 px | 0.43 | 1.34 | 151 |
| stroke 17 | 46 % → 51 % | 77.0 px | 0.43 | 1.11 | 159 |
| stroke 18 | 55 % → 50 % | 102.5 px | 0.43 | 0.90 | 140 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #24 Picasso flat oil — own sheet
own sheet 600 × 600 · Oil · 34 px · 5.1 s

![Brush Artist · Refs · #24 Picasso flat oil — own sheet](Brush-Artist-Refs-24-Picasso-flat-oil-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 35 % → 60 % | 34.6 px | 0.24 | 1.73 | 125 |
| stroke 2 | 40 % → 66 % | 47.1 px | 0.23 | 1.65 | 120 |
| stroke 3 | 56 % → 84 % | 59.7 px | 0.23 | 1.50 | 122 |
| stroke 4 | 56 % → 82 % | 63.9 px | 0.23 | 1.47 | 131 |
| stroke 5 | 55 % → 86 % | 59.9 px | 0.23 | 1.56 | 126 |
| stroke 6 | 56 % → 85 % | 66.3 px | 0.23 | 1.52 | 122 |
| stroke 7 | 60 % → 75 % | 59.1 px | 0.23 | 1.23 | 121 |
| stroke 8 | 56 % → 72 % | 71.1 px | 0.23 | 1.28 | 118 |
| stroke 9 | 42 % → 67 % | 43.8 px | 0.23 | 1.61 | 120 |
| stroke 10 | 46 % → 69 % | 56.7 px | 0.23 | 1.49 | 129 |
| stroke 11 | 59 % → 73 % | 60.6 px | 0.23 | 1.24 | 126 |
| stroke 12 | 59 % → 78 % | 72.3 px | 0.23 | 1.31 | 120 |
| stroke 13 | 47 % → 72 % | 50.2 px | 0.23 | 1.55 | 128 |
| stroke 14 | 48 % → 75 % | 55.1 px | 0.23 | 1.54 | 123 |
| stroke 15 | 53 % → 82 % | 53.5 px | 0.23 | 1.56 | 121 |
| stroke 16 | 49 % → 78 % | 58.9 px | 0.23 | 1.59 | 145 |
| stroke 17 | 60 % → 71 % | 59.6 px | 0.23 | 1.18 | 120 |
| stroke 18 | 56 % → 56 % | 71.0 px | 0.23 | 1.00 | 134 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #25 Yellow heavy flat stroke — own sheet
own sheet 600 × 600 · Heavy acrylic · 110 px · 2.7 s

![Brush Artist · Refs · #25 Yellow heavy flat stroke — own sheet](Brush-Artist-Refs-25-Yellow-heavy-flat-stroke-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 35 % → 35 % | 104.2 px | 0.17 | 0.98 | 622 |

## Brush Artist · Refs · #27 Orange impasto swatch — own sheet
own sheet 600 × 600 · Heavy acrylic · 60 px · 2.9 s

![Brush Artist · Refs · #27 Orange impasto swatch — own sheet](Brush-Artist-Refs-27-Orange-impasto-swatch-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 23 % → 29 % | 61.8 px | 0.34 | 1.29 | 69 |
| stroke 2 | 19 % → 40 % | 62.5 px | 0.33 | 2.07 | 40 |
| stroke 3 | 26 % → 38 % | 94.9 px | 0.34 | 1.48 | 34 |
| stroke 4 | 22 % → 22 % | 62.5 px | 0.33 | 0.96 | 62 |
| stroke 5 | 32 % → 41 % | 62.2 px | 0.33 | 1.28 | 64 |
| stroke 6 | 39 % → 40 % | 112.2 px | 0.33 | 1.02 | 58 |
| stroke 7 | 19 % → 21 % | 63.8 px | 0.33 | 1.11 | 42 |
| stroke 8 | 42 % → 40 % | 143.3 px | 0.33 | 0.97 | 40 |
| stroke 9 | 49 % → 48 % | 97.7 px | 0.33 | 0.97 | 62 |
| stroke 10 | 28 % → 27 % | 87.2 px | 0.33 | 0.96 | 46 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #28 Miles Davis black lines — own sheet
own sheet 600 × 600 · Ink · 22 px · 5.7 s

![Brush Artist · Refs · #28 Miles Davis black lines — own sheet](Brush-Artist-Refs-28-Miles-Davis-black-lines-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 29 % → 36 % | 36.4 px | 0.88 | 1.26 | 161 |
| stroke 2 | 37 % → 57 % | 36.0 px | 0.88 | 1.52 | 122 |
| stroke 3 | 47 % → 48 % | 66.3 px | 0.88 | 1.02 | 90 |
| stroke 4 | 49 % → 58 % | 76.4 px | 0.88 | 1.16 | 149 |
| stroke 5 | 63 % → 64 % | 95.0 px | 0.88 | 1.00 | 115 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #29 Shrigley magenta asterisk — own sheet
own sheet 600 × 600 · Watercolor · 70 px · 5.8 s

![Brush Artist · Refs · #29 Shrigley magenta asterisk — own sheet](Brush-Artist-Refs-29-Shrigley-magenta-asterisk-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 25 % → 44 % | 46.6 px | 0.72 | 1.76 | 167 |
| stroke 2 | 17 % → 17 % | 86.5 px | 0.71 | 1.00 | 181 |
| stroke 3 | 37 % → 43 % | 69.5 px | 0.71 | 1.17 | 189 |
| stroke 4 | 32 % → 33 % | 162.9 px | 0.71 | 1.02 | 184 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #30 Red gouache face patch — own sheet
own sheet 600 × 600 · Gouache · 60 px · 10.5 s

![Brush Artist · Refs · #30 Red gouache face patch — own sheet](Brush-Artist-Refs-30-Red-gouache-face-patch-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 27 % → 51 % | 51.5 px | 0.53 | 1.89 | 152 |
| stroke 2 | 33 % → 57 % | 74.5 px | 0.53 | 1.74 | 147 |
| stroke 3 | 50 % → 77 % | 99.1 px | 0.53 | 1.54 | 147 |
| stroke 4 | 50 % → 77 % | 110.7 px | 0.53 | 1.54 | 177 |
| stroke 5 | 49 % → 78 % | 97.1 px | 0.53 | 1.61 | 165 |
| stroke 6 | 50 % → 80 % | 112.2 px | 0.53 | 1.59 | 162 |
| stroke 7 | 51 % → 78 % | 101.2 px | 0.53 | 1.53 | 168 |
| stroke 8 | 49 % → 76 % | 103.7 px | 0.53 | 1.55 | 166 |
| stroke 9 | 52 % → 80 % | 104.6 px | 0.53 | 1.53 | 155 |
| stroke 10 | 54 % → 76 % | 123.0 px | 0.53 | 1.39 | 150 |
| stroke 11 | 52 % → 74 % | 107.4 px | 0.53 | 1.43 | 155 |
| stroke 12 | 50 % → 74 % | 109.1 px | 0.53 | 1.48 | 157 |
| stroke 13 | 45 % → 72 % | 87.5 px | 0.53 | 1.61 | 150 |
| stroke 14 | 45 % → 63 % | 95.7 px | 0.53 | 1.42 | 211 |
| stroke 15 | 48 % → 58 % | 92.1 px | 0.53 | 1.21 | 165 |
| stroke 16 | 55 % → 54 % | 122.4 px | 0.53 | 0.99 | 163 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #31 Warhol blotted line — own sheet
own sheet 600 × 600 · Ink · 6 px · 4.6 s

![Brush Artist · Refs · #31 Warhol blotted line — own sheet](Brush-Artist-Refs-31-Warhol-blotted-line-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 24 % → 47 % | 15.7 px | 0.82 | 1.93 | 73 |
| stroke 2 | 19 % → 24 % | 15.8 px | 0.82 | 1.27 | 69 |
| stroke 3 | 27 % → 27 % | 24.7 px | 0.82 | 1.02 | 64 |
| stroke 4 | 31 % → 41 % | 27.9 px | 0.82 | 1.32 | 39 |
| stroke 5 | 38 % → 46 % | 34.7 px | 0.82 | 1.22 | 72 |
| stroke 6 | 35 % → 36 % | 25.2 px | 0.81 | 1.03 | 78 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #32 Thick orange swipes — own sheet
own sheet 600 × 600 · Heavy acrylic · 90 px · 3.5 s

![Brush Artist · Refs · #32 Thick orange swipes — own sheet](Brush-Artist-Refs-32-Thick-orange-swipes-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 28 % → 28 % | 86.0 px | 0.03 | 1.00 | 308 |
| stroke 2 | 29 % → 32 % | 89.3 px | 0.03 | 1.13 | 315 |
| stroke 3 | 32 % → 32 % | 102.9 px | 0.03 | 0.98 | 286 |

## Brush Artist · Refs · #33 Red wet-in-wet band — own sheet
own sheet 600 × 600 · Watercolor · 80 px · 6.8 s

![Brush Artist · Refs · #33 Red wet-in-wet band — own sheet](Brush-Artist-Refs-33-Red-wet-in-wet-band-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 43 % → 60 % | 88.2 px | 0.67 | 1.38 | 349 |
| stroke 2 | 47 % → 60 % | 169.5 px | 0.68 | 1.29 | 92 |
| stroke 3 | 59 % → 71 % | 225.1 px | 0.68 | 1.21 | 97 |
| stroke 4 | 60 % → 68 % | 219.0 px | 0.67 | 1.14 | 83 |
| stroke 5 | 54 % → 67 % | 191.1 px | 0.68 | 1.23 | 116 |
| stroke 6 | 59 % → 59 % | 205.6 px | 0.67 | 1.00 | 95 |

## Brush Artist · Refs · #34 Magenta oil patches — own sheet
own sheet 600 × 600 · Oil · 60 px · 4.3 s

![Brush Artist · Refs · #34 Magenta oil patches — own sheet](Brush-Artist-Refs-34-Magenta-oil-patches-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 24 % → 44 % | 61.9 px | 0.13 | 1.86 | 88 |
| stroke 2 | 22 % → 37 % | 62.8 px | 0.13 | 1.68 | 70 |
| stroke 3 | 21 % → 52 % | 62.3 px | 0.13 | 2.42 | 74 |
| stroke 4 | 31 % → 31 % | 97.0 px | 0.13 | 1.00 | 49 |
| stroke 5 | 28 % → 40 % | 61.7 px | 0.13 | 1.46 | 86 |
| stroke 6 | 27 % → 45 % | 80.2 px | 0.13 | 1.65 | 60 |
| stroke 7 | 29 % → 41 % | 82.2 px | 0.13 | 1.42 | 56 |
| stroke 8 | 52 % → 56 % | 134.7 px | 0.13 | 1.07 | 90 |
| stroke 9 | 34 % → 39 % | 87.4 px | 0.13 | 1.13 | 86 |
| stroke 10 | 48 % → 48 % | 152.6 px | 0.13 | 1.00 | 68 |
| stroke 11 | 61 % → 61 % | 185.1 px | 0.13 | 1.00 | 61 |
| stroke 12 | 35 % → 35 % | 104.1 px | 0.13 | 1.00 | 75 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #35 Red band with runs — own sheet
own sheet 600 × 600 · Watercolor · 70 px · 4.2 s

![Brush Artist · Refs · #35 Red band with runs — own sheet](Brush-Artist-Refs-35-Red-band-with-runs-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 39 % → 38 % | 77.5 px | 0.61 | 0.98 | 252 |

## Brush Artist · Refs · #36 Magenta letters flat brush — own sheet
own sheet 600 × 600 · Gouache · 36 px · 9.5 s

![Brush Artist · Refs · #36 Magenta letters flat brush — own sheet](Brush-Artist-Refs-36-Magenta-letters-flat-brush-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 46 % → 46 % | 59.1 px | 0.50 | 1.00 | 34 |
| stroke 2 | 38 % → 48 % | 39.7 px | 0.50 | 1.25 | 31 |
| stroke 3 | 56 % → 63 % | 72.2 px | 0.50 | 1.12 | 30 |
| stroke 4 | 45 % → 53 % | 44.9 px | 0.50 | 1.19 | 102 |
| stroke 5 | 41 % → 52 % | 61.1 px | 0.50 | 1.29 | 66 |
| stroke 6 | 78 % → 76 % | 153.6 px | 0.50 | 0.97 | 15 |
| stroke 7 | 43 % → 50 % | 42.1 px | 0.50 | 1.15 | 107 |
| stroke 8 | 39 % → 59 % | 63.5 px | 0.50 | 1.52 | 60 |
| stroke 9 | 54 % → 53 % | 82.8 px | 0.50 | 0.98 | 19 |
| stroke 10 | 42 % → 61 % | 63.1 px | 0.50 | 1.44 | 66 |
| stroke 11 | 78 % → 77 % | 153.6 px | 0.50 | 0.98 | 15 |
| stroke 12 | 58 % → 68 % | 57.2 px | 0.50 | 1.17 | 101 |
| stroke 13 | 43 % → 50 % | 58.9 px | 0.50 | 1.18 | 31 |
| stroke 14 | 52 % → 73 % | 74.9 px | 0.50 | 1.40 | 32 |
| stroke 15 | 44 % → 52 % | 66.5 px | 0.50 | 1.18 | 71 |
| stroke 16 | 78 % → 76 % | 153.3 px | 0.50 | 0.98 | 15 |
| stroke 17 | 53 % → 61 % | 51.3 px | 0.50 | 1.15 | 104 |
| stroke 18 | 40 % → 47 % | 54.9 px | 0.50 | 1.17 | 28 |
| stroke 19 | 65 % → 63 % | 81.6 px | 0.50 | 0.97 | 27 |
| stroke 20 | 56 % → 54 % | 70.5 px | 0.50 | 0.97 | 28 |
| stroke 21 | 47 % → 46 % | 53.9 px | 0.50 | 0.96 | 80 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #37 Oil still life dabs — own sheet
own sheet 600 × 600 · Oil · 40 px · 3.3 s

![Brush Artist · Refs · #37 Oil still life dabs — own sheet](Brush-Artist-Refs-37-Oil-still-life-dabs-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 20 % → 20 % | 44.0 px | 0.39 | 1.00 | 28 |
| stroke 2 | 18 % → 48 % | 44.4 px | 0.39 | 2.65 | 22 |
| stroke 3 | 23 % → 48 % | 59.8 px | 0.38 | 2.12 | 17 |
| stroke 4 | 22 % → 22 % | 42.7 px | 0.39 | 1.00 | 39 |
| stroke 5 | 17 % → 18 % | 43.2 px | 0.39 | 1.04 | 19 |
| stroke 6 | 37 % → 45 % | 83.3 px | 0.39 | 1.24 | 25 |
| stroke 7 | 16 % → 27 % | 54.8 px | 0.39 | 1.71 | 13 |
| stroke 8 | 14 % → 29 % | 47.9 px | 0.39 | 2.08 | 16 |
| stroke 9 | 23 % → 23 % | 43.9 px | 0.39 | 1.00 | 30 |
| stroke 10 | 31 % → 37 % | 58.3 px | 0.39 | 1.18 | 30 |
| stroke 11 | 39 % → 39 % | 109.7 px | 0.39 | 1.00 | 18 |
| stroke 12 | 31 % → 31 % | 109.5 px | 0.40 | 1.00 | 9 |
| stroke 13 | 17 % → 17 % | 59.0 px | 0.39 | 1.00 | 11 |
| stroke 14 | 35 % → 35 % | 91.9 px | 0.39 | 1.00 | 17 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #38 Sanguine drawing — own sheet
own sheet 600 × 600 · Pastel · 6 px · 2.1 s

![Brush Artist · Refs · #38 Sanguine drawing — own sheet](Brush-Artist-Refs-38-Sanguine-drawing-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 3 % → 14 % | 2.9 px | 0.57 | 4.35 | 4 |
| stroke 2 | 3 % → 7 % | 2.9 px | 0.57 | 2.23 | 8 |
| stroke 3 | 3 % → 9 % | 2.9 px | 0.57 | 2.76 | 7 |
| stroke 4 | 3 % → 19 % | 2.7 px | 0.57 | 6.27 | 3 |
| stroke 5 | 3 % → 8 % | 2.7 px | 0.57 | 2.71 | 7 |
| stroke 6 | 3 % → 20 % | 3.0 px | 0.57 | 6.20 | 8 |
| stroke 7 | 5 % → 15 % | 4.7 px | 0.57 | 2.84 | 3 |
| stroke 8 | 4 % → 15 % | 3.9 px | 0.57 | 3.43 | 7 |
| stroke 9 | 3 % → 7 % | 2.9 px | 0.57 | 2.30 | 6 |
| stroke 10 | 4 % → 17 % | 4.0 px | 0.57 | 3.83 | 4 |
| stroke 11 | 3 % → 5 % | 2.9 px | 0.57 | 1.49 | 3 |
| stroke 12 | 5 % → 16 % | 4.5 px | 0.57 | 3.20 | 7 |
| stroke 13 | 8 % → 18 % | 7.8 px | 0.57 | 2.10 | 8 |
| stroke 14 | 5 % → 15 % | 4.5 px | 0.57 | 2.96 | 6 |
| stroke 15 | 10 % → 18 % | 9.5 px | 0.57 | 1.71 | 3 |
| stroke 16 | 6 % → 16 % | 5.4 px | 0.57 | 2.74 | 4 |
| stroke 17 | 4 % → 9 % | 4.0 px | 0.57 | 2.07 | 3 |
| stroke 18 | 3 % → 5 % | 2.9 px | 0.57 | 1.68 | 8 |
| stroke 19 | 7 % → 17 % | 6.0 px | 0.57 | 2.63 | 6 |
| stroke 20 | 8 % → 15 % | 7.8 px | 0.57 | 1.72 | 3 |
| stroke 21 | 4 % → 4 % | 4.0 px | 0.57 | 1.00 | 7 |
| stroke 22 | 9 % → 14 % | 7.8 px | 0.58 | 1.66 | 3 |
| stroke 23 | 8 % → 12 % | 7.0 px | 0.57 | 1.52 | 6 |
| stroke 24 | 4 % → 7 % | 3.9 px | 0.57 | 1.55 | 3 |
| stroke 25 | 8 % → 15 % | 7.3 px | 0.57 | 1.86 | 7 |
| stroke 26 | 6 % → 8 % | 5.7 px | 0.57 | 1.26 | 3 |
| stroke 27 | 4 % → 4 % | 3.8 px | 0.57 | 1.05 | 7 |
| stroke 28 | 8 % → 12 % | 7.0 px | 0.57 | 1.56 | 3 |
| stroke 29 | 8 % → 17 % | 6.9 px | 0.57 | 2.22 | 4 |
| stroke 30 | 14 % → 18 % | 13.1 px | 0.57 | 1.25 | 5 |
| stroke 31 | 6 % → 7 % | 5.2 px | 0.57 | 1.23 | 8 |
| stroke 32 | 12 % → 13 % | 10.5 px | 0.57 | 1.15 | 6 |
| stroke 33 | 7 % → 8 % | 6.6 px | 0.57 | 1.06 | 4 |
| stroke 34 | 11 % → 14 % | 10.2 px | 0.57 | 1.28 | 7 |
| stroke 35 | 9 % → 15 % | 8.6 px | 0.57 | 1.56 | 3 |
| stroke 36 | 11 % → 13 % | 9.8 px | 0.57 | 1.27 | 6 |
| stroke 37 | 11 % → 17 % | 9.8 px | 0.57 | 1.64 | 4 |
| stroke 38 | 14 % → 21 % | 12.4 px | 0.57 | 1.51 | 6 |
| stroke 39 | 15 % → 18 % | 13.6 px | 0.57 | 1.22 | 5 |
| stroke 40 | 6 % → 7 % | 5.3 px | 0.57 | 1.16 | 3 |
| stroke 41 | 17 % → 17 % | 15.3 px | 0.57 | 1.00 | 6 |
| stroke 42 | 14 % → 16 % | 12.6 px | 0.57 | 1.16 | 3 |
| stroke 43 | 11 % → 13 % | 10.0 px | 0.57 | 1.18 | 7 |
| stroke 44 | 13 % → 16 % | 11.6 px | 0.57 | 1.23 | 7 |
| stroke 45 | 3 % → 3 % | 2.6 px | 0.57 | 1.00 | 3 |
| stroke 46 | 17 % → 17 % | 15.6 px | 0.57 | 1.00 | 5 |
| stroke 47 | 14 % → 14 % | 13.1 px | 0.57 | 1.00 | 4 |
| stroke 48 | 13 % → 14 % | 12.4 px | 0.58 | 1.04 | 4 |
| stroke 49 | 20 % → 20 % | 18.3 px | 0.57 | 1.00 | 6 |
| stroke 50 | 10 % → 10 % | 9.5 px | 0.57 | 1.00 | 4 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #39 Very thick impasto — own sheet
own sheet 600 × 600 · Heavy acrylic · 60 px · 4.1 s

![Brush Artist · Refs · #39 Very thick impasto — own sheet](Brush-Artist-Refs-39-Very-thick-impasto-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 38 % → 37 % | 59.5 px | 0.43 | 0.97 | 265 |
| stroke 2 | 37 % → 40 % | 59.6 px | 0.43 | 1.08 | 281 |
| stroke 3 | 40 % → 39 % | 72.0 px | 0.44 | 0.97 | 249 |
| stroke 4 | 39 % → 38 % | 59.6 px | 0.43 | 0.97 | 280 |
| stroke 5 | 35 % → 34 % | 59.7 px | 0.43 | 0.97 | 257 |

## Brush Artist · Refs · #40 Watercolour blooms — own sheet
own sheet 600 × 600 · Watercolor · 90 px · 5.2 s

![Brush Artist · Refs · #40 Watercolour blooms — own sheet](Brush-Artist-Refs-40-Watercolour-blooms-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 39 % → 38 % | 92.4 px | 0.15 | 0.98 | 671 |

## Brush Artist · Refs · #41 Coloured pencil hatching — own sheet
own sheet 600 × 600 · Pastel · 4 px · 2.3 s

![Brush Artist · Refs · #41 Coloured pencil hatching — own sheet](Brush-Artist-Refs-41-Coloured-pencil-hatching-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 3 % → 14 % | 2.2 px | 0.35 | 4.12 | 6 |
| stroke 2 | 4 % → 7 % | 2.3 px | 0.35 | 1.98 | 3 |
| stroke 3 | 3 % → 11 % | 1.9 px | 0.35 | 3.77 | 5 |
| stroke 4 | 3 % → 20 % | 2.1 px | 0.35 | 5.90 | 2 |
| stroke 5 | 4 % → 7 % | 2.8 px | 0.35 | 1.51 | 2 |
| stroke 6 | 4 % → 13 % | 2.3 px | 0.35 | 3.60 | 2 |
| stroke 7 | 4 % → 15 % | 2.5 px | 0.35 | 3.75 | 5 |
| stroke 8 | 3 % → 12 % | 2.1 px | 0.35 | 3.44 | 4 |
| stroke 9 | 6 % → 12 % | 3.4 px | 0.35 | 2.11 | 2 |
| stroke 10 | 5 % → 16 % | 3.2 px | 0.35 | 3.19 | 2 |
| stroke 11 | 4 % → 13 % | 2.7 px | 0.35 | 3.02 | 5 |
| stroke 12 | 3 % → 3 % | 2.1 px | 0.35 | 1.00 | 2 |
| stroke 13 | 7 % → 16 % | 4.7 px | 0.35 | 2.23 | 2 |
| stroke 14 | 4 % → 14 % | 2.3 px | 0.35 | 3.93 | 2 |
| stroke 15 | 7 % → 13 % | 4.3 px | 0.35 | 1.90 | 5 |
| stroke 16 | 7 % → 11 % | 4.7 px | 0.35 | 1.48 | 5 |
| stroke 17 | 3 % → 3 % | 2.1 px | 0.35 | 1.00 | 2 |
| stroke 18 | 5 % → 8 % | 3.2 px | 0.35 | 1.69 | 4 |
| stroke 19 | 6 % → 14 % | 3.6 px | 0.35 | 2.41 | 3 |
| stroke 20 | 6 % → 16 % | 3.5 px | 0.35 | 2.81 | 2 |
| stroke 21 | 5 % → 15 % | 3.0 px | 0.35 | 3.16 | 2 |
| stroke 22 | 10 % → 17 % | 6.4 px | 0.35 | 1.73 | 2 |
| stroke 23 | 9 % → 13 % | 5.9 px | 0.35 | 1.42 | 5 |
| stroke 24 | 7 % → 14 % | 4.1 px | 0.35 | 2.18 | 2 |
| stroke 25 | 5 % → 10 % | 3.3 px | 0.35 | 2.03 | 3 |
| stroke 26 | 4 % → 6 % | 2.5 px | 0.35 | 1.47 | 2 |
| stroke 27 | 3 % → 7 % | 2.2 px | 0.35 | 2.01 | 6 |
| stroke 28 | 6 % → 9 % | 3.9 px | 0.35 | 1.53 | 3 |
| stroke 29 | 4 % → 15 % | 2.4 px | 0.35 | 3.85 | 2 |
| stroke 30 | 6 % → 9 % | 3.9 px | 0.35 | 1.47 | 4 |
| stroke 31 | 7 % → 15 % | 4.6 px | 0.35 | 2.08 | 4 |
| stroke 32 | 4 % → 7 % | 2.4 px | 0.35 | 1.80 | 2 |
| stroke 33 | 7 % → 11 % | 4.3 px | 0.35 | 1.66 | 2 |
| stroke 34 | 4 % → 6 % | 2.5 px | 0.35 | 1.53 | 4 |
| stroke 35 | 7 % → 14 % | 4.4 px | 0.35 | 2.05 | 7 |
| stroke 36 | 6 % → 6 % | 3.5 px | 0.35 | 1.00 | 2 |
| stroke 37 | 7 % → 15 % | 4.6 px | 0.35 | 2.02 | 3 |
| stroke 38 | 8 % → 13 % | 5.3 px | 0.35 | 1.59 | 3 |
| stroke 39 | 7 % → 12 % | 4.7 px | 0.35 | 1.59 | 2 |
| stroke 40 | 8 % → 19 % | 5.2 px | 0.35 | 2.28 | 4 |
| stroke 41 | 9 % → 13 % | 5.9 px | 0.35 | 1.38 | 2 |
| stroke 42 | 10 % → 18 % | 6.5 px | 0.35 | 1.77 | 4 |
| stroke 43 | 5 % → 8 % | 3.2 px | 0.35 | 1.64 | 2 |
| stroke 44 | 11 % → 15 % | 6.8 px | 0.35 | 1.36 | 3 |
| stroke 45 | 13 % → 18 % | 8.4 px | 0.35 | 1.36 | 5 |
| stroke 46 | 5 % → 7 % | 3.4 px | 0.34 | 1.26 | 3 |
| stroke 47 | 11 % → 13 % | 6.8 px | 0.35 | 1.20 | 2 |
| stroke 48 | 13 % → 17 % | 8.1 px | 0.35 | 1.34 | 4 |
| stroke 49 | 5 % → 9 % | 3.4 px | 0.35 | 1.77 | 2 |
| stroke 50 | 7 % → 7 % | 4.6 px | 0.34 | 1.00 | 4 |
| stroke 51 | 10 % → 17 % | 6.1 px | 0.35 | 1.73 | 2 |
| stroke 52 | 13 % → 16 % | 8.3 px | 0.35 | 1.20 | 2 |
| stroke 53 | 11 % → 15 % | 6.8 px | 0.35 | 1.37 | 5 |
| stroke 54 | 10 % → 15 % | 6.5 px | 0.35 | 1.49 | 2 |
| stroke 55 | 11 % → 14 % | 7.0 px | 0.35 | 1.30 | 3 |
| stroke 56 | 11 % → 13 % | 7.3 px | 0.35 | 1.10 | 4 |
| stroke 57 | 10 % → 14 % | 6.5 px | 0.35 | 1.37 | 5 |
| stroke 58 | 11 % → 13 % | 7.1 px | 0.35 | 1.14 | 4 |
| stroke 59 | 12 % → 14 % | 7.6 px | 0.35 | 1.15 | 4 |
| stroke 60 | 16 % → 20 % | 10.0 px | 0.35 | 1.29 | 5 |
| stroke 61 | 20 % → 21 % | 12.9 px | 0.35 | 1.02 | 3 |
| stroke 62 | 10 % → 10 % | 6.4 px | 0.35 | 1.00 | 4 |
| stroke 63 | 12 % → 13 % | 7.7 px | 0.35 | 1.06 | 6 |
| stroke 64 | 16 % → 16 % | 9.9 px | 0.35 | 1.02 | 2 |
| stroke 65 | 16 % → 16 % | 10.4 px | 0.35 | 1.00 | 5 |
| stroke 66 | 14 % → 14 % | 8.9 px | 0.35 | 1.00 | 5 |
| stroke 67 | 13 % → 13 % | 7.9 px | 0.35 | 1.04 | 2 |
| stroke 68 | 5 % → 9 % | 3.1 px | 0.35 | 1.90 | 5 |
| stroke 69 | 6 % → 6 % | 3.9 px | 0.35 | 1.00 | 2 |
| stroke 70 | 11 % → 13 % | 6.7 px | 0.35 | 1.27 | 7 |
| stroke 71 | 10 % → 12 % | 6.4 px | 0.35 | 1.15 | 5 |
| stroke 72 | 6 % → 7 % | 3.6 px | 0.35 | 1.17 | 2 |
| stroke 73 | 13 % → 13 % | 8.4 px | 0.35 | 1.00 | 6 |
| stroke 74 | 15 % → 15 % | 9.5 px | 0.35 | 1.00 | 2 |
| stroke 75 | 16 % → 16 % | 10.2 px | 0.35 | 1.00 | 2 |
| stroke 76 | 14 % → 14 % | 9.1 px | 0.35 | 1.00 | 5 |
| stroke 77 | 7 % → 10 % | 4.3 px | 0.35 | 1.38 | 5 |
| stroke 78 | 10 % → 10 % | 6.2 px | 0.35 | 1.00 | 2 |
| stroke 79 | 8 % → 8 % | 4.9 px | 0.35 | 1.00 | 5 |
| stroke 80 | 12 % → 12 % | 7.3 px | 0.35 | 1.00 | 2 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #42 Oil pastel shaggy — own sheet
own sheet 600 × 600 · Pastel · 18 px · 2.5 s

![Brush Artist · Refs · #42 Oil pastel shaggy — own sheet](Brush-Artist-Refs-42-Oil-pastel-shaggy-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 9 % → 20 % | 8.0 px | 0.28 | 2.21 | 13 |
| stroke 2 | 10 % → 26 % | 8.6 px | 0.28 | 2.58 | 6 |
| stroke 3 | 10 % → 33 % | 8.9 px | 0.29 | 3.29 | 10 |
| stroke 4 | 10 % → 21 % | 8.8 px | 0.28 | 2.08 | 13 |
| stroke 5 | 11 % → 21 % | 9.9 px | 0.28 | 1.84 | 11 |
| stroke 6 | 10 % → 31 % | 9.1 px | 0.29 | 3.00 | 6 |
| stroke 7 | 14 % → 40 % | 12.6 px | 0.28 | 2.79 | 6 |
| stroke 8 | 11 % → 44 % | 9.5 px | 0.28 | 3.98 | 11 |
| stroke 9 | 13 % → 22 % | 11.5 px | 0.28 | 1.69 | 7 |
| stroke 10 | 11 % → 19 % | 9.5 px | 0.28 | 1.77 | 6 |
| stroke 11 | 10 % → 28 % | 9.0 px | 0.28 | 2.72 | 12 |
| stroke 12 | 14 % → 19 % | 12.3 px | 0.28 | 1.36 | 6 |
| stroke 13 | 19 % → 30 % | 16.7 px | 0.28 | 1.60 | 11 |
| stroke 14 | 9 % → 20 % | 7.9 px | 0.28 | 2.25 | 12 |
| stroke 15 | 10 % → 36 % | 9.0 px | 0.29 | 3.51 | 6 |
| stroke 16 | 16 % → 34 % | 14.4 px | 0.29 | 2.06 | 10 |
| stroke 17 | 21 % → 39 % | 18.6 px | 0.28 | 1.82 | 7 |
| stroke 18 | 25 % → 35 % | 21.6 px | 0.29 | 1.42 | 6 |
| stroke 19 | 22 % → 40 % | 19.1 px | 0.28 | 1.79 | 8 |
| stroke 20 | 23 % → 42 % | 19.9 px | 0.28 | 1.81 | 9 |
| stroke 21 | 14 % → 20 % | 12.7 px | 0.28 | 1.41 | 10 |
| stroke 22 | 14 % → 16 % | 12.0 px | 0.28 | 1.14 | 6 |
| stroke 23 | 20 % → 27 % | 17.3 px | 0.29 | 1.34 | 6 |
| stroke 24 | 30 % → 35 % | 26.0 px | 0.30 | 1.20 | 10 |
| stroke 25 | 20 % → 33 % | 17.4 px | 0.28 | 1.67 | 10 |
| stroke 26 | 11 % → 22 % | 9.2 px | 0.28 | 2.04 | 6 |
| stroke 27 | 31 % → 36 % | 27.6 px | 0.29 | 1.15 | 12 |
| stroke 28 | 19 % → 30 % | 16.5 px | 0.28 | 1.60 | 11 |
| stroke 29 | 11 % → 29 % | 9.4 px | 0.29 | 2.75 | 7 |
| stroke 30 | 14 % → 38 % | 11.9 px | 0.29 | 2.79 | 12 |
| stroke 31 | 16 % → 16 % | 13.9 px | 0.28 | 1.00 | 12 |
| stroke 32 | 20 % → 33 % | 17.2 px | 0.29 | 1.70 | 6 |
| stroke 33 | 20 % → 21 % | 17.6 px | 0.29 | 1.03 | 10 |
| stroke 34 | 30 % → 36 % | 26.0 px | 0.28 | 1.20 | 10 |
| stroke 35 | 29 % → 37 % | 25.2 px | 0.28 | 1.27 | 7 |
| stroke 36 | 25 % → 27 % | 22.0 px | 0.28 | 1.05 | 10 |
| stroke 37 | 21 % → 21 % | 17.9 px | 0.28 | 1.00 | 6 |
| stroke 38 | 29 % → 34 % | 24.6 px | 0.28 | 1.20 | 9 |
| stroke 39 | 15 % → 25 % | 13.2 px | 0.28 | 1.64 | 6 |
| stroke 40 | 34 % → 41 % | 29.5 px | 0.28 | 1.21 | 7 |
| stroke 41 | 32 % → 34 % | 28.3 px | 0.28 | 1.04 | 10 |
| stroke 42 | 21 % → 30 % | 18.8 px | 0.28 | 1.39 | 8 |
| stroke 43 | 14 % → 14 % | 12.4 px | 0.28 | 1.00 | 6 |
| stroke 44 | 29 % → 39 % | 25.3 px | 0.28 | 1.35 | 6 |
| stroke 45 | 25 % → 25 % | 21.7 px | 0.28 | 1.00 | 12 |
| stroke 46 | 40 % → 45 % | 34.6 px | 0.29 | 1.12 | 11 |
| stroke 47 | 38 % → 45 % | 33.1 px | 0.28 | 1.17 | 6 |
| stroke 48 | 27 % → 30 % | 23.5 px | 0.29 | 1.12 | 8 |
| stroke 49 | 32 % → 34 % | 27.9 px | 0.29 | 1.06 | 6 |
| stroke 50 | 39 % → 42 % | 34.1 px | 0.28 | 1.08 | 12 |
| stroke 51 | 20 % → 20 % | 17.4 px | 0.29 | 1.00 | 11 |
| stroke 52 | 37 % → 37 % | 32.1 px | 0.29 | 1.00 | 10 |
| stroke 53 | 23 % → 23 % | 19.8 px | 0.28 | 1.02 | 6 |
| stroke 54 | 28 % → 31 % | 24.4 px | 0.29 | 1.10 | 12 |
| stroke 55 | 17 % → 17 % | 14.6 px | 0.28 | 1.00 | 12 |
| stroke 56 | 21 % → 21 % | 18.2 px | 0.28 | 1.00 | 7 |
| stroke 57 | 36 % → 36 % | 31.3 px | 0.29 | 1.00 | 18 |
| stroke 58 | 29 % → 29 % | 25.3 px | 0.28 | 1.00 | 6 |
| stroke 59 | 50 % → 50 % | 43.8 px | 0.28 | 1.00 | 10 |
| stroke 60 | 19 % → 19 % | 16.5 px | 0.28 | 1.00 | 11 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #43 Dragged black ink blocks — own sheet
own sheet 600 × 600 · Gouache · 70 px · 7.3 s

![Brush Artist · Refs · #43 Dragged black ink blocks — own sheet](Brush-Artist-Refs-43-Dragged-black-ink-blocks-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 46 % → 28 % | 66.4 px | 0.42 | 0.62 | 392 |
| stroke 2 | 35 % → 22 % | 66.2 px | 0.42 | 0.62 | 419 |
| stroke 3 | 36 % → 25 % | 67.5 px | 0.42 | 0.69 | 394 |
| stroke 4 | 39 % → 24 % | 71.3 px | 0.42 | 0.60 | 416 |
| stroke 5 | 43 % → 29 % | 66.4 px | 0.42 | 0.66 | 421 |

## Brush Artist · Refs · #44 Blue looping ribbon — own sheet
own sheet 600 × 600 · Oil · 80 px · 5.5 s

![Brush Artist · Refs · #44 Blue looping ribbon — own sheet](Brush-Artist-Refs-44-Blue-looping-ribbon-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 48 % → 48 % | 42.2 px | 0.78 | 1.00 | 2365 |

## Brush Artist · Refs · #45 Soft pastel pepper — own sheet
own sheet 600 × 600 · Pastel · 40 px · 3.0 s

![Brush Artist · Refs · #45 Soft pastel pepper — own sheet](Brush-Artist-Refs-45-Soft-pastel-pepper-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 15 % → 33 % | 11.3 px | 0.49 | 2.20 | 287 |
| stroke 2 | 25 % → 37 % | 20.6 px | 0.49 | 1.47 | 271 |
| stroke 3 | 34 % → 42 % | 13.8 px | 0.49 | 1.25 | 269 |
| stroke 4 | 32 % → 36 % | 27.8 px | 0.49 | 1.13 | 297 |
| stroke 5 | 37 % → 37 % | 13.9 px | 0.49 | 1.00 | 201 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #46 Red-brown ink lips — own sheet
own sheet 600 × 600 · Watercolor · 70 px · 4.6 s

![Brush Artist · Refs · #46 Red-brown ink lips — own sheet](Brush-Artist-Refs-46-Red-brown-ink-lips-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 28 % → 40 % | 73.4 px | 0.73 | 1.39 | 186 |
| stroke 2 | 44 % → 44 % | 114.4 px | 0.73 | 1.00 | 162 |

## Brush Artist · Refs · #47 Pink knife slabs — own sheet
own sheet 600 × 600 · Heavy acrylic · 90 px · 4.1 s

![Brush Artist · Refs · #47 Pink knife slabs — own sheet](Brush-Artist-Refs-47-Pink-knife-slabs-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 28 % → 34 % | 83.2 px | 0.11 | 1.18 | 269 |
| stroke 2 | 36 % → 41 % | 106.4 px | 0.11 | 1.13 | 243 |
| stroke 3 | 36 % → 41 % | 106.3 px | 0.11 | 1.14 | 270 |
| stroke 4 | 37 % → 36 % | 106.4 px | 0.11 | 0.97 | 267 |

## Brush Artist · Refs · #48 Black bands with drips — own sheet
own sheet 600 × 600 · Gouache · 70 px · 7.6 s

![Brush Artist · Refs · #48 Black bands with drips — own sheet](Brush-Artist-Refs-48-Black-bands-with-drips-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 33 % → 30 % | 59.2 px | 0.39 | 0.91 | 449 |
| stroke 2 | 35 % → 32 % | 58.2 px | 0.39 | 0.92 | 460 |
| stroke 3 | 33 % → 31 % | 58.3 px | 0.39 | 0.94 | 438 |
| stroke 4 | 33 % → 32 % | 58.2 px | 0.39 | 0.95 | 446 |

## Brush Artist · Refs · #49 Magenta letters round brush — own sheet
own sheet 600 × 600 · Ink · 30 px · 7.0 s

![Brush Artist · Refs · #49 Magenta letters round brush — own sheet](Brush-Artist-Refs-49-Magenta-letters-round-brush-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 61 % → 65 % | 64.3 px | 0.52 | 1.06 | 35 |
| stroke 2 | 59 % → 63 % | 52.0 px | 0.53 | 1.07 | 28 |
| stroke 3 | 71 % → 80 % | 74.2 px | 0.53 | 1.13 | 31 |
| stroke 4 | 54 % → 64 % | 48.0 px | 0.52 | 1.18 | 99 |
| stroke 5 | 48 % → 65 % | 63.0 px | 0.52 | 1.35 | 67 |
| stroke 6 | 93 % → 94 % | 141.0 px | 0.53 | 1.01 | 16 |
| stroke 7 | 61 % → 70 % | 51.9 px | 0.52 | 1.14 | 106 |
| stroke 8 | 44 % → 72 % | 63.4 px | 0.53 | 1.61 | 62 |
| stroke 9 | 71 % → 71 % | 86.0 px | 0.53 | 1.00 | 25 |
| stroke 10 | 51 % → 72 % | 66.5 px | 0.52 | 1.42 | 73 |
| stroke 11 | 93 % → 94 % | 140.9 px | 0.53 | 1.01 | 17 |
| stroke 12 | 71 % → 83 % | 60.6 px | 0.52 | 1.18 | 124 |
| stroke 13 | 61 % → 65 % | 67.4 px | 0.53 | 1.05 | 36 |
| stroke 14 | 69 % → 92 % | 78.6 px | 0.53 | 1.33 | 27 |
| stroke 15 | 52 % → 63 % | 68.8 px | 0.52 | 1.20 | 68 |
| stroke 16 | 93 % → 93 % | 140.9 px | 0.53 | 1.00 | 14 |
| stroke 17 | 68 % → 76 % | 58.1 px | 0.52 | 1.12 | 121 |
| stroke 18 | 59 % → 62 % | 64.6 px | 0.52 | 1.05 | 38 |
| stroke 19 | 81 % → 80 % | 82.3 px | 0.53 | 0.99 | 26 |
| stroke 20 | 71 % → 70 % | 72.0 px | 0.52 | 1.00 | 25 |
| stroke 21 | 59 % → 59 % | 61.0 px | 0.52 | 1.00 | 84 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #50 Thick swipes on photo — own sheet
own sheet 600 × 600 · Heavy acrylic · 40 px · 2.7 s

![Brush Artist · Refs · #50 Thick swipes on photo — own sheet](Brush-Artist-Refs-50-Thick-swipes-on-photo-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 24 % → 27 % | 42.6 px | 0.32 | 1.12 | 30 |
| stroke 2 | 21 % → 28 % | 42.4 px | 0.33 | 1.33 | 31 |
| stroke 3 | 26 % → 24 % | 41.8 px | 0.33 | 0.95 | 42 |
| stroke 4 | 26 % → 24 % | 42.6 px | 0.33 | 0.94 | 30 |
| stroke 5 | 24 % → 22 % | 41.8 px | 0.33 | 0.95 | 37 |
| stroke 6 | 21 % → 19 % | 42.9 px | 0.33 | 0.94 | 25 |
| stroke 7 | 36 % → 37 % | 59.4 px | 0.33 | 1.02 | 38 |
| stroke 8 | 34 % → 33 % | 66.7 px | 0.32 | 0.97 | 32 |
| stroke 9 | 25 % → 23 % | 42.0 px | 0.33 | 0.95 | 27 |
| stroke 10 | 28 % → 27 % | 42.2 px | 0.33 | 0.95 | 28 |
| stroke 11 | 23 % → 21 % | 42.6 px | 0.33 | 0.95 | 32 |
| stroke 12 | 24 % → 23 % | 53.2 px | 0.33 | 0.95 | 17 |

## Brush Artist · Ink — dry brush — own sheet
own sheet 600 × 600 · Gouache · 30 px · 2.8 s

![Brush Artist · Ink — dry brush — own sheet](Brush-Artist-Ink-dry-brush-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| ear | 17 % → 4 % | 16.7 px | 0.82 | 0.24 | 463 |
| drag0 | 20 % → 24 % | 25.0 px | 0.82 | 1.22 | 117 |
| drag1 | 25 % → 25 % | 34.2 px | 0.82 | 1.02 | 112 |
| drag2 | 28 % → 25 % | 42.1 px | 0.82 | 0.92 | 81 |
| drag3 | 30 % → 26 % | 50.2 px | 0.82 | 0.87 | 70 |

## Brush Artist · Watercolour — blue — own sheet
own sheet 600 × 600 · Watercolor · 40 px · 6.7 s

![Brush Artist · Watercolour — blue — own sheet](Brush-Artist-Watercolour-blue-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| s0 | 14 % → 28 % | 28.4 px | 0.28 | 2.04 | 39 |
| s1 | 8 % → 36 % | 9.9 px | 0.40 | 4.46 | 34 |
| s2 | 12 % → 21 % | 28.5 px | 0.16 | 1.74 | 35 |
| s3 | 11 % → 18 % | 20.3 px | 0.26 | 1.68 | 44 |
| s4 | 17 % → 34 % | 36.6 px | 0.38 | 1.96 | 55 |
| s5 | 25 % → 33 % | 34.0 px | 0.35 | 1.32 | 39 |
| s6 | 25 % → 30 % | 39.5 px | 0.28 | 1.23 | 49 |
| s7 | 27 % → 34 % | 18.5 px | 0.42 | 1.28 | 30 |
| s8 | 21 % → 25 % | 44.1 px | 0.22 | 1.19 | 35 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Charcoal — stick — own sheet
own sheet 600 × 600 · Charcoal · 28 px · 0.9 s

![Brush Artist · Charcoal — stick — own sheet](Brush-Artist-Charcoal-stick-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| finger0 | 16 % → 21 % | 15.5 px | 0.83 | 1.33 | 18 |
| tip0 | 15 % → 22 % | 18.4 px | 0.83 | 1.47 | 6 |
| finger1 | 16 % → 26 % | 15.7 px | 0.83 | 1.64 | 24 |
| tip1 | 20 % → 27 % | 24.8 px | 0.83 | 1.34 | 8 |
| finger2 | 16 % → 24 % | 16.0 px | 0.83 | 1.45 | 16 |
| tip2 | 20 % → 27 % | 24.1 px | 0.83 | 1.34 | 5 |
| finger3 | 16 % → 18 % | 16.1 px | 0.83 | 1.12 | 20 |
| tip3 | 20 % → 20 % | 24.3 px | 0.83 | 1.00 | 5 |
| cig0 | 38 % → 50 % | 35.5 px | 0.83 | 1.32 | 6 |
| cig1 | 42 % → 55 % | 39.5 px | 0.83 | 1.30 | 6 |
| cig2 | 47 % → 60 % | 44.1 px | 0.83 | 1.27 | 8 |
| cig3 | 51 % → 60 % | 47.1 px | 0.83 | 1.20 | 6 |
| cig4 | 50 % → 55 % | 46.8 px | 0.83 | 1.10 | 8 |
| cig5 | 51 % → 51 % | 47.1 px | 0.83 | 1.00 | 11 |

Numbers say: wet paint spreads well beyond the stroke.

