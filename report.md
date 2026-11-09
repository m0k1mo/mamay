![All brushes](contact.png)

# Brush Lab — 321 brushes · Nov 9, 2026 at 1:52 AM

Every sheet: 1500 × 600, ten strokes in a 5 × 2 grid — 1. light line · 2. heavy line · 3. pressure swell · 4. fast wave · 5. slow wave · 6. spiral · 7. loop · 8. tilted · 9. over the wet one · 10. long, no reload (cell 8 holds «tilted» and «over the wet one» crossed). The CPU reference of Mamay's paint engine; the wet layer settles 20 s at the end.

Columns: **covered** = share of the cell with paint right after the stroke → after settling; **width** = painted area of the stroke ÷ its length (px); **dark** = mean darkness of the painted pixels above the paper's own grain (0 = paper, 1 = black); **spread** = how far wet paint went beyond the stroke (1.0 = stayed); **ms** = the stroke on the CPU; long stroke: paint in each quarter of its length (it should run out: wet → streaks → dry tail).

## Ink Line
Ink · 12 px · 24.6 s

![Ink Line](Ink-Line.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 1 % → 4 % | 4.3 px | 0.55 | 2.45 | 58 |
| heavy line | 5 % → 6 % | 15.7 px | 0.68 | 1.14 | 65 |
| pressure swell | 3 % → 4 % | 11.3 px | 0.64 | 1.40 | 41 |
| fast wave | 10 % → 11 % | 11.2 px | 0.59 | 1.11 | 137 |
| slow wave | 8 % → 10 % | 9.6 px | 0.57 | 1.16 | 169 |
| spiral | 14 % → 15 % | 8.9 px | 0.49 | 1.07 | 275 |
| loop | 8 % → 9 % | 10.6 px | 0.61 | 1.15 | 107 |
| tilted | 5 % → 5 % | 14.3 px | 0.64 | 1.05 | 57 |
| over the wet one | 10 % → 11 % | 12.5 px | 0.64 | 1.15 | 60 |
| long, no reload | 18 % → 17 % | 8.1 px | 0.47 | 0.96 | 378 | quarters: 0.22 → 0.09 → 0.04 → 0.02

Numbers say: light vs heavy: width 4.3 → 15.7 px, dark 0.55 → 0.68; wet paint spreads well beyond the stroke.

## Dense Ink
Ink · 14 px · 25.4 s

![Dense Ink](Dense-Ink.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 5 % → 7 % | 15.2 px | 0.72 | 1.27 | 58 |
| heavy line | 7 % → 7 % | 19.1 px | 0.73 | 1.09 | 74 |
| pressure swell | 5 % → 6 % | 17.9 px | 0.72 | 1.18 | 53 |
| fast wave | 13 % → 13 % | 15.2 px | 0.69 | 1.01 | 147 |
| slow wave | 12 % → 12 % | 13.5 px | 0.67 | 1.04 | 214 |
| spiral | 18 % → 15 % | 12.2 px | 0.65 | 0.80 | 350 |
| loop | 11 % → 12 % | 14.8 px | 0.69 | 1.08 | 131 |
| tilted | 5 % → 6 % | 14.5 px | 0.72 | 1.07 | 70 |
| over the wet one | 12 % → 13 % | 17.7 px | 0.72 | 1.12 | 60 |
| long, no reload | 23 % → 15 % | 10.1 px | 0.64 | 0.66 | 468 | quarters: 0.30 → 0.12 → 0.04 → 0.02

Numbers say: light vs heavy: width 15.2 → 19.1 px, dark 0.72 → 0.73.

## Transparent Wash
Watercolor · 22 px · 26.7 s

![Transparent Wash](Transparent-Wash.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 2 % → 5 % | 6.9 px | 0.27 | 2.26 | 47 |
| heavy line | 7 % → 9 % | 20.4 px | 0.27 | 1.23 | 60 |
| pressure swell | 4 % → 6 % | 15.2 px | 0.28 | 1.54 | 40 |
| fast wave | 14 % → 16 % | 16.1 px | 0.20 | 1.17 | 129 |
| slow wave | 12 % → 15 % | 13.7 px | 0.21 | 1.28 | 258 |
| spiral | 18 % → 22 % | 11.9 px | 0.16 | 1.22 | 200 |
| loop | 11 % → 13 % | 14.5 px | 0.22 | 1.20 | 105 |
| tilted | 8 % → 8 % | 21.1 px | 0.24 | 1.06 | 65 |
| over the wet one | 13 % → 16 % | 16.4 px | 0.24 | 1.19 | 52 |
| long, no reload | 26 % → 32 % | 11.6 px | 0.13 | 1.22 | 365 | quarters: 0.11 → 0.04 → 0.02 → 0.01

Numbers say: light vs heavy: width 6.9 → 20.4 px, dark 0.27 → 0.27; wet paint spreads well beyond the stroke.

## Dry Brush
Gouache · 24 px · 32.7 s

![Dry Brush](Dry-Brush.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 5 % → 1 % | 13.8 px | 0.65 | 0.11 | 58 |
| heavy line | 6 % → 0 % | 18.4 px | 0.65 | 0.02 | 198 |
| pressure swell | 5 % → 0 % | 18.1 px | 0.65 | 0.09 | 53 |
| fast wave | 6 % → 1 % | 6.9 px | 0.65 | 0.08 | 233 |
| slow wave | 7 % → 0 % | 7.8 px | 0.65 | 0.07 | 394 |
| spiral | 7 % → 1 % | 4.4 px | 0.65 | 0.08 | 300 |
| loop | 9 % → 0 % | 12.2 px | 0.65 | 0.05 | 165 |
| tilted | 4 % → 3 % | 10.3 px | 0.65 | 0.89 | 89 |
| over the wet one | 9 % → 1 % | 14.3 px | 0.65 | 0.12 | 85 |
| long, no reload | 6 % → 1 % | 2.7 px | 0.65 | 0.15 | 444 | quarters: 0.12 → 0.00 → 0.00 → 0.00

Numbers say: light vs heavy: width 13.8 → 18.4 px, dark 0.65 → 0.65.

## Wax Crayon
Wax · 8 px · 12.9 s

![Wax Crayon](Wax-Crayon.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 1 % → 1 % | 2.5 px | 0.71 | 1.00 | 39 |
| heavy line | 1 % → 1 % | 3.9 px | 0.69 | 1.00 | 35 |
| pressure swell | 1 % → 1 % | 3.3 px | 0.70 | 1.00 | 16 |
| fast wave | 3 % → 3 % | 3.5 px | 0.69 | 1.00 | 75 |
| slow wave | 3 % → 3 % | 3.4 px | 0.70 | 1.00 | 52 |
| spiral | 5 % → 5 % | 3.3 px | 0.70 | 1.00 | 116 |
| loop | 3 % → 3 % | 3.3 px | 0.70 | 1.00 | 58 |
| tilted | 2 % → 2 % | 5.6 px | 0.68 | 1.00 | 43 |
| over the wet one | 3 % → 3 % | 3.6 px | 0.68 | 1.00 | 28 |
| long, no reload | 7 % → 7 % | 3.3 px | 0.70 | 1.00 | 202 | quarters: 0.06 → 0.06 → 0.06 → 0.06

Numbers say: light vs heavy: width 2.5 → 3.9 px, dark 0.71 → 0.69; the long stroke does not run out of paint.

## Oil Pastel
Wax · 12 px · 12.9 s

![Oil Pastel](Oil-Pastel.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 1 % → 1 % | 4.0 px | 0.68 | 1.00 | 45 |
| heavy line | 2 % → 2 % | 6.5 px | 0.68 | 1.00 | 57 |
| pressure swell | 2 % → 2 % | 5.7 px | 0.69 | 1.00 | 44 |
| fast wave | 5 % → 5 % | 5.7 px | 0.68 | 1.00 | 121 |
| slow wave | 5 % → 5 % | 5.5 px | 0.68 | 1.00 | 113 |
| spiral | 8 % → 8 % | 5.5 px | 0.68 | 1.00 | 189 |
| loop | 4 % → 4 % | 5.6 px | 0.68 | 1.00 | 76 |
| tilted | 2 % → 2 % | 6.8 px | 0.68 | 1.00 | 51 |
| over the wet one | 5 % → 5 % | 5.8 px | 0.68 | 1.00 | 44 |
| long, no reload | 13 % → 13 % | 5.6 px | 0.68 | 1.00 | 203 | quarters: 0.10 → 0.09 → 0.10 → 0.10

Numbers say: light vs heavy: width 4.0 → 6.5 px, dark 0.68 → 0.68; the long stroke does not run out of paint.

## Charcoal
Charcoal · 5 px · 13.2 s

![Charcoal](Charcoal.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 1 % → 1 % | 2.0 px | 0.74 | 1.00 | 33 |
| heavy line | 1 % → 1 % | 3.0 px | 0.74 | 1.00 | 15 |
| pressure swell | 1 % → 1 % | 2.7 px | 0.74 | 1.00 | 20 |
| fast wave | 2 % → 2 % | 2.7 px | 0.73 | 1.00 | 51 |
| slow wave | 2 % → 2 % | 2.6 px | 0.74 | 1.00 | 68 |
| spiral | 4 % → 4 % | 2.5 px | 0.74 | 1.00 | 122 |
| loop | 2 % → 2 % | 2.6 px | 0.74 | 1.00 | 66 |
| tilted | 2 % → 2 % | 4.3 px | 0.72 | 1.00 | 45 |
| over the wet one | 2 % → 2 % | 2.4 px | 0.72 | 1.00 | 25 |
| long, no reload | 6 % → 6 % | 2.7 px | 0.73 | 1.00 | 84 | quarters: 0.05 → 0.05 → 0.05 → 0.05

Numbers say: light vs heavy: width 2.0 → 3.0 px, dark 0.74 → 0.74; the long stroke does not run out of paint.

## Impasto
Heavy acrylic · 22 px · 23.0 s

![Impasto](Impasto.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 8 % → 8 % | 24.1 px | 0.72 | 0.93 | 116 |
| heavy line | 10 % → 9 % | 28.8 px | 0.70 | 0.94 | 172 |
| pressure swell | 7 % → 7 % | 28.1 px | 0.72 | 0.94 | 131 |
| fast wave | 20 % → 13 % | 23.4 px | 0.71 | 0.64 | 325 |
| slow wave | 21 % → 14 % | 24.5 px | 0.71 | 0.66 | 309 |
| spiral | 30 % → 14 % | 19.9 px | 0.71 | 0.46 | 432 |
| loop | 18 % → 14 % | 23.9 px | 0.71 | 0.77 | 205 |
| tilted | 8 % → 8 % | 21.7 px | 0.70 | 1.00 | 115 |
| over the wet one | 17 % → 15 % | 25.4 px | 0.70 | 0.91 | 86 |
| long, no reload | 33 % → 14 % | 14.9 px | 0.71 | 0.42 | 485 | quarters: 0.38 → 0.21 → 0.10 → 0.03

Numbers say: light vs heavy: width 24.1 → 28.8 px, dark 0.72 → 0.70.

## Oil Round
Oil · 18 px · 24.0 s

![Oil Round](Oil-Round.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 2 % → 2 % | 7.2 px | 0.75 | 1.00 | 126 |
| heavy line | 7 % → 7 % | 19.3 px | 0.73 | 1.00 | 138 |
| pressure swell | 4 % → 4 % | 13.7 px | 0.72 | 1.00 | 80 |
| fast wave | 11 % → 11 % | 12.8 px | 0.65 | 1.00 | 371 |
| slow wave | 8 % → 8 % | 9.0 px | 0.57 | 1.00 | 241 |
| spiral | 10 % → 10 % | 6.6 px | 0.50 | 1.00 | 314 |
| loop | 6 % → 6 % | 7.2 px | 0.45 | 1.00 | 173 |
| tilted | 4 % → 4 % | 10.1 px | 0.52 | 1.00 | 115 |
| over the wet one | 6 % → 6 % | 7.6 px | 0.52 | 1.00 | 89 |
| long, no reload | 15 % → 15 % | 6.9 px | 0.42 | 1.00 | 484 | quarters: 0.09 → 0.08 → 0.07 → 0.06

Numbers say: light vs heavy: width 7.2 → 19.3 px, dark 0.75 → 0.73.

## Palette Knife
Oil · 20 px · 21.1 s

![Palette Knife](Palette-Knife.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 8 % → 8 % | 21.9 px | 0.67 | 1.00 | 31 |
| heavy line | 8 % → 8 % | 22.5 px | 0.74 | 1.00 | 21 |
| pressure swell | 6 % → 6 % | 22.3 px | 0.74 | 1.00 | 9 |
| fast wave | 16 % → 16 % | 18.9 px | 0.50 | 1.00 | 44 |
| slow wave | 17 % → 17 % | 19.9 px | 0.43 | 1.00 | 56 |
| spiral | 17 % → 17 % | 11.3 px | 0.46 | 1.00 | 61 |
| loop | 16 % → 16 % | 21.0 px | 0.59 | 1.00 | 33 |
| tilted | 5 % → 5 % | 15.0 px | 0.72 | 1.00 | 21 |
| over the wet one | 13 % → 13 % | 21.0 px | 0.72 | 1.00 | 31 |
| long, no reload | 16 % → 16 % | 7.2 px | 0.49 | 1.00 | 93 | quarters: 0.29 → 0.05 → 0.00 → 0.00

Numbers say: light vs heavy: width 21.9 → 22.5 px, dark 0.67 → 0.74; pressure barely changes the width.

## Water
Watercolor · 20 px · 42.0 s · over bands of wet oil paint and oil pastel in turn (it works on paint already there: look at what it does to the bands; covered counts the bands too)

![Water](Water.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 25 % → 27 % | 73.8 px | 0.80 | 1.06 | 27 |
| heavy line | 24 % → 25 % | 69.8 px | 0.81 | 1.04 | 90 |
| pressure swell | 24 % → 25 % | 89.6 px | 0.81 | 1.03 | 38 |
| fast wave | 24 % → 26 % | 27.7 px | 0.81 | 1.07 | 130 |
| slow wave | 24 % → 25 % | 27.8 px | 0.81 | 1.06 | 171 |
| spiral | 24 % → 26 % | 15.9 px | 0.81 | 1.07 | 224 |
| loop | 24 % → 25 % | 31.1 px | 0.81 | 1.03 | 180 |
| tilted | 24 % → 24 % | 67.0 px | 0.81 | 1.00 | 59 |
| over the wet one | 24 % → 25 % | 0.0 px | 0.81 | 1.06 | 45 |
| long, no reload | 24 % → 26 % | 10.7 px | 0.81 | 1.08 | 310 | quarters: 0.21 → 0.27 → 0.18 → 0.27

Numbers say: light vs heavy: width 73.8 → 69.8 px, dark 0.80 → 0.81; pressure barely changes the width; the long stroke does not run out of paint.

## Blender
Pastel · 16 px · 25.3 s · over bands of wet oil paint and oil pastel in turn (it works on paint already there: look at what it does to the bands; covered counts the bands too)

![Blender](Blender.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 24 % → 24 % | 70.7 px | 0.81 | 1.00 | 33 |
| heavy line | 25 % → 25 % | 72.1 px | 0.80 | 1.00 | 60 |
| pressure swell | 24 % → 24 % | 91.3 px | 0.81 | 1.00 | 33 |
| fast wave | 26 % → 26 % | 30.0 px | 0.79 | 1.00 | 97 |
| slow wave | 26 % → 26 % | 29.9 px | 0.80 | 1.00 | 108 |
| spiral | 28 % → 28 % | 18.7 px | 0.77 | 1.00 | 154 |
| loop | 25 % → 25 % | 33.0 px | 0.80 | 1.00 | 82 |
| tilted | 25 % → 25 % | 70.1 px | 0.79 | 1.00 | 53 |
| over the wet one | 26 % → 26 % | 1.8 px | 0.79 | 1.00 | 37 |
| long, no reload | 30 % → 30 % | 13.7 px | 0.76 | 1.00 | 241 | quarters: 0.20 → 0.28 → 0.23 → 0.30

Numbers say: light vs heavy: width 70.7 → 72.1 px, dark 0.81 → 0.80; pressure barely changes the width; the long stroke does not run out of paint.

## Eraser
Eraser · 16 px · 25.5 s · over bands of wet oil paint and oil pastel in turn (it works on paint already there: look at what it does to the bands; covered counts the bands too)

![Eraser](Eraser.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 24 % → 24 % | 69.6 px | 0.82 | 1.00 | 35 |
| heavy line | 23 % → 23 % | 67.9 px | 0.82 | 1.00 | 45 |
| pressure swell | 23 % → 23 % | 87.3 px | 0.82 | 1.00 | 30 |
| fast wave | 22 % → 22 % | 25.7 px | 0.82 | 1.00 | 96 |
| slow wave | 22 % → 22 % | 25.7 px | 0.82 | 1.00 | 120 |
| spiral | 22 % → 22 % | 14.4 px | 0.82 | 1.00 | 155 |
| loop | 22 % → 22 % | 28.6 px | 0.82 | 1.00 | 87 |
| tilted | 23 % → 23 % | 65.1 px | 0.82 | 1.00 | 58 |
| over the wet one | 23 % → 23 % | 0.0 px | 0.82 | 1.00 | 40 |
| long, no reload | 20 % → 20 % | 8.9 px | 0.82 | 1.00 | 258 | quarters: 0.15 → 0.20 → 0.15 → 0.20

Numbers say: light vs heavy: width 69.6 → 67.9 px, dark 0.82 → 0.82; pressure barely changes the width; the long stroke does not run out of paint.

## Fan
Gouache · 30 px · 38.4 s

![Fan](Fan.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 9 % → 3 % | 25.6 px | 0.63 | 0.37 | 40 |
| heavy line | 11 % → 4 % | 30.9 px | 0.63 | 0.39 | 85 |
| pressure swell | 8 % → 5 % | 31.7 px | 0.63 | 0.55 | 40 |
| fast wave | 17 % → 5 % | 20.2 px | 0.63 | 0.26 | 202 |
| slow wave | 18 % → 5 % | 21.0 px | 0.63 | 0.25 | 241 |
| spiral | 24 % → 5 % | 15.5 px | 0.63 | 0.19 | 221 |
| loop | 17 % → 5 % | 22.7 px | 0.63 | 0.28 | 120 |
| tilted | 5 % → 6 % | 15.0 px | 0.63 | 1.05 | 53 |
| over the wet one | 16 % → 8 % | 29.7 px | 0.63 | 0.49 | 51 |
| long, no reload | 22 % → 5 % | 9.9 px | 0.63 | 0.22 | 398 | quarters: 0.29 → 0.07 → 0.01 → 0.00

Numbers say: light vs heavy: width 25.6 → 30.9 px, dark 0.63 → 0.63.

## Sponge
Gouache · 30 px · 38.1 s

![Sponge](Sponge.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 4 % → 0 % | 11.3 px | 0.62 | 0.12 | 96 |
| heavy line | 12 % → 2 % | 35.4 px | 0.62 | 0.14 | 119 |
| pressure swell | 7 % → 2 % | 27.9 px | 0.62 | 0.28 | 46 |
| fast wave | 20 % → 4 % | 23.2 px | 0.62 | 0.19 | 143 |
| slow wave | 21 % → 4 % | 23.8 px | 0.62 | 0.18 | 265 |
| spiral | 28 % → 4 % | 18.3 px | 0.62 | 0.14 | 244 |
| loop | 18 % → 5 % | 23.0 px | 0.62 | 0.29 | 180 |
| tilted | 7 % → 7 % | 18.2 px | 0.62 | 1.04 | 122 |
| over the wet one | 16 % → 6 % | 27.8 px | 0.62 | 0.37 | 65 |
| long, no reload | 29 % → 5 % | 12.9 px | 0.62 | 0.17 | 371 | quarters: 0.29 → 0.13 → 0.07 → 0.04

Numbers say: light vs heavy: width 11.3 → 35.4 px, dark 0.62 → 0.62.

## Ink — sumi brush
Watercolour 1.00 · 22 px · 40.1 s

![Ink — sumi brush](Ink-sumi-brush.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 8 % → 9 % | 23.9 px | 0.87 | 1.13 | 153 |
| heavy line | 12 % → 13 % | 36.2 px | 0.86 | 1.01 | 102 |
| pressure swell | 10 % → 10 % | 36.1 px | 0.87 | 1.04 | 58 |
| fast wave | 27 % → 27 % | 31.0 px | 0.82 | 1.00 | 210 |
| slow wave | 27 % → 28 % | 31.2 px | 0.82 | 1.02 | 311 |
| spiral | 38 % → 36 % | 25.2 px | 0.75 | 0.95 | 374 |
| loop | 22 % → 23 % | 29.0 px | 0.84 | 1.01 | 207 |
| tilted | 9 % → 9 % | 25.7 px | 0.86 | 1.00 | 109 |
| over the wet one | 20 % → 20 % | 30.0 px | 0.86 | 1.02 | 86 |
| long, no reload | 46 % → 41 % | 20.7 px | 0.70 | 0.90 | 549 | quarters: 0.57 → 0.42 → 0.24 → 0.15

Numbers say: light vs heavy: width 23.9 → 36.2 px, dark 0.87 → 0.86.

## Ink — wash
Watercolour 1.00 · 40 px · 41.0 s

![Ink — wash](Ink-wash.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 13 % → 13 % | 37.3 px | 0.42 | 1.02 | 98 |
| heavy line | 19 % → 19 % | 55.2 px | 0.35 | 1.01 | 114 |
| pressure swell | 13 % → 13 % | 48.2 px | 0.41 | 1.02 | 67 |
| fast wave | 41 % → 42 % | 47.8 px | 0.32 | 1.02 | 361 |
| slow wave | 39 % → 40 % | 45.3 px | 0.42 | 1.02 | 487 |
| spiral | 60 % → 62 % | 39.7 px | 0.33 | 1.02 | 432 |
| loop | 34 % → 34 % | 43.8 px | 0.39 | 1.01 | 201 |
| tilted | 15 % → 15 % | 40.7 px | 0.43 | 1.01 | 129 |
| over the wet one | 30 % → 31 % | 43.4 px | 0.43 | 1.02 | 107 |
| long, no reload | 71 % → 75 % | 32.0 px | 0.31 | 1.05 | 637 | quarters: 0.40 → 0.29 → 0.19 → 0.12

Numbers say: light vs heavy: width 37.3 → 55.2 px, dark 0.42 → 0.35.

## Ink — dry brush
Ink 1.00 · 30 px · 29.4 s

![Ink — dry brush](Ink-dry-brush.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 5 % → 5 % | 15.1 px | 0.82 | 0.94 | 158 |
| heavy line | 7 % → 6 % | 19.2 px | 0.82 | 0.90 | 253 |
| pressure swell | 5 % → 5 % | 18.7 px | 0.82 | 0.98 | 115 |
| fast wave | 12 % → 8 % | 13.3 px | 0.81 | 0.66 | 304 |
| slow wave | 12 % → 8 % | 14.1 px | 0.81 | 0.62 | 500 |
| spiral | 16 % → 8 % | 10.8 px | 0.80 | 0.48 | 511 |
| loop | 11 % → 9 % | 14.4 px | 0.79 | 0.77 | 295 |
| tilted | 5 % → 6 % | 14.9 px | 0.81 | 1.08 | 161 |
| over the wet one | 12 % → 11 % | 18.1 px | 0.81 | 0.95 | 135 |
| long, no reload | 19 % → 9 % | 8.5 px | 0.79 | 0.46 | 734 | quarters: 0.26 → 0.09 → 0.03 → 0.01

Numbers say: light vs heavy: width 15.1 → 19.2 px, dark 0.82 → 0.82.

## Ink — nib
Watercolour 1.00 · 5 px · 27.7 s

![Ink — nib](Ink-nib.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 2 % → 5 % | 5.5 px | 0.89 | 2.46 | 40 |
| heavy line | 2 % → 5 % | 6.4 px | 0.89 | 2.34 | 32 |
| pressure swell | 2 % → 4 % | 6.2 px | 0.89 | 2.53 | 26 |
| fast wave | 5 % → 8 % | 5.9 px | 0.89 | 1.63 | 101 |
| slow wave | 5 % → 8 % | 5.7 px | 0.89 | 1.70 | 81 |
| spiral | 8 % → 11 % | 5.0 px | 0.87 | 1.41 | 147 |
| loop | 4 % → 8 % | 5.7 px | 0.89 | 1.74 | 85 |
| tilted | 4 % → 4 % | 10.3 px | 0.89 | 1.02 | 36 |
| over the wet one | 6 % → 9 % | 6.1 px | 0.89 | 1.61 | 38 |
| long, no reload | 9 % → 12 % | 4.2 px | 0.85 | 1.30 | 201 | quarters: 0.24 → 0.11 → 0.07 → 0.05

Numbers say: light vs heavy: width 5.5 → 6.4 px, dark 0.89 → 0.89; wet paint spreads well beyond the stroke.

## 0.45 · Dry brush
Gouache 0.91 · Ink 0.07 · 34 px · 36.7 s

![0.45 · Dry brush](0-45-Dry-brush.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 9 % → 5 % | 26.6 px | 0.68 | 0.58 | 192 |
| heavy line | 10 % → 6 % | 28.1 px | 0.68 | 0.61 | 167 |
| pressure swell | 7 % → 6 % | 27.6 px | 0.68 | 0.76 | 118 |
| fast wave | 18 % → 7 % | 20.2 px | 0.68 | 0.41 | 392 |
| slow wave | 20 % → 8 % | 22.6 px | 0.68 | 0.38 | 737 |
| spiral | 27 % → 8 % | 18.1 px | 0.68 | 0.29 | 752 |
| loop | 18 % → 9 % | 23.1 px | 0.68 | 0.49 | 519 |
| tilted | 8 % → 8 % | 21.7 px | 0.68 | 1.02 | 248 |
| over the wet one | 18 % → 14 % | 27.7 px | 0.68 | 0.77 | 181 |
| long, no reload | 31 % → 10 % | 14.1 px | 0.68 | 0.32 | 1053 | quarters: 0.36 → 0.25 → 0.17 → 0.14

Numbers say: light vs heavy: width 26.6 → 28.1 px, dark 0.68 → 0.68; pressure barely changes the width.

## Dry pastel
Pastel 1.00 · 26 px · 13.4 s

![Dry pastel](Dry-pastel.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 3 % → 3 % | 8.2 px | 0.37 | 1.00 | 43 |
| heavy line | 5 % → 5 % | 13.1 px | 0.39 | 1.00 | 42 |
| pressure swell | 3 % → 3 % | 11.5 px | 0.39 | 1.00 | 40 |
| fast wave | 10 % → 10 % | 11.9 px | 0.39 | 1.00 | 110 |
| slow wave | 10 % → 10 % | 11.1 px | 0.39 | 1.00 | 220 |
| spiral | 14 % → 14 % | 9.1 px | 0.38 | 1.00 | 216 |
| loop | 7 % → 7 % | 9.5 px | 0.38 | 1.00 | 118 |
| tilted | 3 % → 3 % | 7.5 px | 0.39 | 1.00 | 55 |
| over the wet one | 6 % → 6 % | 10.6 px | 0.39 | 1.00 | 50 |
| long, no reload | 17 % → 17 % | 7.6 px | 0.38 | 1.00 | 315 | quarters: 0.08 → 0.07 → 0.07 → 0.07

Numbers say: light vs heavy: width 8.2 → 13.1 px, dark 0.37 → 0.39; the long stroke does not run out of paint.

## 0.45 · Charcoal
Charcoal 1.00 · 18 px · 14.4 s

![0.45 · Charcoal](0-45-Charcoal.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 2 % → 2 % | 6.2 px | 0.80 | 1.00 | 31 |
| heavy line | 3 % → 3 % | 9.5 px | 0.80 | 1.00 | 29 |
| pressure swell | 2 % → 2 % | 7.8 px | 0.80 | 1.00 | 28 |
| fast wave | 8 % → 8 % | 8.8 px | 0.80 | 1.00 | 70 |
| slow wave | 6 % → 6 % | 7.3 px | 0.80 | 1.00 | 90 |
| spiral | 10 % → 10 % | 6.7 px | 0.80 | 1.00 | 105 |
| loop | 6 % → 6 % | 8.2 px | 0.81 | 1.00 | 53 |
| tilted | 3 % → 3 % | 7.4 px | 0.80 | 1.00 | 26 |
| over the wet one | 5 % → 5 % | 7.9 px | 0.80 | 1.00 | 33 |
| long, no reload | 18 % → 18 % | 7.9 px | 0.80 | 1.00 | 152 | quarters: 0.15 → 0.16 → 0.16 → 0.17

Numbers say: light vs heavy: width 6.2 → 9.5 px, dark 0.80 → 0.80; the long stroke does not run out of paint.

## Watercolour — wash
Watercolour 1.00 · 50 px · 45.8 s

![Watercolour — wash](Watercolour-wash.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 16 % → 16 % | 45.5 px | 0.22 | 1.01 | 129 |
| heavy line | 22 % → 22 % | 64.9 px | 0.19 | 1.00 | 183 |
| pressure swell | 15 % → 15 % | 56.1 px | 0.22 | 1.01 | 104 |
| fast wave | 48 % → 49 % | 55.5 px | 0.19 | 1.01 | 319 |
| slow wave | 46 % → 46 % | 53.3 px | 0.24 | 1.00 | 599 |
| spiral | 66 % → 66 % | 43.7 px | 0.21 | 1.00 | 1230 |
| loop | 40 % → 40 % | 51.4 px | 0.22 | 1.00 | 507 |
| tilted | 18 % → 18 % | 49.7 px | 0.23 | 1.00 | 210 |
| over the wet one | 36 % → 36 % | 49.6 px | 0.23 | 1.01 | 127 |
| long, no reload | 84 % → 84 % | 37.7 px | 0.20 | 1.00 | 809 | quarters: 0.24 → 0.20 → 0.16 → 0.12

Numbers say: light vs heavy: width 45.5 → 64.9 px, dark 0.22 → 0.19.

## Watercolour — wet-in-wet
Watercolour 1.00 · 44 px · 46.5 s

![Watercolour — wet-in-wet](Watercolour-wet-in-wet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 13 % → 21 % | 37.4 px | 0.32 | 1.63 | 142 |
| heavy line | 19 % → 22 % | 54.7 px | 0.34 | 1.17 | 205 |
| pressure swell | 12 % → 17 % | 45.7 px | 0.36 | 1.36 | 102 |
| fast wave | 42 % → 49 % | 48.5 px | 0.33 | 1.16 | 279 |
| slow wave | 40 % → 48 % | 45.7 px | 0.41 | 1.22 | 478 |
| spiral | 63 % → 69 % | 41.3 px | 0.37 | 1.11 | 476 |
| loop | 34 % → 41 % | 44.0 px | 0.37 | 1.21 | 247 |
| tilted | 16 % → 17 % | 44.6 px | 0.36 | 1.05 | 157 |
| over the wet one | 32 % → 40 % | 44.4 px | 0.36 | 1.26 | 126 |
| long, no reload | 79 % → 87 % | 35.3 px | 0.36 | 1.11 | 774 | quarters: 0.40 → 0.37 → 0.33 → 0.26

Numbers say: light vs heavy: width 37.4 → 54.7 px, dark 0.32 → 0.34; wet paint spreads well beyond the stroke.

## Watercolour — glaze
Watercolour 1.00 · 38 px · 39.1 s

![Watercolour — glaze](Watercolour-glaze.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 13 % → 13 % | 36.6 px | 0.07 | 1.02 | 88 |
| heavy line | 19 % → 19 % | 55.4 px | 0.07 | 1.00 | 105 |
| pressure swell | 13 % → 13 % | 47.0 px | 0.07 | 1.02 | 79 |
| fast wave | 39 % → 40 % | 45.6 px | 0.07 | 1.01 | 269 |
| slow wave | 37 % → 37 % | 42.8 px | 0.07 | 1.01 | 417 |
| spiral | 59 % → 60 % | 38.8 px | 0.06 | 1.01 | 413 |
| loop | 33 % → 33 % | 42.6 px | 0.07 | 1.00 | 211 |
| tilted | 14 % → 14 % | 40.1 px | 0.07 | 1.00 | 136 |
| over the wet one | 30 % → 30 % | 42.3 px | 0.07 | 1.01 | 105 |
| long, no reload | 69 % → 70 % | 30.9 px | 0.06 | 1.01 | 878 | quarters: 0.06 → 0.05 → 0.03 → 0.02

Numbers say: light vs heavy: width 36.6 → 55.4 px, dark 0.07 → 0.07.

## Watercolour — granulating
Watercolour 1.00 · 44 px · 43.1 s

![Watercolour — granulating](Watercolour-granulating.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 14 % → 14 % | 41.4 px | 0.35 | 1.01 | 106 |
| heavy line | 21 % → 21 % | 60.4 px | 0.31 | 1.00 | 138 |
| pressure swell | 14 % → 14 % | 52.2 px | 0.34 | 1.01 | 79 |
| fast wave | 45 % → 45 % | 51.7 px | 0.29 | 1.01 | 290 |
| slow wave | 42 % → 42 % | 48.2 px | 0.35 | 1.01 | 477 |
| spiral | 62 % → 63 % | 41.0 px | 0.30 | 1.01 | 484 |
| loop | 37 % → 37 % | 47.6 px | 0.33 | 1.00 | 241 |
| tilted | 16 % → 16 % | 45.5 px | 0.36 | 1.00 | 209 |
| over the wet one | 33 % → 33 % | 46.2 px | 0.36 | 1.01 | 111 |
| long, no reload | 75 % → 76 % | 33.6 px | 0.29 | 1.01 | 878 | quarters: 0.34 → 0.26 → 0.20 → 0.14

Numbers say: light vs heavy: width 41.4 → 60.4 px, dark 0.35 → 0.31.

## Watercolour — dry brush
Watercolour 1.00 · 36 px · 35.4 s

![Watercolour — dry brush](Watercolour-dry-brush.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 10 % → 9 % | 27.8 px | 0.17 | 0.99 | 116 |
| heavy line | 14 % → 12 % | 39.3 px | 0.16 | 0.92 | 199 |
| pressure swell | 11 % → 10 % | 39.6 px | 0.16 | 0.95 | 144 |
| fast wave | 27 % → 20 % | 31.3 px | 0.13 | 0.74 | 326 |
| slow wave | 25 % → 17 % | 28.9 px | 0.14 | 0.70 | 531 |
| spiral | 34 % → 19 % | 22.6 px | 0.13 | 0.56 | 538 |
| loop | 21 % → 18 % | 27.7 px | 0.14 | 0.85 | 281 |
| tilted | 10 % → 10 % | 28.5 px | 0.16 | 1.01 | 154 |
| over the wet one | 21 % → 20 % | 31.0 px | 0.16 | 0.95 | 148 |
| long, no reload | 35 % → 19 % | 15.9 px | 0.14 | 0.54 | 741 | quarters: 0.09 → 0.03 → 0.01 → 0.00

Numbers say: light vs heavy: width 27.8 → 39.3 px, dark 0.17 → 0.16.

## Gouache
Gouache 1.00 · 30 px · 37.9 s

![Gouache](Gouache.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 8 % → 5 % | 23.3 px | 0.29 | 0.60 | 109 |
| heavy line | 12 % → 5 % | 35.5 px | 0.28 | 0.41 | 127 |
| pressure swell | 10 % → 5 % | 36.2 px | 0.28 | 0.49 | 87 |
| fast wave | 22 % → 6 % | 25.0 px | 0.28 | 0.27 | 271 |
| slow wave | 22 % → 7 % | 25.9 px | 0.28 | 0.30 | 447 |
| spiral | 28 % → 6 % | 18.4 px | 0.28 | 0.23 | 471 |
| loop | 18 % → 7 % | 23.7 px | 0.28 | 0.37 | 309 |
| tilted | 9 % → 9 % | 24.0 px | 0.28 | 1.01 | 149 |
| over the wet one | 19 % → 12 % | 28.7 px | 0.28 | 0.62 | 108 |
| long, no reload | 27 % → 8 % | 12.2 px | 0.28 | 0.31 | 652 | quarters: 0.01 → 0.02 → 0.02 → 0.02

Numbers say: light vs heavy: width 23.3 → 35.5 px, dark 0.29 → 0.28; the long stroke does not run out of paint.

## Oil — alla prima
Oil 0.89 · Oil glaze 0.11 · 30 px · 17.3 s

![Oil — alla prima](Oil-alla-prima.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 9 % → 9 % | 27.6 px | 0.50 | 1.00 | 128 |
| heavy line | 10 % → 10 % | 28.7 px | 0.50 | 1.00 | 125 |
| pressure swell | 7 % → 7 % | 27.5 px | 0.51 | 1.00 | 93 |
| fast wave | 22 % → 22 % | 25.5 px | 0.50 | 1.00 | 319 |
| slow wave | 25 % → 25 % | 29.0 px | 0.50 | 1.00 | 602 |
| spiral | 37 % → 37 % | 24.5 px | 0.49 | 1.00 | 530 |
| loop | 21 % → 21 % | 27.5 px | 0.50 | 1.00 | 392 |
| tilted | 10 % → 10 % | 26.8 px | 0.50 | 1.00 | 205 |
| over the wet one | 19 % → 19 % | 27.6 px | 0.50 | 1.00 | 180 |
| long, no reload | 45 % → 45 % | 20.2 px | 0.48 | 1.00 | 835 | quarters: 0.31 → 0.25 → 0.22 → 0.18

Numbers say: light vs heavy: width 27.6 → 28.7 px, dark 0.50 → 0.50; pressure barely changes the width.

## Oil — impasto
Oil heavy 1.00 · 34 px · 19.5 s

![Oil — impasto](Oil-impasto.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 11 % → 11 % | 31.1 px | 0.24 | 1.00 | 148 |
| heavy line | 13 % → 13 % | 36.7 px | 0.23 | 1.00 | 183 |
| pressure swell | 9 % → 9 % | 35.2 px | 0.24 | 1.00 | 106 |
| fast wave | 29 % → 29 % | 33.1 px | 0.23 | 1.00 | 389 |
| slow wave | 30 % → 30 % | 34.4 px | 0.22 | 1.00 | 956 |
| spiral | 47 % → 47 % | 31.2 px | 0.22 | 1.00 | 816 |
| loop | 25 % → 25 % | 32.3 px | 0.23 | 1.00 | 329 |
| tilted | 11 % → 11 % | 32.1 px | 0.24 | 1.00 | 180 |
| over the wet one | 23 % → 23 % | 32.7 px | 0.24 | 1.00 | 151 |
| long, no reload | 52 % → 52 % | 23.4 px | 0.21 | 1.00 | 959 | quarters: 0.17 → 0.13 → 0.11 → 0.09

Numbers say: light vs heavy: width 31.1 → 36.7 px, dark 0.24 → 0.23.

## Oil — glaze
Oil glaze 1.00 · 40 px · 19.4 s

![Oil — glaze](Oil-glaze.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 9 % → 9 % | 27.0 px | 0.50 | 1.00 | 113 |
| heavy line | 13 % → 13 % | 38.3 px | 0.49 | 1.00 | 145 |
| pressure swell | 10 % → 10 % | 36.6 px | 0.50 | 1.00 | 104 |
| fast wave | 29 % → 29 % | 33.5 px | 0.49 | 1.00 | 337 |
| slow wave | 30 % → 30 % | 34.6 px | 0.50 | 1.00 | 560 |
| spiral | 46 % → 46 % | 30.1 px | 0.49 | 1.00 | 552 |
| loop | 24 % → 24 % | 31.4 px | 0.50 | 1.00 | 311 |
| tilted | 11 % → 11 % | 30.4 px | 0.50 | 1.00 | 166 |
| over the wet one | 23 % → 23 % | 32.5 px | 0.50 | 1.00 | 121 |
| long, no reload | 52 % → 52 % | 23.5 px | 0.49 | 1.00 | 1042 | quarters: 0.34 → 0.30 → 0.27 → 0.22

Numbers say: light vs heavy: width 27.0 → 38.3 px, dark 0.50 → 0.49.

## Oil — scumble
Oil 1.00 · 36 px · 19.3 s

![Oil — scumble](Oil-scumble.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 10 % → 10 % | 29.3 px | 0.26 | 1.00 | 225 |
| heavy line | 9 % → 9 % | 26.7 px | 0.25 | 1.00 | 231 |
| pressure swell | 9 % → 9 % | 32.6 px | 0.26 | 1.00 | 139 |
| fast wave | 19 % → 19 % | 22.1 px | 0.21 | 1.00 | 421 |
| slow wave | 23 % → 23 % | 27.0 px | 0.20 | 1.00 | 780 |
| spiral | 33 % → 33 % | 21.6 px | 0.16 | 1.00 | 745 |
| loop | 19 % → 19 % | 24.0 px | 0.22 | 1.00 | 398 |
| tilted | 10 % → 10 % | 27.9 px | 0.25 | 1.00 | 202 |
| over the wet one | 20 % → 20 % | 28.2 px | 0.25 | 1.00 | 181 |
| long, no reload | 35 % → 35 % | 15.9 px | 0.15 | 1.00 | 1095 | quarters: 0.01 → 0.01 → 0.00 → 0.00

Numbers say: light vs heavy: width 29.3 → 26.7 px, dark 0.26 → 0.25; pressure barely changes the width.

## Acrylic — heavy body
Impasto 0.98 · 30 px · 18.3 s

![Acrylic — heavy body](Acrylic-heavy-body.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 8 % → 8 % | 24.3 px | 0.53 | 0.90 | 142 |
| heavy line | 8 % → 7 % | 24.1 px | 0.52 | 0.89 | 121 |
| pressure swell | 8 % → 7 % | 28.9 px | 0.53 | 0.90 | 85 |
| fast wave | 17 % → 13 % | 19.3 px | 0.53 | 0.78 | 297 |
| slow wave | 19 % → 15 % | 21.6 px | 0.52 | 0.79 | 525 |
| spiral | 24 % → 15 % | 15.8 px | 0.52 | 0.61 | 481 |
| loop | 17 % → 13 % | 22.1 px | 0.52 | 0.79 | 263 |
| tilted | 8 % → 8 % | 23.1 px | 0.53 | 0.99 | 138 |
| over the wet one | 17 % → 15 % | 25.5 px | 0.53 | 0.87 | 167 |
| long, no reload | 29 % → 17 % | 13.2 px | 0.52 | 0.57 | 703 | quarters: 0.24 → 0.15 → 0.11 → 0.08

Numbers say: light vs heavy: width 24.3 → 24.1 px, dark 0.53 → 0.52; pressure barely changes the width.

## Acrylic — fluid
Watercolour 1.00 · 36 px · 42.1 s

![Acrylic — fluid](Acrylic-fluid.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 12 % → 12 % | 33.6 px | 0.24 | 1.01 | 135 |
| heavy line | 18 % → 17 % | 50.9 px | 0.21 | 0.99 | 150 |
| pressure swell | 12 % → 12 % | 45.5 px | 0.23 | 1.01 | 78 |
| fast wave | 39 % → 39 % | 45.1 px | 0.19 | 0.99 | 253 |
| slow wave | 35 % → 35 % | 40.9 px | 0.22 | 1.00 | 468 |
| spiral | 55 % → 54 % | 36.4 px | 0.19 | 0.98 | 451 |
| loop | 31 % → 31 % | 40.0 px | 0.21 | 1.00 | 234 |
| tilted | 13 % → 13 % | 36.0 px | 0.24 | 1.00 | 162 |
| over the wet one | 28 % → 28 % | 42.4 px | 0.24 | 1.01 | 94 |
| long, no reload | 61 % → 58 % | 27.4 px | 0.19 | 0.95 | 610 | quarters: 0.20 → 0.14 → 0.09 → 0.06

Numbers say: light vs heavy: width 33.6 → 50.9 px, dark 0.24 → 0.21.

## Acrylic — palette knife
Impasto 1.00 · 42 px · 26.3 s

![Acrylic — palette knife](Acrylic-palette-knife.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 15 % → 15 % | 44.0 px | 0.39 | 0.98 | 55 |
| heavy line | 15 % → 15 % | 44.3 px | 0.40 | 0.98 | 44 |
| pressure swell | 12 % → 12 % | 43.6 px | 0.42 | 0.99 | 13 |
| fast wave | 36 % → 20 % | 42.0 px | 0.37 | 0.55 | 81 |
| slow wave | 37 % → 21 % | 42.7 px | 0.37 | 0.57 | 151 |
| spiral | 47 % → 18 % | 30.7 px | 0.37 | 0.39 | 163 |
| loop | 32 % → 24 % | 41.3 px | 0.36 | 0.77 | 73 |
| tilted | 12 % → 12 % | 33.7 px | 0.39 | 1.00 | 51 |
| over the wet one | 26 % → 25 % | 39.8 px | 0.39 | 0.97 | 63 |
| long, no reload | 53 % → 20 % | 23.7 px | 0.35 | 0.39 | 276 | quarters: 0.00 → 0.00 → 0.00 → 0.01

Numbers say: light vs heavy: width 44.0 → 44.3 px, dark 0.39 → 0.40; pressure barely changes the width; the long stroke does not run out of paint.

## Finger on oil
Oil 1.00 · 30 px · 16.9 s

![Finger on oil](Finger-on-oil.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 7 % → 7 % | 21.0 px | 0.38 | 1.00 | 72 |
| heavy line | 10 % → 10 % | 29.0 px | 0.36 | 1.00 | 93 |
| pressure swell | 7 % → 7 % | 27.7 px | 0.39 | 1.00 | 65 |
| fast wave | 18 % → 18 % | 20.8 px | 0.24 | 1.00 | 236 |
| slow wave | 18 % → 18 % | 21.3 px | 0.33 | 1.00 | 415 |
| spiral | 29 % → 29 % | 19.3 px | 0.27 | 1.00 | 424 |
| loop | 16 % → 16 % | 21.2 px | 0.33 | 1.00 | 163 |
| tilted | 9 % → 9 % | 26.1 px | 0.36 | 1.00 | 91 |
| over the wet one | 18 % → 18 % | 25.4 px | 0.36 | 1.00 | 66 |
| long, no reload | 29 % → 29 % | 13.1 px | 0.26 | 1.00 | 442 | quarters: 0.17 → 0.08 → 0.05 → 0.03

Numbers say: light vs heavy: width 21.0 → 29.0 px, dark 0.38 → 0.36.

## Palette knife — oil
Oil heavy 0.93 · Impasto 0.07 · 44 px · 26.5 s

![Palette knife — oil](Palette-knife-oil.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 16 % → 14 % | 45.7 px | 0.37 | 0.91 | 42 |
| heavy line | 16 % → 16 % | 46.3 px | 0.38 | 0.98 | 48 |
| pressure swell | 12 % → 12 % | 45.2 px | 0.38 | 0.99 | 18 |
| fast wave | 39 % → 35 % | 44.9 px | 0.35 | 0.89 | 157 |
| slow wave | 39 % → 36 % | 45.4 px | 0.35 | 0.92 | 300 |
| spiral | 62 % → 37 % | 40.7 px | 0.35 | 0.60 | 315 |
| loop | 34 % → 31 % | 43.8 px | 0.36 | 0.92 | 167 |
| tilted | 13 % → 13 % | 36.6 px | 0.37 | 1.00 | 55 |
| over the wet one | 28 % → 27 % | 40.8 px | 0.37 | 0.97 | 126 |
| long, no reload | 74 % → 40 % | 33.0 px | 0.34 | 0.54 | 276 | quarters: 0.00 → 0.00 → 0.01 → 0.01

Numbers say: light vs heavy: width 45.7 → 46.3 px, dark 0.37 → 0.38; pressure barely changes the width; the long stroke does not run out of paint.

## 0.45 · Sponge
Watercolour 0.93 · Ink 0.07 · 46 px · 41.9 s

![0.45 · Sponge](0-45-Sponge.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 27 % → 24 % | 77.5 px | 0.13 | 0.91 | 122 |
| heavy line | 32 % → 28 % | 92.0 px | 0.13 | 0.89 | 195 |
| pressure swell | 24 % → 22 % | 90.9 px | 0.13 | 0.91 | 81 |
| fast wave | 60 % → 54 % | 69.8 px | 0.12 | 0.90 | 337 |
| slow wave | 63 % → 59 % | 72.4 px | 0.17 | 0.94 | 455 |
| spiral | 77 % → 74 % | 51.0 px | 0.16 | 0.96 | 420 |
| loop | 54 % → 51 % | 70.4 px | 0.15 | 0.94 | 211 |
| tilted | 17 % → 17 % | 47.9 px | 0.17 | 1.01 | 147 |
| over the wet one | 45 % → 42 % | 76.8 px | 0.17 | 0.93 | 84 |
| long, no reload | 94 % → 90 % | 42.3 px | 0.17 | 0.96 | 565 | quarters: 0.18 → 0.18 → 0.17 → 0.14

Numbers say: light vs heavy: width 77.5 → 92.0 px, dark 0.13 → 0.13.

## 0.45 · Eraser
Watercolour 1.00 · 30 px · 25.2 s · over bands of wet oil paint and oil pastel in turn (it works on paint already there: look at what it does to the bands; covered counts the bands too)

![0.45 · Eraser](0-45-Eraser.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 24 % → 24 % | 69.2 px | 0.82 | 1.00 | 50 |
| heavy line | 23 % → 23 % | 67.4 px | 0.82 | 1.00 | 86 |
| pressure swell | 23 % → 23 % | 86.8 px | 0.82 | 1.00 | 46 |
| fast wave | 21 % → 21 % | 24.7 px | 0.81 | 1.00 | 181 |
| slow wave | 20 % → 20 % | 23.5 px | 0.82 | 1.00 | 378 |
| spiral | 20 % → 20 % | 13.5 px | 0.79 | 1.00 | 388 |
| loop | 21 % → 21 % | 27.8 px | 0.80 | 1.00 | 145 |
| tilted | 23 % → 23 % | 64.8 px | 0.81 | 1.00 | 79 |
| over the wet one | 22 % → 22 % | 0.0 px | 0.81 | 1.00 | 71 |
| long, no reload | 17 % → 17 % | 7.5 px | 0.79 | 1.00 | 387 | quarters: 0.13 → 0.16 → 0.13 → 0.17

Numbers say: light vs heavy: width 69.2 → 67.4 px, dark 0.82 → 0.82; pressure barely changes the width; the long stroke does not run out of paint.

## Lift wet paint
Watercolour 1.00 · 30 px · 24.6 s · over bands of wet oil paint and oil pastel in turn (it works on paint already there: look at what it does to the bands; covered counts the bands too)

![Lift wet paint](Lift-wet-paint.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 24 % → 24 % | 70.1 px | 0.82 | 1.00 | 41 |
| heavy line | 24 % → 24 % | 69.8 px | 0.82 | 1.00 | 54 |
| pressure swell | 24 % → 24 % | 89.6 px | 0.82 | 1.00 | 37 |
| fast wave | 24 % → 24 % | 27.7 px | 0.82 | 1.00 | 119 |
| slow wave | 24 % → 24 % | 27.7 px | 0.82 | 1.00 | 231 |
| spiral | 24 % → 24 % | 15.9 px | 0.82 | 1.00 | 216 |
| loop | 24 % → 24 % | 31.1 px | 0.82 | 1.00 | 165 |
| tilted | 24 % → 24 % | 66.8 px | 0.82 | 1.00 | 84 |
| over the wet one | 24 % → 24 % | 0.0 px | 0.82 | 1.00 | 82 |
| long, no reload | 24 % → 24 % | 10.7 px | 0.82 | 1.00 | 313 | quarters: 0.18 → 0.24 → 0.17 → 0.24

Numbers say: light vs heavy: width 70.1 → 69.8 px, dark 0.82 → 0.82; pressure barely changes the width; the long stroke does not run out of paint.

## Sgraffito
Watercolour 1.00 · 10 px · 24.2 s · over bands of wet oil paint and oil pastel in turn (it works on paint already there: look at what it does to the bands; covered counts the bands too)

![Sgraffito](Sgraffito.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 24 % → 24 % | 69.9 px | 0.81 | 1.00 | 14 |
| heavy line | 24 % → 24 % | 69.8 px | 0.82 | 1.00 | 10 |
| pressure swell | 24 % → 24 % | 89.6 px | 0.82 | 1.00 | 6 |
| fast wave | 24 % → 24 % | 27.7 px | 0.82 | 1.00 | 27 |
| slow wave | 24 % → 24 % | 27.7 px | 0.82 | 1.00 | 46 |
| spiral | 24 % → 24 % | 15.9 px | 0.82 | 1.00 | 68 |
| loop | 24 % → 24 % | 31.1 px | 0.82 | 1.00 | 25 |
| tilted | 24 % → 24 % | 66.9 px | 0.82 | 1.00 | 8 |
| over the wet one | 24 % → 24 % | 0.0 px | 0.82 | 1.00 | 11 |
| long, no reload | 24 % → 24 % | 10.6 px | 0.82 | 1.00 | 66 | quarters: 0.17 → 0.24 → 0.17 → 0.24

Numbers say: light vs heavy: width 69.9 → 69.8 px, dark 0.81 → 0.82; pressure barely changes the width; the long stroke does not run out of paint.

## Brush Artist · Refs · #01 Henry Ward peach cloud
Gouache 1.00 · 44 px · 36.9 s

![Brush Artist · Refs · #01 Henry Ward peach cloud](Brush-Artist-Refs-01-Henry-Ward-peach-cloud.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 5 % → 0 % | 13.4 px | 0.00 | 0.00 | 180 |
| heavy line | 8 % → 0 % | 22.6 px | 0.32 | 0.02 | 183 |
| pressure swell | 7 % → 3 % | 25.5 px | 0.33 | 0.42 | 128 |
| fast wave | 31 % → 3 % | 36.2 px | 0.27 | 0.09 | 479 |
| slow wave | 20 % → 2 % | 23.3 px | 0.32 | 0.11 | 774 |
| spiral | 33 % → 2 % | 21.9 px | 0.35 | 0.07 | 814 |
| loop | 17 % → 0 % | 22.6 px | 0.32 | 0.01 | 389 |
| tilted | 12 % → 11 % | 32.7 px | 0.25 | 0.97 | 253 |
| over the wet one | 17 % → 2 % | 13.5 px | 0.25 | 0.13 | 166 |
| long, no reload | 31 % → 3 % | 14.0 px | 0.32 | 0.08 | 1503 | quarters: 0.03 → 0.03 → 0.03 → 0.03

Numbers say: light vs heavy: width 13.4 → 22.6 px, dark 0.00 → 0.32; the long stroke does not run out of paint.

## Brush Artist · Refs · #02 Henry Ward cream strokes
Gouache 1.00 · 46 px · 38.7 s

![Brush Artist · Refs · #02 Henry Ward cream strokes](Brush-Artist-Refs-02-Henry-Ward-cream-strokes.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 5 % → 0 % | 14.3 px | 0.00 | 0.00 | 158 |
| heavy line | 8 % → 2 % | 24.5 px | 0.41 | 0.24 | 206 |
| pressure swell | 7 % → 3 % | 27.5 px | 0.41 | 0.38 | 137 |
| fast wave | 30 % → 4 % | 34.5 px | 0.36 | 0.15 | 544 |
| slow wave | 22 % → 5 % | 25.2 px | 0.39 | 0.21 | 887 |
| spiral | 43 % → 5 % | 28.5 px | 0.40 | 0.11 | 881 |
| loop | 19 % → 1 % | 25.0 px | 0.39 | 0.04 | 591 |
| tilted | 12 % → 12 % | 33.1 px | 0.34 | 0.98 | 256 |
| over the wet one | 17 % → 1 % | 14.6 px | 0.34 | 0.08 | 184 |
| long, no reload | 26 % → 4 % | 11.5 px | 0.41 | 0.17 | 1074 | quarters: 0.03 → 0.04 → 0.03 → 0.04

Numbers say: light vs heavy: width 14.3 → 24.5 px, dark 0.00 → 0.41; the long stroke does not run out of paint.

## Brush Artist · Refs · #03 Henry Ward navy contours
Impasto 1.00 · 22 px · 20.8 s

![Brush Artist · Refs · #03 Henry Ward navy contours](Brush-Artist-Refs-03-Henry-Ward-navy-contours.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 7 % → 6 % | 19.4 px | 0.72 | 0.90 | 96 |
| heavy line | 6 % → 6 % | 18.3 px | 0.71 | 0.92 | 93 |
| pressure swell | 5 % → 5 % | 20.1 px | 0.75 | 0.89 | 82 |
| fast wave | 16 % → 11 % | 18.3 px | 0.76 | 0.71 | 277 |
| slow wave | 18 % → 14 % | 20.5 px | 0.72 | 0.78 | 395 |
| spiral | 28 % → 13 % | 18.3 px | 0.68 | 0.47 | 466 |
| loop | 13 % → 11 % | 17.0 px | 0.71 | 0.83 | 225 |
| tilted | 7 % → 7 % | 20.7 px | 0.73 | 0.99 | 138 |
| over the wet one | 15 % → 13 % | 20.4 px | 0.73 | 0.88 | 113 |
| long, no reload | 32 % → 13 % | 14.4 px | 0.71 | 0.41 | 625 | quarters: 0.33 → 0.27 → 0.19 → 0.08

Numbers say: light vs heavy: width 19.4 → 18.3 px, dark 0.72 → 0.71; pressure barely changes the width.

## Brush Artist · Refs · #04 Henry Ward grey cloud
Gouache 1.00 · 50 px · 36.7 s

![Brush Artist · Refs · #04 Henry Ward grey cloud](Brush-Artist-Refs-04-Henry-Ward-grey-cloud.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 5 % → 0 % | 14.6 px | 0.00 | 0.00 | 244 |
| heavy line | 10 % → 2 % | 28.5 px | 0.31 | 0.24 | 225 |
| pressure swell | 6 % → 2 % | 24.3 px | 0.31 | 0.37 | 148 |
| fast wave | 32 % → 4 % | 37.5 px | 0.24 | 0.14 | 589 |
| slow wave | 23 % → 2 % | 27.1 px | 0.33 | 0.10 | 898 |
| spiral | 47 % → 3 % | 31.0 px | 0.37 | 0.06 | 937 |
| loop | 19 % → 0 % | 25.2 px | 0.00 | 0.00 | 442 |
| tilted | 12 % → 12 % | 33.6 px | 0.24 | 0.98 | 482 |
| over the wet one | 17 % → 3 % | 14.1 px | 0.24 | 0.17 | 272 |
| long, no reload | 22 % → 4 % | 9.9 px | 0.34 | 0.18 | 1168 | quarters: 0.03 → 0.04 → 0.04 → 0.04

Numbers say: light vs heavy: width 14.6 → 28.5 px, dark 0.00 → 0.31; the long stroke does not run out of paint.

## Brush Artist · Refs · #05 Henry Ward green in rust loops
Impasto 1.00 · 20 px · 17.3 s

![Brush Artist · Refs · #05 Henry Ward green in rust loops](Brush-Artist-Refs-05-Henry-Ward-green-in-rust-loops.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 6 % → 6 % | 18.5 px | 0.56 | 0.88 | 109 |
| heavy line | 8 % → 7 % | 22.1 px | 0.56 | 0.87 | 127 |
| pressure swell | 4 % → 4 % | 16.1 px | 0.58 | 0.93 | 71 |
| fast wave | 16 % → 10 % | 17.9 px | 0.56 | 0.67 | 275 |
| slow wave | 16 % → 12 % | 19.1 px | 0.56 | 0.74 | 364 |
| spiral | 24 % → 11 % | 16.1 px | 0.53 | 0.46 | 449 |
| loop | 15 % → 12 % | 19.7 px | 0.56 | 0.79 | 283 |
| tilted | 7 % → 7 % | 19.8 px | 0.58 | 0.99 | 135 |
| over the wet one | 14 % → 12 % | 18.1 px | 0.58 | 0.85 | 110 |
| long, no reload | 28 % → 12 % | 12.6 px | 0.55 | 0.41 | 635 | quarters: 0.23 → 0.17 → 0.11 → 0.04

Numbers say: light vs heavy: width 18.5 → 22.1 px, dark 0.56 → 0.56.

## Brush Artist · Refs · #06 Henry Ward scrubbed grey
Gouache 1.00 · 50 px · 36.3 s

![Brush Artist · Refs · #06 Henry Ward scrubbed grey](Brush-Artist-Refs-06-Henry-Ward-scrubbed-grey.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 5 % → 0 % | 14.6 px | 0.00 | 0.00 | 175 |
| heavy line | 10 % → 2 % | 28.5 px | 0.33 | 0.24 | 185 |
| pressure swell | 6 % → 2 % | 24.3 px | 0.33 | 0.37 | 161 |
| fast wave | 32 % → 4 % | 37.5 px | 0.25 | 0.14 | 566 |
| slow wave | 23 % → 2 % | 27.1 px | 0.34 | 0.10 | 957 |
| spiral | 47 % → 3 % | 31.0 px | 0.38 | 0.06 | 1427 |
| loop | 19 % → 0 % | 25.2 px | 0.00 | 0.00 | 408 |
| tilted | 12 % → 12 % | 33.6 px | 0.25 | 0.98 | 278 |
| over the wet one | 17 % → 3 % | 14.1 px | 0.25 | 0.17 | 179 |
| long, no reload | 22 % → 4 % | 9.9 px | 0.35 | 0.18 | 1131 | quarters: 0.03 → 0.04 → 0.04 → 0.04

Numbers say: light vs heavy: width 14.6 → 28.5 px, dark 0.00 → 0.33; the long stroke does not run out of paint.

## Brush Artist · Refs · #07 Henry Ward blue L + black zigzag
Impasto 1.00 · 34 px · 20.7 s

![Brush Artist · Refs · #07 Henry Ward blue L + black zigzag](Brush-Artist-Refs-07-Henry-Ward-blue-L-black-zigzag.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 10 % → 9 % | 30.2 px | 0.59 | 0.86 | 123 |
| heavy line | 11 % → 10 % | 30.8 px | 0.59 | 0.93 | 137 |
| pressure swell | 8 % → 8 % | 31.6 px | 0.59 | 0.92 | 103 |
| fast wave | 25 % → 19 % | 28.8 px | 0.60 | 0.77 | 374 |
| slow wave | 26 % → 20 % | 29.7 px | 0.57 | 0.76 | 573 |
| spiral | 44 % → 23 % | 29.1 px | 0.54 | 0.52 | 641 |
| loop | 24 % → 19 % | 30.4 px | 0.57 | 0.80 | 327 |
| tilted | 11 % → 11 % | 29.8 px | 0.61 | 1.00 | 268 |
| over the wet one | 22 % → 20 % | 32.0 px | 0.61 | 0.90 | 226 |
| long, no reload | 50 % → 23 % | 22.5 px | 0.57 | 0.46 | 1182 | quarters: 0.36 → 0.31 → 0.21 → 0.10

Numbers say: light vs heavy: width 30.2 → 30.8 px, dark 0.59 → 0.59; pressure barely changes the width.

## Brush Artist · Refs · #08 Henry Ward olive bands
Gouache 1.00 · 34 px · 30.9 s

![Brush Artist · Refs · #08 Henry Ward olive bands](Brush-Artist-Refs-08-Henry-Ward-olive-bands.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 4 % → 0 % | 11.7 px | 0.00 | 0.00 | 117 |
| heavy line | 9 % → 1 % | 24.9 px | 0.60 | 0.13 | 187 |
| pressure swell | 7 % → 2 % | 25.2 px | 0.61 | 0.29 | 137 |
| fast wave | 18 % → 3 % | 20.5 px | 0.60 | 0.16 | 400 |
| slow wave | 18 % → 2 % | 21.0 px | 0.62 | 0.09 | 598 |
| spiral | 26 % → 1 % | 17.4 px | 0.55 | 0.03 | 561 |
| loop | 13 % → 3 % | 17.5 px | 0.60 | 0.19 | 316 |
| tilted | 8 % → 8 % | 22.8 px | 0.63 | 0.96 | 170 |
| over the wet one | 16 % → 4 % | 22.1 px | 0.63 | 0.23 | 154 |
| long, no reload | 27 % → 3 % | 11.9 px | 0.54 | 0.12 | 942 | quarters: 0.25 → 0.15 → 0.11 → 0.08

Numbers say: light vs heavy: width 11.7 → 24.9 px, dark 0.00 → 0.60.

## Brush Artist · Refs · #09 Henry Ward white loops
Gouache 1.00 · 46 px · 38.9 s

![Brush Artist · Refs · #09 Henry Ward white loops](Brush-Artist-Refs-09-Henry-Ward-white-loops.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 5 % → 0 % | 14.3 px | 0.00 | 0.00 | 169 |
| heavy line | 8 % → 2 % | 24.5 px | 0.43 | 0.24 | 182 |
| pressure swell | 7 % → 3 % | 27.5 px | 0.43 | 0.38 | 137 |
| fast wave | 30 % → 4 % | 34.5 px | 0.38 | 0.15 | 551 |
| slow wave | 22 % → 5 % | 25.2 px | 0.40 | 0.21 | 897 |
| spiral | 43 % → 5 % | 28.5 px | 0.42 | 0.11 | 903 |
| loop | 19 % → 1 % | 25.0 px | 0.41 | 0.04 | 451 |
| tilted | 12 % → 12 % | 33.1 px | 0.37 | 0.98 | 345 |
| over the wet one | 17 % → 1 % | 14.6 px | 0.37 | 0.08 | 221 |
| long, no reload | 26 % → 4 % | 11.5 px | 0.42 | 0.17 | 1026 | quarters: 0.03 → 0.04 → 0.04 → 0.04

Numbers say: light vs heavy: width 14.3 → 24.5 px, dark 0.00 → 0.43; the long stroke does not run out of paint.

## Brush Artist · Refs · #10 Henry Ward maroon loops
Impasto 1.00 · 30 px · 19.9 s

![Brush Artist · Refs · #10 Henry Ward maroon loops](Brush-Artist-Refs-10-Henry-Ward-maroon-loops.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 10 % → 8 % | 27.9 px | 0.73 | 0.88 | 99 |
| heavy line | 11 % → 10 % | 32.1 px | 0.73 | 0.90 | 124 |
| pressure swell | 8 % → 7 % | 29.7 px | 0.74 | 0.91 | 94 |
| fast wave | 23 % → 17 % | 26.5 px | 0.76 | 0.76 | 304 |
| slow wave | 22 % → 19 % | 25.9 px | 0.72 | 0.85 | 501 |
| spiral | 37 % → 18 % | 24.2 px | 0.72 | 0.50 | 555 |
| loop | 17 % → 15 % | 22.1 px | 0.73 | 0.86 | 284 |
| tilted | 10 % → 10 % | 27.6 px | 0.73 | 1.00 | 141 |
| over the wet one | 19 % → 17 % | 26.8 px | 0.73 | 0.86 | 146 |
| long, no reload | 40 % → 17 % | 18.0 px | 0.71 | 0.43 | 831 | quarters: 0.38 → 0.33 → 0.27 → 0.18

Numbers say: light vs heavy: width 27.9 → 32.1 px, dark 0.73 → 0.73.

## Brush Artist · Refs · #11 Henry Ward purple spun balls
Impasto 1.00 · 36 px · 22.5 s

![Brush Artist · Refs · #11 Henry Ward purple spun balls](Brush-Artist-Refs-11-Henry-Ward-purple-spun-balls.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 11 % → 10 % | 31.5 px | 0.74 | 0.93 | 357 |
| heavy line | 11 % → 10 % | 30.5 px | 0.74 | 0.95 | 297 |
| pressure swell | 10 % → 9 % | 36.4 px | 0.75 | 0.92 | 192 |
| fast wave | 27 % → 21 % | 31.1 px | 0.74 | 0.78 | 671 |
| slow wave | 30 % → 24 % | 34.6 px | 0.73 | 0.82 | 648 |
| spiral | 40 % → 24 % | 26.5 px | 0.70 | 0.59 | 708 |
| loop | 24 % → 21 % | 30.7 px | 0.75 | 0.90 | 314 |
| tilted | 10 % → 10 % | 28.5 px | 0.73 | 1.00 | 188 |
| over the wet one | 22 % → 20 % | 33.9 px | 0.73 | 0.91 | 177 |
| long, no reload | 53 % → 25 % | 23.9 px | 0.74 | 0.46 | 1028 | quarters: 0.50 → 0.45 → 0.38 → 0.27

Numbers say: light vs heavy: width 31.5 → 30.5 px, dark 0.74 → 0.74; pressure barely changes the width.

## Brush Artist · Refs · #12 Henry Ward black-olive cage
Gouache 1.00 · 28 px · 28.0 s

![Brush Artist · Refs · #12 Henry Ward black-olive cage](Brush-Artist-Refs-12-Henry-Ward-black-olive-cage.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 4 % → 1 % | 11.9 px | 0.64 | 0.13 | 70 |
| heavy line | 7 % → 1 % | 20.9 px | 0.64 | 0.19 | 158 |
| pressure swell | 6 % → 2 % | 21.4 px | 0.64 | 0.36 | 120 |
| fast wave | 13 % → 2 % | 14.9 px | 0.66 | 0.12 | 321 |
| slow wave | 16 % → 2 % | 18.9 px | 0.64 | 0.12 | 577 |
| spiral | 19 % → 1 % | 12.5 px | 0.61 | 0.03 | 699 |
| loop | 13 % → 3 % | 17.5 px | 0.63 | 0.20 | 273 |
| tilted | 7 % → 7 % | 19.9 px | 0.66 | 0.94 | 179 |
| over the wet one | 14 % → 3 % | 18.1 px | 0.66 | 0.23 | 141 |
| long, no reload | 22 % → 3 % | 9.7 px | 0.57 | 0.14 | 713 | quarters: 0.22 → 0.13 → 0.07 → 0.03

Numbers say: light vs heavy: width 11.9 → 20.9 px, dark 0.64 → 0.64.

## Brush Artist · Refs · #13 Henry Ward blue streaky form
Gouache 1.00 · 50 px · 37.3 s

![Brush Artist · Refs · #13 Henry Ward blue streaky form](Brush-Artist-Refs-13-Henry-Ward-blue-streaky-form.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 5 % → 0 % | 14.6 px | 0.00 | 0.00 | 173 |
| heavy line | 10 % → 2 % | 28.5 px | 0.33 | 0.24 | 181 |
| pressure swell | 6 % → 2 % | 24.3 px | 0.33 | 0.37 | 144 |
| fast wave | 32 % → 4 % | 37.5 px | 0.25 | 0.14 | 580 |
| slow wave | 23 % → 2 % | 27.1 px | 0.34 | 0.10 | 909 |
| spiral | 47 % → 3 % | 31.0 px | 0.37 | 0.06 | 986 |
| loop | 19 % → 0 % | 25.2 px | 0.00 | 0.00 | 664 |
| tilted | 12 % → 12 % | 33.6 px | 0.25 | 0.98 | 319 |
| over the wet one | 17 % → 3 % | 14.1 px | 0.25 | 0.17 | 191 |
| long, no reload | 22 % → 4 % | 9.9 px | 0.35 | 0.18 | 1179 | quarters: 0.03 → 0.04 → 0.04 → 0.04

Numbers say: light vs heavy: width 14.6 → 28.5 px, dark 0.00 → 0.33; the long stroke does not run out of paint.

## Brush Artist · Refs · #14 Henry Ward olive totem
Impasto 1.00 · 48 px · 23.8 s

![Brush Artist · Refs · #14 Henry Ward olive totem](Brush-Artist-Refs-14-Henry-Ward-olive-totem.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 15 % → 14 % | 44.4 px | 0.31 | 0.91 | 189 |
| heavy line | 16 % → 15 % | 46.3 px | 0.31 | 0.95 | 171 |
| pressure swell | 12 % → 11 % | 44.0 px | 0.31 | 0.93 | 156 |
| fast wave | 36 % → 28 % | 41.7 px | 0.36 | 0.78 | 778 |
| slow wave | 37 % → 32 % | 42.3 px | 0.30 | 0.87 | 1035 |
| spiral | 59 % → 35 % | 38.7 px | 0.28 | 0.59 | 953 |
| loop | 30 % → 27 % | 39.1 px | 0.29 | 0.89 | 433 |
| tilted | 13 % → 13 % | 36.4 px | 0.33 | 1.00 | 239 |
| over the wet one | 28 % → 25 % | 40.5 px | 0.33 | 0.92 | 226 |
| long, no reload | 61 % → 31 % | 27.3 px | 0.27 | 0.52 | 1229 | quarters: 0.20 → 0.15 → 0.09 → 0.04

Numbers say: light vs heavy: width 44.4 → 46.3 px, dark 0.31 → 0.31; pressure barely changes the width.

## Brush Artist · Refs · #15 Ultramarine brush script
Ink 1.00 · 4 px · 27.6 s

![Brush Artist · Refs · #15 Ultramarine brush script](Brush-Artist-Refs-15-Ultramarine-brush-script.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 1 % → 3 % | 2.1 px | 0.55 | 3.99 | 38 |
| heavy line | 5 % → 5 % | 15.6 px | 0.62 | 1.00 | 63 |
| pressure swell | 3 % → 4 % | 11.0 px | 0.62 | 1.21 | 41 |
| fast wave | 9 % → 7 % | 10.2 px | 0.54 | 0.81 | 168 |
| slow wave | 8 % → 7 % | 8.8 px | 0.53 | 0.89 | 161 |
| spiral | 11 % → 8 % | 7.3 px | 0.53 | 0.68 | 200 |
| loop | 7 % → 7 % | 9.4 px | 0.54 | 0.96 | 106 |
| tilted | 3 % → 3 % | 7.4 px | 0.64 | 1.04 | 52 |
| over the wet one | 7 % → 7 % | 10.7 px | 0.64 | 1.08 | 50 |
| long, no reload | 16 % → 7 % | 7.1 px | 0.51 | 0.47 | 277 | quarters: 0.14 → 0.04 → 0.01 → 0.00

Numbers say: light vs heavy: width 2.1 → 15.6 px, dark 0.55 → 0.62; wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #18 Blue oil-stick scribbles
Pastel 1.00 · 10 px · 13.5 s

![Brush Artist · Refs · #18 Blue oil-stick scribbles](Brush-Artist-Refs-18-Blue-oil-stick-scribbles.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 1 % → 1 % | 2.9 px | 0.53 | 1.00 | 27 |
| heavy line | 2 % → 2 % | 6.0 px | 0.53 | 1.00 | 35 |
| pressure swell | 1 % → 1 % | 5.5 px | 0.52 | 1.00 | 19 |
| fast wave | 5 % → 5 % | 5.3 px | 0.53 | 1.00 | 72 |
| slow wave | 4 % → 4 % | 5.2 px | 0.53 | 1.00 | 78 |
| spiral | 7 % → 7 % | 4.4 px | 0.52 | 1.00 | 140 |
| loop | 4 % → 4 % | 4.6 px | 0.52 | 1.00 | 118 |
| tilted | 2 % → 2 % | 4.4 px | 0.53 | 1.00 | 57 |
| over the wet one | 3 % → 3 % | 4.8 px | 0.53 | 1.00 | 42 |
| long, no reload | 9 % → 9 % | 4.2 px | 0.52 | 1.00 | 262 | quarters: 0.05 → 0.05 → 0.06 → 0.06

Numbers say: light vs heavy: width 2.9 → 6.0 px, dark 0.53 → 0.53; the long stroke does not run out of paint.

## Brush Artist · Refs · #20 Orange-red crayon scribble
Pastel 1.00 · 14 px · 13.5 s

![Brush Artist · Refs · #20 Orange-red crayon scribble](Brush-Artist-Refs-20-Orange-red-crayon-scribble.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 1 % → 1 % | 3.8 px | 0.53 | 1.00 | 25 |
| heavy line | 3 % → 3 % | 8.0 px | 0.53 | 1.00 | 34 |
| pressure swell | 2 % → 2 % | 7.6 px | 0.55 | 1.00 | 20 |
| fast wave | 6 % → 6 % | 7.3 px | 0.56 | 1.00 | 89 |
| slow wave | 6 % → 6 % | 6.9 px | 0.53 | 1.00 | 98 |
| spiral | 9 % → 9 % | 6.0 px | 0.54 | 1.00 | 152 |
| loop | 5 % → 5 % | 6.1 px | 0.54 | 1.00 | 74 |
| tilted | 2 % → 2 % | 5.6 px | 0.55 | 1.00 | 43 |
| over the wet one | 4 % → 4 % | 6.2 px | 0.55 | 1.00 | 35 |
| long, no reload | 12 % → 12 % | 5.4 px | 0.53 | 1.00 | 245 | quarters: 0.07 → 0.07 → 0.07 → 0.07

Numbers say: light vs heavy: width 3.8 → 8.0 px, dark 0.53 → 0.53; the long stroke does not run out of paint.

## Brush Artist · Refs · #21 Gritty black contours
Gouache 1.00 · 12 px · 28.9 s

![Brush Artist · Refs · #21 Gritty black contours](Brush-Artist-Refs-21-Gritty-black-contours.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 2 % → 0 % | 5.0 px | 0.00 | 0.00 | 90 |
| heavy line | 2 % → 0 % | 6.7 px | 0.00 | 0.00 | 142 |
| pressure swell | 2 % → 0 % | 6.7 px | 0.00 | 0.00 | 100 |
| fast wave | 4 % → 0 % | 4.2 px | 0.81 | 0.03 | 466 |
| slow wave | 4 % → 0 % | 5.2 px | 0.80 | 0.08 | 335 |
| spiral | 6 % → 0 % | 4.2 px | 0.76 | 0.07 | 570 |
| loop | 4 % → 1 % | 5.4 px | 0.80 | 0.16 | 302 |
| tilted | 3 % → 2 % | 7.8 px | 0.78 | 0.88 | 232 |
| over the wet one | 4 % → 0 % | 4.4 px | 0.78 | 0.03 | 291 |
| long, no reload | 6 % → 0 % | 2.6 px | 0.77 | 0.03 | 1364 | quarters: 0.09 → 0.04 → 0.03 → 0.03

Numbers say: light vs heavy: width 5.0 → 6.7 px, dark 0.00 → 0.00.

## Brush Artist · Refs · #22 Bold black brush poster
Ink 1.00 · 20 px · 38.9 s

![Brush Artist · Refs · #22 Bold black brush poster](Brush-Artist-Refs-22-Bold-black-brush-poster.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 4 % → 5 % | 10.3 px | 0.79 | 1.52 | 59 |
| heavy line | 15 % → 14 % | 42.6 px | 0.88 | 0.99 | 123 |
| pressure swell | 9 % → 9 % | 33.6 px | 0.87 | 1.03 | 81 |
| fast wave | 28 % → 27 % | 32.3 px | 0.88 | 0.98 | 239 |
| slow wave | 23 % → 23 % | 27.0 px | 0.87 | 0.98 | 294 |
| spiral | 35 % → 32 % | 23.0 px | 0.87 | 0.92 | 598 |
| loop | 22 % → 22 % | 28.2 px | 0.88 | 1.00 | 348 |
| tilted | 9 % → 9 % | 24.2 px | 0.88 | 1.00 | 216 |
| over the wet one | 20 % → 20 % | 30.8 px | 0.88 | 1.00 | 132 |
| long, no reload | 48 % → 38 % | 21.3 px | 0.85 | 0.79 | 506 | quarters: 0.56 → 0.45 → 0.35 → 0.26

Numbers say: light vs heavy: width 10.3 → 42.6 px, dark 0.79 → 0.88; wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #23 Dry white on orange + black line
Gouache 1.00 · 50 px · 35.9 s

![Brush Artist · Refs · #23 Dry white on orange + black line](Brush-Artist-Refs-23-Dry-white-on-orange-black-line.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 7 % → 0 % | 20.0 px | 0.40 | 0.01 | 147 |
| heavy line | 13 % → 2 % | 38.0 px | 0.41 | 0.16 | 543 |
| pressure swell | 9 % → 1 % | 33.4 px | 0.39 | 0.11 | 469 |
| fast wave | 23 % → 1 % | 26.8 px | 0.39 | 0.04 | 958 |
| slow wave | 27 % → 2 % | 31.1 px | 0.40 | 0.09 | 835 |
| spiral | 34 % → 1 % | 22.2 px | 0.39 | 0.03 | 729 |
| loop | 23 % → 2 % | 29.4 px | 0.39 | 0.09 | 407 |
| tilted | 11 % → 10 % | 30.1 px | 0.38 | 0.94 | 225 |
| over the wet one | 21 % → 3 % | 27.8 px | 0.38 | 0.15 | 185 |
| long, no reload | 38 % → 5 % | 17.2 px | 0.40 | 0.12 | 1276 | quarters: 0.02 → 0.03 → 0.04 → 0.03

Numbers say: light vs heavy: width 20.0 → 38.0 px, dark 0.40 → 0.41; the long stroke does not run out of paint.

## Brush Artist · Refs · #24 Picasso flat oil
Oil 0.89 · Oil glaze 0.11 · 34 px · 23.3 s

![Brush Artist · Refs · #24 Picasso flat oil](Brush-Artist-Refs-24-Picasso-flat-oil.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 10 % → 10 % | 28.8 px | 0.39 | 1.00 | 219 |
| heavy line | 11 % → 11 % | 32.5 px | 0.39 | 1.00 | 170 |
| pressure swell | 8 % → 8 % | 31.7 px | 0.38 | 1.00 | 125 |
| fast wave | 30 % → 30 % | 35.2 px | 0.39 | 1.00 | 536 |
| slow wave | 28 % → 28 % | 32.8 px | 0.38 | 1.00 | 824 |
| spiral | 42 % → 42 % | 27.8 px | 0.38 | 1.00 | 813 |
| loop | 22 % → 22 % | 28.8 px | 0.40 | 1.00 | 470 |
| tilted | 11 % → 11 % | 31.3 px | 0.41 | 1.00 | 315 |
| over the wet one | 20 % → 20 % | 25.3 px | 0.41 | 1.00 | 217 |
| long, no reload | 58 % → 58 % | 26.0 px | 0.32 | 1.00 | 1331 | quarters: 0.23 → 0.22 → 0.19 → 0.17

Numbers say: light vs heavy: width 28.8 → 32.5 px, dark 0.39 → 0.39.

## Brush Artist · Refs · #25 Yellow heavy flat stroke
Impasto 1.00 · 110 px · 57.1 s

![Brush Artist · Refs · #25 Yellow heavy flat stroke](Brush-Artist-Refs-25-Yellow-heavy-flat-stroke.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 35 % → 35 % | 101.0 px | 0.31 | 1.00 | 897 |
| heavy line | 36 % → 35 % | 104.1 px | 0.31 | 0.97 | 656 |
| pressure swell | 28 % → 29 % | 104.0 px | 0.28 | 1.05 | 542 |
| fast wave | 72 % → 75 % | 82.8 px | 0.25 | 1.04 | 2076 |
| slow wave | 72 % → 71 % | 83.7 px | 0.30 | 0.98 | 3242 |
| spiral | 86 % → 81 % | 56.5 px | 0.30 | 0.94 | 4114 |
| loop | 64 % → 63 % | 82.7 px | 0.31 | 0.99 | 1573 |
| tilted | 25 % → 25 % | 70.3 px | 0.28 | 1.00 | 1043 |
| over the wet one | 55 % → 53 % | 83.3 px | 0.28 | 0.97 | 852 |
| long, no reload | 98 % → 96 % | 43.9 px | 0.31 | 0.98 | 5865 | quarters: 0.00 → 0.00 → 0.00 → 0.00

Numbers say: light vs heavy: width 101.0 → 104.1 px, dark 0.31 → 0.31; pressure barely changes the width; the long stroke does not run out of paint.

## Brush Artist · Refs · #27 Orange impasto swatch
Impasto 1.00 · 60 px · 34.1 s

![Brush Artist · Refs · #27 Orange impasto swatch](Brush-Artist-Refs-27-Orange-impasto-swatch.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 18 % → 18 % | 52.9 px | 0.34 | 0.97 | 312 |
| heavy line | 21 % → 20 % | 60.0 px | 0.34 | 0.95 | 313 |
| pressure swell | 15 % → 15 % | 57.8 px | 0.36 | 0.97 | 261 |
| fast wave | 48 % → 46 % | 55.2 px | 0.37 | 0.97 | 948 |
| slow wave | 46 % → 45 % | 53.6 px | 0.33 | 0.97 | 1430 |
| spiral | 68 % → 61 % | 45.1 px | 0.34 | 0.89 | 1520 |
| loop | 40 % → 39 % | 51.8 px | 0.33 | 0.97 | 738 |
| tilted | 16 % → 16 % | 43.7 px | 0.35 | 1.00 | 684 |
| over the wet one | 34 % → 32 % | 50.0 px | 0.35 | 0.97 | 578 |
| long, no reload | 84 % → 76 % | 37.8 px | 0.32 | 0.90 | 1946 | quarters: 0.30 → 0.29 → 0.28 → 0.25

Numbers say: light vs heavy: width 52.9 → 60.0 px, dark 0.34 → 0.34.

## Brush Artist · Refs · #28 Miles Davis black lines
Ink 1.00 · 22 px · 41.6 s

![Brush Artist · Refs · #28 Miles Davis black lines](Brush-Artist-Refs-28-Miles-Davis-black-lines.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 4 % → 6 % | 12.3 px | 0.80 | 1.40 | 66 |
| heavy line | 16 % → 16 % | 45.9 px | 0.88 | 0.99 | 178 |
| pressure swell | 10 % → 10 % | 36.7 px | 0.87 | 1.03 | 123 |
| fast wave | 29 % → 29 % | 33.8 px | 0.88 | 0.99 | 222 |
| slow wave | 27 % → 26 % | 30.7 px | 0.88 | 0.99 | 338 |
| spiral | 39 % → 36 % | 25.4 px | 0.87 | 0.93 | 382 |
| loop | 24 % → 24 % | 31.0 px | 0.88 | 1.00 | 168 |
| tilted | 9 % → 9 % | 26.0 px | 0.88 | 1.01 | 133 |
| over the wet one | 21 % → 21 % | 32.9 px | 0.88 | 1.00 | 126 |
| long, no reload | 53 % → 45 % | 23.9 px | 0.85 | 0.83 | 616 | quarters: 0.61 → 0.53 → 0.41 → 0.31

Numbers say: light vs heavy: width 12.3 → 45.9 px, dark 0.80 → 0.88.

## Brush Artist · Refs · #29 Shrigley magenta asterisk
Watercolour 1.00 · 70 px · 42.7 s

![Brush Artist · Refs · #29 Shrigley magenta asterisk](Brush-Artist-Refs-29-Shrigley-magenta-asterisk.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 10 % → 13 % | 28.0 px | 0.61 | 1.39 | 100 |
| heavy line | 17 % → 18 % | 50.3 px | 0.61 | 1.04 | 304 |
| pressure swell | 11 % → 13 % | 41.1 px | 0.62 | 1.14 | 186 |
| fast wave | 38 % → 38 % | 43.8 px | 0.60 | 1.01 | 551 |
| slow wave | 35 % → 39 % | 41.0 px | 0.62 | 1.11 | 771 |
| spiral | 61 % → 61 % | 40.0 px | 0.60 | 1.01 | 530 |
| loop | 31 % → 32 % | 40.2 px | 0.61 | 1.03 | 323 |
| tilted | 18 % → 18 % | 49.0 px | 0.61 | 1.00 | 284 |
| over the wet one | 31 % → 34 % | 38.5 px | 0.61 | 1.08 | 174 |
| long, no reload | 75 % → 76 % | 33.6 px | 0.60 | 1.01 | 1171 | quarters: 0.53 → 0.50 → 0.48 → 0.45

Numbers say: light vs heavy: width 28.0 → 50.3 px, dark 0.61 → 0.61; the long stroke does not run out of paint.

## Brush Artist · Refs · #30 Red gouache face patch
Gouache 1.00 · 60 px · 49.0 s

![Brush Artist · Refs · #30 Red gouache face patch](Brush-Artist-Refs-30-Red-gouache-face-patch.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 16 % → 14 % | 45.5 px | 0.49 | 0.87 | 203 |
| heavy line | 25 % → 19 % | 71.4 px | 0.49 | 0.78 | 338 |
| pressure swell | 20 % → 17 % | 74.8 px | 0.50 | 0.84 | 206 |
| fast wave | 48 % → 28 % | 55.1 px | 0.51 | 0.58 | 694 |
| slow wave | 50 % → 31 % | 57.3 px | 0.48 | 0.62 | 992 |
| spiral | 59 % → 30 % | 39.0 px | 0.48 | 0.50 | 1576 |
| loop | 40 % → 28 % | 51.4 px | 0.48 | 0.71 | 598 |
| tilted | 17 % → 17 % | 46.7 px | 0.50 | 1.00 | 364 |
| over the wet one | 37 % → 32 % | 55.9 px | 0.50 | 0.87 | 244 |
| long, no reload | 66 % → 28 % | 29.6 px | 0.46 | 0.42 | 1312 | quarters: 0.40 → 0.36 → 0.31 → 0.26

Numbers say: light vs heavy: width 45.5 → 71.4 px, dark 0.49 → 0.49.

## Brush Artist · Refs · #31 Warhol blotted line
Ink 1.00 · 6 px · 24.2 s

![Brush Artist · Refs · #31 Warhol blotted line](Brush-Artist-Refs-31-Warhol-blotted-line.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 1 % → 4 % | 3.0 px | 0.72 | 3.49 | 37 |
| heavy line | 7 % → 7 % | 19.5 px | 0.84 | 0.98 | 90 |
| pressure swell | 4 % → 4 % | 14.2 px | 0.82 | 1.18 | 38 |
| fast wave | 12 % → 9 % | 13.6 px | 0.81 | 0.73 | 152 |
| slow wave | 11 % → 9 % | 12.3 px | 0.80 | 0.80 | 161 |
| spiral | 15 % → 9 % | 10.0 px | 0.79 | 0.58 | 305 |
| loop | 10 % → 9 % | 12.6 px | 0.80 | 0.94 | 172 |
| tilted | 4 % → 4 % | 11.0 px | 0.83 | 1.03 | 99 |
| over the wet one | 9 % → 9 % | 14.0 px | 0.83 | 1.05 | 82 |
| long, no reload | 21 % → 10 % | 9.5 px | 0.78 | 0.45 | 381 | quarters: 0.25 → 0.13 → 0.05 → 0.01

Numbers say: light vs heavy: width 3.0 → 19.5 px, dark 0.72 → 0.84; wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #32 Thick orange swipes
Impasto 1.00 · 90 px · 41.2 s

![Brush Artist · Refs · #32 Thick orange swipes](Brush-Artist-Refs-32-Thick-orange-swipes.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 29 % → 28 % | 83.5 px | 0.37 | 0.99 | 363 |
| heavy line | 30 % → 29 % | 86.8 px | 0.37 | 0.97 | 343 |
| pressure swell | 23 % → 23 % | 84.8 px | 0.38 | 1.01 | 281 |
| fast wave | 64 % → 65 % | 74.2 px | 0.39 | 1.02 | 1165 |
| slow wave | 64 % → 62 % | 73.9 px | 0.37 | 0.97 | 1717 |
| spiral | 80 % → 75 % | 52.6 px | 0.35 | 0.94 | 2424 |
| loop | 56 % → 55 % | 73.0 px | 0.36 | 0.97 | 1122 |
| tilted | 21 % → 21 % | 58.8 px | 0.38 | 1.00 | 724 |
| over the wet one | 46 % → 45 % | 70.6 px | 0.38 | 0.96 | 515 |
| long, no reload | 95 % → 92 % | 42.8 px | 0.36 | 0.97 | 3219 | quarters: 0.35 → 0.35 → 0.35 → 0.34

Numbers say: light vs heavy: width 83.5 → 86.8 px, dark 0.37 → 0.37; pressure barely changes the width; the long stroke does not run out of paint.

## Brush Artist · Refs · #33 Red wet-in-wet band
Watercolour 1.00 · 80 px · 62.8 s

![Brush Artist · Refs · #33 Red wet-in-wet band](Brush-Artist-Refs-33-Red-wet-in-wet-band.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 24 % → 42 % | 69.3 px | 0.54 | 1.75 | 140 |
| heavy line | 33 % → 48 % | 96.9 px | 0.55 | 1.45 | 288 |
| pressure swell | 19 % → 30 % | 72.1 px | 0.57 | 1.56 | 161 |
| fast wave | 65 % → 79 % | 75.5 px | 0.60 | 1.21 | 511 |
| slow wave | 61 % → 78 % | 70.5 px | 0.63 | 1.28 | 1273 |
| spiral | 77 % → 89 % | 50.8 px | 0.64 | 1.15 | 992 |
| loop | 54 % → 67 % | 70.5 px | 0.62 | 1.23 | 581 |
| tilted | 28 % → 30 % | 78.0 px | 0.58 | 1.09 | 359 |
| over the wet one | 55 % → 79 % | 76.7 px | 0.58 | 1.43 | 197 |
| long, no reload | 96 % → 99 % | 42.9 px | 0.66 | 1.04 | 1471 | quarters: 0.68 → 0.68 → 0.68 → 0.64

Numbers say: light vs heavy: width 69.3 → 96.9 px, dark 0.54 → 0.55; the long stroke does not run out of paint; wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #34 Magenta oil patches
Oil 0.89 · Oil glaze 0.11 · 60 px · 24.2 s

![Brush Artist · Refs · #34 Magenta oil patches](Brush-Artist-Refs-34-Magenta-oil-patches.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 18 % → 18 % | 51.4 px | 0.61 | 1.00 | 217 |
| heavy line | 19 % → 19 % | 55.1 px | 0.61 | 1.00 | 246 |
| pressure swell | 15 % → 15 % | 54.6 px | 0.61 | 1.01 | 248 |
| fast wave | 44 % → 45 % | 51.1 px | 0.61 | 1.02 | 663 |
| slow wave | 45 % → 45 % | 52.4 px | 0.61 | 1.00 | 1076 |
| spiral | 68 % → 68 % | 44.9 px | 0.58 | 1.00 | 1382 |
| loop | 42 % → 42 % | 54.2 px | 0.61 | 1.00 | 915 |
| tilted | 17 % → 17 % | 46.3 px | 0.61 | 1.00 | 689 |
| over the wet one | 34 % → 34 % | 48.4 px | 0.61 | 1.00 | 562 |
| long, no reload | 83 % → 83 % | 37.1 px | 0.59 | 1.00 | 2820 | quarters: 0.54 → 0.54 → 0.53 → 0.47

Numbers say: light vs heavy: width 51.4 → 55.1 px, dark 0.61 → 0.61; pressure barely changes the width; the long stroke does not run out of paint.

## Brush Artist · Refs · #35 Red band with runs
Watercolour 1.00 · 70 px · 58.2 s

![Brush Artist · Refs · #35 Red band with runs](Brush-Artist-Refs-35-Red-band-with-runs.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 40 % → 45 % | 115.3 px | 0.42 | 1.14 | 152 |
| heavy line | 45 % → 50 % | 132.0 px | 0.42 | 1.09 | 232 |
| pressure swell | 20 % → 28 % | 76.7 px | 0.48 | 1.37 | 187 |
| fast wave | 66 % → 76 % | 76.8 px | 0.49 | 1.14 | 533 |
| slow wave | 65 % → 76 % | 75.6 px | 0.52 | 1.16 | 1287 |
| spiral | 86 % → 94 % | 56.9 px | 0.53 | 1.09 | 931 |
| loop | 79 % → 88 % | 102.7 px | 0.49 | 1.11 | 501 |
| tilted | 50 % → 51 % | 139.1 px | 0.47 | 1.02 | 300 |
| over the wet one | 78 % → 84 % | 77.5 px | 0.47 | 1.09 | 221 |
| long, no reload | 96 % → 100 % | 43.2 px | 0.58 | 1.04 | 1827 | quarters: 0.59 → 0.60 → 0.59 → 0.56

Numbers say: light vs heavy: width 115.3 → 132.0 px, dark 0.42 → 0.42; the long stroke does not run out of paint.

## Brush Artist · Refs · #36 Magenta letters flat brush
Gouache 1.00 · 36 px · 38.8 s

![Brush Artist · Refs · #36 Magenta letters flat brush](Brush-Artist-Refs-36-Magenta-letters-flat-brush.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 10 % → 10 % | 29.6 px | 0.45 | 0.94 | 124 |
| heavy line | 16 % → 13 % | 47.5 px | 0.45 | 0.78 | 154 |
| pressure swell | 13 % → 11 % | 48.4 px | 0.47 | 0.85 | 114 |
| fast wave | 34 % → 16 % | 39.3 px | 0.47 | 0.48 | 333 |
| slow wave | 35 % → 20 % | 40.5 px | 0.45 | 0.57 | 439 |
| spiral | 46 % → 19 % | 30.6 px | 0.44 | 0.41 | 580 |
| loop | 27 % → 18 % | 35.0 px | 0.45 | 0.67 | 311 |
| tilted | 12 % → 12 % | 32.8 px | 0.47 | 1.00 | 185 |
| over the wet one | 26 % → 22 % | 38.5 px | 0.47 | 0.88 | 121 |
| long, no reload | 49 % → 19 % | 22.0 px | 0.44 | 0.39 | 957 | quarters: 0.30 → 0.27 → 0.22 → 0.18

Numbers say: light vs heavy: width 29.6 → 47.5 px, dark 0.45 → 0.45.

## Brush Artist · Refs · #37 Oil still life dabs
Oil 0.89 · Oil glaze 0.11 · 40 px · 17.9 s

![Brush Artist · Refs · #37 Oil still life dabs](Brush-Artist-Refs-37-Oil-still-life-dabs.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 11 % → 11 % | 32.1 px | 0.36 | 1.00 | 167 |
| heavy line | 12 % → 12 % | 36.1 px | 0.39 | 1.00 | 160 |
| pressure swell | 10 % → 10 % | 39.3 px | 0.40 | 1.00 | 119 |
| fast wave | 30 % → 30 % | 35.0 px | 0.39 | 1.00 | 449 |
| slow wave | 35 % → 35 % | 40.6 px | 0.37 | 1.00 | 751 |
| spiral | 52 % → 52 % | 34.4 px | 0.38 | 1.00 | 803 |
| loop | 29 % → 29 % | 36.9 px | 0.39 | 1.00 | 607 |
| tilted | 12 % → 12 % | 34.7 px | 0.41 | 1.00 | 286 |
| over the wet one | 23 % → 23 % | 30.6 px | 0.41 | 1.00 | 169 |
| long, no reload | 59 % → 59 % | 26.6 px | 0.31 | 1.00 | 1259 | quarters: 0.23 → 0.22 → 0.20 → 0.17

Numbers say: light vs heavy: width 32.1 → 36.1 px, dark 0.36 → 0.39.

## Brush Artist · Refs · #38 Sanguine drawing
Pastel 1.00 · 6 px · 9.4 s

![Brush Artist · Refs · #38 Sanguine drawing](Brush-Artist-Refs-38-Sanguine-drawing.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 1 % → 1 % | 2.1 px | 0.61 | 1.00 | 30 |
| heavy line | 1 % → 1 % | 3.9 px | 0.61 | 1.00 | 21 |
| pressure swell | 1 % → 1 % | 3.8 px | 0.61 | 1.00 | 14 |
| fast wave | 3 % → 3 % | 3.4 px | 0.61 | 1.00 | 43 |
| slow wave | 3 % → 3 % | 3.4 px | 0.61 | 1.00 | 43 |
| spiral | 4 % → 4 % | 2.8 px | 0.61 | 1.00 | 72 |
| loop | 2 % → 2 % | 3.1 px | 0.61 | 1.00 | 39 |
| tilted | 1 % → 1 % | 3.4 px | 0.61 | 1.00 | 32 |
| over the wet one | 2 % → 2 % | 2.9 px | 0.61 | 1.00 | 25 |
| long, no reload | 6 % → 6 % | 2.7 px | 0.61 | 1.00 | 131 | quarters: 0.04 → 0.04 → 0.04 → 0.04

Numbers say: light vs heavy: width 2.1 → 3.9 px, dark 0.61 → 0.61; the long stroke does not run out of paint.

## Brush Artist · Refs · #39 Very thick impasto
Impasto 1.00 · 60 px · 25.0 s

![Brush Artist · Refs · #39 Very thick impasto](Brush-Artist-Refs-39-Very-thick-impasto.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 18 % → 18 % | 53.1 px | 0.61 | 0.97 | 249 |
| heavy line | 21 % → 20 % | 60.0 px | 0.62 | 0.96 | 250 |
| pressure swell | 15 % → 15 % | 58.1 px | 0.62 | 0.97 | 173 |
| fast wave | 48 % → 47 % | 55.3 px | 0.63 | 0.98 | 652 |
| slow wave | 47 % → 45 % | 53.9 px | 0.61 | 0.97 | 904 |
| spiral | 69 % → 63 % | 45.3 px | 0.61 | 0.92 | 937 |
| loop | 40 % → 39 % | 52.1 px | 0.61 | 0.97 | 460 |
| tilted | 16 % → 16 % | 43.8 px | 0.62 | 1.00 | 285 |
| over the wet one | 34 % → 33 % | 50.1 px | 0.62 | 0.97 | 226 |
| long, no reload | 85 % → 79 % | 38.0 px | 0.60 | 0.93 | 1775 | quarters: 0.56 → 0.55 → 0.54 → 0.51

Numbers say: light vs heavy: width 53.1 → 60.0 px, dark 0.61 → 0.62; the long stroke does not run out of paint.

## Brush Artist · Refs · #40 Watercolour blooms
Watercolour 1.00 · 90 px · 53.2 s

![Brush Artist · Refs · #40 Watercolour blooms](Brush-Artist-Refs-40-Watercolour-blooms.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 27 % → 47 % | 78.4 px | 0.08 | 1.72 | 156 |
| heavy line | 38 % → 51 % | 110.0 px | 0.09 | 1.36 | 320 |
| pressure swell | 24 % → 39 % | 91.8 px | 0.09 | 1.61 | 202 |
| fast wave | 68 % → 82 % | 78.3 px | 0.11 | 1.21 | 579 |
| slow wave | 68 % → 81 % | 79.1 px | 0.15 | 1.18 | 1049 |
| spiral | 81 % → 92 % | 53.5 px | 0.14 | 1.14 | 981 |
| loop | 58 % → 72 % | 75.3 px | 0.13 | 1.24 | 895 |
| tilted | 34 % → 36 % | 94.8 px | 0.11 | 1.07 | 432 |
| over the wet one | 62 % → 81 % | 78.2 px | 0.11 | 1.31 | 332 |
| long, no reload | 97 % → 100 % | 43.6 px | 0.17 | 1.03 | 1574 | quarters: 0.21 → 0.20 → 0.17 → 0.13

Numbers say: light vs heavy: width 78.4 → 110.0 px, dark 0.08 → 0.09; wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #41 Coloured pencil hatching
Pastel 1.00 · 4 px · 11.4 s

![Brush Artist · Refs · #41 Coloured pencil hatching](Brush-Artist-Refs-41-Coloured-pencil-hatching.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 1 % → 1 % | 1.6 px | 0.43 | 1.00 | 14 |
| heavy line | 1 % → 1 % | 2.9 px | 0.43 | 1.00 | 19 |
| pressure swell | 1 % → 1 % | 2.8 px | 0.43 | 1.00 | 9 |
| fast wave | 2 % → 2 % | 2.5 px | 0.43 | 1.00 | 30 |
| slow wave | 2 % → 2 % | 2.5 px | 0.43 | 1.00 | 63 |
| spiral | 3 % → 3 % | 2.1 px | 0.43 | 1.00 | 91 |
| loop | 2 % → 2 % | 2.3 px | 0.43 | 1.00 | 88 |
| tilted | 1 % → 1 % | 3.0 px | 0.43 | 1.00 | 33 |
| over the wet one | 2 % → 2 % | 2.3 px | 0.43 | 1.00 | 28 |
| long, no reload | 5 % → 5 % | 2.0 px | 0.42 | 1.00 | 161 | quarters: 0.02 → 0.02 → 0.02 → 0.02

Numbers say: light vs heavy: width 1.6 → 2.9 px, dark 0.43 → 0.43; the long stroke does not run out of paint.

## Brush Artist · Refs · #42 Oil pastel shaggy
Pastel 1.00 · 18 px · 12.3 s

![Brush Artist · Refs · #42 Oil pastel shaggy](Brush-Artist-Refs-42-Oil-pastel-shaggy.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 2 % → 2 % | 4.7 px | 0.36 | 1.00 | 35 |
| heavy line | 3 % → 3 % | 10.0 px | 0.36 | 1.00 | 27 |
| pressure swell | 2 % → 2 % | 9.3 px | 0.34 | 1.00 | 20 |
| fast wave | 8 % → 8 % | 9.2 px | 0.32 | 1.00 | 80 |
| slow wave | 7 % → 7 % | 8.6 px | 0.37 | 1.00 | 122 |
| spiral | 11 % → 11 % | 7.5 px | 0.36 | 1.00 | 126 |
| loop | 6 % → 6 % | 7.8 px | 0.35 | 1.00 | 63 |
| tilted | 2 % → 2 % | 6.5 px | 0.33 | 1.00 | 36 |
| over the wet one | 5 % → 5 % | 7.6 px | 0.33 | 1.00 | 33 |
| long, no reload | 15 % → 15 % | 6.5 px | 0.37 | 1.00 | 183 | quarters: 0.00 → 0.00 → 0.00 → 0.00

Numbers say: light vs heavy: width 4.7 → 10.0 px, dark 0.36 → 0.36; the long stroke does not run out of paint.

## Brush Artist · Refs · #43 Dragged black ink blocks
Gouache 1.00 · 70 px · 28.0 s

![Brush Artist · Refs · #43 Dragged black ink blocks](Brush-Artist-Refs-43-Dragged-black-ink-blocks.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 8 % → 0 % | 24.4 px | 0.64 | 0.02 | 132 |
| heavy line | 20 % → 4 % | 58.5 px | 0.64 | 0.19 | 330 |
| pressure swell | 14 % → 5 % | 53.0 px | 0.64 | 0.38 | 211 |
| fast wave | 36 % → 5 % | 41.8 px | 0.64 | 0.14 | 664 |
| slow wave | 37 % → 3 % | 43.2 px | 0.58 | 0.08 | 1045 |
| spiral | 47 % → 6 % | 30.9 px | 0.54 | 0.12 | 1323 |
| loop | 37 % → 7 % | 47.5 px | 0.63 | 0.19 | 688 |
| tilted | 14 % → 13 % | 39.3 px | 0.62 | 0.96 | 302 |
| over the wet one | 29 % → 10 % | 42.8 px | 0.62 | 0.34 | 255 |
| long, no reload | 55 % → 10 % | 24.6 px | 0.64 | 0.18 | 1537 | quarters: 0.52 → 0.41 → 0.30 → 0.19

Numbers say: light vs heavy: width 24.4 → 58.5 px, dark 0.64 → 0.64.

## Brush Artist · Refs · #44 Blue looping ribbon
Oil 1.00 · 80 px · 25.6 s

![Brush Artist · Refs · #44 Blue looping ribbon](Brush-Artist-Refs-44-Blue-looping-ribbon.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 25 % → 26 % | 73.1 px | 0.72 | 1.04 | 289 |
| heavy line | 27 % → 27 % | 77.7 px | 0.71 | 1.00 | 331 |
| pressure swell | 20 % → 21 % | 76.5 px | 0.71 | 1.03 | 230 |
| fast wave | 62 % → 64 % | 71.4 px | 0.71 | 1.04 | 891 |
| slow wave | 58 % → 58 % | 67.4 px | 0.70 | 1.00 | 1317 |
| spiral | 76 % → 77 % | 50.3 px | 0.69 | 1.00 | 1596 |
| loop | 53 % → 53 % | 69.2 px | 0.69 | 1.00 | 1079 |
| tilted | 20 % → 20 % | 56.1 px | 0.74 | 1.00 | 399 |
| over the wet one | 41 % → 41 % | 58.7 px | 0.74 | 1.00 | 362 |
| long, no reload | 90 % → 90 % | 40.1 px | 0.69 | 1.00 | 2350 | quarters: 0.67 → 0.68 → 0.66 → 0.59

Numbers say: light vs heavy: width 73.1 → 77.7 px, dark 0.72 → 0.71; pressure barely changes the width; the long stroke does not run out of paint.

## Brush Artist · Refs · #45 Soft pastel pepper
Pastel 1.00 · 40 px · 10.5 s

![Brush Artist · Refs · #45 Soft pastel pepper](Brush-Artist-Refs-45-Soft-pastel-pepper.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 4 % → 4 % | 11.0 px | 0.53 | 1.00 | 49 |
| heavy line | 7 % → 7 % | 21.2 px | 0.53 | 1.00 | 49 |
| pressure swell | 5 % → 5 % | 19.0 px | 0.55 | 1.00 | 39 |
| fast wave | 17 % → 17 % | 19.3 px | 0.56 | 1.00 | 135 |
| slow wave | 16 % → 16 % | 18.0 px | 0.54 | 1.00 | 230 |
| spiral | 23 % → 23 % | 15.4 px | 0.54 | 1.00 | 231 |
| loop | 12 % → 12 % | 15.4 px | 0.54 | 1.00 | 133 |
| tilted | 4 % → 4 % | 11.4 px | 0.55 | 1.00 | 98 |
| over the wet one | 10 % → 10 % | 16.7 px | 0.55 | 1.00 | 83 |
| long, no reload | 28 % → 28 % | 12.6 px | 0.53 | 1.00 | 415 | quarters: 0.17 → 0.16 → 0.17 → 0.17

Numbers say: light vs heavy: width 11.0 → 21.2 px, dark 0.53 → 0.53; the long stroke does not run out of paint.

## Brush Artist · Refs · #46 Red-brown ink lips
Watercolour 1.00 · 50 px · 41.2 s

![Brush Artist · Refs · #46 Red-brown ink lips](Brush-Artist-Refs-46-Red-brown-ink-lips.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 15 % → 31 % | 43.9 px | 0.59 | 2.04 | 68 |
| heavy line | 22 % → 35 % | 63.4 px | 0.60 | 1.58 | 108 |
| pressure swell | 13 % → 22 % | 50.3 px | 0.63 | 1.64 | 73 |
| fast wave | 43 % → 64 % | 49.7 px | 0.64 | 1.50 | 258 |
| slow wave | 42 % → 63 % | 49.1 px | 0.67 | 1.49 | 396 |
| spiral | 65 % → 79 % | 42.6 px | 0.69 | 1.22 | 385 |
| loop | 38 % → 55 % | 48.8 px | 0.67 | 1.47 | 200 |
| tilted | 21 % → 23 % | 58.2 px | 0.60 | 1.11 | 139 |
| over the wet one | 42 % → 63 % | 58.5 px | 0.60 | 1.51 | 127 |
| long, no reload | 78 % → 95 % | 35.1 px | 0.70 | 1.21 | 571 | quarters: 0.71 → 0.71 → 0.69 → 0.65

Numbers say: light vs heavy: width 43.9 → 63.4 px, dark 0.59 → 0.60; the long stroke does not run out of paint; wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #47 Pink knife slabs
Impasto 1.00 · 90 px · 31.2 s

![Brush Artist · Refs · #47 Pink knife slabs](Brush-Artist-Refs-47-Pink-knife-slabs.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 27 % → 26 % | 78.7 px | 0.29 | 0.97 | 226 |
| heavy line | 29 % → 28 % | 84.6 px | 0.29 | 0.96 | 233 |
| pressure swell | 22 % → 22 % | 81.2 px | 0.26 | 1.01 | 174 |
| fast wave | 62 % → 61 % | 71.8 px | 0.24 | 0.98 | 622 |
| slow wave | 62 % → 58 % | 71.5 px | 0.28 | 0.94 | 981 |
| spiral | 75 % → 60 % | 49.3 px | 0.28 | 0.80 | 1472 |
| loop | 56 % → 54 % | 72.1 px | 0.29 | 0.97 | 548 |
| tilted | 22 % → 22 % | 60.2 px | 0.25 | 1.00 | 351 |
| over the wet one | 46 % → 44 % | 69.3 px | 0.25 | 0.96 | 265 |
| long, no reload | 93 % → 77 % | 41.9 px | 0.26 | 0.83 | 1649 | quarters: 0.00 → 0.00 → 0.00 → 0.00

Numbers say: light vs heavy: width 78.7 → 84.6 px, dark 0.29 → 0.29; pressure barely changes the width; the long stroke does not run out of paint.

## Brush Artist · Refs · #48 Black bands with drips
Gouache 1.00 · 70 px · 44.9 s

![Brush Artist · Refs · #48 Black bands with drips](Brush-Artist-Refs-48-Black-bands-with-drips.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 28 % → 23 % | 80.2 px | 0.63 | 0.82 | 183 |
| heavy line | 35 % → 26 % | 100.7 px | 0.64 | 0.75 | 244 |
| pressure swell | 25 % → 21 % | 93.8 px | 0.63 | 0.85 | 184 |
| fast wave | 63 % → 41 % | 72.9 px | 0.63 | 0.64 | 593 |
| slow wave | 62 % → 41 % | 71.5 px | 0.63 | 0.66 | 1174 |
| spiral | 69 % → 40 % | 45.7 px | 0.61 | 0.57 | 972 |
| loop | 54 % → 40 % | 69.9 px | 0.63 | 0.74 | 521 |
| tilted | 29 % → 29 % | 80.5 px | 0.62 | 1.01 | 327 |
| over the wet one | 59 % → 48 % | 82.9 px | 0.62 | 0.82 | 239 |
| long, no reload | 78 % → 37 % | 34.9 px | 0.61 | 0.47 | 1439 | quarters: 0.58 → 0.54 → 0.47 → 0.39

Numbers say: light vs heavy: width 80.2 → 100.7 px, dark 0.63 → 0.64.

## Brush Artist · Refs · #49 Magenta letters round brush
Ink 1.00 · 30 px · 32.6 s

![Brush Artist · Refs · #49 Magenta letters round brush](Brush-Artist-Refs-49-Magenta-letters-round-brush.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 6 % → 8 % | 18.1 px | 0.49 | 1.21 | 39 |
| heavy line | 21 % → 20 % | 60.3 px | 0.51 | 0.98 | 105 |
| pressure swell | 13 % → 13 % | 47.1 px | 0.51 | 1.01 | 61 |
| fast wave | 38 % → 38 % | 44.0 px | 0.51 | 1.00 | 184 |
| slow wave | 34 % → 34 % | 39.4 px | 0.51 | 0.99 | 320 |
| spiral | 49 % → 48 % | 32.6 px | 0.51 | 0.96 | 311 |
| loop | 30 % → 30 % | 38.3 px | 0.51 | 1.00 | 160 |
| tilted | 11 % → 12 % | 32.0 px | 0.52 | 1.00 | 103 |
| over the wet one | 27 % → 27 % | 42.2 px | 0.52 | 1.01 | 74 |
| long, no reload | 63 % → 56 % | 28.2 px | 0.50 | 0.90 | 443 | quarters: 0.42 → 0.37 → 0.30 → 0.25

Numbers say: light vs heavy: width 18.1 → 60.3 px, dark 0.49 → 0.51.

## Brush Artist · Refs · #50 Thick swipes on photo
Impasto 1.00 · 40 px · 20.2 s

![Brush Artist · Refs · #50 Thick swipes on photo](Brush-Artist-Refs-50-Thick-swipes-on-photo.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 13 % → 13 % | 38.6 px | 0.27 | 0.95 | 120 |
| heavy line | 14 % → 13 % | 40.0 px | 0.27 | 0.96 | 119 |
| pressure swell | 11 % → 10 % | 40.1 px | 0.24 | 0.95 | 96 |
| fast wave | 35 % → 31 % | 40.1 px | 0.24 | 0.89 | 484 |
| slow wave | 34 % → 32 % | 39.5 px | 0.26 | 0.93 | 753 |
| spiral | 58 % → 46 % | 38.5 px | 0.29 | 0.79 | 702 |
| loop | 29 % → 28 % | 37.4 px | 0.26 | 0.96 | 465 |
| tilted | 12 % → 12 % | 33.6 px | 0.22 | 1.00 | 218 |
| over the wet one | 25 % → 24 % | 36.7 px | 0.22 | 0.96 | 196 |
| long, no reload | 68 % → 46 % | 30.4 px | 0.26 | 0.68 | 881 | quarters: 0.00 → 0.00 → 0.00 → 0.00

Numbers say: light vs heavy: width 38.6 → 40.0 px, dark 0.27 → 0.27; pressure barely changes the width.

## Brush Artist · Refs · Drag #e8b4a8
Gouache 1.00 · 40 px · 21.1 s

![Brush Artist · Refs · Drag #e8b4a8](Brush-Artist-Refs-Drag-e8b4a8.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 3 % → 0 % | 9.3 px | 0.00 | 0.00 | 101 |
| heavy line | 6 % → 0 % | 16.1 px | 0.34 | 0.01 | 121 |
| pressure swell | 3 % → 0 % | 12.9 px | 0.00 | 0.00 | 87 |
| fast wave | 16 % → 0 % | 18.1 px | 0.00 | 0.00 | 357 |
| slow wave | 13 % → 0 % | 15.0 px | 0.00 | 0.00 | 561 |
| spiral | 20 % → 0 % | 13.4 px | 0.00 | 0.00 | 542 |
| loop | 13 % → 0 % | 17.1 px | 0.00 | 0.00 | 314 |
| tilted | 6 % → 5 % | 16.8 px | 0.00 | 0.77 | 249 |
| over the wet one | 7 % → 0 % | 1.8 px | 0.00 | 0.00 | 169 |
| long, no reload | 10 % → 0 % | 4.5 px | 0.00 | 0.00 | 979 | quarters: 0.02 → 0.02 → 0.02 → 0.02

Numbers say: light vs heavy: width 9.3 → 16.1 px, dark 0.00 → 0.34; the long stroke does not run out of paint.

## Brush Artist · Refs · Drag #e8e4e0
Gouache 1.00 · 40 px · 21.2 s

![Brush Artist · Refs · Drag #e8e4e0](Brush-Artist-Refs-Drag-e8e4e0.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 3 % → 0 % | 9.3 px | 0.00 | 0.00 | 164 |
| heavy line | 6 % → 0 % | 16.1 px | 0.43 | 0.01 | 153 |
| pressure swell | 3 % → 0 % | 12.9 px | 0.00 | 0.00 | 180 |
| fast wave | 16 % → 0 % | 18.1 px | 0.00 | 0.00 | 592 |
| slow wave | 13 % → 0 % | 15.0 px | 0.00 | 0.00 | 862 |
| spiral | 20 % → 0 % | 13.4 px | 0.00 | 0.00 | 1046 |
| loop | 13 % → 0 % | 17.1 px | 0.00 | 0.00 | 354 |
| tilted | 6 % → 5 % | 16.8 px | 0.00 | 0.77 | 200 |
| over the wet one | 7 % → 0 % | 1.8 px | 0.00 | 0.00 | 179 |
| long, no reload | 10 % → 0 % | 4.5 px | 0.00 | 0.00 | 1093 | quarters: 0.02 → 0.02 → 0.02 → 0.02

Numbers say: light vs heavy: width 9.3 → 16.1 px, dark 0.00 → 0.43; the long stroke does not run out of paint.

## Brush Artist · Refs · Finger
Pastel 1.00 · 36 px · 22.9 s · over bands of wet oil paint and oil pastel in turn (it works on paint already there: look at what it does to the bands; covered counts the bands too)

![Brush Artist · Refs · Finger](Brush-Artist-Refs-Finger.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 26 % → 26 % | 74.4 px | 0.80 | 1.00 | 69 |
| heavy line | 27 % → 27 % | 79.3 px | 0.80 | 1.00 | 79 |
| pressure swell | 26 % → 26 % | 98.0 px | 0.80 | 1.00 | 58 |
| fast wave | 33 % → 33 % | 38.0 px | 0.78 | 1.00 | 173 |
| slow wave | 31 % → 31 % | 36.3 px | 0.78 | 1.00 | 317 |
| spiral | 38 % → 38 % | 25.3 px | 0.76 | 1.00 | 292 |
| loop | 31 % → 31 % | 39.5 px | 0.79 | 1.00 | 124 |
| tilted | 26 % → 26 % | 73.5 px | 0.78 | 1.00 | 75 |
| over the wet one | 29 % → 29 % | 7.5 px | 0.78 | 1.00 | 53 |
| long, no reload | 39 % → 39 % | 17.4 px | 0.76 | 1.00 | 303 | quarters: 0.24 → 0.36 → 0.32 → 0.37

Numbers say: light vs heavy: width 74.4 → 79.3 px, dark 0.80 → 0.80; pressure barely changes the width; the long stroke does not run out of paint.

## Brush Artist · Ink — wash
Watercolour 1.00 · 38 px · 32.6 s

![Brush Artist · Ink — wash](Brush-Artist-Ink-wash.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 11 % → 11 % | 31.6 px | 0.39 | 1.04 | 91 |
| heavy line | 19 % → 19 % | 54.3 px | 0.32 | 1.03 | 101 |
| pressure swell | 12 % → 13 % | 45.2 px | 0.37 | 1.04 | 80 |
| fast wave | 39 % → 41 % | 45.5 px | 0.31 | 1.04 | 321 |
| slow wave | 37 % → 38 % | 42.9 px | 0.37 | 1.03 | 384 |
| spiral | 58 % → 61 % | 38.6 px | 0.31 | 1.04 | 466 |
| loop | 32 % → 33 % | 41.9 px | 0.35 | 1.02 | 186 |
| tilted | 13 % → 14 % | 37.0 px | 0.38 | 1.04 | 107 |
| over the wet one | 29 % → 30 % | 42.8 px | 0.38 | 1.04 | 75 |
| long, no reload | 67 % → 72 % | 30.0 px | 0.29 | 1.07 | 450 | quarters: 0.34 → 0.27 → 0.19 → 0.12

Numbers say: light vs heavy: width 31.6 → 54.3 px, dark 0.39 → 0.32.

## Brush Artist · Ink — brush line
Ink 1.00 · 16 px · 26.3 s

![Brush Artist · Ink — brush line](Brush-Artist-Ink-brush-line.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 3 % → 5 % | 8.2 px | 0.77 | 1.72 | 36 |
| heavy line | 12 % → 12 % | 35.2 px | 0.88 | 0.99 | 82 |
| pressure swell | 8 % → 8 % | 28.5 px | 0.86 | 1.06 | 49 |
| fast wave | 24 % → 24 % | 28.2 px | 0.87 | 0.98 | 144 |
| slow wave | 20 % → 20 % | 23.7 px | 0.87 | 0.97 | 194 |
| spiral | 31 % → 27 % | 20.3 px | 0.86 | 0.87 | 263 |
| loop | 19 % → 19 % | 24.3 px | 0.87 | 0.99 | 126 |
| tilted | 8 % → 8 % | 21.2 px | 0.88 | 1.01 | 67 |
| over the wet one | 17 % → 17 % | 26.2 px | 0.88 | 1.01 | 66 |
| long, no reload | 44 % → 31 % | 19.7 px | 0.84 | 0.70 | 383 | quarters: 0.51 → 0.41 → 0.30 → 0.20

Numbers say: light vs heavy: width 8.2 → 35.2 px, dark 0.77 → 0.88; wet paint spreads well beyond the stroke.

## Brush Artist · Ink — dry brush
Gouache 1.00 · 30 px · 24.2 s

![Brush Artist · Ink — dry brush](Brush-Artist-Ink-dry-brush.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 3 % → 0 % | 9.5 px | 0.00 | 0.00 | 60 |
| heavy line | 5 % → 0 % | 14.6 px | 0.76 | 0.01 | 152 |
| pressure swell | 5 % → 0 % | 17.5 px | 0.76 | 0.04 | 94 |
| fast wave | 11 % → 1 % | 12.4 px | 0.76 | 0.11 | 324 |
| slow wave | 12 % → 0 % | 14.3 px | 0.76 | 0.00 | 417 |
| spiral | 17 % → 0 % | 11.3 px | 0.76 | 0.02 | 388 |
| loop | 11 % → 0 % | 13.8 px | 0.76 | 0.03 | 231 |
| tilted | 5 % → 5 % | 14.7 px | 0.76 | 0.91 | 181 |
| over the wet one | 10 % → 0 % | 12.8 px | 0.76 | 0.04 | 163 |
| long, no reload | 18 % → 2 % | 8.0 px | 0.76 | 0.10 | 911 | quarters: 0.28 → 0.17 → 0.10 → 0.08

Numbers say: light vs heavy: width 9.5 → 14.6 px, dark 0.00 → 0.76.

## Brush Artist · Watercolour — blue
Watercolour 0.93 · Ink 0.07 · 40 px · 27.1 s

![Brush Artist · Watercolour — blue](Brush-Artist-Watercolour-blue.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 6 % → 11 % | 16.2 px | 0.29 | 1.88 | 42 |
| heavy line | 11 % → 13 % | 31.9 px | 0.29 | 1.17 | 66 |
| pressure swell | 7 % → 9 % | 25.7 px | 0.30 | 1.38 | 44 |
| fast wave | 24 % → 27 % | 28.2 px | 0.29 | 1.12 | 189 |
| slow wave | 23 % → 32 % | 26.4 px | 0.31 | 1.41 | 225 |
| spiral | 39 % → 47 % | 25.6 px | 0.29 | 1.21 | 223 |
| loop | 20 % → 25 % | 25.7 px | 0.30 | 1.25 | 129 |
| tilted | 12 % → 12 % | 34.0 px | 0.30 | 1.00 | 95 |
| over the wet one | 21 % → 25 % | 25.2 px | 0.30 | 1.19 | 63 |
| long, no reload | 53 % → 59 % | 23.6 px | 0.30 | 1.12 | 349 | quarters: 0.23 → 0.21 → 0.19 → 0.16

Numbers say: light vs heavy: width 16.2 → 31.9 px, dark 0.29 → 0.29; wet paint spreads well beyond the stroke.

## Brush Artist · Watercolour — violet
Watercolour 0.93 · Ink 0.07 · 40 px · 27.3 s

![Brush Artist · Watercolour — violet](Brush-Artist-Watercolour-violet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 6 % → 11 % | 16.2 px | 0.36 | 1.88 | 31 |
| heavy line | 11 % → 13 % | 31.9 px | 0.37 | 1.17 | 66 |
| pressure swell | 7 % → 9 % | 25.7 px | 0.38 | 1.38 | 42 |
| fast wave | 24 % → 27 % | 28.2 px | 0.38 | 1.12 | 144 |
| slow wave | 23 % → 32 % | 26.4 px | 0.39 | 1.41 | 228 |
| spiral | 39 % → 47 % | 25.6 px | 0.37 | 1.21 | 220 |
| loop | 20 % → 25 % | 25.7 px | 0.38 | 1.25 | 117 |
| tilted | 12 % → 12 % | 34.0 px | 0.38 | 1.00 | 90 |
| over the wet one | 21 % → 25 % | 25.2 px | 0.38 | 1.19 | 55 |
| long, no reload | 53 % → 59 % | 23.6 px | 0.38 | 1.12 | 484 | quarters: 0.28 → 0.27 → 0.24 → 0.21

Numbers say: light vs heavy: width 16.2 → 31.9 px, dark 0.36 → 0.37; wet paint spreads well beyond the stroke.

## Brush Artist · Watercolour — teal
Watercolour 0.93 · Ink 0.07 · 40 px · 27.7 s

![Brush Artist · Watercolour — teal](Brush-Artist-Watercolour-teal.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 6 % → 11 % | 16.2 px | 0.23 | 1.88 | 32 |
| heavy line | 11 % → 13 % | 31.9 px | 0.23 | 1.17 | 67 |
| pressure swell | 7 % → 9 % | 25.7 px | 0.24 | 1.38 | 55 |
| fast wave | 24 % → 27 % | 28.2 px | 0.23 | 1.12 | 182 |
| slow wave | 23 % → 32 % | 26.4 px | 0.25 | 1.41 | 227 |
| spiral | 39 % → 47 % | 25.6 px | 0.23 | 1.21 | 220 |
| loop | 20 % → 25 % | 25.7 px | 0.24 | 1.25 | 119 |
| tilted | 12 % → 12 % | 34.0 px | 0.24 | 1.00 | 92 |
| over the wet one | 21 % → 25 % | 25.2 px | 0.24 | 1.19 | 58 |
| long, no reload | 53 % → 59 % | 23.6 px | 0.24 | 1.12 | 347 | quarters: 0.18 → 0.16 → 0.15 → 0.13

Numbers say: light vs heavy: width 16.2 → 31.9 px, dark 0.23 → 0.23; wet paint spreads well beyond the stroke.

## Brush Artist · Gouache
Gouache 1.00 · 30 px · 31.2 s

![Brush Artist · Gouache](Brush-Artist-Gouache.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 8 % → 8 % | 24.4 px | 0.27 | 0.97 | 67 |
| heavy line | 15 % → 12 % | 42.8 px | 0.27 | 0.78 | 82 |
| pressure swell | 11 % → 9 % | 41.0 px | 0.27 | 0.85 | 59 |
| fast wave | 30 % → 14 % | 34.9 px | 0.26 | 0.45 | 214 |
| slow wave | 29 % → 14 % | 34.0 px | 0.26 | 0.47 | 324 |
| spiral | 40 % → 14 % | 26.6 px | 0.26 | 0.35 | 335 |
| loop | 24 % → 15 % | 30.6 px | 0.26 | 0.62 | 174 |
| tilted | 10 % → 10 % | 27.4 px | 0.27 | 1.01 | 87 |
| over the wet one | 22 % → 19 % | 32.9 px | 0.27 | 0.89 | 73 |
| long, no reload | 43 % → 15 % | 19.1 px | 0.26 | 0.35 | 447 | quarters: 0.01 → 0.01 → 0.01 → 0.01

Numbers say: light vs heavy: width 24.4 → 42.8 px, dark 0.27 → 0.27; the long stroke does not run out of paint.

## Brush Artist · Oil — bristle
Oil 0.89 · Oil glaze 0.11 · 30 px · 14.5 s

![Brush Artist · Oil — bristle](Brush-Artist-Oil-bristle.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 10 % → 10 % | 28.5 px | 0.53 | 1.00 | 109 |
| heavy line | 11 % → 11 % | 32.4 px | 0.54 | 1.00 | 119 |
| pressure swell | 8 % → 8 % | 31.8 px | 0.54 | 1.00 | 85 |
| fast wave | 28 % → 28 % | 32.0 px | 0.54 | 1.00 | 302 |
| slow wave | 27 % → 27 % | 31.6 px | 0.54 | 1.00 | 501 |
| spiral | 48 % → 48 % | 31.3 px | 0.53 | 1.00 | 729 |
| loop | 22 % → 22 % | 28.9 px | 0.54 | 1.00 | 349 |
| tilted | 11 % → 11 % | 29.9 px | 0.54 | 1.00 | 141 |
| over the wet one | 21 % → 21 % | 29.6 px | 0.54 | 1.00 | 122 |
| long, no reload | 55 % → 55 % | 24.7 px | 0.52 | 1.00 | 823 | quarters: 0.35 → 0.33 → 0.31 → 0.29

Numbers say: light vs heavy: width 28.5 → 32.4 px, dark 0.53 → 0.54.

## Brush Artist · Charcoal — stick
Charcoal 0.78 · Pastel 0.22 · 28 px · 10.0 s

![Brush Artist · Charcoal — stick](Brush-Artist-Charcoal-stick.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 5 % → 5 % | 15.2 px | 0.85 | 1.00 | 19 |
| heavy line | 8 % → 8 % | 24.2 px | 0.85 | 1.00 | 30 |
| pressure swell | 5 % → 5 % | 19.3 px | 0.85 | 1.00 | 19 |
| fast wave | 19 % → 19 % | 21.5 px | 0.85 | 1.00 | 72 |
| slow wave | 18 % → 18 % | 21.1 px | 0.85 | 1.00 | 115 |
| spiral | 25 % → 25 % | 16.3 px | 0.85 | 1.00 | 114 |
| loop | 16 % → 16 % | 20.2 px | 0.85 | 1.00 | 63 |
| tilted | 6 % → 6 % | 17.3 px | 0.85 | 1.00 | 30 |
| over the wet one | 14 % → 14 % | 20.5 px | 0.85 | 1.00 | 29 |
| long, no reload | 41 % → 41 % | 18.5 px | 0.85 | 1.00 | 179 | quarters: 0.39 → 0.39 → 0.39 → 0.39

Numbers say: light vs heavy: width 15.2 → 24.2 px, dark 0.85 → 0.85; the long stroke does not run out of paint.

## Brush Artist · Charcoal — stick B
Charcoal 0.78 · Pastel 0.22 · 36 px · 11.2 s

![Brush Artist · Charcoal — stick B](Brush-Artist-Charcoal-stick-B.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 7 % → 7 % | 19.2 px | 0.85 | 1.00 | 36 |
| heavy line | 10 % → 10 % | 30.5 px | 0.85 | 1.00 | 61 |
| pressure swell | 7 % → 7 % | 24.5 px | 0.85 | 1.00 | 31 |
| fast wave | 24 % → 24 % | 27.6 px | 0.85 | 1.00 | 160 |
| slow wave | 23 % → 23 % | 26.6 px | 0.85 | 1.00 | 190 |
| spiral | 35 % → 35 % | 23.2 px | 0.85 | 1.00 | 219 |
| loop | 19 % → 19 % | 25.2 px | 0.85 | 1.00 | 121 |
| tilted | 7 % → 7 % | 20.3 px | 0.85 | 1.00 | 50 |
| over the wet one | 17 % → 17 % | 25.9 px | 0.85 | 1.00 | 60 |
| long, no reload | 50 % → 50 % | 22.6 px | 0.85 | 1.00 | 317 | quarters: 0.47 → 0.47 → 0.47 → 0.47

Numbers say: light vs heavy: width 19.2 → 30.5 px, dark 0.85 → 0.85; the long stroke does not run out of paint.

## Brush Artist · Charcoal — stick C
Charcoal 0.78 · Pastel 0.22 · 22 px · 10.5 s

![Brush Artist · Charcoal — stick C](Brush-Artist-Charcoal-stick-C.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 4 % → 4 % | 12.2 px | 0.85 | 1.00 | 22 |
| heavy line | 7 % → 7 % | 19.4 px | 0.85 | 1.00 | 39 |
| pressure swell | 4 % → 4 % | 14.3 px | 0.85 | 1.00 | 18 |
| fast wave | 15 % → 15 % | 17.1 px | 0.85 | 1.00 | 58 |
| slow wave | 15 % → 15 % | 17.0 px | 0.85 | 1.00 | 106 |
| spiral | 20 % → 20 % | 13.3 px | 0.85 | 1.00 | 124 |
| loop | 12 % → 12 % | 16.1 px | 0.85 | 1.00 | 74 |
| tilted | 5 % → 5 % | 15.1 px | 0.85 | 1.00 | 38 |
| over the wet one | 11 % → 11 % | 16.8 px | 0.85 | 1.00 | 25 |
| long, no reload | 34 % → 34 % | 15.3 px | 0.85 | 1.00 | 162 | quarters: 0.33 → 0.32 → 0.32 → 0.32

Numbers say: light vs heavy: width 12.2 → 19.4 px, dark 0.85 → 0.85; the long stroke does not run out of paint.

## Oil focus · A G x2 under
Gouache 0.85 · Ink 0.15 + turpentine 50 % · 220 px · 104.6 s

![Oil focus · A G x2 under](Oil-focus-A-G-x2-under.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 65 % → 63 % | 189.2 px | 0.32 | 0.96 | 1189 |
| heavy line | 67 % → 60 % | 193.8 px | 0.33 | 0.89 | 1868 |
| pressure swell | 56 % → 65 % | 209.8 px | 0.34 | 1.17 | 989 |
| fast wave | 97 % → 86 % | 111.6 px | 0.35 | 0.89 | 4461 |
| slow wave | 98 % → 68 % | 113.5 px | 0.31 | 0.69 | 6401 |
| spiral | 99 % → 68 % | 65.3 px | 0.32 | 0.69 | 5908 |
| loop | 98 % → 86 % | 126.4 px | 0.32 | 0.88 | 2710 |
| tilted | 49 % → 49 % | 136.0 px | 0.34 | 1.00 | 1607 |
| over the wet one | 87 % → 83 % | 107.3 px | 0.34 | 0.95 | 1274 |
| long, no reload | 100 % → 79 % | 44.8 px | 0.29 | 0.79 | 8212 | quarters: 0.31 → 0.30 → 0.28 → 0.18

Numbers say: light vs heavy: width 189.2 → 193.8 px, dark 0.32 → 0.33; pressure barely changes the width.

## Oil focus · A G x2
Gouache 1.00 + turpentine 15 % · 260 px · 119.9 s

![Oil focus · A G x2](Oil-focus-A-G-x2.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 74 % → 71 % | 213.6 px | 0.30 | 0.97 | 1971 |
| heavy line | 75 % → 65 % | 219.1 px | 0.30 | 0.86 | 1788 |
| pressure swell | 66 % → 73 % | 248.3 px | 0.28 | 1.10 | 2058 |
| fast wave | 99 % → 90 % | 114.8 px | 0.26 | 0.90 | 5000 |
| slow wave | 100 % → 74 % | 115.1 px | 0.30 | 0.74 | 7880 |
| spiral | 100 % → 77 % | 65.9 px | 0.29 | 0.77 | 7789 |
| loop | 100 % → 93 % | 129.5 px | 0.30 | 0.93 | 4306 |
| tilted | 56 % → 56 % | 154.9 px | 0.27 | 1.00 | 2242 |
| over the wet one | 92 % → 88 % | 103.0 px | 0.27 | 0.96 | 1753 |
| long, no reload | 100 % → 86 % | 44.8 px | 0.29 | 0.86 | 16108 | quarters: 0.00 → 0.00 → 0.00 → 0.00

Numbers say: light vs heavy: width 213.6 → 219.1 px, dark 0.30 → 0.30; pressure barely changes the width.

## Oil focus · B G x2 soft under
Gouache 0.85 · Ink 0.15 + turpentine 50 % · 220 px · 109.4 s

![Oil focus · B G x2 soft under](Oil-focus-B-G-x2-soft-under.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 65 % → 62 % | 188.6 px | 0.32 | 0.96 | 1493 |
| heavy line | 66 % → 59 % | 192.6 px | 0.32 | 0.89 | 1330 |
| pressure swell | 56 % → 65 % | 209.5 px | 0.33 | 1.16 | 1585 |
| fast wave | 97 % → 85 % | 111.5 px | 0.35 | 0.88 | 3304 |
| slow wave | 98 % → 66 % | 113.4 px | 0.31 | 0.67 | 6022 |
| spiral | 99 % → 68 % | 65.3 px | 0.31 | 0.69 | 5997 |
| loop | 97 % → 85 % | 126.2 px | 0.32 | 0.87 | 2727 |
| tilted | 50 % → 50 % | 138.3 px | 0.34 | 1.00 | 1598 |
| over the wet one | 87 % → 83 % | 105.3 px | 0.34 | 0.95 | 1602 |
| long, no reload | 100 % → 78 % | 44.8 px | 0.29 | 0.78 | 8606 | quarters: 0.30 → 0.30 → 0.28 → 0.18

Numbers say: light vs heavy: width 188.6 → 192.6 px, dark 0.32 → 0.32; pressure barely changes the width.

## Oil focus · B G x2 soft
Gouache 1.00 + turpentine 15 % · 260 px · 145.1 s

![Oil focus · B G x2 soft](Oil-focus-B-G-x2-soft.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 73 % → 71 % | 213.2 px | 0.30 | 0.96 | 1603 |
| heavy line | 75 % → 63 % | 218.1 px | 0.30 | 0.84 | 1926 |
| pressure swell | 66 % → 72 % | 247.5 px | 0.27 | 1.10 | 1399 |
| fast wave | 99 % → 89 % | 114.8 px | 0.25 | 0.90 | 5589 |
| slow wave | 100 % → 72 % | 115.0 px | 0.30 | 0.73 | 11674 |
| spiral | 100 % → 76 % | 65.9 px | 0.29 | 0.76 | 11170 |
| loop | 100 % → 93 % | 129.5 px | 0.29 | 0.93 | 7763 |
| tilted | 56 % → 56 % | 156.4 px | 0.26 | 1.00 | 2984 |
| over the wet one | 92 % → 88 % | 101.4 px | 0.26 | 0.95 | 2467 |
| long, no reload | 100 % → 87 % | 44.8 px | 0.28 | 0.87 | 16798 | quarters: 0.00 → 0.00 → 0.00 → 0.00

Numbers say: light vs heavy: width 213.2 → 218.1 px, dark 0.30 → 0.30; pressure barely changes the width.

## Oil focus · C G x2 mix low under
Gouache 0.85 · Ink 0.15 + turpentine 50 % · 220 px · 137.1 s

![Oil focus · C G x2 mix low under](Oil-focus-C-G-x2-mix-low-under.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 65 % → 63 % | 189.2 px | 0.28 | 0.96 | 1262 |
| heavy line | 67 % → 60 % | 193.8 px | 0.29 | 0.89 | 1535 |
| pressure swell | 56 % → 65 % | 209.8 px | 0.33 | 1.17 | 1287 |
| fast wave | 97 % → 86 % | 111.6 px | 0.39 | 0.89 | 5366 |
| slow wave | 98 % → 68 % | 113.5 px | 0.30 | 0.69 | 8808 |
| spiral | 99 % → 68 % | 65.3 px | 0.33 | 0.69 | 8841 |
| loop | 98 % → 86 % | 126.4 px | 0.30 | 0.88 | 6244 |
| tilted | 49 % → 49 % | 136.0 px | 0.38 | 1.00 | 2733 |
| over the wet one | 87 % → 83 % | 107.3 px | 0.38 | 0.95 | 1862 |
| long, no reload | 100 % → 79 % | 44.8 px | 0.28 | 0.79 | 12616 | quarters: 0.29 → 0.29 → 0.27 → 0.17

Numbers say: light vs heavy: width 189.2 → 193.8 px, dark 0.28 → 0.29; pressure barely changes the width.

## Oil focus · C G x2 mix low
Gouache 1.00 + turpentine 15 % · 260 px · 146.2 s

![Oil focus · C G x2 mix low](Oil-focus-C-G-x2-mix-low.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 74 % → 71 % | 213.6 px | 0.32 | 0.97 | 2219 |
| heavy line | 75 % → 65 % | 219.1 px | 0.31 | 0.86 | 2363 |
| pressure swell | 66 % → 73 % | 248.3 px | 0.24 | 1.10 | 1605 |
| fast wave | 99 % → 90 % | 114.8 px | 0.18 | 0.90 | 6624 |
| slow wave | 100 % → 74 % | 115.1 px | 0.29 | 0.74 | 13258 |
| spiral | 100 % → 77 % | 65.9 px | 0.24 | 0.77 | 10786 |
| loop | 100 % → 93 % | 129.5 px | 0.30 | 0.93 | 5694 |
| tilted | 56 % → 56 % | 154.9 px | 0.19 | 1.00 | 3044 |
| over the wet one | 92 % → 88 % | 103.0 px | 0.19 | 0.96 | 3054 |
| long, no reload | 100 % → 86 % | 44.8 px | 0.24 | 0.86 | 15523 | quarters: 0.00 → 0.00 → 0.00 → 0.00

Numbers say: light vs heavy: width 213.6 → 219.1 px, dark 0.32 → 0.31; pressure barely changes the width.

## Oil focus · D G x2 no pickup under
Gouache 0.85 · Ink 0.15 + turpentine 50 % · 220 px · 123.9 s

![Oil focus · D G x2 no pickup under](Oil-focus-D-G-x2-no-pickup-under.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 65 % → 63 % | 189.2 px | 0.32 | 0.96 | 1374 |
| heavy line | 67 % → 60 % | 193.7 px | 0.32 | 0.89 | 1731 |
| pressure swell | 56 % → 65 % | 209.8 px | 0.34 | 1.17 | 1209 |
| fast wave | 96 % → 83 % | 111.4 px | 0.35 | 0.86 | 4853 |
| slow wave | 98 % → 63 % | 113.4 px | 0.31 | 0.64 | 8503 |
| spiral | 99 % → 66 % | 65.3 px | 0.32 | 0.67 | 7877 |
| loop | 98 % → 82 % | 126.3 px | 0.32 | 0.84 | 3637 |
| tilted | 49 % → 49 % | 135.7 px | 0.34 | 1.00 | 4062 |
| over the wet one | 87 % → 82 % | 107.5 px | 0.34 | 0.94 | 1747 |
| long, no reload | 100 % → 67 % | 44.8 px | 0.29 | 0.67 | 11683 | quarters: 0.31 → 0.30 → 0.25 → 0.11

Numbers say: light vs heavy: width 189.2 → 193.7 px, dark 0.32 → 0.32; pressure barely changes the width.

## Oil focus · D G x2 no pickup
Gouache 1.00 + turpentine 15 % · 260 px · 134.8 s

![Oil focus · D G x2 no pickup](Oil-focus-D-G-x2-no-pickup.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 74 % → 71 % | 213.6 px | 0.30 | 0.97 | 1869 |
| heavy line | 75 % → 65 % | 219.1 px | 0.30 | 0.86 | 2137 |
| pressure swell | 66 % → 73 % | 248.2 px | 0.27 | 1.10 | 1991 |
| fast wave | 99 % → 88 % | 114.8 px | 0.25 | 0.88 | 5928 |
| slow wave | 100 % → 70 % | 115.0 px | 0.29 | 0.70 | 10731 |
| spiral | 100 % → 75 % | 65.9 px | 0.28 | 0.75 | 10614 |
| loop | 100 % → 90 % | 129.5 px | 0.29 | 0.90 | 5145 |
| tilted | 55 % → 55 % | 154.8 px | 0.26 | 1.00 | 2975 |
| over the wet one | 92 % → 87 % | 103.1 px | 0.26 | 0.94 | 2480 |
| long, no reload | 100 % → 80 % | 44.8 px | 0.28 | 0.80 | 15367 | quarters: 0.00 → 0.00 → 0.00 → 0.00

Numbers say: light vs heavy: width 213.6 → 219.1 px, dark 0.30 → 0.30; pressure barely changes the width.

## Oil focus · E G x2 dilute 0.3 under
Gouache 0.85 · Ink 0.15 + turpentine 50 % · 220 px · 119.7 s

![Oil focus · E G x2 dilute 0.3 under](Oil-focus-E-G-x2-dilute-0-3-under.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 65 % → 63 % | 189.2 px | 0.32 | 0.96 | 1820 |
| heavy line | 67 % → 60 % | 193.8 px | 0.33 | 0.89 | 1777 |
| pressure swell | 56 % → 65 % | 209.8 px | 0.34 | 1.17 | 1173 |
| fast wave | 97 % → 86 % | 111.6 px | 0.35 | 0.89 | 4602 |
| slow wave | 98 % → 68 % | 113.5 px | 0.31 | 0.69 | 7447 |
| spiral | 99 % → 68 % | 65.3 px | 0.32 | 0.69 | 8327 |
| loop | 98 % → 86 % | 126.4 px | 0.32 | 0.88 | 4330 |
| tilted | 49 % → 49 % | 136.0 px | 0.34 | 1.00 | 2210 |
| over the wet one | 87 % → 83 % | 107.3 px | 0.34 | 0.95 | 1761 |
| long, no reload | 100 % → 79 % | 44.8 px | 0.29 | 0.79 | 11526 | quarters: 0.31 → 0.30 → 0.28 → 0.18

Numbers say: light vs heavy: width 189.2 → 193.8 px, dark 0.32 → 0.33; pressure barely changes the width.

## Oil focus · E G x2 dilute 0.3
Gouache 1.00 + turpentine 30 % · 260 px · 116.6 s

![Oil focus · E G x2 dilute 0.3](Oil-focus-E-G-x2-dilute-0-3.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 74 % → 70 % | 213.4 px | 0.31 | 0.95 | 1540 |
| heavy line | 75 % → 63 % | 218.9 px | 0.32 | 0.83 | 1810 |
| pressure swell | 66 % → 72 % | 247.7 px | 0.29 | 1.09 | 1356 |
| fast wave | 99 % → 88 % | 114.8 px | 0.27 | 0.89 | 5067 |
| slow wave | 100 % → 71 % | 115.0 px | 0.31 | 0.72 | 8631 |
| spiral | 100 % → 74 % | 65.9 px | 0.30 | 0.74 | 8715 |
| loop | 100 % → 90 % | 129.5 px | 0.30 | 0.90 | 4505 |
| tilted | 55 % → 55 % | 154.5 px | 0.28 | 1.00 | 2707 |
| over the wet one | 92 % → 87 % | 103.1 px | 0.28 | 0.95 | 1833 |
| long, no reload | 100 % → 84 % | 44.8 px | 0.29 | 0.84 | 13870 | quarters: 0.00 → 0.00 → 0.00 → 0.00

Numbers say: light vs heavy: width 213.4 → 218.9 px, dark 0.31 → 0.32; pressure barely changes the width.

## Oil focus · F G x2 wet load under
Gouache 0.85 · Ink 0.15 + turpentine 50 % · 220 px · 101.0 s

![Oil focus · F G x2 wet load under](Oil-focus-F-G-x2-wet-load-under.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 65 % → 62 % | 188.7 px | 0.32 | 0.96 | 1054 |
| heavy line | 67 % → 59 % | 193.6 px | 0.32 | 0.88 | 1245 |
| pressure swell | 56 % → 65 % | 209.0 px | 0.33 | 1.16 | 943 |
| fast wave | 97 % → 84 % | 111.5 px | 0.35 | 0.87 | 4040 |
| slow wave | 98 % → 65 % | 113.4 px | 0.31 | 0.67 | 6091 |
| spiral | 99 % → 66 % | 65.2 px | 0.32 | 0.67 | 5911 |
| loop | 98 % → 84 % | 126.3 px | 0.32 | 0.86 | 3744 |
| tilted | 49 % → 49 % | 135.4 px | 0.34 | 1.00 | 1616 |
| over the wet one | 87 % → 82 % | 107.4 px | 0.34 | 0.95 | 1352 |
| long, no reload | 100 % → 77 % | 44.8 px | 0.29 | 0.77 | 9433 | quarters: 0.30 → 0.30 → 0.27 → 0.17

Numbers say: light vs heavy: width 188.7 → 193.6 px, dark 0.32 → 0.32; pressure barely changes the width.

## Oil focus · F G x2 wet load
Gouache 1.00 + turpentine 15 % · 260 px · 115.9 s

![Oil focus · F G x2 wet load](Oil-focus-F-G-x2-wet-load.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 74 % → 72 % | 213.5 px | 0.30 | 0.98 | 1389 |
| heavy line | 75 % → 67 % | 218.7 px | 0.30 | 0.89 | 2043 |
| pressure swell | 67 % → 74 % | 249.6 px | 0.27 | 1.11 | 1129 |
| fast wave | 99 % → 88 % | 114.8 px | 0.26 | 0.88 | 4834 |
| slow wave | 100 % → 73 % | 115.0 px | 0.30 | 0.73 | 8423 |
| spiral | 100 % → 75 % | 65.9 px | 0.29 | 0.75 | 8743 |
| loop | 100 % → 91 % | 129.5 px | 0.29 | 0.91 | 4098 |
| tilted | 55 % → 55 % | 154.5 px | 0.27 | 1.00 | 2217 |
| over the wet one | 92 % → 89 % | 102.9 px | 0.27 | 0.96 | 2231 |
| long, no reload | 100 % → 84 % | 44.8 px | 0.28 | 0.84 | 12829 | quarters: 0.00 → 0.00 → 0.00 → 0.00

Numbers say: light vs heavy: width 213.5 → 218.7 px, dark 0.30 → 0.30; pressure barely changes the width.

## Oil focus · G G x2 fine hairs under
Gouache 0.85 · Ink 0.15 + turpentine 50 % · 220 px · 102.8 s

![Oil focus · G G x2 fine hairs under](Oil-focus-G-G-x2-fine-hairs-under.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 65 % → 63 % | 187.8 px | 0.31 | 0.97 | 1440 |
| heavy line | 66 % → 57 % | 190.4 px | 0.31 | 0.87 | 1449 |
| pressure swell | 55 % → 64 % | 206.0 px | 0.32 | 1.17 | 1063 |
| fast wave | 96 % → 74 % | 111.4 px | 0.33 | 0.77 | 3786 |
| slow wave | 98 % → 60 % | 113.4 px | 0.30 | 0.61 | 6947 |
| spiral | 99 % → 62 % | 65.1 px | 0.31 | 0.63 | 7451 |
| loop | 97 % → 75 % | 126.0 px | 0.31 | 0.77 | 3112 |
| tilted | 49 % → 50 % | 138.1 px | 0.33 | 1.00 | 2183 |
| over the wet one | 87 % → 80 % | 104.4 px | 0.33 | 0.93 | 1381 |
| long, no reload | 100 % → 71 % | 44.8 px | 0.28 | 0.71 | 9473 | quarters: 0.29 → 0.28 → 0.25 → 0.13

Numbers say: light vs heavy: width 187.8 → 190.4 px, dark 0.31 → 0.31; pressure barely changes the width.

## Oil focus · G G x2 fine hairs
Gouache 1.00 + turpentine 15 % · 260 px · 117.6 s

![Oil focus · G G x2 fine hairs](Oil-focus-G-G-x2-fine-hairs.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 73 % → 71 % | 212.2 px | 0.29 | 0.97 | 1594 |
| heavy line | 75 % → 60 % | 216.4 px | 0.29 | 0.80 | 1848 |
| pressure swell | 64 % → 71 % | 241.7 px | 0.26 | 1.10 | 1266 |
| fast wave | 99 % → 84 % | 114.8 px | 0.24 | 0.85 | 5643 |
| slow wave | 100 % → 66 % | 115.0 px | 0.28 | 0.66 | 10736 |
| spiral | 100 % → 72 % | 65.9 px | 0.27 | 0.72 | 8814 |
| loop | 100 % → 87 % | 129.5 px | 0.28 | 0.87 | 4139 |
| tilted | 56 % → 56 % | 156.3 px | 0.25 | 1.00 | 2897 |
| over the wet one | 92 % → 86 % | 100.6 px | 0.25 | 0.93 | 1971 |
| long, no reload | 100 % → 83 % | 44.8 px | 0.27 | 0.83 | 13159 | quarters: 0.00 → 0.00 → 0.00 → 0.00

Numbers say: light vs heavy: width 212.2 → 216.4 px, dark 0.29 → 0.29; pressure barely changes the width.

## Oil focus · H flat x2 soft under
Gouache 0.85 · Ink 0.15 + turpentine 50 % · 220 px · 98.4 s

![Oil focus · H flat x2 soft under](Oil-focus-H-flat-x2-soft-under.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 61 % → 62 % | 178.1 px | 0.33 | 1.00 | 978 |
| heavy line | 63 % → 57 % | 182.7 px | 0.34 | 0.91 | 1934 |
| pressure swell | 52 % → 61 % | 196.4 px | 0.35 | 1.16 | 831 |
| fast wave | 96 % → 83 % | 110.7 px | 0.36 | 0.86 | 3701 |
| slow wave | 97 % → 67 % | 112.6 px | 0.34 | 0.69 | 5663 |
| spiral | 99 % → 72 % | 65.4 px | 0.31 | 0.73 | 5375 |
| loop | 96 % → 83 % | 124.6 px | 0.31 | 0.87 | 2629 |
| tilted | 46 % → 46 % | 129.6 px | 0.35 | 1.00 | 1845 |
| over the wet one | 83 % → 81 % | 103.0 px | 0.35 | 0.97 | 1370 |
| long, no reload | 100 % → 77 % | 44.8 px | 0.30 | 0.77 | 8849 | quarters: 0.31 → 0.31 → 0.29 → 0.18

Numbers say: light vs heavy: width 178.1 → 182.7 px, dark 0.33 → 0.34; pressure barely changes the width.

## Oil focus · H flat x2 soft
Gouache 1.00 + turpentine 15 % · 260 px · 116.7 s

![Oil focus · H flat x2 soft](Oil-focus-H-flat-x2-soft.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 69 % → 69 % | 201.6 px | 0.32 | 0.99 | 1348 |
| heavy line | 71 % → 63 % | 205.0 px | 0.32 | 0.89 | 1587 |
| pressure swell | 62 % → 68 % | 232.8 px | 0.29 | 1.10 | 1357 |
| fast wave | 99 % → 86 % | 114.1 px | 0.27 | 0.87 | 4281 |
| slow wave | 99 % → 73 % | 114.9 px | 0.31 | 0.74 | 8304 |
| spiral | 100 % → 79 % | 65.9 px | 0.30 | 0.79 | 8385 |
| loop | 100 % → 92 % | 129.3 px | 0.31 | 0.92 | 4468 |
| tilted | 53 % → 53 % | 148.2 px | 0.28 | 1.00 | 2865 |
| over the wet one | 89 % → 86 % | 99.3 px | 0.28 | 0.97 | 1890 |
| long, no reload | 100 % → 86 % | 44.8 px | 0.29 | 0.86 | 13508 | quarters: 0.00 → 0.00 → 0.00 → 0.00

Numbers say: light vs heavy: width 201.6 → 205.0 px, dark 0.32 → 0.32; pressure barely changes the width.

## Oil · Henry Ward · Loaded flat
Gouache 1.00 + turpentine 35 % · 84 px · 53.2 s

![Oil · Henry Ward · Loaded flat](Oil-Henry-Ward-Loaded-flat.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 25 % → 20 % | 72.6 px | 0.39 | 0.81 | 290 |
| heavy line | 25 % → 20 % | 71.5 px | 0.40 | 0.82 | 322 |
| pressure swell | 19 % → 18 % | 70.5 px | 0.38 | 0.97 | 229 |
| fast wave | 46 % → 34 % | 53.3 px | 0.36 | 0.73 | 1124 |
| slow wave | 48 % → 36 % | 55.4 px | 0.38 | 0.75 | 1344 |
| spiral | 51 % → 40 % | 33.7 px | 0.38 | 0.78 | 1450 |
| loop | 41 % → 37 % | 52.7 px | 0.38 | 0.91 | 778 |
| tilted | 19 % → 19 % | 53.7 px | 0.36 | 1.01 | 556 |
| over the wet one | 39 % → 38 % | 55.2 px | 0.36 | 0.98 | 377 |
| long, no reload | 63 % → 41 % | 28.2 px | 0.38 | 0.65 | 2305 | quarters: 0.00 → 0.01 → 0.01 → 0.01

Numbers say: light vs heavy: width 72.6 → 71.5 px, dark 0.39 → 0.40; pressure barely changes the width; the long stroke does not run out of paint.

## Oil · Henry Ward · Dry scrub
Gouache 1.00 + turpentine 20 % · 90 px · 37.0 s

![Oil · Henry Ward · Dry scrub](Oil-Henry-Ward-Dry-scrub.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 8 % → 0 % | 21.8 px | 0.00 | 0.00 | 264 |
| heavy line | 14 % → 4 % | 40.5 px | 0.36 | 0.26 | 287 |
| pressure swell | 13 % → 2 % | 47.5 px | 0.31 | 0.14 | 195 |
| fast wave | 53 % → 14 % | 61.0 px | 0.28 | 0.26 | 820 |
| slow wave | 34 % → 12 % | 39.7 px | 0.35 | 0.36 | 1365 |
| spiral | 70 % → 6 % | 46.4 px | 0.33 | 0.09 | 1670 |
| loop | 30 % → 1 % | 39.2 px | 0.31 | 0.04 | 908 |
| tilted | 19 % → 19 % | 53.7 px | 0.27 | 1.00 | 555 |
| over the wet one | 25 % → 10 % | 16.8 px | 0.27 | 0.41 | 293 |
| long, no reload | 45 % → 5 % | 20.1 px | 0.34 | 0.12 | 1857 | quarters: 0.03 → 0.03 → 0.03 → 0.05

Numbers say: light vs heavy: width 21.8 → 40.5 px, dark 0.00 → 0.36; the long stroke does not run out of paint.

## Oil · Henry Ward · Dirty contour
Gouache 1.00 + turpentine 35 % · 34 px · 43.1 s

![Oil · Henry Ward · Dirty contour](Oil-Henry-Ward-Dirty-contour.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 11 % → 10 % | 32.9 px | 0.58 | 0.89 | 104 |
| heavy line | 24 % → 17 % | 68.8 px | 0.58 | 0.71 | 208 |
| pressure swell | 15 % → 11 % | 55.0 px | 0.61 | 0.73 | 155 |
| fast wave | 44 % → 23 % | 50.6 px | 0.60 | 0.52 | 789 |
| slow wave | 41 % → 24 % | 47.8 px | 0.58 | 0.58 | 1329 |
| spiral | 61 % → 27 % | 40.2 px | 0.56 | 0.44 | 833 |
| loop | 37 % → 24 % | 47.5 px | 0.57 | 0.66 | 577 |
| tilted | 14 % → 14 % | 38.0 px | 0.61 | 1.01 | 235 |
| over the wet one | 32 % → 28 % | 51.3 px | 0.61 | 0.87 | 188 |
| long, no reload | 75 % → 30 % | 33.5 px | 0.59 | 0.40 | 1166 | quarters: 0.54 → 0.52 → 0.46 → 0.35

Numbers say: light vs heavy: width 32.9 → 68.8 px, dark 0.58 → 0.58.

## Oil · Henry Ward · Wet drag
Ink 1.00 + turpentine 65 % · 80 px · 47.2 s

![Oil · Henry Ward · Wet drag](Oil-Henry-Ward-Wet-drag.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 25 % → 26 % | 73.9 px | 0.07 | 1.00 | 219 |
| heavy line | 26 % → 26 % | 76.3 px | 0.06 | 0.98 | 327 |
| pressure swell | 19 % → 19 % | 72.4 px | 0.06 | 0.99 | 233 |
| fast wave | 59 % → 59 % | 68.2 px | 0.07 | 0.99 | 704 |
| slow wave | 59 % → 58 % | 68.2 px | 0.06 | 0.98 | 1215 |
| spiral | 77 % → 75 % | 50.8 px | 0.07 | 0.98 | 1264 |
| loop | 54 % → 53 % | 69.6 px | 0.06 | 0.99 | 602 |
| tilted | 20 % → 21 % | 56.3 px | 0.07 | 1.02 | 500 |
| over the wet one | 42 % → 42 % | 61.6 px | 0.07 | 1.00 | 311 |
| long, no reload | 91 % → 91 % | 40.8 px | 0.07 | 1.00 | 2012 | quarters: 0.06 → 0.06 → 0.07 → 0.06

Numbers say: light vs heavy: width 73.9 → 76.3 px, dark 0.07 → 0.06; pressure barely changes the width; the long stroke does not run out of paint.

## Oil · Henry Ward · Thin veil
Watercolour 0.93 · Ink 0.07 + turpentine 80 % · 96 px · 68.3 s

![Oil · Henry Ward · Thin veil](Oil-Henry-Ward-Thin-veil.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 26 % → 28 % | 75.6 px | 0.10 | 1.06 | 261 |
| heavy line | 27 % → 30 % | 77.8 px | 0.10 | 1.10 | 339 |
| pressure swell | 20 % → 23 % | 74.0 px | 0.10 | 1.17 | 314 |
| fast wave | 56 % → 64 % | 64.9 px | 0.10 | 1.13 | 1202 |
| slow wave | 60 % → 66 % | 69.2 px | 0.10 | 1.11 | 1465 |
| spiral | 66 % → 72 % | 43.4 px | 0.10 | 1.10 | 1647 |
| loop | 57 % → 60 % | 74.4 px | 0.10 | 1.05 | 917 |
| tilted | 21 % → 22 % | 59.4 px | 0.10 | 1.02 | 731 |
| over the wet one | 43 % → 47 % | 62.0 px | 0.10 | 1.08 | 686 |
| long, no reload | 83 % → 91 % | 37.0 px | 0.10 | 1.10 | 3221 | quarters: 0.09 → 0.10 → 0.10 → 0.09

Numbers say: light vs heavy: width 75.6 → 77.8 px, dark 0.10 → 0.10; pressure barely changes the width; the long stroke does not run out of paint.

## Oil · Henry Ward · Ground
Ink 0.65 · Watercolour 0.35 + turpentine 75 % · 160 px · 97.9 s

![Oil · Henry Ward · Ground](Oil-Henry-Ward-Ground.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 51 % → 56 % | 148.0 px | 0.06 | 1.10 | 785 |
| heavy line | 53 % → 52 % | 153.8 px | 0.05 | 0.98 | 1165 |
| pressure swell | 41 % → 50 % | 155.4 px | 0.05 | 1.21 | 757 |
| fast wave | 87 % → 93 % | 100.9 px | 0.05 | 1.06 | 2772 |
| slow wave | 87 % → 85 % | 100.7 px | 0.04 | 0.98 | 5960 |
| spiral | 93 % → 92 % | 61.5 px | 0.05 | 0.99 | 7481 |
| loop | 78 % → 78 % | 100.9 px | 0.04 | 1.00 | 2608 |
| tilted | 40 % → 40 % | 110.5 px | 0.05 | 1.01 | 1362 |
| over the wet one | 77 % → 79 % | 103.9 px | 0.05 | 1.03 | 1199 |
| long, no reload | 99 % → 100 % | 44.4 px | 0.04 | 1.01 | 7207 | quarters: 0.01 → 0.02 → 0.04 → 0.07

Numbers say: light vs heavy: width 148.0 → 153.8 px, dark 0.06 → 0.05; pressure barely changes the width; the long stroke does not run out of paint.

## Oil · Henry Ward · HW #02 cream over wet olive
Watercolour 0.93 · Ink 0.07 + turpentine 80 % · 96 px · 76.6 s

![Oil · Henry Ward · HW #02 cream over wet olive](Oil-Henry-Ward-HW-02-cream-over-wet-olive.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 26 % → 28 % | 75.6 px | 0.10 | 1.06 | 433 |
| heavy line | 27 % → 30 % | 77.8 px | 0.11 | 1.10 | 386 |
| pressure swell | 20 % → 23 % | 74.0 px | 0.16 | 1.17 | 328 |
| fast wave | 56 % → 64 % | 64.9 px | 0.15 | 1.13 | 1324 |
| slow wave | 60 % → 66 % | 69.2 px | 0.12 | 1.11 | 3114 |
| spiral | 66 % → 72 % | 43.4 px | 0.13 | 1.10 | 3739 |
| loop | 57 % → 60 % | 74.4 px | 0.12 | 1.05 | 2390 |
| tilted | 21 % → 22 % | 59.4 px | 0.16 | 1.02 | 837 |
| over the wet one | 43 % → 47 % | 62.0 px | 0.16 | 1.08 | 624 |
| long, no reload | 83 % → 91 % | 37.0 px | 0.16 | 1.10 | 4172 | quarters: 0.22 → 0.17 → 0.12 → 0.09

Numbers say: light vs heavy: width 75.6 → 77.8 px, dark 0.10 → 0.11; pressure barely changes the width.

## Oil · Henry Ward · HW #04 grey arcs over ochre
Gouache 1.00 + turpentine 35 % · 84 px · 63.2 s

![Oil · Henry Ward · HW #04 grey arcs over ochre](Oil-Henry-Ward-HW-04-grey-arcs-over-ochre.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 23 % → 21 % | 68.0 px | 0.37 | 0.91 | 468 |
| heavy line | 25 % → 22 % | 71.9 px | 0.35 | 0.90 | 464 |
| pressure swell | 17 % → 18 % | 63.5 px | 0.31 | 1.07 | 302 |
| fast wave | 46 % → 34 % | 52.8 px | 0.26 | 0.73 | 1687 |
| slow wave | 46 % → 34 % | 53.7 px | 0.30 | 0.72 | 2441 |
| spiral | 52 % → 37 % | 34.4 px | 0.25 | 0.71 | 2154 |
| loop | 46 % → 39 % | 59.3 px | 0.30 | 0.85 | 1161 |
| tilted | 19 % → 19 % | 52.1 px | 0.25 | 1.02 | 594 |
| over the wet one | 39 % → 37 % | 55.5 px | 0.25 | 0.95 | 639 |
| long, no reload | 67 % → 40 % | 30.2 px | 0.25 | 0.59 | 2163 | quarters: 0.00 → 0.00 → 0.01 → 0.01

Numbers say: light vs heavy: width 68.0 → 71.9 px, dark 0.37 → 0.35; pressure barely changes the width; the long stroke does not run out of paint.

## Oil · Henry Ward · HW #09 white arches over wet blue-grey
Gouache 1.00 + turpentine 35 % · 84 px · 61.7 s

![Oil · Henry Ward · HW #09 white arches over wet blue-grey](Oil-Henry-Ward-HW-09-white-arches-over-wet-blue-grey.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 25 % → 20 % | 72.6 px | 0.26 | 0.81 | 397 |
| heavy line | 25 % → 20 % | 71.5 px | 0.26 | 0.82 | 463 |
| pressure swell | 19 % → 18 % | 70.5 px | 0.32 | 0.97 | 268 |
| fast wave | 46 % → 34 % | 53.3 px | 0.38 | 0.73 | 1120 |
| slow wave | 48 % → 36 % | 55.4 px | 0.30 | 0.75 | 2257 |
| spiral | 51 % → 40 % | 33.7 px | 0.34 | 0.78 | 2416 |
| loop | 41 % → 37 % | 52.7 px | 0.27 | 0.91 | 955 |
| tilted | 19 % → 19 % | 53.7 px | 0.35 | 1.01 | 831 |
| over the wet one | 39 % → 38 % | 55.2 px | 0.35 | 0.98 | 473 |
| long, no reload | 63 % → 41 % | 28.2 px | 0.37 | 0.65 | 2776 | quarters: 0.34 → 0.27 → 0.21 → 0.14

Numbers say: light vs heavy: width 72.6 → 71.5 px, dark 0.26 → 0.26; pressure barely changes the width.

## Oil · Henry Ward · HW #03 navy contours over wet band
Gouache 1.00 + turpentine 35 % · 84 px · 64.8 s

![Oil · Henry Ward · HW #03 navy contours over wet band](Oil-Henry-Ward-HW-03-navy-contours-over-wet-band.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 25 % → 20 % | 72.6 px | 0.28 | 0.81 | 379 |
| heavy line | 25 % → 20 % | 71.5 px | 0.27 | 0.82 | 409 |
| pressure swell | 19 % → 18 % | 70.5 px | 0.34 | 0.97 | 254 |
| fast wave | 46 % → 34 % | 53.3 px | 0.40 | 0.73 | 1025 |
| slow wave | 48 % → 36 % | 55.4 px | 0.32 | 0.75 | 2115 |
| spiral | 51 % → 40 % | 33.7 px | 0.36 | 0.78 | 2947 |
| loop | 41 % → 37 % | 52.7 px | 0.29 | 0.91 | 879 |
| tilted | 19 % → 19 % | 53.7 px | 0.37 | 1.01 | 504 |
| over the wet one | 39 % → 38 % | 55.2 px | 0.37 | 0.98 | 379 |
| long, no reload | 63 % → 41 % | 28.2 px | 0.39 | 0.65 | 2984 | quarters: 0.35 → 0.28 → 0.22 → 0.15

Numbers say: light vs heavy: width 72.6 → 71.5 px, dark 0.28 → 0.27; pressure barely changes the width.

## Oil · Henry Ward · HW #01 peach cloud and legs over teal
Gouache 1.00 + turpentine 35 % · 84 px · 66.3 s

![Oil · Henry Ward · HW #01 peach cloud and legs over teal](Oil-Henry-Ward-HW-01-peach-cloud-and-legs-over-teal.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 23 % → 21 % | 68.0 px | 0.37 | 0.91 | 394 |
| heavy line | 25 % → 22 % | 71.9 px | 0.35 | 0.90 | 444 |
| pressure swell | 17 % → 18 % | 63.5 px | 0.31 | 1.07 | 338 |
| fast wave | 46 % → 34 % | 52.8 px | 0.26 | 0.73 | 1465 |
| slow wave | 46 % → 34 % | 53.7 px | 0.30 | 0.72 | 1929 |
| spiral | 52 % → 37 % | 34.4 px | 0.25 | 0.71 | 1693 |
| loop | 46 % → 39 % | 59.3 px | 0.30 | 0.85 | 896 |
| tilted | 19 % → 19 % | 52.1 px | 0.26 | 1.02 | 475 |
| over the wet one | 39 % → 37 % | 55.5 px | 0.26 | 0.95 | 609 |
| long, no reload | 67 % → 40 % | 30.2 px | 0.25 | 0.59 | 2532 | quarters: 0.00 → 0.00 → 0.01 → 0.01

Numbers say: light vs heavy: width 68.0 → 71.9 px, dark 0.37 → 0.35; pressure barely changes the width; the long stroke does not run out of paint.

## Oil · Henry Ward · HW #05 rust, pink, green-black
Gouache 1.00 + turpentine 35 % · 84 px · 68.5 s

![Oil · Henry Ward · HW #05 rust, pink, green-black](Oil-Henry-Ward-HW-05-rust-pink-green-black.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 25 % → 20 % | 72.6 px | 0.46 | 0.81 | 400 |
| heavy line | 25 % → 20 % | 71.5 px | 0.45 | 0.82 | 493 |
| pressure swell | 19 % → 18 % | 70.5 px | 0.50 | 0.97 | 345 |
| fast wave | 46 % → 34 % | 53.3 px | 0.56 | 0.73 | 1188 |
| slow wave | 48 % → 36 % | 55.4 px | 0.49 | 0.75 | 1723 |
| spiral | 51 % → 40 % | 33.7 px | 0.53 | 0.78 | 2048 |
| loop | 41 % → 37 % | 52.7 px | 0.46 | 0.91 | 927 |
| tilted | 19 % → 19 % | 53.7 px | 0.53 | 1.01 | 1470 |
| over the wet one | 39 % → 38 % | 55.2 px | 0.53 | 0.98 | 669 |
| long, no reload | 63 % → 41 % | 28.2 px | 0.56 | 0.65 | 3475 | quarters: 0.51 → 0.41 → 0.35 → 0.25

Numbers say: light vs heavy: width 72.6 → 71.5 px, dark 0.46 → 0.45; pressure barely changes the width.

## Oil · Henry Ward · HW #07 blue L and zigzag on lilac
Gouache 1.00 + turpentine 20 % · 90 px · 48.1 s

![Oil · Henry Ward · HW #07 blue L and zigzag on lilac](Oil-Henry-Ward-HW-07-blue-L-and-zigzag-on-lilac.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 8 % → 0 % | 23.4 px | 0.00 | 0.00 | 418 |
| heavy line | 17 % → 6 % | 50.4 px | 0.38 | 0.35 | 509 |
| pressure swell | 15 % → 6 % | 56.1 px | 0.36 | 0.38 | 320 |
| fast wave | 51 % → 9 % | 59.4 px | 0.32 | 0.17 | 1185 |
| slow wave | 40 % → 8 % | 46.5 px | 0.34 | 0.19 | 2434 |
| spiral | 67 % → 7 % | 44.5 px | 0.29 | 0.11 | 2067 |
| loop | 34 % → 1 % | 43.5 px | 0.29 | 0.03 | 957 |
| tilted | 18 % → 19 % | 51.6 px | 0.30 | 1.00 | 593 |
| over the wet one | 27 % → 7 % | 24.6 px | 0.30 | 0.27 | 402 |
| long, no reload | 54 % → 9 % | 24.3 px | 0.30 | 0.17 | 2940 | quarters: 0.03 → 0.02 → 0.03 → 0.05

Numbers say: light vs heavy: width 23.4 → 50.4 px, dark 0.00 → 0.38; the long stroke does not run out of paint.

## Oil · Henry Ward · HW #08 crown and dark oval
Gouache 1.00 + turpentine 35 % · 84 px · 71.7 s

![Oil · Henry Ward · HW #08 crown and dark oval](Oil-Henry-Ward-HW-08-crown-and-dark-oval.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 27 % → 20 % | 78.1 px | 0.14 | 0.76 | 657 |
| heavy line | 35 % → 28 % | 102.9 px | 0.15 | 0.80 | 606 |
| pressure swell | 25 % → 22 % | 93.1 px | 0.21 | 0.89 | 476 |
| fast wave | 55 % → 37 % | 64.1 px | 0.25 | 0.66 | 1350 |
| slow wave | 57 % → 37 % | 66.0 px | 0.16 | 0.64 | 2351 |
| spiral | 62 % → 38 % | 40.6 px | 0.22 | 0.62 | 2814 |
| loop | 49 % → 39 % | 63.3 px | 0.15 | 0.80 | 1373 |
| tilted | 20 % → 20 % | 56.6 px | 0.24 | 1.01 | 710 |
| over the wet one | 48 % → 45 % | 77.5 px | 0.24 | 0.93 | 729 |
| long, no reload | 74 % → 40 % | 33.3 px | 0.26 | 0.54 | 4094 | quarters: 0.26 → 0.21 → 0.13 → 0.07

Numbers say: light vs heavy: width 78.1 → 102.9 px, dark 0.14 → 0.15.

## Oil · Henry Ward · HW #10 green block over maroon
Gouache 1.00 + turpentine 35 % · 84 px · 65.0 s

![Oil · Henry Ward · HW #10 green block over maroon](Oil-Henry-Ward-HW-10-green-block-over-maroon.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 27 % → 20 % | 78.1 px | 0.12 | 0.76 | 610 |
| heavy line | 35 % → 28 % | 102.9 px | 0.12 | 0.80 | 656 |
| pressure swell | 25 % → 22 % | 93.1 px | 0.19 | 0.89 | 448 |
| fast wave | 55 % → 37 % | 64.1 px | 0.23 | 0.66 | 1572 |
| slow wave | 57 % → 37 % | 66.0 px | 0.14 | 0.64 | 2854 |
| spiral | 62 % → 38 % | 40.6 px | 0.20 | 0.62 | 2357 |
| loop | 49 % → 39 % | 63.3 px | 0.13 | 0.80 | 1051 |
| tilted | 20 % → 20 % | 56.6 px | 0.22 | 1.01 | 1078 |
| over the wet one | 48 % → 45 % | 77.5 px | 0.22 | 0.93 | 1510 |
| long, no reload | 74 % → 40 % | 33.3 px | 0.24 | 0.54 | 3531 | quarters: 0.24 → 0.19 → 0.12 → 0.07

Numbers say: light vs heavy: width 78.1 → 102.9 px, dark 0.12 → 0.12.

## Oil · Henry Ward · HW #11 cream mass and purple balls
Gouache 1.00 + turpentine 35 % · 84 px · 61.8 s

![Oil · Henry Ward · HW #11 cream mass and purple balls](Oil-Henry-Ward-HW-11-cream-mass-and-purple-balls.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 25 % → 20 % | 72.6 px | 0.39 | 0.81 | 422 |
| heavy line | 25 % → 20 % | 71.5 px | 0.40 | 0.82 | 453 |
| pressure swell | 19 % → 18 % | 70.5 px | 0.35 | 0.97 | 279 |
| fast wave | 46 % → 34 % | 53.3 px | 0.29 | 0.73 | 1244 |
| slow wave | 48 % → 36 % | 55.4 px | 0.35 | 0.75 | 2278 |
| spiral | 51 % → 40 % | 33.7 px | 0.31 | 0.78 | 2081 |
| loop | 41 % → 37 % | 52.7 px | 0.37 | 0.91 | 1002 |
| tilted | 19 % → 19 % | 53.7 px | 0.32 | 1.01 | 559 |
| over the wet one | 39 % → 38 % | 55.2 px | 0.32 | 0.98 | 825 |
| long, no reload | 63 % → 41 % | 28.2 px | 0.29 | 0.65 | 3086 | quarters: 0.00 → 0.01 → 0.01 → 0.01

Numbers say: light vs heavy: width 72.6 → 71.5 px, dark 0.39 → 0.40; pressure barely changes the width; the long stroke does not run out of paint.

## Oil · Henry Ward · HW #13 blue scrub under red
Gouache 1.00 + turpentine 35 % · 84 px · 63.0 s

![Oil · Henry Ward · HW #13 blue scrub under red](Oil-Henry-Ward-HW-13-blue-scrub-under-red.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 23 % → 21 % | 68.0 px | 0.50 | 0.91 | 430 |
| heavy line | 25 % → 22 % | 71.9 px | 0.53 | 0.90 | 525 |
| pressure swell | 17 % → 18 % | 63.5 px | 0.55 | 1.07 | 284 |
| fast wave | 46 % → 34 % | 52.8 px | 0.58 | 0.73 | 961 |
| slow wave | 46 % → 34 % | 53.7 px | 0.57 | 0.72 | 1613 |
| spiral | 52 % → 37 % | 34.4 px | 0.59 | 0.71 | 1725 |
| loop | 46 % → 39 % | 59.3 px | 0.56 | 0.85 | 1167 |
| tilted | 19 % → 19 % | 52.1 px | 0.59 | 1.02 | 579 |
| over the wet one | 39 % → 37 % | 55.5 px | 0.59 | 0.95 | 523 |
| long, no reload | 67 % → 40 % | 30.2 px | 0.59 | 0.59 | 2632 | quarters: 0.57 → 0.48 → 0.41 → 0.28

Numbers say: light vs heavy: width 68.0 → 71.9 px, dark 0.50 → 0.53; pressure barely changes the width.

## Oil · Henry Ward · HW #14 olive totem on dark
Gouache 1.00 + turpentine 35 % · 84 px · 65.0 s

![Oil · Henry Ward · HW #14 olive totem on dark](Oil-Henry-Ward-HW-14-olive-totem-on-dark.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 27 % → 20 % | 78.1 px | 0.19 | 0.76 | 513 |
| heavy line | 35 % → 28 % | 102.9 px | 0.21 | 0.80 | 586 |
| pressure swell | 25 % → 22 % | 93.1 px | 0.26 | 0.89 | 465 |
| fast wave | 55 % → 37 % | 64.1 px | 0.30 | 0.66 | 1401 |
| slow wave | 57 % → 37 % | 66.0 px | 0.22 | 0.64 | 2714 |
| spiral | 62 % → 38 % | 40.6 px | 0.27 | 0.62 | 2332 |
| loop | 49 % → 39 % | 63.3 px | 0.20 | 0.80 | 1406 |
| tilted | 20 % → 20 % | 56.6 px | 0.29 | 1.01 | 890 |
| over the wet one | 48 % → 45 % | 77.5 px | 0.29 | 0.93 | 987 |
| long, no reload | 74 % → 40 % | 33.3 px | 0.31 | 0.54 | 2953 | quarters: 0.31 → 0.26 → 0.17 → 0.10

Numbers say: light vs heavy: width 78.1 → 102.9 px, dark 0.19 → 0.21.

## Oil · Henry Ward · Ground #2b2f1c flat
Ink 0.65 · Watercolour 0.35 + turpentine 75 % · 160 px · 86.4 s

![Oil · Henry Ward · Ground #2b2f1c flat](Oil-Henry-Ward-Ground-2b2f1c-flat.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 51 % → 56 % | 148.0 px | 0.48 | 1.10 | 658 |
| heavy line | 53 % → 52 % | 153.8 px | 0.53 | 0.98 | 1268 |
| pressure swell | 41 % → 50 % | 155.4 px | 0.53 | 1.21 | 787 |
| fast wave | 87 % → 93 % | 100.9 px | 0.58 | 1.06 | 2865 |
| slow wave | 87 % → 85 % | 100.7 px | 0.60 | 0.98 | 4278 |
| spiral | 93 % → 92 % | 61.5 px | 0.57 | 0.99 | 5044 |
| loop | 78 % → 78 % | 100.9 px | 0.59 | 1.00 | 1813 |
| tilted | 40 % → 40 % | 110.5 px | 0.57 | 1.01 | 1694 |
| over the wet one | 77 % → 79 % | 103.9 px | 0.57 | 1.03 | 1079 |
| long, no reload | 99 % → 100 % | 44.4 px | 0.60 | 1.01 | 5932 | quarters: 0.73 → 0.69 → 0.59 → 0.43

Numbers say: light vs heavy: width 148.0 → 153.8 px, dark 0.48 → 0.53; pressure barely changes the width.

## Oil · Henry Ward · Thin veil #2b3a44 flat
Watercolour 0.93 · Ink 0.07 + turpentine 80 % · 96 px · 75.5 s

![Oil · Henry Ward · Thin veil #2b3a44 flat](Oil-Henry-Ward-Thin-veil-2b3a44-flat.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 26 % → 28 % | 75.6 px | 0.10 | 1.06 | 432 |
| heavy line | 27 % → 30 % | 77.8 px | 0.11 | 1.10 | 416 |
| pressure swell | 20 % → 23 % | 74.0 px | 0.16 | 1.17 | 266 |
| fast wave | 56 % → 64 % | 64.9 px | 0.15 | 1.13 | 929 |
| slow wave | 60 % → 66 % | 69.2 px | 0.12 | 1.11 | 2264 |
| spiral | 66 % → 72 % | 43.4 px | 0.13 | 1.10 | 2529 |
| loop | 57 % → 60 % | 74.4 px | 0.12 | 1.05 | 1594 |
| tilted | 21 % → 22 % | 59.4 px | 0.16 | 1.02 | 749 |
| over the wet one | 43 % → 47 % | 62.0 px | 0.16 | 1.08 | 472 |
| long, no reload | 83 % → 91 % | 37.0 px | 0.16 | 1.10 | 2597 | quarters: 0.22 → 0.17 → 0.12 → 0.09

Numbers say: light vs heavy: width 75.6 → 77.8 px, dark 0.10 → 0.11; pressure barely changes the width.

## Oil · Henry Ward · Loaded flat #ece6c0 flat
Gouache 1.00 + turpentine 30 % · 84 px · 74.6 s

![Oil · Henry Ward · Loaded flat #ece6c0 flat](Oil-Henry-Ward-Loaded-flat-ece6c0-flat.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 25 % → 20 % | 72.6 px | 0.41 | 0.82 | 278 |
| heavy line | 25 % → 20 % | 71.4 px | 0.42 | 0.83 | 343 |
| pressure swell | 19 % → 18 % | 70.5 px | 0.37 | 0.97 | 228 |
| fast wave | 46 % → 33 % | 53.1 px | 0.32 | 0.73 | 1129 |
| slow wave | 48 % → 36 % | 55.1 px | 0.38 | 0.76 | 2018 |
| spiral | 51 % → 40 % | 33.5 px | 0.34 | 0.78 | 2290 |
| loop | 40 % → 37 % | 52.4 px | 0.39 | 0.92 | 1109 |
| tilted | 19 % → 19 % | 53.4 px | 0.34 | 1.01 | 910 |
| over the wet one | 39 % → 38 % | 55.2 px | 0.34 | 0.98 | 586 |
| long, no reload | 61 % → 40 % | 27.3 px | 0.31 | 0.65 | 3576 | quarters: 0.00 → 0.01 → 0.01 → 0.02

Numbers say: light vs heavy: width 72.6 → 71.4 px, dark 0.41 → 0.42; pressure barely changes the width; the long stroke does not run out of paint.

## Oil · Henry Ward · Dry scrub #ece6c0 filbert
Gouache 1.00 + turpentine 20 % · 90 px · 55.5 s

![Oil · Henry Ward · Dry scrub #ece6c0 filbert](Oil-Henry-Ward-Dry-scrub-ece6c0-filbert.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 8 % → 0 % | 23.4 px | 0.00 | 0.00 | 423 |
| heavy line | 17 % → 6 % | 50.4 px | 0.37 | 0.35 | 597 |
| pressure swell | 15 % → 6 % | 56.1 px | 0.35 | 0.38 | 326 |
| fast wave | 51 % → 9 % | 59.4 px | 0.30 | 0.17 | 1985 |
| slow wave | 40 % → 8 % | 46.5 px | 0.32 | 0.19 | 3290 |
| spiral | 67 % → 7 % | 44.5 px | 0.27 | 0.11 | 4204 |
| loop | 34 % → 1 % | 43.5 px | 0.28 | 0.03 | 1176 |
| tilted | 18 % → 19 % | 51.6 px | 0.28 | 1.00 | 769 |
| over the wet one | 27 % → 7 % | 24.6 px | 0.28 | 0.27 | 495 |
| long, no reload | 54 % → 9 % | 24.3 px | 0.28 | 0.17 | 2940 | quarters: 0.03 → 0.02 → 0.03 → 0.05

Numbers say: light vs heavy: width 23.4 → 50.4 px, dark 0.00 → 0.37; the long stroke does not run out of paint.

## Oil · Henry Ward · Ground #8a6a20 flat
Ink 0.65 · Watercolour 0.35 + turpentine 75 % · 160 px · 89.1 s

![Oil · Henry Ward · Ground #8a6a20 flat](Oil-Henry-Ward-Ground-8a6a20-flat.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 51 % → 56 % | 148.0 px | 0.17 | 1.10 | 968 |
| heavy line | 53 % → 52 % | 153.8 px | 0.19 | 0.98 | 1192 |
| pressure swell | 41 % → 50 % | 155.4 px | 0.19 | 1.21 | 933 |
| fast wave | 87 % → 93 % | 100.9 px | 0.22 | 1.06 | 2837 |
| slow wave | 87 % → 85 % | 100.7 px | 0.24 | 0.98 | 5108 |
| spiral | 93 % → 92 % | 61.5 px | 0.23 | 0.99 | 4233 |
| loop | 78 % → 78 % | 100.9 px | 0.23 | 1.00 | 2520 |
| tilted | 40 % → 40 % | 110.5 px | 0.23 | 1.01 | 970 |
| over the wet one | 77 % → 79 % | 103.9 px | 0.23 | 1.03 | 836 |
| long, no reload | 99 % → 100 % | 44.4 px | 0.23 | 1.01 | 6021 | quarters: 0.31 → 0.28 → 0.21 → 0.15

Numbers say: light vs heavy: width 148.0 → 153.8 px, dark 0.17 → 0.19; pressure barely changes the width.

## Oil · Henry Ward · Loaded flat #b8bcc0 filbert
Gouache 1.00 + turpentine 35 % · 84 px · 62.5 s

![Oil · Henry Ward · Loaded flat #b8bcc0 filbert](Oil-Henry-Ward-Loaded-flat-b8bcc0-filbert.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 23 % → 21 % | 68.0 px | 0.37 | 0.91 | 413 |
| heavy line | 25 % → 22 % | 71.9 px | 0.35 | 0.90 | 580 |
| pressure swell | 17 % → 18 % | 63.5 px | 0.31 | 1.07 | 352 |
| fast wave | 46 % → 34 % | 52.8 px | 0.26 | 0.73 | 1282 |
| slow wave | 46 % → 34 % | 53.7 px | 0.30 | 0.72 | 1544 |
| spiral | 52 % → 37 % | 34.4 px | 0.25 | 0.71 | 1560 |
| loop | 46 % → 39 % | 59.3 px | 0.30 | 0.85 | 837 |
| tilted | 19 % → 19 % | 52.1 px | 0.25 | 1.02 | 425 |
| over the wet one | 39 % → 37 % | 55.5 px | 0.25 | 0.95 | 678 |
| long, no reload | 67 % → 40 % | 30.2 px | 0.25 | 0.59 | 2433 | quarters: 0.00 → 0.00 → 0.01 → 0.01

Numbers say: light vs heavy: width 68.0 → 71.9 px, dark 0.37 → 0.35; pressure barely changes the width; the long stroke does not run out of paint.

## Oil · Henry Ward · Dry scrub #c8ccd0 worn
Gouache 1.00 + turpentine 20 % · 90 px · 40.2 s

![Oil · Henry Ward · Dry scrub #c8ccd0 worn](Oil-Henry-Ward-Dry-scrub-c8ccd0-worn.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 17 % → 0 % | 48.9 px | 0.00 | 0.00 | 475 |
| heavy line | 30 % → 1 % | 87.7 px | 0.29 | 0.03 | 517 |
| pressure swell | 21 % → 6 % | 77.3 px | 0.30 | 0.30 | 347 |
| fast wave | 68 % → 7 % | 78.4 px | 0.21 | 0.10 | 1159 |
| slow wave | 51 % → 4 % | 58.9 px | 0.26 | 0.08 | 1898 |
| spiral | 72 % → 10 % | 47.7 px | 0.22 | 0.14 | 1995 |
| loop | 51 % → 0 % | 66.3 px | 0.24 | 0.01 | 1587 |
| tilted | 20 % → 20 % | 57.1 px | 0.21 | 1.00 | 575 |
| over the wet one | 41 % → 9 % | 56.7 px | 0.21 | 0.21 | 417 |
| long, no reload | 80 % → 0 % | 36.0 px | 0.22 | 0.00 | 2378 | quarters: 0.01 → 0.01 → 0.01 → 0.02

Numbers say: light vs heavy: width 48.9 → 87.7 px, dark 0.00 → 0.29; the long stroke does not run out of paint.

## Oil · Henry Ward · Wet drag #9ea4aa flat
Ink 1.00 + turpentine 65 % · 80 px · 64.8 s

![Oil · Henry Ward · Wet drag #9ea4aa flat](Oil-Henry-Ward-Wet-drag-9ea4aa-flat.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 25 % → 26 % | 73.9 px | 0.06 | 1.00 | 305 |
| heavy line | 26 % → 26 % | 76.3 px | 0.07 | 0.98 | 470 |
| pressure swell | 19 % → 19 % | 72.4 px | 0.07 | 0.99 | 388 |
| fast wave | 59 % → 59 % | 68.2 px | 0.09 | 0.99 | 1204 |
| slow wave | 59 % → 58 % | 68.2 px | 0.07 | 0.98 | 2450 |
| spiral | 77 % → 75 % | 50.8 px | 0.08 | 0.98 | 1757 |
| loop | 54 % → 53 % | 69.6 px | 0.08 | 0.99 | 872 |
| tilted | 20 % → 21 % | 56.3 px | 0.08 | 1.02 | 585 |
| over the wet one | 42 % → 42 % | 61.6 px | 0.08 | 1.00 | 522 |
| long, no reload | 91 % → 91 % | 40.8 px | 0.08 | 1.00 | 2761 | quarters: 0.08 → 0.08 → 0.08 → 0.07

Numbers say: light vs heavy: width 73.9 → 76.3 px, dark 0.06 → 0.07; pressure barely changes the width.

## Oil · Henry Ward · Ground #e8b4a8 flat
Ink 0.65 · Watercolour 0.35 + turpentine 75 % · 160 px · 81.7 s

![Oil · Henry Ward · Ground #e8b4a8 flat](Oil-Henry-Ward-Ground-e8b4a8-flat.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 51 % → 56 % | 148.0 px | 0.06 | 1.10 | 772 |
| heavy line | 53 % → 52 % | 153.8 px | 0.05 | 0.98 | 1461 |
| pressure swell | 41 % → 50 % | 155.4 px | 0.05 | 1.21 | 627 |
| fast wave | 87 % → 93 % | 100.9 px | 0.04 | 1.06 | 2391 |
| slow wave | 87 % → 85 % | 100.7 px | 0.04 | 0.98 | 4397 |
| spiral | 93 % → 92 % | 61.5 px | 0.05 | 0.99 | 4392 |
| loop | 78 % → 78 % | 100.9 px | 0.04 | 1.00 | 2239 |
| tilted | 40 % → 40 % | 110.5 px | 0.05 | 1.01 | 1548 |
| over the wet one | 77 % → 79 % | 103.9 px | 0.05 | 1.03 | 1076 |
| long, no reload | 99 % → 100 % | 44.4 px | 0.04 | 1.01 | 5968 | quarters: 0.00 → 0.01 → 0.04 → 0.07

Numbers say: light vs heavy: width 148.0 → 153.8 px, dark 0.06 → 0.05; pressure barely changes the width; the long stroke does not run out of paint.

## Oil · Henry Ward · Loaded flat #6e7f90 flat
Gouache 1.00 + turpentine 35 % · 84 px · 61.1 s

![Oil · Henry Ward · Loaded flat #6e7f90 flat](Oil-Henry-Ward-Loaded-flat-6e7f90-flat.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 25 % → 20 % | 72.6 px | 0.26 | 0.81 | 291 |
| heavy line | 25 % → 20 % | 71.5 px | 0.26 | 0.82 | 484 |
| pressure swell | 19 % → 18 % | 70.5 px | 0.32 | 0.97 | 335 |
| fast wave | 46 % → 34 % | 53.3 px | 0.38 | 0.73 | 1145 |
| slow wave | 48 % → 36 % | 55.4 px | 0.30 | 0.75 | 2702 |
| spiral | 51 % → 40 % | 33.7 px | 0.34 | 0.78 | 2099 |
| loop | 41 % → 37 % | 52.7 px | 0.27 | 0.91 | 1141 |
| tilted | 19 % → 19 % | 53.7 px | 0.35 | 1.01 | 596 |
| over the wet one | 39 % → 38 % | 55.2 px | 0.35 | 0.98 | 559 |
| long, no reload | 63 % → 41 % | 28.2 px | 0.37 | 0.65 | 3244 | quarters: 0.34 → 0.27 → 0.21 → 0.14

Numbers say: light vs heavy: width 72.6 → 71.5 px, dark 0.26 → 0.26; pressure barely changes the width.

## Oil · Henry Ward · Loaded flat #f6f6f2 filbert
Gouache 1.00 + turpentine 30 % · 84 px · 52.2 s

![Oil · Henry Ward · Loaded flat #f6f6f2 filbert](Oil-Henry-Ward-Loaded-flat-f6f6f2-filbert.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 23 % → 21 % | 68.0 px | 0.44 | 0.91 | 339 |
| heavy line | 25 % → 22 % | 71.7 px | 0.44 | 0.91 | 387 |
| pressure swell | 17 % → 18 % | 63.2 px | 0.40 | 1.09 | 267 |
| fast wave | 46 % → 34 % | 52.6 px | 0.37 | 0.75 | 1152 |
| slow wave | 46 % → 33 % | 53.2 px | 0.40 | 0.73 | 1898 |
| spiral | 52 % → 37 % | 34.0 px | 0.36 | 0.72 | 1675 |
| loop | 45 % → 39 % | 58.9 px | 0.40 | 0.85 | 932 |
| tilted | 18 % → 19 % | 51.5 px | 0.37 | 1.02 | 390 |
| over the wet one | 38 % → 36 % | 55.6 px | 0.37 | 0.95 | 418 |
| long, no reload | 66 % → 39 % | 29.4 px | 0.35 | 0.60 | 2235 | quarters: 0.00 → 0.01 → 0.01 → 0.02

Numbers say: light vs heavy: width 68.0 → 71.7 px, dark 0.44 → 0.44; pressure barely changes the width; the long stroke does not run out of paint.

## Oil · Henry Ward · Dry scrub #f6f6f2 filbert
Gouache 1.00 + turpentine 20 % · 90 px · 38.1 s

![Oil · Henry Ward · Dry scrub #f6f6f2 filbert](Oil-Henry-Ward-Dry-scrub-f6f6f2-filbert.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 8 % → 0 % | 23.4 px | 0.00 | 0.00 | 284 |
| heavy line | 17 % → 6 % | 50.4 px | 0.38 | 0.35 | 359 |
| pressure swell | 15 % → 6 % | 56.1 px | 0.36 | 0.38 | 295 |
| fast wave | 51 % → 9 % | 59.4 px | 0.32 | 0.17 | 942 |
| slow wave | 40 % → 8 % | 46.5 px | 0.34 | 0.19 | 1590 |
| spiral | 67 % → 7 % | 44.5 px | 0.30 | 0.11 | 1826 |
| loop | 34 % → 1 % | 43.5 px | 0.30 | 0.03 | 771 |
| tilted | 18 % → 19 % | 51.6 px | 0.30 | 1.00 | 459 |
| over the wet one | 27 % → 7 % | 24.6 px | 0.30 | 0.27 | 337 |
| long, no reload | 54 % → 9 % | 24.3 px | 0.30 | 0.17 | 2042 | quarters: 0.03 → 0.02 → 0.03 → 0.05

Numbers say: light vs heavy: width 23.4 → 50.4 px, dark 0.00 → 0.38; the long stroke does not run out of paint.

## Oil · Henry Ward · Ground #e8e2da flat
Gouache 1.00 + turpentine 30 % · 160 px · 78.8 s

![Oil · Henry Ward · Ground #e8e2da flat](Oil-Henry-Ward-Ground-e8e2da-flat.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 51 % → 43 % | 148.1 px | 0.36 | 0.84 | 740 |
| heavy line | 52 % → 45 % | 151.1 px | 0.37 | 0.87 | 872 |
| pressure swell | 41 % → 43 % | 154.5 px | 0.36 | 1.04 | 653 |
| fast wave | 85 % → 82 % | 97.7 px | 0.36 | 0.97 | 2996 |
| slow wave | 86 % → 68 % | 99.0 px | 0.36 | 0.80 | 4016 |
| spiral | 88 % → 62 % | 58.2 px | 0.36 | 0.70 | 4060 |
| loop | 75 % → 67 % | 96.9 px | 0.37 | 0.89 | 1801 |
| tilted | 38 % → 38 % | 107.0 px | 0.36 | 1.00 | 1358 |
| over the wet one | 76 % → 68 % | 104.8 px | 0.36 | 0.90 | 909 |
| long, no reload | 98 % → 81 % | 44.0 px | 0.36 | 0.83 | 6117 | quarters: 0.00 → 0.00 → 0.00 → 0.00

Numbers say: light vs heavy: width 148.1 → 151.1 px, dark 0.36 → 0.37; pressure barely changes the width.

## Oil · Henry Ward · Loaded flat #6a7a80 flat
Gouache 1.00 + turpentine 35 % · 84 px · 53.9 s

![Oil · Henry Ward · Loaded flat #6a7a80 flat](Oil-Henry-Ward-Loaded-flat-6a7a80-flat.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 25 % → 20 % | 72.6 px | 0.28 | 0.81 | 422 |
| heavy line | 25 % → 20 % | 71.5 px | 0.27 | 0.82 | 348 |
| pressure swell | 19 % → 18 % | 70.5 px | 0.34 | 0.97 | 228 |
| fast wave | 46 % → 34 % | 53.3 px | 0.40 | 0.73 | 795 |
| slow wave | 48 % → 36 % | 55.4 px | 0.32 | 0.75 | 1798 |
| spiral | 51 % → 40 % | 33.7 px | 0.36 | 0.78 | 2067 |
| loop | 41 % → 37 % | 52.7 px | 0.29 | 0.91 | 1134 |
| tilted | 19 % → 19 % | 53.7 px | 0.37 | 1.01 | 446 |
| over the wet one | 39 % → 38 % | 55.2 px | 0.37 | 0.98 | 357 |
| long, no reload | 63 % → 41 % | 28.2 px | 0.39 | 0.65 | 2213 | quarters: 0.35 → 0.28 → 0.22 → 0.15

Numbers say: light vs heavy: width 72.6 → 71.5 px, dark 0.28 → 0.27; pressure barely changes the width.

## Oil · Henry Ward · Loaded flat #5a1810 flat
Gouache 1.00 + turpentine 35 % · 84 px · 57.0 s

![Oil · Henry Ward · Loaded flat #5a1810 flat](Oil-Henry-Ward-Loaded-flat-5a1810-flat.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 25 % → 20 % | 72.6 px | 0.62 | 0.81 | 400 |
| heavy line | 25 % → 20 % | 71.5 px | 0.62 | 0.82 | 352 |
| pressure swell | 19 % → 18 % | 70.5 px | 0.64 | 0.97 | 467 |
| fast wave | 46 % → 34 % | 53.3 px | 0.67 | 0.73 | 1818 |
| slow wave | 48 % → 36 % | 55.4 px | 0.64 | 0.75 | 1523 |
| spiral | 51 % → 40 % | 33.7 px | 0.65 | 0.78 | 1600 |
| loop | 41 % → 37 % | 52.7 px | 0.62 | 0.91 | 953 |
| tilted | 19 % → 19 % | 53.7 px | 0.66 | 1.01 | 468 |
| over the wet one | 39 % → 38 % | 55.2 px | 0.66 | 0.98 | 498 |
| long, no reload | 63 % → 41 % | 28.2 px | 0.67 | 0.65 | 2270 | quarters: 0.61 → 0.50 → 0.43 → 0.32

Numbers say: light vs heavy: width 72.6 → 71.5 px, dark 0.62 → 0.62; pressure barely changes the width.

## Oil · Henry Ward · Dirty contour #1c2240 flat
Gouache 1.00 + turpentine 35 % · 34 px · 43.5 s

![Oil · Henry Ward · Dirty contour #1c2240 flat](Oil-Henry-Ward-Dirty-contour-1c2240-flat.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 11 % → 10 % | 32.9 px | 0.55 | 0.89 | 143 |
| heavy line | 24 % → 17 % | 68.8 px | 0.55 | 0.71 | 367 |
| pressure swell | 15 % → 11 % | 55.0 px | 0.59 | 0.73 | 162 |
| fast wave | 44 % → 23 % | 50.6 px | 0.64 | 0.52 | 492 |
| slow wave | 41 % → 24 % | 47.8 px | 0.59 | 0.58 | 848 |
| spiral | 61 % → 27 % | 40.2 px | 0.61 | 0.44 | 963 |
| loop | 37 % → 24 % | 47.5 px | 0.58 | 0.66 | 432 |
| tilted | 14 % → 14 % | 38.0 px | 0.63 | 1.01 | 218 |
| over the wet one | 32 % → 28 % | 51.3 px | 0.63 | 0.87 | 225 |
| long, no reload | 75 % → 30 % | 33.5 px | 0.62 | 0.40 | 1228 | quarters: 0.57 → 0.55 → 0.50 → 0.39

Numbers say: light vs heavy: width 32.9 → 68.8 px, dark 0.55 → 0.55.

## Oil · Henry Ward · Ground #22403f flat
Ink 0.65 · Watercolour 0.35 + turpentine 75 % · 160 px · 75.8 s

![Oil · Henry Ward · Ground #22403f flat](Oil-Henry-Ward-Ground-22403f-flat.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 51 % → 56 % | 148.0 px | 0.38 | 1.10 | 547 |
| heavy line | 53 % → 52 % | 153.8 px | 0.42 | 0.98 | 1001 |
| pressure swell | 41 % → 50 % | 155.4 px | 0.43 | 1.21 | 584 |
| fast wave | 87 % → 93 % | 100.9 px | 0.47 | 1.06 | 2011 |
| slow wave | 87 % → 85 % | 100.7 px | 0.50 | 0.98 | 3456 |
| spiral | 93 % → 92 % | 61.5 px | 0.48 | 0.99 | 3330 |
| loop | 78 % → 78 % | 100.9 px | 0.48 | 1.00 | 1620 |
| tilted | 40 % → 40 % | 110.5 px | 0.47 | 1.01 | 1801 |
| over the wet one | 77 % → 79 % | 103.9 px | 0.47 | 1.03 | 1002 |
| long, no reload | 99 % → 100 % | 44.4 px | 0.49 | 1.01 | 6253 | quarters: 0.63 → 0.58 → 0.47 → 0.33

Numbers say: light vs heavy: width 148.0 → 153.8 px, dark 0.38 → 0.42; pressure barely changes the width.

## Oil · Henry Ward · Loaded flat #f0b89a filbert
Gouache 1.00 + turpentine 35 % · 84 px · 55.3 s

![Oil · Henry Ward · Loaded flat #f0b89a filbert](Oil-Henry-Ward-Loaded-flat-f0b89a-filbert.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 23 % → 21 % | 68.0 px | 0.37 | 0.91 | 342 |
| heavy line | 25 % → 22 % | 71.9 px | 0.35 | 0.90 | 355 |
| pressure swell | 17 % → 18 % | 63.5 px | 0.31 | 1.07 | 254 |
| fast wave | 46 % → 34 % | 52.8 px | 0.26 | 0.73 | 845 |
| slow wave | 46 % → 34 % | 53.7 px | 0.30 | 0.72 | 1423 |
| spiral | 52 % → 37 % | 34.4 px | 0.25 | 0.71 | 1757 |
| loop | 46 % → 39 % | 59.3 px | 0.30 | 0.85 | 865 |
| tilted | 19 % → 19 % | 52.1 px | 0.26 | 1.02 | 417 |
| over the wet one | 39 % → 37 % | 55.5 px | 0.26 | 0.95 | 382 |
| long, no reload | 67 % → 40 % | 30.2 px | 0.25 | 0.59 | 2890 | quarters: 0.00 → 0.00 → 0.01 → 0.01

Numbers say: light vs heavy: width 68.0 → 71.9 px, dark 0.37 → 0.35; pressure barely changes the width; the long stroke does not run out of paint.

## Oil · Henry Ward · Dry scrub #f0b89a filbert
Gouache 1.00 + turpentine 20 % · 90 px · 38.9 s

![Oil · Henry Ward · Dry scrub #f0b89a filbert](Oil-Henry-Ward-Dry-scrub-f0b89a-filbert.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 8 % → 0 % | 23.4 px | 0.00 | 0.00 | 370 |
| heavy line | 17 % → 6 % | 50.4 px | 0.33 | 0.36 | 478 |
| pressure swell | 15 % → 6 % | 56.2 px | 0.31 | 0.37 | 337 |
| fast wave | 51 % → 8 % | 59.4 px | 0.25 | 0.16 | 1243 |
| slow wave | 40 % → 7 % | 46.5 px | 0.27 | 0.18 | 2185 |
| spiral | 68 % → 7 % | 44.6 px | 0.21 | 0.11 | 2123 |
| loop | 34 % → 1 % | 43.5 px | 0.22 | 0.03 | 720 |
| tilted | 18 % → 19 % | 51.6 px | 0.21 | 1.00 | 421 |
| over the wet one | 27 % → 7 % | 24.7 px | 0.21 | 0.26 | 301 |
| long, no reload | 54 % → 9 % | 24.4 px | 0.21 | 0.17 | 1809 | quarters: 0.03 → 0.01 → 0.02 → 0.04

Numbers say: light vs heavy: width 23.4 → 50.4 px, dark 0.00 → 0.33; the long stroke does not run out of paint.

## Oil · Henry Ward · Dirty contour #1c2238 flat
Gouache 1.00 + turpentine 35 % · 34 px · 43.5 s

![Oil · Henry Ward · Dirty contour #1c2238 flat](Oil-Henry-Ward-Dirty-contour-1c2238-flat.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 11 % → 10 % | 32.9 px | 0.55 | 0.89 | 162 |
| heavy line | 24 % → 17 % | 68.8 px | 0.55 | 0.71 | 353 |
| pressure swell | 15 % → 11 % | 55.0 px | 0.59 | 0.73 | 214 |
| fast wave | 44 % → 23 % | 50.6 px | 0.64 | 0.52 | 578 |
| slow wave | 41 % → 24 % | 47.8 px | 0.60 | 0.58 | 802 |
| spiral | 61 % → 27 % | 40.2 px | 0.61 | 0.44 | 880 |
| loop | 37 % → 24 % | 47.5 px | 0.58 | 0.66 | 449 |
| tilted | 14 % → 14 % | 38.0 px | 0.63 | 1.01 | 211 |
| over the wet one | 32 % → 28 % | 51.3 px | 0.63 | 0.87 | 249 |
| long, no reload | 75 % → 30 % | 33.5 px | 0.63 | 0.40 | 1605 | quarters: 0.58 → 0.56 → 0.50 → 0.39

Numbers say: light vs heavy: width 32.9 → 68.8 px, dark 0.55 → 0.55.

## Oil · Henry Ward · Ground #ece8e2 flat
Gouache 1.00 + turpentine 30 % · 160 px · 77.9 s

![Oil · Henry Ward · Ground #ece8e2 flat](Oil-Henry-Ward-Ground-ece8e2-flat.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 51 % → 43 % | 148.1 px | 0.37 | 0.84 | 680 |
| heavy line | 52 % → 45 % | 151.1 px | 0.38 | 0.87 | 785 |
| pressure swell | 41 % → 43 % | 154.5 px | 0.37 | 1.04 | 582 |
| fast wave | 85 % → 82 % | 97.7 px | 0.37 | 0.97 | 2206 |
| slow wave | 86 % → 68 % | 99.0 px | 0.37 | 0.80 | 5788 |
| spiral | 88 % → 62 % | 58.2 px | 0.37 | 0.70 | 5518 |
| loop | 75 % → 67 % | 96.9 px | 0.38 | 0.89 | 1711 |
| tilted | 38 % → 38 % | 107.0 px | 0.37 | 1.00 | 1034 |
| over the wet one | 76 % → 68 % | 104.8 px | 0.37 | 0.90 | 1003 |
| long, no reload | 98 % → 81 % | 44.0 px | 0.37 | 0.83 | 5815 | quarters: 0.00 → 0.00 → 0.00 → 0.00

Numbers say: light vs heavy: width 148.1 → 151.1 px, dark 0.37 → 0.38; pressure barely changes the width.

## Oil · Henry Ward · Loaded flat #a03c1c flat
Gouache 1.00 + turpentine 35 % · 84 px · 52.6 s

![Oil · Henry Ward · Loaded flat #a03c1c flat](Oil-Henry-Ward-Loaded-flat-a03c1c-flat.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 25 % → 20 % | 72.6 px | 0.46 | 0.81 | 305 |
| heavy line | 25 % → 20 % | 71.5 px | 0.45 | 0.82 | 328 |
| pressure swell | 19 % → 18 % | 70.5 px | 0.50 | 0.97 | 222 |
| fast wave | 46 % → 34 % | 53.3 px | 0.56 | 0.73 | 834 |
| slow wave | 48 % → 36 % | 55.4 px | 0.49 | 0.75 | 1492 |
| spiral | 51 % → 40 % | 33.7 px | 0.53 | 0.78 | 2408 |
| loop | 41 % → 37 % | 52.7 px | 0.46 | 0.91 | 1359 |
| tilted | 19 % → 19 % | 53.7 px | 0.53 | 1.01 | 849 |
| over the wet one | 39 % → 38 % | 55.2 px | 0.53 | 0.98 | 627 |
| long, no reload | 63 % → 41 % | 28.2 px | 0.56 | 0.65 | 2366 | quarters: 0.51 → 0.41 → 0.35 → 0.25

Numbers say: light vs heavy: width 72.6 → 71.5 px, dark 0.46 → 0.45; pressure barely changes the width.

## Oil · Henry Ward · Dirty contour #1f3a2c flat
Gouache 1.00 + turpentine 35 % · 34 px · 38.7 s

![Oil · Henry Ward · Dirty contour #1f3a2c flat](Oil-Henry-Ward-Dirty-contour-1f3a2c-flat.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 11 % → 10 % | 32.9 px | 0.49 | 0.89 | 112 |
| heavy line | 24 % → 17 % | 68.8 px | 0.49 | 0.71 | 223 |
| pressure swell | 15 % → 11 % | 55.0 px | 0.53 | 0.73 | 201 |
| fast wave | 44 % → 23 % | 50.6 px | 0.58 | 0.52 | 488 |
| slow wave | 41 % → 24 % | 47.8 px | 0.53 | 0.58 | 938 |
| spiral | 61 % → 27 % | 40.2 px | 0.55 | 0.44 | 880 |
| loop | 37 % → 24 % | 47.5 px | 0.52 | 0.66 | 442 |
| tilted | 14 % → 14 % | 38.0 px | 0.58 | 1.01 | 212 |
| over the wet one | 32 % → 28 % | 51.3 px | 0.58 | 0.87 | 213 |
| long, no reload | 75 % → 30 % | 33.5 px | 0.57 | 0.40 | 1236 | quarters: 0.52 → 0.50 → 0.44 → 0.33

Numbers say: light vs heavy: width 32.9 → 68.8 px, dark 0.49 → 0.49.

## Oil · Henry Ward · Loaded flat #ecc8c8 worn
Gouache 1.00 + turpentine 35 % · 84 px · 66.2 s

![Oil · Henry Ward · Loaded flat #ecc8c8 worn](Oil-Henry-Ward-Loaded-flat-ecc8c8-worn.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 27 % → 20 % | 78.1 px | 0.36 | 0.76 | 396 |
| heavy line | 35 % → 28 % | 102.9 px | 0.35 | 0.80 | 459 |
| pressure swell | 25 % → 22 % | 93.1 px | 0.31 | 0.89 | 487 |
| fast wave | 55 % → 37 % | 64.1 px | 0.27 | 0.66 | 1078 |
| slow wave | 57 % → 37 % | 66.0 px | 0.33 | 0.64 | 1873 |
| spiral | 62 % → 38 % | 40.6 px | 0.29 | 0.62 | 1876 |
| loop | 49 % → 39 % | 63.3 px | 0.34 | 0.80 | 989 |
| tilted | 20 % → 20 % | 56.6 px | 0.28 | 1.01 | 565 |
| over the wet one | 48 % → 45 % | 77.5 px | 0.28 | 0.93 | 499 |
| long, no reload | 74 % → 40 % | 33.3 px | 0.26 | 0.54 | 2927 | quarters: 0.00 → 0.00 → 0.01 → 0.02

Numbers say: light vs heavy: width 78.1 → 102.9 px, dark 0.36 → 0.35; the long stroke does not run out of paint.

## Oil · Henry Ward · Loaded flat #62c8e8 flat
Gouache 1.00 + turpentine 35 % · 84 px · 70.3 s

![Oil · Henry Ward · Loaded flat #62c8e8 flat](Oil-Henry-Ward-Loaded-flat-62c8e8-flat.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 25 % → 20 % | 72.6 px | 0.29 | 0.81 | 280 |
| heavy line | 25 % → 20 % | 71.5 px | 0.30 | 0.82 | 311 |
| pressure swell | 19 % → 18 % | 70.5 px | 0.24 | 0.97 | 304 |
| fast wave | 46 % → 34 % | 53.3 px | 0.18 | 0.73 | 757 |
| slow wave | 48 % → 36 % | 55.4 px | 0.25 | 0.75 | 1416 |
| spiral | 51 % → 40 % | 33.7 px | 0.21 | 0.78 | 2240 |
| loop | 41 % → 37 % | 52.7 px | 0.28 | 0.91 | 893 |
| tilted | 19 % → 19 % | 53.7 px | 0.21 | 1.01 | 579 |
| over the wet one | 39 % → 38 % | 55.2 px | 0.21 | 0.98 | 358 |
| long, no reload | 63 % → 41 % | 28.2 px | 0.18 | 0.65 | 2122 | quarters: 0.00 → 0.00 → 0.01 → 0.01

Numbers say: light vs heavy: width 72.6 → 71.5 px, dark 0.29 → 0.30; pressure barely changes the width; the long stroke does not run out of paint.

## Oil · Henry Ward · Loaded flat #0f2018 flat
Gouache 1.00 + turpentine 35 % · 84 px · 70.5 s

![Oil · Henry Ward · Loaded flat #0f2018 flat](Oil-Henry-Ward-Loaded-flat-0f2018-flat.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 25 % → 20 % | 72.6 px | 0.64 | 0.81 | 302 |
| heavy line | 25 % → 20 % | 71.5 px | 0.64 | 0.82 | 476 |
| pressure swell | 19 % → 18 % | 70.5 px | 0.68 | 0.97 | 256 |
| fast wave | 46 % → 34 % | 53.3 px | 0.72 | 0.73 | 782 |
| slow wave | 48 % → 36 % | 55.4 px | 0.67 | 0.75 | 1382 |
| spiral | 51 % → 40 % | 33.7 px | 0.70 | 0.78 | 2131 |
| loop | 41 % → 37 % | 52.7 px | 0.65 | 0.91 | 2248 |
| tilted | 19 % → 19 % | 53.7 px | 0.70 | 1.01 | 753 |
| over the wet one | 39 % → 38 % | 55.2 px | 0.70 | 0.98 | 626 |
| long, no reload | 63 % → 41 % | 28.2 px | 0.72 | 0.65 | 3166 | quarters: 0.65 → 0.54 → 0.47 → 0.35

Numbers say: light vs heavy: width 72.6 → 71.5 px, dark 0.64 → 0.64; pressure barely changes the width.

## Oil · Henry Ward · Ground #e6e2ee flat
Gouache 1.00 + turpentine 30 % · 160 px · 99.5 s

![Oil · Henry Ward · Ground #e6e2ee flat](Oil-Henry-Ward-Ground-e6e2ee-flat.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 51 % → 43 % | 148.1 px | 0.37 | 0.84 | 931 |
| heavy line | 52 % → 45 % | 151.1 px | 0.37 | 0.87 | 1302 |
| pressure swell | 41 % → 43 % | 154.5 px | 0.36 | 1.04 | 760 |
| fast wave | 85 % → 82 % | 97.7 px | 0.36 | 0.97 | 3241 |
| slow wave | 86 % → 68 % | 99.0 px | 0.37 | 0.80 | 5403 |
| spiral | 88 % → 62 % | 58.2 px | 0.37 | 0.70 | 5702 |
| loop | 75 % → 67 % | 96.9 px | 0.37 | 0.89 | 2304 |
| tilted | 38 % → 38 % | 107.0 px | 0.37 | 1.00 | 1422 |
| over the wet one | 76 % → 68 % | 104.8 px | 0.37 | 0.90 | 1636 |
| long, no reload | 98 % → 81 % | 44.0 px | 0.36 | 0.83 | 10066 | quarters: 0.00 → 0.00 → 0.00 → 0.00

Numbers say: light vs heavy: width 148.1 → 151.1 px, dark 0.37 → 0.37; pressure barely changes the width.

## Oil · Henry Ward · Dry scrub #f2f0f6 filbert
Gouache 1.00 + turpentine 20 % · 90 px · 51.0 s

![Oil · Henry Ward · Dry scrub #f2f0f6 filbert](Oil-Henry-Ward-Dry-scrub-f2f0f6-filbert.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 8 % → 0 % | 23.4 px | 0.00 | 0.00 | 349 |
| heavy line | 17 % → 6 % | 50.4 px | 0.38 | 0.35 | 464 |
| pressure swell | 15 % → 6 % | 56.1 px | 0.36 | 0.38 | 342 |
| fast wave | 51 % → 9 % | 59.4 px | 0.32 | 0.17 | 1341 |
| slow wave | 40 % → 8 % | 46.5 px | 0.34 | 0.19 | 2405 |
| spiral | 67 % → 7 % | 44.5 px | 0.29 | 0.11 | 2143 |
| loop | 34 % → 1 % | 43.5 px | 0.29 | 0.03 | 1165 |
| tilted | 18 % → 19 % | 51.6 px | 0.30 | 1.00 | 623 |
| over the wet one | 27 % → 7 % | 24.6 px | 0.30 | 0.27 | 517 |
| long, no reload | 54 % → 9 % | 24.3 px | 0.30 | 0.17 | 2434 | quarters: 0.03 → 0.02 → 0.03 → 0.05

Numbers say: light vs heavy: width 23.4 → 50.4 px, dark 0.00 → 0.38; the long stroke does not run out of paint.

## Oil · Henry Ward · Dirty contour #1e4a78 flat
Gouache 1.00 + turpentine 35 % · 34 px · 51.4 s

![Oil · Henry Ward · Dirty contour #1e4a78 flat](Oil-Henry-Ward-Dirty-contour-1e4a78-flat.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 11 % → 10 % | 32.9 px | 0.43 | 0.89 | 158 |
| heavy line | 24 % → 17 % | 68.8 px | 0.43 | 0.71 | 317 |
| pressure swell | 15 % → 11 % | 55.0 px | 0.48 | 0.73 | 271 |
| fast wave | 44 % → 23 % | 50.6 px | 0.54 | 0.52 | 620 |
| slow wave | 41 % → 24 % | 47.8 px | 0.48 | 0.58 | 1351 |
| spiral | 61 % → 27 % | 40.2 px | 0.50 | 0.44 | 1061 |
| loop | 37 % → 24 % | 47.5 px | 0.46 | 0.66 | 1114 |
| tilted | 14 % → 14 % | 38.0 px | 0.53 | 1.01 | 516 |
| over the wet one | 32 % → 28 % | 51.3 px | 0.53 | 0.87 | 292 |
| long, no reload | 75 % → 30 % | 33.5 px | 0.52 | 0.40 | 1840 | quarters: 0.47 → 0.45 → 0.38 → 0.27

Numbers say: light vs heavy: width 32.9 → 68.8 px, dark 0.43 → 0.43.

## Oil · Henry Ward · Dirty contour #141414 flat
Gouache 1.00 + turpentine 35 % · 34 px · 48.9 s

![Oil · Henry Ward · Dirty contour #141414 flat](Oil-Henry-Ward-Dirty-contour-141414-flat.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 11 % → 10 % | 32.9 px | 0.62 | 0.89 | 128 |
| heavy line | 24 % → 17 % | 68.8 px | 0.62 | 0.71 | 243 |
| pressure swell | 15 % → 11 % | 55.0 px | 0.65 | 0.73 | 201 |
| fast wave | 44 % → 23 % | 50.6 px | 0.68 | 0.52 | 618 |
| slow wave | 41 % → 24 % | 47.8 px | 0.65 | 0.58 | 1036 |
| spiral | 61 % → 27 % | 40.2 px | 0.66 | 0.44 | 967 |
| loop | 37 % → 24 % | 47.5 px | 0.64 | 0.66 | 529 |
| tilted | 14 % → 14 % | 38.0 px | 0.68 | 1.01 | 252 |
| over the wet one | 32 % → 28 % | 51.3 px | 0.68 | 0.87 | 228 |
| long, no reload | 75 % → 30 % | 33.5 px | 0.68 | 0.40 | 1684 | quarters: 0.62 → 0.60 → 0.55 → 0.44

Numbers say: light vs heavy: width 32.9 → 68.8 px, dark 0.62 → 0.62.

## Oil · Henry Ward · Dry scrub #c89038 filbert
Gouache 1.00 + turpentine 20 % · 90 px · 45.3 s

![Oil · Henry Ward · Dry scrub #c89038 filbert](Oil-Henry-Ward-Dry-scrub-c89038-filbert.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 8 % → 0 % | 23.4 px | 0.00 | 0.00 | 268 |
| heavy line | 17 % → 6 % | 50.4 px | 0.14 | 0.36 | 394 |
| pressure swell | 15 % → 6 % | 56.2 px | 0.17 | 0.37 | 382 |
| fast wave | 51 % → 8 % | 59.4 px | 0.21 | 0.16 | 1304 |
| slow wave | 40 % → 7 % | 46.5 px | 0.18 | 0.18 | 1888 |
| spiral | 68 % → 7 % | 44.6 px | 0.28 | 0.11 | 1695 |
| loop | 34 % → 1 % | 43.5 px | 0.23 | 0.03 | 773 |
| tilted | 18 % → 19 % | 51.6 px | 0.26 | 1.00 | 554 |
| over the wet one | 27 % → 7 % | 24.7 px | 0.26 | 0.26 | 491 |
| long, no reload | 54 % → 9 % | 24.4 px | 0.26 | 0.17 | 2068 | quarters: 0.10 → 0.14 → 0.10 → 0.04

Numbers say: light vs heavy: width 23.4 → 50.4 px, dark 0.00 → 0.14.

## Oil · Henry Ward · Ground #efe8b8 flat
Gouache 1.00 + turpentine 30 % · 160 px · 93.8 s

![Oil · Henry Ward · Ground #efe8b8 flat](Oil-Henry-Ward-Ground-efe8b8-flat.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 51 % → 43 % | 148.1 px | 0.37 | 0.84 | 844 |
| heavy line | 52 % → 45 % | 151.1 px | 0.37 | 0.87 | 1054 |
| pressure swell | 41 % → 43 % | 154.5 px | 0.36 | 1.04 | 744 |
| fast wave | 85 % → 82 % | 97.7 px | 0.36 | 0.97 | 2739 |
| slow wave | 86 % → 68 % | 99.0 px | 0.37 | 0.80 | 7102 |
| spiral | 88 % → 62 % | 58.2 px | 0.37 | 0.70 | 4970 |
| loop | 75 % → 67 % | 96.9 px | 0.37 | 0.89 | 1901 |
| tilted | 38 % → 38 % | 107.0 px | 0.37 | 1.00 | 1190 |
| over the wet one | 76 % → 68 % | 104.8 px | 0.37 | 0.90 | 1259 |
| long, no reload | 98 % → 81 % | 44.0 px | 0.36 | 0.83 | 5844 | quarters: 0.00 → 0.00 → 0.00 → 0.00

Numbers say: light vs heavy: width 148.1 → 151.1 px, dark 0.37 → 0.37; pressure barely changes the width.

## Oil · Henry Ward · Loaded flat #a89ac8 worn
Gouache 1.00 + turpentine 35 % · 84 px · 63.0 s

![Oil · Henry Ward · Loaded flat #a89ac8 worn](Oil-Henry-Ward-Loaded-flat-a89ac8-worn.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 27 % → 20 % | 78.1 px | 0.14 | 0.76 | 499 |
| heavy line | 35 % → 28 % | 102.9 px | 0.15 | 0.80 | 667 |
| pressure swell | 25 % → 22 % | 93.1 px | 0.21 | 0.89 | 428 |
| fast wave | 55 % → 37 % | 64.1 px | 0.25 | 0.66 | 1437 |
| slow wave | 57 % → 37 % | 66.0 px | 0.16 | 0.64 | 2046 |
| spiral | 62 % → 38 % | 40.6 px | 0.22 | 0.62 | 1994 |
| loop | 49 % → 39 % | 63.3 px | 0.15 | 0.80 | 1210 |
| tilted | 20 % → 20 % | 56.6 px | 0.24 | 1.01 | 582 |
| over the wet one | 48 % → 45 % | 77.5 px | 0.24 | 0.93 | 549 |
| long, no reload | 74 % → 40 % | 33.3 px | 0.26 | 0.54 | 2737 | quarters: 0.26 → 0.21 → 0.13 → 0.07

Numbers say: light vs heavy: width 78.1 → 102.9 px, dark 0.14 → 0.15.

## Oil · Henry Ward · Dirty contour #2a2418 flat
Gouache 1.00 + turpentine 35 % · 34 px · 45.2 s

![Oil · Henry Ward · Dirty contour #2a2418 flat](Oil-Henry-Ward-Dirty-contour-2a2418-flat.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 11 % → 10 % | 32.9 px | 0.54 | 0.89 | 121 |
| heavy line | 24 % → 17 % | 68.8 px | 0.54 | 0.71 | 250 |
| pressure swell | 15 % → 11 % | 55.0 px | 0.58 | 0.73 | 173 |
| fast wave | 44 % → 23 % | 50.6 px | 0.62 | 0.52 | 509 |
| slow wave | 41 % → 24 % | 47.8 px | 0.59 | 0.58 | 857 |
| spiral | 61 % → 27 % | 40.2 px | 0.60 | 0.44 | 1413 |
| loop | 37 % → 24 % | 47.5 px | 0.57 | 0.66 | 495 |
| tilted | 14 % → 14 % | 38.0 px | 0.62 | 1.01 | 240 |
| over the wet one | 32 % → 28 % | 51.3 px | 0.62 | 0.87 | 232 |
| long, no reload | 75 % → 30 % | 33.5 px | 0.62 | 0.40 | 1365 | quarters: 0.57 → 0.55 → 0.49 → 0.38

Numbers say: light vs heavy: width 32.9 → 68.8 px, dark 0.54 → 0.54.

## Oil · Henry Ward · Loaded flat #2a2418 filbert
Gouache 1.00 + turpentine 35 % · 84 px · 65.1 s

![Oil · Henry Ward · Loaded flat #2a2418 filbert](Oil-Henry-Ward-Loaded-flat-2a2418-filbert.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 23 % → 21 % | 68.0 px | 0.55 | 0.91 | 394 |
| heavy line | 25 % → 22 % | 71.9 px | 0.58 | 0.90 | 448 |
| pressure swell | 17 % → 18 % | 63.5 px | 0.61 | 1.07 | 321 |
| fast wave | 46 % → 34 % | 52.8 px | 0.65 | 0.73 | 1166 |
| slow wave | 46 % → 34 % | 53.7 px | 0.63 | 0.72 | 2062 |
| spiral | 52 % → 37 % | 34.4 px | 0.66 | 0.71 | 3816 |
| loop | 46 % → 39 % | 59.3 px | 0.62 | 0.85 | 1128 |
| tilted | 19 % → 19 % | 52.1 px | 0.65 | 1.02 | 510 |
| over the wet one | 39 % → 37 % | 55.5 px | 0.65 | 0.95 | 497 |
| long, no reload | 67 % → 40 % | 30.2 px | 0.66 | 0.59 | 2901 | quarters: 0.63 → 0.53 → 0.46 → 0.32

Numbers say: light vs heavy: width 68.0 → 71.9 px, dark 0.55 → 0.58; pressure barely changes the width.

## Oil · Henry Ward · Dry scrub #efeee6 worn
Gouache 1.00 + turpentine 20 % · 90 px · 44.6 s

![Oil · Henry Ward · Dry scrub #efeee6 worn](Oil-Henry-Ward-Dry-scrub-efeee6-worn.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 17 % → 0 % | 48.9 px | 0.00 | 0.00 | 406 |
| heavy line | 30 % → 1 % | 87.7 px | 0.32 | 0.03 | 1218 |
| pressure swell | 21 % → 6 % | 77.3 px | 0.32 | 0.30 | 733 |
| fast wave | 68 % → 7 % | 78.4 px | 0.26 | 0.11 | 1798 |
| slow wave | 51 % → 4 % | 58.8 px | 0.30 | 0.08 | 2286 |
| spiral | 72 % → 10 % | 47.7 px | 0.27 | 0.14 | 2696 |
| loop | 51 % → 0 % | 66.3 px | 0.27 | 0.01 | 1145 |
| tilted | 20 % → 20 % | 57.1 px | 0.26 | 1.00 | 766 |
| over the wet one | 41 % → 9 % | 56.7 px | 0.26 | 0.22 | 499 |
| long, no reload | 80 % → 0 % | 36.0 px | 0.25 | 0.00 | 3040 | quarters: 0.01 → 0.02 → 0.01 → 0.02

Numbers say: light vs heavy: width 48.9 → 87.7 px, dark 0.00 → 0.32; the long stroke does not run out of paint.

## Oil · Henry Ward · Ground #e6e2f0 flat
Gouache 1.00 + turpentine 30 % · 160 px · 91.6 s

![Oil · Henry Ward · Ground #e6e2f0 flat](Oil-Henry-Ward-Ground-e6e2f0-flat.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 51 % → 43 % | 148.1 px | 0.37 | 0.84 | 1088 |
| heavy line | 52 % → 45 % | 151.1 px | 0.37 | 0.87 | 907 |
| pressure swell | 41 % → 43 % | 154.5 px | 0.36 | 1.04 | 761 |
| fast wave | 85 % → 82 % | 97.7 px | 0.36 | 0.97 | 2954 |
| slow wave | 86 % → 68 % | 99.0 px | 0.37 | 0.80 | 5378 |
| spiral | 88 % → 62 % | 58.2 px | 0.37 | 0.70 | 4662 |
| loop | 75 % → 67 % | 96.9 px | 0.37 | 0.89 | 2259 |
| tilted | 38 % → 38 % | 107.0 px | 0.37 | 1.00 | 1211 |
| over the wet one | 76 % → 68 % | 104.8 px | 0.37 | 0.90 | 1136 |
| long, no reload | 98 % → 81 % | 44.0 px | 0.36 | 0.83 | 7303 | quarters: 0.00 → 0.00 → 0.00 → 0.00

Numbers say: light vs heavy: width 148.1 → 151.1 px, dark 0.37 → 0.37; pressure barely changes the width.

## Oil · Henry Ward · Loaded flat #a8b84a worn
Gouache 1.00 + turpentine 35 % · 84 px · 65.9 s

![Oil · Henry Ward · Loaded flat #a8b84a worn](Oil-Henry-Ward-Loaded-flat-a8b84a-worn.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 27 % → 20 % | 78.1 px | 0.12 | 0.76 | 442 |
| heavy line | 35 % → 28 % | 102.9 px | 0.12 | 0.80 | 599 |
| pressure swell | 25 % → 22 % | 93.1 px | 0.19 | 0.89 | 461 |
| fast wave | 55 % → 37 % | 64.1 px | 0.23 | 0.66 | 1566 |
| slow wave | 57 % → 37 % | 66.0 px | 0.14 | 0.64 | 2265 |
| spiral | 62 % → 38 % | 40.6 px | 0.20 | 0.62 | 2170 |
| loop | 49 % → 39 % | 63.3 px | 0.13 | 0.80 | 1100 |
| tilted | 20 % → 20 % | 56.6 px | 0.22 | 1.01 | 1000 |
| over the wet one | 48 % → 45 % | 77.5 px | 0.22 | 0.93 | 637 |
| long, no reload | 74 % → 40 % | 33.3 px | 0.24 | 0.54 | 2753 | quarters: 0.24 → 0.19 → 0.12 → 0.07

Numbers say: light vs heavy: width 78.1 → 102.9 px, dark 0.12 → 0.12.

## Oil · Henry Ward · Thin veil #5a8a6a flat
Watercolour 0.93 · Ink 0.07 + turpentine 80 % · 96 px · 62.9 s

![Oil · Henry Ward · Thin veil #5a8a6a flat](Oil-Henry-Ward-Thin-veil-5a8a6a-flat.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 26 % → 28 % | 75.6 px | 0.06 | 1.06 | 352 |
| heavy line | 27 % → 30 % | 77.8 px | 0.06 | 1.10 | 331 |
| pressure swell | 20 % → 23 % | 74.0 px | 0.07 | 1.17 | 292 |
| fast wave | 56 % → 64 % | 64.9 px | 0.07 | 1.13 | 927 |
| slow wave | 60 % → 66 % | 69.2 px | 0.06 | 1.11 | 2717 |
| spiral | 66 % → 72 % | 43.4 px | 0.06 | 1.10 | 2082 |
| loop | 57 % → 60 % | 74.4 px | 0.06 | 1.05 | 897 |
| tilted | 21 % → 22 % | 59.4 px | 0.07 | 1.02 | 594 |
| over the wet one | 43 % → 47 % | 62.0 px | 0.07 | 1.08 | 439 |
| long, no reload | 83 % → 91 % | 37.0 px | 0.07 | 1.10 | 4195 | quarters: 0.08 → 0.07 → 0.06 → 0.05

Numbers say: light vs heavy: width 75.6 → 77.8 px, dark 0.06 → 0.06; pressure barely changes the width.

## Oil · Henry Ward · Loaded flat #4a1420 worn
Gouache 1.00 + turpentine 35 % · 84 px · 70.4 s

![Oil · Henry Ward · Loaded flat #4a1420 worn](Oil-Henry-Ward-Loaded-flat-4a1420-worn.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 27 % → 20 % | 78.1 px | 0.57 | 0.76 | 480 |
| heavy line | 35 % → 28 % | 102.9 px | 0.58 | 0.80 | 561 |
| pressure swell | 25 % → 22 % | 93.1 px | 0.60 | 0.89 | 426 |
| fast wave | 55 % → 37 % | 64.1 px | 0.62 | 0.66 | 1574 |
| slow wave | 57 % → 37 % | 66.0 px | 0.59 | 0.64 | 2240 |
| spiral | 62 % → 38 % | 40.6 px | 0.61 | 0.62 | 2374 |
| loop | 49 % → 39 % | 63.3 px | 0.58 | 0.80 | 1221 |
| tilted | 20 % → 20 % | 56.6 px | 0.62 | 1.01 | 768 |
| over the wet one | 48 % → 45 % | 77.5 px | 0.62 | 0.93 | 682 |
| long, no reload | 74 % → 40 % | 33.3 px | 0.63 | 0.54 | 3211 | quarters: 0.63 → 0.57 → 0.47 → 0.36

Numbers say: light vs heavy: width 78.1 → 102.9 px, dark 0.57 → 0.58.

## Oil · Henry Ward · Dirty contour #2a0a10 flat
Gouache 1.00 + turpentine 35 % · 34 px · 54.2 s

![Oil · Henry Ward · Dirty contour #2a0a10 flat](Oil-Henry-Ward-Dirty-contour-2a0a10-flat.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 11 % → 10 % | 32.9 px | 0.64 | 0.89 | 177 |
| heavy line | 24 % → 17 % | 68.8 px | 0.64 | 0.71 | 471 |
| pressure swell | 15 % → 11 % | 55.0 px | 0.65 | 0.73 | 220 |
| fast wave | 44 % → 23 % | 50.6 px | 0.67 | 0.52 | 556 |
| slow wave | 41 % → 24 % | 47.8 px | 0.66 | 0.58 | 970 |
| spiral | 61 % → 27 % | 40.2 px | 0.66 | 0.44 | 1078 |
| loop | 37 % → 24 % | 47.5 px | 0.65 | 0.66 | 500 |
| tilted | 14 % → 14 % | 38.0 px | 0.67 | 1.01 | 270 |
| over the wet one | 32 % → 28 % | 51.3 px | 0.67 | 0.87 | 364 |
| long, no reload | 75 % → 30 % | 33.5 px | 0.67 | 0.40 | 1592 | quarters: 0.61 → 0.59 → 0.54 → 0.44

Numbers say: light vs heavy: width 32.9 → 68.8 px, dark 0.64 → 0.64.

## Oil · Henry Ward · Dry scrub #c0506a worn
Gouache 1.00 + turpentine 20 % · 90 px · 44.8 s

![Oil · Henry Ward · Dry scrub #c0506a worn](Oil-Henry-Ward-Dry-scrub-c0506a-worn.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 17 % → 0 % | 48.9 px | 0.00 | 0.00 | 366 |
| heavy line | 30 % → 1 % | 87.7 px | 0.27 | 0.03 | 526 |
| pressure swell | 21 % → 6 % | 77.3 px | 0.26 | 0.30 | 433 |
| fast wave | 68 % → 7 % | 78.4 px | 0.34 | 0.10 | 1664 |
| slow wave | 51 % → 4 % | 58.9 px | 0.28 | 0.08 | 2439 |
| spiral | 72 % → 10 % | 47.7 px | 0.35 | 0.14 | 2386 |
| loop | 51 % → 0 % | 66.3 px | 0.27 | 0.01 | 1164 |
| tilted | 20 % → 20 % | 57.1 px | 0.34 | 1.00 | 828 |
| over the wet one | 41 % → 9 % | 56.7 px | 0.34 | 0.21 | 657 |
| long, no reload | 80 % → 0 % | 36.0 px | 0.30 | 0.00 | 2769 | quarters: 0.22 → 0.17 → 0.16 → 0.11

Numbers say: light vs heavy: width 48.9 → 87.7 px, dark 0.00 → 0.27.

## Oil · Henry Ward · Ground #d8d4c8 flat
Ink 0.65 · Watercolour 0.35 + turpentine 75 % · 160 px · 98.1 s

![Oil · Henry Ward · Ground #d8d4c8 flat](Oil-Henry-Ward-Ground-d8d4c8-flat.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 51 % → 56 % | 148.0 px | 0.06 | 1.10 | 699 |
| heavy line | 53 % → 52 % | 153.8 px | 0.06 | 0.98 | 1346 |
| pressure swell | 41 % → 50 % | 155.4 px | 0.05 | 1.21 | 756 |
| fast wave | 87 % → 93 % | 100.9 px | 0.05 | 1.06 | 3585 |
| slow wave | 87 % → 85 % | 100.7 px | 0.04 | 0.98 | 4378 |
| spiral | 93 % → 92 % | 61.5 px | 0.05 | 0.99 | 4562 |
| loop | 78 % → 78 % | 100.9 px | 0.04 | 1.00 | 1989 |
| tilted | 40 % → 40 % | 110.5 px | 0.05 | 1.01 | 1127 |
| over the wet one | 77 % → 79 % | 103.9 px | 0.05 | 1.03 | 968 |
| long, no reload | 99 % → 100 % | 44.4 px | 0.04 | 1.01 | 7201 | quarters: 0.00 → 0.02 → 0.04 → 0.07

Numbers say: light vs heavy: width 148.0 → 153.8 px, dark 0.06 → 0.06; pressure barely changes the width; the long stroke does not run out of paint.

## Oil · Henry Ward · Loaded flat #e8d8b0 flat
Gouache 1.00 + turpentine 35 % · 84 px · 71.1 s

![Oil · Henry Ward · Loaded flat #e8d8b0 flat](Oil-Henry-Ward-Loaded-flat-e8d8b0-flat.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 25 % → 20 % | 72.6 px | 0.39 | 0.81 | 390 |
| heavy line | 25 % → 20 % | 71.5 px | 0.40 | 0.82 | 454 |
| pressure swell | 19 % → 18 % | 70.5 px | 0.35 | 0.97 | 357 |
| fast wave | 46 % → 34 % | 53.3 px | 0.29 | 0.73 | 1253 |
| slow wave | 48 % → 36 % | 55.4 px | 0.35 | 0.75 | 2773 |
| spiral | 51 % → 40 % | 33.7 px | 0.31 | 0.78 | 2229 |
| loop | 41 % → 37 % | 52.7 px | 0.37 | 0.91 | 1074 |
| tilted | 19 % → 19 % | 53.7 px | 0.32 | 1.01 | 590 |
| over the wet one | 39 % → 38 % | 55.2 px | 0.32 | 0.98 | 507 |
| long, no reload | 63 % → 41 % | 28.2 px | 0.29 | 0.65 | 3140 | quarters: 0.00 → 0.01 → 0.01 → 0.01

Numbers say: light vs heavy: width 72.6 → 71.5 px, dark 0.39 → 0.40; pressure barely changes the width; the long stroke does not run out of paint.

## Oil · Henry Ward · Dry scrub #f2ead0 filbert
Gouache 1.00 + turpentine 20 % · 90 px · 51.1 s

![Oil · Henry Ward · Dry scrub #f2ead0 filbert](Oil-Henry-Ward-Dry-scrub-f2ead0-filbert.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 8 % → 0 % | 23.4 px | 0.00 | 0.00 | 345 |
| heavy line | 17 % → 6 % | 50.4 px | 0.37 | 0.35 | 512 |
| pressure swell | 15 % → 6 % | 56.1 px | 0.35 | 0.38 | 353 |
| fast wave | 51 % → 9 % | 59.4 px | 0.31 | 0.17 | 1251 |
| slow wave | 40 % → 8 % | 46.5 px | 0.33 | 0.19 | 1968 |
| spiral | 67 % → 7 % | 44.5 px | 0.28 | 0.11 | 2507 |
| loop | 34 % → 1 % | 43.5 px | 0.28 | 0.03 | 995 |
| tilted | 18 % → 19 % | 51.6 px | 0.28 | 1.00 | 539 |
| over the wet one | 27 % → 7 % | 24.6 px | 0.28 | 0.27 | 369 |
| long, no reload | 54 % → 9 % | 24.3 px | 0.28 | 0.17 | 2631 | quarters: 0.03 → 0.02 → 0.03 → 0.05

Numbers say: light vs heavy: width 23.4 → 50.4 px, dark 0.00 → 0.37; the long stroke does not run out of paint.

## Oil · Henry Ward · Loaded flat #2a1428 flat
Gouache 1.00 + turpentine 35 % · 84 px · 66.1 s

![Oil · Henry Ward · Loaded flat #2a1428 flat](Oil-Henry-Ward-Loaded-flat-2a1428-flat.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 25 % → 20 % | 72.6 px | 0.65 | 0.81 | 365 |
| heavy line | 25 % → 20 % | 71.5 px | 0.64 | 0.82 | 428 |
| pressure swell | 19 % → 18 % | 70.5 px | 0.68 | 0.97 | 278 |
| fast wave | 46 % → 34 % | 53.3 px | 0.72 | 0.73 | 997 |
| slow wave | 48 % → 36 % | 55.4 px | 0.68 | 0.75 | 2398 |
| spiral | 51 % → 40 % | 33.7 px | 0.70 | 0.78 | 2415 |
| loop | 41 % → 37 % | 52.7 px | 0.65 | 0.91 | 1032 |
| tilted | 19 % → 19 % | 53.7 px | 0.70 | 1.01 | 567 |
| over the wet one | 39 % → 38 % | 55.2 px | 0.70 | 0.98 | 476 |
| long, no reload | 63 % → 41 % | 28.2 px | 0.72 | 0.65 | 3175 | quarters: 0.65 → 0.54 → 0.47 → 0.35

Numbers say: light vs heavy: width 72.6 → 71.5 px, dark 0.65 → 0.64; pressure barely changes the width.

## Oil · Henry Ward · Ground #e8e4e0 flat
Gouache 1.00 + turpentine 30 % · 160 px · 98.1 s

![Oil · Henry Ward · Ground #e8e4e0 flat](Oil-Henry-Ward-Ground-e8e4e0-flat.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 51 % → 43 % | 148.1 px | 0.37 | 0.84 | 1189 |
| heavy line | 52 % → 45 % | 151.1 px | 0.37 | 0.87 | 1168 |
| pressure swell | 41 % → 43 % | 154.5 px | 0.37 | 1.04 | 795 |
| fast wave | 85 % → 82 % | 97.7 px | 0.36 | 0.97 | 2887 |
| slow wave | 86 % → 68 % | 99.0 px | 0.37 | 0.80 | 5464 |
| spiral | 88 % → 62 % | 58.2 px | 0.37 | 0.70 | 4711 |
| loop | 75 % → 67 % | 96.9 px | 0.37 | 0.89 | 2579 |
| tilted | 38 % → 38 % | 107.0 px | 0.37 | 1.00 | 1392 |
| over the wet one | 76 % → 68 % | 104.8 px | 0.37 | 0.90 | 1220 |
| long, no reload | 98 % → 81 % | 44.0 px | 0.36 | 0.83 | 7525 | quarters: 0.00 → 0.00 → 0.00 → 0.00

Numbers say: light vs heavy: width 148.1 → 151.1 px, dark 0.37 → 0.37; pressure barely changes the width.

## Oil · Henry Ward · Loaded flat #8a2a18 filbert
Gouache 1.00 + turpentine 35 % · 84 px · 64.6 s

![Oil · Henry Ward · Loaded flat #8a2a18 filbert](Oil-Henry-Ward-Loaded-flat-8a2a18-filbert.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 23 % → 21 % | 68.0 px | 0.50 | 0.91 | 405 |
| heavy line | 25 % → 22 % | 71.9 px | 0.53 | 0.90 | 423 |
| pressure swell | 17 % → 18 % | 63.5 px | 0.55 | 1.07 | 314 |
| fast wave | 46 % → 34 % | 52.8 px | 0.58 | 0.73 | 1124 |
| slow wave | 46 % → 34 % | 53.7 px | 0.57 | 0.72 | 1964 |
| spiral | 52 % → 37 % | 34.4 px | 0.59 | 0.71 | 2089 |
| loop | 46 % → 39 % | 59.3 px | 0.56 | 0.85 | 1068 |
| tilted | 19 % → 19 % | 52.1 px | 0.59 | 1.02 | 496 |
| over the wet one | 39 % → 37 % | 55.5 px | 0.59 | 0.95 | 447 |
| long, no reload | 67 % → 40 % | 30.2 px | 0.59 | 0.59 | 3121 | quarters: 0.57 → 0.48 → 0.41 → 0.28

Numbers say: light vs heavy: width 68.0 → 71.9 px, dark 0.50 → 0.53; pressure barely changes the width.

## Oil · Henry Ward · Loaded flat #a8c8dc filbert
Gouache 1.00 + turpentine 35 % · 84 px · 62.9 s

![Oil · Henry Ward · Loaded flat #a8c8dc filbert](Oil-Henry-Ward-Loaded-flat-a8c8dc-filbert.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 23 % → 21 % | 68.0 px | 0.38 | 0.91 | 385 |
| heavy line | 25 % → 22 % | 71.9 px | 0.36 | 0.90 | 416 |
| pressure swell | 17 % → 18 % | 63.5 px | 0.32 | 1.07 | 410 |
| fast wave | 46 % → 34 % | 52.8 px | 0.27 | 0.73 | 1395 |
| slow wave | 46 % → 34 % | 53.7 px | 0.31 | 0.72 | 1682 |
| spiral | 52 % → 37 % | 34.4 px | 0.26 | 0.71 | 1912 |
| loop | 46 % → 39 % | 59.3 px | 0.31 | 0.85 | 1107 |
| tilted | 19 % → 19 % | 52.1 px | 0.27 | 1.02 | 648 |
| over the wet one | 39 % → 37 % | 55.5 px | 0.27 | 0.95 | 454 |
| long, no reload | 67 % → 40 % | 30.2 px | 0.26 | 0.59 | 2753 | quarters: 0.00 → 0.00 → 0.01 → 0.01

Numbers say: light vs heavy: width 68.0 → 71.9 px, dark 0.38 → 0.36; pressure barely changes the width; the long stroke does not run out of paint.

## Oil · Henry Ward · Dry scrub #d8e8f0 filbert
Gouache 1.00 + turpentine 20 % · 90 px · 48.5 s

![Oil · Henry Ward · Dry scrub #d8e8f0 filbert](Oil-Henry-Ward-Dry-scrub-d8e8f0-filbert.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 8 % → 0 % | 23.4 px | 0.00 | 0.00 | 344 |
| heavy line | 17 % → 6 % | 50.4 px | 0.37 | 0.35 | 434 |
| pressure swell | 15 % → 6 % | 56.1 px | 0.35 | 0.38 | 327 |
| fast wave | 51 % → 9 % | 59.4 px | 0.30 | 0.17 | 1101 |
| slow wave | 40 % → 8 % | 46.5 px | 0.33 | 0.19 | 2473 |
| spiral | 67 % → 7 % | 44.5 px | 0.28 | 0.11 | 1797 |
| loop | 34 % → 1 % | 43.5 px | 0.28 | 0.03 | 904 |
| tilted | 18 % → 19 % | 51.6 px | 0.28 | 1.00 | 569 |
| over the wet one | 27 % → 7 % | 24.6 px | 0.28 | 0.27 | 408 |
| long, no reload | 54 % → 9 % | 24.3 px | 0.28 | 0.17 | 2793 | quarters: 0.03 → 0.02 → 0.03 → 0.05

Numbers say: light vs heavy: width 23.4 → 50.4 px, dark 0.00 → 0.37; the long stroke does not run out of paint.

## Oil · Henry Ward · Ground #3a3a34 flat
Ink 0.65 · Watercolour 0.35 + turpentine 75 % · 160 px · 95.5 s

![Oil · Henry Ward · Ground #3a3a34 flat](Oil-Henry-Ward-Ground-3a3a34-flat.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 51 % → 56 % | 148.0 px | 0.37 | 1.10 | 1068 |
| heavy line | 53 % → 52 % | 153.8 px | 0.41 | 0.98 | 1187 |
| pressure swell | 41 % → 50 % | 155.4 px | 0.42 | 1.21 | 681 |
| fast wave | 87 % → 93 % | 100.9 px | 0.46 | 1.06 | 2507 |
| slow wave | 87 % → 85 % | 100.7 px | 0.49 | 0.98 | 4785 |
| spiral | 93 % → 92 % | 61.5 px | 0.47 | 0.99 | 4217 |
| loop | 78 % → 78 % | 100.9 px | 0.47 | 1.00 | 2451 |
| tilted | 40 % → 40 % | 110.5 px | 0.46 | 1.01 | 1541 |
| over the wet one | 77 % → 79 % | 103.9 px | 0.46 | 1.03 | 1023 |
| long, no reload | 99 % → 100 % | 44.4 px | 0.48 | 1.01 | 7337 | quarters: 0.63 → 0.58 → 0.47 → 0.32

Numbers say: light vs heavy: width 148.0 → 153.8 px, dark 0.37 → 0.41; pressure barely changes the width.

## Oil · Henry Ward · Loaded flat #8a906a worn
Gouache 1.00 + turpentine 35 % · 84 px · 72.3 s

![Oil · Henry Ward · Loaded flat #8a906a worn](Oil-Henry-Ward-Loaded-flat-8a906a-worn.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 27 % → 20 % | 78.1 px | 0.19 | 0.76 | 505 |
| heavy line | 35 % → 28 % | 102.9 px | 0.21 | 0.80 | 1367 |
| pressure swell | 25 % → 22 % | 93.1 px | 0.26 | 0.89 | 773 |
| fast wave | 55 % → 37 % | 64.1 px | 0.30 | 0.66 | 1351 |
| slow wave | 57 % → 37 % | 66.0 px | 0.22 | 0.64 | 2493 |
| spiral | 62 % → 38 % | 40.6 px | 0.27 | 0.62 | 3084 |
| loop | 49 % → 39 % | 63.3 px | 0.20 | 0.80 | 1313 |
| tilted | 20 % → 20 % | 56.6 px | 0.29 | 1.01 | 692 |
| over the wet one | 48 % → 45 % | 77.5 px | 0.29 | 0.93 | 665 |
| long, no reload | 74 % → 40 % | 33.3 px | 0.31 | 0.54 | 3847 | quarters: 0.31 → 0.26 → 0.17 → 0.10

Numbers say: light vs heavy: width 78.1 → 102.9 px, dark 0.19 → 0.21.

## Oil · Henry Ward · Loaded flat #7a8458 flat
Gouache 1.00 + turpentine 35 % · 84 px · 67.1 s

![Oil · Henry Ward · Loaded flat #7a8458 flat](Oil-Henry-Ward-Loaded-flat-7a8458-flat.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 25 % → 20 % | 72.6 px | 0.26 | 0.81 | 368 |
| heavy line | 25 % → 20 % | 71.5 px | 0.25 | 0.82 | 418 |
| pressure swell | 19 % → 18 % | 70.5 px | 0.31 | 0.97 | 313 |
| fast wave | 46 % → 34 % | 53.3 px | 0.37 | 0.73 | 1059 |
| slow wave | 48 % → 36 % | 55.4 px | 0.29 | 0.75 | 2216 |
| spiral | 51 % → 40 % | 33.7 px | 0.34 | 0.78 | 2143 |
| loop | 41 % → 37 % | 52.7 px | 0.26 | 0.91 | 1058 |
| tilted | 19 % → 19 % | 53.7 px | 0.35 | 1.01 | 565 |
| over the wet one | 39 % → 38 % | 55.2 px | 0.35 | 0.98 | 451 |
| long, no reload | 63 % → 41 % | 28.2 px | 0.37 | 0.65 | 3642 | quarters: 0.33 → 0.26 → 0.21 → 0.14

Numbers say: light vs heavy: width 72.6 → 71.5 px, dark 0.26 → 0.25; pressure barely changes the width.

## Oil · Henry Ward · Dry scrub #a8ae88 filbert
Gouache 1.00 + turpentine 20 % · 90 px · 49.2 s

![Oil · Henry Ward · Dry scrub #a8ae88 filbert](Oil-Henry-Ward-Dry-scrub-a8ae88-filbert.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 8 % → 0 % | 23.4 px | 0.00 | 0.00 | 646 |
| heavy line | 17 % → 6 % | 50.4 px | 0.08 | 0.36 | 825 |
| pressure swell | 15 % → 6 % | 56.2 px | 0.12 | 0.37 | 883 |
| fast wave | 51 % → 8 % | 59.4 px | 0.16 | 0.16 | 1053 |
| slow wave | 40 % → 7 % | 46.5 px | 0.13 | 0.18 | 1860 |
| spiral | 68 % → 7 % | 44.6 px | 0.23 | 0.11 | 2116 |
| loop | 34 % → 1 % | 43.5 px | 0.18 | 0.03 | 1248 |
| tilted | 18 % → 19 % | 51.6 px | 0.21 | 1.00 | 558 |
| over the wet one | 27 % → 7 % | 24.7 px | 0.21 | 0.26 | 386 |
| long, no reload | 54 % → 9 % | 24.4 px | 0.21 | 0.17 | 2358 | quarters: 0.07 → 0.11 → 0.07 → 0.03

Numbers say: light vs heavy: width 23.4 → 50.4 px, dark 0.00 → 0.08.

## Surface test · Under SmoothPanel
Gouache 1.00 + turpentine 30 % · 60 px · 58.1 s

![Surface test · Under SmoothPanel](Surface-test-Under-SmoothPanel.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 16 % → 16 % | 46.4 px | 0.47 | 0.97 | 449 |
| heavy line | 16 % → 15 % | 46.8 px | 0.47 | 0.95 | 468 |
| pressure swell | 12 % → 13 % | 46.0 px | 0.48 | 1.07 | 204 |
| fast wave | 28 % → 20 % | 32.7 px | 0.49 | 0.72 | 664 |
| slow wave | 34 % → 24 % | 38.9 px | 0.47 | 0.70 | 1129 |
| spiral | 51 % → 26 % | 33.3 px | 0.45 | 0.52 | 1294 |
| loop | 26 % → 21 % | 33.3 px | 0.46 | 0.82 | 617 |
| tilted | 15 % → 15 % | 40.9 px | 0.49 | 1.01 | 488 |
| over the wet one | 29 % → 26 % | 40.9 px | 0.49 | 0.90 | 387 |
| long, no reload | 58 % → 26 % | 25.9 px | 0.48 | 0.44 | 1840 | quarters: 0.39 → 0.29 → 0.22 → 0.14

Numbers say: light vs heavy: width 46.4 → 46.8 px, dark 0.47 → 0.47; pressure barely changes the width.

## Surface test · Oil 0% SmoothPanel
Oil 1.00 · 70 px · 32.4 s

![Surface test · Oil 0% SmoothPanel](Surface-test-Oil-0-SmoothPanel.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 20 % → 21 % | 59.1 px | 0.40 | 1.02 | 336 |
| heavy line | 20 % → 20 % | 58.0 px | 0.40 | 1.00 | 385 |
| pressure swell | 15 % → 15 % | 56.2 px | 0.36 | 1.02 | 320 |
| fast wave | 43 % → 44 % | 49.4 px | 0.32 | 1.03 | 1282 |
| slow wave | 45 % → 45 % | 51.9 px | 0.38 | 1.00 | 1424 |
| spiral | 51 % → 51 % | 33.6 px | 0.34 | 1.00 | 1575 |
| loop | 42 % → 42 % | 54.9 px | 0.37 | 1.00 | 784 |
| tilted | 18 % → 18 % | 50.2 px | 0.35 | 1.00 | 542 |
| over the wet one | 35 % → 35 % | 47.5 px | 0.35 | 1.00 | 405 |
| long, no reload | 71 % → 71 % | 31.9 px | 0.30 | 1.00 | 2736 | quarters: 0.00 → 0.00 → 0.00 → 0.00

Numbers say: light vs heavy: width 59.1 → 58.0 px, dark 0.40 → 0.40; pressure barely changes the width.

## Surface test · Oil 40% SmoothPanel
Gouache 1.00 + turpentine 40 % · 70 px · 58.3 s

![Surface test · Oil 40% SmoothPanel](Surface-test-Oil-40-SmoothPanel.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 18 % → 17 % | 51.5 px | 0.41 | 0.97 | 247 |
| heavy line | 20 % → 18 % | 57.7 px | 0.41 | 0.92 | 331 |
| pressure swell | 15 % → 16 % | 56.5 px | 0.39 | 1.03 | 240 |
| fast wave | 37 % → 25 % | 43.1 px | 0.37 | 0.68 | 976 |
| slow wave | 41 % → 27 % | 47.3 px | 0.39 | 0.66 | 1813 |
| spiral | 51 % → 28 % | 33.8 px | 0.39 | 0.56 | 1583 |
| loop | 34 % → 28 % | 44.1 px | 0.39 | 0.82 | 697 |
| tilted | 18 % → 18 % | 49.6 px | 0.37 | 1.00 | 438 |
| over the wet one | 35 % → 31 % | 48.1 px | 0.37 | 0.89 | 356 |
| long, no reload | 62 % → 28 % | 27.8 px | 0.39 | 0.46 | 2019 | quarters: 0.00 → 0.01 → 0.01 → 0.01

Numbers say: light vs heavy: width 51.5 → 57.7 px, dark 0.41 → 0.41; the long stroke does not run out of paint.

## Surface test · Oil 80% SmoothPanel
Watercolour 0.93 · Ink 0.07 + turpentine 80 % · 70 px · 57.5 s

![Surface test · Oil 80% SmoothPanel](Surface-test-Oil-80-SmoothPanel.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 19 % → 24 % | 54.2 px | 0.09 | 1.27 | 264 |
| heavy line | 19 % → 25 % | 54.0 px | 0.09 | 1.35 | 324 |
| pressure swell | 15 % → 20 % | 57.4 px | 0.09 | 1.32 | 232 |
| fast wave | 41 % → 53 % | 47.1 px | 0.09 | 1.29 | 957 |
| slow wave | 37 % → 49 % | 42.4 px | 0.09 | 1.34 | 1656 |
| spiral | 46 % → 58 % | 30.2 px | 0.09 | 1.27 | 1439 |
| loop | 36 % → 49 % | 46.9 px | 0.09 | 1.35 | 615 |
| tilted | 17 % → 17 % | 47.2 px | 0.09 | 1.03 | 443 |
| over the wet one | 35 % → 43 % | 49.3 px | 0.09 | 1.25 | 355 |
| long, no reload | 61 % → 76 % | 27.5 px | 0.09 | 1.25 | 2348 | quarters: 0.08 → 0.09 → 0.08 → 0.05

Numbers say: light vs heavy: width 54.2 → 54.0 px, dark 0.09 → 0.09; pressure barely changes the width.

## Surface test · Dry scrub SmoothPanel
Gouache 1.00 + turpentine 20 % · 70 px · 48.4 s

![Surface test · Dry scrub SmoothPanel](Surface-test-Dry-scrub-SmoothPanel.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 13 % → 0 % | 36.7 px | 0.00 | 0.00 | 274 |
| heavy line | 28 % → 2 % | 80.6 px | 0.34 | 0.07 | 372 |
| pressure swell | 18 % → 7 % | 68.2 px | 0.35 | 0.39 | 300 |
| fast wave | 61 % → 24 % | 70.6 px | 0.28 | 0.39 | 1177 |
| slow wave | 43 % → 16 % | 49.5 px | 0.32 | 0.36 | 1830 |
| spiral | 69 % → 12 % | 45.4 px | 0.32 | 0.18 | 1968 |
| loop | 44 % → 3 % | 57.4 px | 0.29 | 0.07 | 1546 |
| tilted | 16 % → 16 % | 44.5 px | 0.28 | 1.01 | 805 |
| over the wet one | 35 % → 13 % | 52.5 px | 0.28 | 0.37 | 407 |
| long, no reload | 87 % → 18 % | 39.1 px | 0.30 | 0.20 | 2935 | quarters: 0.00 → 0.01 → 0.01 → 0.02

Numbers say: light vs heavy: width 36.7 → 80.6 px, dark 0.00 → 0.34; the long stroke does not run out of paint.

## Surface test · Watercolour SmoothPanel
Watercolour 1.00 + water 40 % · 60 px · 44.1 s

![Surface test · Watercolour SmoothPanel](Surface-test-Watercolour-SmoothPanel.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 8 % → 15 % | 24.2 px | 0.38 | 1.74 | 81 |
| heavy line | 16 % → 19 % | 47.6 px | 0.38 | 1.18 | 171 |
| pressure swell | 10 % → 13 % | 37.5 px | 0.40 | 1.30 | 149 |
| fast wave | 36 % → 40 % | 41.1 px | 0.36 | 1.12 | 357 |
| slow wave | 33 % → 39 % | 38.0 px | 0.38 | 1.18 | 521 |
| spiral | 56 % → 59 % | 36.8 px | 0.33 | 1.05 | 564 |
| loop | 28 % → 33 % | 36.8 px | 0.39 | 1.16 | 333 |
| tilted | 18 % → 18 % | 51.1 px | 0.38 | 1.00 | 187 |
| over the wet one | 30 % → 33 % | 33.0 px | 0.38 | 1.10 | 140 |
| long, no reload | 73 % → 75 % | 32.5 px | 0.31 | 1.04 | 1058 | quarters: 0.36 → 0.28 → 0.21 → 0.15

Numbers say: light vs heavy: width 24.2 → 47.6 px, dark 0.38 → 0.38; wet paint spreads well beyond the stroke.

## Surface test · Surface test · smooth panel
Gouache 1.00 + turpentine 40 % · 70 px · 60.6 s

![Surface test · Surface test · smooth panel](Surface-test-Surface-test-smooth-panel.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 18 % → 17 % | 51.5 px | 0.41 | 0.97 | 377 |
| heavy line | 20 % → 18 % | 57.7 px | 0.41 | 0.92 | 353 |
| pressure swell | 15 % → 16 % | 56.5 px | 0.39 | 1.03 | 230 |
| fast wave | 37 % → 25 % | 43.1 px | 0.37 | 0.68 | 946 |
| slow wave | 41 % → 27 % | 47.3 px | 0.39 | 0.66 | 1445 |
| spiral | 51 % → 28 % | 33.8 px | 0.39 | 0.56 | 1961 |
| loop | 34 % → 28 % | 44.1 px | 0.39 | 0.82 | 688 |
| tilted | 18 % → 18 % | 49.6 px | 0.37 | 1.00 | 471 |
| over the wet one | 35 % → 31 % | 48.1 px | 0.37 | 0.89 | 371 |
| long, no reload | 62 % → 28 % | 27.8 px | 0.39 | 0.46 | 2077 | quarters: 0.00 → 0.01 → 0.01 → 0.01

Numbers say: light vs heavy: width 51.5 → 57.7 px, dark 0.41 → 0.41; the long stroke does not run out of paint.

## Surface test · Under Paper
Gouache 1.00 + turpentine 30 % · 60 px · 58.5 s

![Surface test · Under Paper](Surface-test-Under-Paper.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 16 % → 15 % | 45.7 px | 0.49 | 0.96 | 298 |
| heavy line | 16 % → 15 % | 46.2 px | 0.49 | 0.94 | 292 |
| pressure swell | 12 % → 13 % | 45.6 px | 0.50 | 1.06 | 215 |
| fast wave | 26 % → 24 % | 29.6 px | 0.51 | 0.93 | 813 |
| slow wave | 33 % → 26 % | 37.7 px | 0.48 | 0.80 | 1256 |
| spiral | 47 % → 33 % | 30.9 px | 0.46 | 0.70 | 1661 |
| loop | 25 % → 22 % | 31.8 px | 0.48 | 0.91 | 578 |
| tilted | 13 % → 14 % | 37.6 px | 0.51 | 1.04 | 420 |
| over the wet one | 29 % → 28 % | 42.4 px | 0.51 | 0.99 | 306 |
| long, no reload | 50 % → 35 % | 22.3 px | 0.49 | 0.71 | 1877 | quarters: 0.40 → 0.29 → 0.23 → 0.17

Numbers say: light vs heavy: width 45.7 → 46.2 px, dark 0.49 → 0.49; pressure barely changes the width.

## Surface test · Oil 0% Paper
Oil 1.00 · 70 px · 32.7 s

![Surface test · Oil 0% Paper](Surface-test-Oil-0-Paper.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 20 % → 21 % | 59.0 px | 0.40 | 1.01 | 325 |
| heavy line | 20 % → 20 % | 58.1 px | 0.39 | 1.00 | 369 |
| pressure swell | 15 % → 15 % | 56.3 px | 0.36 | 1.02 | 250 |
| fast wave | 41 % → 42 % | 47.6 px | 0.31 | 1.03 | 1033 |
| slow wave | 45 % → 45 % | 51.8 px | 0.38 | 1.00 | 1796 |
| spiral | 50 % → 50 % | 33.3 px | 0.36 | 1.00 | 2131 |
| loop | 41 % → 41 % | 53.4 px | 0.38 | 1.00 | 878 |
| tilted | 18 % → 18 % | 48.9 px | 0.34 | 1.00 | 539 |
| over the wet one | 35 % → 35 % | 47.8 px | 0.34 | 1.00 | 415 |
| long, no reload | 68 % → 68 % | 30.6 px | 0.33 | 1.00 | 2647 | quarters: 0.00 → 0.00 → 0.00 → 0.01

Numbers say: light vs heavy: width 59.0 → 58.1 px, dark 0.40 → 0.39; pressure barely changes the width; the long stroke does not run out of paint.

## Surface test · Oil 40% Paper
Gouache 1.00 + turpentine 40 % · 70 px · 59.0 s

![Surface test · Oil 40% Paper](Surface-test-Oil-40-Paper.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 18 % → 17 % | 51.1 px | 0.40 | 0.96 | 279 |
| heavy line | 19 % → 18 % | 56.5 px | 0.41 | 0.91 | 476 |
| pressure swell | 15 % → 15 % | 55.6 px | 0.39 | 1.02 | 287 |
| fast wave | 34 % → 29 % | 39.4 px | 0.37 | 0.84 | 909 |
| slow wave | 39 % → 30 % | 44.9 px | 0.39 | 0.76 | 1389 |
| spiral | 47 % → 33 % | 30.8 px | 0.38 | 0.71 | 1634 |
| loop | 32 % → 29 % | 41.5 px | 0.40 | 0.90 | 710 |
| tilted | 16 % → 17 % | 44.5 px | 0.37 | 1.04 | 594 |
| over the wet one | 34 % → 33 % | 50.4 px | 0.37 | 0.96 | 504 |
| long, no reload | 54 % → 39 % | 24.0 px | 0.38 | 0.72 | 1954 | quarters: 0.00 → 0.01 → 0.01 → 0.01

Numbers say: light vs heavy: width 51.1 → 56.5 px, dark 0.40 → 0.41; pressure barely changes the width; the long stroke does not run out of paint.

## Surface test · Oil 80% Paper
Watercolour 0.93 · Ink 0.07 + turpentine 80 % · 70 px · 54.1 s

![Surface test · Oil 80% Paper](Surface-test-Oil-80-Paper.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 19 % → 24 % | 54.0 px | 0.09 | 1.27 | 364 |
| heavy line | 18 % → 25 % | 53.2 px | 0.09 | 1.35 | 384 |
| pressure swell | 15 % → 20 % | 56.6 px | 0.09 | 1.32 | 268 |
| fast wave | 36 % → 51 % | 41.2 px | 0.09 | 1.43 | 793 |
| slow wave | 33 % → 47 % | 37.8 px | 0.09 | 1.45 | 1316 |
| spiral | 42 % → 58 % | 27.9 px | 0.09 | 1.37 | 1506 |
| loop | 33 % → 47 % | 43.0 px | 0.09 | 1.42 | 648 |
| tilted | 15 % → 17 % | 42.3 px | 0.09 | 1.13 | 561 |
| over the wet one | 34 % → 42 % | 53.1 px | 0.09 | 1.24 | 449 |
| long, no reload | 51 % → 75 % | 23.1 px | 0.09 | 1.45 | 1865 | quarters: 0.08 → 0.09 → 0.07 → 0.06

Numbers say: light vs heavy: width 54.0 → 53.2 px, dark 0.09 → 0.09; pressure barely changes the width.

## Surface test · Dry scrub Paper
Gouache 1.00 + turpentine 20 % · 70 px · 43.5 s

![Surface test · Dry scrub Paper](Surface-test-Dry-scrub-Paper.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 13 % → 0 % | 36.7 px | 0.00 | 0.00 | 376 |
| heavy line | 28 % → 2 % | 80.6 px | 0.34 | 0.06 | 399 |
| pressure swell | 18 % → 7 % | 66.9 px | 0.35 | 0.38 | 275 |
| fast wave | 60 % → 18 % | 69.1 px | 0.28 | 0.29 | 1119 |
| slow wave | 42 % → 11 % | 48.9 px | 0.32 | 0.26 | 1698 |
| spiral | 67 % → 9 % | 44.3 px | 0.33 | 0.14 | 1892 |
| loop | 44 % → 2 % | 57.4 px | 0.29 | 0.05 | 1236 |
| tilted | 16 % → 16 % | 44.0 px | 0.28 | 1.00 | 450 |
| over the wet one | 35 % → 11 % | 52.5 px | 0.28 | 0.31 | 411 |
| long, no reload | 80 % → 17 % | 36.0 px | 0.30 | 0.21 | 2316 | quarters: 0.00 → 0.01 → 0.02 → 0.03

Numbers say: light vs heavy: width 36.7 → 80.6 px, dark 0.00 → 0.34; the long stroke does not run out of paint.

## Surface test · Watercolour Paper
Watercolour 1.00 + water 40 % · 60 px · 39.2 s

![Surface test · Watercolour Paper](Surface-test-Watercolour-Paper.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 8 % → 14 % | 24.2 px | 0.37 | 1.73 | 60 |
| heavy line | 16 % → 19 % | 47.6 px | 0.38 | 1.18 | 149 |
| pressure swell | 10 % → 13 % | 37.5 px | 0.40 | 1.30 | 77 |
| fast wave | 35 % → 39 % | 41.0 px | 0.35 | 1.11 | 332 |
| slow wave | 33 % → 38 % | 37.8 px | 0.37 | 1.15 | 484 |
| spiral | 55 % → 58 % | 36.2 px | 0.32 | 1.05 | 506 |
| loop | 28 % → 32 % | 36.7 px | 0.38 | 1.14 | 311 |
| tilted | 18 % → 18 % | 50.6 px | 0.37 | 1.00 | 238 |
| over the wet one | 30 % → 33 % | 33.2 px | 0.37 | 1.09 | 262 |
| long, no reload | 69 % → 72 % | 31.0 px | 0.31 | 1.05 | 826 | quarters: 0.35 → 0.25 → 0.20 → 0.15

Numbers say: light vs heavy: width 24.2 → 47.6 px, dark 0.37 → 0.38; wet paint spreads well beyond the stroke.

## Surface test · Surface test · paper
Gouache 1.00 + turpentine 40 % · 70 px · 58.3 s

![Surface test · Surface test · paper](Surface-test-Surface-test-paper.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 18 % → 17 % | 51.1 px | 0.40 | 0.96 | 293 |
| heavy line | 19 % → 18 % | 56.5 px | 0.41 | 0.91 | 367 |
| pressure swell | 15 % → 15 % | 55.6 px | 0.39 | 1.02 | 252 |
| fast wave | 34 % → 29 % | 39.4 px | 0.37 | 0.84 | 1037 |
| slow wave | 39 % → 30 % | 44.9 px | 0.39 | 0.76 | 1584 |
| spiral | 47 % → 33 % | 30.8 px | 0.38 | 0.71 | 1591 |
| loop | 32 % → 29 % | 41.5 px | 0.40 | 0.90 | 764 |
| tilted | 16 % → 17 % | 44.5 px | 0.37 | 1.04 | 437 |
| over the wet one | 34 % → 33 % | 50.4 px | 0.37 | 0.96 | 396 |
| long, no reload | 54 % → 39 % | 24.0 px | 0.38 | 0.72 | 2549 | quarters: 0.00 → 0.01 → 0.01 → 0.01

Numbers say: light vs heavy: width 51.1 → 56.5 px, dark 0.40 → 0.41; pressure barely changes the width; the long stroke does not run out of paint.

## Surface test · Under FineCanvas
Gouache 1.00 + turpentine 30 % · 60 px · 56.0 s

![Surface test · Under FineCanvas](Surface-test-Under-FineCanvas.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 16 % → 15 % | 46.4 px | 0.48 | 0.97 | 248 |
| heavy line | 16 % → 15 % | 46.8 px | 0.48 | 0.94 | 264 |
| pressure swell | 12 % → 13 % | 46.0 px | 0.49 | 1.07 | 210 |
| fast wave | 28 % → 24 % | 31.9 px | 0.50 | 0.86 | 871 |
| slow wave | 34 % → 27 % | 38.9 px | 0.48 | 0.79 | 1280 |
| spiral | 50 % → 31 % | 32.9 px | 0.46 | 0.62 | 1319 |
| loop | 26 % → 23 % | 33.1 px | 0.47 | 0.88 | 643 |
| tilted | 14 % → 15 % | 39.4 px | 0.50 | 1.03 | 395 |
| over the wet one | 29 % → 29 % | 41.8 px | 0.50 | 1.00 | 308 |
| long, no reload | 53 % → 33 % | 24.0 px | 0.48 | 0.62 | 2382 | quarters: 0.40 → 0.31 → 0.25 → 0.18

Numbers say: light vs heavy: width 46.4 → 46.8 px, dark 0.48 → 0.48; pressure barely changes the width.

## Surface test · Oil 0% FineCanvas
Oil 1.00 · 70 px · 35.5 s

![Surface test · Oil 0% FineCanvas](Surface-test-Oil-0-FineCanvas.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 20 % → 21 % | 59.1 px | 0.40 | 1.01 | 311 |
| heavy line | 20 % → 20 % | 58.0 px | 0.40 | 1.00 | 412 |
| pressure swell | 15 % → 15 % | 56.2 px | 0.36 | 1.02 | 266 |
| fast wave | 43 % → 44 % | 49.4 px | 0.32 | 1.03 | 1029 |
| slow wave | 45 % → 45 % | 51.9 px | 0.39 | 1.00 | 1650 |
| spiral | 51 % → 51 % | 33.4 px | 0.36 | 1.00 | 2994 |
| loop | 42 % → 42 % | 54.5 px | 0.38 | 1.00 | 749 |
| tilted | 18 % → 18 % | 50.0 px | 0.35 | 1.00 | 551 |
| over the wet one | 35 % → 35 % | 47.5 px | 0.35 | 1.00 | 358 |
| long, no reload | 70 % → 70 % | 31.6 px | 0.33 | 1.00 | 2388 | quarters: 0.00 → 0.00 → 0.00 → 0.00

Numbers say: light vs heavy: width 59.1 → 58.0 px, dark 0.40 → 0.40; pressure barely changes the width; the long stroke does not run out of paint.

## Surface test · Oil 40% FineCanvas
Gouache 1.00 + turpentine 40 % · 70 px · 61.4 s

![Surface test · Oil 40% FineCanvas](Surface-test-Oil-40-FineCanvas.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 18 % → 17 % | 51.5 px | 0.41 | 0.96 | 373 |
| heavy line | 20 % → 18 % | 57.6 px | 0.41 | 0.92 | 365 |
| pressure swell | 15 % → 16 % | 56.6 px | 0.39 | 1.03 | 259 |
| fast wave | 37 % → 28 % | 42.4 px | 0.36 | 0.77 | 1511 |
| slow wave | 41 % → 30 % | 47.1 px | 0.38 | 0.74 | 2024 |
| spiral | 49 % → 33 % | 32.3 px | 0.38 | 0.67 | 1919 |
| loop | 34 % → 30 % | 43.4 px | 0.40 | 0.89 | 715 |
| tilted | 17 % → 18 % | 47.8 px | 0.37 | 1.02 | 421 |
| over the wet one | 35 % → 33 % | 49.2 px | 0.37 | 0.95 | 333 |
| long, no reload | 58 % → 38 % | 25.8 px | 0.38 | 0.66 | 1963 | quarters: 0.00 → 0.01 → 0.01 → 0.01

Numbers say: light vs heavy: width 51.5 → 57.6 px, dark 0.41 → 0.41; the long stroke does not run out of paint.

## Surface test · Oil 80% FineCanvas
Watercolour 0.93 · Ink 0.07 + turpentine 80 % · 70 px · 57.3 s

![Surface test · Oil 80% FineCanvas](Surface-test-Oil-80-FineCanvas.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 19 % → 24 % | 54.2 px | 0.09 | 1.27 | 265 |
| heavy line | 19 % → 25 % | 54.1 px | 0.09 | 1.35 | 293 |
| pressure swell | 15 % → 20 % | 57.4 px | 0.09 | 1.32 | 352 |
| fast wave | 40 % → 52 % | 46.5 px | 0.09 | 1.30 | 1440 |
| slow wave | 36 % → 49 % | 42.0 px | 0.09 | 1.34 | 1406 |
| spiral | 46 % → 58 % | 30.3 px | 0.09 | 1.26 | 1783 |
| loop | 36 % → 49 % | 46.5 px | 0.09 | 1.37 | 664 |
| tilted | 17 % → 17 % | 46.6 px | 0.09 | 1.04 | 463 |
| over the wet one | 35 % → 43 % | 49.9 px | 0.09 | 1.25 | 337 |
| long, no reload | 59 % → 77 % | 26.4 px | 0.09 | 1.31 | 2043 | quarters: 0.08 → 0.09 → 0.08 → 0.06

Numbers say: light vs heavy: width 54.2 → 54.1 px, dark 0.09 → 0.09; pressure barely changes the width.

## Surface test · Dry scrub FineCanvas
Gouache 1.00 + turpentine 20 % · 70 px · 42.9 s

![Surface test · Dry scrub FineCanvas](Surface-test-Dry-scrub-FineCanvas.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 13 % → 0 % | 36.7 px | 0.00 | 0.00 | 273 |
| heavy line | 28 % → 2 % | 80.7 px | 0.34 | 0.07 | 436 |
| pressure swell | 18 % → 7 % | 68.2 px | 0.35 | 0.39 | 300 |
| fast wave | 61 % → 23 % | 70.5 px | 0.28 | 0.38 | 1141 |
| slow wave | 43 % → 15 % | 49.5 px | 0.32 | 0.36 | 1667 |
| spiral | 69 % → 12 % | 45.3 px | 0.32 | 0.18 | 2203 |
| loop | 44 % → 3 % | 57.4 px | 0.29 | 0.07 | 949 |
| tilted | 16 % → 16 % | 44.5 px | 0.28 | 1.00 | 489 |
| over the wet one | 35 % → 13 % | 52.5 px | 0.28 | 0.37 | 409 |
| long, no reload | 87 % → 18 % | 39.0 px | 0.30 | 0.20 | 2277 | quarters: 0.00 → 0.01 → 0.01 → 0.02

Numbers say: light vs heavy: width 36.7 → 80.7 px, dark 0.00 → 0.34; the long stroke does not run out of paint.

## Surface test · Watercolour FineCanvas
Watercolour 1.00 + water 40 % · 60 px · 42.4 s

![Surface test · Watercolour FineCanvas](Surface-test-Watercolour-FineCanvas.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 8 % → 15 % | 24.2 px | 0.38 | 1.74 | 65 |
| heavy line | 16 % → 19 % | 47.6 px | 0.38 | 1.18 | 162 |
| pressure swell | 10 % → 13 % | 37.6 px | 0.40 | 1.30 | 90 |
| fast wave | 36 % → 40 % | 41.2 px | 0.36 | 1.12 | 477 |
| slow wave | 33 % → 39 % | 38.1 px | 0.38 | 1.17 | 654 |
| spiral | 56 % → 59 % | 36.9 px | 0.33 | 1.05 | 506 |
| loop | 28 % → 33 % | 36.8 px | 0.39 | 1.16 | 302 |
| tilted | 18 % → 18 % | 51.2 px | 0.38 | 1.00 | 182 |
| over the wet one | 30 % → 33 % | 33.1 px | 0.38 | 1.10 | 120 |
| long, no reload | 72 % → 75 % | 32.5 px | 0.31 | 1.04 | 936 | quarters: 0.36 → 0.27 → 0.21 → 0.16

Numbers say: light vs heavy: width 24.2 → 47.6 px, dark 0.38 → 0.38; wet paint spreads well beyond the stroke.

## Surface test · Surface test · fine canvas
Gouache 1.00 + turpentine 40 % · 70 px · 64.7 s

![Surface test · Surface test · fine canvas](Surface-test-Surface-test-fine-canvas.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 18 % → 17 % | 51.5 px | 0.41 | 0.96 | 286 |
| heavy line | 20 % → 18 % | 57.6 px | 0.41 | 0.92 | 457 |
| pressure swell | 15 % → 16 % | 56.6 px | 0.39 | 1.03 | 297 |
| fast wave | 37 % → 28 % | 42.4 px | 0.36 | 0.77 | 944 |
| slow wave | 41 % → 30 % | 47.1 px | 0.38 | 0.74 | 1529 |
| spiral | 49 % → 33 % | 32.3 px | 0.38 | 0.67 | 1531 |
| loop | 34 % → 30 % | 43.4 px | 0.40 | 0.89 | 859 |
| tilted | 17 % → 18 % | 47.8 px | 0.37 | 1.02 | 714 |
| over the wet one | 35 % → 33 % | 49.2 px | 0.37 | 0.95 | 653 |
| long, no reload | 58 % → 38 % | 25.8 px | 0.38 | 0.66 | 2101 | quarters: 0.00 → 0.01 → 0.01 → 0.01

Numbers say: light vs heavy: width 51.5 → 57.6 px, dark 0.41 → 0.41; the long stroke does not run out of paint.

## Surface test · Under CoarseLinen
Gouache 1.00 + turpentine 30 % · 60 px · 57.1 s

![Surface test · Under CoarseLinen](Surface-test-Under-CoarseLinen.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 16 % → 15 % | 46.3 px | 0.48 | 0.97 | 310 |
| heavy line | 16 % → 15 % | 46.6 px | 0.48 | 0.94 | 296 |
| pressure swell | 12 % → 13 % | 45.8 px | 0.50 | 1.07 | 226 |
| fast wave | 27 % → 25 % | 31.2 px | 0.51 | 0.92 | 805 |
| slow wave | 33 % → 27 % | 38.5 px | 0.48 | 0.82 | 1371 |
| spiral | 49 % → 33 % | 32.4 px | 0.46 | 0.67 | 1259 |
| loop | 25 % → 23 % | 32.6 px | 0.48 | 0.91 | 721 |
| tilted | 14 % → 14 % | 39.1 px | 0.51 | 1.03 | 623 |
| over the wet one | 29 % → 29 % | 41.8 px | 0.51 | 1.00 | 549 |
| long, no reload | 52 % → 36 % | 23.5 px | 0.49 | 0.69 | 1869 | quarters: 0.40 → 0.30 → 0.25 → 0.18

Numbers say: light vs heavy: width 46.3 → 46.6 px, dark 0.48 → 0.48; pressure barely changes the width.

## Surface test · Oil 0% CoarseLinen
Oil 1.00 · 70 px · 32.7 s

![Surface test · Oil 0% CoarseLinen](Surface-test-Oil-0-CoarseLinen.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 20 % → 21 % | 59.1 px | 0.40 | 1.01 | 457 |
| heavy line | 20 % → 20 % | 58.0 px | 0.40 | 1.00 | 379 |
| pressure swell | 15 % → 15 % | 56.2 px | 0.36 | 1.02 | 233 |
| fast wave | 42 % → 44 % | 49.0 px | 0.32 | 1.03 | 1013 |
| slow wave | 45 % → 45 % | 51.9 px | 0.39 | 1.00 | 1622 |
| spiral | 51 % → 51 % | 33.4 px | 0.36 | 1.00 | 1781 |
| loop | 42 % → 42 % | 54.3 px | 0.38 | 1.00 | 782 |
| tilted | 18 % → 18 % | 49.7 px | 0.34 | 1.00 | 801 |
| over the wet one | 35 % → 35 % | 47.5 px | 0.34 | 1.00 | 529 |
| long, no reload | 70 % → 70 % | 31.2 px | 0.33 | 1.00 | 2411 | quarters: 0.00 → 0.00 → 0.00 → 0.01

Numbers say: light vs heavy: width 59.1 → 58.0 px, dark 0.40 → 0.40; pressure barely changes the width; the long stroke does not run out of paint.

## Surface test · Oil 40% CoarseLinen
Gouache 1.00 + turpentine 40 % · 70 px · 60.7 s

![Surface test · Oil 40% CoarseLinen](Surface-test-Oil-40-CoarseLinen.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 18 % → 17 % | 51.4 px | 0.41 | 0.96 | 288 |
| heavy line | 20 % → 18 % | 57.4 px | 0.41 | 0.92 | 337 |
| pressure swell | 15 % → 15 % | 56.4 px | 0.39 | 1.03 | 226 |
| fast wave | 36 % → 30 % | 41.8 px | 0.37 | 0.82 | 920 |
| slow wave | 40 % → 31 % | 46.7 px | 0.39 | 0.76 | 1720 |
| spiral | 48 % → 33 % | 31.6 px | 0.39 | 0.70 | 1640 |
| loop | 33 % → 30 % | 42.8 px | 0.40 | 0.90 | 733 |
| tilted | 17 % → 17 % | 47.3 px | 0.37 | 1.02 | 455 |
| over the wet one | 35 % → 33 % | 49.3 px | 0.37 | 0.97 | 363 |
| long, no reload | 57 % → 40 % | 25.5 px | 0.38 | 0.70 | 2531 | quarters: 0.00 → 0.01 → 0.01 → 0.01

Numbers say: light vs heavy: width 51.4 → 57.4 px, dark 0.41 → 0.41; the long stroke does not run out of paint.

## Surface test · Oil 80% CoarseLinen
Watercolour 0.93 · Ink 0.07 + turpentine 80 % · 70 px · 57.1 s

![Surface test · Oil 80% CoarseLinen](Surface-test-Oil-80-CoarseLinen.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 19 % → 24 % | 54.2 px | 0.09 | 1.27 | 354 |
| heavy line | 19 % → 25 % | 54.0 px | 0.09 | 1.35 | 365 |
| pressure swell | 15 % → 20 % | 57.2 px | 0.09 | 1.32 | 203 |
| fast wave | 39 % → 52 % | 44.8 px | 0.09 | 1.35 | 914 |
| slow wave | 35 % → 48 % | 40.8 px | 0.09 | 1.37 | 1375 |
| spiral | 45 % → 59 % | 29.7 px | 0.09 | 1.30 | 1472 |
| loop | 35 % → 49 % | 45.4 px | 0.09 | 1.38 | 690 |
| tilted | 16 % → 17 % | 45.2 px | 0.09 | 1.07 | 624 |
| over the wet one | 35 % → 43 % | 51.1 px | 0.09 | 1.24 | 442 |
| long, no reload | 58 % → 77 % | 25.9 px | 0.09 | 1.33 | 2064 | quarters: 0.08 → 0.09 → 0.08 → 0.06

Numbers say: light vs heavy: width 54.2 → 54.0 px, dark 0.09 → 0.09; pressure barely changes the width.

## Surface test · Dry scrub CoarseLinen
Gouache 1.00 + turpentine 20 % · 70 px · 45.3 s

![Surface test · Dry scrub CoarseLinen](Surface-test-Dry-scrub-CoarseLinen.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 13 % → 0 % | 36.7 px | 0.00 | 0.00 | 281 |
| heavy line | 28 % → 2 % | 80.7 px | 0.33 | 0.07 | 426 |
| pressure swell | 18 % → 7 % | 68.0 px | 0.35 | 0.38 | 317 |
| fast wave | 61 % → 22 % | 70.2 px | 0.28 | 0.36 | 1522 |
| slow wave | 43 % → 14 % | 49.4 px | 0.32 | 0.33 | 1647 |
| spiral | 68 % → 11 % | 45.1 px | 0.32 | 0.16 | 1841 |
| loop | 44 % → 3 % | 57.4 px | 0.29 | 0.07 | 1628 |
| tilted | 16 % → 16 % | 44.5 px | 0.28 | 1.01 | 957 |
| over the wet one | 35 % → 12 % | 52.6 px | 0.28 | 0.36 | 403 |
| long, no reload | 85 % → 17 % | 37.9 px | 0.30 | 0.21 | 2291 | quarters: 0.00 → 0.01 → 0.01 → 0.02

Numbers say: light vs heavy: width 36.7 → 80.7 px, dark 0.00 → 0.33; the long stroke does not run out of paint.

## Surface test · Watercolour CoarseLinen
Watercolour 1.00 + water 40 % · 60 px · 41.5 s

![Surface test · Watercolour CoarseLinen](Surface-test-Watercolour-CoarseLinen.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 8 % → 14 % | 24.2 px | 0.38 | 1.74 | 67 |
| heavy line | 16 % → 19 % | 47.7 px | 0.38 | 1.18 | 162 |
| pressure swell | 10 % → 13 % | 37.5 px | 0.40 | 1.30 | 101 |
| fast wave | 36 % → 40 % | 41.1 px | 0.36 | 1.11 | 339 |
| slow wave | 33 % → 38 % | 38.0 px | 0.37 | 1.17 | 497 |
| spiral | 56 % → 59 % | 36.8 px | 0.32 | 1.05 | 474 |
| loop | 28 % → 33 % | 36.8 px | 0.39 | 1.15 | 385 |
| tilted | 18 % → 18 % | 51.0 px | 0.37 | 1.00 | 318 |
| over the wet one | 30 % → 33 % | 33.2 px | 0.37 | 1.10 | 274 |
| long, no reload | 71 % → 74 % | 32.0 px | 0.31 | 1.04 | 810 | quarters: 0.36 → 0.27 → 0.21 → 0.16

Numbers say: light vs heavy: width 24.2 → 47.7 px, dark 0.38 → 0.38; wet paint spreads well beyond the stroke.

## Surface test · Surface test · coarse linen
Gouache 1.00 + turpentine 40 % · 70 px · 61.2 s

![Surface test · Surface test · coarse linen](Surface-test-Surface-test-coarse-linen.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 18 % → 17 % | 51.4 px | 0.41 | 0.96 | 268 |
| heavy line | 20 % → 18 % | 57.4 px | 0.41 | 0.92 | 363 |
| pressure swell | 15 % → 15 % | 56.4 px | 0.39 | 1.03 | 238 |
| fast wave | 36 % → 30 % | 41.8 px | 0.37 | 0.82 | 882 |
| slow wave | 40 % → 31 % | 46.7 px | 0.39 | 0.76 | 2216 |
| spiral | 48 % → 33 % | 31.6 px | 0.39 | 0.70 | 1509 |
| loop | 33 % → 30 % | 42.8 px | 0.40 | 0.90 | 718 |
| tilted | 17 % → 17 % | 47.3 px | 0.37 | 1.02 | 427 |
| over the wet one | 35 % → 33 % | 49.3 px | 0.37 | 0.97 | 361 |
| long, no reload | 57 % → 40 % | 25.5 px | 0.38 | 0.70 | 2532 | quarters: 0.00 → 0.01 → 0.01 → 0.01

Numbers say: light vs heavy: width 51.4 → 57.4 px, dark 0.41 → 0.41; the long stroke does not run out of paint.

## v3 · Any shape · K stamp
Gouache 1.00 · 48 px · 56.3 s

![v3 · Any shape · K stamp](v3-Any-shape-K-stamp.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 20 % → 19 % | 59.0 px | 0.40 | 0.92 | 279 |
| heavy line | 20 % → 19 % | 59.2 px | 0.40 | 0.94 | 271 |
| pressure swell | 12 % → 11 % | 43.7 px | 0.40 | 0.98 | 202 |
| fast wave | 42 % → 34 % | 48.1 px | 0.40 | 0.83 | 879 |
| slow wave | 42 % → 34 % | 48.3 px | 0.40 | 0.80 | 1745 |
| spiral | 66 % → 47 % | 43.6 px | 0.40 | 0.72 | 1254 |
| loop | 37 % → 34 % | 48.2 px | 0.40 | 0.91 | 592 |
| tilted | 15 % → 15 % | 42.0 px | 0.40 | 1.00 | 320 |
| over the wet one | 33 % → 32 % | 51.3 px | 0.40 | 0.95 | 267 |
| long, no reload | 81 % → 50 % | 36.5 px | 0.40 | 0.61 | 2124 | quarters: 0.35 → 0.35 → 0.33 → 0.30

Numbers say: light vs heavy: width 59.0 → 59.2 px, dark 0.40 → 0.40; pressure barely changes the width; the long stroke does not run out of paint.

## v3 · Any shape · K of hairs
Oil 1.00 · 48 px · 23.3 s

![v3 · Any shape · K of hairs](v3-Any-shape-K-of-hairs.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 20 % → 20 % | 56.7 px | 0.47 | 1.00 | 346 |
| heavy line | 28 % → 28 % | 80.7 px | 0.47 | 1.00 | 413 |
| pressure swell | 16 % → 16 % | 59.3 px | 0.48 | 1.01 | 162 |
| fast wave | 49 % → 50 % | 56.2 px | 0.46 | 1.04 | 586 |
| slow wave | 50 % → 50 % | 57.9 px | 0.48 | 1.00 | 1399 |
| spiral | 67 % → 67 % | 44.0 px | 0.46 | 1.00 | 891 |
| loop | 45 % → 45 % | 58.6 px | 0.48 | 1.00 | 470 |
| tilted | 16 % → 16 % | 45.9 px | 0.48 | 1.00 | 246 |
| over the wet one | 40 % → 40 % | 64.9 px | 0.48 | 1.00 | 245 |
| long, no reload | 83 % → 83 % | 37.4 px | 0.43 | 1.00 | 1409 | quarters: 0.48 → 0.44 → 0.35 → 0.26

Numbers say: light vs heavy: width 56.7 → 80.7 px, dark 0.47 → 0.47.

## v3 · Any shape · Star stamp
Gouache 1.00 · 44 px · 47.5 s

![v3 · Any shape · Star stamp](v3-Any-shape-Star-stamp.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 13 % → 11 % | 37.9 px | 0.36 | 0.83 | 200 |
| heavy line | 13 % → 12 % | 38.5 px | 0.36 | 0.87 | 153 |
| pressure swell | 10 % → 10 % | 39.2 px | 0.36 | 0.93 | 99 |
| fast wave | 33 % → 27 % | 38.0 px | 0.36 | 0.83 | 407 |
| slow wave | 33 % → 26 % | 38.4 px | 0.35 | 0.79 | 680 |
| spiral | 56 % → 42 % | 37.2 px | 0.35 | 0.74 | 640 |
| loop | 28 % → 24 % | 36.0 px | 0.36 | 0.88 | 335 |
| tilted | 13 % → 13 % | 37.0 px | 0.36 | 1.01 | 254 |
| over the wet one | 26 % → 24 % | 36.4 px | 0.36 | 0.90 | 238 |
| long, no reload | 68 % → 47 % | 30.5 px | 0.35 | 0.69 | 1025 | quarters: 0.01 → 0.01 → 0.01 → 0.01

Numbers say: light vs heavy: width 37.9 → 38.5 px, dark 0.36 → 0.36; pressure barely changes the width; the long stroke does not run out of paint.

## v3 · Any shape · Star of hairs
Oil 1.00 · 44 px · 21.1 s

![v3 · Any shape · Star of hairs](v3-Any-shape-Star-of-hairs.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 15 % → 15 % | 43.7 px | 0.34 | 1.00 | 172 |
| heavy line | 23 % → 23 % | 67.9 px | 0.33 | 1.00 | 207 |
| pressure swell | 14 % → 14 % | 53.1 px | 0.35 | 1.00 | 134 |
| fast wave | 45 % → 46 % | 52.1 px | 0.32 | 1.01 | 447 |
| slow wave | 44 % → 44 % | 50.8 px | 0.33 | 1.00 | 845 |
| spiral | 63 % → 63 % | 41.8 px | 0.32 | 1.00 | 783 |
| loop | 39 % → 39 % | 50.5 px | 0.33 | 1.00 | 408 |
| tilted | 14 % → 14 % | 39.1 px | 0.34 | 1.00 | 228 |
| over the wet one | 34 % → 34 % | 55.6 px | 0.34 | 1.00 | 187 |
| long, no reload | 79 % → 79 % | 35.4 px | 0.30 | 1.00 | 2100 | quarters: 0.32 → 0.29 → 0.24 → 0.18

Numbers say: light vs heavy: width 43.7 → 67.9 px, dark 0.34 → 0.33.

## v3 · Any shape · Rag
Oil 1.00 · 60 px · 27.8 s

![v3 · Any shape · Rag](v3-Any-shape-Rag.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 34 % → 37 % | 98.5 px | 0.29 | 1.08 | 268 |
| heavy line | 41 % → 41 % | 118.0 px | 0.30 | 1.00 | 357 |
| pressure swell | 31 % → 33 % | 116.1 px | 0.29 | 1.05 | 250 |
| fast wave | 69 % → 74 % | 80.2 px | 0.29 | 1.07 | 860 |
| slow wave | 72 % → 72 % | 83.4 px | 0.30 | 1.00 | 2243 |
| spiral | 83 % → 83 % | 54.7 px | 0.30 | 1.00 | 1936 |
| loop | 62 % → 62 % | 80.3 px | 0.31 | 1.00 | 932 |
| tilted | 23 % → 23 % | 63.2 px | 0.30 | 1.00 | 396 |
| over the wet one | 56 % → 58 % | 93.3 px | 0.30 | 1.03 | 350 |
| long, no reload | 94 % → 94 % | 42.2 px | 0.30 | 1.00 | 2119 | quarters: 0.35 → 0.32 → 0.28 → 0.22

Numbers say: light vs heavy: width 98.5 → 118.0 px, dark 0.29 → 0.30.

## v3 · Any shape · Dry oil on canvas
Oil 1.00 · 40 px · 19.4 s

![v3 · Any shape · Dry oil on canvas](v3-Any-shape-Dry-oil-on-canvas.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 11 % → 11 % | 33.2 px | 0.31 | 1.00 | 183 |
| heavy line | 13 % → 13 % | 38.9 px | 0.33 | 1.00 | 181 |
| pressure swell | 10 % → 10 % | 38.4 px | 0.32 | 1.00 | 88 |
| fast wave | 28 % → 28 % | 32.6 px | 0.30 | 1.00 | 395 |
| slow wave | 32 % → 32 % | 37.5 px | 0.31 | 1.00 | 624 |
| spiral | 48 % → 48 % | 31.8 px | 0.28 | 1.00 | 576 |
| loop | 27 % → 27 % | 34.4 px | 0.31 | 1.00 | 284 |
| tilted | 9 % → 9 % | 25.3 px | 0.31 | 1.00 | 150 |
| over the wet one | 22 % → 22 % | 36.3 px | 0.31 | 1.00 | 146 |
| long, no reload | 55 % → 55 % | 24.7 px | 0.25 | 1.00 | 832 | quarters: 0.00 → 0.00 → 0.00 → 0.00

Numbers say: light vs heavy: width 33.2 → 38.9 px, dark 0.31 → 0.33; the long stroke does not run out of paint.

## v3 · Any shape · Two colours streaks
Oil 1.00 · 44 px · 25.0 s

![v3 · Any shape · Two colours streaks](v3-Any-shape-Two-colours-streaks.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 14 % → 14 % | 39.7 px | 0.35 | 1.00 | 209 |
| heavy line | 16 % → 16 % | 46.1 px | 0.31 | 1.00 | 181 |
| pressure swell | 11 % → 11 % | 42.8 px | 0.39 | 1.00 | 139 |
| fast wave | 37 % → 37 % | 43.1 px | 0.34 | 1.00 | 663 |
| slow wave | 35 % → 35 % | 40.8 px | 0.30 | 1.00 | 1268 |
| spiral | 61 % → 61 % | 40.5 px | 0.35 | 1.00 | 934 |
| loop | 32 % → 32 % | 41.1 px | 0.32 | 1.00 | 418 |
| tilted | 13 % → 13 % | 37.2 px | 0.36 | 1.00 | 299 |
| over the wet one | 27 % → 27 % | 39.2 px | 0.36 | 1.00 | 214 |
| long, no reload | 73 % → 73 % | 32.8 px | 0.32 | 1.00 | 1205 | quarters: 0.29 → 0.28 → 0.25 → 0.20

Numbers say: light vs heavy: width 39.7 → 46.1 px, dark 0.35 → 0.31.

## Watercolour · Wash
Watercolour 1.00 + water 65 % · 60 px · 56.8 s

![Watercolour · Wash](Watercolour-Wash.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 15 % → 19 % | 43.3 px | 0.14 | 1.27 | 165 |
| heavy line | 30 % → 30 % | 86.4 px | 0.13 | 1.01 | 285 |
| pressure swell | 18 % → 19 % | 68.1 px | 0.17 | 1.07 | 208 |
| fast wave | 57 % → 60 % | 65.7 px | 0.13 | 1.05 | 883 |
| slow wave | 53 % → 55 % | 61.3 px | 0.14 | 1.03 | 2641 |
| spiral | 70 % → 71 % | 45.9 px | 0.11 | 1.01 | 2074 |
| loop | 46 % → 48 % | 60.0 px | 0.14 | 1.03 | 486 |
| tilted | 21 % → 21 % | 57.5 px | 0.15 | 1.01 | 385 |
| over the wet one | 42 % → 45 % | 60.4 px | 0.15 | 1.07 | 290 |
| long, no reload | 88 % → 90 % | 39.2 px | 0.10 | 1.03 | 2183 | quarters: 0.15 → 0.11 → 0.07 → 0.04

Numbers say: light vs heavy: width 43.3 → 86.4 px, dark 0.14 → 0.13.

## Watercolour · Wet-in-wet
Watercolour 1.00 + water 80 % · 60 px · 69.7 s

![Watercolour · Wet-in-wet](Watercolour-Wet-in-wet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 13 % → 30 % | 37.7 px | 0.18 | 2.34 | 126 |
| heavy line | 25 % → 39 % | 73.8 px | 0.20 | 1.52 | 321 |
| pressure swell | 16 % → 28 % | 58.1 px | 0.23 | 1.79 | 370 |
| fast wave | 49 % → 73 % | 56.1 px | 0.21 | 1.50 | 1293 |
| slow wave | 47 % → 69 % | 54.5 px | 0.22 | 1.46 | 909 |
| spiral | 66 % → 80 % | 43.8 px | 0.19 | 1.20 | 1081 |
| loop | 43 % → 60 % | 55.2 px | 0.23 | 1.40 | 678 |
| tilted | 20 % → 21 % | 55.5 px | 0.19 | 1.03 | 281 |
| over the wet one | 40 % → 64 % | 56.3 px | 0.19 | 1.59 | 263 |
| long, no reload | 84 % → 97 % | 37.5 px | 0.19 | 1.16 | 1444 | quarters: 0.33 → 0.22 → 0.14 → 0.08

Numbers say: light vs heavy: width 37.7 → 73.8 px, dark 0.18 → 0.20; wet paint spreads well beyond the stroke.

## Watercolour · Glaze
Watercolour 1.00 + water 75 % · 50 px · 50.1 s

![Watercolour · Glaze](Watercolour-Glaze.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 13 % → 17 % | 38.1 px | 0.03 | 1.29 | 139 |
| heavy line | 26 % → 27 % | 74.6 px | 0.03 | 1.04 | 230 |
| pressure swell | 16 % → 18 % | 60.1 px | 0.03 | 1.11 | 157 |
| fast wave | 50 % → 54 % | 57.9 px | 0.03 | 1.08 | 812 |
| slow wave | 46 % → 50 % | 53.3 px | 0.03 | 1.08 | 841 |
| spiral | 62 % → 66 % | 41.1 px | 0.02 | 1.06 | 959 |
| loop | 42 % → 44 % | 54.1 px | 0.03 | 1.06 | 448 |
| tilted | 17 % → 17 % | 46.8 px | 0.03 | 1.04 | 266 |
| over the wet one | 37 % → 41 % | 57.5 px | 0.03 | 1.09 | 249 |
| long, no reload | 78 % → 86 % | 34.9 px | 0.02 | 1.10 | 1315 | quarters: 0.04 → 0.02 → 0.01 → 0.01

Numbers say: light vs heavy: width 38.1 → 74.6 px, dark 0.03 → 0.03.

## Watercolour · Granulating
Watercolour 1.00 + water 60 % · 56 px · 53.5 s

![Watercolour · Granulating](Watercolour-Granulating.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 14 % → 18 % | 40.6 px | 0.20 | 1.28 | 221 |
| heavy line | 28 % → 28 % | 80.2 px | 0.18 | 1.01 | 249 |
| pressure swell | 17 % → 18 % | 62.9 px | 0.24 | 1.07 | 179 |
| fast wave | 53 % → 55 % | 61.1 px | 0.18 | 1.04 | 611 |
| slow wave | 51 % → 52 % | 58.5 px | 0.19 | 1.03 | 953 |
| spiral | 67 % → 68 % | 44.3 px | 0.15 | 1.01 | 1009 |
| loop | 45 % → 46 % | 58.1 px | 0.20 | 1.03 | 495 |
| tilted | 20 % → 20 % | 54.5 px | 0.22 | 1.01 | 443 |
| over the wet one | 40 % → 43 % | 57.5 px | 0.22 | 1.06 | 360 |
| long, no reload | 87 % → 89 % | 38.9 px | 0.15 | 1.03 | 1445 | quarters: 0.23 → 0.17 → 0.10 → 0.06

Numbers say: light vs heavy: width 40.6 → 80.2 px, dark 0.20 → 0.18.

## Watercolour · Dry brush
Watercolour 1.00 + water 35 % · 44 px · 45.3 s

![Watercolour · Dry brush](Watercolour-Dry-brush.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 6 % → 2 % | 16.0 px | 0.01 | 0.40 | 99 |
| heavy line | 19 % → 19 % | 56.3 px | 0.10 | 1.00 | 216 |
| pressure swell | 14 % → 15 % | 54.3 px | 0.09 | 1.03 | 124 |
| fast wave | 47 % → 47 % | 54.2 px | 0.03 | 1.00 | 673 |
| slow wave | 38 % → 38 % | 43.8 px | 0.05 | 1.01 | 713 |
| spiral | 62 % → 63 % | 41.2 px | 0.03 | 1.01 | 770 |
| loop | 33 % → 31 % | 42.8 px | 0.02 | 0.95 | 354 |
| tilted | 11 % → 12 % | 31.7 px | 0.07 | 1.04 | 212 |
| over the wet one | 29 % → 29 % | 48.7 px | 0.07 | 1.01 | 185 |
| long, no reload | 72 % → 67 % | 32.3 px | 0.03 | 0.93 | 1550 | quarters: 0.03 → 0.01 → 0.02 → 0.03

Numbers say: light vs heavy: width 16.0 → 56.3 px, dark 0.01 → 0.10.

## Watercolour · Runs
Watercolour 1.00 + water 80 % · 60 px · 71.4 s

![Watercolour · Runs](Watercolour-Runs.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 26 % → 36 % | 75.2 px | 0.35 | 1.38 | 149 |
| heavy line | 39 % → 42 % | 114.4 px | 0.38 | 1.06 | 345 |
| pressure swell | 17 % → 28 % | 64.3 px | 0.42 | 1.63 | 237 |
| fast wave | 64 % → 74 % | 73.6 px | 0.41 | 1.16 | 1033 |
| slow wave | 56 % → 68 % | 64.9 px | 0.43 | 1.21 | 2672 |
| spiral | 73 % → 82 % | 47.9 px | 0.42 | 1.13 | 1108 |
| loop | 60 % → 69 % | 78.2 px | 0.42 | 1.14 | 637 |
| tilted | 30 % → 31 % | 84.7 px | 0.38 | 1.02 | 389 |
| over the wet one | 56 % → 67 % | 70.4 px | 0.38 | 1.21 | 288 |
| long, no reload | 89 % → 99 % | 40.1 px | 0.43 | 1.11 | 2090 | quarters: 0.57 → 0.50 → 0.40 → 0.26

Numbers say: light vs heavy: width 75.2 → 114.4 px, dark 0.35 → 0.38; wet paint spreads well beyond the stroke.

## Watercolour · Two-tone
Watercolour 1.00 + water 60 % · 56 px · 57.9 s

![Watercolour · Two-tone](Watercolour-Two-tone.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 15 % → 18 % | 43.8 px | 0.55 | 1.23 | 140 |
| heavy line | 30 % → 30 % | 85.9 px | 0.57 | 1.01 | 241 |
| pressure swell | 18 % → 19 % | 65.9 px | 0.57 | 1.06 | 199 |
| fast wave | 56 % → 59 % | 64.5 px | 0.53 | 1.05 | 700 |
| slow wave | 52 % → 53 % | 60.1 px | 0.56 | 1.03 | 1070 |
| spiral | 69 % → 69 % | 45.2 px | 0.31 | 1.01 | 1736 |
| loop | 47 % → 48 % | 60.9 px | 0.53 | 1.03 | 509 |
| tilted | 19 % → 19 % | 52.9 px | 0.53 | 1.01 | 269 |
| over the wet one | 41 % → 43 % | 61.7 px | 0.53 | 1.06 | 345 |
| long, no reload | 86 % → 89 % | 38.5 px | 0.18 | 1.03 | 1813 | quarters: 0.27 → 0.21 → 0.14 → 0.08

Numbers say: light vs heavy: width 43.8 → 85.9 px, dark 0.55 → 0.57.

## Watercolour · SH blue
Watercolour 1.00 + water 30 % · 46 px · 42.2 s

![Watercolour · SH blue](Watercolour-SH-blue.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 6 % → 13 % | 18.7 px | 0.40 | 2.04 | 63 |
| heavy line | 13 % → 17 % | 37.9 px | 0.41 | 1.30 | 140 |
| pressure swell | 8 % → 12 % | 29.8 px | 0.45 | 1.49 | 84 |
| fast wave | 29 % → 34 % | 33.0 px | 0.45 | 1.21 | 336 |
| slow wave | 26 % → 32 % | 30.0 px | 0.39 | 1.24 | 458 |
| spiral | 44 % → 50 % | 28.9 px | 0.31 | 1.14 | 473 |
| loop | 23 % → 29 % | 29.2 px | 0.41 | 1.28 | 360 |
| tilted | 15 % → 15 % | 42.1 px | 0.39 | 1.00 | 220 |
| over the wet one | 25 % → 30 % | 27.6 px | 0.39 | 1.18 | 158 |
| long, no reload | 59 % → 63 % | 26.3 px | 0.30 | 1.08 | 924 | quarters: 0.32 → 0.22 → 0.17 → 0.12

Numbers say: light vs heavy: width 18.7 → 37.9 px, dark 0.40 → 0.41; wet paint spreads well beyond the stroke.

## Watercolour · SH violet
Watercolour 1.00 + water 30 % · 46 px · 43.9 s

![Watercolour · SH violet](Watercolour-SH-violet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 6 % → 13 % | 18.7 px | 0.59 | 2.04 | 71 |
| heavy line | 13 % → 17 % | 37.9 px | 0.60 | 1.30 | 150 |
| pressure swell | 8 % → 12 % | 29.8 px | 0.62 | 1.49 | 97 |
| fast wave | 29 % → 34 % | 33.0 px | 0.63 | 1.21 | 598 |
| slow wave | 26 % → 32 % | 30.0 px | 0.59 | 1.24 | 755 |
| spiral | 44 % → 50 % | 28.9 px | 0.53 | 1.14 | 822 |
| loop | 23 % → 29 % | 29.2 px | 0.60 | 1.28 | 247 |
| tilted | 15 % → 15 % | 42.1 px | 0.58 | 1.00 | 257 |
| over the wet one | 25 % → 30 % | 27.6 px | 0.58 | 1.18 | 168 |
| long, no reload | 59 % → 63 % | 26.3 px | 0.51 | 1.08 | 773 | quarters: 0.46 → 0.38 → 0.31 → 0.24

Numbers say: light vs heavy: width 18.7 → 37.9 px, dark 0.59 → 0.60; wet paint spreads well beyond the stroke.

## Watercolour · SH teal
Watercolour 1.00 + water 30 % · 46 px · 41.3 s

![Watercolour · SH teal](Watercolour-SH-teal.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 6 % → 13 % | 18.7 px | 0.21 | 2.04 | 67 |
| heavy line | 13 % → 17 % | 37.9 px | 0.22 | 1.30 | 146 |
| pressure swell | 8 % → 12 % | 29.8 px | 0.25 | 1.49 | 131 |
| fast wave | 29 % → 34 % | 33.0 px | 0.25 | 1.21 | 464 |
| slow wave | 26 % → 32 % | 30.0 px | 0.21 | 1.24 | 454 |
| spiral | 44 % → 50 % | 28.9 px | 0.16 | 1.14 | 466 |
| loop | 23 % → 29 % | 29.2 px | 0.22 | 1.28 | 272 |
| tilted | 15 % → 15 % | 42.1 px | 0.21 | 1.00 | 190 |
| over the wet one | 25 % → 30 % | 27.6 px | 0.21 | 1.18 | 156 |
| long, no reload | 59 % → 63 % | 26.3 px | 0.16 | 1.08 | 960 | quarters: 0.17 → 0.12 → 0.09 → 0.07

Numbers say: light vs heavy: width 18.7 → 37.9 px, dark 0.21 → 0.22; wet paint spreads well beyond the stroke.

## Watercolour · #16 Shrigley strokes
Watercolour 1.00 + water 30 % · 46 px · 42.3 s

![Watercolour · #16 Shrigley strokes](Watercolour-16-Shrigley-strokes.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 6 % → 13 % | 18.7 px | 0.40 | 2.04 | 87 |
| heavy line | 13 % → 17 % | 37.9 px | 0.41 | 1.30 | 155 |
| pressure swell | 8 % → 12 % | 29.8 px | 0.45 | 1.49 | 94 |
| fast wave | 29 % → 34 % | 33.0 px | 0.45 | 1.21 | 382 |
| slow wave | 26 % → 32 % | 30.0 px | 0.39 | 1.24 | 462 |
| spiral | 44 % → 50 % | 28.9 px | 0.31 | 1.14 | 540 |
| loop | 23 % → 29 % | 29.2 px | 0.41 | 1.28 | 249 |
| tilted | 15 % → 15 % | 42.1 px | 0.39 | 1.00 | 177 |
| over the wet one | 25 % → 30 % | 27.6 px | 0.39 | 1.18 | 142 |
| long, no reload | 59 % → 63 % | 26.3 px | 0.30 | 1.08 | 1006 | quarters: 0.32 → 0.22 → 0.17 → 0.12

Numbers say: light vs heavy: width 18.7 → 37.9 px, dark 0.40 → 0.41; wet paint spreads well beyond the stroke.

## Watercolour · #29 Shrigley asterisk
Watercolour 1.00 + water 50 % · 70 px · 67.0 s

![Watercolour · #29 Shrigley asterisk](Watercolour-29-Shrigley-asterisk.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 20 % → 23 % | 57.5 px | 0.60 | 1.17 | 186 |
| heavy line | 39 % → 39 % | 112.6 px | 0.62 | 1.00 | 524 |
| pressure swell | 24 % → 25 % | 88.7 px | 0.61 | 1.06 | 336 |
| fast wave | 68 % → 72 % | 78.5 px | 0.61 | 1.06 | 1306 |
| slow wave | 64 % → 64 % | 73.9 px | 0.62 | 1.01 | 1491 |
| spiral | 76 % → 77 % | 50.3 px | 0.57 | 1.01 | 1454 |
| loop | 57 % → 58 % | 74.2 px | 0.60 | 1.01 | 818 |
| tilted | 24 % → 24 % | 67.8 px | 0.60 | 1.00 | 447 |
| over the wet one | 52 % → 55 % | 78.6 px | 0.60 | 1.06 | 573 |
| long, no reload | 92 % → 94 % | 41.3 px | 0.55 | 1.02 | 2540 | quarters: 0.57 → 0.56 → 0.54 → 0.45

Numbers say: light vs heavy: width 57.5 → 112.6 px, dark 0.60 → 0.62.

## Watercolour · Pink flame
Watercolour 1.00 + water 80 % · 60 px · 71.9 s

![Watercolour · Pink flame](Watercolour-Pink-flame.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 31 % → 59 % | 90.2 px | 0.05 | 1.89 | 172 |
| heavy line | 35 % → 48 % | 101.8 px | 0.08 | 1.37 | 252 |
| pressure swell | 17 % → 42 % | 62.8 px | 0.08 | 2.50 | 207 |
| fast wave | 64 % → 95 % | 74.2 px | 0.09 | 1.48 | 734 |
| slow wave | 64 % → 80 % | 74.2 px | 0.10 | 1.24 | 1173 |
| spiral | 76 % → 79 % | 50.2 px | 0.10 | 1.04 | 1146 |
| loop | 56 % → 71 % | 72.7 px | 0.10 | 1.27 | 831 |
| tilted | 28 % → 29 % | 79.4 px | 0.08 | 1.03 | 328 |
| over the wet one | 56 % → 76 % | 77.7 px | 0.08 | 1.35 | 283 |
| long, no reload | 88 % → 95 % | 39.3 px | 0.10 | 1.08 | 1828 | quarters: 0.16 → 0.12 → 0.07 → 0.04

Numbers say: light vs heavy: width 90.2 → 101.8 px, dark 0.05 → 0.08; wet paint spreads well beyond the stroke.

## Watercolour · #33 Red band, pink flames
Watercolour 1.00 + water 60 % · 90 px · 83.9 s

![Watercolour · #33 Red band, pink flames](Watercolour-33-Red-band-pink-flames.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 29 % → 49 % | 82.9 px | 0.44 | 1.71 | 219 |
| heavy line | 45 % → 57 % | 129.8 px | 0.50 | 1.27 | 471 |
| pressure swell | 27 % → 46 % | 100.1 px | 0.47 | 1.71 | 348 |
| fast wave | 71 % → 86 % | 82.5 px | 0.58 | 1.20 | 1184 |
| slow wave | 72 % → 83 % | 83.5 px | 0.57 | 1.15 | 2594 |
| spiral | 85 % → 95 % | 55.9 px | 0.54 | 1.12 | 2558 |
| loop | 62 % → 79 % | 80.6 px | 0.54 | 1.27 | 909 |
| tilted | 37 % → 39 % | 103.8 px | 0.51 | 1.04 | 900 |
| over the wet one | 66 % → 87 % | 80.4 px | 0.51 | 1.32 | 456 |
| long, no reload | 95 % → 100 % | 42.6 px | 0.58 | 1.05 | 2892 | quarters: 0.66 → 0.64 → 0.60 → 0.48

Numbers say: light vs heavy: width 82.9 → 129.8 px, dark 0.44 → 0.50; wet paint spreads well beyond the stroke.

## Watercolour · #35 Red band with runs
Watercolour 1.00 + water 75 % · 80 px · 84.4 s

![Watercolour · #35 Red band with runs](Watercolour-35-Red-band-with-runs.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 37 % → 52 % | 108.6 px | 0.16 | 1.39 | 256 |
| heavy line | 50 % → 56 % | 145.9 px | 0.31 | 1.11 | 445 |
| pressure swell | 20 % → 34 % | 76.7 px | 0.22 | 1.64 | 320 |
| fast wave | 69 % → 80 % | 79.9 px | 0.36 | 1.16 | 1213 |
| slow wave | 70 % → 78 % | 80.6 px | 0.42 | 1.12 | 1980 |
| spiral | 87 % → 95 % | 57.7 px | 0.16 | 1.09 | 2677 |
| loop | 73 % → 86 % | 93.9 px | 0.35 | 1.18 | 826 |
| tilted | 47 % → 47 % | 130.4 px | 0.32 | 1.01 | 506 |
| over the wet one | 73 % → 86 % | 72.8 px | 0.32 | 1.18 | 433 |
| long, no reload | 94 % → 100 % | 42.0 px | 0.26 | 1.07 | 3302 | quarters: 0.41 → 0.31 → 0.22 → 0.13

Numbers say: light vs heavy: width 108.6 → 145.9 px, dark 0.16 → 0.31; wet paint spreads well beyond the stroke.

## Watercolour · Sepia wash
Watercolour 1.00 + water 60 % · 80 px · 71.8 s

![Watercolour · Sepia wash](Watercolour-Sepia-wash.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 18 % → 36 % | 53.2 px | 0.20 | 1.95 | 223 |
| heavy line | 34 % → 45 % | 98.0 px | 0.20 | 1.34 | 536 |
| pressure swell | 21 % → 33 % | 76.9 px | 0.22 | 1.62 | 269 |
| fast wave | 62 % → 82 % | 71.9 px | 0.24 | 1.32 | 929 |
| slow wave | 60 % → 76 % | 69.5 px | 0.23 | 1.26 | 1452 |
| spiral | 76 % → 85 % | 50.0 px | 0.22 | 1.12 | 1679 |
| loop | 54 % → 66 % | 69.8 px | 0.24 | 1.23 | 1011 |
| tilted | 26 % → 27 % | 72.4 px | 0.22 | 1.04 | 511 |
| over the wet one | 51 % → 74 % | 70.8 px | 0.22 | 1.45 | 388 |
| long, no reload | 94 % → 99 % | 42.1 px | 0.23 | 1.05 | 2238 | quarters: 0.35 → 0.26 → 0.20 → 0.13

Numbers say: light vs heavy: width 53.2 → 98.0 px, dark 0.20 → 0.20; wet paint spreads well beyond the stroke.

## Watercolour · #40 Olive and sepia blooms
Watercolour 1.00 + water 55 % · 90 px · 74.9 s

![Watercolour · #40 Olive and sepia blooms](Watercolour-40-Olive-and-sepia-blooms.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 20 % → 38 % | 59.3 px | 0.19 | 1.86 | 337 |
| heavy line | 37 % → 48 % | 107.6 px | 0.21 | 1.29 | 461 |
| pressure swell | 23 % → 37 % | 87.2 px | 0.23 | 1.59 | 314 |
| fast wave | 67 % → 86 % | 77.6 px | 0.25 | 1.28 | 1148 |
| slow wave | 66 % → 80 % | 75.8 px | 0.24 | 1.22 | 1808 |
| spiral | 79 % → 87 % | 52.0 px | 0.23 | 1.11 | 2005 |
| loop | 58 % → 69 % | 74.6 px | 0.25 | 1.19 | 807 |
| tilted | 29 % → 30 % | 80.8 px | 0.22 | 1.04 | 671 |
| over the wet one | 57 % → 79 % | 77.9 px | 0.22 | 1.39 | 456 |
| long, no reload | 95 % → 99 % | 42.8 px | 0.24 | 1.04 | 2956 | quarters: 0.36 → 0.28 → 0.20 → 0.14

Numbers say: light vs heavy: width 59.3 → 107.6 px, dark 0.19 → 0.21; wet paint spreads well beyond the stroke.

## Watercolour · #46 Lips on wet paper
Watercolour 1.00 + water 65 % · 50 px · 62.4 s

![Watercolour · #46 Lips on wet paper](Watercolour-46-Lips-on-wet-paper.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 11 % → 28 % | 32.3 px | 0.62 | 2.52 | 111 |
| heavy line | 22 % → 35 % | 64.7 px | 0.64 | 1.56 | 195 |
| pressure swell | 13 % → 25 % | 49.9 px | 0.64 | 1.88 | 152 |
| fast wave | 44 % → 68 % | 50.5 px | 0.65 | 1.56 | 830 |
| slow wave | 41 % → 64 % | 47.7 px | 0.65 | 1.54 | 785 |
| spiral | 64 % → 76 % | 42.0 px | 0.66 | 1.20 | 834 |
| loop | 37 % → 56 % | 47.7 px | 0.66 | 1.52 | 331 |
| tilted | 18 % → 19 % | 50.0 px | 0.62 | 1.06 | 296 |
| over the wet one | 36 % → 58 % | 51.1 px | 0.62 | 1.60 | 229 |
| long, no reload | 79 % → 96 % | 35.3 px | 0.66 | 1.22 | 1480 | quarters: 0.72 → 0.71 → 0.66 → 0.56

Numbers say: light vs heavy: width 32.3 → 64.7 px, dark 0.62 → 0.64; wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #01 Henry Ward peach cloud — own sheet
own sheet 600 × 600 · Gouache 1.00 · 44 px · 16.1 s

![Brush Artist · Refs · #01 Henry Ward peach cloud — own sheet](Brush-Artist-Refs-01-Henry-Ward-peach-cloud-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 6 % → 16 % | 16.4 px | 0.53 | 2.83 | 380 |
| stroke 2 | 11 % → 30 % | 36.0 px | 0.54 | 2.69 | 264 |
| stroke 3 | 16 % → 32 % | 47.3 px | 0.54 | 1.95 | 316 |
| stroke 4 | 21 % → 34 % | 69.8 px | 0.54 | 1.62 | 309 |
| stroke 5 | 21 % → 31 % | 61.8 px | 0.54 | 1.46 | 211 |
| stroke 6 | 20 % → 24 % | 62.0 px | 0.54 | 1.21 | 184 |
| stroke 7 | 9 % → 33 % | 23.4 px | 0.53 | 3.53 | 164 |
| stroke 8 | 14 % → 32 % | 34.9 px | 0.53 | 2.29 | 203 |
| stroke 9 | 13 % → 33 % | 34.1 px | 0.53 | 2.48 | 207 |
| stroke 10 | 13 % → 34 % | 35.6 px | 0.53 | 2.58 | 210 |
| stroke 11 | 14 % → 37 % | 40.7 px | 0.54 | 2.54 | 199 |
| stroke 12 | 14 % → 39 % | 42.7 px | 0.54 | 2.76 | 159 |
| stroke 13 | 19 % → 43 % | 55.6 px | 0.54 | 2.22 | 189 |
| stroke 14 | 27 % → 44 % | 77.9 px | 0.54 | 1.63 | 239 |
| stroke 15 | 30 % → 48 % | 89.6 px | 0.53 | 1.59 | 184 |
| stroke 16 | 35 % → 49 % | 106.0 px | 0.53 | 1.39 | 214 |
| stroke 17 | 35 % → 50 % | 99.5 px | 0.53 | 1.41 | 311 |
| stroke 18 | 41 % → 49 % | 118.9 px | 0.53 | 1.20 | 216 |
| stroke 19 | 42 % → 49 % | 117.4 px | 0.54 | 1.17 | 212 |
| stroke 20 | 43 % → 46 % | 124.4 px | 0.54 | 1.06 | 222 |
| stroke 21 | 44 % → 42 % | 127.1 px | 0.54 | 0.96 | 252 |
| stroke 22 | 46 % → 43 % | 132.7 px | 0.54 | 0.94 | 247 |
| stroke 23 | 49 % → 43 % | 140.2 px | 0.54 | 0.88 | 254 |
| stroke 24 | 53 % → 45 % | 157.4 px | 0.54 | 0.86 | 207 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #02 Henry Ward cream strokes — own sheet
own sheet 600 × 600 · Gouache 1.00 · 46 px · 12.5 s

![Brush Artist · Refs · #02 Henry Ward cream strokes — own sheet](Brush-Artist-Refs-02-Henry-Ward-cream-strokes-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 9 % → 2 % | 18.3 px | 0.65 | 0.27 | 243 |
| stroke 2 | 15 % → 6 % | 40.0 px | 0.65 | 0.40 | 299 |
| stroke 3 | 19 % → 22 % | 49.3 px | 0.64 | 1.14 | 289 |
| stroke 4 | 23 % → 22 % | 57.0 px | 0.64 | 0.96 | 349 |
| stroke 5 | 24 % → 27 % | 59.9 px | 0.64 | 1.09 | 297 |
| stroke 6 | 18 % → 16 % | 44.5 px | 0.64 | 0.88 | 301 |
| stroke 7 | 21 % → 10 % | 53.6 px | 0.64 | 0.49 | 269 |

## Brush Artist · Refs · #03 Henry Ward navy contours — own sheet
own sheet 600 × 600 · Impasto 1.00 · 22 px · 3.8 s

![Brush Artist · Refs · #03 Henry Ward navy contours — own sheet](Brush-Artist-Refs-03-Henry-Ward-navy-contours-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 10 % → 15 % | 20.0 px | 0.70 | 1.51 | 167 |
| stroke 2 | 16 % → 19 % | 22.1 px | 0.70 | 1.19 | 163 |
| stroke 3 | 20 % → 20 % | 29.5 px | 0.71 | 0.99 | 240 |
| stroke 4 | 19 % → 17 % | 43.6 px | 0.71 | 0.89 | 372 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #04 Henry Ward grey cloud — own sheet
own sheet 600 × 600 · Gouache 1.00 · 50 px · 15.5 s

![Brush Artist · Refs · #04 Henry Ward grey cloud — own sheet](Brush-Artist-Refs-04-Henry-Ward-grey-cloud-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 5 % → 21 % | 15.7 px | 0.32 | 3.92 | 389 |
| stroke 2 | 14 % → 22 % | 40.2 px | 0.31 | 1.56 | 302 |
| stroke 3 | 21 % → 23 % | 59.8 px | 0.31 | 1.07 | 304 |
| stroke 4 | 27 % → 24 % | 79.7 px | 0.31 | 0.86 | 359 |
| stroke 5 | 28 % → 27 % | 83.5 px | 0.31 | 0.97 | 270 |
| stroke 6 | 33 % → 30 % | 109.1 px | 0.31 | 0.91 | 329 |
| stroke 7 | 34 % → 37 % | 100.9 px | 0.30 | 1.06 | 388 |
| stroke 8 | 38 % → 39 % | 112.7 px | 0.30 | 1.02 | 342 |
| stroke 9 | 32 % → 40 % | 95.0 px | 0.31 | 1.26 | 334 |
| stroke 10 | 34 % → 40 % | 108.1 px | 0.31 | 1.20 | 285 |
| stroke 11 | 35 % → 37 % | 98.1 px | 0.31 | 1.07 | 322 |
| stroke 12 | 32 % → 35 % | 97.7 px | 0.30 | 1.08 | 255 |
| stroke 13 | 28 % → 39 % | 80.2 px | 0.31 | 1.38 | 280 |
| stroke 14 | 34 % → 39 % | 102.0 px | 0.31 | 1.13 | 381 |
| stroke 15 | 35 % → 38 % | 101.4 px | 0.31 | 1.08 | 278 |
| stroke 16 | 39 % → 37 % | 117.6 px | 0.31 | 0.95 | 360 |
| stroke 17 | 39 % → 32 % | 112.8 px | 0.32 | 0.81 | 315 |
| stroke 18 | 40 % → 29 % | 133.3 px | 0.32 | 0.72 | 389 |
| stroke 19 | 38 % → 24 % | 113.5 px | 0.32 | 0.63 | 391 |
| stroke 20 | 40 % → 23 % | 125.7 px | 0.32 | 0.58 | 440 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #05 Henry Ward green in rust loops — own sheet
own sheet 600 × 600 · Impasto 1.00 · 20 px · 3.6 s

![Brush Artist · Refs · #05 Henry Ward green in rust loops — own sheet](Brush-Artist-Refs-05-Henry-Ward-green-in-rust-loops-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 11 % → 16 % | 19.1 px | 0.02 | 1.49 | 223 |
| stroke 2 | 12 % → 10 % | 24.0 px | 0.02 | 0.86 | 289 |
| stroke 3 | 20 % → 17 % | 35.4 px | 0.02 | 0.89 | 185 |

## Brush Artist · Refs · #06 Henry Ward scrubbed grey — own sheet
own sheet 600 × 600 · Gouache 1.00 · 50 px · 17.4 s

![Brush Artist · Refs · #06 Henry Ward scrubbed grey — own sheet](Brush-Artist-Refs-06-Henry-Ward-scrubbed-grey-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 6 % → 24 % | 15.9 px | 0.32 | 3.74 | 308 |
| stroke 2 | 16 % → 25 % | 41.5 px | 0.32 | 1.60 | 354 |
| stroke 3 | 21 % → 24 % | 64.8 px | 0.31 | 1.11 | 345 |
| stroke 4 | 25 % → 24 % | 78.2 px | 0.31 | 0.98 | 393 |
| stroke 5 | 31 % → 30 % | 93.0 px | 0.31 | 0.98 | 350 |
| stroke 6 | 38 % → 31 % | 115.8 px | 0.31 | 0.82 | 284 |
| stroke 7 | 36 % → 36 % | 103.7 px | 0.31 | 1.00 | 391 |
| stroke 8 | 40 % → 36 % | 125.2 px | 0.31 | 0.92 | 363 |
| stroke 9 | 35 % → 38 % | 107.6 px | 0.31 | 1.08 | 255 |
| stroke 10 | 34 % → 38 % | 111.5 px | 0.31 | 1.12 | 225 |
| stroke 11 | 35 % → 37 % | 101.9 px | 0.31 | 1.08 | 285 |
| stroke 12 | 33 % → 36 % | 100.2 px | 0.31 | 1.10 | 231 |
| stroke 13 | 25 % → 38 % | 70.7 px | 0.31 | 1.53 | 221 |
| stroke 14 | 30 % → 40 % | 89.5 px | 0.31 | 1.31 | 309 |
| stroke 15 | 34 % → 45 % | 96.4 px | 0.32 | 1.35 | 247 |
| stroke 16 | 35 % → 45 % | 112.9 px | 0.32 | 1.29 | 245 |
| stroke 17 | 37 % → 43 % | 110.8 px | 0.32 | 1.14 | 273 |
| stroke 18 | 41 % → 41 % | 124.1 px | 0.32 | 1.00 | 304 |
| stroke 19 | 38 % → 36 % | 113.1 px | 0.32 | 0.95 | 294 |
| stroke 20 | 38 % → 35 % | 118.9 px | 0.32 | 0.91 | 352 |
| stroke 21 | 40 % → 31 % | 116.3 px | 0.33 | 0.76 | 347 |
| stroke 22 | 38 % → 28 % | 127.0 px | 0.33 | 0.73 | 287 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #07 Henry Ward blue L + black zigzag — own sheet
own sheet 600 × 600 · Impasto 1.00 · 34 px · 2.9 s

![Brush Artist · Refs · #07 Henry Ward blue L + black zigzag — own sheet](Brush-Artist-Refs-07-Henry-Ward-blue-L-black-zigzag-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 13 % → 15 % | 31.2 px | 0.58 | 1.09 | 188 |
| stroke 2 | 15 % → 14 % | 37.7 px | 0.58 | 0.90 | 123 |

## Brush Artist · Refs · #08 Henry Ward olive bands — own sheet
own sheet 600 × 600 · Gouache 1.00 · 34 px · 8.5 s

![Brush Artist · Refs · #08 Henry Ward olive bands — own sheet](Brush-Artist-Refs-08-Henry-Ward-olive-bands-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 12 % → 7 % | 24.2 px | 0.58 | 0.61 | 251 |
| stroke 2 | 18 % → 9 % | 40.7 px | 0.58 | 0.49 | 229 |
| stroke 3 | 17 % → 18 % | 35.0 px | 0.58 | 1.07 | 250 |
| stroke 4 | 21 % → 15 % | 44.7 px | 0.58 | 0.75 | 296 |
| stroke 5 | 26 % → 20 % | 54.3 px | 0.56 | 0.77 | 388 |
| stroke 6 | 19 % → 10 % | 36.1 px | 0.53 | 0.52 | 371 |

## Brush Artist · Refs · #09 Henry Ward white loops — own sheet
own sheet 600 × 600 · Gouache 1.00 · 46 px · 9.5 s

![Brush Artist · Refs · #09 Henry Ward white loops — own sheet](Brush-Artist-Refs-09-Henry-Ward-white-loops-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 23 % → 0 % | 12.2 px | 0.00 | 0.00 | 1274 |
| stroke 2 | 27 % → 0 % | 27.3 px | 0.08 | 0.00 | 1642 |
| stroke 3 | 34 % → 0 % | 31.4 px | 0.08 | 0.00 | 1458 |
| stroke 4 | 8 % → 0 % | 18.1 px | 0.00 | 0.00 | 240 |
| stroke 5 | 5 % → 0 % | 14.6 px | 0.00 | 0.00 | 231 |
| stroke 6 | 5 % → 0 % | 12.7 px | 0.08 | 0.00 | 253 |
| stroke 7 | 10 % → 0 % | 25.1 px | 0.08 | 0.00 | 227 |
| stroke 8 | 5 % → 0 % | 8.2 px | 0.00 | 0.00 | 255 |

## Brush Artist · Refs · #10 Henry Ward maroon loops — own sheet
own sheet 600 × 600 · Impasto 1.00 · 30 px · 4.4 s

![Brush Artist · Refs · #10 Henry Ward maroon loops — own sheet](Brush-Artist-Refs-10-Henry-Ward-maroon-loops-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 12 % → 26 % | 28.9 px | 0.72 | 2.25 | 391 |
| stroke 2 | 23 % → 39 % | 51.0 px | 0.72 | 1.74 | 215 |
| stroke 3 | 30 % → 36 % | 59.6 px | 0.72 | 1.20 | 287 |
| stroke 4 | 40 % → 38 % | 91.4 px | 0.72 | 0.94 | 168 |
| stroke 5 | 33 % → 29 % | 82.1 px | 0.71 | 0.89 | 232 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #11 Henry Ward purple spun balls — own sheet
own sheet 600 × 600 · Impasto 1.00 · 36 px · 4.6 s

![Brush Artist · Refs · #11 Henry Ward purple spun balls — own sheet](Brush-Artist-Refs-11-Henry-Ward-purple-spun-balls-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 22 % → 31 % | 24.4 px | 0.69 | 1.42 | 320 |
| stroke 2 | 31 % → 44 % | 34.3 px | 0.69 | 1.39 | 331 |
| stroke 3 | 34 % → 33 % | 37.7 px | 0.69 | 0.97 | 442 |

## Brush Artist · Refs · #12 Henry Ward black-olive cage — own sheet
own sheet 600 × 600 · Gouache 1.00 · 28 px · 8.1 s

![Brush Artist · Refs · #12 Henry Ward black-olive cage — own sheet](Brush-Artist-Refs-12-Henry-Ward-black-olive-cage-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 10 % → 13 % | 19.0 px | 0.59 | 1.33 | 352 |
| stroke 2 | 9 % → 16 % | 21.7 px | 0.59 | 1.73 | 272 |
| stroke 3 | 21 % → 20 % | 33.2 px | 0.59 | 0.97 | 380 |
| stroke 4 | 22 % → 17 % | 44.0 px | 0.59 | 0.78 | 331 |
| stroke 5 | 21 % → 12 % | 38.0 px | 0.59 | 0.59 | 300 |
| stroke 6 | 32 % → 19 % | 60.4 px | 0.59 | 0.59 | 362 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #13 Henry Ward blue streaky form — own sheet
own sheet 600 × 600 · Gouache 1.00 · 50 px · 12.4 s

![Brush Artist · Refs · #13 Henry Ward blue streaky form — own sheet](Brush-Artist-Refs-13-Henry-Ward-blue-streaky-form-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 5 % → 0 % | 15.9 px | 0.00 | 0.00 | 323 |
| stroke 2 | 13 % → 0 % | 40.6 px | 0.00 | 0.00 | 363 |
| stroke 3 | 22 % → 0 % | 62.3 px | 0.00 | 0.00 | 376 |
| stroke 4 | 24 % → 0 % | 78.6 px | 0.00 | 0.00 | 403 |
| stroke 5 | 31 % → 0 % | 90.3 px | 0.00 | 0.00 | 245 |
| stroke 6 | 37 % → 0 % | 105.4 px | 0.00 | 0.00 | 307 |
| stroke 7 | 37 % → 0 % | 107.4 px | 0.00 | 0.00 | 265 |
| stroke 8 | 40 % → 0 % | 120.5 px | 0.00 | 0.00 | 254 |
| stroke 9 | 33 % → 0 % | 103.1 px | 0.00 | 0.00 | 228 |
| stroke 10 | 32 % → 0 % | 105.9 px | 0.00 | 0.00 | 238 |
| stroke 11 | 30 % → 0 % | 92.7 px | 0.00 | 0.00 | 289 |
| stroke 12 | 27 % → 0 % | 79.3 px | 0.00 | 0.00 | 215 |
| stroke 13 | 24 % → 0 % | 76.3 px | 0.00 | 0.00 | 249 |
| stroke 14 | 29 % → 0 % | 85.6 px | 0.00 | 0.00 | 337 |
| stroke 15 | 30 % → 0 % | 87.0 px | 0.00 | 0.00 | 256 |
| stroke 16 | 35 % → 0 % | 105.4 px | 0.00 | 0.00 | 297 |
| stroke 17 | 41 % → 0 % | 103.0 px | 0.00 | 0.00 | 245 |
| stroke 18 | 48 % → 0 % | 117.7 px | 0.00 | 0.00 | 299 |
| stroke 19 | 52 % → 0 % | 104.7 px | 0.00 | 0.00 | 257 |
| stroke 20 | 60 % → 0 % | 115.3 px | 0.00 | 0.00 | 289 |
| stroke 21 | 7 % → 0 % | 15.0 px | 0.00 | 0.00 | 212 |
| stroke 22 | 6 % → 0 % | 17.2 px | 0.00 | 0.00 | 216 |
| stroke 23 | 10 % → 0 % | 30.3 px | 0.00 | 0.00 | 200 |
| stroke 24 | 3 % → 0 % | 9.6 px | 0.00 | 0.00 | 190 |
| stroke 25 | 3 % → 0 % | 7.3 px | 0.00 | 0.00 | 191 |

## Brush Artist · Refs · #14 Henry Ward olive totem — own sheet
own sheet 600 × 600 · Impasto 1.00 · 48 px · 9.0 s

![Brush Artist · Refs · #14 Henry Ward olive totem — own sheet](Brush-Artist-Refs-14-Henry-Ward-olive-totem-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 18 % → 46 % | 46.6 px | 0.38 | 2.57 | 212 |
| stroke 2 | 20 % → 50 % | 61.7 px | 0.38 | 2.53 | 193 |
| stroke 3 | 27 % → 52 % | 93.9 px | 0.39 | 1.89 | 210 |
| stroke 4 | 30 % → 54 % | 110.9 px | 0.39 | 1.82 | 221 |
| stroke 5 | 38 % → 63 % | 134.1 px | 0.39 | 1.64 | 207 |
| stroke 6 | 38 % → 64 % | 149.8 px | 0.39 | 1.67 | 182 |
| stroke 7 | 35 % → 60 % | 119.1 px | 0.39 | 1.70 | 187 |
| stroke 8 | 37 % → 62 % | 141.6 px | 0.39 | 1.67 | 212 |
| stroke 9 | 38 % → 62 % | 131.6 px | 0.39 | 1.64 | 197 |
| stroke 10 | 37 % → 61 % | 136.5 px | 0.39 | 1.65 | 209 |
| stroke 11 | 38 % → 64 % | 136.7 px | 0.39 | 1.66 | 171 |
| stroke 12 | 38 % → 64 % | 143.5 px | 0.38 | 1.68 | 209 |
| stroke 13 | 37 % → 66 % | 129.3 px | 0.39 | 1.78 | 163 |
| stroke 14 | 36 % → 61 % | 131.1 px | 0.39 | 1.70 | 247 |
| stroke 15 | 39 % → 65 % | 134.4 px | 0.39 | 1.66 | 198 |
| stroke 16 | 38 % → 63 % | 136.6 px | 0.39 | 1.67 | 199 |
| stroke 17 | 37 % → 61 % | 124.1 px | 0.39 | 1.64 | 238 |
| stroke 18 | 40 % → 65 % | 152.2 px | 0.39 | 1.63 | 171 |
| stroke 19 | 38 % → 58 % | 131.3 px | 0.39 | 1.54 | 161 |
| stroke 20 | 40 % → 53 % | 142.6 px | 0.39 | 1.31 | 247 |
| stroke 21 | 46 % → 53 % | 136.0 px | 0.39 | 1.15 | 176 |
| stroke 22 | 53 % → 51 % | 143.0 px | 0.39 | 0.97 | 203 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #15 Ultramarine brush script — own sheet
own sheet 600 × 600 · Ink 1.00 · 4 px · 11.0 s

![Brush Artist · Refs · #15 Ultramarine brush script — own sheet](Brush-Artist-Refs-15-Ultramarine-brush-script-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 40 % → 42 % | 9.0 px | 0.65 | 1.05 | 77 |
| stroke 2 | 41 % → 43 % | 9.0 px | 0.67 | 1.07 | 91 |
| stroke 3 | 39 % → 42 % | 9.4 px | 0.72 | 1.08 | 41 |
| stroke 4 | 42 % → 46 % | 10.2 px | 0.74 | 1.10 | 21 |
| stroke 5 | 46 % → 49 % | 10.1 px | 0.72 | 1.06 | 43 |
| stroke 6 | 43 % → 45 % | 9.7 px | 0.65 | 1.05 | 65 |
| stroke 7 | 44 % → 47 % | 9.3 px | 0.72 | 1.08 | 39 |
| stroke 8 | 37 % → 39 % | 8.9 px | 0.65 | 1.06 | 56 |
| stroke 9 | 39 % → 42 % | 9.1 px | 0.70 | 1.07 | 50 |
| stroke 10 | 35 % → 37 % | 9.6 px | 0.66 | 1.05 | 62 |
| stroke 11 | 44 % → 47 % | 9.9 px | 0.69 | 1.06 | 41 |
| stroke 12 | 39 % → 41 % | 9.4 px | 0.65 | 1.06 | 70 |
| stroke 13 | 45 % → 46 % | 10.1 px | 0.69 | 1.04 | 33 |
| stroke 14 | 37 % → 40 % | 9.6 px | 0.71 | 1.07 | 36 |
| stroke 15 | 37 % → 38 % | 9.0 px | 0.67 | 1.05 | 63 |
| stroke 16 | 42 % → 45 % | 9.4 px | 0.70 | 1.06 | 34 |
| stroke 17 | 41 % → 45 % | 7.1 px | 0.71 | 1.09 | 52 |
| stroke 18 | 43 % → 45 % | 9.3 px | 0.73 | 1.05 | 36 |
| stroke 19 | 40 % → 42 % | 9.0 px | 0.65 | 1.06 | 70 |
| stroke 20 | 42 % → 44 % | 9.7 px | 0.69 | 1.06 | 47 |
| stroke 21 | 39 % → 42 % | 9.6 px | 0.69 | 1.07 | 42 |
| stroke 22 | 44 % → 46 % | 8.9 px | 0.65 | 1.06 | 66 |
| stroke 23 | 38 % → 42 % | 9.5 px | 0.72 | 1.10 | 41 |
| stroke 24 | 39 % → 42 % | 9.1 px | 0.73 | 1.06 | 50 |
| stroke 25 | 41 % → 44 % | 10.0 px | 0.71 | 1.06 | 35 |
| stroke 26 | 45 % → 47 % | 9.1 px | 0.66 | 1.04 | 55 |
| stroke 27 | 43 % → 45 % | 9.0 px | 0.62 | 1.05 | 64 |
| stroke 28 | 45 % → 47 % | 9.3 px | 0.70 | 1.06 | 49 |
| stroke 29 | 35 % → 38 % | 10.4 px | 0.69 | 1.08 | 29 |
| stroke 30 | 39 % → 40 % | 8.5 px | 0.70 | 1.04 | 60 |
| stroke 31 | 43 % → 46 % | 10.4 px | 0.74 | 1.07 | 19 |
| stroke 32 | 41 % → 45 % | 9.3 px | 0.70 | 1.09 | 31 |
| stroke 33 | 35 % → 40 % | 10.9 px | 0.73 | 1.13 | 25 |
| stroke 34 | 41 % → 45 % | 10.1 px | 0.74 | 1.09 | 25 |
| stroke 35 | 36 % → 38 % | 9.4 px | 0.67 | 1.06 | 47 |

## Brush Artist · Refs · #18 Blue oil-stick scribbles — own sheet
own sheet 600 × 600 · Pastel 1.00 · 10 px · 4.5 s

![Brush Artist · Refs · #18 Blue oil-stick scribbles — own sheet](Brush-Artist-Refs-18-Blue-oil-stick-scribbles-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 16 % → 32 % | 3.9 px | 0.49 | 2.03 | 165 |
| stroke 2 | 13 % → 37 % | 3.6 px | 0.49 | 2.75 | 217 |
| stroke 3 | 16 % → 26 % | 5.8 px | 0.49 | 1.64 | 272 |
| stroke 4 | 15 % → 29 % | 7.9 px | 0.49 | 1.91 | 263 |
| stroke 5 | 29 % → 34 % | 8.5 px | 0.49 | 1.18 | 287 |
| stroke 6 | 26 % → 26 % | 9.4 px | 0.49 | 1.02 | 252 |
| stroke 7 | 26 % → 32 % | 8.4 px | 0.49 | 1.24 | 283 |
| stroke 8 | 30 % → 30 % | 17.0 px | 0.49 | 1.00 | 334 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #20 Orange-red crayon scribble — own sheet
own sheet 600 × 600 · Pastel 1.00 · 14 px · 3.8 s

![Brush Artist · Refs · #20 Orange-red crayon scribble — own sheet](Brush-Artist-Refs-20-Orange-red-crayon-scribble-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 8 % → 19 % | 5.5 px | 0.59 | 2.47 | 379 |
| stroke 2 | 9 % → 22 % | 6.6 px | 0.60 | 2.50 | 299 |
| stroke 3 | 13 % → 21 % | 8.3 px | 0.60 | 1.65 | 320 |
| stroke 4 | 24 % → 32 % | 8.8 px | 0.60 | 1.36 | 282 |
| stroke 5 | 28 % → 28 % | 7.9 px | 0.59 | 1.00 | 223 |
| stroke 6 | 22 % → 22 % | 16.4 px | 0.60 | 1.00 | 217 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #21 Gritty black contours — own sheet
own sheet 600 × 600 · Gouache 1.00 · 12 px · 5.0 s

![Brush Artist · Refs · #21 Gritty black contours — own sheet](Brush-Artist-Refs-21-Gritty-black-contours-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 6 % → 5 % | 6.6 px | 0.36 | 0.78 | 209 |
| stroke 2 | 5 % → 3 % | 8.8 px | 0.36 | 0.52 | 223 |
| stroke 3 | 9 % → 2 % | 8.2 px | 0.37 | 0.24 | 156 |
| stroke 4 | 10 % → 5 % | 12.2 px | 0.36 | 0.46 | 190 |
| stroke 5 | 11 % → 5 % | 13.8 px | 0.36 | 0.44 | 121 |

## Brush Artist · Refs · #22 Bold black brush poster — own sheet
own sheet 600 × 600 · Ink 1.00 · 20 px · 5.9 s

![Brush Artist · Refs · #22 Bold black brush poster — own sheet](Brush-Artist-Refs-22-Bold-black-brush-poster-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 24 % → 28 % | 38.8 px | 0.95 | 1.18 | 133 |
| stroke 2 | 28 % → 39 % | 42.9 px | 0.94 | 1.38 | 25 |
| stroke 3 | 30 % → 30 % | 46.0 px | 0.94 | 1.00 | 49 |
| stroke 4 | 30 % → 41 % | 57.8 px | 0.94 | 1.41 | 60 |
| stroke 5 | 27 % → 27 % | 46.3 px | 0.93 | 1.00 | 93 |

## Brush Artist · Refs · #23 Dry white on orange + black line — own sheet
own sheet 600 × 600 · Gouache 1.00 · 50 px · 13.5 s

![Brush Artist · Refs · #23 Dry white on orange + black line — own sheet](Brush-Artist-Refs-23-Dry-white-on-orange-black-line-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 9 % → 26 % | 31.3 px | 0.40 | 2.83 | 198 |
| stroke 2 | 12 % → 23 % | 41.9 px | 0.40 | 1.94 | 203 |
| stroke 3 | 19 % → 25 % | 69.2 px | 0.40 | 1.35 | 203 |
| stroke 4 | 22 % → 28 % | 86.4 px | 0.40 | 1.30 | 226 |
| stroke 5 | 31 % → 32 % | 111.7 px | 0.40 | 1.05 | 206 |
| stroke 6 | 32 % → 35 % | 131.3 px | 0.40 | 1.11 | 223 |
| stroke 7 | 27 % → 33 % | 104.5 px | 0.40 | 1.21 | 189 |
| stroke 8 | 27 % → 31 % | 105.5 px | 0.40 | 1.16 | 251 |
| stroke 9 | 27 % → 32 % | 100.6 px | 0.40 | 1.17 | 322 |
| stroke 10 | 27 % → 31 % | 105.0 px | 0.40 | 1.17 | 211 |
| stroke 11 | 29 % → 34 % | 109.0 px | 0.40 | 1.17 | 190 |
| stroke 12 | 30 % → 33 % | 115.8 px | 0.40 | 1.11 | 197 |
| stroke 13 | 30 % → 35 % | 112.0 px | 0.40 | 1.15 | 194 |
| stroke 14 | 30 % → 34 % | 117.0 px | 0.40 | 1.15 | 231 |
| stroke 15 | 30 % → 32 % | 112.9 px | 0.39 | 1.05 | 185 |
| stroke 16 | 29 % → 27 % | 117.1 px | 0.39 | 0.93 | 194 |
| stroke 17 | 29 % → 22 % | 100.6 px | 0.39 | 0.77 | 191 |
| stroke 18 | 36 % → 23 % | 128.7 px | 0.39 | 0.65 | 210 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #24 Picasso flat oil — own sheet
own sheet 600 × 600 · Oil 0.89 · Oil glaze 0.11 · 34 px · 7.7 s

![Brush Artist · Refs · #24 Picasso flat oil — own sheet](Brush-Artist-Refs-24-Picasso-flat-oil-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 14 % → 44 % | 30.0 px | 0.22 | 3.11 | 162 |
| stroke 2 | 19 % → 47 % | 44.5 px | 0.23 | 2.49 | 188 |
| stroke 3 | 27 % → 56 % | 59.7 px | 0.23 | 2.06 | 176 |
| stroke 4 | 37 % → 62 % | 82.9 px | 0.23 | 1.69 | 181 |
| stroke 5 | 41 % → 68 % | 91.2 px | 0.22 | 1.64 | 170 |
| stroke 6 | 42 % → 63 % | 96.5 px | 0.22 | 1.52 | 195 |
| stroke 7 | 42 % → 63 % | 87.5 px | 0.23 | 1.51 | 152 |
| stroke 8 | 42 % → 63 % | 101.6 px | 0.23 | 1.50 | 167 |
| stroke 9 | 34 % → 60 % | 74.4 px | 0.23 | 1.76 | 164 |
| stroke 10 | 38 % → 58 % | 89.8 px | 0.23 | 1.55 | 183 |
| stroke 11 | 35 % → 56 % | 74.6 px | 0.24 | 1.61 | 159 |
| stroke 12 | 37 % → 58 % | 88.3 px | 0.24 | 1.56 | 178 |
| stroke 13 | 35 % → 64 % | 77.9 px | 0.25 | 1.81 | 210 |
| stroke 14 | 36 % → 66 % | 82.0 px | 0.24 | 1.82 | 203 |
| stroke 15 | 36 % → 60 % | 76.0 px | 0.24 | 1.67 | 201 |
| stroke 16 | 36 % → 52 % | 83.2 px | 0.24 | 1.46 | 213 |
| stroke 17 | 41 % → 47 % | 86.1 px | 0.24 | 1.15 | 292 |
| stroke 18 | 42 % → 42 % | 101.0 px | 0.24 | 1.00 | 329 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #25 Yellow heavy flat stroke — own sheet
own sheet 600 × 600 · Impasto 1.00 · 110 px · 4.5 s

![Brush Artist · Refs · #25 Yellow heavy flat stroke — own sheet](Brush-Artist-Refs-25-Yellow-heavy-flat-stroke-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 18 % → 18 % | 103.7 px | 0.16 | 0.98 | 808 |

## Brush Artist · Refs · #27 Orange impasto swatch — own sheet
own sheet 600 × 600 · Impasto 1.00 · 60 px · 5.9 s

![Brush Artist · Refs · #27 Orange impasto swatch — own sheet](Brush-Artist-Refs-27-Orange-impasto-swatch-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 8 % → 21 % | 58.4 px | 0.32 | 2.66 | 107 |
| stroke 2 | 7 % → 33 % | 62.2 px | 0.32 | 4.61 | 56 |
| stroke 3 | 25 % → 34 % | 238.0 px | 0.32 | 1.41 | 53 |
| stroke 4 | 10 % → 12 % | 69.5 px | 0.34 | 1.26 | 97 |
| stroke 5 | 17 % → 32 % | 61.8 px | 0.31 | 1.90 | 80 |
| stroke 6 | 17 % → 31 % | 143.7 px | 0.32 | 1.77 | 101 |
| stroke 7 | 8 % → 14 % | 68.6 px | 0.31 | 1.88 | 55 |
| stroke 8 | 32 % → 33 % | 328.8 px | 0.32 | 1.04 | 66 |
| stroke 9 | 37 % → 36 % | 182.9 px | 0.32 | 0.97 | 144 |
| stroke 10 | 33 % → 32 % | 298.6 px | 0.32 | 0.97 | 116 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #28 Miles Davis black lines — own sheet
own sheet 600 × 600 · Ink 1.00 · 22 px · 9.9 s

![Brush Artist · Refs · #28 Miles Davis black lines — own sheet](Brush-Artist-Refs-28-Miles-Davis-black-lines-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 22 % → 31 % | 36.1 px | 0.88 | 1.42 | 363 |
| stroke 2 | 26 % → 47 % | 35.8 px | 0.88 | 1.79 | 267 |
| stroke 3 | 38 % → 42 % | 73.3 px | 0.88 | 1.11 | 273 |
| stroke 4 | 41 % → 47 % | 81.4 px | 0.88 | 1.16 | 374 |
| stroke 5 | 54 % → 54 % | 108.2 px | 0.88 | 1.00 | 287 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #29 Shrigley magenta asterisk — own sheet
own sheet 600 × 600 · Watercolour 1.00 · 70 px · 9.4 s

![Brush Artist · Refs · #29 Shrigley magenta asterisk — own sheet](Brush-Artist-Refs-29-Shrigley-magenta-asterisk-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 13 % → 37 % | 46.6 px | 0.67 | 2.86 | 315 |
| stroke 2 | 12 % → 12 % | 87.1 px | 0.67 | 1.00 | 344 |
| stroke 3 | 28 % → 37 % | 100.9 px | 0.67 | 1.31 | 414 |
| stroke 4 | 23 % → 23 % | 164.0 px | 0.67 | 1.02 | 424 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #30 Red gouache face patch — own sheet
own sheet 600 × 600 · Gouache 1.00 · 60 px · 16.1 s

![Brush Artist · Refs · #30 Red gouache face patch — own sheet](Brush-Artist-Refs-30-Red-gouache-face-patch-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 11 % → 37 % | 50.6 px | 0.54 | 3.29 | 362 |
| stroke 2 | 15 % → 41 % | 74.2 px | 0.54 | 2.74 | 283 |
| stroke 3 | 24 % → 50 % | 115.1 px | 0.54 | 2.08 | 247 |
| stroke 4 | 26 % → 52 % | 133.4 px | 0.54 | 1.95 | 289 |
| stroke 5 | 34 % → 60 % | 160.6 px | 0.54 | 1.77 | 261 |
| stroke 6 | 35 % → 61 % | 178.6 px | 0.54 | 1.76 | 299 |
| stroke 7 | 35 % → 59 % | 164.2 px | 0.54 | 1.70 | 256 |
| stroke 8 | 34 % → 56 % | 162.3 px | 0.54 | 1.66 | 274 |
| stroke 9 | 36 % → 60 % | 172.7 px | 0.53 | 1.66 | 256 |
| stroke 10 | 38 % → 62 % | 196.7 px | 0.53 | 1.64 | 291 |
| stroke 11 | 37 % → 61 % | 181.6 px | 0.53 | 1.67 | 368 |
| stroke 12 | 36 % → 58 % | 179.8 px | 0.53 | 1.60 | 399 |
| stroke 13 | 33 % → 46 % | 157.0 px | 0.53 | 1.38 | 329 |
| stroke 14 | 33 % → 41 % | 159.9 px | 0.53 | 1.24 | 377 |
| stroke 15 | 33 % → 37 % | 153.6 px | 0.53 | 1.12 | 221 |
| stroke 16 | 39 % → 39 % | 186.3 px | 0.53 | 0.98 | 210 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #31 Warhol blotted line — own sheet
own sheet 600 × 600 · Ink 1.00 · 6 px · 5.9 s

![Brush Artist · Refs · #31 Warhol blotted line — own sheet](Brush-Artist-Refs-31-Warhol-blotted-line-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 22 % → 43 % | 16.5 px | 0.83 | 1.94 | 178 |
| stroke 2 | 17 % → 23 % | 15.7 px | 0.81 | 1.35 | 128 |
| stroke 3 | 24 % → 25 % | 24.9 px | 0.81 | 1.03 | 129 |
| stroke 4 | 32 % → 41 % | 32.7 px | 0.83 | 1.28 | 99 |
| stroke 5 | 37 % → 45 % | 38.1 px | 0.83 | 1.21 | 92 |
| stroke 6 | 34 % → 35 % | 27.8 px | 0.81 | 1.03 | 95 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #32 Thick orange swipes — own sheet
own sheet 600 × 600 · Impasto 1.00 · 90 px · 4.5 s

![Brush Artist · Refs · #32 Thick orange swipes — own sheet](Brush-Artist-Refs-32-Thick-orange-swipes-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 14 % → 27 % | 86.6 px | 0.02 | 1.89 | 402 |
| stroke 2 | 26 % → 37 % | 177.9 px | 0.02 | 1.41 | 367 |
| stroke 3 | 27 % → 27 % | 176.1 px | 0.02 | 0.98 | 441 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #33 Red wet-in-wet band — own sheet
own sheet 600 × 600 · Watercolour 1.00 · 80 px · 13.5 s

![Brush Artist · Refs · #33 Red wet-in-wet band — own sheet](Brush-Artist-Refs-33-Red-wet-in-wet-band-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 22 % → 57 % | 83.4 px | 0.61 | 2.61 | 489 |
| stroke 2 | 28 % → 51 % | 228.4 px | 0.62 | 1.82 | 150 |
| stroke 3 | 34 % → 53 % | 330.0 px | 0.61 | 1.57 | 110 |
| stroke 4 | 40 % → 60 % | 389.9 px | 0.62 | 1.51 | 124 |
| stroke 5 | 40 % → 55 % | 339.4 px | 0.61 | 1.38 | 150 |
| stroke 6 | 41 % → 48 % | 310.3 px | 0.59 | 1.18 | 136 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #34 Magenta oil patches — own sheet
own sheet 600 × 600 · Oil 0.89 · Oil glaze 0.11 · 60 px · 4.2 s

![Brush Artist · Refs · #34 Magenta oil patches — own sheet](Brush-Artist-Refs-34-Magenta-oil-patches-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 8 % → 39 % | 57.1 px | 0.13 | 4.77 | 109 |
| stroke 2 | 8 % → 28 % | 56.8 px | 0.14 | 3.32 | 92 |
| stroke 3 | 7 % → 32 % | 58.6 px | 0.13 | 4.60 | 88 |
| stroke 4 | 15 % → 19 % | 122.2 px | 0.12 | 1.26 | 76 |
| stroke 5 | 21 % → 30 % | 112.2 px | 0.13 | 1.45 | 124 |
| stroke 6 | 19 % → 36 % | 159.7 px | 0.13 | 1.91 | 83 |
| stroke 7 | 28 % → 33 % | 226.6 px | 0.13 | 1.17 | 94 |
| stroke 8 | 30 % → 37 % | 213.6 px | 0.13 | 1.21 | 133 |
| stroke 9 | 23 % → 25 % | 147.9 px | 0.14 | 1.07 | 117 |
| stroke 10 | 27 % → 27 % | 240.6 px | 0.14 | 1.00 | 112 |
| stroke 11 | 33 % → 33 % | 297.2 px | 0.13 | 1.00 | 82 |
| stroke 12 | 24 % → 24 % | 173.6 px | 0.13 | 1.00 | 89 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #35 Red band with runs — own sheet
own sheet 600 × 600 · Watercolour 1.00 · 70 px · 11.0 s

![Brush Artist · Refs · #35 Red band with runs — own sheet](Brush-Artist-Refs-35-Red-band-with-runs-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 37 % → 47 % | 140.3 px | 0.45 | 1.27 | 353 |

## Brush Artist · Refs · #36 Magenta letters flat brush — own sheet
own sheet 600 × 600 · Gouache 1.00 · 36 px · 14.5 s

![Brush Artist · Refs · #36 Magenta letters flat brush — own sheet](Brush-Artist-Refs-36-Magenta-letters-flat-brush-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 20 % → 38 % | 58.3 px | 0.50 | 1.95 | 40 |
| stroke 2 | 20 % → 31 % | 45.2 px | 0.51 | 1.54 | 31 |
| stroke 3 | 28 % → 52 % | 84.6 px | 0.50 | 1.83 | 73 |
| stroke 4 | 26 % → 44 % | 50.3 px | 0.51 | 1.69 | 265 |
| stroke 5 | 33 % → 54 % | 96.3 px | 0.50 | 1.63 | 149 |
| stroke 6 | 43 % → 56 % | 246.0 px | 0.49 | 1.30 | 29 |
| stroke 7 | 30 % → 43 % | 56.6 px | 0.50 | 1.43 | 249 |
| stroke 8 | 31 % → 52 % | 97.7 px | 0.51 | 1.66 | 147 |
| stroke 9 | 38 % → 50 % | 158.2 px | 0.51 | 1.31 | 52 |
| stroke 10 | 37 % → 62 % | 107.5 px | 0.50 | 1.68 | 149 |
| stroke 11 | 39 % → 61 % | 225.6 px | 0.49 | 1.55 | 18 |
| stroke 12 | 44 % → 55 % | 82.9 px | 0.50 | 1.26 | 129 |
| stroke 13 | 31 % → 45 % | 113.5 px | 0.51 | 1.43 | 43 |
| stroke 14 | 34 % → 50 % | 129.9 px | 0.51 | 1.47 | 36 |
| stroke 15 | 36 % → 54 % | 105.5 px | 0.50 | 1.49 | 91 |
| stroke 16 | 39 % → 47 % | 221.7 px | 0.50 | 1.23 | 18 |
| stroke 17 | 43 % → 51 % | 81.6 px | 0.50 | 1.18 | 162 |
| stroke 18 | 26 % → 35 % | 95.6 px | 0.50 | 1.34 | 44 |
| stroke 19 | 39 % → 37 % | 112.8 px | 0.50 | 0.97 | 39 |
| stroke 20 | 45 % → 44 % | 129.9 px | 0.51 | 0.98 | 42 |
| stroke 21 | 40 % → 38 % | 78.2 px | 0.50 | 0.94 | 114 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #37 Oil still life dabs — own sheet
own sheet 600 × 600 · Oil 0.89 · Oil glaze 0.11 · 40 px · 3.2 s

![Brush Artist · Refs · #37 Oil still life dabs — own sheet](Brush-Artist-Refs-37-Oil-still-life-dabs-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 6 % → 6 % | 38.2 px | 0.37 | 1.00 | 37 |
| stroke 2 | 6 % → 26 % | 39.8 px | 0.40 | 4.69 | 30 |
| stroke 3 | 11 % → 33 % | 86.6 px | 0.39 | 3.00 | 20 |
| stroke 4 | 8 % → 8 % | 39.3 px | 0.37 | 1.00 | 51 |
| stroke 5 | 6 % → 10 % | 43.2 px | 0.38 | 1.67 | 33 |
| stroke 6 | 13 % → 29 % | 80.2 px | 0.40 | 2.26 | 47 |
| stroke 7 | 11 % → 22 % | 113.9 px | 0.38 | 2.08 | 15 |
| stroke 8 | 8 % → 13 % | 85.3 px | 0.38 | 1.59 | 16 |
| stroke 9 | 12 % → 13 % | 61.1 px | 0.36 | 1.12 | 46 |
| stroke 10 | 20 % → 24 % | 100.4 px | 0.40 | 1.20 | 50 |
| stroke 11 | 23 % → 27 % | 194.4 px | 0.41 | 1.15 | 20 |
| stroke 12 | 20 % → 20 % | 212.5 px | 0.39 | 1.00 | 13 |
| stroke 13 | 15 % → 15 % | 150.5 px | 0.42 | 1.00 | 22 |
| stroke 14 | 15 % → 15 % | 121.2 px | 0.38 | 1.00 | 18 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #38 Sanguine drawing — own sheet
own sheet 600 × 600 · Pastel 1.00 · 6 px · 2.9 s

![Brush Artist · Refs · #38 Sanguine drawing — own sheet](Brush-Artist-Refs-38-Sanguine-drawing-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 3 % → 15 % | 3.3 px | 0.57 | 4.99 | 11 |
| stroke 2 | 3 % → 8 % | 2.9 px | 0.57 | 3.03 | 6 |
| stroke 3 | 3 % → 9 % | 3.3 px | 0.57 | 3.13 | 9 |
| stroke 4 | 2 % → 18 % | 2.8 px | 0.57 | 7.17 | 7 |
| stroke 5 | 3 % → 7 % | 2.9 px | 0.57 | 2.87 | 11 |
| stroke 6 | 3 % → 19 % | 3.5 px | 0.57 | 6.36 | 7 |
| stroke 7 | 5 % → 15 % | 5.3 px | 0.57 | 3.13 | 6 |
| stroke 8 | 4 % → 16 % | 4.8 px | 0.57 | 3.71 | 11 |
| stroke 9 | 3 % → 8 % | 3.4 px | 0.57 | 2.52 | 7 |
| stroke 10 | 4 % → 16 % | 4.9 px | 0.57 | 3.75 | 7 |
| stroke 11 | 3 % → 4 % | 3.0 px | 0.57 | 1.63 | 7 |
| stroke 12 | 4 % → 16 % | 4.7 px | 0.57 | 3.75 | 6 |
| stroke 13 | 8 % → 18 % | 9.2 px | 0.57 | 2.20 | 7 |
| stroke 14 | 5 % → 14 % | 5.3 px | 0.57 | 2.95 | 6 |
| stroke 15 | 9 % → 18 % | 10.7 px | 0.57 | 1.88 | 6 |
| stroke 16 | 6 % → 16 % | 7.0 px | 0.57 | 2.64 | 11 |
| stroke 17 | 4 % → 9 % | 5.0 px | 0.57 | 2.12 | 14 |
| stroke 18 | 3 % → 5 % | 3.1 px | 0.57 | 1.89 | 6 |
| stroke 19 | 6 % → 17 % | 7.4 px | 0.57 | 2.68 | 11 |
| stroke 20 | 9 % → 14 % | 9.8 px | 0.57 | 1.66 | 7 |
| stroke 21 | 4 % → 4 % | 4.6 px | 0.57 | 1.00 | 12 |
| stroke 22 | 8 % → 14 % | 9.2 px | 0.57 | 1.71 | 6 |
| stroke 23 | 8 % → 12 % | 8.7 px | 0.57 | 1.63 | 6 |
| stroke 24 | 4 % → 8 % | 5.0 px | 0.57 | 1.72 | 7 |
| stroke 25 | 8 % → 15 % | 9.3 px | 0.57 | 1.87 | 8 |
| stroke 26 | 6 % → 8 % | 6.9 px | 0.57 | 1.32 | 6 |
| stroke 27 | 4 % → 5 % | 4.8 px | 0.57 | 1.07 | 6 |
| stroke 28 | 8 % → 13 % | 8.9 px | 0.57 | 1.61 | 9 |
| stroke 29 | 8 % → 17 % | 9.0 px | 0.57 | 2.18 | 7 |
| stroke 30 | 13 % → 17 % | 15.2 px | 0.57 | 1.29 | 6 |
| stroke 31 | 5 % → 7 % | 6.0 px | 0.57 | 1.24 | 7 |
| stroke 32 | 11 % → 14 % | 12.9 px | 0.57 | 1.23 | 17 |
| stroke 33 | 8 % → 9 % | 9.5 px | 0.57 | 1.06 | 7 |
| stroke 34 | 11 % → 14 % | 12.3 px | 0.57 | 1.34 | 13 |
| stroke 35 | 9 % → 15 % | 10.7 px | 0.57 | 1.57 | 8 |
| stroke 36 | 10 % → 13 % | 11.9 px | 0.57 | 1.26 | 6 |
| stroke 37 | 10 % → 16 % | 11.4 px | 0.57 | 1.63 | 7 |
| stroke 38 | 14 % → 20 % | 15.3 px | 0.57 | 1.46 | 6 |
| stroke 39 | 14 % → 17 % | 16.5 px | 0.57 | 1.20 | 11 |
| stroke 40 | 6 % → 7 % | 7.3 px | 0.57 | 1.15 | 6 |
| stroke 41 | 16 % → 16 % | 18.2 px | 0.57 | 1.01 | 6 |
| stroke 42 | 14 % → 16 % | 16.1 px | 0.57 | 1.15 | 6 |
| stroke 43 | 11 % → 13 % | 13.0 px | 0.57 | 1.16 | 12 |
| stroke 44 | 13 % → 16 % | 15.2 px | 0.57 | 1.19 | 8 |
| stroke 45 | 2 % → 2 % | 2.8 px | 0.56 | 1.00 | 11 |
| stroke 46 | 17 % → 17 % | 18.9 px | 0.57 | 1.00 | 10 |
| stroke 47 | 14 % → 14 % | 15.9 px | 0.57 | 1.00 | 7 |
| stroke 48 | 13 % → 14 % | 14.7 px | 0.57 | 1.06 | 9 |
| stroke 49 | 19 % → 19 % | 21.8 px | 0.57 | 1.00 | 6 |
| stroke 50 | 11 % → 11 % | 12.2 px | 0.57 | 1.00 | 6 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #39 Very thick impasto — own sheet
own sheet 600 × 600 · Impasto 1.00 · 60 px · 6.1 s

![Brush Artist · Refs · #39 Very thick impasto — own sheet](Brush-Artist-Refs-39-Very-thick-impasto-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 24 % → 35 % | 55.6 px | 0.43 | 1.44 | 296 |
| stroke 2 | 30 % → 46 % | 91.2 px | 0.43 | 1.52 | 340 |
| stroke 3 | 37 % → 48 % | 123.1 px | 0.44 | 1.31 | 603 |
| stroke 4 | 31 % → 43 % | 90.2 px | 0.43 | 1.39 | 611 |
| stroke 5 | 41 % → 39 % | 102.0 px | 0.43 | 0.97 | 530 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #40 Watercolour blooms — own sheet
own sheet 600 × 600 · Watercolour 1.00 · 90 px · 10.4 s

![Brush Artist · Refs · #40 Watercolour blooms — own sheet](Brush-Artist-Refs-40-Watercolour-blooms-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 21 % → 27 % | 92.8 px | 0.12 | 1.28 | 1260 |

## Brush Artist · Refs · #41 Coloured pencil hatching — own sheet
own sheet 600 × 600 · Pastel 1.00 · 4 px · 3.1 s

![Brush Artist · Refs · #41 Coloured pencil hatching — own sheet](Brush-Artist-Refs-41-Coloured-pencil-hatching-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 3 % → 15 % | 2.3 px | 0.35 | 5.04 | 10 |
| stroke 2 | 3 % → 8 % | 2.5 px | 0.35 | 2.34 | 13 |
| stroke 3 | 3 % → 12 % | 2.2 px | 0.35 | 4.03 | 6 |
| stroke 4 | 3 % → 20 % | 2.4 px | 0.35 | 6.35 | 7 |
| stroke 5 | 4 % → 8 % | 3.5 px | 0.35 | 1.78 | 7 |
| stroke 6 | 3 % → 14 % | 2.3 px | 0.35 | 4.57 | 12 |
| stroke 7 | 4 % → 17 % | 3.0 px | 0.35 | 4.34 | 9 |
| stroke 8 | 3 % → 13 % | 2.4 px | 0.35 | 4.14 | 8 |
| stroke 9 | 5 % → 12 % | 4.1 px | 0.35 | 2.18 | 8 |
| stroke 10 | 6 % → 17 % | 4.4 px | 0.35 | 2.92 | 6 |
| stroke 11 | 4 % → 14 % | 3.2 px | 0.35 | 3.38 | 10 |
| stroke 12 | 3 % → 3 % | 2.2 px | 0.35 | 1.00 | 9 |
| stroke 13 | 8 % → 19 % | 6.0 px | 0.35 | 2.35 | 8 |
| stroke 14 | 4 % → 15 % | 2.7 px | 0.35 | 4.14 | 7 |
| stroke 15 | 6 % → 13 % | 4.6 px | 0.35 | 2.12 | 10 |
| stroke 16 | 7 % → 12 % | 5.6 px | 0.35 | 1.63 | 8 |
| stroke 17 | 3 % → 3 % | 2.4 px | 0.35 | 1.00 | 6 |
| stroke 18 | 5 % → 9 % | 4.0 px | 0.36 | 1.63 | 8 |
| stroke 19 | 5 % → 14 % | 4.0 px | 0.35 | 2.72 | 8 |
| stroke 20 | 6 % → 16 % | 4.2 px | 0.35 | 2.94 | 9 |
| stroke 21 | 5 % → 15 % | 3.6 px | 0.35 | 3.13 | 10 |
| stroke 22 | 10 % → 18 % | 7.7 px | 0.35 | 1.77 | 5 |
| stroke 23 | 10 % → 15 % | 7.2 px | 0.35 | 1.54 | 5 |
| stroke 24 | 7 % → 15 % | 5.3 px | 0.35 | 2.12 | 7 |
| stroke 25 | 5 % → 12 % | 4.0 px | 0.35 | 2.27 | 9 |
| stroke 26 | 4 % → 7 % | 3.1 px | 0.35 | 1.79 | 5 |
| stroke 27 | 3 % → 8 % | 2.6 px | 0.35 | 2.35 | 10 |
| stroke 28 | 7 % → 11 % | 5.2 px | 0.36 | 1.68 | 6 |
| stroke 29 | 3 % → 15 % | 2.6 px | 0.35 | 4.48 | 5 |
| stroke 30 | 7 % → 10 % | 5.2 px | 0.35 | 1.40 | 5 |
| stroke 31 | 7 % → 16 % | 5.8 px | 0.35 | 2.09 | 5 |
| stroke 32 | 3 % → 6 % | 2.4 px | 0.36 | 1.93 | 4 |
| stroke 33 | 8 % → 13 % | 5.9 px | 0.35 | 1.65 | 5 |
| stroke 34 | 3 % → 6 % | 2.6 px | 0.35 | 1.71 | 4 |
| stroke 35 | 7 % → 15 % | 5.4 px | 0.35 | 2.11 | 6 |
| stroke 36 | 5 % → 5 % | 4.0 px | 0.35 | 1.01 | 4 |
| stroke 37 | 8 % → 16 % | 5.9 px | 0.35 | 2.07 | 6 |
| stroke 38 | 8 % → 14 % | 6.2 px | 0.35 | 1.71 | 10 |
| stroke 39 | 7 % → 12 % | 5.4 px | 0.35 | 1.65 | 5 |
| stroke 40 | 9 % → 20 % | 6.7 px | 0.36 | 2.23 | 4 |
| stroke 41 | 10 % → 15 % | 7.7 px | 0.35 | 1.46 | 4 |
| stroke 42 | 11 % → 19 % | 8.5 px | 0.36 | 1.73 | 4 |
| stroke 43 | 5 % → 9 % | 4.1 px | 0.35 | 1.66 | 4 |
| stroke 44 | 11 % → 15 % | 8.5 px | 0.36 | 1.41 | 4 |
| stroke 45 | 14 % → 19 % | 10.5 px | 0.35 | 1.37 | 9 |
| stroke 46 | 5 % → 7 % | 4.0 px | 0.35 | 1.38 | 4 |
| stroke 47 | 11 % → 14 % | 8.7 px | 0.36 | 1.21 | 6 |
| stroke 48 | 13 % → 18 % | 10.0 px | 0.36 | 1.36 | 6 |
| stroke 49 | 6 % → 9 % | 4.3 px | 0.35 | 1.65 | 4 |
| stroke 50 | 7 % → 7 % | 5.6 px | 0.35 | 1.00 | 4 |
| stroke 51 | 10 % → 16 % | 7.4 px | 0.36 | 1.67 | 7 |
| stroke 52 | 14 % → 16 % | 10.5 px | 0.35 | 1.19 | 4 |
| stroke 53 | 12 % → 16 % | 9.0 px | 0.35 | 1.35 | 5 |
| stroke 54 | 11 % → 16 % | 8.5 px | 0.35 | 1.46 | 5 |
| stroke 55 | 12 % → 16 % | 9.0 px | 0.35 | 1.34 | 4 |
| stroke 56 | 12 % → 13 % | 9.0 px | 0.35 | 1.11 | 4 |
| stroke 57 | 11 % → 14 % | 8.2 px | 0.36 | 1.31 | 4 |
| stroke 58 | 11 % → 12 % | 8.6 px | 0.35 | 1.12 | 6 |
| stroke 59 | 13 % → 15 % | 9.8 px | 0.35 | 1.16 | 5 |
| stroke 60 | 17 % → 22 % | 13.1 px | 0.35 | 1.26 | 4 |
| stroke 61 | 21 % → 22 % | 15.6 px | 0.35 | 1.05 | 5 |
| stroke 62 | 10 % → 10 % | 7.5 px | 0.35 | 1.00 | 6 |
| stroke 63 | 12 % → 13 % | 9.5 px | 0.35 | 1.09 | 6 |
| stroke 64 | 16 % → 17 % | 12.4 px | 0.35 | 1.02 | 6 |
| stroke 65 | 17 % → 17 % | 12.7 px | 0.35 | 1.00 | 5 |
| stroke 66 | 15 % → 15 % | 11.9 px | 0.35 | 1.00 | 5 |
| stroke 67 | 13 % → 14 % | 9.9 px | 0.35 | 1.06 | 8 |
| stroke 68 | 5 % → 10 % | 4.1 px | 0.35 | 1.90 | 5 |
| stroke 69 | 6 % → 6 % | 4.3 px | 0.35 | 1.00 | 4 |
| stroke 70 | 11 % → 14 % | 8.5 px | 0.35 | 1.28 | 4 |
| stroke 71 | 10 % → 12 % | 7.7 px | 0.35 | 1.17 | 4 |
| stroke 72 | 6 % → 7 % | 4.5 px | 0.35 | 1.26 | 9 |
| stroke 73 | 14 % → 14 % | 10.4 px | 0.35 | 1.00 | 5 |
| stroke 74 | 16 % → 16 % | 12.3 px | 0.35 | 1.00 | 4 |
| stroke 75 | 17 % → 17 % | 13.1 px | 0.35 | 1.00 | 5 |
| stroke 76 | 15 % → 15 % | 11.7 px | 0.36 | 1.00 | 5 |
| stroke 77 | 8 % → 10 % | 6.0 px | 0.35 | 1.32 | 5 |
| stroke 78 | 10 % → 10 % | 7.5 px | 0.35 | 1.00 | 5 |
| stroke 79 | 8 % → 8 % | 6.2 px | 0.35 | 1.00 | 5 |
| stroke 80 | 12 % → 12 % | 9.1 px | 0.36 | 1.00 | 4 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #42 Oil pastel shaggy — own sheet
own sheet 600 × 600 · Pastel 1.00 · 18 px · 3.0 s

![Brush Artist · Refs · #42 Oil pastel shaggy — own sheet](Brush-Artist-Refs-42-Oil-pastel-shaggy-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 5 % → 27 % | 8.5 px | 0.27 | 5.25 | 10 |
| stroke 2 | 5 % → 24 % | 7.8 px | 0.29 | 5.02 | 16 |
| stroke 3 | 5 % → 29 % | 8.8 px | 0.28 | 5.49 | 12 |
| stroke 4 | 5 % → 11 % | 9.1 px | 0.26 | 1.99 | 17 |
| stroke 5 | 6 % → 11 % | 10.2 px | 0.26 | 1.77 | 10 |
| stroke 6 | 8 % → 36 % | 13.4 px | 0.28 | 4.52 | 12 |
| stroke 7 | 11 % → 30 % | 18.0 px | 0.28 | 2.79 | 11 |
| stroke 8 | 7 % → 37 % | 10.8 px | 0.28 | 5.63 | 10 |
| stroke 9 | 8 % → 21 % | 13.4 px | 0.28 | 2.61 | 10 |
| stroke 10 | 8 % → 18 % | 13.2 px | 0.29 | 2.30 | 10 |
| stroke 11 | 5 % → 26 % | 8.8 px | 0.28 | 4.89 | 10 |
| stroke 12 | 8 % → 19 % | 13.1 px | 0.28 | 2.33 | 10 |
| stroke 13 | 12 % → 23 % | 20.4 px | 0.28 | 1.91 | 10 |
| stroke 14 | 5 % → 22 % | 7.6 px | 0.28 | 4.76 | 13 |
| stroke 15 | 6 % → 24 % | 9.1 px | 0.28 | 4.28 | 11 |
| stroke 16 | 9 % → 21 % | 15.5 px | 0.29 | 2.21 | 15 |
| stroke 17 | 16 % → 37 % | 26.3 px | 0.28 | 2.36 | 10 |
| stroke 18 | 14 % → 25 % | 22.6 px | 0.28 | 1.82 | 16 |
| stroke 19 | 14 % → 30 % | 23.7 px | 0.28 | 2.08 | 13 |
| stroke 20 | 21 % → 39 % | 35.4 px | 0.28 | 1.81 | 11 |
| stroke 21 | 9 % → 16 % | 14.2 px | 0.28 | 1.88 | 17 |
| stroke 22 | 14 % → 17 % | 23.1 px | 0.27 | 1.19 | 12 |
| stroke 23 | 12 % → 17 % | 20.4 px | 0.29 | 1.37 | 10 |
| stroke 24 | 18 % → 26 % | 30.0 px | 0.29 | 1.43 | 13 |
| stroke 25 | 19 % → 34 % | 32.1 px | 0.28 | 1.75 | 10 |
| stroke 26 | 5 % → 13 % | 8.8 px | 0.28 | 2.45 | 12 |
| stroke 27 | 18 % → 26 % | 30.3 px | 0.29 | 1.41 | 11 |
| stroke 28 | 14 % → 23 % | 23.2 px | 0.29 | 1.66 | 14 |
| stroke 29 | 9 % → 26 % | 14.2 px | 0.29 | 3.08 | 11 |
| stroke 30 | 15 % → 36 % | 24.5 px | 0.28 | 2.44 | 10 |
| stroke 31 | 13 % → 17 % | 22.3 px | 0.29 | 1.24 | 10 |
| stroke 32 | 16 % → 29 % | 26.3 px | 0.29 | 1.82 | 14 |
| stroke 33 | 15 % → 16 % | 24.3 px | 0.28 | 1.09 | 11 |
| stroke 34 | 19 % → 27 % | 31.4 px | 0.28 | 1.44 | 10 |
| stroke 35 | 25 % → 35 % | 40.9 px | 0.28 | 1.39 | 16 |
| stroke 36 | 24 % → 33 % | 40.2 px | 0.28 | 1.34 | 11 |
| stroke 37 | 11 % → 12 % | 18.4 px | 0.28 | 1.04 | 11 |
| stroke 38 | 19 % → 24 % | 30.7 px | 0.29 | 1.31 | 10 |
| stroke 39 | 16 % → 22 % | 27.0 px | 0.27 | 1.35 | 11 |
| stroke 40 | 21 % → 29 % | 34.9 px | 0.28 | 1.37 | 18 |
| stroke 41 | 31 % → 34 % | 51.2 px | 0.28 | 1.12 | 10 |
| stroke 42 | 23 % → 29 % | 37.9 px | 0.28 | 1.28 | 13 |
| stroke 43 | 12 % → 12 % | 20.2 px | 0.28 | 1.00 | 10 |
| stroke 44 | 29 % → 36 % | 48.3 px | 0.28 | 1.24 | 10 |
| stroke 45 | 16 % → 16 % | 25.6 px | 0.27 | 1.00 | 10 |
| stroke 46 | 28 % → 33 % | 46.9 px | 0.28 | 1.15 | 10 |
| stroke 47 | 37 % → 41 % | 61.6 px | 0.28 | 1.09 | 22 |
| stroke 48 | 28 % → 35 % | 47.2 px | 0.28 | 1.26 | 14 |
| stroke 49 | 27 % → 30 % | 43.8 px | 0.29 | 1.11 | 10 |
| stroke 50 | 37 % → 40 % | 61.8 px | 0.28 | 1.07 | 14 |
| stroke 51 | 15 % → 15 % | 25.8 px | 0.28 | 1.00 | 10 |
| stroke 52 | 37 % → 37 % | 61.4 px | 0.28 | 1.01 | 10 |
| stroke 53 | 22 % → 26 % | 35.6 px | 0.29 | 1.20 | 12 |
| stroke 54 | 17 % → 19 % | 29.0 px | 0.29 | 1.10 | 10 |
| stroke 55 | 15 % → 15 % | 24.6 px | 0.29 | 1.00 | 10 |
| stroke 56 | 13 % → 14 % | 21.3 px | 0.27 | 1.08 | 10 |
| stroke 57 | 23 % → 23 % | 38.0 px | 0.29 | 1.00 | 11 |
| stroke 58 | 26 % → 28 % | 43.7 px | 0.28 | 1.06 | 11 |
| stroke 59 | 40 % → 40 % | 66.1 px | 0.28 | 1.00 | 16 |
| stroke 60 | 21 % → 21 % | 34.4 px | 0.29 | 1.00 | 10 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #43 Dragged black ink blocks — own sheet
own sheet 600 × 600 · Gouache 1.00 · 70 px · 8.9 s

![Brush Artist · Refs · #43 Dragged black ink blocks — own sheet](Brush-Artist-Refs-43-Dragged-black-ink-blocks-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 19 % → 12 % | 43.7 px | 0.43 | 0.63 | 461 |
| stroke 2 | 18 % → 14 % | 65.2 px | 0.43 | 0.75 | 537 |
| stroke 3 | 26 % → 19 % | 91.9 px | 0.43 | 0.74 | 553 |
| stroke 4 | 27 % → 17 % | 95.5 px | 0.41 | 0.62 | 609 |
| stroke 5 | 35 % → 18 % | 81.1 px | 0.40 | 0.51 | 576 |

## Brush Artist · Refs · #44 Blue looping ribbon — own sheet
own sheet 600 × 600 · Oil 1.00 · 80 px · 5.5 s

![Brush Artist · Refs · #44 Blue looping ribbon — own sheet](Brush-Artist-Refs-44-Blue-looping-ribbon-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 32 % → 32 % | 42.1 px | 0.78 | 1.00 | 2809 |

## Brush Artist · Refs · #45 Soft pastel pepper — own sheet
own sheet 600 × 600 · Pastel 1.00 · 40 px · 6.3 s

![Brush Artist · Refs · #45 Soft pastel pepper — own sheet](Brush-Artist-Refs-45-Soft-pastel-pepper-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 10 % → 38 % | 11.3 px | 0.50 | 3.71 | 357 |
| stroke 2 | 18 % → 33 % | 20.7 px | 0.50 | 1.88 | 354 |
| stroke 3 | 25 % → 36 % | 16.9 px | 0.50 | 1.46 | 322 |
| stroke 4 | 24 % → 34 % | 29.4 px | 0.50 | 1.45 | 695 |
| stroke 5 | 30 % → 30 % | 20.9 px | 0.49 | 1.00 | 396 |
| stroke 6 | 35 % → 44 % | 22.7 px | 0.50 | 1.24 | 626 |
| stroke 7 | 39 % → 43 % | 21.3 px | 0.50 | 1.11 | 703 |
| stroke 8 | 43 % → 43 % | 43.7 px | 0.50 | 1.00 | 538 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #46 Red-brown ink lips — own sheet
own sheet 600 × 600 · Watercolour 1.00 · 50 px · 10.5 s

![Brush Artist · Refs · #46 Red-brown ink lips — own sheet](Brush-Artist-Refs-46-Red-brown-ink-lips-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 13 % → 26 % | 54.5 px | 0.56 | 1.96 | 199 |
| stroke 2 | 17 % → 31 % | 72.4 px | 0.53 | 1.89 | 113 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #47 Pink knife slabs — own sheet
own sheet 600 × 600 · Impasto 1.00 · 90 px · 5.8 s

![Brush Artist · Refs · #47 Pink knife slabs — own sheet](Brush-Artist-Refs-47-Pink-knife-slabs-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 16 % → 32 % | 81.5 px | 0.10 | 1.97 | 493 |
| stroke 2 | 29 % → 42 % | 165.6 px | 0.11 | 1.45 | 336 |
| stroke 3 | 29 % → 43 % | 165.1 px | 0.13 | 1.47 | 475 |
| stroke 4 | 39 % → 38 % | 165.8 px | 0.14 | 0.97 | 342 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #48 Black bands with drips — own sheet
own sheet 600 × 600 · Gouache 1.00 · 70 px · 15.6 s

![Brush Artist · Refs · #48 Black bands with drips — own sheet](Brush-Artist-Refs-48-Black-bands-with-drips-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 28 % → 40 % | 72.6 px | 0.38 | 1.43 | 664 |
| stroke 2 | 43 % → 55 % | 137.3 px | 0.38 | 1.30 | 625 |
| stroke 3 | 45 % → 56 % | 141.4 px | 0.38 | 1.23 | 737 |
| stroke 4 | 48 % → 45 % | 139.2 px | 0.37 | 0.94 | 756 |

## Brush Artist · Refs · #49 Magenta letters round brush — own sheet
own sheet 600 × 600 · Ink 1.00 · 30 px · 12.7 s

![Brush Artist · Refs · #49 Magenta letters round brush — own sheet](Brush-Artist-Refs-49-Magenta-letters-round-brush-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 27 % → 46 % | 64.7 px | 0.52 | 1.68 | 29 |
| stroke 2 | 29 % → 41 % | 53.0 px | 0.53 | 1.40 | 31 |
| stroke 3 | 42 % → 68 % | 98.0 px | 0.52 | 1.62 | 36 |
| stroke 4 | 33 % → 52 % | 53.5 px | 0.52 | 1.56 | 153 |
| stroke 5 | 41 % → 66 % | 97.1 px | 0.52 | 1.62 | 105 |
| stroke 6 | 56 % → 72 % | 237.9 px | 0.52 | 1.28 | 21 |
| stroke 7 | 42 % → 58 % | 65.1 px | 0.52 | 1.36 | 108 |
| stroke 8 | 36 % → 61 % | 92.6 px | 0.53 | 1.71 | 72 |
| stroke 9 | 50 % → 62 % | 156.5 px | 0.52 | 1.24 | 38 |
| stroke 10 | 43 % → 73 % | 102.9 px | 0.52 | 1.68 | 141 |
| stroke 11 | 52 % → 72 % | 221.9 px | 0.52 | 1.39 | 28 |
| stroke 12 | 54 % → 70 % | 84.9 px | 0.52 | 1.28 | 152 |
| stroke 13 | 42 % → 53 % | 116.2 px | 0.53 | 1.27 | 50 |
| stroke 14 | 45 % → 68 % | 131.6 px | 0.53 | 1.52 | 53 |
| stroke 15 | 43 % → 63 % | 101.8 px | 0.52 | 1.47 | 105 |
| stroke 16 | 52 % → 61 % | 220.3 px | 0.52 | 1.19 | 24 |
| stroke 17 | 53 % → 64 % | 82.3 px | 0.52 | 1.19 | 197 |
| stroke 18 | 36 % → 43 % | 98.8 px | 0.53 | 1.20 | 33 |
| stroke 19 | 53 % → 52 % | 122.0 px | 0.52 | 0.99 | 29 |
| stroke 20 | 55 % → 55 % | 127.4 px | 0.52 | 1.00 | 28 |
| stroke 21 | 49 % → 49 % | 80.4 px | 0.52 | 1.00 | 117 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #50 Thick swipes on photo — own sheet
own sheet 600 × 600 · Impasto 1.00 · 40 px · 4.5 s

![Brush Artist · Refs · #50 Thick swipes on photo — own sheet](Brush-Artist-Refs-50-Thick-swipes-on-photo-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 9 % → 21 % | 43.0 px | 0.35 | 2.32 | 47 |
| stroke 2 | 9 % → 16 % | 42.2 px | 0.34 | 1.82 | 42 |
| stroke 3 | 10 % → 11 % | 42.0 px | 0.32 | 1.06 | 56 |
| stroke 4 | 11 % → 18 % | 44.0 px | 0.35 | 1.60 | 49 |
| stroke 5 | 11 % → 10 % | 42.2 px | 0.34 | 0.94 | 45 |
| stroke 6 | 17 % → 21 % | 99.5 px | 0.35 | 1.19 | 40 |
| stroke 7 | 22 % → 26 % | 92.9 px | 0.35 | 1.18 | 72 |
| stroke 8 | 21 % → 20 % | 119.7 px | 0.35 | 0.96 | 119 |
| stroke 9 | 10 % → 11 % | 43.0 px | 0.30 | 1.11 | 77 |
| stroke 10 | 22 % → 22 % | 75.4 px | 0.35 | 0.96 | 100 |
| stroke 11 | 8 % → 8 % | 41.8 px | 0.36 | 0.95 | 67 |
| stroke 12 | 17 % → 16 % | 94.4 px | 0.35 | 0.96 | 38 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Ink — dry brush — own sheet
own sheet 600 × 600 · Gouache 1.00 · 30 px · 4.1 s

![Brush Artist · Ink — dry brush — own sheet](Brush-Artist-Ink-dry-brush-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| ear | 8 % → 3 % | 10.3 px | 0.85 | 0.33 | 656 |
| drag0 | 5 % → 9 % | 10.0 px | 0.85 | 1.67 | 182 |
| drag1 | 9 % → 10 % | 18.7 px | 0.85 | 1.07 | 132 |
| drag2 | 11 % → 10 % | 25.2 px | 0.85 | 0.91 | 129 |
| drag3 | 14 % → 11 % | 35.4 px | 0.85 | 0.76 | 128 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Watercolour — blue — own sheet
own sheet 600 × 600 · Watercolour 0.93 · Ink 0.07 · 40 px · 21.3 s

![Brush Artist · Watercolour — blue — own sheet](Brush-Artist-Watercolour-blue-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| s0 | 7 % → 24 % | 28.8 px | 0.30 | 3.32 | 42 |
| s1 | 6 % → 33 % | 10.1 px | 0.37 | 6.00 | 48 |
| s2 | 10 % → 19 % | 44.2 px | 0.26 | 1.81 | 50 |
| s3 | 10 % → 18 % | 26.7 px | 0.31 | 1.92 | 112 |
| s4 | 14 % → 30 % | 38.6 px | 0.36 | 2.16 | 136 |
| s5 | 19 % → 29 % | 39.3 px | 0.37 | 1.54 | 100 |
| s6 | 18 % → 22 % | 48.7 px | 0.31 | 1.25 | 86 |
| s7 | 25 % → 36 % | 32.7 px | 0.37 | 1.46 | 99 |
| s8 | 21 % → 25 % | 79.8 px | 0.30 | 1.20 | 149 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Charcoal — stick — own sheet
own sheet 600 × 600 · Charcoal 0.78 · Pastel 0.22 · 28 px · 2.4 s

![Brush Artist · Charcoal — stick — own sheet](Brush-Artist-Charcoal-stick-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| finger0 | 12 % → 25 % | 21.2 px | 0.83 | 2.03 | 51 |
| tip0 | 13 % → 21 % | 33.8 px | 0.83 | 1.70 | 12 |
| finger1 | 23 % → 41 % | 40.4 px | 0.83 | 1.77 | 44 |
| tip1 | 21 % → 29 % | 57.3 px | 0.83 | 1.38 | 13 |
| finger2 | 25 % → 37 % | 43.8 px | 0.83 | 1.49 | 45 |
| tip2 | 21 % → 29 % | 55.7 px | 0.83 | 1.40 | 12 |
| finger3 | 24 % → 27 % | 42.7 px | 0.83 | 1.14 | 36 |
| tip3 | 20 % → 20 % | 54.1 px | 0.83 | 1.00 | 15 |
| cig0 | 34 % → 47 % | 75.0 px | 0.83 | 1.39 | 24 |
| cig1 | 36 % → 47 % | 80.5 px | 0.83 | 1.30 | 34 |
| cig2 | 39 % → 47 % | 86.7 px | 0.83 | 1.20 | 46 |
| cig3 | 41 % → 47 % | 91.3 px | 0.83 | 1.14 | 30 |
| cig4 | 44 % → 46 % | 97.5 px | 0.83 | 1.06 | 23 |
| cig5 | 46 % → 46 % | 102.9 px | 0.83 | 1.00 | 22 |

Numbers say: wet paint spreads well beyond the stroke.

## Oil focus · A G x2 — own sheet
own sheet 2000 × 1320 · Gouache 1.00 + turpentine 15 % · 260 px · 121.4 s

![Oil focus · A G x2 — own sheet](Oil-focus-A-G-x2-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 15 % → 53 % | 191.4 px | 0.49 | 3.40 | 12364 |
| stroke 2 | 28 % → 34 % | 352.2 px | 0.39 | 1.21 | 9312 |
| stroke 3 | 34 % → 35 % | 315.4 px | 0.45 | 1.04 | 13627 |
| stroke 4 | 40 % → 33 % | 553.2 px | 0.49 | 0.83 | 14254 |
| stroke 5 | 49 % → 37 % | 798.7 px | 0.51 | 0.75 | 6693 |

Numbers say: wet paint spreads well beyond the stroke.

## Oil focus · B G x2 soft — own sheet
own sheet 2000 × 1320 · Gouache 1.00 + turpentine 15 % · 260 px · 119.5 s

![Oil focus · B G x2 soft — own sheet](Oil-focus-B-G-x2-soft-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 15 % → 52 % | 190.3 px | 0.49 | 3.38 | 11661 |
| stroke 2 | 28 % → 34 % | 351.7 px | 0.39 | 1.18 | 8965 |
| stroke 3 | 34 % → 35 % | 314.3 px | 0.45 | 1.04 | 13368 |
| stroke 4 | 40 % → 33 % | 550.6 px | 0.49 | 0.82 | 14196 |
| stroke 5 | 49 % → 36 % | 797.9 px | 0.51 | 0.74 | 6486 |

Numbers say: wet paint spreads well beyond the stroke.

## Oil focus · C G x2 mix low — own sheet
own sheet 2000 × 1320 · Gouache 1.00 + turpentine 15 % · 260 px · 115.4 s

![Oil focus · C G x2 mix low — own sheet](Oil-focus-C-G-x2-mix-low-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 15 % → 53 % | 191.4 px | 0.47 | 3.40 | 8042 |
| stroke 2 | 28 % → 34 % | 352.2 px | 0.39 | 1.21 | 7493 |
| stroke 3 | 34 % → 35 % | 315.4 px | 0.44 | 1.04 | 14341 |
| stroke 4 | 40 % → 33 % | 553.2 px | 0.48 | 0.83 | 15173 |
| stroke 5 | 49 % → 37 % | 798.7 px | 0.49 | 0.75 | 10840 |

Numbers say: wet paint spreads well beyond the stroke.

## Oil focus · D G x2 no pickup — own sheet
own sheet 2000 × 1320 · Gouache 1.00 + turpentine 15 % · 260 px · 96.7 s

![Oil focus · D G x2 no pickup — own sheet](Oil-focus-D-G-x2-no-pickup-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 15 % → 52 % | 191.3 px | 0.49 | 3.35 | 8557 |
| stroke 2 | 28 % → 33 % | 352.1 px | 0.39 | 1.16 | 8394 |
| stroke 3 | 34 % → 34 % | 313.4 px | 0.45 | 1.03 | 15048 |
| stroke 4 | 40 % → 32 % | 549.8 px | 0.49 | 0.82 | 12041 |
| stroke 5 | 49 % → 36 % | 797.5 px | 0.51 | 0.74 | 5151 |

Numbers say: wet paint spreads well beyond the stroke.

## Oil focus · E G x2 dilute 0.3 — own sheet
own sheet 2000 × 1320 · Gouache 1.00 + turpentine 30 % · 260 px · 95.7 s

![Oil focus · E G x2 dilute 0.3 — own sheet](Oil-focus-E-G-x2-dilute-0-3-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 15 % → 52 % | 191.4 px | 0.47 | 3.35 | 8383 |
| stroke 2 | 28 % → 33 % | 352.2 px | 0.36 | 1.17 | 7891 |
| stroke 3 | 34 % → 35 % | 314.1 px | 0.44 | 1.03 | 14834 |
| stroke 4 | 40 % → 33 % | 549.6 px | 0.47 | 0.82 | 11706 |
| stroke 5 | 49 % → 36 % | 797.0 px | 0.49 | 0.74 | 5494 |

Numbers say: wet paint spreads well beyond the stroke.

## Oil focus · F G x2 wet load — own sheet
own sheet 2000 × 1320 · Gouache 1.00 + turpentine 15 % · 260 px · 96.0 s

![Oil focus · F G x2 wet load — own sheet](Oil-focus-F-G-x2-wet-load-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 15 % → 54 % | 190.6 px | 0.48 | 3.48 | 7561 |
| stroke 2 | 28 % → 36 % | 351.7 px | 0.39 | 1.26 | 8989 |
| stroke 3 | 36 % → 36 % | 339.3 px | 0.45 | 0.98 | 13116 |
| stroke 4 | 43 % → 34 % | 591.4 px | 0.48 | 0.80 | 11412 |
| stroke 5 | 50 % → 37 % | 816.5 px | 0.50 | 0.74 | 6594 |

Numbers say: wet paint spreads well beyond the stroke.

## Oil focus · G G x2 fine hairs — own sheet
own sheet 2000 × 1320 · Gouache 1.00 + turpentine 15 % · 260 px · 77.2 s

![Oil focus · G G x2 fine hairs — own sheet](Oil-focus-G-G-x2-fine-hairs-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 15 % → 46 % | 187.0 px | 0.48 | 3.03 | 9486 |
| stroke 2 | 28 % → 27 % | 347.7 px | 0.37 | 0.96 | 5244 |
| stroke 3 | 33 % → 32 % | 310.1 px | 0.44 | 0.98 | 9824 |
| stroke 4 | 38 % → 28 % | 533.2 px | 0.49 | 0.74 | 9341 |
| stroke 5 | 48 % → 30 % | 784.1 px | 0.52 | 0.62 | 4782 |

Numbers say: wet paint spreads well beyond the stroke.

## Oil focus · H flat x2 soft — own sheet
own sheet 2000 × 1320 · Gouache 1.00 + turpentine 15 % · 260 px · 75.8 s

![Oil focus · H flat x2 soft — own sheet](Oil-focus-H-flat-x2-soft-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 15 % → 51 % | 187.7 px | 0.49 | 3.37 | 8625 |
| stroke 2 | 28 % → 34 % | 343.0 px | 0.40 | 1.22 | 4785 |
| stroke 3 | 33 % → 34 % | 308.8 px | 0.46 | 1.04 | 9024 |
| stroke 4 | 39 % → 32 % | 542.3 px | 0.49 | 0.83 | 8562 |
| stroke 5 | 47 % → 35 % | 771.5 px | 0.51 | 0.75 | 4424 |

Numbers say: wet paint spreads well beyond the stroke.

## Oil · Henry Ward · HW #02 cream over wet olive — own sheet
own sheet 600 × 600 · Watercolour 0.93 · Ink 0.07 + turpentine 80 % · 96 px · 39.5 s

![Oil · Henry Ward · HW #02 cream over wet olive — own sheet](Oil-Henry-Ward-HW-02-cream-over-wet-olive-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 44 % → 52 % | 86.0 px | 0.64 | 1.17 | 1607 |
| stroke 2 | 56 % → 58 % | 144.3 px | 0.61 | 1.03 | 2624 |
| stroke 3 | 65 % → 58 % | 205.6 px | 0.61 | 0.89 | 2003 |
| stroke 4 | 69 % → 61 % | 241.1 px | 0.62 | 0.88 | 2215 |
| stroke 5 | 69 % → 66 % | 240.7 px | 0.61 | 0.95 | 2066 |
| stroke 6 | 68 % → 55 % | 240.2 px | 0.59 | 0.81 | 2107 |
| stroke 7 | 77 % → 46 % | 239.6 px | 0.58 | 0.59 | 2014 |
| stroke 8 | 94 % → 39 % | 239.8 px | 0.60 | 0.42 | 2724 |
| stroke 9 | 100 % → 37 % | 192.3 px | 0.57 | 0.37 | 1715 |
| stroke 10 | 10 % → 58 % | 72.8 px | 0.62 | 5.76 | 292 |
| stroke 11 | 20 % → 65 % | 130.9 px | 0.62 | 3.28 | 393 |
| stroke 12 | 20 % → 50 % | 187.7 px | 0.58 | 2.45 | 211 |
| stroke 13 | 42 % → 59 % | 182.7 px | 0.61 | 1.41 | 409 |
| stroke 14 | 41 % → 58 % | 237.2 px | 0.61 | 1.43 | 435 |
| stroke 15 | 42 % → 57 % | 281.6 px | 0.62 | 1.38 | 412 |
| stroke 16 | 43 % → 57 % | 219.5 px | 0.62 | 1.33 | 598 |
| stroke 17 | 45 % → 64 % | 301.4 px | 0.60 | 1.42 | 486 |
| stroke 18 | 49 % → 65 % | 344.7 px | 0.61 | 1.32 | 452 |
| stroke 19 | 49 % → 59 % | 418.5 px | 0.59 | 1.22 | 247 |
| stroke 20 | 42 % → 50 % | 349.7 px | 0.58 | 1.19 | 278 |
| stroke 21 | 46 % → 47 % | 231.1 px | 0.58 | 1.02 | 609 |
| stroke 22 | 60 % → 59 % | 515.9 px | 0.61 | 0.99 | 435 |
| stroke 23 | 58 % → 56 % | 391.2 px | 0.62 | 0.98 | 530 |
| stroke 24 | 64 % → 65 % | 425.3 px | 0.62 | 1.00 | 441 |
| stroke 25 | 68 % → 69 % | 603.6 px | 0.60 | 1.01 | 243 |
| stroke 26 | 50 % → 50 % | 402.4 px | 0.58 | 0.99 | 372 |

Numbers say: wet paint spreads well beyond the stroke.

## Oil · Henry Ward · HW #04 grey arcs over ochre — own sheet
own sheet 600 × 600 · Gouache 1.00 + turpentine 35 % · 84 px · 62.3 s

![Oil · Henry Ward · HW #04 grey arcs over ochre — own sheet](Oil-Henry-Ward-HW-04-grey-arcs-over-ochre-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 47 % → 59 % | 79.1 px | 0.39 | 1.26 | 1590 |
| stroke 2 | 63 % → 69 % | 149.2 px | 0.40 | 1.10 | 1822 |
| stroke 3 | 70 % → 62 % | 209.4 px | 0.40 | 0.88 | 2307 |
| stroke 4 | 71 % → 69 % | 217.9 px | 0.33 | 0.98 | 2668 |
| stroke 5 | 71 % → 67 % | 218.3 px | 0.27 | 0.95 | 2690 |
| stroke 6 | 71 % → 57 % | 217.0 px | 0.20 | 0.81 | 2565 |
| stroke 7 | 75 % → 45 % | 218.8 px | 0.09 | 0.60 | 1922 |
| stroke 8 | 94 % → 48 % | 218.4 px | 0.03 | 0.51 | 2505 |
| stroke 9 | 100 % → 42 % | 167.6 px | 0.03 | 0.42 | 2911 |
| stroke 10 | 11 % → 71 % | 62.9 px | 0.29 | 6.60 | 545 |
| stroke 11 | 18 % → 62 % | 93.0 px | 0.30 | 3.47 | 656 |
| stroke 12 | 24 % → 64 % | 157.8 px | 0.31 | 2.64 | 583 |
| stroke 13 | 33 % → 67 % | 202.5 px | 0.36 | 2.03 | 603 |
| stroke 14 | 32 % → 71 % | 264.5 px | 0.29 | 2.24 | 652 |
| stroke 15 | 38 % → 64 % | 296.9 px | 0.37 | 1.67 | 658 |
| stroke 16 | 33 % → 62 % | 160.9 px | 0.32 | 1.88 | 1266 |
| stroke 17 | 53 % → 63 % | 227.8 px | 0.40 | 1.19 | 939 |
| stroke 18 | 46 % → 62 % | 216.1 px | 0.34 | 1.35 | 1069 |
| stroke 19 | 55 % → 62 % | 251.9 px | 0.39 | 1.12 | 938 |
| stroke 20 | 48 % → 66 % | 369.2 px | 0.32 | 1.37 | 796 |
| stroke 21 | 48 % → 67 % | 310.5 px | 0.30 | 1.40 | 1413 |
| stroke 22 | 51 % → 71 % | 347.7 px | 0.29 | 1.39 | 1333 |
| stroke 23 | 55 % → 65 % | 266.7 px | 0.33 | 1.18 | 1337 |
| stroke 24 | 54 % → 64 % | 275.5 px | 0.32 | 1.19 | 1312 |
| stroke 25 | 56 % → 62 % | 329.3 px | 0.34 | 1.11 | 975 |
| stroke 26 | 52 % → 62 % | 274.2 px | 0.32 | 1.19 | 1542 |
| stroke 27 | 43 % → 57 % | 245.3 px | 0.20 | 1.32 | 628 |
| stroke 28 | 40 % → 53 % | 268.0 px | 0.14 | 1.33 | 423 |
| stroke 29 | 39 % → 47 % | 235.0 px | 0.12 | 1.22 | 669 |
| stroke 30 | 47 % → 47 % | 217.0 px | 0.03 | 1.00 | 482 |

Numbers say: wet paint spreads well beyond the stroke.

## Oil · Henry Ward · HW #09 white arches over wet blue-grey — own sheet
own sheet 600 × 600 · Gouache 1.00 + turpentine 35 % · 84 px · 78.5 s

![Oil · Henry Ward · HW #09 white arches over wet blue-grey — own sheet](Oil-Henry-Ward-HW-09-white-arches-over-wet-blue-grey-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 47 % → 22 % | 81.2 px | 0.13 | 0.47 | 1867 |
| stroke 2 | 62 % → 34 % | 143.9 px | 0.13 | 0.55 | 2361 |
| stroke 3 | 70 % → 41 % | 206.7 px | 0.13 | 0.59 | 2858 |
| stroke 4 | 71 % → 54 % | 217.4 px | 0.13 | 0.76 | 3476 |
| stroke 5 | 71 % → 66 % | 219.0 px | 0.13 | 0.92 | 3149 |
| stroke 6 | 71 % → 65 % | 217.3 px | 0.12 | 0.92 | 3776 |
| stroke 7 | 75 % → 61 % | 218.8 px | 0.12 | 0.81 | 3432 |
| stroke 8 | 93 % → 59 % | 218.7 px | 0.12 | 0.63 | 3433 |
| stroke 9 | 100 % → 54 % | 167.6 px | 0.11 | 0.54 | 4126 |
| stroke 10 | 8 % → 49 % | 22.2 px | 0.12 | 6.16 | 1322 |
| stroke 11 | 14 % → 57 % | 32.8 px | 0.12 | 4.04 | 1416 |
| stroke 12 | 16 % → 59 % | 48.1 px | 0.12 | 3.75 | 1414 |
| stroke 13 | 18 % → 63 % | 61.0 px | 0.12 | 3.46 | 800 |
| stroke 14 | 22 % → 61 % | 31.7 px | 0.12 | 2.80 | 1399 |
| stroke 15 | 30 % → 58 % | 133.0 px | 0.12 | 1.96 | 2156 |
| stroke 16 | 39 % → 69 % | 204.5 px | 0.12 | 1.75 | 1706 |
| stroke 17 | 37 % → 53 % | 137.4 px | 0.13 | 1.41 | 1272 |
| stroke 18 | 46 % → 58 % | 182.4 px | 0.12 | 1.27 | 1695 |
| stroke 19 | 49 % → 58 % | 203.7 px | 0.13 | 1.18 | 1335 |
| stroke 20 | 53 % → 63 % | 216.0 px | 0.12 | 1.19 | 1443 |
| stroke 21 | 54 % → 58 % | 200.5 px | 0.11 | 1.07 | 1551 |
| stroke 22 | 63 % → 69 % | 370.7 px | 0.12 | 1.10 | 1676 |
| stroke 23 | 59 % → 61 % | 272.9 px | 0.12 | 1.05 | 1883 |
| stroke 24 | 61 % → 65 % | 332.2 px | 0.13 | 1.05 | 1072 |
| stroke 25 | 70 % → 73 % | 488.3 px | 0.12 | 1.04 | 618 |
| stroke 26 | 60 % → 61 % | 298.1 px | 0.12 | 1.02 | 1058 |
| stroke 27 | 60 % → 62 % | 396.9 px | 0.12 | 1.02 | 465 |
| stroke 28 | 63 % → 58 % | 248.4 px | 0.12 | 0.92 | 813 |

Numbers say: wet paint spreads well beyond the stroke.

## Oil · Henry Ward · HW #03 navy contours over wet band — own sheet
own sheet 600 × 600 · Gouache 1.00 + turpentine 35 % · 84 px · 47.2 s

![Oil · Henry Ward · HW #03 navy contours over wet band — own sheet](Oil-Henry-Ward-HW-03-navy-contours-over-wet-band-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 50 % → 44 % | 87.6 px | 0.65 | 0.89 | 1786 |
| stroke 2 | 61 % → 51 % | 145.4 px | 0.61 | 0.83 | 2101 |
| stroke 3 | 69 % → 52 % | 202.1 px | 0.58 | 0.75 | 2779 |
| stroke 4 | 71 % → 59 % | 218.5 px | 0.55 | 0.83 | 3000 |
| stroke 5 | 71 % → 60 % | 217.2 px | 0.56 | 0.85 | 2868 |
| stroke 6 | 71 % → 48 % | 222.3 px | 0.53 | 0.67 | 3389 |
| stroke 7 | 74 % → 36 % | 218.0 px | 0.53 | 0.48 | 2796 |
| stroke 8 | 95 % → 29 % | 218.1 px | 0.58 | 0.30 | 3282 |
| stroke 9 | 100 % → 19 % | 170.3 px | 0.66 | 0.19 | 2648 |
| stroke 10 | 9 % → 56 % | 64.0 px | 0.56 | 5.98 | 533 |
| stroke 11 | 16 % → 63 % | 151.7 px | 0.56 | 3.92 | 338 |
| stroke 12 | 25 % → 62 % | 241.0 px | 0.53 | 2.43 | 300 |
| stroke 13 | 26 % → 50 % | 221.6 px | 0.53 | 1.93 | 475 |
| stroke 14 | 27 % → 59 % | 233.0 px | 0.62 | 2.20 | 241 |
| stroke 15 | 37 % → 58 % | 298.6 px | 0.59 | 1.57 | 320 |
| stroke 16 | 45 % → 46 % | 132.4 px | 0.55 | 1.03 | 1411 |
| stroke 17 | 49 % → 48 % | 177.1 px | 0.57 | 0.97 | 1177 |

Numbers say: wet paint spreads well beyond the stroke.

## Oil · Henry Ward · HW #01 peach cloud and legs over teal — own sheet
own sheet 600 × 600 · Gouache 1.00 + turpentine 35 % · 84 px · 55.7 s

![Oil · Henry Ward · HW #01 peach cloud and legs over teal — own sheet](Oil-Henry-Ward-HW-01-peach-cloud-and-legs-over-teal-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 50 % → 52 % | 88.9 px | 0.56 | 1.02 | 3251 |
| stroke 2 | 62 % → 59 % | 146.9 px | 0.56 | 0.95 | 2794 |
| stroke 3 | 69 % → 61 % | 203.4 px | 0.57 | 0.88 | 2715 |
| stroke 4 | 71 % → 69 % | 220.1 px | 0.57 | 0.97 | 3947 |
| stroke 5 | 70 % → 60 % | 218.3 px | 0.56 | 0.86 | 4213 |
| stroke 6 | 71 % → 57 % | 218.3 px | 0.48 | 0.81 | 3342 |
| stroke 7 | 77 % → 52 % | 222.3 px | 0.37 | 0.68 | 2903 |
| stroke 8 | 95 % → 47 % | 219.1 px | 0.30 | 0.50 | 4725 |
| stroke 9 | 100 % → 43 % | 170.3 px | 0.16 | 0.43 | 3803 |
| stroke 10 | 16 % → 57 % | 61.5 px | 0.56 | 3.58 | 667 |
| stroke 11 | 25 % → 60 % | 109.2 px | 0.57 | 2.45 | 504 |
| stroke 12 | 30 % → 63 % | 157.9 px | 0.57 | 2.08 | 585 |
| stroke 13 | 38 % → 69 % | 192.3 px | 0.57 | 1.83 | 501 |
| stroke 14 | 52 % → 58 % | 195.6 px | 0.56 | 1.12 | 743 |
| stroke 15 | 42 % → 61 % | 207.0 px | 0.57 | 1.46 | 495 |
| stroke 16 | 41 % → 69 % | 218.5 px | 0.57 | 1.67 | 1129 |
| stroke 17 | 35 % → 59 % | 193.7 px | 0.46 | 1.67 | 878 |
| stroke 18 | 41 % → 63 % | 348.3 px | 0.46 | 1.52 | 458 |
| stroke 19 | 53 % → 78 % | 433.8 px | 0.46 | 1.48 | 428 |
| stroke 20 | 51 % → 76 % | 394.3 px | 0.46 | 1.50 | 427 |
| stroke 21 | 47 % → 64 % | 385.6 px | 0.47 | 1.37 | 368 |
| stroke 22 | 46 % → 57 % | 317.1 px | 0.46 | 1.24 | 381 |
| stroke 23 | 45 % → 56 % | 161.2 px | 0.30 | 1.24 | 248 |
| stroke 24 | 51 % → 50 % | 189.5 px | 0.27 | 0.98 | 363 |

Numbers say: wet paint spreads well beyond the stroke.

## Oil · Henry Ward · HW #05 rust, pink, green-black — own sheet
own sheet 600 × 600 · Gouache 1.00 + turpentine 35 % · 84 px · 52.9 s

![Oil · Henry Ward · HW #05 rust, pink, green-black — own sheet](Oil-Henry-Ward-HW-05-rust-pink-green-black-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 49 % → 58 % | 83.9 px | 0.58 | 1.18 | 1864 |
| stroke 2 | 63 % → 64 % | 148.0 px | 0.51 | 1.03 | 2361 |
| stroke 3 | 69 % → 64 % | 207.2 px | 0.42 | 0.93 | 4031 |
| stroke 4 | 71 % → 71 % | 218.5 px | 0.38 | 1.01 | 3693 |
| stroke 5 | 71 % → 70 % | 220.5 px | 0.40 | 0.99 | 2906 |
| stroke 6 | 70 % → 68 % | 216.1 px | 0.42 | 0.97 | 2597 |
| stroke 7 | 74 % → 60 % | 217.7 px | 0.47 | 0.81 | 4425 |
| stroke 8 | 93 % → 58 % | 217.2 px | 0.58 | 0.62 | 3324 |
| stroke 9 | 100 % → 54 % | 167.6 px | 0.72 | 0.54 | 2162 |
| stroke 10 | 17 % → 61 % | 60.7 px | 0.57 | 3.60 | 493 |
| stroke 11 | 26 % → 66 % | 108.2 px | 0.46 | 2.57 | 854 |
| stroke 12 | 31 % → 66 % | 163.8 px | 0.42 | 2.11 | 911 |
| stroke 13 | 37 % → 68 % | 195.9 px | 0.39 | 1.85 | 781 |
| stroke 14 | 52 % → 64 % | 234.2 px | 0.52 | 1.23 | 345 |
| stroke 15 | 45 % → 67 % | 226.1 px | 0.44 | 1.48 | 374 |
| stroke 16 | 39 % → 68 % | 265.5 px | 0.39 | 1.74 | 304 |
| stroke 17 | 44 % → 71 % | 225.7 px | 0.38 | 1.62 | 901 |
| stroke 18 | 46 % → 71 % | 247.2 px | 0.40 | 1.55 | 865 |
| stroke 19 | 41 % → 67 % | 204.4 px | 0.42 | 1.66 | 662 |
| stroke 20 | 49 % → 68 % | 362.8 px | 0.43 | 1.40 | 224 |
| stroke 21 | 49 % → 68 % | 362.2 px | 0.45 | 1.38 | 348 |
| stroke 22 | 51 % → 70 % | 424.8 px | 0.45 | 1.38 | 276 |
| stroke 23 | 44 % → 62 % | 252.9 px | 0.43 | 1.41 | 545 |
| stroke 24 | 47 % → 56 % | 224.3 px | 0.54 | 1.19 | 432 |
| stroke 25 | 59 % → 58 % | 208.1 px | 0.64 | 0.99 | 417 |

Numbers say: wet paint spreads well beyond the stroke.

## Oil · Henry Ward · HW #07 blue L and zigzag on lilac — own sheet
own sheet 600 × 600 · Gouache 1.00 + turpentine 20 % · 90 px · 45.7 s

![Oil · Henry Ward · HW #07 blue L and zigzag on lilac — own sheet](Oil-Henry-Ward-HW-07-blue-L-and-zigzag-on-lilac-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 45 % → 30 % | 81.4 px | 0.27 | 0.67 | 2563 |
| stroke 2 | 58 % → 40 % | 140.1 px | 0.35 | 0.69 | 1901 |
| stroke 3 | 67 % → 67 % | 204.7 px | 0.37 | 1.00 | 2090 |
| stroke 4 | 70 % → 52 % | 231.4 px | 0.34 | 0.74 | 2243 |
| stroke 5 | 69 % → 61 % | 227.8 px | 0.33 | 0.88 | 1900 |
| stroke 6 | 69 % → 62 % | 227.3 px | 0.31 | 0.91 | 2217 |
| stroke 7 | 75 % → 57 % | 228.0 px | 0.26 | 0.76 | 2478 |
| stroke 8 | 96 % → 52 % | 229.1 px | 0.19 | 0.54 | 2247 |
| stroke 9 | 100 % → 55 % | 182.6 px | 0.16 | 0.55 | 1659 |
| stroke 10 | 13 % → 34 % | 36.8 px | 0.29 | 2.54 | 493 |
| stroke 11 | 23 % → 42 % | 76.7 px | 0.37 | 1.87 | 653 |
| stroke 12 | 22 % → 43 % | 78.3 px | 0.37 | 1.99 | 424 |
| stroke 13 | 23 % → 47 % | 91.3 px | 0.37 | 2.01 | 506 |
| stroke 14 | 29 % → 50 % | 130.4 px | 0.34 | 1.73 | 541 |
| stroke 15 | 31 % → 56 % | 154.2 px | 0.33 | 1.80 | 411 |
| stroke 16 | 36 % → 62 % | 161.8 px | 0.33 | 1.71 | 778 |
| stroke 17 | 34 % → 63 % | 170.5 px | 0.31 | 1.86 | 595 |
| stroke 18 | 43 % → 61 % | 189.0 px | 0.29 | 1.43 | 859 |
| stroke 19 | 47 % → 57 % | 190.1 px | 0.26 | 1.21 | 542 |
| stroke 20 | 52 % → 56 % | 202.4 px | 0.22 | 1.06 | 688 |
| stroke 21 | 62 % → 52 % | 203.7 px | 0.19 | 0.84 | 608 |
| stroke 22 | 71 % → 51 % | 220.2 px | 0.17 | 0.73 | 787 |
| stroke 23 | 62 % → 54 % | 343.6 px | 0.29 | 0.87 | 347 |
| stroke 24 | 73 % → 56 % | 482.9 px | 0.23 | 0.77 | 330 |
| stroke 25 | 68 % → 53 % | 253.8 px | 0.32 | 0.79 | 895 |
| stroke 26 | 68 % → 61 % | 734.8 px | 0.29 | 0.90 | 222 |
| stroke 27 | 75 % → 64 % | 718.4 px | 0.28 | 0.85 | 254 |
| stroke 28 | 75 % → 63 % | 566.1 px | 0.28 | 0.84 | 404 |
| stroke 29 | 75 % → 63 % | 656.7 px | 0.28 | 0.85 | 307 |
| stroke 30 | 79 % → 65 % | 610.9 px | 0.28 | 0.83 | 381 |
| stroke 31 | 79 % → 65 % | 1163.8 px | 0.26 | 0.83 | 165 |

Numbers say: wet paint spreads well beyond the stroke.

## Oil · Henry Ward · HW #08 crown and dark oval — own sheet
own sheet 600 × 600 · Gouache 1.00 + turpentine 35 % · 84 px · 32.9 s

![Oil · Henry Ward · HW #08 crown and dark oval — own sheet](Oil-Henry-Ward-HW-08-crown-and-dark-oval-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 50 % → 0 % | 88.4 px | 0.00 | 0.00 | 1465 |
| stroke 2 | 61 % → 0 % | 142.2 px | 0.00 | 0.00 | 1663 |
| stroke 3 | 70 % → 3 % | 206.2 px | 0.13 | 0.04 | 2204 |
| stroke 4 | 72 % → 7 % | 223.4 px | 0.11 | 0.10 | 2109 |
| stroke 5 | 71 % → 12 % | 220.0 px | 0.11 | 0.18 | 2480 |
| stroke 6 | 70 % → 12 % | 219.6 px | 0.11 | 0.18 | 2035 |
| stroke 7 | 74 % → 13 % | 217.8 px | 0.11 | 0.18 | 1924 |
| stroke 8 | 94 % → 13 % | 217.4 px | 0.11 | 0.14 | 2334 |
| stroke 9 | 100 % → 8 % | 166.8 px | 0.12 | 0.08 | 1987 |
| stroke 10 | 20 % → 0 % | 80.6 px | 0.00 | 0.00 | 748 |
| stroke 11 | 30 % → 1 % | 155.4 px | 0.11 | 0.03 | 714 |
| stroke 12 | 36 % → 3 % | 227.4 px | 0.13 | 0.09 | 602 |
| stroke 13 | 34 % → 9 % | 102.8 px | 0.11 | 0.26 | 987 |
| stroke 14 | 42 % → 12 % | 306.3 px | 0.11 | 0.29 | 558 |
| stroke 15 | 43 % → 12 % | 355.2 px | 0.11 | 0.28 | 531 |
| stroke 16 | 42 % → 12 % | 343.2 px | 0.11 | 0.28 | 416 |
| stroke 17 | 45 % → 14 % | 289.4 px | 0.11 | 0.30 | 459 |
| stroke 18 | 11 % → 13 % | 97.1 px | 0.11 | 1.17 | 410 |
| stroke 19 | 22 % → 12 % | 190.4 px | 0.11 | 0.56 | 408 |
| stroke 20 | 28 % → 13 % | 208.9 px | 0.11 | 0.47 | 478 |

## Oil · Henry Ward · HW #10 green block over maroon — own sheet
own sheet 600 × 600 · Gouache 1.00 + turpentine 35 % · 84 px · 45.3 s

![Oil · Henry Ward · HW #10 green block over maroon — own sheet](Oil-Henry-Ward-HW-10-green-block-over-maroon-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 50 % → 44 % | 86.7 px | 0.20 | 0.89 | 1435 |
| stroke 2 | 61 % → 49 % | 141.4 px | 0.30 | 0.79 | 1640 |
| stroke 3 | 70 % → 53 % | 209.0 px | 0.42 | 0.76 | 2525 |
| stroke 4 | 71 % → 58 % | 218.2 px | 0.50 | 0.82 | 2444 |
| stroke 5 | 70 % → 59 % | 215.7 px | 0.59 | 0.84 | 2341 |
| stroke 6 | 71 % → 55 % | 218.8 px | 0.62 | 0.78 | 2207 |
| stroke 7 | 75 % → 46 % | 219.1 px | 0.64 | 0.61 | 2116 |
| stroke 8 | 94 % → 40 % | 217.8 px | 0.62 | 0.43 | 3066 |
| stroke 9 | 100 % → 30 % | 172.0 px | 0.55 | 0.30 | 2078 |
| stroke 10 | 16 % → 49 % | 91.0 px | 0.24 | 3.09 | 296 |
| stroke 11 | 24 % → 51 % | 161.2 px | 0.35 | 2.08 | 439 |
| stroke 12 | 28 % → 57 % | 242.2 px | 0.46 | 2.03 | 421 |
| stroke 13 | 42 % → 52 % | 277.0 px | 0.31 | 1.24 | 370 |
| stroke 14 | 36 % → 56 % | 293.9 px | 0.39 | 1.53 | 510 |
| stroke 15 | 31 % → 57 % | 277.1 px | 0.44 | 1.87 | 505 |
| stroke 16 | 30 % → 57 % | 210.5 px | 0.48 | 1.91 | 844 |
| stroke 17 | 34 % → 59 % | 224.4 px | 0.54 | 1.75 | 751 |
| stroke 18 | 34 % → 58 % | 239.1 px | 0.60 | 1.69 | 955 |
| stroke 19 | 37 % → 55 % | 265.3 px | 0.63 | 1.49 | 616 |
| stroke 20 | 37 % → 51 % | 261.7 px | 0.64 | 1.38 | 799 |
| stroke 21 | 43 % → 48 % | 158.3 px | 0.51 | 1.12 | 1242 |
| stroke 22 | 41 % → 47 % | 334.1 px | 0.65 | 1.13 | 517 |
| stroke 23 | 45 % → 43 % | 281.5 px | 0.63 | 0.95 | 560 |
| stroke 24 | 50 % → 37 % | 279.2 px | 0.60 | 0.73 | 474 |

Numbers say: wet paint spreads well beyond the stroke.

## Oil · Henry Ward · HW #11 cream mass and purple balls — own sheet
own sheet 600 × 600 · Gouache 1.00 + turpentine 35 % · 84 px · 51.7 s

![Oil · Henry Ward · HW #11 cream mass and purple balls — own sheet](Oil-Henry-Ward-HW-11-cream-mass-and-purple-balls-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 49 % → 47 % | 83.5 px | 0.11 | 0.96 | 1915 |
| stroke 2 | 62 % → 51 % | 147.7 px | 0.11 | 0.81 | 2897 |
| stroke 3 | 70 % → 52 % | 210.2 px | 0.11 | 0.74 | 2861 |
| stroke 4 | 71 % → 58 % | 221.0 px | 0.12 | 0.82 | 3124 |
| stroke 5 | 71 % → 59 % | 217.6 px | 0.21 | 0.83 | 3020 |
| stroke 6 | 70 % → 59 % | 216.5 px | 0.30 | 0.85 | 4078 |
| stroke 7 | 76 % → 50 % | 221.8 px | 0.35 | 0.66 | 2490 |
| stroke 8 | 94 % → 49 % | 219.3 px | 0.42 | 0.52 | 2245 |
| stroke 9 | 100 % → 47 % | 171.2 px | 0.55 | 0.47 | 2582 |
| stroke 10 | 15 % → 50 % | 63.1 px | 0.11 | 3.38 | 465 |
| stroke 11 | 20 % → 51 % | 106.3 px | 0.11 | 2.54 | 658 |
| stroke 12 | 26 % → 52 % | 144.5 px | 0.11 | 2.02 | 675 |
| stroke 13 | 31 % → 57 % | 194.5 px | 0.11 | 1.82 | 481 |
| stroke 14 | 34 % → 58 % | 227.2 px | 0.14 | 1.71 | 608 |
| stroke 15 | 34 % → 58 % | 204.3 px | 0.19 | 1.73 | 531 |
| stroke 16 | 34 % → 60 % | 227.9 px | 0.26 | 1.76 | 489 |
| stroke 17 | 34 % → 59 % | 214.0 px | 0.30 | 1.76 | 395 |
| stroke 18 | 50 % → 50 % | 258.4 px | 0.11 | 1.00 | 504 |
| stroke 19 | 52 % → 51 % | 304.9 px | 0.11 | 1.00 | 532 |
| stroke 20 | 52 % → 52 % | 367.4 px | 0.11 | 1.00 | 685 |
| stroke 21 | 58 % → 58 % | 452.7 px | 0.11 | 1.01 | 700 |
| stroke 22 | 52 % → 58 % | 365.7 px | 0.16 | 1.11 | 504 |
| stroke 23 | 42 % → 59 % | 280.4 px | 0.25 | 1.41 | 446 |
| stroke 24 | 38 % → 60 % | 266.1 px | 0.28 | 1.58 | 419 |
| stroke 25 | 45 % → 58 % | 128.2 px | 0.34 | 1.29 | 863 |
| stroke 26 | 58 % → 68 % | 171.4 px | 0.35 | 1.18 | 863 |
| stroke 27 | 61 % → 60 % | 157.1 px | 0.34 | 0.98 | 1184 |

Numbers say: wet paint spreads well beyond the stroke.

## Oil · Henry Ward · HW #13 blue scrub under red — own sheet
own sheet 600 × 600 · Gouache 1.00 + turpentine 35 % · 84 px · 51.7 s

![Oil · Henry Ward · HW #13 blue scrub under red — own sheet](Oil-Henry-Ward-HW-13-blue-scrub-under-red-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 49 % → 13 % | 83.9 px | 0.06 | 0.28 | 2031 |
| stroke 2 | 61 % → 29 % | 142.5 px | 0.06 | 0.47 | 2147 |
| stroke 3 | 69 % → 38 % | 204.0 px | 0.07 | 0.55 | 2491 |
| stroke 4 | 71 % → 51 % | 220.1 px | 0.07 | 0.71 | 3140 |
| stroke 5 | 70 % → 66 % | 216.7 px | 0.07 | 0.94 | 3628 |
| stroke 6 | 71 % → 74 % | 220.3 px | 0.07 | 1.05 | 2207 |
| stroke 7 | 75 % → 72 % | 216.3 px | 0.07 | 0.97 | 1719 |
| stroke 8 | 95 % → 72 % | 222.8 px | 0.07 | 0.76 | 2598 |
| stroke 9 | 100 % → 73 % | 165.9 px | 0.07 | 0.73 | 2145 |
| stroke 10 | 18 % → 18 % | 64.9 px | 0.05 | 1.03 | 464 |
| stroke 11 | 24 % → 35 % | 143.8 px | 0.06 | 1.47 | 480 |
| stroke 12 | 28 % → 38 % | 175.3 px | 0.07 | 1.32 | 572 |
| stroke 13 | 13 % → 42 % | 62.1 px | 0.07 | 3.24 | 721 |
| stroke 14 | 23 % → 55 % | 123.4 px | 0.07 | 2.37 | 608 |
| stroke 15 | 33 % → 65 % | 173.0 px | 0.07 | 1.99 | 598 |
| stroke 16 | 38 % → 73 % | 197.9 px | 0.07 | 1.90 | 643 |
| stroke 17 | 42 % → 74 % | 218.9 px | 0.07 | 1.78 | 657 |
| stroke 18 | 43 % → 72 % | 195.3 px | 0.07 | 1.67 | 770 |
| stroke 19 | 49 % → 72 % | 203.5 px | 0.07 | 1.47 | 712 |
| stroke 20 | 59 % → 72 % | 219.3 px | 0.07 | 1.23 | 519 |
| stroke 21 | 70 % → 73 % | 213.1 px | 0.07 | 1.04 | 575 |
| stroke 22 | 48 % → 49 % | 263.1 px | 0.07 | 1.01 | 619 |
| stroke 23 | 62 % → 62 % | 317.9 px | 0.07 | 1.00 | 852 |
| stroke 24 | 67 % → 67 % | 382.3 px | 0.07 | 1.00 | 899 |
| stroke 25 | 74 % → 74 % | 363.3 px | 0.07 | 1.01 | 903 |
| stroke 26 | 73 % → 74 % | 376.5 px | 0.07 | 1.01 | 699 |
| stroke 27 | 71 % → 72 % | 344.9 px | 0.07 | 1.01 | 521 |
| stroke 28 | 72 % → 72 % | 296.9 px | 0.07 | 1.01 | 753 |
| stroke 29 | 74 % → 73 % | 287.7 px | 0.07 | 0.99 | 606 |

Numbers say: wet paint spreads well beyond the stroke.

## Oil · Henry Ward · HW #14 olive totem on dark — own sheet
own sheet 600 × 600 · Gouache 1.00 + turpentine 35 % · 84 px · 49.7 s

![Oil · Henry Ward · HW #14 olive totem on dark — own sheet](Oil-Henry-Ward-HW-14-olive-totem-on-dark-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 47 % → 45 % | 78.9 px | 0.39 | 0.97 | 1706 |
| stroke 2 | 62 % → 53 % | 146.1 px | 0.41 | 0.85 | 2577 |
| stroke 3 | 70 % → 52 % | 208.2 px | 0.41 | 0.74 | 2905 |
| stroke 4 | 71 % → 59 % | 219.3 px | 0.41 | 0.82 | 3316 |
| stroke 5 | 71 % → 64 % | 217.3 px | 0.41 | 0.90 | 3009 |
| stroke 6 | 71 % → 60 % | 216.7 px | 0.41 | 0.85 | 2472 |
| stroke 7 | 74 % → 50 % | 219.2 px | 0.40 | 0.68 | 2660 |
| stroke 8 | 94 % → 50 % | 217.9 px | 0.39 | 0.53 | 3011 |
| stroke 9 | 100 % → 47 % | 172.0 px | 0.39 | 0.47 | 2338 |
| stroke 10 | 20 % → 74 % | 85.2 px | 0.40 | 3.67 | 775 |
| stroke 11 | 33 % → 77 % | 139.9 px | 0.40 | 2.36 | 816 |
| stroke 12 | 48 % → 69 % | 200.7 px | 0.40 | 1.43 | 655 |
| stroke 13 | 40 % → 52 % | 198.2 px | 0.41 | 1.30 | 609 |
| stroke 14 | 47 % → 56 % | 268.0 px | 0.41 | 1.20 | 660 |
| stroke 15 | 52 % → 61 % | 282.0 px | 0.41 | 1.17 | 883 |
| stroke 16 | 42 % → 54 % | 229.4 px | 0.41 | 1.29 | 689 |
| stroke 17 | 40 % → 48 % | 202.4 px | 0.40 | 1.22 | 730 |
| stroke 18 | 45 % → 50 % | 212.8 px | 0.39 | 1.09 | 467 |
| stroke 19 | 56 % → 54 % | 299.7 px | 0.41 | 0.97 | 457 |
| stroke 20 | 54 % → 54 % | 330.7 px | 0.41 | 1.01 | 545 |
| stroke 21 | 57 % → 58 % | 375.3 px | 0.41 | 1.02 | 606 |
| stroke 22 | 61 % → 62 % | 410.0 px | 0.41 | 1.02 | 442 |
| stroke 23 | 64 % → 63 % | 414.1 px | 0.40 | 0.98 | 410 |
| stroke 24 | 61 % → 60 % | 416.4 px | 0.41 | 0.98 | 300 |
| stroke 25 | 56 % → 55 % | 369.5 px | 0.41 | 0.98 | 362 |
| stroke 26 | 51 % → 49 % | 313.3 px | 0.40 | 0.96 | 467 |
| stroke 27 | 51 % → 49 % | 249.3 px | 0.39 | 0.96 | 467 |

Numbers say: wet paint spreads well beyond the stroke.

## Surface test · Surface test · smooth panel — own sheet
own sheet 600 × 600 · Gouache 1.00 + turpentine 40 % · 70 px · 13.0 s

![Surface test · Surface test · smooth panel — own sheet](Surface-test-Surface-test-smooth-panel-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 15 % → 44 % | 42.2 px | 0.35 | 2.96 | 401 |
| stroke 2 | 21 % → 44 % | 66.5 px | 0.33 | 2.10 | 398 |
| stroke 3 | 21 % → 36 % | 65.7 px | 0.30 | 1.76 | 560 |
| stroke 4 | 26 % → 26 % | 59.1 px | 0.28 | 1.02 | 552 |
| stroke 5 | 21 % → 42 % | 55.0 px | 0.56 | 1.95 | 572 |
| stroke 6 | 32 % → 54 % | 106.9 px | 0.39 | 1.66 | 450 |
| stroke 7 | 31 % → 44 % | 102.8 px | 0.34 | 1.40 | 405 |
| stroke 8 | 41 % → 42 % | 135.9 px | 0.15 | 1.02 | 616 |
| stroke 9 | 45 % → 25 % | 123.5 px | 0.17 | 0.55 | 180 |

Numbers say: wet paint spreads well beyond the stroke.

## Surface test · Surface test · paper — own sheet
own sheet 600 × 600 · Gouache 1.00 + turpentine 40 % · 70 px · 13.6 s

![Surface test · Surface test · paper — own sheet](Surface-test-Surface-test-paper-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 14 % → 43 % | 40.1 px | 0.35 | 3.03 | 413 |
| stroke 2 | 20 % → 42 % | 64.9 px | 0.33 | 2.07 | 419 |
| stroke 3 | 20 % → 35 % | 64.0 px | 0.30 | 1.75 | 445 |
| stroke 4 | 25 % → 26 % | 58.1 px | 0.29 | 1.02 | 442 |
| stroke 5 | 21 % → 42 % | 54.9 px | 0.55 | 1.95 | 479 |
| stroke 6 | 32 % → 53 % | 106.1 px | 0.39 | 1.66 | 419 |
| stroke 7 | 30 % → 42 % | 99.5 px | 0.34 | 1.38 | 387 |
| stroke 8 | 41 % → 40 % | 135.1 px | 0.14 | 0.97 | 567 |
| stroke 9 | 45 % → 23 % | 123.3 px | 0.15 | 0.51 | 180 |

Numbers say: wet paint spreads well beyond the stroke.

## Surface test · Surface test · fine canvas — own sheet
own sheet 600 × 600 · Gouache 1.00 + turpentine 40 % · 70 px · 14.1 s

![Surface test · Surface test · fine canvas — own sheet](Surface-test-Surface-test-fine-canvas-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 15 % → 44 % | 41.9 px | 0.35 | 2.97 | 535 |
| stroke 2 | 21 % → 44 % | 66.6 px | 0.33 | 2.09 | 600 |
| stroke 3 | 21 % → 36 % | 65.8 px | 0.30 | 1.76 | 694 |
| stroke 4 | 26 % → 26 % | 59.6 px | 0.29 | 1.02 | 545 |
| stroke 5 | 21 % → 42 % | 55.0 px | 0.56 | 1.96 | 715 |
| stroke 6 | 32 % → 54 % | 107.0 px | 0.39 | 1.66 | 492 |
| stroke 7 | 31 % → 43 % | 102.6 px | 0.34 | 1.40 | 405 |
| stroke 8 | 41 % → 42 % | 135.9 px | 0.15 | 1.01 | 595 |
| stroke 9 | 45 % → 25 % | 123.6 px | 0.17 | 0.55 | 167 |

Numbers say: wet paint spreads well beyond the stroke.

## Surface test · Surface test · coarse linen — own sheet
own sheet 600 × 600 · Gouache 1.00 + turpentine 40 % · 70 px · 13.3 s

![Surface test · Surface test · coarse linen — own sheet](Surface-test-Surface-test-coarse-linen-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 15 % → 44 % | 41.2 px | 0.35 | 3.01 | 402 |
| stroke 2 | 21 % → 43 % | 66.3 px | 0.33 | 2.09 | 439 |
| stroke 3 | 21 % → 36 % | 65.4 px | 0.30 | 1.76 | 456 |
| stroke 4 | 26 % → 26 % | 59.2 px | 0.29 | 1.02 | 452 |
| stroke 5 | 21 % → 42 % | 55.1 px | 0.56 | 1.95 | 485 |
| stroke 6 | 32 % → 54 % | 106.9 px | 0.39 | 1.66 | 458 |
| stroke 7 | 31 % → 43 % | 102.0 px | 0.34 | 1.39 | 389 |
| stroke 8 | 41 % → 41 % | 135.9 px | 0.15 | 1.01 | 568 |
| stroke 9 | 45 % → 24 % | 123.5 px | 0.16 | 0.54 | 173 |

Numbers say: wet paint spreads well beyond the stroke.

## Watercolour · #16 Shrigley strokes — own sheet
own sheet 600 × 600 · Watercolour 1.00 + water 30 % · 46 px · 12.4 s

![Watercolour · #16 Shrigley strokes — own sheet](Watercolour-16-Shrigley-strokes-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| s0 | 7 % → 30 % | 33.9 px | 0.40 | 4.10 | 90 |
| s1 | 6 % → 39 % | 11.8 px | 0.54 | 6.64 | 74 |
| s2 | 12 % → 24 % | 60.5 px | 0.31 | 2.02 | 69 |
| s3 | 11 % → 25 % | 32.5 px | 0.49 | 2.34 | 93 |
| s4 | 15 % → 36 % | 46.0 px | 0.50 | 2.35 | 100 |
| s5 | 21 % → 34 % | 47.5 px | 0.53 | 1.63 | 95 |
| s6 | 20 % → 28 % | 61.8 px | 0.43 | 1.34 | 97 |
| s7 | 29 % → 44 % | 44.8 px | 0.54 | 1.53 | 81 |
| s8 | 24 % → 31 % | 109.8 px | 0.41 | 1.27 | 83 |

Numbers say: wet paint spreads well beyond the stroke.

## Watercolour · #29 Shrigley asterisk — own sheet
own sheet 600 × 600 · Watercolour 1.00 + water 50 % · 70 px · 17.9 s

![Watercolour · #29 Shrigley asterisk — own sheet](Watercolour-29-Shrigley-asterisk-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 28 % → 63 % | 98.0 px | 0.65 | 2.25 | 566 |
| stroke 2 | 24 % → 24 % | 170.8 px | 0.65 | 1.00 | 426 |
| stroke 3 | 50 % → 63 % | 179.5 px | 0.66 | 1.24 | 522 |
| stroke 4 | 42 % → 42 % | 299.7 px | 0.65 | 1.00 | 531 |

Numbers say: wet paint spreads well beyond the stroke.

## Watercolour · #33 Red band, pink flames — own sheet
own sheet 600 × 600 · Watercolour 1.00 + water 60 % · 90 px · 23.4 s

![Watercolour · #33 Red band, pink flames — own sheet](Watercolour-33-Red-band-pink-flames-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 25 % → 62 % | 101.5 px | 0.36 | 2.50 | 646 |
| stroke 2 | 29 % → 65 % | 180.0 px | 0.30 | 2.28 | 185 |
| stroke 3 | 32 % → 62 % | 250.7 px | 0.30 | 1.93 | 241 |
| stroke 4 | 37 % → 66 % | 300.3 px | 0.29 | 1.81 | 247 |
| stroke 5 | 36 % → 68 % | 341.7 px | 0.27 | 1.89 | 176 |
| stroke 6 | 38 % → 64 % | 301.4 px | 0.26 | 1.68 | 220 |
| stroke 7 | 47 % → 65 % | 262.8 px | 0.24 | 1.40 | 221 |

Numbers say: wet paint spreads well beyond the stroke.

## Watercolour · #35 Red band with runs — own sheet
own sheet 600 × 600 · Watercolour 1.00 + water 75 % · 80 px · 17.4 s

![Watercolour · #35 Red band with runs — own sheet](Watercolour-35-Red-band-with-runs-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 38 % → 48 % | 147.8 px | 0.21 | 1.27 | 603 |

## Watercolour · #40 Olive and sepia blooms — own sheet
own sheet 600 × 600 · Watercolour 1.00 + water 55 % · 90 px · 19.6 s

![Watercolour · #40 Olive and sepia blooms — own sheet](Watercolour-40-Olive-and-sepia-blooms-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 27 % → 58 % | 94.2 px | 0.21 | 2.15 | 1075 |
| stroke 2 | 47 % → 62 % | 150.6 px | 0.22 | 1.31 | 868 |

Numbers say: wet paint spreads well beyond the stroke.

## Watercolour · #46 Lips on wet paper — own sheet
own sheet 600 × 600 · Watercolour 1.00 + water 65 % · 50 px · 13.4 s

![Watercolour · #46 Lips on wet paper — own sheet](Watercolour-46-Lips-on-wet-paper-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 13 % → 32 % | 56.0 px | 0.53 | 2.35 | 140 |
| stroke 2 | 15 % → 32 % | 63.8 px | 0.52 | 2.22 | 148 |

Numbers say: wet paint spreads well beyond the stroke.

