![All brushes](contact.png)

# Brush Lab — 147 brushes · 3 Nov 2026 at 19:31

Every sheet: 1500 × 600, ten strokes in a 5 × 2 grid — 1. light line · 2. heavy line · 3. pressure swell · 4. fast wave · 5. slow wave · 6. spiral · 7. loop · 8. tilted · 9. over the wet one · 10. long, no reload (cell 8 holds «tilted» and «over the wet one» crossed). The CPU reference of Mamay's paint engine; the wet layer settles 20 s at the end.

Columns: **covered** = share of the cell with paint right after the stroke → after settling; **width** = painted area of the stroke ÷ its length (px); **dark** = mean darkness of the painted pixels above the paper's own grain (0 = paper, 1 = black); **spread** = how far wet paint went beyond the stroke (1.0 = stayed); **ms** = the stroke on the CPU; long stroke: paint in each quarter of its length (it should run out: wet → streaks → dry tail).

## Ink Line
Ink · 12 px · 22.9 s

![Ink Line](Ink-Line.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 1 % → 4 % | 4.3 px | 0.55 | 2.44 | 25 |
| heavy line | 5 % → 6 % | 15.7 px | 0.68 | 1.13 | 71 |
| pressure swell | 3 % → 4 % | 11.3 px | 0.64 | 1.40 | 34 |
| fast wave | 10 % → 11 % | 11.2 px | 0.59 | 1.11 | 123 |
| slow wave | 8 % → 10 % | 9.6 px | 0.57 | 1.16 | 114 |
| spiral | 14 % → 15 % | 8.9 px | 0.50 | 1.07 | 153 |
| loop | 8 % → 9 % | 10.6 px | 0.61 | 1.16 | 87 |
| tilted | 5 % → 5 % | 14.4 px | 0.65 | 1.05 | 48 |
| over the wet one | 10 % → 11 % | 12.5 px | 0.65 | 1.15 | 48 |
| long, no reload | 18 % → 17 % | 8.1 px | 0.47 | 0.96 | 251 | quarters: 0.22 → 0.09 → 0.04 → 0.02

Numbers say: light vs heavy: width 4.3 → 15.7 px, dark 0.55 → 0.68; wet paint spreads well beyond the stroke.

## Dense Ink
Ink · 14 px · 23.3 s

![Dense Ink](Dense-Ink.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 5 % → 7 % | 15.2 px | 0.72 | 1.26 | 32 |
| heavy line | 7 % → 7 % | 19.1 px | 0.73 | 1.09 | 72 |
| pressure swell | 5 % → 6 % | 17.9 px | 0.72 | 1.17 | 40 |
| fast wave | 13 % → 13 % | 15.3 px | 0.69 | 1.01 | 124 |
| slow wave | 12 % → 12 % | 13.6 px | 0.67 | 1.04 | 130 |
| spiral | 18 % → 15 % | 12.2 px | 0.65 | 0.80 | 210 |
| loop | 11 % → 12 % | 14.8 px | 0.69 | 1.08 | 106 |
| tilted | 5 % → 6 % | 14.6 px | 0.72 | 1.07 | 54 |
| over the wet one | 12 % → 13 % | 17.7 px | 0.72 | 1.11 | 44 |
| long, no reload | 23 % → 15 % | 10.1 px | 0.64 | 0.66 | 273 | quarters: 0.30 → 0.12 → 0.04 → 0.02

Numbers say: light vs heavy: width 15.2 → 19.1 px, dark 0.72 → 0.73.

## Transparent Wash
Watercolor · 22 px · 24.1 s

![Transparent Wash](Transparent-Wash.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 2 % → 5 % | 6.9 px | 0.27 | 2.25 | 52 |
| heavy line | 7 % → 9 % | 20.4 px | 0.27 | 1.22 | 61 |
| pressure swell | 4 % → 6 % | 15.2 px | 0.28 | 1.54 | 27 |
| fast wave | 14 % → 16 % | 16.1 px | 0.20 | 1.17 | 88 |
| slow wave | 12 % → 15 % | 13.7 px | 0.21 | 1.28 | 176 |
| spiral | 18 % → 22 % | 11.9 px | 0.16 | 1.23 | 140 |
| loop | 11 % → 13 % | 14.5 px | 0.22 | 1.20 | 83 |
| tilted | 8 % → 8 % | 21.1 px | 0.24 | 1.06 | 47 |
| over the wet one | 13 % → 16 % | 16.4 px | 0.24 | 1.18 | 41 |
| long, no reload | 26 % → 32 % | 11.6 px | 0.13 | 1.22 | 250 | quarters: 0.11 → 0.04 → 0.02 → 0.01

Numbers say: light vs heavy: width 6.9 → 20.4 px, dark 0.27 → 0.27; wet paint spreads well beyond the stroke.

## Dry Brush
Gouache · 24 px · 19.2 s

![Dry Brush](Dry-Brush.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 5 % → 0 % | 14.0 px | 0.65 | 0.09 | 77 |
| heavy line | 6 % → 0 % | 18.6 px | 0.65 | 0.02 | 84 |
| pressure swell | 5 % → 0 % | 18.2 px | 0.65 | 0.08 | 48 |
| fast wave | 6 % → 1 % | 7.3 px | 0.65 | 0.08 | 128 |
| slow wave | 7 % → 0 % | 8.1 px | 0.65 | 0.06 | 208 |
| spiral | 7 % → 0 % | 4.6 px | 0.65 | 0.07 | 201 |
| loop | 10 % → 0 % | 12.4 px | 0.65 | 0.04 | 103 |
| tilted | 4 % → 3 % | 10.6 px | 0.65 | 0.88 | 62 |
| over the wet one | 9 % → 1 % | 14.5 px | 0.65 | 0.12 | 68 |
| long, no reload | 6 % → 1 % | 2.9 px | 0.65 | 0.14 | 301 | quarters: 0.12 → 0.00 → 0.00 → 0.00

Numbers say: light vs heavy: width 14.0 → 18.6 px, dark 0.65 → 0.65.

## Wax Crayon
Wax · 8 px · 9.0 s

![Wax Crayon](Wax-Crayon.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 1 % → 1 % | 2.5 px | 0.71 | 1.00 | 14 |
| heavy line | 1 % → 1 % | 3.9 px | 0.69 | 1.00 | 10 |
| pressure swell | 1 % → 1 % | 3.3 px | 0.70 | 1.00 | 9 |
| fast wave | 3 % → 3 % | 3.5 px | 0.69 | 1.00 | 53 |
| slow wave | 3 % → 3 % | 3.4 px | 0.70 | 1.00 | 43 |
| spiral | 5 % → 5 % | 3.3 px | 0.70 | 1.00 | 86 |
| loop | 3 % → 3 % | 3.3 px | 0.70 | 1.00 | 37 |
| tilted | 2 % → 2 % | 5.6 px | 0.68 | 1.00 | 27 |
| over the wet one | 3 % → 3 % | 3.6 px | 0.68 | 1.00 | 9 |
| long, no reload | 7 % → 7 % | 3.3 px | 0.70 | 1.00 | 109 | quarters: 0.06 → 0.06 → 0.06 → 0.06

Numbers say: light vs heavy: width 2.5 → 3.9 px, dark 0.71 → 0.69; the long stroke does not run out of paint.

## Oil Pastel
Wax · 12 px · 9.2 s

![Oil Pastel](Oil-Pastel.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 1 % → 1 % | 4.0 px | 0.68 | 1.00 | 44 |
| heavy line | 2 % → 2 % | 6.5 px | 0.68 | 1.00 | 22 |
| pressure swell | 2 % → 2 % | 5.7 px | 0.69 | 1.00 | 16 |
| fast wave | 5 % → 5 % | 5.7 px | 0.68 | 1.00 | 48 |
| slow wave | 5 % → 5 % | 5.5 px | 0.68 | 1.00 | 56 |
| spiral | 8 % → 8 % | 5.5 px | 0.68 | 1.00 | 98 |
| loop | 4 % → 4 % | 5.6 px | 0.68 | 1.00 | 43 |
| tilted | 2 % → 2 % | 6.8 px | 0.68 | 1.00 | 39 |
| over the wet one | 5 % → 5 % | 5.8 px | 0.68 | 1.00 | 15 |
| long, no reload | 13 % → 13 % | 5.6 px | 0.68 | 1.00 | 150 | quarters: 0.10 → 0.09 → 0.10 → 0.10

Numbers say: light vs heavy: width 4.0 → 6.5 px, dark 0.68 → 0.68; the long stroke does not run out of paint.

## Charcoal
Charcoal · 5 px · 8.8 s

![Charcoal](Charcoal.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 1 % → 1 % | 2.0 px | 0.74 | 1.00 | 30 |
| heavy line | 1 % → 1 % | 3.0 px | 0.74 | 1.00 | 9 |
| pressure swell | 1 % → 1 % | 2.7 px | 0.74 | 1.00 | 6 |
| fast wave | 2 % → 2 % | 2.7 px | 0.73 | 1.00 | 30 |
| slow wave | 2 % → 2 % | 2.6 px | 0.74 | 1.00 | 25 |
| spiral | 4 % → 4 % | 2.5 px | 0.74 | 1.00 | 61 |
| loop | 2 % → 2 % | 2.6 px | 0.74 | 1.00 | 31 |
| tilted | 2 % → 2 % | 4.3 px | 0.72 | 1.00 | 19 |
| over the wet one | 2 % → 2 % | 2.4 px | 0.72 | 1.00 | 16 |
| long, no reload | 6 % → 6 % | 2.7 px | 0.73 | 1.00 | 71 | quarters: 0.05 → 0.05 → 0.05 → 0.05

Numbers say: light vs heavy: width 2.0 → 3.0 px, dark 0.74 → 0.74; the long stroke does not run out of paint.

## Impasto
Heavy acrylic · 22 px · 13.5 s

![Impasto](Impasto.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 8 % → 8 % | 24.1 px | 0.71 | 0.93 | 79 |
| heavy line | 10 % → 9 % | 28.8 px | 0.70 | 0.94 | 88 |
| pressure swell | 7 % → 7 % | 28.1 px | 0.72 | 0.94 | 45 |
| fast wave | 20 % → 13 % | 23.5 px | 0.71 | 0.64 | 157 |
| slow wave | 21 % → 14 % | 24.5 px | 0.71 | 0.66 | 216 |
| spiral | 30 % → 14 % | 20.0 px | 0.71 | 0.46 | 246 |
| loop | 18 % → 14 % | 23.9 px | 0.71 | 0.77 | 121 |
| tilted | 8 % → 8 % | 21.8 px | 0.70 | 1.00 | 74 |
| over the wet one | 17 % → 15 % | 25.4 px | 0.70 | 0.91 | 58 |
| long, no reload | 34 % → 14 % | 15.2 px | 0.71 | 0.41 | 361 | quarters: 0.38 → 0.21 → 0.10 → 0.03

Numbers say: light vs heavy: width 24.1 → 28.8 px, dark 0.71 → 0.70.

## Oil Round
Oil · 18 px · 16.1 s

![Oil Round](Oil-Round.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 2 % → 2 % | 7.2 px | 0.75 | 1.00 | 37 |
| heavy line | 7 % → 7 % | 19.3 px | 0.73 | 1.00 | 44 |
| pressure swell | 4 % → 4 % | 13.7 px | 0.72 | 1.00 | 43 |
| fast wave | 11 % → 11 % | 12.7 px | 0.65 | 1.00 | 136 |
| slow wave | 8 % → 8 % | 9.0 px | 0.57 | 1.00 | 128 |
| spiral | 10 % → 10 % | 6.6 px | 0.50 | 1.00 | 204 |
| loop | 5 % → 5 % | 7.1 px | 0.45 | 1.00 | 77 |
| tilted | 4 % → 4 % | 10.1 px | 0.52 | 1.00 | 52 |
| over the wet one | 6 % → 6 % | 7.4 px | 0.52 | 1.00 | 56 |
| long, no reload | 15 % → 15 % | 6.8 px | 0.42 | 1.00 | 302 | quarters: 0.08 → 0.08 → 0.07 → 0.06

Numbers say: light vs heavy: width 7.2 → 19.3 px, dark 0.75 → 0.73.

## Palette Knife
Oil · 20 px · 15.5 s

![Palette Knife](Palette-Knife.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 8 % → 8 % | 21.9 px | 0.67 | 1.00 | 13 |
| heavy line | 8 % → 8 % | 22.5 px | 0.73 | 1.00 | 23 |
| pressure swell | 6 % → 6 % | 22.4 px | 0.74 | 1.00 | 9 |
| fast wave | 17 % → 17 % | 19.3 px | 0.49 | 1.00 | 21 |
| slow wave | 17 % → 17 % | 19.9 px | 0.43 | 1.00 | 31 |
| spiral | 18 % → 18 % | 11.7 px | 0.45 | 1.00 | 55 |
| loop | 16 % → 16 % | 21.0 px | 0.58 | 1.00 | 24 |
| tilted | 5 % → 5 % | 15.0 px | 0.72 | 1.00 | 9 |
| over the wet one | 13 % → 13 % | 21.0 px | 0.72 | 1.00 | 6 |
| long, no reload | 17 % → 17 % | 7.5 px | 0.47 | 1.00 | 59 | quarters: 0.29 → 0.05 → 0.00 → 0.00

Numbers say: light vs heavy: width 21.9 → 22.5 px, dark 0.67 → 0.73; pressure barely changes the width.

## Water
Watercolor · 20 px · 33.2 s · over bands of wet oil paint and oil pastel in turn (it works on paint already there: look at what it does to the bands; covered counts the bands too)

![Water](Water.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 25 % → 27 % | 73.8 px | 0.80 | 1.06 | 21 |
| heavy line | 24 % → 25 % | 69.8 px | 0.81 | 1.04 | 46 |
| pressure swell | 24 % → 25 % | 89.6 px | 0.81 | 1.03 | 26 |
| fast wave | 24 % → 26 % | 27.7 px | 0.81 | 1.07 | 98 |
| slow wave | 24 % → 25 % | 27.7 px | 0.81 | 1.06 | 131 |
| spiral | 24 % → 26 % | 15.9 px | 0.81 | 1.07 | 156 |
| loop | 24 % → 25 % | 31.1 px | 0.81 | 1.03 | 87 |
| tilted | 24 % → 24 % | 67.0 px | 0.81 | 1.00 | 55 |
| over the wet one | 24 % → 25 % | 0.0 px | 0.81 | 1.06 | 37 |
| long, no reload | 24 % → 26 % | 10.7 px | 0.81 | 1.08 | 231 | quarters: 0.21 → 0.27 → 0.18 → 0.27

Numbers say: light vs heavy: width 73.8 → 69.8 px, dark 0.80 → 0.81; pressure barely changes the width; the long stroke does not run out of paint.

## Blender
Pastel · 16 px · 18.5 s · over bands of wet oil paint and oil pastel in turn (it works on paint already there: look at what it does to the bands; covered counts the bands too)

![Blender](Blender.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 24 % → 24 % | 70.7 px | 0.81 | 1.00 | 12 |
| heavy line | 25 % → 25 % | 72.1 px | 0.80 | 1.00 | 30 |
| pressure swell | 24 % → 24 % | 91.3 px | 0.81 | 1.00 | 20 |
| fast wave | 26 % → 26 % | 30.0 px | 0.79 | 1.00 | 64 |
| slow wave | 26 % → 26 % | 29.9 px | 0.80 | 1.00 | 86 |
| spiral | 28 % → 28 % | 18.7 px | 0.77 | 1.00 | 100 |
| loop | 25 % → 25 % | 32.9 px | 0.80 | 1.00 | 52 |
| tilted | 25 % → 25 % | 70.1 px | 0.79 | 1.00 | 31 |
| over the wet one | 26 % → 26 % | 1.8 px | 0.79 | 1.00 | 37 |
| long, no reload | 30 % → 30 % | 13.7 px | 0.76 | 1.00 | 172 | quarters: 0.20 → 0.28 → 0.23 → 0.30

Numbers say: light vs heavy: width 70.7 → 72.1 px, dark 0.81 → 0.80; pressure barely changes the width; the long stroke does not run out of paint.

## Eraser
Eraser · 16 px · 18.4 s · over bands of wet oil paint and oil pastel in turn (it works on paint already there: look at what it does to the bands; covered counts the bands too)

![Eraser](Eraser.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 24 % → 24 % | 69.5 px | 0.82 | 1.00 | 13 |
| heavy line | 23 % → 23 % | 67.9 px | 0.82 | 1.00 | 29 |
| pressure swell | 23 % → 23 % | 87.3 px | 0.82 | 1.00 | 18 |
| fast wave | 22 % → 22 % | 25.7 px | 0.82 | 1.00 | 60 |
| slow wave | 22 % → 22 % | 25.7 px | 0.82 | 1.00 | 81 |
| spiral | 22 % → 22 % | 14.4 px | 0.82 | 1.00 | 90 |
| loop | 22 % → 22 % | 28.6 px | 0.82 | 1.00 | 69 |
| tilted | 23 % → 23 % | 65.1 px | 0.82 | 1.00 | 42 |
| over the wet one | 23 % → 23 % | 0.0 px | 0.82 | 1.00 | 28 |
| long, no reload | 20 % → 20 % | 8.9 px | 0.82 | 1.00 | 186 | quarters: 0.15 → 0.20 → 0.15 → 0.20

Numbers say: light vs heavy: width 69.5 → 67.9 px, dark 0.82 → 0.82; pressure barely changes the width; the long stroke does not run out of paint.

## Fan
Gouache · 30 px · 27.3 s

![Fan](Fan.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 9 % → 3 % | 25.7 px | 0.63 | 0.37 | 27 |
| heavy line | 11 % → 4 % | 31.0 px | 0.63 | 0.39 | 47 |
| pressure swell | 8 % → 5 % | 31.7 px | 0.63 | 0.55 | 29 |
| fast wave | 18 % → 5 % | 20.3 px | 0.63 | 0.26 | 83 |
| slow wave | 18 % → 5 % | 21.1 px | 0.63 | 0.25 | 158 |
| spiral | 24 % → 5 % | 15.8 px | 0.63 | 0.20 | 142 |
| loop | 17 % → 5 % | 22.7 px | 0.63 | 0.29 | 96 |
| tilted | 5 % → 6 % | 15.1 px | 0.63 | 1.05 | 44 |
| over the wet one | 16 % → 8 % | 29.8 px | 0.63 | 0.50 | 44 |
| long, no reload | 23 % → 5 % | 10.1 px | 0.63 | 0.22 | 242 | quarters: 0.29 → 0.07 → 0.01 → 0.00

Numbers say: light vs heavy: width 25.7 → 31.0 px, dark 0.63 → 0.63.

## Sponge
Gouache · 30 px · 27.0 s

![Sponge](Sponge.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 4 % → 0 % | 11.4 px | 0.62 | 0.12 | 29 |
| heavy line | 12 % → 2 % | 35.4 px | 0.62 | 0.14 | 59 |
| pressure swell | 7 % → 2 % | 27.9 px | 0.62 | 0.27 | 38 |
| fast wave | 20 % → 4 % | 23.2 px | 0.62 | 0.19 | 116 |
| slow wave | 21 % → 4 % | 23.7 px | 0.62 | 0.18 | 212 |
| spiral | 28 % → 4 % | 18.3 px | 0.62 | 0.14 | 170 |
| loop | 18 % → 5 % | 23.0 px | 0.62 | 0.29 | 84 |
| tilted | 7 % → 7 % | 18.2 px | 0.62 | 1.04 | 92 |
| over the wet one | 16 % → 6 % | 27.8 px | 0.62 | 0.37 | 49 |
| long, no reload | 29 % → 5 % | 12.9 px | 0.62 | 0.17 | 262 | quarters: 0.29 → 0.13 → 0.07 → 0.04

Numbers say: light vs heavy: width 11.4 → 35.4 px, dark 0.62 → 0.62.

## Ink — sumi brush
Watercolor · 22 px · 27.2 s

![Ink — sumi brush](Ink-sumi-brush.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 8 % → 9 % | 23.8 px | 0.77 | 1.13 | 44 |
| heavy line | 13 % → 13 % | 38.0 px | 0.72 | 1.01 | 51 |
| pressure swell | 9 % → 10 % | 34.5 px | 0.75 | 1.05 | 47 |
| fast wave | 27 % → 28 % | 31.7 px | 0.58 | 1.03 | 149 |
| slow wave | 25 % → 26 % | 29.0 px | 0.61 | 1.05 | 239 |
| spiral | 37 % → 38 % | 24.3 px | 0.51 | 1.03 | 248 |
| loop | 22 % → 22 % | 28.2 px | 0.66 | 1.03 | 138 |
| tilted | 9 % → 9 % | 24.7 px | 0.73 | 1.03 | 58 |
| over the wet one | 20 % → 21 % | 31.1 px | 0.73 | 1.03 | 58 |
| long, no reload | 42 % → 43 % | 18.9 px | 0.46 | 1.02 | 359 | quarters: 0.47 → 0.23 → 0.11 → 0.06

Numbers say: light vs heavy: width 23.8 → 38.0 px, dark 0.77 → 0.72.

## Ink — wash
Watercolor · 40 px · 30.2 s

![Ink — wash](Ink-wash.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 13 % → 13 % | 36.5 px | 0.17 | 1.04 | 72 |
| heavy line | 18 % → 19 % | 53.5 px | 0.13 | 1.04 | 77 |
| pressure swell | 12 % → 13 % | 46.6 px | 0.16 | 1.05 | 51 |
| fast wave | 40 % → 42 % | 45.9 px | 0.12 | 1.06 | 211 |
| slow wave | 38 % → 40 % | 43.6 px | 0.17 | 1.06 | 330 |
| spiral | 58 % → 62 % | 38.5 px | 0.12 | 1.06 | 328 |
| loop | 33 % → 34 % | 42.9 px | 0.15 | 1.03 | 167 |
| tilted | 14 % → 14 % | 38.1 px | 0.17 | 1.03 | 101 |
| over the wet one | 29 % → 31 % | 43.2 px | 0.17 | 1.06 | 73 |
| long, no reload | 66 % → 75 % | 29.8 px | 0.12 | 1.12 | 470 | quarters: 0.16 → 0.11 → 0.07 → 0.04

Numbers say: light vs heavy: width 36.5 → 53.5 px, dark 0.17 → 0.13.

## Ink — dry brush
Ink · 30 px · 23.0 s

![Ink — dry brush](Ink-dry-brush.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 9 % → 7 % | 25.2 px | 0.81 | 0.79 | 82 |
| heavy line | 10 % → 8 % | 29.6 px | 0.80 | 0.76 | 112 |
| pressure swell | 7 % → 6 % | 27.9 px | 0.81 | 0.85 | 61 |
| fast wave | 21 % → 8 % | 24.2 px | 0.79 | 0.40 | 218 |
| slow wave | 18 % → 7 % | 20.3 px | 0.79 | 0.39 | 352 |
| spiral | 24 % → 8 % | 15.6 px | 0.78 | 0.34 | 384 |
| loop | 19 % → 8 % | 24.3 px | 0.78 | 0.45 | 194 |
| tilted | 8 % → 8 % | 22.2 px | 0.78 | 1.02 | 157 |
| over the wet one | 17 % → 14 % | 25.9 px | 0.78 | 0.81 | 87 |
| long, no reload | 20 % → 8 % | 9.1 px | 0.79 | 0.41 | 506 | quarters: 0.32 → 0.02 → 0.00 → 0.00

Numbers say: light vs heavy: width 25.2 → 29.6 px, dark 0.81 → 0.80.

## Ink — nib
Watercolor · 5 px · 22.1 s

![Ink — nib](Ink-nib.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 2 % → 5 % | 5.4 px | 0.86 | 2.45 | 21 |
| heavy line | 2 % → 5 % | 6.4 px | 0.86 | 2.33 | 32 |
| pressure swell | 2 % → 4 % | 6.2 px | 0.86 | 2.52 | 12 |
| fast wave | 5 % → 8 % | 5.8 px | 0.82 | 1.65 | 59 |
| slow wave | 5 % → 8 % | 5.6 px | 0.82 | 1.73 | 51 |
| spiral | 7 % → 11 % | 4.8 px | 0.75 | 1.45 | 96 |
| loop | 4 % → 8 % | 5.6 px | 0.84 | 1.75 | 57 |
| tilted | 4 % → 4 % | 10.1 px | 0.85 | 1.04 | 33 |
| over the wet one | 6 % → 9 % | 6.3 px | 0.85 | 1.61 | 24 |
| long, no reload | 9 % → 12 % | 4.0 px | 0.70 | 1.37 | 140 | quarters: 0.23 → 0.08 → 0.04 → 0.02

Numbers say: light vs heavy: width 5.4 → 6.4 px, dark 0.86 → 0.86; wet paint spreads well beyond the stroke.

## 0.45 · Dry brush
Gouache · 34 px · 23.6 s

![0.45 · Dry brush](0-45-Dry-brush.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 10 % → 3 % | 29.4 px | 0.67 | 0.29 | 98 |
| heavy line | 11 % → 3 % | 31.6 px | 0.67 | 0.30 | 111 |
| pressure swell | 8 % → 3 % | 31.5 px | 0.67 | 0.41 | 67 |
| fast wave | 19 % → 3 % | 22.5 px | 0.67 | 0.18 | 253 |
| slow wave | 20 % → 4 % | 23.2 px | 0.67 | 0.18 | 462 |
| spiral | 21 % → 3 % | 14.1 px | 0.67 | 0.16 | 479 |
| loop | 20 % → 4 % | 26.1 px | 0.67 | 0.20 | 243 |
| tilted | 9 % → 8 % | 24.0 px | 0.67 | 0.98 | 122 |
| over the wet one | 19 % → 6 % | 28.2 px | 0.67 | 0.34 | 115 |
| long, no reload | 20 % → 4 % | 9.1 px | 0.67 | 0.19 | 648 | quarters: 0.36 → 0.10 → 0.00 → 0.00

Numbers say: light vs heavy: width 29.4 → 31.6 px, dark 0.67 → 0.67; pressure barely changes the width.

## Dry pastel
Pastel · 26 px · 9.9 s

![Dry pastel](Dry-pastel.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 3 % → 3 % | 8.3 px | 0.38 | 1.00 | 30 |
| heavy line | 5 % → 5 % | 13.2 px | 0.39 | 1.00 | 29 |
| pressure swell | 3 % → 3 % | 11.7 px | 0.38 | 1.00 | 20 |
| fast wave | 10 % → 10 % | 11.9 px | 0.39 | 1.00 | 91 |
| slow wave | 10 % → 10 % | 11.3 px | 0.39 | 1.00 | 129 |
| spiral | 15 % → 15 % | 9.6 px | 0.39 | 1.00 | 167 |
| loop | 7 % → 7 % | 9.4 px | 0.39 | 1.00 | 82 |
| tilted | 3 % → 3 % | 8.3 px | 0.38 | 1.00 | 40 |
| over the wet one | 7 % → 7 % | 11.1 px | 0.38 | 1.00 | 31 |
| long, no reload | 18 % → 18 % | 8.2 px | 0.39 | 1.00 | 229 | quarters: 0.08 → 0.08 → 0.08 → 0.07

Numbers say: light vs heavy: width 8.3 → 13.2 px, dark 0.38 → 0.39; the long stroke does not run out of paint.

## 0.45 · Charcoal
Charcoal · 18 px · 9.5 s

![0.45 · Charcoal](0-45-Charcoal.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 2 % → 2 % | 6.5 px | 0.80 | 1.00 | 26 |
| heavy line | 3 % → 3 % | 9.2 px | 0.80 | 1.00 | 10 |
| pressure swell | 2 % → 2 % | 8.8 px | 0.80 | 1.00 | 15 |
| fast wave | 7 % → 7 % | 8.5 px | 0.80 | 1.00 | 35 |
| slow wave | 7 % → 7 % | 8.0 px | 0.80 | 1.00 | 50 |
| spiral | 12 % → 12 % | 7.9 px | 0.80 | 1.00 | 71 |
| loop | 6 % → 6 % | 8.1 px | 0.80 | 1.00 | 35 |
| tilted | 3 % → 3 % | 7.5 px | 0.80 | 1.00 | 22 |
| over the wet one | 6 % → 6 % | 7.9 px | 0.80 | 1.00 | 16 |
| long, no reload | 17 % → 17 % | 7.8 px | 0.80 | 1.00 | 93 | quarters: 0.15 → 0.16 → 0.15 → 0.16

Numbers say: light vs heavy: width 6.5 → 9.2 px, dark 0.80 → 0.80; the long stroke does not run out of paint.

## Watercolour — wash
Watercolor · 50 px · 32.2 s

![Watercolour — wash](Watercolour-wash.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 15 % → 16 % | 43.3 px | 0.03 | 1.05 | 96 |
| heavy line | 21 % → 22 % | 62.1 px | 0.03 | 1.04 | 109 |
| pressure swell | 14 % → 15 % | 54.3 px | 0.03 | 1.04 | 86 |
| fast wave | 47 % → 49 % | 53.8 px | 0.02 | 1.04 | 272 |
| slow wave | 45 % → 46 % | 52.0 px | 0.04 | 1.03 | 464 |
| spiral | 64 % → 66 % | 42.5 px | 0.03 | 1.03 | 451 |
| loop | 39 % → 40 % | 50.3 px | 0.03 | 1.02 | 231 |
| tilted | 17 % → 17 % | 47.3 px | 0.04 | 1.03 | 156 |
| over the wet one | 35 % → 36 % | 49.0 px | 0.04 | 1.04 | 115 |
| long, no reload | 79 % → 84 % | 35.5 px | 0.03 | 1.06 | 646 | quarters: 0.04 → 0.03 → 0.02 → 0.01

Numbers say: light vs heavy: width 43.3 → 62.1 px, dark 0.03 → 0.03.

## Watercolour — wet-in-wet
Watercolor · 44 px · 30.6 s

![Watercolour — wet-in-wet](Watercolour-wet-in-wet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 13 % → 13 % | 36.6 px | 0.07 | 1.05 | 80 |
| heavy line | 18 % → 19 % | 52.4 px | 0.06 | 1.04 | 103 |
| pressure swell | 12 % → 12 % | 44.9 px | 0.07 | 1.04 | 65 |
| fast wave | 40 % → 41 % | 45.9 px | 0.05 | 1.04 | 222 |
| slow wave | 39 % → 40 % | 45.0 px | 0.08 | 1.03 | 374 |
| spiral | 62 % → 63 % | 40.8 px | 0.06 | 1.02 | 374 |
| loop | 33 % → 34 % | 43.2 px | 0.07 | 1.03 | 193 |
| tilted | 14 % → 15 % | 39.1 px | 0.08 | 1.04 | 126 |
| over the wet one | 29 % → 31 % | 42.0 px | 0.08 | 1.05 | 82 |
| long, no reload | 75 % → 78 % | 33.6 px | 0.06 | 1.04 | 564 | quarters: 0.07 → 0.06 → 0.04 → 0.03

Numbers say: light vs heavy: width 36.6 → 52.4 px, dark 0.07 → 0.06.

## Watercolour — glaze
Watercolor · 38 px · 29.8 s

![Watercolour — glaze](Watercolour-glaze.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 12 % → 13 % | 35.2 px | 0.03 | 1.05 | 70 |
| heavy line | 18 % → 19 % | 52.2 px | 0.02 | 1.06 | 84 |
| pressure swell | 12 % → 13 % | 44.6 px | 0.02 | 1.07 | 59 |
| fast wave | 37 % → 40 % | 42.4 px | 0.02 | 1.08 | 192 |
| slow wave | 35 % → 37 % | 40.2 px | 0.02 | 1.08 | 318 |
| spiral | 54 % → 59 % | 35.9 px | 0.02 | 1.09 | 317 |
| loop | 32 % → 33 % | 40.8 px | 0.02 | 1.05 | 162 |
| tilted | 13 % → 14 % | 37.0 px | 0.03 | 1.03 | 112 |
| over the wet one | 28 % → 30 % | 41.7 px | 0.03 | 1.06 | 83 |
| long, no reload | 60 % → 69 % | 26.8 px | 0.02 | 1.15 | 485 | quarters: 0.02 → 0.01 → 0.01 → 0.00

Numbers say: light vs heavy: width 35.2 → 52.2 px, dark 0.03 → 0.02.

## Watercolour — granulating
Watercolor · 44 px · 30.6 s

![Watercolour — granulating](Watercolour-granulating.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 14 % → 14 % | 40.5 px | 0.05 | 1.03 | 86 |
| heavy line | 20 % → 21 % | 59.2 px | 0.04 | 1.02 | 100 |
| pressure swell | 14 % → 14 % | 51.3 px | 0.05 | 1.02 | 71 |
| fast wave | 44 % → 45 % | 50.3 px | 0.04 | 1.04 | 234 |
| slow wave | 40 % → 42 % | 46.0 px | 0.06 | 1.06 | 372 |
| spiral | 59 % → 63 % | 38.7 px | 0.04 | 1.07 | 367 |
| loop | 36 % → 37 % | 46.9 px | 0.05 | 1.02 | 199 |
| tilted | 15 % → 16 % | 43.1 px | 0.06 | 1.03 | 129 |
| over the wet one | 32 % → 33 % | 46.6 px | 0.06 | 1.04 | 89 |
| long, no reload | 68 % → 76 % | 30.3 px | 0.04 | 1.12 | 554 | quarters: 0.06 → 0.04 → 0.02 → 0.02

Numbers say: light vs heavy: width 40.5 → 59.2 px, dark 0.05 → 0.04.

## Watercolour — dry brush
Watercolor · 36 px · 25.8 s

![Watercolour — dry brush](Watercolour-dry-brush.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 9 % → 9 % | 24.9 px | 0.07 | 1.09 | 97 |
| heavy line | 13 % → 13 % | 36.7 px | 0.06 | 0.99 | 100 |
| pressure swell | 10 % → 10 % | 36.4 px | 0.06 | 1.04 | 70 |
| fast wave | 24 % → 19 % | 27.3 px | 0.05 | 0.82 | 252 |
| slow wave | 22 % → 17 % | 25.2 px | 0.05 | 0.78 | 426 |
| spiral | 29 % → 20 % | 19.3 px | 0.05 | 0.67 | 421 |
| loop | 19 % → 18 % | 24.6 px | 0.05 | 0.94 | 220 |
| tilted | 9 % → 10 % | 24.3 px | 0.06 | 1.10 | 115 |
| over the wet one | 20 % → 20 % | 31.7 px | 0.06 | 0.99 | 97 |
| long, no reload | 28 % → 19 % | 12.4 px | 0.05 | 0.70 | 584 | quarters: 0.03 → 0.01 → 0.00 → 0.00

Numbers say: light vs heavy: width 24.9 → 36.7 px, dark 0.07 → 0.06.

## Gouache
Gouache · 30 px · 23.9 s

![Gouache](Gouache.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 8 % → 5 % | 24.4 px | 0.28 | 0.64 | 68 |
| heavy line | 14 % → 6 % | 39.7 px | 0.28 | 0.47 | 87 |
| pressure swell | 10 % → 6 % | 38.6 px | 0.28 | 0.60 | 60 |
| fast wave | 28 % → 7 % | 32.2 px | 0.28 | 0.25 | 202 |
| slow wave | 27 % → 8 % | 31.4 px | 0.28 | 0.29 | 319 |
| spiral | 38 % → 8 % | 24.8 px | 0.27 | 0.22 | 322 |
| loop | 22 % → 8 % | 28.6 px | 0.28 | 0.35 | 181 |
| tilted | 9 % → 9 % | 23.8 px | 0.27 | 1.01 | 85 |
| over the wet one | 20 % → 13 % | 31.1 px | 0.27 | 0.66 | 78 |
| long, no reload | 40 % → 9 % | 17.9 px | 0.27 | 0.24 | 474 | quarters: 0.01 → 0.01 → 0.02 → 0.02

Numbers say: light vs heavy: width 24.4 → 39.7 px, dark 0.28 → 0.28; the long stroke does not run out of paint.

## Oil — alla prima
Oil · 30 px · 17.6 s

![Oil — alla prima](Oil-alla-prima.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 9 % → 9 % | 27.6 px | 0.51 | 1.00 | 76 |
| heavy line | 10 % → 10 % | 30.3 px | 0.51 | 1.00 | 87 |
| pressure swell | 8 % → 8 % | 29.8 px | 0.53 | 1.00 | 63 |
| fast wave | 24 % → 24 % | 28.1 px | 0.51 | 1.00 | 225 |
| slow wave | 26 % → 26 % | 29.5 px | 0.51 | 1.00 | 356 |
| spiral | 40 % → 40 % | 26.4 px | 0.50 | 1.00 | 362 |
| loop | 21 % → 21 % | 27.6 px | 0.52 | 1.00 | 192 |
| tilted | 11 % → 11 % | 30.4 px | 0.51 | 1.00 | 107 |
| over the wet one | 20 % → 20 % | 26.5 px | 0.51 | 1.00 | 85 |
| long, no reload | 49 % → 49 % | 22.0 px | 0.50 | 1.00 | 542 | quarters: 0.32 → 0.28 → 0.25 → 0.22

Numbers say: light vs heavy: width 27.6 → 30.3 px, dark 0.51 → 0.51; pressure barely changes the width.

## Oil — impasto
Oil · 34 px · 18.7 s

![Oil — impasto](Oil-impasto.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 12 % → 12 % | 33.4 px | 0.25 | 1.00 | 92 |
| heavy line | 12 % → 12 % | 36.3 px | 0.25 | 1.00 | 103 |
| pressure swell | 10 % → 10 % | 35.9 px | 0.26 | 1.00 | 77 |
| fast wave | 30 % → 30 % | 35.1 px | 0.25 | 1.00 | 280 |
| slow wave | 31 % → 31 % | 35.7 px | 0.25 | 1.00 | 438 |
| spiral | 52 % → 52 % | 34.0 px | 0.23 | 1.00 | 454 |
| loop | 26 % → 26 % | 33.7 px | 0.24 | 1.00 | 230 |
| tilted | 12 % → 12 % | 32.8 px | 0.26 | 1.00 | 122 |
| over the wet one | 23 % → 23 % | 31.9 px | 0.26 | 1.00 | 105 |
| long, no reload | 60 % → 60 % | 26.9 px | 0.22 | 1.00 | 692 | quarters: 0.18 → 0.16 → 0.13 → 0.10

Numbers say: light vs heavy: width 33.4 → 36.3 px, dark 0.25 → 0.25; pressure barely changes the width.

## Oil — glaze
Oil · 40 px · 14.7 s

![Oil — glaze](Oil-glaze.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 9 % → 9 % | 25.4 px | 0.50 | 1.00 | 106 |
| heavy line | 13 % → 13 % | 36.3 px | 0.49 | 1.00 | 117 |
| pressure swell | 9 % → 9 % | 35.3 px | 0.50 | 1.00 | 83 |
| fast wave | 26 % → 26 % | 30.1 px | 0.48 | 1.00 | 252 |
| slow wave | 29 % → 29 % | 33.7 px | 0.49 | 1.00 | 462 |
| spiral | 44 % → 44 % | 29.0 px | 0.49 | 1.00 | 447 |
| loop | 23 % → 23 % | 30.2 px | 0.50 | 1.00 | 227 |
| tilted | 10 % → 10 % | 28.9 px | 0.50 | 1.00 | 132 |
| over the wet one | 22 % → 22 % | 31.6 px | 0.50 | 1.00 | 105 |
| long, no reload | 51 % → 51 % | 22.7 px | 0.49 | 1.00 | 662 | quarters: 0.33 → 0.29 → 0.26 → 0.22

Numbers say: light vs heavy: width 25.4 → 36.3 px, dark 0.50 → 0.49.

## Oil — scumble
Oil · 36 px · 19.4 s

![Oil — scumble](Oil-scumble.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 11 % → 11 % | 33.1 px | 0.27 | 1.00 | 117 |
| heavy line | 12 % → 12 % | 36.1 px | 0.27 | 1.00 | 122 |
| pressure swell | 9 % → 9 % | 35.5 px | 0.28 | 1.00 | 86 |
| fast wave | 26 % → 26 % | 29.6 px | 0.19 | 1.00 | 321 |
| slow wave | 27 % → 27 % | 30.9 px | 0.18 | 1.00 | 534 |
| spiral | 41 % → 41 % | 27.1 px | 0.13 | 1.00 | 520 |
| loop | 24 % → 24 % | 30.6 px | 0.20 | 1.00 | 277 |
| tilted | 11 % → 11 % | 30.4 px | 0.25 | 1.00 | 132 |
| over the wet one | 22 % → 22 % | 31.4 px | 0.25 | 1.00 | 139 |
| long, no reload | 45 % → 45 % | 20.3 px | 0.12 | 1.00 | 802 | quarters: 0.00 → 0.00 → 0.00 → 0.00

Numbers say: light vs heavy: width 33.1 → 36.1 px, dark 0.27 → 0.27; pressure barely changes the width.

## Acrylic — heavy body
Heavy acrylic · 30 px · 14.2 s

![Acrylic — heavy body](Acrylic-heavy-body.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 10 % → 9 % | 28.9 px | 0.51 | 0.91 | 89 |
| heavy line | 11 % → 10 % | 31.1 px | 0.51 | 0.93 | 97 |
| pressure swell | 8 % → 8 % | 30.7 px | 0.53 | 0.94 | 65 |
| fast wave | 23 % → 15 % | 26.5 px | 0.52 | 0.64 | 265 |
| slow wave | 24 % → 16 % | 27.7 px | 0.51 | 0.65 | 373 |
| spiral | 35 % → 15 % | 23.3 px | 0.51 | 0.43 | 389 |
| loop | 21 % → 16 % | 26.9 px | 0.51 | 0.76 | 196 |
| tilted | 9 % → 9 % | 24.9 px | 0.52 | 0.99 | 102 |
| over the wet one | 19 % → 17 % | 27.7 px | 0.52 | 0.89 | 96 |
| long, no reload | 39 % → 16 % | 17.3 px | 0.51 | 0.41 | 533 | quarters: 0.29 → 0.20 → 0.12 → 0.04

Numbers say: light vs heavy: width 28.9 → 31.1 px, dark 0.51 → 0.51; pressure barely changes the width.

## Acrylic — fluid
Watercolor · 36 px · 29.0 s

![Acrylic — fluid](Acrylic-fluid.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 12 % → 12 % | 34.3 px | 0.08 | 1.02 | 76 |
| heavy line | 18 % → 18 % | 51.6 px | 0.07 | 1.01 | 124 |
| pressure swell | 12 % → 12 % | 44.8 px | 0.08 | 1.01 | 61 |
| fast wave | 37 % → 38 % | 42.6 px | 0.07 | 1.02 | 195 |
| slow wave | 34 % → 35 % | 39.2 px | 0.07 | 1.03 | 320 |
| spiral | 52 % → 53 % | 34.2 px | 0.07 | 1.03 | 341 |
| loop | 30 % → 31 % | 39.4 px | 0.07 | 1.02 | 168 |
| tilted | 12 % → 12 % | 32.6 px | 0.08 | 1.04 | 104 |
| over the wet one | 27 % → 28 % | 43.2 px | 0.08 | 1.02 | 80 |
| long, no reload | 56 % → 58 % | 25.3 px | 0.06 | 1.04 | 476 | quarters: 0.06 → 0.05 → 0.03 → 0.02

Numbers say: light vs heavy: width 34.3 → 51.6 px, dark 0.08 → 0.07.

## Acrylic — palette knife
Heavy acrylic · 42 px · 18.8 s

![Acrylic — palette knife](Acrylic-palette-knife.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 15 % → 15 % | 44.0 px | 0.36 | 0.98 | 26 |
| heavy line | 15 % → 15 % | 44.2 px | 0.38 | 0.97 | 21 |
| pressure swell | 12 % → 12 % | 43.5 px | 0.40 | 0.99 | 15 |
| fast wave | 36 % → 20 % | 41.9 px | 0.35 | 0.56 | 53 |
| slow wave | 37 % → 21 % | 42.6 px | 0.35 | 0.57 | 84 |
| spiral | 50 % → 18 % | 32.8 px | 0.35 | 0.37 | 91 |
| loop | 32 % → 24 % | 41.2 px | 0.34 | 0.75 | 48 |
| tilted | 12 % → 12 % | 33.6 px | 0.37 | 1.00 | 22 |
| over the wet one | 26 % → 25 % | 39.7 px | 0.37 | 0.97 | 26 |
| long, no reload | 57 % → 21 % | 25.7 px | 0.33 | 0.36 | 137 | quarters: 0.00 → 0.00 → 0.00 → 0.01

Numbers say: light vs heavy: width 44.0 → 44.2 px, dark 0.36 → 0.38; pressure barely changes the width; the long stroke does not run out of paint.

## Finger on oil
Oil · 30 px · 13.1 s

![Finger on oil](Finger-on-oil.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 8 % → 8 % | 23.7 px | 0.40 | 1.00 | 51 |
| heavy line | 13 % → 13 % | 36.5 px | 0.38 | 1.00 | 68 |
| pressure swell | 9 % → 9 % | 33.3 px | 0.41 | 1.00 | 44 |
| fast wave | 22 % → 22 % | 26.0 px | 0.35 | 1.00 | 127 |
| slow wave | 24 % → 24 % | 27.8 px | 0.35 | 1.00 | 215 |
| spiral | 36 % → 36 % | 23.5 px | 0.27 | 1.00 | 207 |
| loop | 21 % → 21 % | 27.3 px | 0.36 | 1.00 | 109 |
| tilted | 9 % → 9 % | 26.4 px | 0.39 | 1.00 | 77 |
| over the wet one | 20 % → 20 % | 29.3 px | 0.39 | 1.00 | 47 |
| long, no reload | 36 % → 36 % | 16.3 px | 0.26 | 1.00 | 331 | quarters: 0.23 → 0.11 → 0.05 → 0.02

Numbers say: light vs heavy: width 23.7 → 36.5 px, dark 0.40 → 0.38.

## Palette knife — oil
Oil · 44 px · 18.9 s

![Palette knife — oil](Palette-knife-oil.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 16 % → 16 % | 45.6 px | 0.33 | 1.00 | 22 |
| heavy line | 16 % → 16 % | 46.3 px | 0.36 | 1.00 | 24 |
| pressure swell | 12 % → 12 % | 45.2 px | 0.35 | 1.00 | 14 |
| fast wave | 39 % → 39 % | 44.9 px | 0.31 | 1.00 | 45 |
| slow wave | 39 % → 39 % | 45.4 px | 0.32 | 1.00 | 94 |
| spiral | 62 % → 62 % | 40.9 px | 0.26 | 1.00 | 93 |
| loop | 34 % → 34 % | 43.8 px | 0.33 | 1.00 | 52 |
| tilted | 13 % → 13 % | 36.6 px | 0.35 | 1.00 | 22 |
| over the wet one | 28 % → 28 % | 40.8 px | 0.35 | 1.00 | 21 |
| long, no reload | 74 % → 74 % | 33.1 px | 0.24 | 1.00 | 146 | quarters: 0.00 → 0.00 → 0.00 → 0.00

Numbers say: light vs heavy: width 45.6 → 46.3 px, dark 0.33 → 0.36; pressure barely changes the width.

## 0.45 · Sponge
Watercolor · 46 px · 30.5 s

![0.45 · Sponge](0-45-Sponge.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 23 % → 15 % | 66.4 px | 0.02 | 0.67 | 60 |
| heavy line | 28 % → 23 % | 81.1 px | 0.02 | 0.81 | 75 |
| pressure swell | 20 % → 16 % | 76.7 px | 0.03 | 0.76 | 44 |
| fast wave | 46 % → 32 % | 53.0 px | 0.03 | 0.70 | 162 |
| slow wave | 53 % → 46 % | 60.7 px | 0.04 | 0.87 | 285 |
| spiral | 65 % → 53 % | 42.6 px | 0.04 | 0.82 | 290 |
| loop | 46 % → 40 % | 60.1 px | 0.04 | 0.86 | 150 |
| tilted | 16 % → 17 % | 43.8 px | 0.05 | 1.07 | 110 |
| over the wet one | 40 % → 35 % | 67.3 px | 0.05 | 0.89 | 71 |
| long, no reload | 74 % → 65 % | 33.2 px | 0.04 | 0.88 | 404 | quarters: 0.05 → 0.04 → 0.03 → 0.02

Numbers say: light vs heavy: width 66.4 → 81.1 px, dark 0.02 → 0.02.

## 0.45 · Eraser
Eraser · 30 px · 18.8 s · over bands of wet oil paint and oil pastel in turn (it works on paint already there: look at what it does to the bands; covered counts the bands too)

![0.45 · Eraser](0-45-Eraser.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 24 % → 24 % | 69.2 px | 0.82 | 1.00 | 37 |
| heavy line | 23 % → 23 % | 67.4 px | 0.81 | 1.00 | 48 |
| pressure swell | 23 % → 23 % | 86.7 px | 0.82 | 1.00 | 37 |
| fast wave | 21 % → 21 % | 24.7 px | 0.81 | 1.00 | 100 |
| slow wave | 20 % → 20 % | 23.5 px | 0.82 | 1.00 | 188 |
| spiral | 20 % → 20 % | 13.5 px | 0.79 | 1.00 | 207 |
| loop | 21 % → 21 % | 27.8 px | 0.80 | 1.00 | 104 |
| tilted | 23 % → 23 % | 64.8 px | 0.81 | 1.00 | 48 |
| over the wet one | 22 % → 22 % | 0.0 px | 0.81 | 1.00 | 59 |
| long, no reload | 17 % → 17 % | 7.5 px | 0.79 | 1.00 | 270 | quarters: 0.13 → 0.16 → 0.13 → 0.17

Numbers say: light vs heavy: width 69.2 → 67.4 px, dark 0.82 → 0.81; pressure barely changes the width; the long stroke does not run out of paint.

## Lift wet paint
Eraser · 30 px · 18.6 s · over bands of wet oil paint and oil pastel in turn (it works on paint already there: look at what it does to the bands; covered counts the bands too)

![Lift wet paint](Lift-wet-paint.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 24 % → 24 % | 70.1 px | 0.82 | 1.00 | 27 |
| heavy line | 24 % → 24 % | 69.8 px | 0.82 | 1.00 | 43 |
| pressure swell | 24 % → 24 % | 89.5 px | 0.82 | 1.00 | 24 |
| fast wave | 24 % → 24 % | 27.7 px | 0.82 | 1.00 | 97 |
| slow wave | 24 % → 24 % | 27.7 px | 0.82 | 1.00 | 164 |
| spiral | 24 % → 24 % | 15.9 px | 0.82 | 1.00 | 144 |
| loop | 24 % → 24 % | 31.1 px | 0.82 | 1.00 | 96 |
| tilted | 24 % → 24 % | 66.8 px | 0.82 | 1.00 | 52 |
| over the wet one | 24 % → 24 % | 0.0 px | 0.82 | 1.00 | 37 |
| long, no reload | 24 % → 24 % | 10.7 px | 0.82 | 1.00 | 240 | quarters: 0.18 → 0.24 → 0.17 → 0.24

Numbers say: light vs heavy: width 70.1 → 69.8 px, dark 0.82 → 0.82; pressure barely changes the width; the long stroke does not run out of paint.

## Sgraffito
Eraser · 10 px · 18.2 s · over bands of wet oil paint and oil pastel in turn (it works on paint already there: look at what it does to the bands; covered counts the bands too)

![Sgraffito](Sgraffito.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 24 % → 24 % | 69.5 px | 0.81 | 1.00 | 9 |
| heavy line | 24 % → 24 % | 69.5 px | 0.82 | 1.00 | 6 |
| pressure swell | 24 % → 24 % | 89.5 px | 0.82 | 1.00 | 6 |
| fast wave | 24 % → 24 % | 27.4 px | 0.82 | 1.00 | 24 |
| slow wave | 24 % → 24 % | 27.4 px | 0.81 | 1.00 | 19 |
| spiral | 24 % → 24 % | 15.7 px | 0.81 | 1.00 | 32 |
| loop | 24 % → 24 % | 30.9 px | 0.82 | 1.00 | 20 |
| tilted | 24 % → 24 % | 66.6 px | 0.82 | 1.00 | 5 |
| over the wet one | 24 % → 24 % | 0.0 px | 0.82 | 1.00 | 9 |
| long, no reload | 24 % → 24 % | 10.6 px | 0.82 | 1.00 | 56 | quarters: 0.17 → 0.24 → 0.17 → 0.24

Numbers say: light vs heavy: width 69.5 → 69.5 px, dark 0.81 → 0.82; pressure barely changes the width; the long stroke does not run out of paint.

## Brush Artist · Refs · #01 Henry Ward peach cloud
Gouache · 44 px · 34.5 s

![Brush Artist · Refs · #01 Henry Ward peach cloud](Brush-Artist-Refs-01-Henry-Ward-peach-cloud.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 15 % → 13 % | 42.3 px | 0.33 | 0.87 | 139 |
| heavy line | 16 % → 14 % | 45.7 px | 0.33 | 0.91 | 145 |
| pressure swell | 12 % → 11 % | 44.3 px | 0.33 | 0.92 | 105 |
| fast wave | 38 % → 25 % | 43.9 px | 0.33 | 0.65 | 374 |
| slow wave | 38 % → 26 % | 43.6 px | 0.33 | 0.68 | 629 |
| spiral | 61 % → 28 % | 40.2 px | 0.33 | 0.46 | 625 |
| loop | 32 % → 26 % | 41.6 px | 0.33 | 0.81 | 321 |
| tilted | 13 % → 13 % | 36.8 px | 0.33 | 1.00 | 170 |
| over the wet one | 27 % → 26 % | 39.2 px | 0.33 | 0.95 | 144 |
| long, no reload | 72 % → 28 % | 32.2 px | 0.33 | 0.40 | 923 | quarters: 0.01 → 0.01 → 0.01 → 0.01

Numbers say: light vs heavy: width 42.3 → 45.7 px, dark 0.33 → 0.33; pressure barely changes the width; the long stroke does not run out of paint.

## Brush Artist · Refs · #02 Henry Ward cream strokes
Gouache · 46 px · 35.5 s

![Brush Artist · Refs · #02 Henry Ward cream strokes](Brush-Artist-Refs-02-Henry-Ward-cream-strokes.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 14 % → 13 % | 41.4 px | 0.42 | 0.94 | 134 |
| heavy line | 15 % → 15 % | 44.5 px | 0.42 | 0.96 | 138 |
| pressure swell | 12 % → 11 % | 43.9 px | 0.42 | 0.95 | 109 |
| fast wave | 36 % → 25 % | 41.9 px | 0.41 | 0.69 | 384 |
| slow wave | 36 % → 25 % | 41.8 px | 0.41 | 0.70 | 626 |
| spiral | 59 % → 28 % | 39.2 px | 0.41 | 0.46 | 641 |
| loop | 31 % → 27 % | 40.3 px | 0.41 | 0.86 | 326 |
| tilted | 13 % → 13 % | 37.3 px | 0.42 | 1.00 | 185 |
| over the wet one | 27 % → 26 % | 38.4 px | 0.42 | 0.96 | 143 |
| long, no reload | 70 % → 29 % | 31.3 px | 0.41 | 0.41 | 919 | quarters: 0.01 → 0.01 → 0.01 → 0.01

Numbers say: light vs heavy: width 41.4 → 44.5 px, dark 0.42 → 0.42; pressure barely changes the width; the long stroke does not run out of paint.

## Brush Artist · Refs · #03 Henry Ward navy contours
Heavy acrylic · 22 px · 13.2 s

![Brush Artist · Refs · #03 Henry Ward navy contours](Brush-Artist-Refs-03-Henry-Ward-navy-contours.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 7 % → 7 % | 21.5 px | 0.70 | 0.94 | 66 |
| heavy line | 8 % → 8 % | 23.4 px | 0.70 | 0.95 | 66 |
| pressure swell | 6 % → 6 % | 23.2 px | 0.73 | 0.94 | 46 |
| fast wave | 19 % → 12 % | 21.8 px | 0.72 | 0.66 | 171 |
| slow wave | 19 % → 13 % | 22.4 px | 0.72 | 0.69 | 269 |
| spiral | 30 % → 13 % | 19.5 px | 0.72 | 0.45 | 302 |
| loop | 17 % → 13 % | 21.4 px | 0.72 | 0.81 | 167 |
| tilted | 8 % → 8 % | 22.6 px | 0.71 | 1.00 | 89 |
| over the wet one | 16 % → 14 % | 21.2 px | 0.71 | 0.89 | 72 |
| long, no reload | 34 % → 14 % | 15.1 px | 0.72 | 0.40 | 439 | quarters: 0.35 → 0.29 → 0.20 → 0.08

Numbers say: light vs heavy: width 21.5 → 23.4 px, dark 0.70 → 0.70; pressure barely changes the width.

## Brush Artist · Refs · #04 Henry Ward grey cloud
Gouache · 50 px · 37.0 s

![Brush Artist · Refs · #04 Henry Ward grey cloud](Brush-Artist-Refs-04-Henry-Ward-grey-cloud.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 16 % → 15 % | 47.1 px | 0.32 | 0.90 | 163 |
| heavy line | 17 % → 16 % | 50.6 px | 0.32 | 0.94 | 167 |
| pressure swell | 13 % → 12 % | 49.2 px | 0.32 | 0.94 | 121 |
| fast wave | 41 % → 28 % | 47.4 px | 0.32 | 0.67 | 428 |
| slow wave | 41 % → 28 % | 47.2 px | 0.32 | 0.69 | 691 |
| spiral | 63 % → 30 % | 41.3 px | 0.32 | 0.48 | 711 |
| loop | 35 % → 29 % | 45.6 px | 0.32 | 0.84 | 381 |
| tilted | 14 % → 14 % | 40.3 px | 0.32 | 1.00 | 191 |
| over the wet one | 30 % → 29 % | 43.2 px | 0.32 | 0.96 | 160 |
| long, no reload | 76 % → 32 % | 33.9 px | 0.32 | 0.43 | 984 | quarters: 0.01 → 0.01 → 0.01 → 0.01

Numbers say: light vs heavy: width 47.1 → 50.6 px, dark 0.32 → 0.32; pressure barely changes the width; the long stroke does not run out of paint.

## Brush Artist · Refs · #05 Henry Ward green in rust loops
Heavy acrylic · 20 px · 13.2 s

![Brush Artist · Refs · #05 Henry Ward green in rust loops](Brush-Artist-Refs-05-Henry-Ward-green-in-rust-loops.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 7 % → 6 % | 19.5 px | 0.55 | 0.94 | 67 |
| heavy line | 7 % → 7 % | 21.2 px | 0.55 | 0.94 | 75 |
| pressure swell | 6 % → 5 % | 21.5 px | 0.57 | 0.92 | 48 |
| fast wave | 17 % → 11 % | 19.7 px | 0.56 | 0.64 | 171 |
| slow wave | 18 % → 12 % | 20.3 px | 0.56 | 0.66 | 251 |
| spiral | 27 % → 12 % | 17.9 px | 0.55 | 0.42 | 294 |
| loop | 15 % → 12 % | 19.5 px | 0.55 | 0.80 | 158 |
| tilted | 8 % → 8 % | 21.7 px | 0.56 | 1.00 | 84 |
| over the wet one | 15 % → 13 % | 19.1 px | 0.56 | 0.87 | 67 |
| long, no reload | 30 % → 12 % | 13.4 px | 0.56 | 0.39 | 445 | quarters: 0.25 → 0.18 → 0.10 → 0.02

Numbers say: light vs heavy: width 19.5 → 21.2 px, dark 0.55 → 0.55; pressure barely changes the width.

## Brush Artist · Refs · #06 Henry Ward scrubbed grey
Gouache · 50 px · 36.0 s

![Brush Artist · Refs · #06 Henry Ward scrubbed grey](Brush-Artist-Refs-06-Henry-Ward-scrubbed-grey.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 16 % → 15 % | 47.1 px | 0.33 | 0.90 | 132 |
| heavy line | 17 % → 16 % | 50.6 px | 0.33 | 0.94 | 158 |
| pressure swell | 13 % → 12 % | 49.2 px | 0.33 | 0.94 | 118 |
| fast wave | 41 % → 28 % | 47.4 px | 0.33 | 0.67 | 403 |
| slow wave | 41 % → 28 % | 47.2 px | 0.33 | 0.69 | 692 |
| spiral | 63 % → 30 % | 41.3 px | 0.33 | 0.48 | 679 |
| loop | 35 % → 29 % | 45.6 px | 0.33 | 0.84 | 339 |
| tilted | 14 % → 14 % | 40.3 px | 0.33 | 1.00 | 182 |
| over the wet one | 30 % → 29 % | 43.2 px | 0.33 | 0.96 | 158 |
| long, no reload | 76 % → 32 % | 33.9 px | 0.33 | 0.43 | 1014 | quarters: 0.01 → 0.01 → 0.01 → 0.01

Numbers say: light vs heavy: width 47.1 → 50.6 px, dark 0.33 → 0.33; pressure barely changes the width; the long stroke does not run out of paint.

## Brush Artist · Refs · #07 Henry Ward blue L + black zigzag
Heavy acrylic · 34 px · 15.4 s

![Brush Artist · Refs · #07 Henry Ward blue L + black zigzag](Brush-Artist-Refs-07-Henry-Ward-blue-L-black-zigzag.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 11 % → 11 % | 33.1 px | 0.57 | 0.93 | 84 |
| heavy line | 12 % → 11 % | 35.7 px | 0.57 | 0.93 | 101 |
| pressure swell | 9 % → 9 % | 35.2 px | 0.59 | 0.94 | 74 |
| fast wave | 29 % → 20 % | 33.6 px | 0.59 | 0.69 | 230 |
| slow wave | 30 % → 21 % | 34.1 px | 0.58 | 0.73 | 453 |
| spiral | 47 % → 22 % | 31.3 px | 0.58 | 0.46 | 406 |
| loop | 25 % → 21 % | 32.7 px | 0.58 | 0.82 | 211 |
| tilted | 11 % → 11 % | 29.8 px | 0.58 | 1.00 | 112 |
| over the wet one | 22 % → 20 % | 31.7 px | 0.58 | 0.91 | 104 |
| long, no reload | 53 % → 22 % | 23.8 px | 0.59 | 0.42 | 581 | quarters: 0.40 → 0.32 → 0.21 → 0.10

Numbers say: light vs heavy: width 33.1 → 35.7 px, dark 0.57 → 0.57; pressure barely changes the width.

## Brush Artist · Refs · #08 Henry Ward olive bands
Gouache · 34 px · 22.5 s

![Brush Artist · Refs · #08 Henry Ward olive bands](Brush-Artist-Refs-08-Henry-Ward-olive-bands.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 8 % → 2 % | 24.7 px | 0.57 | 0.27 | 55 |
| heavy line | 12 % → 3 % | 33.9 px | 0.57 | 0.22 | 140 |
| pressure swell | 8 % → 3 % | 30.8 px | 0.57 | 0.38 | 76 |
| fast wave | 25 % → 4 % | 29.2 px | 0.57 | 0.15 | 251 |
| slow wave | 25 % → 4 % | 28.9 px | 0.57 | 0.15 | 411 |
| spiral | 39 % → 4 % | 25.7 px | 0.57 | 0.10 | 417 |
| loop | 22 % → 5 % | 28.8 px | 0.57 | 0.21 | 212 |
| tilted | 10 % → 10 % | 28.6 px | 0.57 | 0.98 | 109 |
| over the wet one | 20 % → 8 % | 28.3 px | 0.57 | 0.40 | 101 |
| long, no reload | 45 % → 6 % | 20.0 px | 0.57 | 0.13 | 620 | quarters: 0.35 → 0.27 → 0.17 → 0.08

Numbers say: light vs heavy: width 24.7 → 33.9 px, dark 0.57 → 0.57.

## Brush Artist · Refs · #09 Henry Ward white loops
Gouache · 46 px · 37.1 s

![Brush Artist · Refs · #09 Henry Ward white loops](Brush-Artist-Refs-09-Henry-Ward-white-loops.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 14 % → 13 % | 41.4 px | 0.44 | 0.94 | 132 |
| heavy line | 15 % → 15 % | 44.5 px | 0.45 | 0.96 | 164 |
| pressure swell | 12 % → 11 % | 43.9 px | 0.45 | 0.95 | 104 |
| fast wave | 36 % → 25 % | 41.9 px | 0.44 | 0.69 | 359 |
| slow wave | 36 % → 25 % | 41.8 px | 0.43 | 0.70 | 622 |
| spiral | 59 % → 28 % | 39.2 px | 0.43 | 0.46 | 620 |
| loop | 31 % → 27 % | 40.3 px | 0.43 | 0.86 | 299 |
| tilted | 13 % → 13 % | 37.3 px | 0.44 | 1.00 | 175 |
| over the wet one | 27 % → 26 % | 38.4 px | 0.44 | 0.96 | 140 |
| long, no reload | 70 % → 29 % | 31.3 px | 0.43 | 0.41 | 925 | quarters: 0.01 → 0.01 → 0.01 → 0.01

Numbers say: light vs heavy: width 41.4 → 44.5 px, dark 0.44 → 0.45; pressure barely changes the width; the long stroke does not run out of paint.

## Brush Artist · Refs · #10 Henry Ward maroon loops
Heavy acrylic · 30 px · 13.9 s

![Brush Artist · Refs · #10 Henry Ward maroon loops](Brush-Artist-Refs-10-Henry-Ward-maroon-loops.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 10 % → 9 % | 28.0 px | 0.70 | 0.94 | 82 |
| heavy line | 10 % → 10 % | 30.2 px | 0.69 | 0.95 | 89 |
| pressure swell | 8 % → 8 % | 30.0 px | 0.73 | 0.94 | 67 |
| fast wave | 24 % → 17 % | 28.3 px | 0.73 | 0.71 | 219 |
| slow wave | 25 % → 18 % | 29.0 px | 0.73 | 0.73 | 382 |
| spiral | 39 % → 18 % | 26.0 px | 0.72 | 0.47 | 374 |
| loop | 21 % → 18 % | 27.6 px | 0.72 | 0.85 | 191 |
| tilted | 10 % → 10 % | 27.9 px | 0.72 | 1.00 | 108 |
| over the wet one | 20 % → 18 % | 26.8 px | 0.72 | 0.91 | 92 |
| long, no reload | 46 % → 18 % | 20.6 px | 0.73 | 0.40 | 507 | quarters: 0.44 → 0.38 → 0.31 → 0.22

Numbers say: light vs heavy: width 28.0 → 30.2 px, dark 0.70 → 0.69; pressure barely changes the width.

## Brush Artist · Refs · #11 Henry Ward purple spun balls
Heavy acrylic · 36 px · 15.6 s

![Brush Artist · Refs · #11 Henry Ward purple spun balls](Brush-Artist-Refs-11-Henry-Ward-purple-spun-balls.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 12 % → 11 % | 34.1 px | 0.70 | 0.96 | 103 |
| heavy line | 13 % → 12 % | 36.6 px | 0.70 | 0.96 | 95 |
| pressure swell | 10 % → 9 % | 36.2 px | 0.74 | 0.95 | 73 |
| fast wave | 30 % → 23 % | 34.6 px | 0.73 | 0.75 | 258 |
| slow wave | 30 % → 24 % | 35.0 px | 0.73 | 0.79 | 430 |
| spiral | 49 % → 25 % | 32.3 px | 0.73 | 0.50 | 411 |
| loop | 26 % → 23 % | 33.4 px | 0.73 | 0.88 | 232 |
| tilted | 11 % → 11 % | 31.2 px | 0.72 | 1.00 | 121 |
| over the wet one | 23 % → 21 % | 32.1 px | 0.72 | 0.93 | 93 |
| long, no reload | 55 % → 24 % | 24.8 px | 0.73 | 0.44 | 621 | quarters: 0.51 → 0.46 → 0.39 → 0.28

Numbers say: light vs heavy: width 34.1 → 36.6 px, dark 0.70 → 0.70; pressure barely changes the width.

## Brush Artist · Refs · #12 Henry Ward black-olive cage
Gouache · 28 px · 22.1 s

![Brush Artist · Refs · #12 Henry Ward black-olive cage](Brush-Artist-Refs-12-Henry-Ward-black-olive-cage.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 7 % → 3 % | 20.9 px | 0.61 | 0.35 | 56 |
| heavy line | 9 % → 4 % | 26.1 px | 0.61 | 0.41 | 112 |
| pressure swell | 6 % → 4 % | 23.9 px | 0.61 | 0.61 | 61 |
| fast wave | 20 % → 4 % | 23.7 px | 0.61 | 0.19 | 204 |
| slow wave | 20 % → 4 % | 23.3 px | 0.61 | 0.21 | 337 |
| spiral | 32 % → 4 % | 21.4 px | 0.61 | 0.14 | 345 |
| loop | 18 % → 5 % | 22.8 px | 0.61 | 0.28 | 179 |
| tilted | 9 % → 9 % | 25.4 px | 0.61 | 0.98 | 95 |
| over the wet one | 17 % → 8 % | 21.8 px | 0.61 | 0.46 | 79 |
| long, no reload | 39 % → 6 % | 17.6 px | 0.61 | 0.15 | 497 | quarters: 0.31 → 0.26 → 0.19 → 0.10

Numbers say: light vs heavy: width 20.9 → 26.1 px, dark 0.61 → 0.61.

## Brush Artist · Refs · #13 Henry Ward blue streaky form
Gouache · 50 px · 39.7 s

![Brush Artist · Refs · #13 Henry Ward blue streaky form](Brush-Artist-Refs-13-Henry-Ward-blue-streaky-form.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 16 % → 15 % | 47.1 px | 0.33 | 0.90 | 144 |
| heavy line | 17 % → 16 % | 50.6 px | 0.33 | 0.94 | 150 |
| pressure swell | 13 % → 12 % | 49.2 px | 0.33 | 0.94 | 171 |
| fast wave | 41 % → 28 % | 47.4 px | 0.33 | 0.67 | 387 |
| slow wave | 41 % → 28 % | 47.2 px | 0.33 | 0.69 | 696 |
| spiral | 63 % → 30 % | 41.3 px | 0.33 | 0.48 | 703 |
| loop | 35 % → 29 % | 45.6 px | 0.33 | 0.84 | 343 |
| tilted | 14 % → 14 % | 40.3 px | 0.33 | 1.00 | 180 |
| over the wet one | 30 % → 29 % | 43.2 px | 0.33 | 0.96 | 159 |
| long, no reload | 76 % → 32 % | 33.9 px | 0.33 | 0.43 | 996 | quarters: 0.01 → 0.01 → 0.01 → 0.01

Numbers say: light vs heavy: width 47.1 → 50.6 px, dark 0.33 → 0.33; pressure barely changes the width; the long stroke does not run out of paint.

## Brush Artist · Refs · #14 Henry Ward olive totem
Heavy acrylic · 48 px · 17.9 s

![Brush Artist · Refs · #14 Henry Ward olive totem](Brush-Artist-Refs-14-Henry-Ward-olive-totem.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 15 % → 15 % | 44.8 px | 0.31 | 0.94 | 135 |
| heavy line | 16 % → 16 % | 47.7 px | 0.31 | 0.95 | 137 |
| pressure swell | 13 % → 12 % | 47.0 px | 0.32 | 0.95 | 102 |
| fast wave | 38 % → 30 % | 43.9 px | 0.30 | 0.79 | 361 |
| slow wave | 39 % → 31 % | 44.5 px | 0.30 | 0.81 | 610 |
| spiral | 58 % → 32 % | 38.1 px | 0.30 | 0.55 | 605 |
| loop | 33 % → 29 % | 42.6 px | 0.30 | 0.89 | 311 |
| tilted | 13 % → 13 % | 37.5 px | 0.31 | 1.00 | 166 |
| over the wet one | 28 % → 26 % | 41.1 px | 0.31 | 0.93 | 144 |
| long, no reload | 67 % → 33 % | 30.3 px | 0.30 | 0.49 | 868 | quarters: 0.25 → 0.18 → 0.10 → 0.03

Numbers say: light vs heavy: width 44.8 → 47.7 px, dark 0.31 → 0.31; pressure barely changes the width.

## Brush Artist · Refs · #15 Ultramarine brush script
Ink · 10 px · 25.0 s

![Brush Artist · Refs · #15 Ultramarine brush script](Brush-Artist-Refs-15-Ultramarine-brush-script.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 2 % → 5 % | 5.0 px | 0.53 | 2.62 | 34 |
| heavy line | 10 % → 10 % | 29.6 px | 0.66 | 1.00 | 83 |
| pressure swell | 6 % → 6 % | 20.8 px | 0.68 | 1.12 | 51 |
| fast wave | 18 % → 17 % | 20.2 px | 0.59 | 0.95 | 146 |
| slow wave | 14 % → 14 % | 16.1 px | 0.59 | 1.00 | 130 |
| spiral | 22 % → 18 % | 14.5 px | 0.54 | 0.82 | 245 |
| loop | 13 % → 14 % | 17.4 px | 0.61 | 1.02 | 128 |
| tilted | 6 % → 6 % | 15.5 px | 0.68 | 1.01 | 56 |
| over the wet one | 13 % → 13 % | 20.5 px | 0.68 | 1.04 | 55 |
| long, no reload | 33 % → 20 % | 14.8 px | 0.52 | 0.59 | 362 | quarters: 0.30 → 0.14 → 0.05 → 0.02

Numbers say: light vs heavy: width 5.0 → 29.6 px, dark 0.53 → 0.66; wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #18 Blue oil-stick scribbles
Pastel · 10 px · 9.3 s

![Brush Artist · Refs · #18 Blue oil-stick scribbles](Brush-Artist-Refs-18-Blue-oil-stick-scribbles.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 1 % → 1 % | 2.9 px | 0.52 | 1.00 | 17 |
| heavy line | 2 % → 2 % | 5.5 px | 0.53 | 1.00 | 16 |
| pressure swell | 1 % → 1 % | 5.0 px | 0.53 | 1.00 | 13 |
| fast wave | 4 % → 4 % | 4.8 px | 0.53 | 1.00 | 53 |
| slow wave | 4 % → 4 % | 4.4 px | 0.53 | 1.00 | 55 |
| spiral | 7 % → 7 % | 4.5 px | 0.52 | 1.00 | 90 |
| loop | 3 % → 3 % | 4.5 px | 0.52 | 1.00 | 49 |
| tilted | 2 % → 2 % | 4.7 px | 0.53 | 1.00 | 24 |
| over the wet one | 3 % → 3 % | 4.7 px | 0.53 | 1.00 | 17 |
| long, no reload | 10 % → 10 % | 4.4 px | 0.53 | 1.00 | 166 | quarters: 0.06 → 0.06 → 0.06 → 0.06

Numbers say: light vs heavy: width 2.9 → 5.5 px, dark 0.52 → 0.53; the long stroke does not run out of paint.

## Brush Artist · Refs · #20 Orange-red crayon scribble
Pastel · 14 px · 9.2 s

![Brush Artist · Refs · #20 Orange-red crayon scribble](Brush-Artist-Refs-20-Orange-red-crayon-scribble.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 1 % → 1 % | 4.0 px | 0.53 | 1.00 | 19 |
| heavy line | 3 % → 3 % | 8.0 px | 0.53 | 1.00 | 20 |
| pressure swell | 2 % → 2 % | 7.6 px | 0.53 | 1.00 | 12 |
| fast wave | 6 % → 6 % | 7.2 px | 0.53 | 1.00 | 50 |
| slow wave | 6 % → 6 % | 6.6 px | 0.53 | 1.00 | 56 |
| spiral | 9 % → 9 % | 6.2 px | 0.53 | 1.00 | 108 |
| loop | 5 % → 5 % | 6.2 px | 0.53 | 1.00 | 56 |
| tilted | 2 % → 2 % | 5.6 px | 0.53 | 1.00 | 26 |
| over the wet one | 4 % → 4 % | 6.6 px | 0.53 | 1.00 | 25 |
| long, no reload | 13 % → 13 % | 5.7 px | 0.53 | 1.00 | 142 | quarters: 0.07 → 0.07 → 0.08 → 0.08

Numbers say: light vs heavy: width 4.0 → 8.0 px, dark 0.53 → 0.53; the long stroke does not run out of paint.

## Brush Artist · Refs · #21 Gritty black contours
Gouache · 12 px · 21.8 s

![Brush Artist · Refs · #21 Gritty black contours](Brush-Artist-Refs-21-Gritty-black-contours.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 3 % → 0 % | 8.8 px | 0.79 | 0.12 | 48 |
| heavy line | 4 % → 0 % | 11.9 px | 0.79 | 0.10 | 100 |
| pressure swell | 3 % → 0 % | 11.6 px | 0.79 | 0.15 | 57 |
| fast wave | 7 % → 1 % | 8.5 px | 0.79 | 0.10 | 178 |
| slow wave | 8 % → 1 % | 9.0 px | 0.79 | 0.09 | 190 |
| spiral | 9 % → 1 % | 6.0 px | 0.79 | 0.10 | 424 |
| loop | 8 % → 1 % | 9.9 px | 0.79 | 0.09 | 173 |
| tilted | 4 % → 4 % | 10.8 px | 0.79 | 0.90 | 84 |
| over the wet one | 7 % → 1 % | 9.7 px | 0.79 | 0.17 | 77 |
| long, no reload | 7 % → 1 % | 3.3 px | 0.79 | 0.12 | 462 | quarters: 0.20 → 0.07 → 0.00 → 0.00

Numbers say: light vs heavy: width 8.8 → 11.9 px, dark 0.79 → 0.79.

## Brush Artist · Refs · #22 Bold black brush poster
Ink · 20 px · 30.0 s

![Brush Artist · Refs · #22 Bold black brush poster](Brush-Artist-Refs-22-Bold-black-brush-poster.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 3 % → 5 % | 9.5 px | 0.79 | 1.63 | 31 |
| heavy line | 15 % → 15 % | 44.6 px | 0.88 | 0.99 | 83 |
| pressure swell | 9 % → 9 % | 31.9 px | 0.87 | 1.04 | 48 |
| fast wave | 27 % → 26 % | 31.2 px | 0.87 | 0.98 | 157 |
| slow wave | 22 % → 21 % | 25.2 px | 0.87 | 0.98 | 197 |
| spiral | 34 % → 32 % | 22.2 px | 0.87 | 0.94 | 246 |
| loop | 20 % → 20 % | 26.2 px | 0.88 | 1.00 | 198 |
| tilted | 8 % → 8 % | 22.7 px | 0.88 | 1.01 | 65 |
| over the wet one | 19 % → 19 % | 30.5 px | 0.88 | 1.00 | 136 |
| long, no reload | 45 % → 38 % | 20.2 px | 0.86 | 0.84 | 384 | quarters: 0.54 → 0.45 → 0.35 → 0.27

Numbers say: light vs heavy: width 9.5 → 44.6 px, dark 0.79 → 0.88; wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #23 Dry white on orange + black line
Gouache · 50 px · 27.5 s

![Brush Artist · Refs · #23 Dry white on orange + black line](Brush-Artist-Refs-23-Dry-white-on-orange-black-line.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 12 % → 2 % | 35.1 px | 0.39 | 0.13 | 77 |
| heavy line | 16 % → 2 % | 46.9 px | 0.39 | 0.11 | 196 |
| pressure swell | 11 % → 2 % | 42.6 px | 0.39 | 0.19 | 109 |
| fast wave | 34 % → 3 % | 39.7 px | 0.39 | 0.09 | 374 |
| slow wave | 34 % → 3 % | 39.0 px | 0.39 | 0.10 | 730 |
| spiral | 49 % → 4 % | 32.6 px | 0.38 | 0.07 | 831 |
| loop | 30 % → 4 % | 39.1 px | 0.38 | 0.12 | 368 |
| tilted | 13 % → 12 % | 34.9 px | 0.38 | 0.98 | 188 |
| over the wet one | 26 % → 7 % | 38.0 px | 0.38 | 0.27 | 199 |
| long, no reload | 58 % → 5 % | 26.1 px | 0.38 | 0.09 | 1021 | quarters: 0.02 → 0.02 → 0.03 → 0.04

Numbers say: light vs heavy: width 35.1 → 46.9 px, dark 0.39 → 0.39; the long stroke does not run out of paint.

## Brush Artist · Refs · #24 Picasso flat oil
Oil · 34 px · 22.3 s

![Brush Artist · Refs · #24 Picasso flat oil](Brush-Artist-Refs-24-Picasso-flat-oil.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 11 % → 11 % | 32.2 px | 0.39 | 1.00 | 110 |
| heavy line | 12 % → 12 % | 35.0 px | 0.39 | 1.00 | 106 |
| pressure swell | 9 % → 9 % | 34.4 px | 0.41 | 1.00 | 84 |
| fast wave | 30 % → 30 % | 34.2 px | 0.41 | 1.00 | 305 |
| slow wave | 30 % → 30 % | 34.9 px | 0.41 | 1.00 | 574 |
| spiral | 51 % → 51 % | 33.7 px | 0.40 | 1.00 | 794 |
| loop | 25 % → 25 % | 32.6 px | 0.41 | 1.00 | 362 |
| tilted | 11 % → 11 % | 32.0 px | 0.41 | 1.00 | 244 |
| over the wet one | 22 % → 22 % | 30.7 px | 0.41 | 1.00 | 164 |
| long, no reload | 61 % → 61 % | 27.6 px | 0.39 | 1.00 | 967 | quarters: 0.28 → 0.28 → 0.26 → 0.24

Numbers say: light vs heavy: width 32.2 → 35.0 px, dark 0.39 → 0.39; pressure barely changes the width.

## Brush Artist · Refs · #25 Yellow heavy flat stroke
Heavy acrylic · 110 px · 39.4 s

![Brush Artist · Refs · #25 Yellow heavy flat stroke](Brush-Artist-Refs-25-Yellow-heavy-flat-stroke.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 35 % → 36 % | 101.3 px | 0.30 | 1.02 | 334 |
| heavy line | 36 % → 35 % | 105.0 px | 0.30 | 0.97 | 375 |
| pressure swell | 28 % → 29 % | 105.4 px | 0.30 | 1.04 | 317 |
| fast wave | 72 % → 76 % | 83.8 px | 0.30 | 1.05 | 1652 |
| slow wave | 73 % → 72 % | 84.7 px | 0.29 | 0.98 | 2357 |
| spiral | 86 % → 83 % | 56.7 px | 0.28 | 0.97 | 2081 |
| loop | 65 % → 64 % | 83.6 px | 0.30 | 0.99 | 1043 |
| tilted | 26 % → 26 % | 71.5 px | 0.30 | 1.00 | 544 |
| over the wet one | 55 % → 54 % | 83.1 px | 0.30 | 0.97 | 467 |
| long, no reload | 98 % → 97 % | 44.1 px | 0.29 | 0.99 | 2997 | quarters: 0.00 → 0.00 → 0.00 → 0.00

Numbers say: light vs heavy: width 101.3 → 105.0 px, dark 0.30 → 0.30; pressure barely changes the width; the long stroke does not run out of paint.

## Brush Artist · Refs · #27 Orange impasto swatch
Heavy acrylic · 60 px · 30.0 s

![Brush Artist · Refs · #27 Orange impasto swatch](Brush-Artist-Refs-27-Orange-impasto-swatch.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 20 % → 19 % | 56.7 px | 0.35 | 0.97 | 163 |
| heavy line | 20 % → 20 % | 59.3 px | 0.35 | 0.97 | 155 |
| pressure swell | 16 % → 15 % | 59.6 px | 0.36 | 0.97 | 273 |
| fast wave | 48 % → 46 % | 55.0 px | 0.35 | 0.98 | 630 |
| slow wave | 48 % → 47 % | 55.8 px | 0.36 | 0.98 | 1301 |
| spiral | 69 % → 62 % | 45.5 px | 0.35 | 0.91 | 912 |
| loop | 42 % → 40 % | 53.8 px | 0.35 | 0.97 | 473 |
| tilted | 16 % → 16 % | 44.0 px | 0.36 | 1.00 | 253 |
| over the wet one | 34 % → 33 % | 50.6 px | 0.36 | 0.97 | 212 |
| long, no reload | 85 % → 75 % | 38.1 px | 0.35 | 0.88 | 1271 | quarters: 0.33 → 0.31 → 0.29 → 0.26

Numbers say: light vs heavy: width 56.7 → 59.3 px, dark 0.35 → 0.35; pressure barely changes the width.

## Brush Artist · Refs · #28 Miles Davis black lines
Ink · 22 px · 32.3 s

![Brush Artist · Refs · #28 Miles Davis black lines](Brush-Artist-Refs-28-Miles-Davis-black-lines.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 4 % → 6 % | 12.2 px | 0.81 | 1.48 | 48 |
| heavy line | 17 % → 17 % | 49.1 px | 0.88 | 0.99 | 109 |
| pressure swell | 10 % → 10 % | 35.9 px | 0.87 | 1.03 | 52 |
| fast wave | 30 % → 30 % | 35.0 px | 0.87 | 0.98 | 180 |
| slow wave | 25 % → 25 % | 28.5 px | 0.87 | 0.99 | 341 |
| spiral | 38 % → 37 % | 25.3 px | 0.87 | 0.96 | 268 |
| loop | 23 % → 23 % | 29.4 px | 0.88 | 1.00 | 148 |
| tilted | 9 % → 9 % | 25.0 px | 0.88 | 1.01 | 69 |
| over the wet one | 21 % → 21 % | 34.1 px | 0.88 | 1.00 | 91 |
| long, no reload | 51 % → 43 % | 22.7 px | 0.86 | 0.85 | 363 | quarters: 0.59 → 0.51 → 0.40 → 0.31

Numbers say: light vs heavy: width 12.2 → 49.1 px, dark 0.81 → 0.88.

## Brush Artist · Refs · #29 Shrigley magenta asterisk
Watercolor · 70 px · 35.1 s

![Brush Artist · Refs · #29 Shrigley magenta asterisk](Brush-Artist-Refs-29-Shrigley-magenta-asterisk.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 10 % → 13 % | 28.0 px | 0.65 | 1.36 | 55 |
| heavy line | 17 % → 18 % | 50.3 px | 0.64 | 1.03 | 146 |
| pressure swell | 11 % → 12 % | 41.1 px | 0.65 | 1.13 | 81 |
| fast wave | 38 % → 38 % | 43.7 px | 0.64 | 1.00 | 326 |
| slow wave | 35 % → 39 % | 41.0 px | 0.65 | 1.10 | 527 |
| spiral | 61 % → 61 % | 40.0 px | 0.64 | 1.01 | 470 |
| loop | 31 % → 32 % | 40.2 px | 0.65 | 1.03 | 244 |
| tilted | 18 % → 18 % | 49.0 px | 0.65 | 1.00 | 217 |
| over the wet one | 31 % → 34 % | 38.4 px | 0.65 | 1.07 | 236 |
| long, no reload | 75 % → 75 % | 33.5 px | 0.64 | 1.00 | 775 | quarters: 0.55 → 0.53 → 0.52 → 0.49

Numbers say: light vs heavy: width 28.0 → 50.3 px, dark 0.65 → 0.64; the long stroke does not run out of paint.

## Brush Artist · Refs · #30 Red gouache face patch
Gouache · 60 px · 39.3 s

![Brush Artist · Refs · #30 Red gouache face patch](Brush-Artist-Refs-30-Red-gouache-face-patch.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 16 % → 15 % | 46.9 px | 0.49 | 0.91 | 175 |
| heavy line | 25 % → 20 % | 73.8 px | 0.49 | 0.80 | 240 |
| pressure swell | 19 % → 17 % | 72.6 px | 0.49 | 0.86 | 147 |
| fast wave | 48 % → 28 % | 55.1 px | 0.49 | 0.58 | 487 |
| slow wave | 48 % → 28 % | 55.3 px | 0.49 | 0.59 | 847 |
| spiral | 59 % → 28 % | 39.1 px | 0.49 | 0.48 | 909 |
| loop | 40 % → 29 % | 51.3 px | 0.49 | 0.74 | 434 |
| tilted | 16 % → 16 % | 45.7 px | 0.49 | 1.01 | 310 |
| over the wet one | 36 % → 32 % | 55.3 px | 0.49 | 0.88 | 207 |
| long, no reload | 67 % → 30 % | 30.0 px | 0.49 | 0.45 | 1070 | quarters: 0.43 → 0.38 → 0.32 → 0.26

Numbers say: light vs heavy: width 46.9 → 73.8 px, dark 0.49 → 0.49.

## Brush Artist · Refs · #31 Warhol blotted line
Ink · 6 px · 25.2 s

![Brush Artist · Refs · #31 Warhol blotted line](Brush-Artist-Refs-31-Warhol-blotted-line.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 1 % → 3 % | 2.6 px | 0.75 | 3.30 | 26 |
| heavy line | 7 % → 7 % | 20.6 px | 0.83 | 0.97 | 72 |
| pressure swell | 4 % → 4 % | 14.8 px | 0.84 | 1.12 | 60 |
| fast wave | 12 % → 9 % | 13.8 px | 0.82 | 0.77 | 124 |
| slow wave | 10 % → 8 % | 11.2 px | 0.80 | 0.85 | 106 |
| spiral | 15 % → 9 % | 9.7 px | 0.80 | 0.58 | 215 |
| loop | 9 % → 9 % | 11.9 px | 0.80 | 0.94 | 96 |
| tilted | 3 % → 3 % | 8.6 px | 0.84 | 1.04 | 47 |
| over the wet one | 8 % → 8 % | 14.5 px | 0.84 | 1.02 | 63 |
| long, no reload | 21 % → 9 % | 9.6 px | 0.78 | 0.43 | 350 | quarters: 0.25 → 0.13 → 0.05 → 0.01

Numbers say: light vs heavy: width 2.6 → 20.6 px, dark 0.75 → 0.83; wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #32 Thick orange swipes
Heavy acrylic · 90 px · 32.8 s

![Brush Artist · Refs · #32 Thick orange swipes](Brush-Artist-Refs-32-Thick-orange-swipes.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 29 % → 29 % | 82.9 px | 0.38 | 1.00 | 401 |
| heavy line | 30 % → 29 % | 86.3 px | 0.38 | 0.97 | 420 |
| pressure swell | 23 % → 23 % | 86.5 px | 0.38 | 1.01 | 235 |
| fast wave | 63 % → 65 % | 73.1 px | 0.38 | 1.03 | 856 |
| slow wave | 64 % → 63 % | 73.5 px | 0.39 | 0.98 | 1469 |
| spiral | 79 % → 77 % | 52.2 px | 0.38 | 0.98 | 1967 |
| loop | 57 % → 56 % | 73.4 px | 0.38 | 0.99 | 955 |
| tilted | 21 % → 21 % | 59.3 px | 0.38 | 1.00 | 407 |
| over the wet one | 47 % → 45 % | 70.7 px | 0.38 | 0.97 | 431 |
| long, no reload | 95 % → 93 % | 42.7 px | 0.38 | 0.98 | 2632 | quarters: 0.38 → 0.38 → 0.37 → 0.35

Numbers say: light vs heavy: width 82.9 → 86.3 px, dark 0.38 → 0.38; pressure barely changes the width; the long stroke does not run out of paint.

## Brush Artist · Refs · #33 Red wet-in-wet band
Watercolor · 80 px · 39.7 s

![Brush Artist · Refs · #33 Red wet-in-wet band](Brush-Artist-Refs-33-Red-wet-in-wet-band.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 21 % → 21 % | 60.7 px | 0.66 | 1.01 | 167 |
| heavy line | 30 % → 30 % | 88.4 px | 0.66 | 0.98 | 262 |
| pressure swell | 20 % → 21 % | 75.9 px | 0.67 | 1.03 | 162 |
| fast wave | 61 % → 64 % | 71.0 px | 0.65 | 1.04 | 475 |
| slow wave | 60 % → 60 % | 68.9 px | 0.68 | 1.00 | 976 |
| spiral | 75 % → 75 % | 49.7 px | 0.67 | 1.00 | 885 |
| loop | 52 % → 52 % | 67.5 px | 0.67 | 1.00 | 544 |
| tilted | 24 % → 24 % | 67.8 px | 0.66 | 1.00 | 323 |
| over the wet one | 48 % → 50 % | 66.6 px | 0.66 | 1.04 | 297 |
| long, no reload | 95 % → 96 % | 42.8 px | 0.67 | 1.00 | 1638 | quarters: 0.68 → 0.68 → 0.67 → 0.61

Numbers say: light vs heavy: width 60.7 → 88.4 px, dark 0.66 → 0.66; the long stroke does not run out of paint.

## Brush Artist · Refs · #34 Magenta oil patches
Oil · 60 px · 25.2 s

![Brush Artist · Refs · #34 Magenta oil patches](Brush-Artist-Refs-34-Magenta-oil-patches.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 19 % → 19 % | 55.6 px | 0.59 | 1.00 | 335 |
| heavy line | 21 % → 21 % | 59.7 px | 0.59 | 1.00 | 389 |
| pressure swell | 16 % → 16 % | 58.8 px | 0.62 | 1.01 | 207 |
| fast wave | 48 % → 49 % | 55.4 px | 0.62 | 1.02 | 627 |
| slow wave | 48 % → 48 % | 55.8 px | 0.62 | 1.00 | 1276 |
| spiral | 70 % → 70 % | 46.3 px | 0.62 | 1.00 | 1070 |
| loop | 42 % → 42 % | 54.2 px | 0.62 | 1.00 | 522 |
| tilted | 17 % → 17 % | 46.8 px | 0.62 | 1.00 | 407 |
| over the wet one | 35 % → 35 % | 50.0 px | 0.62 | 1.00 | 257 |
| long, no reload | 86 % → 86 % | 38.7 px | 0.62 | 1.00 | 1389 | quarters: 0.59 → 0.58 → 0.57 → 0.52

Numbers say: light vs heavy: width 55.6 → 59.7 px, dark 0.59 → 0.59; pressure barely changes the width; the long stroke does not run out of paint.

## Brush Artist · Refs · #35 Red band with runs
Watercolor · 70 px · 36.6 s

![Brush Artist · Refs · #35 Red band with runs](Brush-Artist-Refs-35-Red-band-with-runs.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 18 % → 19 % | 53.2 px | 0.57 | 1.05 | 108 |
| heavy line | 27 % → 27 % | 78.7 px | 0.57 | 0.99 | 266 |
| pressure swell | 18 % → 18 % | 67.0 px | 0.59 | 1.02 | 122 |
| fast wave | 56 % → 56 % | 64.8 px | 0.57 | 1.00 | 395 |
| slow wave | 54 % → 55 % | 62.6 px | 0.60 | 1.01 | 786 |
| spiral | 72 % → 72 % | 47.6 px | 0.59 | 0.99 | 923 |
| loop | 48 % → 48 % | 61.7 px | 0.58 | 1.01 | 338 |
| tilted | 22 % → 22 % | 60.5 px | 0.58 | 1.00 | 222 |
| over the wet one | 43 % → 45 % | 59.7 px | 0.58 | 1.05 | 141 |
| long, no reload | 93 % → 92 % | 41.6 px | 0.59 | 0.99 | 882 | quarters: 0.58 → 0.59 → 0.57 → 0.53

Numbers say: light vs heavy: width 53.2 → 78.7 px, dark 0.57 → 0.57; the long stroke does not run out of paint.

## Brush Artist · Refs · #36 Magenta letters flat brush
Gouache · 36 px · 32.3 s

![Brush Artist · Refs · #36 Magenta letters flat brush](Brush-Artist-Refs-36-Magenta-letters-flat-brush.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 10 % → 10 % | 29.0 px | 0.45 | 0.98 | 99 |
| heavy line | 17 % → 14 % | 49.1 px | 0.45 | 0.85 | 143 |
| pressure swell | 13 % → 12 % | 49.4 px | 0.45 | 0.89 | 69 |
| fast wave | 35 % → 19 % | 40.3 px | 0.45 | 0.54 | 349 |
| slow wave | 35 % → 19 % | 39.9 px | 0.45 | 0.54 | 389 |
| spiral | 46 % → 19 % | 30.4 px | 0.45 | 0.42 | 363 |
| loop | 27 % → 20 % | 35.3 px | 0.45 | 0.72 | 224 |
| tilted | 11 % → 11 % | 29.8 px | 0.45 | 1.00 | 112 |
| over the wet one | 24 % → 22 % | 38.1 px | 0.45 | 0.92 | 87 |
| long, no reload | 46 % → 19 % | 20.8 px | 0.45 | 0.40 | 518 | quarters: 0.29 → 0.25 → 0.22 → 0.18

Numbers say: light vs heavy: width 29.0 → 49.1 px, dark 0.45 → 0.45.

## Brush Artist · Refs · #37 Oil still life dabs
Oil · 40 px · 20.3 s

![Brush Artist · Refs · #37 Oil still life dabs](Brush-Artist-Refs-37-Oil-still-life-dabs.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 13 % → 13 % | 37.9 px | 0.39 | 1.00 | 277 |
| heavy line | 14 % → 14 % | 41.1 px | 0.38 | 1.00 | 153 |
| pressure swell | 11 % → 11 % | 40.2 px | 0.40 | 1.00 | 102 |
| fast wave | 34 % → 34 % | 39.8 px | 0.40 | 1.00 | 371 |
| slow wave | 35 % → 35 % | 40.2 px | 0.39 | 1.00 | 600 |
| spiral | 59 % → 59 % | 38.7 px | 0.38 | 1.00 | 622 |
| loop | 29 % → 29 % | 37.8 px | 0.39 | 1.00 | 317 |
| tilted | 13 % → 13 % | 35.8 px | 0.39 | 1.00 | 172 |
| over the wet one | 26 % → 26 % | 35.6 px | 0.39 | 1.00 | 141 |
| long, no reload | 69 % → 69 % | 30.9 px | 0.37 | 1.00 | 865 | quarters: 0.31 → 0.30 → 0.28 → 0.24

Numbers say: light vs heavy: width 37.9 → 41.1 px, dark 0.39 → 0.38; pressure barely changes the width.

## Brush Artist · Refs · #38 Sanguine drawing
Pastel · 6 px · 8.8 s

![Brush Artist · Refs · #38 Sanguine drawing](Brush-Artist-Refs-38-Sanguine-drawing.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 1 % → 1 % | 2.0 px | 0.61 | 1.00 | 9 |
| heavy line | 1 % → 1 % | 3.5 px | 0.62 | 1.00 | 22 |
| pressure swell | 1 % → 1 % | 3.3 px | 0.62 | 1.00 | 14 |
| fast wave | 3 % → 3 % | 3.2 px | 0.61 | 1.00 | 37 |
| slow wave | 3 % → 3 % | 3.0 px | 0.61 | 1.00 | 40 |
| spiral | 4 % → 4 % | 2.9 px | 0.61 | 1.00 | 74 |
| loop | 2 % → 2 % | 3.0 px | 0.61 | 1.00 | 33 |
| tilted | 1 % → 1 % | 3.4 px | 0.62 | 1.00 | 20 |
| over the wet one | 2 % → 2 % | 2.9 px | 0.62 | 1.00 | 15 |
| long, no reload | 7 % → 7 % | 3.0 px | 0.61 | 1.00 | 102 | quarters: 0.04 → 0.05 → 0.05 → 0.05

Numbers say: light vs heavy: width 2.0 → 3.5 px, dark 0.61 → 0.62; the long stroke does not run out of paint.

## Brush Artist · Refs · #39 Very thick impasto
Heavy acrylic · 60 px · 21.1 s

![Brush Artist · Refs · #39 Very thick impasto](Brush-Artist-Refs-39-Very-thick-impasto.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 20 % → 19 % | 56.8 px | 0.61 | 0.97 | 176 |
| heavy line | 20 % → 20 % | 59.4 px | 0.61 | 0.97 | 177 |
| pressure swell | 16 % → 15 % | 59.6 px | 0.62 | 0.97 | 127 |
| fast wave | 48 % → 47 % | 55.2 px | 0.62 | 0.98 | 466 |
| slow wave | 48 % → 47 % | 56.0 px | 0.62 | 0.98 | 775 |
| spiral | 69 % → 65 % | 45.6 px | 0.62 | 0.93 | 791 |
| loop | 42 % → 41 % | 54.0 px | 0.62 | 0.97 | 403 |
| tilted | 16 % → 16 % | 44.0 px | 0.62 | 1.00 | 232 |
| over the wet one | 34 % → 33 % | 50.7 px | 0.62 | 0.97 | 188 |
| long, no reload | 85 % → 79 % | 38.3 px | 0.62 | 0.93 | 1146 | quarters: 0.58 → 0.57 → 0.55 → 0.52

Numbers say: light vs heavy: width 56.8 → 59.4 px, dark 0.61 → 0.61; pressure barely changes the width; the long stroke does not run out of paint.

## Brush Artist · Refs · #40 Watercolour blooms
Watercolor · 90 px · 37.8 s

![Brush Artist · Refs · #40 Watercolour blooms](Brush-Artist-Refs-40-Watercolour-blooms.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 23 % → 24 % | 68.2 px | 0.12 | 1.02 | 140 |
| heavy line | 34 % → 33 % | 98.4 px | 0.12 | 0.98 | 265 |
| pressure swell | 23 % → 24 % | 85.3 px | 0.13 | 1.04 | 148 |
| fast wave | 66 % → 69 % | 76.7 px | 0.12 | 1.04 | 570 |
| slow wave | 65 % → 65 % | 74.7 px | 0.16 | 1.00 | 834 |
| spiral | 79 % → 79 % | 52.0 px | 0.15 | 1.00 | 832 |
| loop | 57 % → 57 % | 73.7 px | 0.14 | 1.00 | 405 |
| tilted | 26 % → 26 % | 73.8 px | 0.14 | 1.00 | 330 |
| over the wet one | 53 % → 55 % | 73.9 px | 0.14 | 1.05 | 222 |
| long, no reload | 97 % → 97 % | 43.5 px | 0.15 | 1.00 | 1251 | quarters: 0.18 → 0.17 → 0.14 → 0.11

Numbers say: light vs heavy: width 68.2 → 98.4 px, dark 0.12 → 0.12.

## Brush Artist · Refs · #41 Coloured pencil hatching
Pastel · 4 px · 8.9 s

![Brush Artist · Refs · #41 Coloured pencil hatching](Brush-Artist-Refs-41-Coloured-pencil-hatching.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 1 % → 1 % | 1.6 px | 0.42 | 1.00 | 10 |
| heavy line | 1 % → 1 % | 2.6 px | 0.43 | 1.00 | 8 |
| pressure swell | 1 % → 1 % | 2.1 px | 0.43 | 1.00 | 5 |
| fast wave | 2 % → 2 % | 2.2 px | 0.42 | 1.00 | 29 |
| slow wave | 2 % → 2 % | 2.1 px | 0.43 | 1.00 | 23 |
| spiral | 3 % → 3 % | 2.1 px | 0.43 | 1.00 | 48 |
| loop | 2 % → 2 % | 2.2 px | 0.43 | 1.00 | 22 |
| tilted | 1 % → 1 % | 3.0 px | 0.42 | 1.00 | 11 |
| over the wet one | 2 % → 2 % | 2.2 px | 0.42 | 1.00 | 15 |
| long, no reload | 5 % → 5 % | 2.3 px | 0.43 | 1.00 | 75 | quarters: 0.02 → 0.02 → 0.02 → 0.03

Numbers say: light vs heavy: width 1.6 → 2.6 px, dark 0.42 → 0.43; the long stroke does not run out of paint.

## Brush Artist · Refs · #42 Oil pastel shaggy
Pastel · 18 px · 9.4 s

![Brush Artist · Refs · #42 Oil pastel shaggy](Brush-Artist-Refs-42-Oil-pastel-shaggy.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 2 % → 2 % | 5.1 px | 0.35 | 1.00 | 21 |
| heavy line | 4 % → 4 % | 10.7 px | 0.36 | 1.00 | 22 |
| pressure swell | 3 % → 3 % | 9.5 px | 0.36 | 1.00 | 17 |
| fast wave | 8 % → 8 % | 9.0 px | 0.36 | 1.00 | 68 |
| slow wave | 7 % → 7 % | 8.2 px | 0.36 | 1.00 | 79 |
| spiral | 12 % → 12 % | 7.7 px | 0.36 | 1.00 | 111 |
| loop | 6 % → 6 % | 7.9 px | 0.36 | 1.00 | 53 |
| tilted | 2 % → 2 % | 6.9 px | 0.36 | 1.00 | 35 |
| over the wet one | 6 % → 6 % | 8.5 px | 0.36 | 1.00 | 28 |
| long, no reload | 15 % → 15 % | 6.9 px | 0.36 | 1.00 | 159 | quarters: 0.00 → 0.00 → 0.00 → 0.00

Numbers say: light vs heavy: width 5.1 → 10.7 px, dark 0.35 → 0.36; the long stroke does not run out of paint.

## Brush Artist · Refs · #43 Dragged black ink blocks
Gouache · 70 px · 29.6 s

![Brush Artist · Refs · #43 Dragged black ink blocks](Brush-Artist-Refs-43-Dragged-black-ink-blocks.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 19 % → 5 % | 54.9 px | 0.57 | 0.28 | 136 |
| heavy line | 24 % → 9 % | 69.0 px | 0.57 | 0.38 | 363 |
| pressure swell | 17 % → 9 % | 63.4 px | 0.57 | 0.53 | 179 |
| fast wave | 51 % → 11 % | 58.7 px | 0.57 | 0.21 | 589 |
| slow wave | 50 % → 10 % | 58.1 px | 0.57 | 0.20 | 887 |
| spiral | 65 % → 14 % | 42.6 px | 0.57 | 0.22 | 920 |
| loop | 45 % → 12 % | 58.1 px | 0.57 | 0.27 | 468 |
| tilted | 17 % → 16 % | 46.4 px | 0.57 | 0.98 | 264 |
| over the wet one | 37 % → 20 % | 55.6 px | 0.57 | 0.56 | 217 |
| long, no reload | 82 % → 17 % | 36.6 px | 0.57 | 0.21 | 1389 | quarters: 0.54 → 0.52 → 0.47 → 0.40

Numbers say: light vs heavy: width 54.9 → 69.0 px, dark 0.57 → 0.57.

## Brush Artist · Refs · #44 Blue looping ribbon
Oil · 80 px · 24.7 s

![Brush Artist · Refs · #44 Blue looping ribbon](Brush-Artist-Refs-44-Blue-looping-ribbon.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 26 % → 27 % | 74.8 px | 0.71 | 1.04 | 252 |
| heavy line | 27 % → 27 % | 79.6 px | 0.71 | 1.00 | 269 |
| pressure swell | 21 % → 21 % | 78.1 px | 0.72 | 1.03 | 197 |
| fast wave | 61 % → 64 % | 70.3 px | 0.73 | 1.05 | 719 |
| slow wave | 61 % → 61 % | 70.0 px | 0.73 | 1.00 | 1257 |
| spiral | 78 % → 78 % | 51.3 px | 0.73 | 1.00 | 1230 |
| loop | 54 % → 54 % | 69.7 px | 0.72 | 1.00 | 641 |
| tilted | 20 % → 20 % | 57.2 px | 0.71 | 1.00 | 347 |
| over the wet one | 44 % → 44 % | 64.9 px | 0.71 | 1.00 | 291 |
| long, no reload | 96 % → 96 % | 42.8 px | 0.73 | 1.00 | 1809 | quarters: 0.72 → 0.72 → 0.72 → 0.69

Numbers say: light vs heavy: width 74.8 → 79.6 px, dark 0.71 → 0.71; pressure barely changes the width; the long stroke does not run out of paint.

## Brush Artist · Refs · #45 Soft pastel pepper
Pastel · 40 px · 9.9 s

![Brush Artist · Refs · #45 Soft pastel pepper](Brush-Artist-Refs-45-Soft-pastel-pepper.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 4 % → 4 % | 11.3 px | 0.53 | 1.00 | 47 |
| heavy line | 8 % → 8 % | 23.0 px | 0.53 | 1.00 | 44 |
| pressure swell | 5 % → 5 % | 19.5 px | 0.53 | 1.00 | 82 |
| fast wave | 17 % → 17 % | 19.4 px | 0.53 | 1.00 | 112 |
| slow wave | 15 % → 15 % | 17.1 px | 0.53 | 1.00 | 216 |
| spiral | 25 % → 25 % | 16.3 px | 0.53 | 1.00 | 214 |
| loop | 12 % → 12 % | 16.1 px | 0.53 | 1.00 | 97 |
| tilted | 5 % → 5 % | 12.8 px | 0.53 | 1.00 | 71 |
| over the wet one | 11 % → 11 % | 17.7 px | 0.53 | 1.00 | 44 |
| long, no reload | 30 % → 30 % | 13.6 px | 0.53 | 1.00 | 297 | quarters: 0.18 → 0.18 → 0.18 → 0.18

Numbers say: light vs heavy: width 11.3 → 23.0 px, dark 0.53 → 0.53; the long stroke does not run out of paint.

## Brush Artist · Refs · #46 Red-brown ink lips
Watercolor · 70 px · 34.7 s

![Brush Artist · Refs · #46 Red-brown ink lips](Brush-Artist-Refs-46-Red-brown-ink-lips.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 18 % → 18 % | 53.2 px | 0.74 | 1.00 | 90 |
| heavy line | 27 % → 27 % | 78.7 px | 0.74 | 0.98 | 182 |
| pressure swell | 18 % → 18 % | 67.0 px | 0.75 | 1.01 | 104 |
| fast wave | 56 % → 58 % | 64.8 px | 0.73 | 1.03 | 333 |
| slow wave | 54 % → 54 % | 62.6 px | 0.74 | 1.00 | 552 |
| spiral | 72 % → 72 % | 47.6 px | 0.74 | 1.00 | 573 |
| loop | 48 % → 48 % | 61.7 px | 0.74 | 1.00 | 299 |
| tilted | 22 % → 22 % | 60.5 px | 0.74 | 1.00 | 227 |
| over the wet one | 43 % → 44 % | 59.9 px | 0.74 | 1.03 | 131 |
| long, no reload | 93 % → 93 % | 41.6 px | 0.74 | 1.00 | 835 | quarters: 0.73 → 0.73 → 0.72 → 0.67

Numbers say: light vs heavy: width 53.2 → 78.7 px, dark 0.74 → 0.74; the long stroke does not run out of paint.

## Brush Artist · Refs · #47 Pink knife slabs
Heavy acrylic · 90 px · 26.3 s

![Brush Artist · Refs · #47 Pink knife slabs](Brush-Artist-Refs-47-Pink-knife-slabs.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 28 % → 27 % | 81.0 px | 0.28 | 0.97 | 198 |
| heavy line | 29 % → 28 % | 83.4 px | 0.28 | 0.97 | 225 |
| pressure swell | 22 % → 22 % | 83.4 px | 0.28 | 1.01 | 131 |
| fast wave | 61 % → 60 % | 70.1 px | 0.27 | 0.98 | 515 |
| slow wave | 61 % → 59 % | 70.9 px | 0.26 | 0.96 | 905 |
| spiral | 76 % → 58 % | 50.0 px | 0.26 | 0.76 | 902 |
| loop | 55 % → 54 % | 71.7 px | 0.27 | 0.97 | 477 |
| tilted | 21 % → 21 % | 59.3 px | 0.28 | 1.00 | 233 |
| over the wet one | 46 % → 44 % | 67.9 px | 0.28 | 0.96 | 201 |
| long, no reload | 92 % → 76 % | 41.3 px | 0.26 | 0.83 | 1264 | quarters: 0.00 → 0.00 → 0.00 → 0.00

Numbers say: light vs heavy: width 81.0 → 83.4 px, dark 0.28 → 0.28; pressure barely changes the width; the long stroke does not run out of paint.

## Brush Artist · Refs · #48 Black bands with drips
Gouache · 70 px · 39.7 s

![Brush Artist · Refs · #48 Black bands with drips](Brush-Artist-Refs-48-Black-bands-with-drips.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 19 % → 18 % | 54.6 px | 0.69 | 0.93 | 163 |
| heavy line | 29 % → 24 % | 83.0 px | 0.69 | 0.84 | 239 |
| pressure swell | 23 % → 21 % | 86.1 px | 0.69 | 0.92 | 169 |
| fast wave | 53 % → 36 % | 61.8 px | 0.69 | 0.68 | 499 |
| slow wave | 53 % → 36 % | 61.7 px | 0.69 | 0.67 | 887 |
| spiral | 64 % → 35 % | 41.9 px | 0.69 | 0.55 | 818 |
| loop | 45 % → 36 % | 57.8 px | 0.69 | 0.81 | 432 |
| tilted | 19 % → 19 % | 52.3 px | 0.69 | 1.00 | 258 |
| over the wet one | 41 % → 38 % | 62.4 px | 0.69 | 0.92 | 221 |
| long, no reload | 74 % → 37 % | 33.3 px | 0.69 | 0.50 | 1202 | quarters: 0.64 → 0.61 → 0.54 → 0.45

Numbers say: light vs heavy: width 54.6 → 83.0 px, dark 0.69 → 0.69.

## Brush Artist · Refs · #49 Magenta letters round brush
Ink · 30 px · 29.3 s

![Brush Artist · Refs · #49 Magenta letters round brush](Brush-Artist-Refs-49-Magenta-letters-round-brush.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 6 % → 8 % | 17.5 px | 0.50 | 1.28 | 32 |
| heavy line | 21 % → 21 % | 62.0 px | 0.51 | 0.99 | 108 |
| pressure swell | 12 % → 13 % | 46.3 px | 0.52 | 1.01 | 55 |
| fast wave | 38 % → 38 % | 44.3 px | 0.51 | 0.99 | 188 |
| slow wave | 32 % → 31 % | 36.4 px | 0.51 | 0.99 | 297 |
| spiral | 50 % → 48 % | 32.8 px | 0.51 | 0.97 | 294 |
| loop | 29 % → 29 % | 37.6 px | 0.51 | 1.00 | 151 |
| tilted | 11 % → 11 % | 30.7 px | 0.52 | 1.01 | 78 |
| over the wet one | 26 % → 26 % | 42.1 px | 0.52 | 1.01 | 68 |
| long, no reload | 61 % → 56 % | 27.5 px | 0.51 | 0.92 | 442 | quarters: 0.41 → 0.36 → 0.30 → 0.25

Numbers say: light vs heavy: width 17.5 → 62.0 px, dark 0.50 → 0.51.

## Brush Artist · Refs · #50 Thick swipes on photo
Heavy acrylic · 40 px · 16.7 s

![Brush Artist · Refs · #50 Thick swipes on photo](Brush-Artist-Refs-50-Thick-swipes-on-photo.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 13 % → 13 % | 38.0 px | 0.25 | 0.96 | 111 |
| heavy line | 14 % → 13 % | 40.1 px | 0.25 | 0.96 | 115 |
| pressure swell | 11 % → 10 % | 40.1 px | 0.25 | 0.95 | 87 |
| fast wave | 33 % → 31 % | 38.3 px | 0.25 | 0.93 | 281 |
| slow wave | 34 % → 32 % | 39.1 px | 0.25 | 0.95 | 488 |
| spiral | 58 % → 47 % | 38.5 px | 0.24 | 0.80 | 491 |
| loop | 28 % → 27 % | 36.8 px | 0.26 | 0.95 | 245 |
| tilted | 12 % → 12 % | 34.0 px | 0.25 | 1.00 | 123 |
| over the wet one | 25 % → 24 % | 35.2 px | 0.25 | 0.95 | 110 |
| long, no reload | 66 % → 46 % | 29.5 px | 0.24 | 0.70 | 709 | quarters: 0.00 → 0.00 → 0.00 → 0.00

Numbers say: light vs heavy: width 38.0 → 40.1 px, dark 0.25 → 0.25; pressure barely changes the width; the long stroke does not run out of paint.

## Brush Artist · Ink — wash
Watercolor · 38 px · 29.3 s

![Brush Artist · Ink — wash](Brush-Artist-Ink-wash.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 11 % → 11 % | 31.6 px | 0.38 | 1.03 | 60 |
| heavy line | 19 % → 19 % | 54.3 px | 0.32 | 1.03 | 95 |
| pressure swell | 12 % → 12 % | 45.1 px | 0.36 | 1.04 | 60 |
| fast wave | 39 % → 41 % | 44.7 px | 0.30 | 1.05 | 175 |
| slow wave | 37 % → 38 % | 42.6 px | 0.37 | 1.04 | 306 |
| spiral | 57 % → 60 % | 37.9 px | 0.30 | 1.04 | 319 |
| loop | 32 % → 33 % | 41.8 px | 0.34 | 1.02 | 174 |
| tilted | 13 % → 14 % | 36.8 px | 0.38 | 1.04 | 105 |
| over the wet one | 29 % → 30 % | 42.8 px | 0.38 | 1.04 | 77 |
| long, no reload | 65 % → 70 % | 29.2 px | 0.29 | 1.08 | 469 | quarters: 0.33 → 0.26 → 0.18 → 0.11

Numbers say: light vs heavy: width 31.6 → 54.3 px, dark 0.38 → 0.32.

## Brush Artist · Ink — brush line
Ink · 16 px · 23.8 s

![Brush Artist · Ink — brush line](Brush-Artist-Ink-brush-line.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 3 % → 5 % | 7.7 px | 0.78 | 1.80 | 35 |
| heavy line | 13 % → 13 % | 39.0 px | 0.88 | 0.99 | 72 |
| pressure swell | 8 % → 8 % | 28.4 px | 0.87 | 1.05 | 44 |
| fast wave | 24 % → 23 % | 27.6 px | 0.87 | 0.96 | 136 |
| slow wave | 19 % → 19 % | 22.5 px | 0.87 | 0.97 | 163 |
| spiral | 30 % → 27 % | 19.9 px | 0.86 | 0.90 | 234 |
| loop | 18 % → 18 % | 23.4 px | 0.88 | 1.00 | 113 |
| tilted | 7 % → 7 % | 20.1 px | 0.88 | 1.01 | 53 |
| over the wet one | 17 % → 17 % | 26.8 px | 0.88 | 1.00 | 53 |
| long, no reload | 42 % → 31 % | 18.8 px | 0.85 | 0.73 | 329 | quarters: 0.49 → 0.40 → 0.30 → 0.21

Numbers say: light vs heavy: width 7.7 → 39.0 px, dark 0.78 → 0.88; wet paint spreads well beyond the stroke.

## Brush Artist · Ink — dry brush
Gouache · 30 px · 20.6 s

![Brush Artist · Ink — dry brush](Brush-Artist-Ink-dry-brush.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 7 % → 1 % | 21.8 px | 0.71 | 0.11 | 50 |
| heavy line | 10 % → 1 % | 27.7 px | 0.71 | 0.10 | 119 |
| pressure swell | 7 % → 2 % | 25.5 px | 0.71 | 0.23 | 62 |
| fast wave | 21 % → 2 % | 24.2 px | 0.71 | 0.09 | 161 |
| slow wave | 21 % → 2 % | 23.9 px | 0.71 | 0.08 | 380 |
| spiral | 31 % → 2 % | 20.6 px | 0.71 | 0.06 | 355 |
| loop | 18 % → 2 % | 23.9 px | 0.71 | 0.13 | 178 |
| tilted | 9 % → 8 % | 24.1 px | 0.71 | 0.96 | 101 |
| over the wet one | 17 % → 4 % | 22.8 px | 0.71 | 0.24 | 78 |
| long, no reload | 31 % → 3 % | 14.0 px | 0.71 | 0.09 | 536 | quarters: 0.38 → 0.32 → 0.22 → 0.09

Numbers say: light vs heavy: width 21.8 → 27.7 px, dark 0.71 → 0.71.

## Brush Artist · Watercolour — blue
Watercolor · 40 px · 26.1 s

![Brush Artist · Watercolour — blue](Brush-Artist-Watercolour-blue.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 6 % → 10 % | 16.7 px | 0.25 | 1.70 | 30 |
| heavy line | 11 % → 12 % | 31.5 px | 0.25 | 1.13 | 68 |
| pressure swell | 7 % → 9 % | 25.4 px | 0.26 | 1.32 | 47 |
| fast wave | 24 % → 25 % | 27.8 px | 0.24 | 1.05 | 135 |
| slow wave | 22 % → 27 % | 25.9 px | 0.26 | 1.22 | 211 |
| spiral | 38 % → 41 % | 25.1 px | 0.22 | 1.08 | 227 |
| loop | 20 % → 22 % | 25.3 px | 0.26 | 1.13 | 129 |
| tilted | 12 % → 12 % | 33.3 px | 0.26 | 1.00 | 84 |
| over the wet one | 21 % → 24 % | 24.7 px | 0.26 | 1.15 | 49 |
| long, no reload | 51 % → 54 % | 23.0 px | 0.22 | 1.04 | 326 | quarters: 0.18 → 0.14 → 0.11 → 0.08

Numbers say: light vs heavy: width 16.7 → 31.5 px, dark 0.25 → 0.25; wet paint spreads well beyond the stroke.

## Brush Artist · Watercolour — violet
Watercolor · 40 px · 25.5 s

![Brush Artist · Watercolour — violet](Brush-Artist-Watercolour-violet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 6 % → 10 % | 16.7 px | 0.40 | 1.70 | 30 |
| heavy line | 11 % → 12 % | 31.5 px | 0.40 | 1.13 | 70 |
| pressure swell | 7 % → 9 % | 25.4 px | 0.41 | 1.32 | 35 |
| fast wave | 24 % → 25 % | 27.8 px | 0.38 | 1.05 | 131 |
| slow wave | 22 % → 27 % | 25.9 px | 0.40 | 1.22 | 196 |
| spiral | 38 % → 41 % | 25.1 px | 0.36 | 1.08 | 209 |
| loop | 20 % → 22 % | 25.3 px | 0.40 | 1.13 | 112 |
| tilted | 12 % → 12 % | 33.3 px | 0.40 | 1.00 | 86 |
| over the wet one | 21 % → 24 % | 24.7 px | 0.40 | 1.15 | 55 |
| long, no reload | 51 % → 54 % | 23.0 px | 0.34 | 1.04 | 335 | quarters: 0.28 → 0.22 → 0.17 → 0.14

Numbers say: light vs heavy: width 16.7 → 31.5 px, dark 0.40 → 0.40; wet paint spreads well beyond the stroke.

## Brush Artist · Watercolour — teal
Watercolor · 40 px · 25.6 s

![Brush Artist · Watercolour — teal](Brush-Artist-Watercolour-teal.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 6 % → 10 % | 16.7 px | 0.16 | 1.70 | 29 |
| heavy line | 11 % → 12 % | 31.5 px | 0.16 | 1.13 | 68 |
| pressure swell | 7 % → 9 % | 25.4 px | 0.17 | 1.32 | 32 |
| fast wave | 24 % → 25 % | 27.8 px | 0.15 | 1.05 | 127 |
| slow wave | 22 % → 27 % | 25.9 px | 0.17 | 1.22 | 220 |
| spiral | 38 % → 41 % | 25.1 px | 0.15 | 1.08 | 205 |
| loop | 20 % → 22 % | 25.3 px | 0.16 | 1.13 | 107 |
| tilted | 12 % → 12 % | 33.3 px | 0.16 | 1.00 | 90 |
| over the wet one | 21 % → 24 % | 24.7 px | 0.16 | 1.15 | 46 |
| long, no reload | 51 % → 54 % | 23.0 px | 0.14 | 1.04 | 365 | quarters: 0.11 → 0.09 → 0.07 → 0.06

Numbers say: light vs heavy: width 16.7 → 31.5 px, dark 0.16 → 0.16; wet paint spreads well beyond the stroke.

## Brush Artist · Gouache
Gouache · 30 px · 30.0 s

![Brush Artist · Gouache](Brush-Artist-Gouache.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 8 % → 8 % | 24.4 px | 0.27 | 0.97 | 60 |
| heavy line | 15 % → 11 % | 42.8 px | 0.27 | 0.78 | 91 |
| pressure swell | 11 % → 9 % | 41.0 px | 0.27 | 0.84 | 57 |
| fast wave | 30 % → 13 % | 34.4 px | 0.26 | 0.45 | 177 |
| slow wave | 29 % → 14 % | 33.9 px | 0.26 | 0.46 | 312 |
| spiral | 40 % → 14 % | 26.6 px | 0.26 | 0.35 | 330 |
| loop | 23 % → 15 % | 30.4 px | 0.26 | 0.62 | 161 |
| tilted | 10 % → 10 % | 27.1 px | 0.26 | 1.01 | 90 |
| over the wet one | 21 % → 19 % | 32.8 px | 0.26 | 0.89 | 83 |
| long, no reload | 43 % → 15 % | 19.1 px | 0.26 | 0.35 | 498 | quarters: 0.01 → 0.01 → 0.01 → 0.01

Numbers say: light vs heavy: width 24.4 → 42.8 px, dark 0.27 → 0.27; the long stroke does not run out of paint.

## Brush Artist · Oil — bristle
Oil · 30 px · 17.5 s

![Brush Artist · Oil — bristle](Brush-Artist-Oil-bristle.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 9 % → 9 % | 26.2 px | 0.54 | 1.00 | 86 |
| heavy line | 10 % → 10 % | 28.5 px | 0.54 | 1.00 | 102 |
| pressure swell | 8 % → 8 % | 28.2 px | 0.55 | 1.00 | 85 |
| fast wave | 24 % → 24 % | 27.3 px | 0.55 | 1.00 | 258 |
| slow wave | 24 % → 24 % | 28.2 px | 0.55 | 1.00 | 452 |
| spiral | 39 % → 39 % | 25.6 px | 0.54 | 1.00 | 444 |
| loop | 20 % → 20 % | 26.2 px | 0.54 | 1.00 | 238 |
| tilted | 11 % → 11 % | 29.9 px | 0.54 | 1.00 | 138 |
| over the wet one | 20 % → 20 % | 25.2 px | 0.54 | 1.00 | 108 |
| long, no reload | 50 % → 50 % | 22.4 px | 0.54 | 1.00 | 688 | quarters: 0.32 → 0.30 → 0.29 → 0.28

Numbers say: light vs heavy: width 26.2 → 28.5 px, dark 0.54 → 0.54; pressure barely changes the width; the long stroke does not run out of paint.

## Brush Artist · Charcoal — stick
Charcoal · 28 px · 9.7 s

![Brush Artist · Charcoal — stick](Brush-Artist-Charcoal-stick.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 3 % → 3 % | 8.4 px | 0.85 | 1.00 | 22 |
| heavy line | 6 % → 6 % | 17.8 px | 0.85 | 1.00 | 19 |
| pressure swell | 4 % → 4 % | 13.9 px | 0.85 | 1.00 | 15 |
| fast wave | 12 % → 12 % | 14.0 px | 0.85 | 1.00 | 44 |
| slow wave | 11 % → 11 % | 12.5 px | 0.85 | 1.00 | 88 |
| spiral | 19 % → 19 % | 12.7 px | 0.85 | 1.00 | 77 |
| loop | 10 % → 10 % | 12.8 px | 0.85 | 1.00 | 43 |
| tilted | 4 % → 4 % | 10.9 px | 0.85 | 1.00 | 31 |
| over the wet one | 9 % → 9 % | 13.5 px | 0.85 | 1.00 | 20 |
| long, no reload | 27 % → 27 % | 12.2 px | 0.85 | 1.00 | 105 | quarters: 0.26 → 0.25 → 0.26 → 0.27

Numbers say: light vs heavy: width 8.4 → 17.8 px, dark 0.85 → 0.85; the long stroke does not run out of paint.

## Brush Artist · Charcoal — stick B
Charcoal · 36 px · 9.6 s

![Brush Artist · Charcoal — stick B](Brush-Artist-Charcoal-stick-B.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 4 % → 4 % | 10.5 px | 0.85 | 1.00 | 19 |
| heavy line | 7 % → 7 % | 21.1 px | 0.85 | 1.00 | 38 |
| pressure swell | 4 % → 4 % | 16.5 px | 0.85 | 1.00 | 21 |
| fast wave | 15 % → 15 % | 16.8 px | 0.85 | 1.00 | 62 |
| slow wave | 13 % → 13 % | 14.7 px | 0.85 | 1.00 | 119 |
| spiral | 23 % → 23 % | 15.0 px | 0.85 | 1.00 | 112 |
| loop | 11 % → 11 % | 14.8 px | 0.85 | 1.00 | 47 |
| tilted | 4 % → 4 % | 12.3 px | 0.85 | 1.00 | 40 |
| over the wet one | 10 % → 10 % | 15.9 px | 0.85 | 1.00 | 22 |
| long, no reload | 31 % → 31 % | 13.9 px | 0.85 | 1.00 | 159 | quarters: 0.30 → 0.28 → 0.29 → 0.30

Numbers say: light vs heavy: width 10.5 → 21.1 px, dark 0.85 → 0.85; the long stroke does not run out of paint.

## Brush Artist · Charcoal — stick C
Charcoal · 22 px · 10.6 s

![Brush Artist · Charcoal — stick C](Brush-Artist-Charcoal-stick-C.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 2 % → 2 % | 6.9 px | 0.85 | 1.00 | 18 |
| heavy line | 5 % → 5 % | 15.3 px | 0.85 | 1.00 | 17 |
| pressure swell | 3 % → 3 % | 12.2 px | 0.85 | 1.00 | 13 |
| fast wave | 10 % → 10 % | 12.1 px | 0.85 | 1.00 | 43 |
| slow wave | 9 % → 9 % | 10.8 px | 0.85 | 1.00 | 62 |
| spiral | 17 % → 17 % | 11.0 px | 0.85 | 1.00 | 75 |
| loop | 9 % → 9 % | 11.4 px | 0.85 | 1.00 | 35 |
| tilted | 4 % → 4 % | 9.9 px | 0.85 | 1.00 | 24 |
| over the wet one | 8 % → 8 % | 11.7 px | 0.85 | 1.00 | 11 |
| long, no reload | 24 % → 24 % | 11.0 px | 0.85 | 1.00 | 100 | quarters: 0.24 → 0.22 → 0.23 → 0.24

Numbers say: light vs heavy: width 6.9 → 15.3 px, dark 0.85 → 0.85; the long stroke does not run out of paint.

## Brush Artist · Refs · #01 Henry Ward peach cloud — own sheet
own sheet 600 × 600 · Gouache · 44 px · 14.2 s

![Brush Artist · Refs · #01 Henry Ward peach cloud — own sheet](Brush-Artist-Refs-01-Henry-Ward-peach-cloud-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 35 % → 49 % | 45.3 px | 0.60 | 1.39 | 158 |
| stroke 2 | 41 % → 66 % | 66.4 px | 0.60 | 1.59 | 134 |
| stroke 3 | 45 % → 75 % | 59.4 px | 0.60 | 1.67 | 149 |
| stroke 4 | 49 % → 71 % | 79.7 px | 0.60 | 1.45 | 133 |
| stroke 5 | 41 % → 69 % | 56.0 px | 0.60 | 1.67 | 144 |
| stroke 6 | 49 % → 55 % | 72.6 px | 0.60 | 1.12 | 155 |
| stroke 7 | 33 % → 60 % | 45.2 px | 0.60 | 1.83 | 151 |
| stroke 8 | 38 % → 62 % | 48.5 px | 0.60 | 1.66 | 156 |
| stroke 9 | 46 % → 69 % | 57.7 px | 0.60 | 1.49 | 166 |
| stroke 10 | 52 % → 74 % | 64.8 px | 0.60 | 1.44 | 186 |
| stroke 11 | 53 % → 77 % | 73.3 px | 0.60 | 1.45 | 155 |
| stroke 12 | 62 % → 89 % | 84.4 px | 0.60 | 1.43 | 170 |
| stroke 13 | 61 % → 85 % | 81.3 px | 0.60 | 1.39 | 146 |
| stroke 14 | 60 % → 85 % | 77.8 px | 0.60 | 1.42 | 171 |
| stroke 15 | 67 % → 87 % | 91.2 px | 0.60 | 1.29 | 161 |
| stroke 16 | 73 % → 90 % | 101.7 px | 0.60 | 1.24 | 146 |
| stroke 17 | 70 % → 86 % | 86.2 px | 0.60 | 1.24 | 168 |
| stroke 18 | 71 % → 86 % | 93.2 px | 0.60 | 1.22 | 167 |
| stroke 19 | 74 % → 86 % | 91.5 px | 0.60 | 1.17 | 171 |
| stroke 20 | 73 % → 83 % | 96.9 px | 0.60 | 1.14 | 157 |
| stroke 21 | 73 % → 78 % | 98.6 px | 0.60 | 1.06 | 154 |
| stroke 22 | 76 % → 80 % | 102.2 px | 0.60 | 1.05 | 175 |
| stroke 23 | 75 % → 76 % | 95.9 px | 0.60 | 1.01 | 169 |
| stroke 24 | 80 % → 80 % | 107.6 px | 0.60 | 1.00 | 152 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #02 Henry Ward cream strokes — own sheet
own sheet 600 × 600 · Gouache · 46 px · 9.5 s

![Brush Artist · Refs · #02 Henry Ward cream strokes — own sheet](Brush-Artist-Refs-02-Henry-Ward-cream-strokes-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 34 % → 39 % | 43.6 px | 0.73 | 1.18 | 221 |
| stroke 2 | 37 % → 38 % | 53.2 px | 0.73 | 1.01 | 209 |
| stroke 3 | 32 % → 42 % | 44.2 px | 0.73 | 1.32 | 222 |
| stroke 4 | 39 % → 59 % | 53.3 px | 0.73 | 1.52 | 231 |
| stroke 5 | 56 % → 55 % | 72.7 px | 0.73 | 0.98 | 212 |
| stroke 6 | 36 % → 51 % | 43.6 px | 0.73 | 1.42 | 218 |
| stroke 7 | 50 % → 49 % | 63.7 px | 0.73 | 0.98 | 188 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #03 Henry Ward navy contours — own sheet
own sheet 600 × 600 · Heavy acrylic · 22 px · 2.5 s

![Brush Artist · Refs · #03 Henry Ward navy contours — own sheet](Brush-Artist-Refs-03-Henry-Ward-navy-contours-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 15 % → 20 % | 23.1 px | 0.69 | 1.28 | 123 |
| stroke 2 | 28 % → 30 % | 26.3 px | 0.69 | 1.09 | 90 |
| stroke 3 | 28 % → 28 % | 29.4 px | 0.70 | 0.99 | 128 |
| stroke 4 | 26 % → 24 % | 45.9 px | 0.69 | 0.92 | 156 |

## Brush Artist · Refs · #04 Henry Ward grey cloud — own sheet
own sheet 600 × 600 · Gouache · 50 px · 13.3 s

![Brush Artist · Refs · #04 Henry Ward grey cloud — own sheet](Brush-Artist-Refs-04-Henry-Ward-grey-cloud-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 33 % → 59 % | 49.5 px | 0.40 | 1.81 | 205 |
| stroke 2 | 38 % → 64 % | 58.2 px | 0.40 | 1.68 | 232 |
| stroke 3 | 59 % → 82 % | 81.0 px | 0.40 | 1.39 | 222 |
| stroke 4 | 58 % → 83 % | 87.5 px | 0.40 | 1.41 | 235 |
| stroke 5 | 61 % → 86 % | 90.7 px | 0.40 | 1.41 | 214 |
| stroke 6 | 61 % → 89 % | 98.2 px | 0.40 | 1.45 | 190 |
| stroke 7 | 60 % → 84 % | 88.7 px | 0.40 | 1.39 | 229 |
| stroke 8 | 57 % → 84 % | 85.9 px | 0.40 | 1.48 | 226 |
| stroke 9 | 60 % → 86 % | 88.9 px | 0.40 | 1.44 | 204 |
| stroke 10 | 61 % → 88 % | 98.3 px | 0.40 | 1.44 | 199 |
| stroke 11 | 61 % → 86 % | 83.2 px | 0.40 | 1.40 | 209 |
| stroke 12 | 62 % → 86 % | 94.7 px | 0.40 | 1.38 | 206 |
| stroke 13 | 62 % → 86 % | 84.6 px | 0.40 | 1.39 | 217 |
| stroke 14 | 60 % → 84 % | 93.4 px | 0.40 | 1.39 | 220 |
| stroke 15 | 60 % → 83 % | 88.4 px | 0.40 | 1.38 | 214 |
| stroke 16 | 61 % → 84 % | 96.2 px | 0.40 | 1.38 | 212 |
| stroke 17 | 60 % → 84 % | 84.0 px | 0.40 | 1.41 | 207 |
| stroke 18 | 61 % → 84 % | 96.8 px | 0.40 | 1.39 | 189 |
| stroke 19 | 60 % → 62 % | 89.9 px | 0.40 | 1.03 | 197 |
| stroke 20 | 61 % → 61 % | 99.6 px | 0.40 | 0.99 | 224 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #05 Henry Ward green in rust loops — own sheet
own sheet 600 × 600 · Heavy acrylic · 20 px · 2.3 s

![Brush Artist · Refs · #05 Henry Ward green in rust loops — own sheet](Brush-Artist-Refs-05-Henry-Ward-green-in-rust-loops-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 16 % → 24 % | 20.9 px | 0.02 | 1.48 | 101 |
| stroke 2 | 15 % → 13 % | 22.7 px | 0.03 | 0.90 | 138 |
| stroke 3 | 25 % → 24 % | 37.1 px | 0.02 | 0.94 | 119 |

## Brush Artist · Refs · #06 Henry Ward scrubbed grey — own sheet
own sheet 600 × 600 · Gouache · 50 px · 15.2 s

![Brush Artist · Refs · #06 Henry Ward scrubbed grey — own sheet](Brush-Artist-Refs-06-Henry-Ward-scrubbed-grey-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 35 % → 59 % | 49.2 px | 0.40 | 1.71 | 219 |
| stroke 2 | 41 % → 66 % | 64.6 px | 0.40 | 1.58 | 231 |
| stroke 3 | 59 % → 89 % | 86.2 px | 0.40 | 1.51 | 192 |
| stroke 4 | 58 % → 88 % | 92.9 px | 0.40 | 1.51 | 211 |
| stroke 5 | 56 % → 86 % | 84.4 px | 0.40 | 1.53 | 310 |
| stroke 6 | 60 % → 86 % | 93.2 px | 0.40 | 1.44 | 211 |
| stroke 7 | 61 % → 85 % | 88.7 px | 0.40 | 1.38 | 222 |
| stroke 8 | 62 % → 88 % | 98.2 px | 0.40 | 1.43 | 214 |
| stroke 9 | 61 % → 89 % | 88.8 px | 0.40 | 1.46 | 192 |
| stroke 10 | 59 % → 89 % | 95.5 px | 0.40 | 1.50 | 180 |
| stroke 11 | 60 % → 84 % | 85.9 px | 0.40 | 1.42 | 219 |
| stroke 12 | 58 % → 83 % | 93.4 px | 0.40 | 1.43 | 221 |
| stroke 13 | 58 % → 83 % | 83.2 px | 0.40 | 1.44 | 226 |
| stroke 14 | 56 % → 84 % | 84.9 px | 0.40 | 1.49 | 235 |
| stroke 15 | 58 % → 85 % | 83.3 px | 0.40 | 1.46 | 222 |
| stroke 16 | 63 % → 90 % | 96.7 px | 0.40 | 1.44 | 203 |
| stroke 17 | 61 % → 86 % | 88.7 px | 0.40 | 1.42 | 200 |
| stroke 18 | 61 % → 85 % | 95.6 px | 0.40 | 1.39 | 221 |
| stroke 19 | 57 % → 85 % | 87.0 px | 0.40 | 1.49 | 210 |
| stroke 20 | 58 % → 84 % | 93.6 px | 0.40 | 1.45 | 231 |
| stroke 21 | 58 % → 68 % | 84.6 px | 0.40 | 1.17 | 209 |
| stroke 22 | 62 % → 61 % | 98.3 px | 0.40 | 0.99 | 210 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #07 Henry Ward blue L + black zigzag — own sheet
own sheet 600 × 600 · Heavy acrylic · 34 px · 1.9 s

![Brush Artist · Refs · #07 Henry Ward blue L + black zigzag — own sheet](Brush-Artist-Refs-07-Henry-Ward-blue-L-black-zigzag-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 30 % → 31 % | 35.6 px | 0.59 | 1.05 | 110 |
| stroke 2 | 31 % → 29 % | 38.6 px | 0.59 | 0.94 | 88 |

## Brush Artist · Refs · #08 Henry Ward olive bands — own sheet
own sheet 600 × 600 · Gouache · 34 px · 5.5 s

![Brush Artist · Refs · #08 Henry Ward olive bands — own sheet](Brush-Artist-Refs-08-Henry-Ward-olive-bands-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 33 % → 19 % | 32.3 px | 0.57 | 0.58 | 175 |
| stroke 2 | 37 % → 20 % | 44.3 px | 0.57 | 0.53 | 167 |
| stroke 3 | 30 % → 23 % | 32.4 px | 0.57 | 0.75 | 157 |
| stroke 4 | 38 % → 37 % | 44.3 px | 0.57 | 0.98 | 172 |
| stroke 5 | 50 % → 35 % | 52.4 px | 0.57 | 0.71 | 171 |
| stroke 6 | 36 % → 22 % | 32.2 px | 0.57 | 0.61 | 174 |

## Brush Artist · Refs · #09 Henry Ward white loops — own sheet
own sheet 600 × 600 · Gouache · 46 px · 8.6 s

![Brush Artist · Refs · #09 Henry Ward white loops — own sheet](Brush-Artist-Refs-09-Henry-Ward-white-loops-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 50 % → 59 % | 15.8 px | 0.17 | 1.18 | 975 |
| stroke 2 | 53 % → 55 % | 37.4 px | 0.18 | 1.03 | 1076 |
| stroke 3 | 60 % → 57 % | 35.0 px | 0.19 | 0.94 | 1019 |

## Brush Artist · Refs · #10 Henry Ward maroon loops — own sheet
own sheet 600 × 600 · Heavy acrylic · 30 px · 3.0 s

![Brush Artist · Refs · #10 Henry Ward maroon loops — own sheet](Brush-Artist-Refs-10-Henry-Ward-maroon-loops-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 16 % → 33 % | 28.6 px | 0.72 | 2.07 | 193 |
| stroke 2 | 29 % → 47 % | 46.0 px | 0.72 | 1.60 | 123 |
| stroke 3 | 40 % → 50 % | 54.7 px | 0.72 | 1.24 | 145 |
| stroke 4 | 45 % → 43 % | 64.1 px | 0.72 | 0.96 | 110 |
| stroke 5 | 41 % → 38 % | 70.6 px | 0.72 | 0.93 | 129 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #11 Henry Ward purple spun balls — own sheet
own sheet 600 × 600 · Heavy acrylic · 36 px · 3.1 s

![Brush Artist · Refs · #11 Henry Ward purple spun balls — own sheet](Brush-Artist-Refs-11-Henry-Ward-purple-spun-balls-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 35 % → 43 % | 17.2 px | 0.68 | 1.23 | 327 |
| stroke 2 | 45 % → 52 % | 21.9 px | 0.68 | 1.15 | 315 |
| stroke 3 | 45 % → 43 % | 21.8 px | 0.68 | 0.96 | 344 |

## Brush Artist · Refs · #12 Henry Ward black-olive cage — own sheet
own sheet 600 × 600 · Gouache · 28 px · 5.4 s

![Brush Artist · Refs · #12 Henry Ward black-olive cage — own sheet](Brush-Artist-Refs-12-Henry-Ward-black-olive-cage-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 18 % → 22 % | 24.3 px | 0.59 | 1.24 | 196 |
| stroke 2 | 16 % → 26 % | 27.7 px | 0.59 | 1.61 | 194 |
| stroke 3 | 34 % → 34 % | 40.4 px | 0.59 | 1.01 | 212 |
| stroke 4 | 34 % → 34 % | 42.8 px | 0.59 | 1.03 | 131 |
| stroke 5 | 34 % → 21 % | 43.1 px | 0.59 | 0.60 | 133 |
| stroke 6 | 52 % → 37 % | 67.3 px | 0.59 | 0.72 | 174 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #13 Henry Ward blue streaky form — own sheet
own sheet 600 × 600 · Gouache · 50 px · 14.5 s

![Brush Artist · Refs · #13 Henry Ward blue streaky form — own sheet](Brush-Artist-Refs-13-Henry-Ward-blue-streaky-form-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 34 % → 64 % | 49.1 px | 0.05 | 1.86 | 192 |
| stroke 2 | 42 % → 66 % | 67.5 px | 0.05 | 1.58 | 217 |
| stroke 3 | 60 % → 86 % | 85.2 px | 0.05 | 1.43 | 228 |
| stroke 4 | 60 % → 89 % | 97.8 px | 0.06 | 1.49 | 212 |
| stroke 5 | 61 % → 86 % | 86.7 px | 0.06 | 1.42 | 222 |
| stroke 6 | 56 % → 82 % | 86.1 px | 0.06 | 1.47 | 228 |
| stroke 7 | 62 % → 85 % | 92.3 px | 0.05 | 1.38 | 214 |
| stroke 8 | 62 % → 85 % | 96.3 px | 0.06 | 1.37 | 225 |
| stroke 9 | 62 % → 87 % | 94.7 px | 0.05 | 1.41 | 219 |
| stroke 10 | 63 % → 89 % | 102.4 px | 0.05 | 1.40 | 192 |
| stroke 11 | 58 % → 86 % | 87.3 px | 0.06 | 1.48 | 195 |
| stroke 12 | 58 % → 82 % | 91.0 px | 0.05 | 1.42 | 221 |
| stroke 13 | 61 % → 88 % | 89.4 px | 0.06 | 1.44 | 183 |
| stroke 14 | 54 % → 82 % | 83.9 px | 0.06 | 1.53 | 208 |
| stroke 15 | 57 % → 83 % | 82.3 px | 0.06 | 1.45 | 217 |
| stroke 16 | 56 % → 84 % | 90.5 px | 0.06 | 1.51 | 206 |
| stroke 17 | 61 % → 84 % | 93.7 px | 0.06 | 1.39 | 202 |
| stroke 18 | 61 % → 82 % | 95.3 px | 0.06 | 1.35 | 296 |
| stroke 19 | 68 % → 80 % | 84.6 px | 0.06 | 1.18 | 210 |
| stroke 20 | 78 % → 77 % | 93.1 px | 0.06 | 0.99 | 305 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #14 Henry Ward olive totem — own sheet
own sheet 600 × 600 · Heavy acrylic · 48 px · 6.6 s

![Brush Artist · Refs · #14 Henry Ward olive totem — own sheet](Brush-Artist-Refs-14-Henry-Ward-olive-totem-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 31 % → 50 % | 46.9 px | 0.38 | 1.58 | 131 |
| stroke 2 | 36 % → 62 % | 64.3 px | 0.38 | 1.71 | 120 |
| stroke 3 | 54 % → 76 % | 79.7 px | 0.38 | 1.42 | 130 |
| stroke 4 | 50 % → 73 % | 88.4 px | 0.38 | 1.46 | 142 |
| stroke 5 | 56 % → 78 % | 83.2 px | 0.38 | 1.39 | 117 |
| stroke 6 | 54 % → 81 % | 96.5 px | 0.38 | 1.50 | 120 |
| stroke 7 | 52 % → 75 % | 74.2 px | 0.38 | 1.45 | 125 |
| stroke 8 | 51 % → 77 % | 90.4 px | 0.38 | 1.53 | 180 |
| stroke 9 | 56 % → 81 % | 82.9 px | 0.38 | 1.44 | 137 |
| stroke 10 | 56 % → 78 % | 94.7 px | 0.38 | 1.40 | 136 |
| stroke 11 | 57 % → 79 % | 90.0 px | 0.38 | 1.38 | 135 |
| stroke 12 | 53 % → 80 % | 90.4 px | 0.38 | 1.53 | 121 |
| stroke 13 | 55 % → 83 % | 82.0 px | 0.38 | 1.51 | 110 |
| stroke 14 | 52 % → 76 % | 86.9 px | 0.38 | 1.48 | 133 |
| stroke 15 | 58 % → 82 % | 85.5 px | 0.38 | 1.41 | 117 |
| stroke 16 | 54 % → 80 % | 89.8 px | 0.38 | 1.47 | 137 |
| stroke 17 | 53 % → 78 % | 77.7 px | 0.38 | 1.45 | 149 |
| stroke 18 | 57 % → 84 % | 100.3 px | 0.38 | 1.47 | 119 |
| stroke 19 | 57 % → 80 % | 86.5 px | 0.38 | 1.41 | 122 |
| stroke 20 | 55 % → 76 % | 95.2 px | 0.38 | 1.40 | 128 |
| stroke 21 | 52 % → 67 % | 83.7 px | 0.37 | 1.30 | 120 |
| stroke 22 | 60 % → 59 % | 94.0 px | 0.37 | 0.98 | 128 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #15 Ultramarine brush script — own sheet
own sheet 600 × 600 · Ink · 10 px · 9.1 s

![Brush Artist · Refs · #15 Ultramarine brush script — own sheet](Brush-Artist-Refs-15-Ultramarine-brush-script-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 69 % → 72 % | 17.0 px | 0.75 | 1.05 | 62 |
| stroke 2 | 70 % → 72 % | 16.6 px | 0.73 | 1.04 | 75 |
| stroke 3 | 70 % → 74 % | 17.4 px | 0.74 | 1.05 | 72 |
| stroke 4 | 71 % → 72 % | 16.3 px | 0.71 | 1.01 | 112 |
| stroke 5 | 66 % → 69 % | 15.7 px | 0.71 | 1.04 | 95 |
| stroke 6 | 67 % → 71 % | 18.5 px | 0.75 | 1.05 | 52 |
| stroke 7 | 69 % → 71 % | 15.9 px | 0.72 | 1.04 | 87 |
| stroke 8 | 69 % → 71 % | 17.6 px | 0.74 | 1.02 | 65 |
| stroke 9 | 67 % → 70 % | 16.5 px | 0.73 | 1.05 | 86 |
| stroke 10 | 65 % → 69 % | 17.1 px | 0.74 | 1.05 | 68 |
| stroke 11 | 72 % → 75 % | 17.5 px | 0.74 | 1.04 | 76 |
| stroke 12 | 68 % → 69 % | 15.8 px | 0.72 | 1.01 | 119 |
| stroke 13 | 66 % → 69 % | 15.7 px | 0.72 | 1.04 | 105 |
| stroke 14 | 67 % → 71 % | 18.2 px | 0.75 | 1.05 | 59 |
| stroke 15 | 69 % → 73 % | 18.8 px | 0.76 | 1.05 | 59 |
| stroke 16 | 68 % → 72 % | 17.4 px | 0.75 | 1.04 | 74 |
| stroke 17 | 68 % → 69 % | 18.1 px | 0.75 | 1.02 | 55 |
| stroke 18 | 68 % → 71 % | 17.2 px | 0.75 | 1.05 | 72 |
| stroke 19 | 66 % → 71 % | 18.9 px | 0.76 | 1.07 | 47 |
| stroke 20 | 68 % → 72 % | 18.8 px | 0.76 | 1.06 | 48 |
| stroke 21 | 70 % → 73 % | 16.0 px | 0.71 | 1.03 | 107 |
| stroke 22 | 77 % → 79 % | 12.6 px | 0.75 | 1.02 | 74 |
| stroke 23 | 67 % → 71 % | 16.9 px | 0.74 | 1.05 | 57 |
| stroke 24 | 66 % → 69 % | 17.9 px | 0.76 | 1.05 | 64 |
| stroke 25 | 69 % → 72 % | 16.5 px | 0.73 | 1.04 | 87 |
| stroke 26 | 70 % → 71 % | 15.8 px | 0.70 | 1.01 | 108 |

## Brush Artist · Refs · #18 Blue oil-stick scribbles — own sheet
own sheet 600 × 600 · Pastel · 10 px · 2.8 s

![Brush Artist · Refs · #18 Blue oil-stick scribbles — own sheet](Brush-Artist-Refs-18-Blue-oil-stick-scribbles-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 18 % → 37 % | 3.8 px | 0.49 | 2.02 | 136 |
| stroke 2 | 16 % → 40 % | 3.6 px | 0.49 | 2.52 | 142 |
| stroke 3 | 18 % → 29 % | 5.8 px | 0.49 | 1.59 | 165 |
| stroke 4 | 17 % → 32 % | 7.8 px | 0.49 | 1.90 | 161 |
| stroke 5 | 32 % → 37 % | 7.8 px | 0.49 | 1.15 | 136 |
| stroke 6 | 30 % → 30 % | 9.2 px | 0.49 | 1.02 | 107 |
| stroke 7 | 28 % → 35 % | 7.5 px | 0.49 | 1.26 | 129 |
| stroke 8 | 33 % → 33 % | 16.3 px | 0.49 | 1.00 | 160 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #20 Orange-red crayon scribble — own sheet
own sheet 600 × 600 · Pastel · 14 px · 2.6 s

![Brush Artist · Refs · #20 Orange-red crayon scribble — own sheet](Brush-Artist-Refs-20-Orange-red-crayon-scribble-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 9 % → 20 % | 5.5 px | 0.59 | 2.30 | 194 |
| stroke 2 | 10 % → 25 % | 6.5 px | 0.59 | 2.49 | 135 |
| stroke 3 | 15 % → 25 % | 8.3 px | 0.59 | 1.61 | 152 |
| stroke 4 | 28 % → 35 % | 8.3 px | 0.59 | 1.25 | 160 |
| stroke 5 | 32 % → 32 % | 7.0 px | 0.59 | 1.00 | 155 |
| stroke 6 | 24 % → 24 % | 16.1 px | 0.59 | 1.00 | 132 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #21 Gritty black contours — own sheet
own sheet 600 × 600 · Gouache · 12 px · 4.0 s

![Brush Artist · Refs · #21 Gritty black contours — own sheet](Brush-Artist-Refs-21-Gritty-black-contours-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 12 % → 9 % | 10.6 px | 0.36 | 0.74 | 131 |
| stroke 2 | 10 % → 6 % | 14.1 px | 0.36 | 0.62 | 147 |
| stroke 3 | 18 % → 5 % | 12.5 px | 0.36 | 0.28 | 100 |
| stroke 4 | 19 % → 9 % | 18.4 px | 0.36 | 0.47 | 115 |
| stroke 5 | 19 % → 10 % | 17.9 px | 0.36 | 0.50 | 85 |

## Brush Artist · Refs · #22 Bold black brush poster — own sheet
own sheet 600 × 600 · Ink · 20 px · 4.7 s

![Brush Artist · Refs · #22 Bold black brush poster — own sheet](Brush-Artist-Refs-22-Bold-black-brush-poster-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 34 % → 37 % | 36.3 px | 0.94 | 1.10 | 91 |
| stroke 2 | 55 % → 66 % | 36.9 px | 0.95 | 1.21 | 22 |
| stroke 3 | 49 % → 49 % | 40.5 px | 0.94 | 1.00 | 44 |
| stroke 4 | 36 % → 43 % | 45.3 px | 0.94 | 1.20 | 49 |
| stroke 5 | 35 % → 35 % | 40.5 px | 0.94 | 1.00 | 88 |

## Brush Artist · Refs · #23 Dry white on orange + black line — own sheet
own sheet 600 × 600 · Gouache · 50 px · 9.4 s

![Brush Artist · Refs · #23 Dry white on orange + black line — own sheet](Brush-Artist-Refs-23-Dry-white-on-orange-black-line-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 26 % → 47 % | 44.0 px | 0.44 | 1.79 | 143 |
| stroke 2 | 31 % → 48 % | 53.3 px | 0.44 | 1.54 | 162 |
| stroke 3 | 50 % → 68 % | 81.7 px | 0.44 | 1.35 | 186 |
| stroke 4 | 48 % → 64 % | 87.6 px | 0.44 | 1.34 | 154 |
| stroke 5 | 50 % → 53 % | 76.7 px | 0.44 | 1.06 | 138 |
| stroke 6 | 49 % → 58 % | 93.3 px | 0.44 | 1.19 | 147 |
| stroke 7 | 39 % → 56 % | 66.4 px | 0.44 | 1.42 | 137 |
| stroke 8 | 41 % → 53 % | 74.2 px | 0.44 | 1.29 | 146 |
| stroke 9 | 51 % → 66 % | 83.2 px | 0.44 | 1.30 | 151 |
| stroke 10 | 54 % → 70 % | 96.3 px | 0.44 | 1.30 | 148 |
| stroke 11 | 49 % → 68 % | 80.7 px | 0.43 | 1.39 | 147 |
| stroke 12 | 49 % → 64 % | 88.4 px | 0.43 | 1.30 | 152 |
| stroke 13 | 52 % → 62 % | 84.2 px | 0.43 | 1.19 | 153 |
| stroke 14 | 48 % → 61 % | 89.7 px | 0.43 | 1.26 | 151 |
| stroke 15 | 49 % → 65 % | 78.9 px | 0.44 | 1.33 | 145 |
| stroke 16 | 46 % → 61 % | 84.9 px | 0.43 | 1.34 | 146 |
| stroke 17 | 46 % → 51 % | 77.0 px | 0.43 | 1.11 | 190 |
| stroke 18 | 55 % → 50 % | 102.5 px | 0.43 | 0.90 | 142 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #24 Picasso flat oil — own sheet
own sheet 600 × 600 · Oil · 34 px · 5.0 s

![Brush Artist · Refs · #24 Picasso flat oil — own sheet](Brush-Artist-Refs-24-Picasso-flat-oil-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 35 % → 60 % | 34.6 px | 0.24 | 1.73 | 118 |
| stroke 2 | 40 % → 66 % | 47.1 px | 0.23 | 1.65 | 128 |
| stroke 3 | 56 % → 84 % | 59.7 px | 0.23 | 1.50 | 145 |
| stroke 4 | 56 % → 82 % | 63.9 px | 0.23 | 1.47 | 125 |
| stroke 5 | 55 % → 86 % | 59.9 px | 0.23 | 1.56 | 129 |
| stroke 6 | 56 % → 85 % | 66.3 px | 0.23 | 1.52 | 123 |
| stroke 7 | 60 % → 75 % | 59.1 px | 0.23 | 1.23 | 122 |
| stroke 8 | 56 % → 72 % | 71.1 px | 0.23 | 1.28 | 131 |
| stroke 9 | 42 % → 67 % | 43.8 px | 0.23 | 1.61 | 121 |
| stroke 10 | 46 % → 69 % | 56.7 px | 0.23 | 1.49 | 119 |
| stroke 11 | 59 % → 73 % | 60.6 px | 0.23 | 1.24 | 113 |
| stroke 12 | 59 % → 78 % | 72.3 px | 0.23 | 1.31 | 125 |
| stroke 13 | 47 % → 72 % | 50.2 px | 0.23 | 1.55 | 122 |
| stroke 14 | 48 % → 75 % | 55.1 px | 0.23 | 1.54 | 126 |
| stroke 15 | 53 % → 82 % | 53.5 px | 0.23 | 1.56 | 120 |
| stroke 16 | 49 % → 78 % | 58.9 px | 0.23 | 1.59 | 130 |
| stroke 17 | 60 % → 71 % | 59.6 px | 0.23 | 1.18 | 124 |
| stroke 18 | 56 % → 56 % | 71.0 px | 0.23 | 1.00 | 114 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #25 Yellow heavy flat stroke — own sheet
own sheet 600 × 600 · Heavy acrylic · 110 px · 2.7 s

![Brush Artist · Refs · #25 Yellow heavy flat stroke — own sheet](Brush-Artist-Refs-25-Yellow-heavy-flat-stroke-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 35 % → 35 % | 104.2 px | 0.17 | 0.98 | 624 |

## Brush Artist · Refs · #27 Orange impasto swatch — own sheet
own sheet 600 × 600 · Heavy acrylic · 60 px · 3.0 s

![Brush Artist · Refs · #27 Orange impasto swatch — own sheet](Brush-Artist-Refs-27-Orange-impasto-swatch-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 23 % → 29 % | 61.8 px | 0.34 | 1.29 | 66 |
| stroke 2 | 19 % → 40 % | 62.5 px | 0.33 | 2.07 | 43 |
| stroke 3 | 26 % → 38 % | 94.9 px | 0.34 | 1.48 | 36 |
| stroke 4 | 22 % → 22 % | 62.5 px | 0.33 | 0.96 | 62 |
| stroke 5 | 32 % → 41 % | 62.2 px | 0.33 | 1.28 | 62 |
| stroke 6 | 39 % → 40 % | 112.2 px | 0.33 | 1.02 | 59 |
| stroke 7 | 19 % → 21 % | 63.8 px | 0.33 | 1.11 | 42 |
| stroke 8 | 42 % → 40 % | 143.3 px | 0.33 | 0.97 | 44 |
| stroke 9 | 49 % → 48 % | 97.7 px | 0.33 | 0.97 | 63 |
| stroke 10 | 28 % → 27 % | 87.2 px | 0.33 | 0.96 | 52 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #28 Miles Davis black lines — own sheet
own sheet 600 × 600 · Ink · 22 px · 5.5 s

![Brush Artist · Refs · #28 Miles Davis black lines — own sheet](Brush-Artist-Refs-28-Miles-Davis-black-lines-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 29 % → 36 % | 36.4 px | 0.88 | 1.26 | 163 |
| stroke 2 | 37 % → 57 % | 36.0 px | 0.88 | 1.52 | 126 |
| stroke 3 | 47 % → 48 % | 66.3 px | 0.88 | 1.02 | 88 |
| stroke 4 | 49 % → 58 % | 76.4 px | 0.88 | 1.16 | 155 |
| stroke 5 | 63 % → 64 % | 95.0 px | 0.88 | 1.00 | 116 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #29 Shrigley magenta asterisk — own sheet
own sheet 600 × 600 · Watercolor · 70 px · 5.7 s

![Brush Artist · Refs · #29 Shrigley magenta asterisk — own sheet](Brush-Artist-Refs-29-Shrigley-magenta-asterisk-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 25 % → 44 % | 46.6 px | 0.72 | 1.76 | 172 |
| stroke 2 | 17 % → 17 % | 86.5 px | 0.71 | 1.00 | 181 |
| stroke 3 | 37 % → 43 % | 69.5 px | 0.71 | 1.17 | 177 |
| stroke 4 | 32 % → 33 % | 162.9 px | 0.71 | 1.02 | 179 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #30 Red gouache face patch — own sheet
own sheet 600 × 600 · Gouache · 60 px · 10.4 s

![Brush Artist · Refs · #30 Red gouache face patch — own sheet](Brush-Artist-Refs-30-Red-gouache-face-patch-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 27 % → 51 % | 51.5 px | 0.53 | 1.89 | 155 |
| stroke 2 | 33 % → 57 % | 74.5 px | 0.53 | 1.74 | 150 |
| stroke 3 | 50 % → 77 % | 99.1 px | 0.53 | 1.54 | 146 |
| stroke 4 | 50 % → 77 % | 110.7 px | 0.53 | 1.54 | 152 |
| stroke 5 | 49 % → 78 % | 97.1 px | 0.53 | 1.61 | 169 |
| stroke 6 | 50 % → 80 % | 112.2 px | 0.53 | 1.59 | 149 |
| stroke 7 | 51 % → 78 % | 101.2 px | 0.53 | 1.53 | 146 |
| stroke 8 | 49 % → 76 % | 103.7 px | 0.53 | 1.55 | 170 |
| stroke 9 | 52 % → 80 % | 104.6 px | 0.53 | 1.53 | 161 |
| stroke 10 | 54 % → 76 % | 123.0 px | 0.53 | 1.39 | 156 |
| stroke 11 | 52 % → 74 % | 107.4 px | 0.53 | 1.43 | 147 |
| stroke 12 | 50 % → 74 % | 109.1 px | 0.53 | 1.48 | 155 |
| stroke 13 | 45 % → 72 % | 87.5 px | 0.53 | 1.61 | 157 |
| stroke 14 | 45 % → 63 % | 95.7 px | 0.53 | 1.42 | 176 |
| stroke 15 | 48 % → 58 % | 92.1 px | 0.53 | 1.21 | 173 |
| stroke 16 | 55 % → 54 % | 122.4 px | 0.53 | 0.99 | 154 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #31 Warhol blotted line — own sheet
own sheet 600 × 600 · Ink · 6 px · 4.4 s

![Brush Artist · Refs · #31 Warhol blotted line — own sheet](Brush-Artist-Refs-31-Warhol-blotted-line-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 24 % → 47 % | 15.7 px | 0.82 | 1.93 | 61 |
| stroke 2 | 19 % → 24 % | 15.8 px | 0.82 | 1.27 | 54 |
| stroke 3 | 27 % → 27 % | 24.7 px | 0.82 | 1.02 | 69 |
| stroke 4 | 31 % → 41 % | 27.9 px | 0.82 | 1.32 | 43 |
| stroke 5 | 38 % → 46 % | 34.7 px | 0.82 | 1.22 | 61 |
| stroke 6 | 35 % → 36 % | 25.2 px | 0.81 | 1.03 | 62 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #32 Thick orange swipes — own sheet
own sheet 600 × 600 · Heavy acrylic · 90 px · 3.5 s

![Brush Artist · Refs · #32 Thick orange swipes — own sheet](Brush-Artist-Refs-32-Thick-orange-swipes-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 28 % → 28 % | 86.0 px | 0.03 | 1.00 | 303 |
| stroke 2 | 29 % → 32 % | 89.3 px | 0.03 | 1.13 | 287 |
| stroke 3 | 32 % → 32 % | 102.9 px | 0.03 | 0.98 | 278 |

## Brush Artist · Refs · #33 Red wet-in-wet band — own sheet
own sheet 600 × 600 · Watercolor · 80 px · 7.0 s

![Brush Artist · Refs · #33 Red wet-in-wet band — own sheet](Brush-Artist-Refs-33-Red-wet-in-wet-band-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 45 % → 63 % | 92.3 px | 0.66 | 1.38 | 366 |
| stroke 2 | 50 % → 63 % | 180.2 px | 0.67 | 1.28 | 98 |
| stroke 3 | 61 % → 74 % | 234.0 px | 0.67 | 1.22 | 95 |
| stroke 4 | 62 % → 71 % | 228.8 px | 0.67 | 1.15 | 96 |
| stroke 5 | 57 % → 70 % | 201.2 px | 0.67 | 1.22 | 108 |
| stroke 6 | 61 % → 61 % | 212.9 px | 0.67 | 1.00 | 111 |

## Brush Artist · Refs · #34 Magenta oil patches — own sheet
own sheet 600 × 600 · Oil · 60 px · 4.2 s

![Brush Artist · Refs · #34 Magenta oil patches — own sheet](Brush-Artist-Refs-34-Magenta-oil-patches-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 24 % → 44 % | 61.9 px | 0.13 | 1.86 | 87 |
| stroke 2 | 22 % → 37 % | 62.8 px | 0.13 | 1.68 | 70 |
| stroke 3 | 21 % → 52 % | 62.3 px | 0.13 | 2.42 | 70 |
| stroke 4 | 31 % → 31 % | 97.0 px | 0.13 | 1.00 | 54 |
| stroke 5 | 28 % → 40 % | 61.7 px | 0.13 | 1.46 | 86 |
| stroke 6 | 27 % → 45 % | 80.2 px | 0.13 | 1.65 | 61 |
| stroke 7 | 29 % → 41 % | 82.2 px | 0.13 | 1.42 | 70 |
| stroke 8 | 52 % → 56 % | 134.7 px | 0.13 | 1.07 | 80 |
| stroke 9 | 34 % → 39 % | 87.4 px | 0.13 | 1.13 | 84 |
| stroke 10 | 48 % → 48 % | 152.6 px | 0.13 | 1.00 | 56 |
| stroke 11 | 61 % → 61 % | 185.1 px | 0.13 | 1.00 | 53 |
| stroke 12 | 35 % → 35 % | 104.1 px | 0.13 | 1.00 | 63 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #35 Red band with runs — own sheet
own sheet 600 × 600 · Watercolor · 70 px · 4.2 s

![Brush Artist · Refs · #35 Red band with runs — own sheet](Brush-Artist-Refs-35-Red-band-with-runs-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 41 % → 39 % | 82.9 px | 0.59 | 0.95 | 257 |

## Brush Artist · Refs · #36 Magenta letters flat brush — own sheet
own sheet 600 × 600 · Gouache · 36 px · 9.9 s

![Brush Artist · Refs · #36 Magenta letters flat brush — own sheet](Brush-Artist-Refs-36-Magenta-letters-flat-brush-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 46 % → 46 % | 59.1 px | 0.50 | 1.00 | 28 |
| stroke 2 | 38 % → 48 % | 39.7 px | 0.50 | 1.25 | 27 |
| stroke 3 | 56 % → 63 % | 72.2 px | 0.50 | 1.12 | 31 |
| stroke 4 | 45 % → 53 % | 44.9 px | 0.50 | 1.19 | 117 |
| stroke 5 | 41 % → 52 % | 61.1 px | 0.50 | 1.29 | 73 |
| stroke 6 | 78 % → 76 % | 153.6 px | 0.50 | 0.97 | 17 |
| stroke 7 | 43 % → 50 % | 42.1 px | 0.50 | 1.15 | 106 |
| stroke 8 | 39 % → 59 % | 63.5 px | 0.50 | 1.52 | 62 |
| stroke 9 | 54 % → 53 % | 82.8 px | 0.50 | 0.98 | 25 |
| stroke 10 | 42 % → 61 % | 63.1 px | 0.50 | 1.44 | 74 |
| stroke 11 | 78 % → 77 % | 153.6 px | 0.50 | 0.98 | 15 |
| stroke 12 | 58 % → 68 % | 57.2 px | 0.50 | 1.17 | 116 |
| stroke 13 | 43 % → 50 % | 58.9 px | 0.50 | 1.18 | 32 |
| stroke 14 | 52 % → 73 % | 74.9 px | 0.50 | 1.40 | 29 |
| stroke 15 | 44 % → 52 % | 66.5 px | 0.50 | 1.18 | 70 |
| stroke 16 | 78 % → 76 % | 153.3 px | 0.50 | 0.98 | 12 |
| stroke 17 | 53 % → 61 % | 51.3 px | 0.50 | 1.15 | 102 |
| stroke 18 | 40 % → 47 % | 54.9 px | 0.50 | 1.17 | 26 |
| stroke 19 | 65 % → 63 % | 81.6 px | 0.50 | 0.97 | 33 |
| stroke 20 | 56 % → 54 % | 70.5 px | 0.50 | 0.97 | 30 |
| stroke 21 | 47 % → 46 % | 53.9 px | 0.50 | 0.96 | 82 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #37 Oil still life dabs — own sheet
own sheet 600 × 600 · Oil · 40 px · 3.5 s

![Brush Artist · Refs · #37 Oil still life dabs — own sheet](Brush-Artist-Refs-37-Oil-still-life-dabs-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 20 % → 20 % | 44.0 px | 0.39 | 1.00 | 32 |
| stroke 2 | 18 % → 48 % | 44.4 px | 0.39 | 2.65 | 20 |
| stroke 3 | 23 % → 48 % | 59.8 px | 0.38 | 2.12 | 20 |
| stroke 4 | 22 % → 22 % | 42.7 px | 0.39 | 1.00 | 33 |
| stroke 5 | 17 % → 18 % | 43.2 px | 0.39 | 1.04 | 20 |
| stroke 6 | 37 % → 45 % | 83.3 px | 0.39 | 1.24 | 30 |
| stroke 7 | 16 % → 27 % | 54.8 px | 0.39 | 1.71 | 11 |
| stroke 8 | 14 % → 29 % | 47.9 px | 0.39 | 2.08 | 16 |
| stroke 9 | 23 % → 23 % | 43.9 px | 0.39 | 1.00 | 34 |
| stroke 10 | 31 % → 37 % | 58.3 px | 0.39 | 1.18 | 32 |
| stroke 11 | 39 % → 39 % | 109.7 px | 0.39 | 1.00 | 18 |
| stroke 12 | 31 % → 31 % | 109.5 px | 0.40 | 1.00 | 10 |
| stroke 13 | 17 % → 17 % | 59.0 px | 0.39 | 1.00 | 13 |
| stroke 14 | 35 % → 35 % | 91.9 px | 0.39 | 1.00 | 17 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #38 Sanguine drawing — own sheet
own sheet 600 × 600 · Pastel · 6 px · 2.2 s

![Brush Artist · Refs · #38 Sanguine drawing — own sheet](Brush-Artist-Refs-38-Sanguine-drawing-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 3 % → 14 % | 2.9 px | 0.57 | 4.35 | 8 |
| stroke 2 | 3 % → 7 % | 2.9 px | 0.57 | 2.23 | 7 |
| stroke 3 | 3 % → 9 % | 2.9 px | 0.57 | 2.76 | 4 |
| stroke 4 | 3 % → 19 % | 2.7 px | 0.57 | 6.27 | 9 |
| stroke 5 | 3 % → 8 % | 2.7 px | 0.57 | 2.71 | 3 |
| stroke 6 | 3 % → 20 % | 3.0 px | 0.57 | 6.20 | 6 |
| stroke 7 | 5 % → 15 % | 4.7 px | 0.57 | 2.84 | 3 |
| stroke 8 | 4 % → 15 % | 3.9 px | 0.57 | 3.43 | 7 |
| stroke 9 | 3 % → 7 % | 2.9 px | 0.57 | 2.30 | 3 |
| stroke 10 | 4 % → 17 % | 4.0 px | 0.57 | 3.83 | 6 |
| stroke 11 | 3 % → 5 % | 2.9 px | 0.57 | 1.49 | 3 |
| stroke 12 | 5 % → 16 % | 4.5 px | 0.57 | 3.20 | 7 |
| stroke 13 | 8 % → 18 % | 7.8 px | 0.57 | 2.10 | 3 |
| stroke 14 | 5 % → 15 % | 4.5 px | 0.57 | 2.96 | 5 |
| stroke 15 | 10 % → 18 % | 9.5 px | 0.57 | 1.71 | 3 |
| stroke 16 | 6 % → 16 % | 5.4 px | 0.57 | 2.74 | 5 |
| stroke 17 | 4 % → 9 % | 4.0 px | 0.57 | 2.07 | 5 |
| stroke 18 | 3 % → 5 % | 2.9 px | 0.57 | 1.68 | 7 |
| stroke 19 | 7 % → 17 % | 6.0 px | 0.57 | 2.63 | 6 |
| stroke 20 | 8 % → 15 % | 7.8 px | 0.57 | 1.72 | 4 |
| stroke 21 | 4 % → 4 % | 4.0 px | 0.57 | 1.00 | 7 |
| stroke 22 | 9 % → 14 % | 7.8 px | 0.58 | 1.66 | 3 |
| stroke 23 | 8 % → 12 % | 7.0 px | 0.57 | 1.52 | 5 |
| stroke 24 | 4 % → 7 % | 3.9 px | 0.57 | 1.55 | 3 |
| stroke 25 | 8 % → 15 % | 7.3 px | 0.57 | 1.86 | 7 |
| stroke 26 | 6 % → 8 % | 5.7 px | 0.57 | 1.26 | 4 |
| stroke 27 | 4 % → 4 % | 3.8 px | 0.57 | 1.05 | 7 |
| stroke 28 | 8 % → 12 % | 7.0 px | 0.57 | 1.56 | 7 |
| stroke 29 | 8 % → 17 % | 6.9 px | 0.57 | 2.22 | 7 |
| stroke 30 | 14 % → 18 % | 13.1 px | 0.57 | 1.25 | 8 |
| stroke 31 | 6 % → 7 % | 5.2 px | 0.57 | 1.23 | 3 |
| stroke 32 | 12 % → 13 % | 10.5 px | 0.57 | 1.15 | 3 |
| stroke 33 | 7 % → 8 % | 6.6 px | 0.57 | 1.06 | 4 |
| stroke 34 | 11 % → 14 % | 10.2 px | 0.57 | 1.28 | 5 |
| stroke 35 | 9 % → 15 % | 8.6 px | 0.57 | 1.56 | 4 |
| stroke 36 | 11 % → 13 % | 9.8 px | 0.57 | 1.27 | 8 |
| stroke 37 | 11 % → 17 % | 9.8 px | 0.57 | 1.64 | 4 |
| stroke 38 | 14 % → 21 % | 12.4 px | 0.57 | 1.51 | 6 |
| stroke 39 | 15 % → 18 % | 13.6 px | 0.57 | 1.22 | 3 |
| stroke 40 | 6 % → 7 % | 5.3 px | 0.57 | 1.16 | 8 |
| stroke 41 | 17 % → 17 % | 15.3 px | 0.57 | 1.00 | 4 |
| stroke 42 | 14 % → 16 % | 12.6 px | 0.57 | 1.16 | 4 |
| stroke 43 | 11 % → 13 % | 10.0 px | 0.57 | 1.18 | 5 |
| stroke 44 | 13 % → 16 % | 11.6 px | 0.57 | 1.23 | 5 |
| stroke 45 | 3 % → 3 % | 2.6 px | 0.57 | 1.00 | 7 |
| stroke 46 | 17 % → 17 % | 15.6 px | 0.57 | 1.00 | 3 |
| stroke 47 | 14 % → 14 % | 13.1 px | 0.57 | 1.00 | 6 |
| stroke 48 | 13 % → 14 % | 12.4 px | 0.58 | 1.04 | 5 |
| stroke 49 | 20 % → 20 % | 18.3 px | 0.57 | 1.00 | 3 |
| stroke 50 | 10 % → 10 % | 9.5 px | 0.57 | 1.00 | 4 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #39 Very thick impasto — own sheet
own sheet 600 × 600 · Heavy acrylic · 60 px · 4.1 s

![Brush Artist · Refs · #39 Very thick impasto — own sheet](Brush-Artist-Refs-39-Very-thick-impasto-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 38 % → 37 % | 59.5 px | 0.43 | 0.97 | 253 |
| stroke 2 | 37 % → 40 % | 59.6 px | 0.43 | 1.08 | 267 |
| stroke 3 | 40 % → 39 % | 72.0 px | 0.44 | 0.97 | 238 |
| stroke 4 | 39 % → 38 % | 59.6 px | 0.43 | 0.97 | 288 |
| stroke 5 | 35 % → 34 % | 59.7 px | 0.43 | 0.97 | 278 |

## Brush Artist · Refs · #40 Watercolour blooms — own sheet
own sheet 600 × 600 · Watercolor · 90 px · 5.4 s

![Brush Artist · Refs · #40 Watercolour blooms — own sheet](Brush-Artist-Refs-40-Watercolour-blooms-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 39 % → 39 % | 94.2 px | 0.13 | 1.00 | 747 |

## Brush Artist · Refs · #41 Coloured pencil hatching — own sheet
own sheet 600 × 600 · Pastel · 4 px · 2.5 s

![Brush Artist · Refs · #41 Coloured pencil hatching — own sheet](Brush-Artist-Refs-41-Coloured-pencil-hatching-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 3 % → 14 % | 2.2 px | 0.35 | 4.12 | 5 |
| stroke 2 | 4 % → 7 % | 2.3 px | 0.35 | 1.98 | 7 |
| stroke 3 | 3 % → 11 % | 1.9 px | 0.35 | 3.77 | 5 |
| stroke 4 | 3 % → 20 % | 2.1 px | 0.35 | 5.90 | 4 |
| stroke 5 | 4 % → 7 % | 2.8 px | 0.35 | 1.51 | 2 |
| stroke 6 | 4 % → 13 % | 2.3 px | 0.35 | 3.60 | 2 |
| stroke 7 | 4 % → 15 % | 2.5 px | 0.35 | 3.75 | 2 |
| stroke 8 | 3 % → 12 % | 2.1 px | 0.35 | 3.44 | 4 |
| stroke 9 | 6 % → 12 % | 3.4 px | 0.35 | 2.11 | 2 |
| stroke 10 | 5 % → 16 % | 3.2 px | 0.35 | 3.19 | 4 |
| stroke 11 | 4 % → 13 % | 2.7 px | 0.35 | 3.02 | 2 |
| stroke 12 | 3 % → 3 % | 2.1 px | 0.35 | 1.00 | 5 |
| stroke 13 | 7 % → 16 % | 4.7 px | 0.35 | 2.23 | 2 |
| stroke 14 | 4 % → 14 % | 2.3 px | 0.35 | 3.93 | 6 |
| stroke 15 | 7 % → 13 % | 4.3 px | 0.35 | 1.90 | 2 |
| stroke 16 | 7 % → 11 % | 4.7 px | 0.35 | 1.48 | 3 |
| stroke 17 | 3 % → 3 % | 2.1 px | 0.35 | 1.00 | 3 |
| stroke 18 | 5 % → 8 % | 3.2 px | 0.35 | 1.69 | 5 |
| stroke 19 | 6 % → 14 % | 3.6 px | 0.35 | 2.41 | 6 |
| stroke 20 | 6 % → 16 % | 3.5 px | 0.35 | 2.81 | 2 |
| stroke 21 | 5 % → 15 % | 3.0 px | 0.35 | 3.16 | 5 |
| stroke 22 | 10 % → 17 % | 6.4 px | 0.35 | 1.73 | 4 |
| stroke 23 | 9 % → 13 % | 5.9 px | 0.35 | 1.42 | 3 |
| stroke 24 | 7 % → 14 % | 4.1 px | 0.35 | 2.18 | 2 |
| stroke 25 | 5 % → 10 % | 3.3 px | 0.35 | 2.03 | 5 |
| stroke 26 | 4 % → 6 % | 2.5 px | 0.35 | 1.47 | 2 |
| stroke 27 | 3 % → 7 % | 2.2 px | 0.35 | 2.01 | 2 |
| stroke 28 | 6 % → 9 % | 3.9 px | 0.35 | 1.53 | 5 |
| stroke 29 | 4 % → 15 % | 2.4 px | 0.35 | 3.85 | 13 |
| stroke 30 | 6 % → 9 % | 3.9 px | 0.35 | 1.47 | 7 |
| stroke 31 | 7 % → 15 % | 4.6 px | 0.35 | 2.08 | 4 |
| stroke 32 | 4 % → 7 % | 2.4 px | 0.35 | 1.80 | 5 |
| stroke 33 | 7 % → 11 % | 4.3 px | 0.35 | 1.66 | 6 |
| stroke 34 | 4 % → 6 % | 2.5 px | 0.35 | 1.53 | 2 |
| stroke 35 | 7 % → 14 % | 4.4 px | 0.35 | 2.05 | 4 |
| stroke 36 | 6 % → 6 % | 3.5 px | 0.35 | 1.00 | 3 |
| stroke 37 | 7 % → 15 % | 4.6 px | 0.35 | 2.02 | 3 |
| stroke 38 | 8 % → 13 % | 5.3 px | 0.35 | 1.59 | 4 |
| stroke 39 | 7 % → 12 % | 4.7 px | 0.35 | 1.59 | 3 |
| stroke 40 | 8 % → 19 % | 5.2 px | 0.35 | 2.28 | 5 |
| stroke 41 | 9 % → 13 % | 5.9 px | 0.35 | 1.38 | 4 |
| stroke 42 | 10 % → 18 % | 6.5 px | 0.35 | 1.77 | 6 |
| stroke 43 | 5 % → 8 % | 3.2 px | 0.35 | 1.64 | 2 |
| stroke 44 | 11 % → 15 % | 6.8 px | 0.35 | 1.36 | 5 |
| stroke 45 | 13 % → 18 % | 8.4 px | 0.35 | 1.36 | 5 |
| stroke 46 | 5 % → 7 % | 3.4 px | 0.34 | 1.26 | 4 |
| stroke 47 | 11 % → 13 % | 6.8 px | 0.35 | 1.20 | 5 |
| stroke 48 | 13 % → 17 % | 8.1 px | 0.35 | 1.34 | 3 |
| stroke 49 | 5 % → 9 % | 3.4 px | 0.35 | 1.77 | 2 |
| stroke 50 | 7 % → 7 % | 4.6 px | 0.34 | 1.00 | 2 |
| stroke 51 | 10 % → 17 % | 6.1 px | 0.35 | 1.73 | 2 |
| stroke 52 | 13 % → 16 % | 8.3 px | 0.35 | 1.20 | 5 |
| stroke 53 | 11 % → 15 % | 6.8 px | 0.35 | 1.37 | 5 |
| stroke 54 | 10 % → 15 % | 6.5 px | 0.35 | 1.49 | 4 |
| stroke 55 | 11 % → 14 % | 7.0 px | 0.35 | 1.30 | 5 |
| stroke 56 | 11 % → 13 % | 7.3 px | 0.35 | 1.10 | 2 |
| stroke 57 | 10 % → 14 % | 6.5 px | 0.35 | 1.37 | 5 |
| stroke 58 | 11 % → 13 % | 7.1 px | 0.35 | 1.14 | 3 |
| stroke 59 | 12 % → 14 % | 7.6 px | 0.35 | 1.15 | 2 |
| stroke 60 | 16 % → 20 % | 10.0 px | 0.35 | 1.29 | 5 |
| stroke 61 | 20 % → 21 % | 12.9 px | 0.35 | 1.02 | 8 |
| stroke 62 | 10 % → 10 % | 6.4 px | 0.35 | 1.00 | 6 |
| stroke 63 | 12 % → 13 % | 7.7 px | 0.35 | 1.06 | 6 |
| stroke 64 | 16 % → 16 % | 9.9 px | 0.35 | 1.02 | 6 |
| stroke 65 | 16 % → 16 % | 10.4 px | 0.35 | 1.00 | 2 |
| stroke 66 | 14 % → 14 % | 8.9 px | 0.35 | 1.00 | 5 |
| stroke 67 | 13 % → 13 % | 7.9 px | 0.35 | 1.04 | 3 |
| stroke 68 | 5 % → 9 % | 3.1 px | 0.35 | 1.90 | 5 |
| stroke 69 | 6 % → 6 % | 3.9 px | 0.35 | 1.00 | 5 |
| stroke 70 | 11 % → 13 % | 6.7 px | 0.35 | 1.27 | 4 |
| stroke 71 | 10 % → 12 % | 6.4 px | 0.35 | 1.15 | 4 |
| stroke 72 | 6 % → 7 % | 3.6 px | 0.35 | 1.17 | 4 |
| stroke 73 | 13 % → 13 % | 8.4 px | 0.35 | 1.00 | 2 |
| stroke 74 | 15 % → 15 % | 9.5 px | 0.35 | 1.00 | 4 |
| stroke 75 | 16 % → 16 % | 10.2 px | 0.35 | 1.00 | 3 |
| stroke 76 | 14 % → 14 % | 9.1 px | 0.35 | 1.00 | 5 |
| stroke 77 | 7 % → 10 % | 4.3 px | 0.35 | 1.38 | 5 |
| stroke 78 | 10 % → 10 % | 6.2 px | 0.35 | 1.00 | 3 |
| stroke 79 | 8 % → 8 % | 4.9 px | 0.35 | 1.00 | 3 |
| stroke 80 | 12 % → 12 % | 7.3 px | 0.35 | 1.00 | 3 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #42 Oil pastel shaggy — own sheet
own sheet 600 × 600 · Pastel · 18 px · 2.5 s

![Brush Artist · Refs · #42 Oil pastel shaggy — own sheet](Brush-Artist-Refs-42-Oil-pastel-shaggy-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 9 % → 20 % | 8.0 px | 0.28 | 2.21 | 14 |
| stroke 2 | 10 % → 26 % | 8.6 px | 0.28 | 2.58 | 6 |
| stroke 3 | 10 % → 33 % | 8.9 px | 0.29 | 3.29 | 8 |
| stroke 4 | 10 % → 21 % | 8.8 px | 0.28 | 2.08 | 11 |
| stroke 5 | 11 % → 21 % | 9.9 px | 0.28 | 1.84 | 12 |
| stroke 6 | 10 % → 31 % | 9.1 px | 0.29 | 3.00 | 11 |
| stroke 7 | 14 % → 40 % | 12.6 px | 0.28 | 2.79 | 6 |
| stroke 8 | 11 % → 44 % | 9.5 px | 0.28 | 3.98 | 6 |
| stroke 9 | 13 % → 22 % | 11.5 px | 0.28 | 1.69 | 9 |
| stroke 10 | 11 % → 19 % | 9.5 px | 0.28 | 1.77 | 7 |
| stroke 11 | 10 % → 28 % | 9.0 px | 0.28 | 2.72 | 15 |
| stroke 12 | 14 % → 19 % | 12.3 px | 0.28 | 1.36 | 15 |
| stroke 13 | 19 % → 30 % | 16.7 px | 0.28 | 1.60 | 8 |
| stroke 14 | 9 % → 20 % | 7.9 px | 0.28 | 2.25 | 12 |
| stroke 15 | 10 % → 36 % | 9.0 px | 0.29 | 3.51 | 9 |
| stroke 16 | 16 % → 34 % | 14.4 px | 0.29 | 2.06 | 6 |
| stroke 17 | 21 % → 39 % | 18.6 px | 0.28 | 1.82 | 8 |
| stroke 18 | 25 % → 35 % | 21.6 px | 0.29 | 1.42 | 10 |
| stroke 19 | 22 % → 40 % | 19.1 px | 0.28 | 1.79 | 8 |
| stroke 20 | 23 % → 42 % | 19.9 px | 0.28 | 1.81 | 7 |
| stroke 21 | 14 % → 20 % | 12.7 px | 0.28 | 1.41 | 12 |
| stroke 22 | 14 % → 16 % | 12.0 px | 0.28 | 1.14 | 8 |
| stroke 23 | 20 % → 27 % | 17.3 px | 0.29 | 1.34 | 8 |
| stroke 24 | 30 % → 35 % | 26.0 px | 0.30 | 1.20 | 6 |
| stroke 25 | 20 % → 33 % | 17.4 px | 0.28 | 1.67 | 7 |
| stroke 26 | 11 % → 22 % | 9.2 px | 0.28 | 2.04 | 6 |
| stroke 27 | 31 % → 36 % | 27.6 px | 0.29 | 1.15 | 6 |
| stroke 28 | 19 % → 30 % | 16.5 px | 0.28 | 1.60 | 6 |
| stroke 29 | 11 % → 29 % | 9.4 px | 0.29 | 2.75 | 6 |
| stroke 30 | 14 % → 38 % | 11.9 px | 0.29 | 2.79 | 11 |
| stroke 31 | 16 % → 16 % | 13.9 px | 0.28 | 1.00 | 10 |
| stroke 32 | 20 % → 33 % | 17.2 px | 0.29 | 1.70 | 9 |
| stroke 33 | 20 % → 21 % | 17.6 px | 0.29 | 1.03 | 6 |
| stroke 34 | 30 % → 36 % | 26.0 px | 0.28 | 1.20 | 8 |
| stroke 35 | 29 % → 37 % | 25.2 px | 0.28 | 1.27 | 13 |
| stroke 36 | 25 % → 27 % | 22.0 px | 0.28 | 1.05 | 11 |
| stroke 37 | 21 % → 21 % | 17.9 px | 0.28 | 1.00 | 9 |
| stroke 38 | 29 % → 34 % | 24.6 px | 0.28 | 1.20 | 6 |
| stroke 39 | 15 % → 25 % | 13.2 px | 0.28 | 1.64 | 8 |
| stroke 40 | 34 % → 41 % | 29.5 px | 0.28 | 1.21 | 6 |
| stroke 41 | 32 % → 34 % | 28.3 px | 0.28 | 1.04 | 9 |
| stroke 42 | 21 % → 30 % | 18.8 px | 0.28 | 1.39 | 6 |
| stroke 43 | 14 % → 14 % | 12.4 px | 0.28 | 1.00 | 7 |
| stroke 44 | 29 % → 39 % | 25.3 px | 0.28 | 1.35 | 7 |
| stroke 45 | 25 % → 25 % | 21.7 px | 0.28 | 1.00 | 10 |
| stroke 46 | 40 % → 45 % | 34.6 px | 0.29 | 1.12 | 10 |
| stroke 47 | 38 % → 45 % | 33.1 px | 0.28 | 1.17 | 12 |
| stroke 48 | 27 % → 30 % | 23.5 px | 0.29 | 1.12 | 7 |
| stroke 49 | 32 % → 34 % | 27.9 px | 0.29 | 1.06 | 8 |
| stroke 50 | 39 % → 42 % | 34.1 px | 0.28 | 1.08 | 7 |
| stroke 51 | 20 % → 20 % | 17.4 px | 0.29 | 1.00 | 7 |
| stroke 52 | 37 % → 37 % | 32.1 px | 0.29 | 1.00 | 6 |
| stroke 53 | 23 % → 23 % | 19.8 px | 0.28 | 1.02 | 8 |
| stroke 54 | 28 % → 31 % | 24.4 px | 0.29 | 1.10 | 6 |
| stroke 55 | 17 % → 17 % | 14.6 px | 0.28 | 1.00 | 6 |
| stroke 56 | 21 % → 21 % | 18.2 px | 0.28 | 1.00 | 8 |
| stroke 57 | 36 % → 36 % | 31.3 px | 0.29 | 1.00 | 10 |
| stroke 58 | 29 % → 29 % | 25.3 px | 0.28 | 1.00 | 6 |
| stroke 59 | 50 % → 50 % | 43.8 px | 0.28 | 1.00 | 10 |
| stroke 60 | 19 % → 19 % | 16.5 px | 0.28 | 1.00 | 9 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #43 Dragged black ink blocks — own sheet
own sheet 600 × 600 · Gouache · 70 px · 7.5 s

![Brush Artist · Refs · #43 Dragged black ink blocks — own sheet](Brush-Artist-Refs-43-Dragged-black-ink-blocks-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 46 % → 28 % | 66.4 px | 0.42 | 0.62 | 389 |
| stroke 2 | 35 % → 22 % | 66.2 px | 0.42 | 0.62 | 409 |
| stroke 3 | 36 % → 25 % | 67.5 px | 0.42 | 0.69 | 404 |
| stroke 4 | 39 % → 24 % | 71.3 px | 0.42 | 0.60 | 414 |
| stroke 5 | 43 % → 29 % | 66.4 px | 0.42 | 0.66 | 417 |

## Brush Artist · Refs · #44 Blue looping ribbon — own sheet
own sheet 600 × 600 · Oil · 80 px · 5.4 s

![Brush Artist · Refs · #44 Blue looping ribbon — own sheet](Brush-Artist-Refs-44-Blue-looping-ribbon-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 48 % → 48 % | 42.2 px | 0.78 | 1.00 | 2398 |

## Brush Artist · Refs · #45 Soft pastel pepper — own sheet
own sheet 600 × 600 · Pastel · 40 px · 3.0 s

![Brush Artist · Refs · #45 Soft pastel pepper — own sheet](Brush-Artist-Refs-45-Soft-pastel-pepper-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 15 % → 33 % | 11.3 px | 0.49 | 2.20 | 310 |
| stroke 2 | 25 % → 37 % | 20.6 px | 0.49 | 1.47 | 269 |
| stroke 3 | 34 % → 42 % | 13.8 px | 0.49 | 1.25 | 257 |
| stroke 4 | 32 % → 36 % | 27.8 px | 0.49 | 1.13 | 267 |
| stroke 5 | 37 % → 37 % | 13.9 px | 0.49 | 1.00 | 191 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #46 Red-brown ink lips — own sheet
own sheet 600 × 600 · Watercolor · 70 px · 4.7 s

![Brush Artist · Refs · #46 Red-brown ink lips — own sheet](Brush-Artist-Refs-46-Red-brown-ink-lips-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 30 % → 43 % | 78.1 px | 0.72 | 1.42 | 196 |
| stroke 2 | 45 % → 45 % | 119.4 px | 0.72 | 1.00 | 159 |

## Brush Artist · Refs · #47 Pink knife slabs — own sheet
own sheet 600 × 600 · Heavy acrylic · 90 px · 4.1 s

![Brush Artist · Refs · #47 Pink knife slabs — own sheet](Brush-Artist-Refs-47-Pink-knife-slabs-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 28 % → 34 % | 83.2 px | 0.11 | 1.18 | 266 |
| stroke 2 | 36 % → 41 % | 106.4 px | 0.11 | 1.13 | 256 |
| stroke 3 | 36 % → 41 % | 106.3 px | 0.11 | 1.14 | 284 |
| stroke 4 | 37 % → 36 % | 106.4 px | 0.11 | 0.97 | 275 |

## Brush Artist · Refs · #48 Black bands with drips — own sheet
own sheet 600 × 600 · Gouache · 70 px · 7.6 s

![Brush Artist · Refs · #48 Black bands with drips — own sheet](Brush-Artist-Refs-48-Black-bands-with-drips-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 33 % → 30 % | 59.2 px | 0.39 | 0.91 | 450 |
| stroke 2 | 35 % → 32 % | 58.2 px | 0.39 | 0.92 | 443 |
| stroke 3 | 33 % → 31 % | 58.3 px | 0.39 | 0.94 | 446 |
| stroke 4 | 33 % → 32 % | 58.2 px | 0.39 | 0.95 | 447 |

## Brush Artist · Refs · #49 Magenta letters round brush — own sheet
own sheet 600 × 600 · Ink · 30 px · 7.2 s

![Brush Artist · Refs · #49 Magenta letters round brush — own sheet](Brush-Artist-Refs-49-Magenta-letters-round-brush-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 61 % → 65 % | 64.3 px | 0.52 | 1.06 | 29 |
| stroke 2 | 59 % → 63 % | 52.0 px | 0.53 | 1.07 | 39 |
| stroke 3 | 71 % → 80 % | 74.2 px | 0.53 | 1.13 | 28 |
| stroke 4 | 54 % → 64 % | 48.0 px | 0.52 | 1.18 | 103 |
| stroke 5 | 48 % → 65 % | 63.0 px | 0.52 | 1.35 | 66 |
| stroke 6 | 93 % → 94 % | 141.0 px | 0.53 | 1.01 | 15 |
| stroke 7 | 61 % → 70 % | 51.9 px | 0.52 | 1.14 | 113 |
| stroke 8 | 44 % → 72 % | 63.4 px | 0.53 | 1.61 | 63 |
| stroke 9 | 71 % → 71 % | 86.0 px | 0.53 | 1.00 | 26 |
| stroke 10 | 51 % → 72 % | 66.5 px | 0.52 | 1.42 | 66 |
| stroke 11 | 93 % → 94 % | 140.9 px | 0.53 | 1.01 | 17 |
| stroke 12 | 71 % → 83 % | 60.6 px | 0.52 | 1.18 | 114 |
| stroke 13 | 61 % → 65 % | 67.4 px | 0.53 | 1.05 | 33 |
| stroke 14 | 69 % → 92 % | 78.6 px | 0.53 | 1.33 | 33 |
| stroke 15 | 52 % → 63 % | 68.8 px | 0.52 | 1.20 | 65 |
| stroke 16 | 93 % → 93 % | 140.9 px | 0.53 | 1.00 | 20 |
| stroke 17 | 68 % → 76 % | 58.1 px | 0.52 | 1.12 | 103 |
| stroke 18 | 59 % → 62 % | 64.6 px | 0.52 | 1.05 | 29 |
| stroke 19 | 81 % → 80 % | 82.3 px | 0.53 | 0.99 | 29 |
| stroke 20 | 71 % → 70 % | 72.0 px | 0.52 | 1.00 | 26 |
| stroke 21 | 59 % → 59 % | 61.0 px | 0.52 | 1.00 | 80 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #50 Thick swipes on photo — own sheet
own sheet 600 × 600 · Heavy acrylic · 40 px · 2.6 s

![Brush Artist · Refs · #50 Thick swipes on photo — own sheet](Brush-Artist-Refs-50-Thick-swipes-on-photo-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 24 % → 27 % | 42.6 px | 0.32 | 1.12 | 34 |
| stroke 2 | 21 % → 28 % | 42.4 px | 0.33 | 1.33 | 26 |
| stroke 3 | 26 % → 24 % | 41.8 px | 0.33 | 0.95 | 37 |
| stroke 4 | 26 % → 24 % | 42.6 px | 0.33 | 0.94 | 28 |
| stroke 5 | 24 % → 22 % | 41.8 px | 0.33 | 0.95 | 36 |
| stroke 6 | 21 % → 19 % | 42.9 px | 0.33 | 0.94 | 23 |
| stroke 7 | 36 % → 37 % | 59.4 px | 0.33 | 1.02 | 38 |
| stroke 8 | 34 % → 33 % | 66.7 px | 0.32 | 0.97 | 29 |
| stroke 9 | 25 % → 23 % | 42.0 px | 0.33 | 0.95 | 32 |
| stroke 10 | 28 % → 27 % | 42.2 px | 0.33 | 0.95 | 37 |
| stroke 11 | 23 % → 21 % | 42.6 px | 0.33 | 0.95 | 28 |
| stroke 12 | 24 % → 23 % | 53.2 px | 0.33 | 0.95 | 19 |

## Brush Artist · Ink — dry brush — own sheet
own sheet 600 × 600 · Gouache · 30 px · 2.7 s

![Brush Artist · Ink — dry brush — own sheet](Brush-Artist-Ink-dry-brush-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| ear | 17 % → 4 % | 16.7 px | 0.82 | 0.24 | 453 |
| drag0 | 20 % → 24 % | 25.0 px | 0.82 | 1.22 | 117 |
| drag1 | 25 % → 25 % | 34.2 px | 0.82 | 1.02 | 104 |
| drag2 | 28 % → 25 % | 42.1 px | 0.82 | 0.92 | 91 |
| drag3 | 30 % → 26 % | 50.2 px | 0.82 | 0.87 | 72 |

## Brush Artist · Watercolour — blue — own sheet
own sheet 600 × 600 · Watercolor · 40 px · 6.5 s

![Brush Artist · Watercolour — blue — own sheet](Brush-Artist-Watercolour-blue-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| s0 | 14 % → 28 % | 28.4 px | 0.28 | 2.04 | 40 |
| s1 | 8 % → 36 % | 9.9 px | 0.40 | 4.46 | 38 |
| s2 | 12 % → 21 % | 28.5 px | 0.16 | 1.74 | 38 |
| s3 | 11 % → 18 % | 20.3 px | 0.26 | 1.68 | 53 |
| s4 | 17 % → 34 % | 36.6 px | 0.38 | 1.96 | 54 |
| s5 | 25 % → 33 % | 34.0 px | 0.35 | 1.32 | 42 |
| s6 | 25 % → 30 % | 39.5 px | 0.28 | 1.23 | 42 |
| s7 | 27 % → 34 % | 18.5 px | 0.42 | 1.28 | 26 |
| s8 | 21 % → 25 % | 44.1 px | 0.22 | 1.19 | 32 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Charcoal — stick — own sheet
own sheet 600 × 600 · Charcoal · 28 px · 0.9 s

![Brush Artist · Charcoal — stick — own sheet](Brush-Artist-Charcoal-stick-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| finger0 | 16 % → 21 % | 15.5 px | 0.83 | 1.33 | 23 |
| tip0 | 15 % → 22 % | 18.4 px | 0.83 | 1.47 | 6 |
| finger1 | 16 % → 26 % | 15.7 px | 0.83 | 1.64 | 22 |
| tip1 | 20 % → 27 % | 24.8 px | 0.83 | 1.34 | 9 |
| finger2 | 16 % → 24 % | 16.0 px | 0.83 | 1.45 | 22 |
| tip2 | 20 % → 27 % | 24.1 px | 0.83 | 1.34 | 5 |
| finger3 | 16 % → 18 % | 16.1 px | 0.83 | 1.12 | 20 |
| tip3 | 20 % → 20 % | 24.3 px | 0.83 | 1.00 | 6 |
| cig0 | 38 % → 50 % | 35.5 px | 0.83 | 1.32 | 10 |
| cig1 | 42 % → 55 % | 39.5 px | 0.83 | 1.30 | 10 |
| cig2 | 47 % → 60 % | 44.1 px | 0.83 | 1.27 | 6 |
| cig3 | 51 % → 60 % | 47.1 px | 0.83 | 1.20 | 6 |
| cig4 | 50 % → 55 % | 46.8 px | 0.83 | 1.10 | 7 |
| cig5 | 51 % → 51 % | 47.1 px | 0.83 | 1.00 | 6 |

Numbers say: wet paint spreads well beyond the stroke.

