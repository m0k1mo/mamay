![All brushes](contact.png)

# Brush Lab — 150 brushes · Nov 4, 2026 at 9:13 AM

Every sheet: 1500 × 600, ten strokes in a 5 × 2 grid — 1. light line · 2. heavy line · 3. pressure swell · 4. fast wave · 5. slow wave · 6. spiral · 7. loop · 8. tilted · 9. over the wet one · 10. long, no reload (cell 8 holds «tilted» and «over the wet one» crossed). The CPU reference of Mamay's paint engine; the wet layer settles 20 s at the end.

Columns: **covered** = share of the cell with paint right after the stroke → after settling; **width** = painted area of the stroke ÷ its length (px); **dark** = mean darkness of the painted pixels above the paper's own grain (0 = paper, 1 = black); **spread** = how far wet paint went beyond the stroke (1.0 = stayed); **ms** = the stroke on the CPU; long stroke: paint in each quarter of its length (it should run out: wet → streaks → dry tail).

## Ink Line
Ink · 12 px · 27.3 s

![Ink Line](Ink-Line.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 1 % → 4 % | 4.3 px | 0.55 | 2.44 | 60 |
| heavy line | 5 % → 6 % | 15.7 px | 0.68 | 1.13 | 71 |
| pressure swell | 3 % → 4 % | 11.3 px | 0.64 | 1.40 | 45 |
| fast wave | 10 % → 11 % | 11.2 px | 0.59 | 1.11 | 123 |
| slow wave | 8 % → 10 % | 9.6 px | 0.57 | 1.16 | 123 |
| spiral | 14 % → 15 % | 8.9 px | 0.50 | 1.07 | 216 |
| loop | 8 % → 9 % | 10.6 px | 0.61 | 1.16 | 110 |
| tilted | 5 % → 5 % | 14.4 px | 0.65 | 1.05 | 60 |
| over the wet one | 10 % → 11 % | 12.5 px | 0.65 | 1.15 | 53 |
| long, no reload | 18 % → 17 % | 8.1 px | 0.47 | 0.96 | 311 | quarters: 0.22 → 0.09 → 0.04 → 0.02

Numbers say: light vs heavy: width 4.3 → 15.7 px, dark 0.55 → 0.68; wet paint spreads well beyond the stroke.

## Dense Ink
Ink · 14 px · 28.7 s

![Dense Ink](Dense-Ink.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 5 % → 7 % | 15.2 px | 0.72 | 1.26 | 71 |
| heavy line | 7 % → 7 % | 19.1 px | 0.73 | 1.09 | 96 |
| pressure swell | 5 % → 6 % | 17.9 px | 0.72 | 1.17 | 66 |
| fast wave | 13 % → 13 % | 15.3 px | 0.69 | 1.01 | 133 |
| slow wave | 12 % → 12 % | 13.6 px | 0.67 | 1.04 | 152 |
| spiral | 18 % → 15 % | 12.2 px | 0.65 | 0.80 | 248 |
| loop | 11 % → 12 % | 14.8 px | 0.69 | 1.08 | 130 |
| tilted | 5 % → 6 % | 14.6 px | 0.72 | 1.07 | 63 |
| over the wet one | 12 % → 13 % | 17.7 px | 0.72 | 1.11 | 58 |
| long, no reload | 23 % → 15 % | 10.1 px | 0.64 | 0.66 | 344 | quarters: 0.30 → 0.12 → 0.04 → 0.02

Numbers say: light vs heavy: width 15.2 → 19.1 px, dark 0.72 → 0.73.

## Transparent Wash
Watercolor · 22 px · 29.9 s

![Transparent Wash](Transparent-Wash.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 2 % → 5 % | 6.9 px | 0.27 | 2.25 | 97 |
| heavy line | 7 % → 9 % | 20.4 px | 0.27 | 1.22 | 81 |
| pressure swell | 4 % → 6 % | 15.2 px | 0.28 | 1.54 | 64 |
| fast wave | 14 % → 16 % | 16.1 px | 0.20 | 1.17 | 119 |
| slow wave | 12 % → 15 % | 13.7 px | 0.21 | 1.28 | 171 |
| spiral | 18 % → 22 % | 11.9 px | 0.16 | 1.23 | 192 |
| loop | 11 % → 13 % | 14.5 px | 0.22 | 1.20 | 100 |
| tilted | 8 % → 8 % | 21.1 px | 0.24 | 1.06 | 62 |
| over the wet one | 13 % → 16 % | 16.4 px | 0.24 | 1.18 | 48 |
| long, no reload | 26 % → 32 % | 11.6 px | 0.13 | 1.22 | 292 | quarters: 0.11 → 0.04 → 0.02 → 0.01

Numbers say: light vs heavy: width 6.9 → 20.4 px, dark 0.27 → 0.27; wet paint spreads well beyond the stroke.

## Dry Brush
Gouache · 24 px · 25.1 s

![Dry Brush](Dry-Brush.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 5 % → 0 % | 14.0 px | 0.65 | 0.09 | 102 |
| heavy line | 6 % → 0 % | 18.6 px | 0.65 | 0.02 | 204 |
| pressure swell | 5 % → 0 % | 18.2 px | 0.65 | 0.08 | 54 |
| fast wave | 6 % → 1 % | 7.3 px | 0.65 | 0.08 | 170 |
| slow wave | 7 % → 0 % | 8.1 px | 0.65 | 0.06 | 434 |
| spiral | 7 % → 0 % | 4.6 px | 0.65 | 0.07 | 323 |
| loop | 10 % → 0 % | 12.4 px | 0.65 | 0.04 | 167 |
| tilted | 4 % → 3 % | 10.6 px | 0.65 | 0.88 | 74 |
| over the wet one | 9 % → 1 % | 14.5 px | 0.65 | 0.12 | 125 |
| long, no reload | 6 % → 1 % | 2.9 px | 0.65 | 0.14 | 758 | quarters: 0.12 → 0.00 → 0.00 → 0.00

Numbers say: light vs heavy: width 14.0 → 18.6 px, dark 0.65 → 0.65.

## Wax Crayon
Wax · 8 px · 12.6 s

![Wax Crayon](Wax-Crayon.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 1 % → 1 % | 2.5 px | 0.71 | 1.00 | 35 |
| heavy line | 1 % → 1 % | 3.9 px | 0.69 | 1.00 | 40 |
| pressure swell | 1 % → 1 % | 3.3 px | 0.70 | 1.00 | 19 |
| fast wave | 3 % → 3 % | 3.5 px | 0.69 | 1.00 | 48 |
| slow wave | 3 % → 3 % | 3.4 px | 0.70 | 1.00 | 43 |
| spiral | 5 % → 5 % | 3.3 px | 0.70 | 1.00 | 98 |
| loop | 3 % → 3 % | 3.3 px | 0.70 | 1.00 | 51 |
| tilted | 2 % → 2 % | 5.6 px | 0.68 | 1.00 | 46 |
| over the wet one | 3 % → 3 % | 3.6 px | 0.68 | 1.00 | 25 |
| long, no reload | 7 % → 7 % | 3.3 px | 0.70 | 1.00 | 187 | quarters: 0.06 → 0.06 → 0.06 → 0.06

Numbers say: light vs heavy: width 2.5 → 3.9 px, dark 0.71 → 0.69; the long stroke does not run out of paint.

## Oil Pastel
Wax · 12 px · 12.4 s

![Oil Pastel](Oil-Pastel.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 1 % → 1 % | 4.0 px | 0.68 | 1.00 | 29 |
| heavy line | 2 % → 2 % | 6.5 px | 0.68 | 1.00 | 35 |
| pressure swell | 2 % → 2 % | 5.7 px | 0.69 | 1.00 | 22 |
| fast wave | 5 % → 5 % | 5.7 px | 0.68 | 1.00 | 103 |
| slow wave | 5 % → 5 % | 5.5 px | 0.68 | 1.00 | 70 |
| spiral | 8 % → 8 % | 5.5 px | 0.68 | 1.00 | 147 |
| loop | 4 % → 4 % | 5.6 px | 0.68 | 1.00 | 92 |
| tilted | 2 % → 2 % | 6.8 px | 0.68 | 1.00 | 57 |
| over the wet one | 5 % → 5 % | 5.8 px | 0.68 | 1.00 | 29 |
| long, no reload | 13 % → 13 % | 5.6 px | 0.68 | 1.00 | 186 | quarters: 0.10 → 0.09 → 0.10 → 0.10

Numbers say: light vs heavy: width 4.0 → 6.5 px, dark 0.68 → 0.68; the long stroke does not run out of paint.

## Charcoal
Charcoal · 5 px · 11.5 s

![Charcoal](Charcoal.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 1 % → 1 % | 2.0 px | 0.74 | 1.00 | 26 |
| heavy line | 1 % → 1 % | 3.0 px | 0.74 | 1.00 | 19 |
| pressure swell | 1 % → 1 % | 2.7 px | 0.74 | 1.00 | 10 |
| fast wave | 2 % → 2 % | 2.7 px | 0.73 | 1.00 | 34 |
| slow wave | 2 % → 2 % | 2.6 px | 0.74 | 1.00 | 27 |
| spiral | 4 % → 4 % | 2.5 px | 0.74 | 1.00 | 62 |
| loop | 2 % → 2 % | 2.6 px | 0.74 | 1.00 | 36 |
| tilted | 2 % → 2 % | 4.3 px | 0.72 | 1.00 | 29 |
| over the wet one | 2 % → 2 % | 2.4 px | 0.72 | 1.00 | 18 |
| long, no reload | 6 % → 6 % | 2.7 px | 0.73 | 1.00 | 85 | quarters: 0.05 → 0.05 → 0.05 → 0.05

Numbers say: light vs heavy: width 2.0 → 3.0 px, dark 0.74 → 0.74; the long stroke does not run out of paint.

## Impasto
Heavy acrylic · 22 px · 17.8 s

![Impasto](Impasto.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 8 % → 8 % | 24.1 px | 0.71 | 0.93 | 61 |
| heavy line | 10 % → 9 % | 28.8 px | 0.70 | 0.94 | 132 |
| pressure swell | 7 % → 7 % | 28.1 px | 0.72 | 0.94 | 76 |
| fast wave | 20 % → 13 % | 23.5 px | 0.71 | 0.64 | 232 |
| slow wave | 21 % → 14 % | 24.5 px | 0.71 | 0.66 | 284 |
| spiral | 30 % → 14 % | 20.0 px | 0.71 | 0.46 | 305 |
| loop | 18 % → 14 % | 23.9 px | 0.71 | 0.77 | 181 |
| tilted | 8 % → 8 % | 21.8 px | 0.70 | 1.00 | 97 |
| over the wet one | 17 % → 15 % | 25.4 px | 0.70 | 0.91 | 145 |
| long, no reload | 34 % → 14 % | 15.2 px | 0.71 | 0.41 | 686 | quarters: 0.38 → 0.21 → 0.10 → 0.03

Numbers say: light vs heavy: width 24.1 → 28.8 px, dark 0.71 → 0.70.

## Oil Round
Oil · 18 px · 20.9 s

![Oil Round](Oil-Round.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 2 % → 2 % | 7.2 px | 0.75 | 1.00 | 46 |
| heavy line | 7 % → 7 % | 19.3 px | 0.73 | 1.00 | 87 |
| pressure swell | 4 % → 4 % | 13.7 px | 0.72 | 1.00 | 51 |
| fast wave | 11 % → 11 % | 12.7 px | 0.65 | 1.00 | 162 |
| slow wave | 8 % → 8 % | 9.0 px | 0.57 | 1.00 | 251 |
| spiral | 10 % → 10 % | 6.6 px | 0.50 | 1.00 | 331 |
| loop | 5 % → 5 % | 7.1 px | 0.45 | 1.00 | 143 |
| tilted | 4 % → 4 % | 10.1 px | 0.52 | 1.00 | 81 |
| over the wet one | 6 % → 6 % | 7.4 px | 0.52 | 1.00 | 58 |
| long, no reload | 15 % → 15 % | 6.8 px | 0.42 | 1.00 | 454 | quarters: 0.08 → 0.08 → 0.07 → 0.06

Numbers say: light vs heavy: width 7.2 → 19.3 px, dark 0.75 → 0.73.

## Palette Knife
Oil · 20 px · 20.8 s

![Palette Knife](Palette-Knife.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 8 % → 8 % | 21.9 px | 0.67 | 1.00 | 14 |
| heavy line | 8 % → 8 % | 22.5 px | 0.73 | 1.00 | 21 |
| pressure swell | 6 % → 6 % | 22.4 px | 0.74 | 1.00 | 8 |
| fast wave | 17 % → 17 % | 19.3 px | 0.49 | 1.00 | 33 |
| slow wave | 17 % → 17 % | 19.9 px | 0.43 | 1.00 | 50 |
| spiral | 18 % → 18 % | 11.7 px | 0.45 | 1.00 | 74 |
| loop | 16 % → 16 % | 21.0 px | 0.58 | 1.00 | 27 |
| tilted | 5 % → 5 % | 15.0 px | 0.72 | 1.00 | 20 |
| over the wet one | 13 % → 13 % | 21.0 px | 0.72 | 1.00 | 17 |
| long, no reload | 17 % → 17 % | 7.5 px | 0.47 | 1.00 | 66 | quarters: 0.29 → 0.05 → 0.00 → 0.00

Numbers say: light vs heavy: width 21.9 → 22.5 px, dark 0.67 → 0.73; pressure barely changes the width.

## Water
Watercolor · 20 px · 47.2 s · over bands of wet oil paint and oil pastel in turn (it works on paint already there: look at what it does to the bands; covered counts the bands too)

![Water](Water.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 25 % → 27 % | 73.8 px | 0.80 | 1.06 | 48 |
| heavy line | 24 % → 25 % | 69.8 px | 0.81 | 1.04 | 80 |
| pressure swell | 24 % → 25 % | 89.6 px | 0.81 | 1.03 | 61 |
| fast wave | 24 % → 26 % | 27.7 px | 0.81 | 1.07 | 139 |
| slow wave | 24 % → 25 % | 27.7 px | 0.81 | 1.06 | 216 |
| spiral | 24 % → 26 % | 15.9 px | 0.81 | 1.07 | 218 |
| loop | 24 % → 25 % | 31.1 px | 0.81 | 1.03 | 104 |
| tilted | 24 % → 24 % | 67.0 px | 0.81 | 1.00 | 98 |
| over the wet one | 24 % → 25 % | 0.0 px | 0.81 | 1.06 | 65 |
| long, no reload | 24 % → 26 % | 10.7 px | 0.81 | 1.08 | 317 | quarters: 0.21 → 0.27 → 0.18 → 0.27

Numbers say: light vs heavy: width 73.8 → 69.8 px, dark 0.80 → 0.81; pressure barely changes the width; the long stroke does not run out of paint.

## Blender
Pastel · 16 px · 29.9 s · over bands of wet oil paint and oil pastel in turn (it works on paint already there: look at what it does to the bands; covered counts the bands too)

![Blender](Blender.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 24 % → 24 % | 70.7 px | 0.81 | 1.00 | 30 |
| heavy line | 25 % → 25 % | 72.1 px | 0.80 | 1.00 | 57 |
| pressure swell | 24 % → 24 % | 91.3 px | 0.81 | 1.00 | 42 |
| fast wave | 26 % → 26 % | 30.0 px | 0.79 | 1.00 | 97 |
| slow wave | 26 % → 26 % | 29.9 px | 0.80 | 1.00 | 121 |
| spiral | 28 % → 28 % | 18.7 px | 0.77 | 1.00 | 145 |
| loop | 25 % → 25 % | 32.9 px | 0.80 | 1.00 | 131 |
| tilted | 25 % → 25 % | 70.1 px | 0.79 | 1.00 | 64 |
| over the wet one | 26 % → 26 % | 1.8 px | 0.79 | 1.00 | 40 |
| long, no reload | 30 % → 30 % | 13.7 px | 0.76 | 1.00 | 305 | quarters: 0.20 → 0.28 → 0.23 → 0.30

Numbers say: light vs heavy: width 70.7 → 72.1 px, dark 0.81 → 0.80; pressure barely changes the width; the long stroke does not run out of paint.

## Eraser
Eraser · 16 px · 29.4 s · over bands of wet oil paint and oil pastel in turn (it works on paint already there: look at what it does to the bands; covered counts the bands too)

![Eraser](Eraser.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 24 % → 24 % | 69.5 px | 0.82 | 1.00 | 42 |
| heavy line | 23 % → 23 % | 67.9 px | 0.82 | 1.00 | 67 |
| pressure swell | 23 % → 23 % | 87.3 px | 0.82 | 1.00 | 30 |
| fast wave | 22 % → 22 % | 25.7 px | 0.82 | 1.00 | 91 |
| slow wave | 22 % → 22 % | 25.7 px | 0.82 | 1.00 | 121 |
| spiral | 22 % → 22 % | 14.4 px | 0.82 | 1.00 | 214 |
| loop | 22 % → 22 % | 28.6 px | 0.82 | 1.00 | 133 |
| tilted | 23 % → 23 % | 65.1 px | 0.82 | 1.00 | 66 |
| over the wet one | 23 % → 23 % | 0.0 px | 0.82 | 1.00 | 63 |
| long, no reload | 20 % → 20 % | 8.9 px | 0.82 | 1.00 | 329 | quarters: 0.15 → 0.20 → 0.15 → 0.20

Numbers say: light vs heavy: width 69.5 → 67.9 px, dark 0.82 → 0.82; pressure barely changes the width; the long stroke does not run out of paint.

## Fan
Gouache · 30 px · 38.9 s

![Fan](Fan.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 9 % → 3 % | 25.7 px | 0.63 | 0.37 | 72 |
| heavy line | 11 % → 4 % | 31.0 px | 0.63 | 0.39 | 99 |
| pressure swell | 8 % → 5 % | 31.7 px | 0.63 | 0.55 | 45 |
| fast wave | 18 % → 5 % | 20.3 px | 0.63 | 0.26 | 143 |
| slow wave | 18 % → 5 % | 21.1 px | 0.63 | 0.25 | 333 |
| spiral | 24 % → 5 % | 15.8 px | 0.63 | 0.20 | 294 |
| loop | 17 % → 5 % | 22.7 px | 0.63 | 0.29 | 212 |
| tilted | 5 % → 6 % | 15.1 px | 0.63 | 1.05 | 68 |
| over the wet one | 16 % → 8 % | 29.8 px | 0.63 | 0.50 | 84 |
| long, no reload | 23 % → 5 % | 10.1 px | 0.63 | 0.22 | 353 | quarters: 0.29 → 0.07 → 0.01 → 0.00

Numbers say: light vs heavy: width 25.7 → 31.0 px, dark 0.63 → 0.63.

## Sponge
Gouache · 30 px · 38.4 s

![Sponge](Sponge.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 4 % → 0 % | 11.4 px | 0.62 | 0.12 | 58 |
| heavy line | 12 % → 2 % | 35.4 px | 0.62 | 0.14 | 86 |
| pressure swell | 7 % → 2 % | 27.9 px | 0.62 | 0.27 | 53 |
| fast wave | 20 % → 4 % | 23.2 px | 0.62 | 0.19 | 210 |
| slow wave | 21 % → 4 % | 23.7 px | 0.62 | 0.18 | 429 |
| spiral | 28 % → 4 % | 18.3 px | 0.62 | 0.14 | 319 |
| loop | 18 % → 5 % | 23.0 px | 0.62 | 0.29 | 237 |
| tilted | 7 % → 7 % | 18.2 px | 0.62 | 1.04 | 134 |
| over the wet one | 16 % → 6 % | 27.8 px | 0.62 | 0.37 | 71 |
| long, no reload | 29 % → 5 % | 12.9 px | 0.62 | 0.17 | 427 | quarters: 0.29 → 0.13 → 0.07 → 0.04

Numbers say: light vs heavy: width 11.4 → 35.4 px, dark 0.62 → 0.62.

## Ink — sumi brush
Watercolor · 22 px · 40.2 s

![Ink — sumi brush](Ink-sumi-brush.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 8 % → 9 % | 23.9 px | 0.87 | 1.12 | 118 |
| heavy line | 13 % → 13 % | 38.1 px | 0.86 | 1.01 | 128 |
| pressure swell | 9 % → 10 % | 34.5 px | 0.87 | 1.05 | 62 |
| fast wave | 28 % → 28 % | 32.6 px | 0.81 | 1.01 | 239 |
| slow wave | 26 % → 26 % | 29.7 px | 0.83 | 1.03 | 530 |
| spiral | 38 % → 38 % | 25.3 px | 0.75 | 1.00 | 506 |
| loop | 22 % → 22 % | 28.5 px | 0.85 | 1.02 | 250 |
| tilted | 9 % → 9 % | 25.3 px | 0.86 | 1.01 | 118 |
| over the wet one | 20 % → 21 % | 30.7 px | 0.86 | 1.03 | 94 |
| long, no reload | 45 % → 43 % | 20.1 px | 0.69 | 0.97 | 547 | quarters: 0.55 → 0.41 → 0.24 → 0.15

Numbers say: light vs heavy: width 23.9 → 38.1 px, dark 0.87 → 0.86.

## Ink — wash
Watercolor · 40 px · 47.3 s

![Ink — wash](Ink-wash.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 13 % → 13 % | 37.3 px | 0.42 | 1.02 | 123 |
| heavy line | 19 % → 19 % | 55.2 px | 0.35 | 1.01 | 138 |
| pressure swell | 13 % → 13 % | 48.2 px | 0.40 | 1.02 | 103 |
| fast wave | 41 % → 42 % | 47.8 px | 0.32 | 1.02 | 243 |
| slow wave | 39 % → 40 % | 45.3 px | 0.42 | 1.02 | 582 |
| spiral | 60 % → 62 % | 39.7 px | 0.33 | 1.02 | 446 |
| loop | 34 % → 34 % | 43.8 px | 0.39 | 1.01 | 301 |
| tilted | 15 % → 15 % | 40.7 px | 0.43 | 1.01 | 216 |
| over the wet one | 30 % → 31 % | 43.4 px | 0.43 | 1.02 | 146 |
| long, no reload | 71 % → 75 % | 32.0 px | 0.31 | 1.05 | 707 | quarters: 0.40 → 0.29 → 0.19 → 0.12

Numbers say: light vs heavy: width 37.3 → 55.2 px, dark 0.42 → 0.35.

## Ink — dry brush
Ink · 30 px · 34.1 s

![Ink — dry brush](Ink-dry-brush.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 9 % → 7 % | 25.4 px | 0.81 | 0.78 | 112 |
| heavy line | 10 % → 8 % | 29.9 px | 0.79 | 0.75 | 157 |
| pressure swell | 7 % → 6 % | 28.1 px | 0.81 | 0.84 | 91 |
| fast wave | 21 % → 8 % | 24.3 px | 0.79 | 0.40 | 269 |
| slow wave | 17 % → 7 % | 20.2 px | 0.79 | 0.39 | 652 |
| spiral | 23 % → 8 % | 15.4 px | 0.78 | 0.34 | 505 |
| loop | 19 % → 8 % | 24.4 px | 0.78 | 0.44 | 329 |
| tilted | 8 % → 8 % | 22.7 px | 0.78 | 1.02 | 248 |
| over the wet one | 17 % → 14 % | 25.9 px | 0.78 | 0.81 | 194 |
| long, no reload | 20 % → 8 % | 9.0 px | 0.79 | 0.42 | 761 | quarters: 0.32 → 0.02 → 0.00 → 0.00

Numbers say: light vs heavy: width 25.4 → 29.9 px, dark 0.81 → 0.79.

## Ink — nib
Watercolor · 5 px · 32.8 s

![Ink — nib](Ink-nib.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 2 % → 5 % | 5.5 px | 0.89 | 2.46 | 31 |
| heavy line | 2 % → 5 % | 6.4 px | 0.89 | 2.33 | 27 |
| pressure swell | 2 % → 4 % | 6.2 px | 0.89 | 2.52 | 40 |
| fast wave | 5 % → 8 % | 5.9 px | 0.89 | 1.63 | 122 |
| slow wave | 5 % → 8 % | 5.7 px | 0.89 | 1.70 | 131 |
| spiral | 8 % → 11 % | 5.0 px | 0.87 | 1.41 | 147 |
| loop | 4 % → 8 % | 5.7 px | 0.89 | 1.73 | 73 |
| tilted | 4 % → 4 % | 10.3 px | 0.89 | 1.02 | 41 |
| over the wet one | 6 % → 9 % | 6.1 px | 0.89 | 1.61 | 62 |
| long, no reload | 9 % → 12 % | 4.2 px | 0.84 | 1.30 | 236 | quarters: 0.24 → 0.11 → 0.07 → 0.05

Numbers say: light vs heavy: width 5.5 → 6.4 px, dark 0.89 → 0.89; wet paint spreads well beyond the stroke.

## 0.45 · Dry brush
Gouache · 34 px · 35.7 s

![0.45 · Dry brush](0-45-Dry-brush.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 8 % → 2 % | 22.2 px | 0.68 | 0.29 | 226 |
| heavy line | 8 % → 3 % | 23.3 px | 0.68 | 0.31 | 165 |
| pressure swell | 6 % → 3 % | 24.3 px | 0.68 | 0.39 | 106 |
| fast wave | 13 % → 3 % | 15.3 px | 0.68 | 0.23 | 461 |
| slow wave | 16 % → 3 % | 18.3 px | 0.68 | 0.20 | 701 |
| spiral | 20 % → 3 % | 13.2 px | 0.68 | 0.15 | 741 |
| loop | 14 % → 4 % | 18.3 px | 0.68 | 0.26 | 392 |
| tilted | 6 % → 6 % | 17.9 px | 0.68 | 1.01 | 182 |
| over the wet one | 14 % → 6 % | 22.1 px | 0.68 | 0.41 | 224 |
| long, no reload | 21 % → 4 % | 9.3 px | 0.68 | 0.18 | 1272 | quarters: 0.28 → 0.14 → 0.07 → 0.03

Numbers say: light vs heavy: width 22.2 → 23.3 px, dark 0.68 → 0.68; pressure barely changes the width.

## Dry pastel
Pastel · 26 px · 14.4 s

![Dry pastel](Dry-pastel.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 3 % → 3 % | 8.3 px | 0.38 | 1.00 | 54 |
| heavy line | 5 % → 5 % | 13.2 px | 0.39 | 1.00 | 55 |
| pressure swell | 3 % → 3 % | 11.7 px | 0.38 | 1.00 | 49 |
| fast wave | 10 % → 10 % | 11.9 px | 0.39 | 1.00 | 133 |
| slow wave | 10 % → 10 % | 11.3 px | 0.39 | 1.00 | 184 |
| spiral | 15 % → 15 % | 9.6 px | 0.39 | 1.00 | 185 |
| loop | 7 % → 7 % | 9.4 px | 0.39 | 1.00 | 119 |
| tilted | 3 % → 3 % | 8.3 px | 0.38 | 1.00 | 72 |
| over the wet one | 7 % → 7 % | 11.1 px | 0.38 | 1.00 | 51 |
| long, no reload | 18 % → 18 % | 8.2 px | 0.39 | 1.00 | 325 | quarters: 0.08 → 0.08 → 0.08 → 0.07

Numbers say: light vs heavy: width 8.3 → 13.2 px, dark 0.38 → 0.39; the long stroke does not run out of paint.

## 0.45 · Charcoal
Charcoal · 18 px · 14.1 s

![0.45 · Charcoal](0-45-Charcoal.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 2 % → 2 % | 6.5 px | 0.80 | 1.00 | 40 |
| heavy line | 3 % → 3 % | 9.2 px | 0.80 | 1.00 | 37 |
| pressure swell | 2 % → 2 % | 8.8 px | 0.80 | 1.00 | 28 |
| fast wave | 7 % → 7 % | 8.5 px | 0.80 | 1.00 | 56 |
| slow wave | 7 % → 7 % | 8.0 px | 0.80 | 1.00 | 84 |
| spiral | 12 % → 12 % | 7.9 px | 0.80 | 1.00 | 117 |
| loop | 6 % → 6 % | 8.1 px | 0.80 | 1.00 | 62 |
| tilted | 3 % → 3 % | 7.5 px | 0.80 | 1.00 | 29 |
| over the wet one | 6 % → 6 % | 7.9 px | 0.80 | 1.00 | 22 |
| long, no reload | 17 % → 17 % | 7.8 px | 0.80 | 1.00 | 153 | quarters: 0.15 → 0.16 → 0.15 → 0.16

Numbers say: light vs heavy: width 6.5 → 9.2 px, dark 0.80 → 0.80; the long stroke does not run out of paint.

## Watercolour — wash
Watercolor · 50 px · 50.7 s

![Watercolour — wash](Watercolour-wash.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 16 % → 16 % | 45.5 px | 0.22 | 1.00 | 161 |
| heavy line | 22 % → 22 % | 64.9 px | 0.19 | 1.00 | 160 |
| pressure swell | 15 % → 15 % | 56.1 px | 0.22 | 1.01 | 125 |
| fast wave | 48 % → 49 % | 55.6 px | 0.19 | 1.01 | 324 |
| slow wave | 46 % → 46 % | 53.3 px | 0.24 | 1.00 | 600 |
| spiral | 66 % → 66 % | 43.7 px | 0.21 | 1.00 | 1167 |
| loop | 40 % → 40 % | 51.4 px | 0.22 | 1.00 | 333 |
| tilted | 18 % → 18 % | 49.7 px | 0.23 | 1.00 | 249 |
| over the wet one | 36 % → 36 % | 49.6 px | 0.23 | 1.01 | 175 |
| long, no reload | 84 % → 84 % | 37.7 px | 0.20 | 1.00 | 941 | quarters: 0.24 → 0.20 → 0.16 → 0.12

Numbers say: light vs heavy: width 45.5 → 64.9 px, dark 0.22 → 0.19.

## Watercolour — wet-in-wet
Watercolor · 44 px · 50.0 s

![Watercolour — wet-in-wet](Watercolour-wet-in-wet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 13 % → 19 % | 38.4 px | 0.34 | 1.43 | 105 |
| heavy line | 19 % → 20 % | 54.6 px | 0.36 | 1.05 | 109 |
| pressure swell | 12 % → 15 % | 46.5 px | 0.37 | 1.22 | 94 |
| fast wave | 41 % → 45 % | 47.7 px | 0.35 | 1.09 | 336 |
| slow wave | 40 % → 45 % | 46.2 px | 0.42 | 1.12 | 517 |
| spiral | 63 % → 67 % | 41.5 px | 0.38 | 1.06 | 553 |
| loop | 34 % → 37 % | 44.4 px | 0.40 | 1.09 | 338 |
| tilted | 15 % → 16 % | 41.5 px | 0.38 | 1.06 | 176 |
| over the wet one | 31 % → 37 % | 43.9 px | 0.38 | 1.21 | 114 |
| long, no reload | 78 % → 84 % | 34.8 px | 0.37 | 1.08 | 1143 | quarters: 0.39 → 0.37 → 0.32 → 0.26

Numbers say: light vs heavy: width 38.4 → 54.6 px, dark 0.34 → 0.36.

## Watercolour — glaze
Watercolor · 38 px · 45.3 s

![Watercolour — glaze](Watercolour-glaze.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 13 % → 13 % | 36.6 px | 0.07 | 1.01 | 100 |
| heavy line | 19 % → 19 % | 55.4 px | 0.07 | 1.00 | 119 |
| pressure swell | 13 % → 13 % | 47.0 px | 0.07 | 1.01 | 62 |
| fast wave | 40 % → 40 % | 45.6 px | 0.07 | 1.01 | 436 |
| slow wave | 37 % → 37 % | 42.8 px | 0.07 | 1.01 | 504 |
| spiral | 59 % → 60 % | 38.8 px | 0.06 | 1.01 | 442 |
| loop | 33 % → 33 % | 42.6 px | 0.07 | 1.00 | 205 |
| tilted | 14 % → 14 % | 40.1 px | 0.07 | 1.00 | 161 |
| over the wet one | 30 % → 30 % | 42.3 px | 0.07 | 1.01 | 121 |
| long, no reload | 69 % → 70 % | 30.9 px | 0.06 | 1.01 | 618 | quarters: 0.06 → 0.05 → 0.03 → 0.02

Numbers say: light vs heavy: width 36.6 → 55.4 px, dark 0.07 → 0.07.

## Watercolour — granulating
Watercolor · 44 px · 46.1 s

![Watercolour — granulating](Watercolour-granulating.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 14 % → 14 % | 41.4 px | 0.35 | 1.00 | 112 |
| heavy line | 21 % → 21 % | 60.4 px | 0.31 | 1.00 | 164 |
| pressure swell | 14 % → 14 % | 52.2 px | 0.34 | 1.01 | 78 |
| fast wave | 45 % → 45 % | 51.7 px | 0.29 | 1.01 | 342 |
| slow wave | 42 % → 42 % | 48.2 px | 0.35 | 1.01 | 555 |
| spiral | 62 % → 63 % | 41.0 px | 0.30 | 1.01 | 577 |
| loop | 37 % → 37 % | 47.6 px | 0.33 | 1.00 | 388 |
| tilted | 16 % → 16 % | 45.5 px | 0.35 | 1.00 | 171 |
| over the wet one | 33 % → 33 % | 46.2 px | 0.35 | 1.01 | 142 |
| long, no reload | 75 % → 76 % | 33.6 px | 0.29 | 1.01 | 790 | quarters: 0.34 → 0.26 → 0.20 → 0.14

Numbers say: light vs heavy: width 41.4 → 60.4 px, dark 0.35 → 0.31.

## Watercolour — dry brush
Watercolor · 36 px · 40.1 s

![Watercolour — dry brush](Watercolour-dry-brush.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 10 % → 10 % | 28.0 px | 0.17 | 1.01 | 166 |
| heavy line | 14 % → 13 % | 40.1 px | 0.16 | 0.93 | 138 |
| pressure swell | 11 % → 11 % | 40.5 px | 0.16 | 0.98 | 121 |
| fast wave | 27 % → 20 % | 30.8 px | 0.13 | 0.74 | 335 |
| slow wave | 24 % → 17 % | 28.1 px | 0.14 | 0.71 | 672 |
| spiral | 34 % → 20 % | 22.4 px | 0.13 | 0.57 | 614 |
| loop | 21 % → 18 % | 27.2 px | 0.14 | 0.86 | 334 |
| tilted | 10 % → 10 % | 28.6 px | 0.16 | 1.00 | 151 |
| over the wet one | 22 % → 20 % | 31.4 px | 0.16 | 0.95 | 144 |
| long, no reload | 36 % → 19 % | 16.1 px | 0.14 | 0.54 | 1251 | quarters: 0.09 → 0.03 → 0.01 → 0.00

Numbers say: light vs heavy: width 28.0 → 40.1 px, dark 0.17 → 0.16.

## Gouache
Gouache · 30 px · 35.7 s

![Gouache](Gouache.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 8 % → 6 % | 24.7 px | 0.28 | 0.66 | 105 |
| heavy line | 14 % → 7 % | 39.8 px | 0.28 | 0.49 | 121 |
| pressure swell | 10 % → 6 % | 38.8 px | 0.28 | 0.62 | 83 |
| fast wave | 28 % → 8 % | 32.8 px | 0.28 | 0.27 | 309 |
| slow wave | 27 % → 8 % | 31.6 px | 0.28 | 0.30 | 490 |
| spiral | 38 % → 8 % | 25.0 px | 0.28 | 0.22 | 475 |
| loop | 22 % → 8 % | 28.8 px | 0.28 | 0.36 | 339 |
| tilted | 9 % → 9 % | 24.6 px | 0.27 | 1.00 | 176 |
| over the wet one | 20 % → 13 % | 31.0 px | 0.27 | 0.67 | 111 |
| long, no reload | 40 % → 10 % | 17.9 px | 0.27 | 0.24 | 697 | quarters: 0.01 → 0.01 → 0.02 → 0.02

Numbers say: light vs heavy: width 24.7 → 39.8 px, dark 0.28 → 0.28; the long stroke does not run out of paint.

## Oil — alla prima
Oil · 30 px · 19.5 s

![Oil — alla prima](Oil-alla-prima.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 10 % → 10 % | 27.7 px | 0.51 | 1.00 | 148 |
| heavy line | 10 % → 10 % | 30.4 px | 0.51 | 1.00 | 153 |
| pressure swell | 8 % → 8 % | 29.9 px | 0.53 | 1.00 | 93 |
| fast wave | 25 % → 25 % | 29.1 px | 0.52 | 1.00 | 265 |
| slow wave | 26 % → 26 % | 29.9 px | 0.52 | 1.00 | 445 |
| spiral | 41 % → 41 % | 26.8 px | 0.51 | 1.00 | 546 |
| loop | 22 % → 22 % | 28.0 px | 0.52 | 1.00 | 238 |
| tilted | 11 % → 11 % | 31.1 px | 0.51 | 1.00 | 160 |
| over the wet one | 21 % → 21 % | 26.6 px | 0.51 | 1.00 | 102 |
| long, no reload | 50 % → 50 % | 22.3 px | 0.50 | 1.00 | 703 | quarters: 0.33 → 0.30 → 0.26 → 0.22

Numbers say: light vs heavy: width 27.7 → 30.4 px, dark 0.51 → 0.51; pressure barely changes the width.

## Oil — impasto
Oil · 34 px · 26.2 s

![Oil — impasto](Oil-impasto.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 12 % → 12 % | 33.5 px | 0.23 | 1.00 | 183 |
| heavy line | 13 % → 13 % | 36.3 px | 0.23 | 1.00 | 135 |
| pressure swell | 10 % → 10 % | 35.9 px | 0.25 | 1.00 | 79 |
| fast wave | 27 % → 27 % | 31.5 px | 0.23 | 1.00 | 311 |
| slow wave | 29 % → 29 % | 33.9 px | 0.23 | 1.00 | 652 |
| spiral | 46 % → 46 % | 30.0 px | 0.22 | 1.00 | 650 |
| loop | 25 % → 25 % | 32.2 px | 0.23 | 1.00 | 302 |
| tilted | 12 % → 12 % | 32.4 px | 0.24 | 1.00 | 152 |
| over the wet one | 23 % → 23 % | 31.5 px | 0.24 | 1.00 | 156 |
| long, no reload | 50 % → 50 % | 22.6 px | 0.22 | 1.00 | 1015 | quarters: 0.18 → 0.13 → 0.10 → 0.08

Numbers say: light vs heavy: width 33.5 → 36.3 px, dark 0.23 → 0.23; pressure barely changes the width.

## Oil — glaze
Oil · 40 px · 23.5 s

![Oil — glaze](Oil-glaze.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 9 % → 9 % | 27.0 px | 0.50 | 1.00 | 114 |
| heavy line | 13 % → 13 % | 38.2 px | 0.49 | 1.00 | 126 |
| pressure swell | 10 % → 10 % | 36.6 px | 0.50 | 1.00 | 96 |
| fast wave | 29 % → 29 % | 33.5 px | 0.49 | 1.00 | 344 |
| slow wave | 30 % → 30 % | 34.5 px | 0.50 | 1.00 | 637 |
| spiral | 46 % → 46 % | 30.0 px | 0.49 | 1.00 | 605 |
| loop | 24 % → 24 % | 31.4 px | 0.50 | 1.00 | 273 |
| tilted | 11 % → 11 % | 30.3 px | 0.50 | 1.00 | 225 |
| over the wet one | 22 % → 22 % | 32.5 px | 0.50 | 1.00 | 145 |
| long, no reload | 52 % → 52 % | 23.5 px | 0.49 | 1.00 | 1048 | quarters: 0.34 → 0.30 → 0.27 → 0.22

Numbers say: light vs heavy: width 27.0 → 38.2 px, dark 0.50 → 0.49.

## Oil — scumble
Oil · 36 px · 25.8 s

![Oil — scumble](Oil-scumble.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 9 % → 9 % | 26.5 px | 0.28 | 1.00 | 285 |
| heavy line | 9 % → 9 % | 26.0 px | 0.27 | 1.00 | 271 |
| pressure swell | 8 % → 8 % | 30.8 px | 0.25 | 1.00 | 195 |
| fast wave | 18 % → 18 % | 20.5 px | 0.22 | 1.00 | 450 |
| slow wave | 22 % → 22 % | 25.0 px | 0.21 | 1.00 | 808 |
| spiral | 31 % → 31 % | 20.6 px | 0.17 | 1.00 | 863 |
| loop | 18 % → 18 % | 23.1 px | 0.23 | 1.00 | 576 |
| tilted | 9 % → 9 % | 26.0 px | 0.25 | 1.00 | 252 |
| over the wet one | 19 % → 19 % | 26.4 px | 0.25 | 1.00 | 182 |
| long, no reload | 34 % → 34 % | 15.3 px | 0.15 | 1.00 | 1115 | quarters: 0.00 → 0.00 → 0.00 → 0.00

Numbers say: light vs heavy: width 26.5 → 26.0 px, dark 0.28 → 0.27; pressure barely changes the width.

## Acrylic — heavy body
Heavy acrylic · 30 px · 20.5 s

![Acrylic — heavy body](Acrylic-heavy-body.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 10 % → 9 % | 29.2 px | 0.51 | 0.92 | 183 |
| heavy line | 11 % → 10 % | 31.3 px | 0.51 | 0.93 | 225 |
| pressure swell | 8 % → 8 % | 30.8 px | 0.53 | 0.94 | 122 |
| fast wave | 23 % → 14 % | 26.7 px | 0.51 | 0.62 | 324 |
| slow wave | 24 % → 15 % | 27.8 px | 0.51 | 0.64 | 570 |
| spiral | 35 % → 15 % | 23.3 px | 0.51 | 0.42 | 486 |
| loop | 21 % → 16 % | 27.1 px | 0.51 | 0.76 | 319 |
| tilted | 9 % → 9 % | 25.5 px | 0.51 | 1.00 | 157 |
| over the wet one | 19 % → 17 % | 27.6 px | 0.51 | 0.90 | 127 |
| long, no reload | 38 % → 15 % | 17.2 px | 0.51 | 0.40 | 849 | quarters: 0.30 → 0.19 → 0.11 → 0.04

Numbers say: light vs heavy: width 29.2 → 31.3 px, dark 0.51 → 0.51; pressure barely changes the width.

## Acrylic — fluid
Watercolor · 36 px · 42.0 s

![Acrylic — fluid](Acrylic-fluid.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 12 % → 12 % | 34.8 px | 0.24 | 1.01 | 107 |
| heavy line | 18 % → 18 % | 52.6 px | 0.21 | 0.99 | 132 |
| pressure swell | 12 % → 12 % | 45.4 px | 0.23 | 1.00 | 133 |
| fast wave | 38 % → 38 % | 44.1 px | 0.19 | 0.98 | 288 |
| slow wave | 35 % → 35 % | 40.5 px | 0.22 | 1.00 | 469 |
| spiral | 55 % → 53 % | 36.0 px | 0.19 | 0.98 | 516 |
| loop | 31 % → 31 % | 40.2 px | 0.21 | 1.00 | 213 |
| tilted | 12 % → 12 % | 34.2 px | 0.24 | 1.00 | 142 |
| over the wet one | 27 % → 28 % | 42.3 px | 0.24 | 1.01 | 131 |
| long, no reload | 61 % → 58 % | 27.6 px | 0.19 | 0.95 | 969 | quarters: 0.20 → 0.14 → 0.09 → 0.06

Numbers say: light vs heavy: width 34.8 → 52.6 px, dark 0.24 → 0.21.

## Acrylic — palette knife
Heavy acrylic · 42 px · 23.5 s

![Acrylic — palette knife](Acrylic-palette-knife.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 15 % → 15 % | 44.0 px | 0.40 | 0.98 | 58 |
| heavy line | 15 % → 15 % | 44.2 px | 0.40 | 0.98 | 42 |
| pressure swell | 12 % → 11 % | 43.5 px | 0.42 | 0.99 | 27 |
| fast wave | 36 % → 20 % | 42.0 px | 0.37 | 0.55 | 99 |
| slow wave | 37 % → 21 % | 42.6 px | 0.37 | 0.57 | 169 |
| spiral | 49 % → 18 % | 32.5 px | 0.37 | 0.37 | 166 |
| loop | 32 % → 24 % | 41.2 px | 0.36 | 0.75 | 134 |
| tilted | 12 % → 12 % | 33.6 px | 0.39 | 1.00 | 68 |
| over the wet one | 26 % → 25 % | 39.7 px | 0.39 | 0.97 | 71 |
| long, no reload | 57 % → 21 % | 25.6 px | 0.35 | 0.36 | 206 | quarters: 0.00 → 0.00 → 0.00 → 0.01

Numbers say: light vs heavy: width 44.0 → 44.2 px, dark 0.40 → 0.40; pressure barely changes the width; the long stroke does not run out of paint.

## Finger on oil
Oil · 30 px · 17.6 s

![Finger on oil](Finger-on-oil.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 6 % → 6 % | 16.1 px | 0.39 | 1.00 | 68 |
| heavy line | 7 % → 7 % | 20.7 px | 0.38 | 1.00 | 90 |
| pressure swell | 6 % → 6 % | 21.5 px | 0.39 | 1.00 | 59 |
| fast wave | 11 % → 11 % | 13.2 px | 0.37 | 1.00 | 176 |
| slow wave | 17 % → 17 % | 19.2 px | 0.36 | 1.00 | 301 |
| spiral | 21 % → 21 % | 14.1 px | 0.34 | 1.00 | 236 |
| loop | 13 % → 13 % | 16.5 px | 0.37 | 1.00 | 162 |
| tilted | 7 % → 7 % | 20.7 px | 0.39 | 1.00 | 162 |
| over the wet one | 14 % → 14 % | 19.7 px | 0.39 | 1.00 | 106 |
| long, no reload | 22 % → 22 % | 9.9 px | 0.33 | 1.00 | 549 | quarters: 0.14 → 0.08 → 0.06 → 0.04

Numbers say: light vs heavy: width 16.1 → 20.7 px, dark 0.39 → 0.38.

## Palette knife — oil
Oil · 44 px · 27.5 s

![Palette knife — oil](Palette-knife-oil.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 16 % → 16 % | 45.7 px | 0.36 | 1.00 | 53 |
| heavy line | 16 % → 16 % | 46.3 px | 0.39 | 1.00 | 54 |
| pressure swell | 12 % → 12 % | 45.2 px | 0.38 | 1.00 | 27 |
| fast wave | 39 % → 39 % | 44.9 px | 0.35 | 1.01 | 101 |
| slow wave | 39 % → 39 % | 45.4 px | 0.35 | 1.00 | 170 |
| spiral | 62 % → 62 % | 40.9 px | 0.27 | 1.00 | 188 |
| loop | 34 % → 34 % | 43.8 px | 0.36 | 1.00 | 165 |
| tilted | 13 % → 13 % | 36.6 px | 0.38 | 1.00 | 43 |
| over the wet one | 28 % → 28 % | 40.8 px | 0.38 | 1.00 | 54 |
| long, no reload | 74 % → 74 % | 33.2 px | 0.25 | 1.00 | 244 | quarters: 0.00 → 0.00 → 0.00 → 0.00

Numbers say: light vs heavy: width 45.7 → 46.3 px, dark 0.36 → 0.39; pressure barely changes the width; the long stroke does not run out of paint.

## 0.45 · Sponge
Watercolor · 46 px · 44.8 s

![0.45 · Sponge](0-45-Sponge.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 27 % → 18 % | 78.2 px | 0.09 | 0.67 | 57 |
| heavy line | 32 % → 25 % | 91.7 px | 0.09 | 0.78 | 85 |
| pressure swell | 24 % → 17 % | 90.3 px | 0.11 | 0.71 | 60 |
| fast wave | 59 % → 43 % | 68.1 px | 0.10 | 0.73 | 246 |
| slow wave | 59 % → 48 % | 68.5 px | 0.13 | 0.80 | 388 |
| spiral | 75 % → 57 % | 49.3 px | 0.12 | 0.76 | 343 |
| loop | 53 % → 43 % | 68.6 px | 0.11 | 0.81 | 264 |
| tilted | 18 % → 18 % | 49.4 px | 0.15 | 1.00 | 132 |
| over the wet one | 44 % → 37 % | 74.4 px | 0.15 | 0.84 | 96 |
| long, no reload | 89 % → 71 % | 39.9 px | 0.13 | 0.79 | 561 | quarters: 0.13 → 0.12 → 0.10 → 0.07

Numbers say: light vs heavy: width 78.2 → 91.7 px, dark 0.09 → 0.09.

## 0.45 · Eraser
Eraser · 30 px · 28.4 s · over bands of wet oil paint and oil pastel in turn (it works on paint already there: look at what it does to the bands; covered counts the bands too)

![0.45 · Eraser](0-45-Eraser.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 24 % → 24 % | 69.2 px | 0.82 | 1.00 | 54 |
| heavy line | 23 % → 23 % | 67.4 px | 0.81 | 1.00 | 65 |
| pressure swell | 23 % → 23 % | 86.7 px | 0.82 | 1.00 | 44 |
| fast wave | 21 % → 21 % | 24.7 px | 0.81 | 1.00 | 220 |
| slow wave | 20 % → 20 % | 23.5 px | 0.82 | 1.00 | 445 |
| spiral | 20 % → 20 % | 13.5 px | 0.79 | 1.00 | 293 |
| loop | 21 % → 21 % | 27.8 px | 0.80 | 1.00 | 142 |
| tilted | 23 % → 23 % | 64.8 px | 0.81 | 1.00 | 83 |
| over the wet one | 22 % → 22 % | 0.0 px | 0.81 | 1.00 | 75 |
| long, no reload | 17 % → 17 % | 7.5 px | 0.79 | 1.00 | 409 | quarters: 0.13 → 0.16 → 0.13 → 0.17

Numbers say: light vs heavy: width 69.2 → 67.4 px, dark 0.82 → 0.81; pressure barely changes the width; the long stroke does not run out of paint.

## Lift wet paint
Eraser · 30 px · 26.4 s · over bands of wet oil paint and oil pastel in turn (it works on paint already there: look at what it does to the bands; covered counts the bands too)

![Lift wet paint](Lift-wet-paint.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 24 % → 24 % | 70.1 px | 0.82 | 1.00 | 46 |
| heavy line | 24 % → 24 % | 69.8 px | 0.82 | 1.00 | 64 |
| pressure swell | 24 % → 24 % | 89.5 px | 0.82 | 1.00 | 46 |
| fast wave | 24 % → 24 % | 27.7 px | 0.82 | 1.00 | 127 |
| slow wave | 24 % → 24 % | 27.7 px | 0.82 | 1.00 | 211 |
| spiral | 24 % → 24 % | 15.9 px | 0.82 | 1.00 | 230 |
| loop | 24 % → 24 % | 31.1 px | 0.82 | 1.00 | 129 |
| tilted | 24 % → 24 % | 66.8 px | 0.82 | 1.00 | 79 |
| over the wet one | 24 % → 24 % | 0.0 px | 0.82 | 1.00 | 87 |
| long, no reload | 24 % → 24 % | 10.7 px | 0.82 | 1.00 | 414 | quarters: 0.18 → 0.24 → 0.17 → 0.24

Numbers say: light vs heavy: width 70.1 → 69.8 px, dark 0.82 → 0.82; pressure barely changes the width; the long stroke does not run out of paint.

## Sgraffito
Eraser · 10 px · 25.8 s · over bands of wet oil paint and oil pastel in turn (it works on paint already there: look at what it does to the bands; covered counts the bands too)

![Sgraffito](Sgraffito.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 24 % → 24 % | 69.5 px | 0.81 | 1.00 | 13 |
| heavy line | 24 % → 24 % | 69.5 px | 0.82 | 1.00 | 12 |
| pressure swell | 24 % → 24 % | 89.5 px | 0.82 | 1.00 | 6 |
| fast wave | 24 % → 24 % | 27.4 px | 0.82 | 1.00 | 32 |
| slow wave | 24 % → 24 % | 27.4 px | 0.81 | 1.00 | 35 |
| spiral | 24 % → 24 % | 15.7 px | 0.81 | 1.00 | 51 |
| loop | 24 % → 24 % | 30.9 px | 0.82 | 1.00 | 23 |
| tilted | 24 % → 24 % | 66.6 px | 0.82 | 1.00 | 10 |
| over the wet one | 24 % → 24 % | 0.0 px | 0.82 | 1.00 | 8 |
| long, no reload | 24 % → 24 % | 10.6 px | 0.82 | 1.00 | 54 | quarters: 0.17 → 0.24 → 0.17 → 0.24

Numbers say: light vs heavy: width 69.5 → 69.5 px, dark 0.81 → 0.82; pressure barely changes the width; the long stroke does not run out of paint.

## Brush Artist · Refs · #01 Henry Ward peach cloud
Gouache · 44 px · 44.3 s

![Brush Artist · Refs · #01 Henry Ward peach cloud](Brush-Artist-Refs-01-Henry-Ward-peach-cloud.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 13 % → 9 % | 37.9 px | 0.33 | 0.68 | 272 |
| heavy line | 14 % → 10 % | 41.1 px | 0.33 | 0.74 | 247 |
| pressure swell | 11 % → 9 % | 41.0 px | 0.33 | 0.80 | 140 |
| fast wave | 25 % → 13 % | 29.2 px | 0.33 | 0.51 | 488 |
| slow wave | 30 % → 15 % | 34.6 px | 0.33 | 0.50 | 938 |
| spiral | 41 % → 16 % | 27.0 px | 0.33 | 0.39 | 920 |
| loop | 25 % → 16 % | 33.0 px | 0.33 | 0.61 | 478 |
| tilted | 11 % → 11 % | 31.3 px | 0.33 | 1.00 | 321 |
| over the wet one | 24 % → 20 % | 36.1 px | 0.33 | 0.85 | 265 |
| long, no reload | 44 % → 18 % | 19.8 px | 0.33 | 0.41 | 1287 | quarters: 0.01 → 0.02 → 0.02 → 0.02

Numbers say: light vs heavy: width 37.9 → 41.1 px, dark 0.33 → 0.33; pressure barely changes the width; the long stroke does not run out of paint.

## Brush Artist · Refs · #02 Henry Ward cream strokes
Gouache · 46 px · 46.7 s

![Brush Artist · Refs · #02 Henry Ward cream strokes](Brush-Artist-Refs-02-Henry-Ward-cream-strokes.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 13 % → 10 % | 37.9 px | 0.41 | 0.73 | 179 |
| heavy line | 14 % → 12 % | 40.9 px | 0.41 | 0.82 | 218 |
| pressure swell | 11 % → 10 % | 41.1 px | 0.42 | 0.88 | 177 |
| fast wave | 25 % → 13 % | 28.7 px | 0.41 | 0.51 | 532 |
| slow wave | 29 % → 15 % | 34.0 px | 0.41 | 0.51 | 960 |
| spiral | 40 % → 16 % | 26.6 px | 0.41 | 0.40 | 1188 |
| loop | 25 % → 16 % | 32.6 px | 0.41 | 0.64 | 534 |
| tilted | 11 % → 11 % | 30.7 px | 0.41 | 1.00 | 220 |
| over the wet one | 24 % → 21 % | 36.1 px | 0.41 | 0.86 | 180 |
| long, no reload | 44 % → 19 % | 19.6 px | 0.41 | 0.43 | 1372 | quarters: 0.01 → 0.02 → 0.03 → 0.03

Numbers say: light vs heavy: width 37.9 → 40.9 px, dark 0.41 → 0.41; pressure barely changes the width; the long stroke does not run out of paint.

## Brush Artist · Refs · #03 Henry Ward navy contours
Heavy acrylic · 22 px · 18.1 s

![Brush Artist · Refs · #03 Henry Ward navy contours](Brush-Artist-Refs-03-Henry-Ward-navy-contours.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 7 % → 7 % | 21.6 px | 0.70 | 0.94 | 101 |
| heavy line | 8 % → 8 % | 23.5 px | 0.70 | 0.95 | 108 |
| pressure swell | 6 % → 6 % | 23.2 px | 0.73 | 0.94 | 79 |
| fast wave | 19 % → 12 % | 21.9 px | 0.72 | 0.65 | 285 |
| slow wave | 19 % → 13 % | 22.5 px | 0.72 | 0.68 | 570 |
| spiral | 30 % → 13 % | 19.5 px | 0.72 | 0.45 | 664 |
| loop | 17 % → 13 % | 21.5 px | 0.72 | 0.81 | 239 |
| tilted | 8 % → 8 % | 22.7 px | 0.71 | 1.00 | 143 |
| over the wet one | 16 % → 14 % | 21.3 px | 0.71 | 0.89 | 94 |
| long, no reload | 34 % → 13 % | 15.1 px | 0.72 | 0.40 | 574 | quarters: 0.35 → 0.29 → 0.19 → 0.07

Numbers say: light vs heavy: width 21.6 → 23.5 px, dark 0.70 → 0.70; pressure barely changes the width.

## Brush Artist · Refs · #04 Henry Ward grey cloud
Gouache · 50 px · 48.5 s

![Brush Artist · Refs · #04 Henry Ward grey cloud](Brush-Artist-Refs-04-Henry-Ward-grey-cloud.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 15 % → 11 % | 43.6 px | 0.32 | 0.73 | 201 |
| heavy line | 16 % → 13 % | 46.9 px | 0.32 | 0.79 | 241 |
| pressure swell | 12 % → 10 % | 46.8 px | 0.32 | 0.84 | 140 |
| fast wave | 29 % → 15 % | 32.9 px | 0.32 | 0.52 | 606 |
| slow wave | 34 % → 17 % | 39.2 px | 0.32 | 0.51 | 865 |
| spiral | 44 % → 18 % | 28.7 px | 0.32 | 0.42 | 1105 |
| loop | 29 % → 18 % | 37.7 px | 0.32 | 0.62 | 737 |
| tilted | 12 % → 12 % | 34.2 px | 0.32 | 1.00 | 231 |
| over the wet one | 27 % → 23 % | 41.1 px | 0.32 | 0.86 | 205 |
| long, no reload | 49 % → 21 % | 21.8 px | 0.32 | 0.44 | 1341 | quarters: 0.01 → 0.02 → 0.02 → 0.03

Numbers say: light vs heavy: width 43.6 → 46.9 px, dark 0.32 → 0.32; pressure barely changes the width; the long stroke does not run out of paint.

## Brush Artist · Refs · #05 Henry Ward green in rust loops
Heavy acrylic · 20 px · 20.4 s

![Brush Artist · Refs · #05 Henry Ward green in rust loops](Brush-Artist-Refs-05-Henry-Ward-green-in-rust-loops.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 7 % → 6 % | 19.5 px | 0.55 | 0.94 | 109 |
| heavy line | 7 % → 7 % | 21.4 px | 0.55 | 0.94 | 161 |
| pressure swell | 6 % → 5 % | 21.6 px | 0.57 | 0.92 | 113 |
| fast wave | 17 % → 11 % | 19.8 px | 0.56 | 0.64 | 460 |
| slow wave | 18 % → 12 % | 20.4 px | 0.55 | 0.65 | 530 |
| spiral | 27 % → 11 % | 17.9 px | 0.55 | 0.42 | 692 |
| loop | 15 % → 12 % | 19.5 px | 0.55 | 0.79 | 325 |
| tilted | 8 % → 8 % | 21.7 px | 0.55 | 1.00 | 191 |
| over the wet one | 15 % → 13 % | 19.3 px | 0.55 | 0.87 | 190 |
| long, no reload | 30 % → 12 % | 13.3 px | 0.56 | 0.39 | 692 | quarters: 0.25 → 0.18 → 0.10 → 0.02

Numbers say: light vs heavy: width 19.5 → 21.4 px, dark 0.55 → 0.55; pressure barely changes the width.

## Brush Artist · Refs · #06 Henry Ward scrubbed grey
Gouache · 50 px · 48.8 s

![Brush Artist · Refs · #06 Henry Ward scrubbed grey](Brush-Artist-Refs-06-Henry-Ward-scrubbed-grey.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 15 % → 11 % | 43.6 px | 0.34 | 0.73 | 335 |
| heavy line | 16 % → 13 % | 46.9 px | 0.34 | 0.79 | 240 |
| pressure swell | 12 % → 10 % | 46.8 px | 0.34 | 0.84 | 167 |
| fast wave | 29 % → 15 % | 32.9 px | 0.34 | 0.52 | 661 |
| slow wave | 34 % → 17 % | 39.2 px | 0.34 | 0.51 | 1122 |
| spiral | 44 % → 18 % | 28.7 px | 0.34 | 0.42 | 956 |
| loop | 29 % → 18 % | 37.7 px | 0.34 | 0.62 | 739 |
| tilted | 12 % → 12 % | 34.2 px | 0.34 | 1.00 | 296 |
| over the wet one | 27 % → 23 % | 41.1 px | 0.34 | 0.86 | 268 |
| long, no reload | 49 % → 21 % | 21.8 px | 0.34 | 0.44 | 1286 | quarters: 0.01 → 0.02 → 0.02 → 0.03

Numbers say: light vs heavy: width 43.6 → 46.9 px, dark 0.34 → 0.34; pressure barely changes the width; the long stroke does not run out of paint.

## Brush Artist · Refs · #07 Henry Ward blue L + black zigzag
Heavy acrylic · 34 px · 21.4 s

![Brush Artist · Refs · #07 Henry Ward blue L + black zigzag](Brush-Artist-Refs-07-Henry-Ward-blue-L-black-zigzag.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 11 % → 11 % | 33.2 px | 0.58 | 0.93 | 158 |
| heavy line | 12 % → 12 % | 35.9 px | 0.58 | 0.93 | 213 |
| pressure swell | 9 % → 9 % | 35.3 px | 0.59 | 0.94 | 99 |
| fast wave | 29 % → 20 % | 33.7 px | 0.58 | 0.68 | 392 |
| slow wave | 30 % → 21 % | 34.2 px | 0.58 | 0.72 | 516 |
| spiral | 47 % → 22 % | 31.3 px | 0.58 | 0.46 | 600 |
| loop | 25 % → 21 % | 32.7 px | 0.58 | 0.82 | 337 |
| tilted | 11 % → 11 % | 30.0 px | 0.58 | 1.00 | 197 |
| over the wet one | 22 % → 20 % | 31.8 px | 0.58 | 0.91 | 175 |
| long, no reload | 53 % → 22 % | 23.8 px | 0.59 | 0.42 | 877 | quarters: 0.40 → 0.32 → 0.21 → 0.10

Numbers say: light vs heavy: width 33.2 → 35.9 px, dark 0.58 → 0.58; pressure barely changes the width.

## Brush Artist · Refs · #08 Henry Ward olive bands
Gouache · 34 px · 31.8 s

![Brush Artist · Refs · #08 Henry Ward olive bands](Brush-Artist-Refs-08-Henry-Ward-olive-bands.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 4 % → 0 % | 12.2 px | 0.61 | 0.04 | 149 |
| heavy line | 7 % → 0 % | 19.3 px | 0.61 | 0.02 | 171 |
| pressure swell | 5 % → 0 % | 18.7 px | 0.61 | 0.03 | 90 |
| fast wave | 10 % → 0 % | 11.1 px | 0.61 | 0.02 | 299 |
| slow wave | 15 % → 1 % | 17.0 px | 0.61 | 0.06 | 632 |
| spiral | 19 % → 1 % | 12.7 px | 0.61 | 0.03 | 501 |
| loop | 12 % → 1 % | 15.3 px | 0.61 | 0.09 | 314 |
| tilted | 5 % → 5 % | 15.1 px | 0.61 | 0.96 | 175 |
| over the wet one | 11 % → 2 % | 16.9 px | 0.61 | 0.22 | 181 |
| long, no reload | 22 % → 2 % | 9.8 px | 0.61 | 0.09 | 1066 | quarters: 0.21 → 0.15 → 0.11 → 0.09

Numbers say: light vs heavy: width 12.2 → 19.3 px, dark 0.61 → 0.61.

## Brush Artist · Refs · #09 Henry Ward white loops
Gouache · 46 px · 53.1 s

![Brush Artist · Refs · #09 Henry Ward white loops](Brush-Artist-Refs-09-Henry-Ward-white-loops.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 13 % → 10 % | 37.9 px | 0.44 | 0.73 | 224 |
| heavy line | 14 % → 12 % | 40.9 px | 0.44 | 0.82 | 237 |
| pressure swell | 11 % → 10 % | 41.1 px | 0.44 | 0.88 | 242 |
| fast wave | 25 % → 13 % | 28.7 px | 0.43 | 0.51 | 562 |
| slow wave | 29 % → 15 % | 34.0 px | 0.43 | 0.51 | 934 |
| spiral | 40 % → 16 % | 26.6 px | 0.43 | 0.40 | 1065 |
| loop | 25 % → 16 % | 32.6 px | 0.43 | 0.64 | 501 |
| tilted | 11 % → 11 % | 30.7 px | 0.44 | 1.00 | 337 |
| over the wet one | 24 % → 21 % | 36.1 px | 0.44 | 0.86 | 306 |
| long, no reload | 44 % → 19 % | 19.6 px | 0.43 | 0.43 | 1384 | quarters: 0.01 → 0.02 → 0.03 → 0.03

Numbers say: light vs heavy: width 37.9 → 40.9 px, dark 0.44 → 0.44; pressure barely changes the width; the long stroke does not run out of paint.

## Brush Artist · Refs · #10 Henry Ward maroon loops
Heavy acrylic · 30 px · 25.4 s

![Brush Artist · Refs · #10 Henry Ward maroon loops](Brush-Artist-Refs-10-Henry-Ward-maroon-loops.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 10 % → 9 % | 28.0 px | 0.71 | 0.94 | 212 |
| heavy line | 10 % → 10 % | 30.3 px | 0.71 | 0.95 | 204 |
| pressure swell | 8 % → 8 % | 30.0 px | 0.73 | 0.94 | 173 |
| fast wave | 25 % → 17 % | 28.4 px | 0.73 | 0.70 | 451 |
| slow wave | 25 % → 18 % | 29.0 px | 0.72 | 0.73 | 602 |
| spiral | 39 % → 18 % | 26.0 px | 0.72 | 0.47 | 684 |
| loop | 21 % → 18 % | 27.6 px | 0.72 | 0.85 | 340 |
| tilted | 10 % → 10 % | 28.0 px | 0.72 | 1.00 | 210 |
| over the wet one | 20 % → 18 % | 27.0 px | 0.72 | 0.91 | 150 |
| long, no reload | 46 % → 18 % | 20.5 px | 0.73 | 0.40 | 946 | quarters: 0.44 → 0.38 → 0.31 → 0.22

Numbers say: light vs heavy: width 28.0 → 30.3 px, dark 0.71 → 0.71; pressure barely changes the width.

## Brush Artist · Refs · #11 Henry Ward purple spun balls
Heavy acrylic · 36 px · 28.0 s

![Brush Artist · Refs · #11 Henry Ward purple spun balls](Brush-Artist-Refs-11-Henry-Ward-purple-spun-balls.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 12 % → 11 % | 34.2 px | 0.71 | 0.96 | 157 |
| heavy line | 13 % → 12 % | 36.7 px | 0.71 | 0.95 | 164 |
| pressure swell | 10 % → 9 % | 36.2 px | 0.74 | 0.95 | 131 |
| fast wave | 30 % → 22 % | 34.6 px | 0.73 | 0.75 | 464 |
| slow wave | 30 % → 24 % | 35.1 px | 0.73 | 0.79 | 670 |
| spiral | 49 % → 24 % | 32.3 px | 0.73 | 0.50 | 1009 |
| loop | 26 % → 23 % | 33.4 px | 0.73 | 0.88 | 436 |
| tilted | 11 % → 11 % | 31.2 px | 0.73 | 1.00 | 352 |
| over the wet one | 23 % → 21 % | 32.3 px | 0.73 | 0.93 | 287 |
| long, no reload | 55 % → 24 % | 24.8 px | 0.73 | 0.44 | 1726 | quarters: 0.51 → 0.46 → 0.39 → 0.28

Numbers say: light vs heavy: width 34.2 → 36.7 px, dark 0.71 → 0.71; pressure barely changes the width.

## Brush Artist · Refs · #12 Henry Ward black-olive cage
Gouache · 28 px · 31.7 s

![Brush Artist · Refs · #12 Henry Ward black-olive cage](Brush-Artist-Refs-12-Henry-Ward-black-olive-cage.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 3 % → 0 % | 10.1 px | 0.65 | 0.08 | 172 |
| heavy line | 5 % → 0 % | 15.3 px | 0.65 | 0.08 | 217 |
| pressure swell | 4 % → 0 % | 14.9 px | 0.65 | 0.10 | 97 |
| fast wave | 8 % → 0 % | 8.9 px | 0.65 | 0.04 | 284 |
| slow wave | 12 % → 1 % | 13.6 px | 0.65 | 0.09 | 545 |
| spiral | 16 % → 1 % | 10.4 px | 0.65 | 0.04 | 497 |
| loop | 9 % → 2 % | 12.3 px | 0.65 | 0.17 | 331 |
| tilted | 5 % → 4 % | 13.0 px | 0.65 | 0.95 | 232 |
| over the wet one | 9 % → 3 % | 13.2 px | 0.65 | 0.27 | 134 |
| long, no reload | 18 % → 2 % | 8.3 px | 0.65 | 0.12 | 739 | quarters: 0.19 → 0.14 → 0.11 → 0.10

Numbers say: light vs heavy: width 10.1 → 15.3 px, dark 0.65 → 0.65.

## Brush Artist · Refs · #13 Henry Ward blue streaky form
Gouache · 50 px · 49.3 s

![Brush Artist · Refs · #13 Henry Ward blue streaky form](Brush-Artist-Refs-13-Henry-Ward-blue-streaky-form.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 15 % → 11 % | 43.6 px | 0.34 | 0.73 | 240 |
| heavy line | 16 % → 13 % | 46.9 px | 0.34 | 0.79 | 226 |
| pressure swell | 12 % → 10 % | 46.8 px | 0.34 | 0.84 | 236 |
| fast wave | 29 % → 15 % | 32.9 px | 0.34 | 0.52 | 621 |
| slow wave | 34 % → 17 % | 39.2 px | 0.34 | 0.51 | 1134 |
| spiral | 44 % → 18 % | 28.7 px | 0.34 | 0.42 | 883 |
| loop | 29 % → 18 % | 37.7 px | 0.34 | 0.62 | 651 |
| tilted | 12 % → 12 % | 34.2 px | 0.34 | 1.00 | 284 |
| over the wet one | 27 % → 23 % | 41.1 px | 0.34 | 0.86 | 297 |
| long, no reload | 49 % → 21 % | 21.8 px | 0.33 | 0.44 | 1401 | quarters: 0.01 → 0.02 → 0.02 → 0.03

Numbers say: light vs heavy: width 43.6 → 46.9 px, dark 0.34 → 0.34; pressure barely changes the width; the long stroke does not run out of paint.

## Brush Artist · Refs · #14 Henry Ward olive totem
Heavy acrylic · 48 px · 27.0 s

![Brush Artist · Refs · #14 Henry Ward olive totem](Brush-Artist-Refs-14-Henry-Ward-olive-totem.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 15 % → 15 % | 44.9 px | 0.31 | 0.95 | 312 |
| heavy line | 16 % → 16 % | 47.7 px | 0.31 | 0.95 | 300 |
| pressure swell | 13 % → 12 % | 47.1 px | 0.32 | 0.95 | 149 |
| fast wave | 38 % → 30 % | 44.0 px | 0.30 | 0.78 | 565 |
| slow wave | 39 % → 31 % | 44.6 px | 0.30 | 0.81 | 999 |
| spiral | 58 % → 32 % | 38.2 px | 0.30 | 0.55 | 948 |
| loop | 33 % → 29 % | 42.7 px | 0.30 | 0.89 | 386 |
| tilted | 13 % → 13 % | 37.6 px | 0.31 | 1.00 | 266 |
| over the wet one | 28 % → 26 % | 41.2 px | 0.31 | 0.93 | 223 |
| long, no reload | 68 % → 33 % | 30.3 px | 0.30 | 0.49 | 1636 | quarters: 0.25 → 0.18 → 0.09 → 0.03

Numbers say: light vs heavy: width 44.9 → 47.7 px, dark 0.31 → 0.31; pressure barely changes the width.

## Brush Artist · Refs · #15 Ultramarine brush script
Ink · 4 px · 31.4 s

![Brush Artist · Refs · #15 Ultramarine brush script](Brush-Artist-Refs-15-Ultramarine-brush-script.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 1 % → 3 % | 2.2 px | 0.55 | 3.90 | 32 |
| heavy line | 6 % → 6 % | 16.7 px | 0.58 | 0.99 | 73 |
| pressure swell | 3 % → 4 % | 12.1 px | 0.64 | 1.15 | 45 |
| fast wave | 9 % → 7 % | 10.6 px | 0.54 | 0.81 | 131 |
| slow wave | 7 % → 7 % | 8.4 px | 0.54 | 0.93 | 115 |
| spiral | 11 % → 7 % | 7.2 px | 0.52 | 0.66 | 254 |
| loop | 7 % → 7 % | 9.2 px | 0.53 | 0.98 | 127 |
| tilted | 3 % → 3 % | 8.2 px | 0.62 | 1.02 | 55 |
| over the wet one | 7 % → 7 % | 11.5 px | 0.62 | 1.05 | 55 |
| long, no reload | 16 % → 8 % | 7.3 px | 0.50 | 0.48 | 407 | quarters: 0.15 → 0.04 → 0.01 → 0.00

Numbers say: light vs heavy: width 2.2 → 16.7 px, dark 0.55 → 0.58; wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #18 Blue oil-stick scribbles
Pastel · 10 px · 13.5 s

![Brush Artist · Refs · #18 Blue oil-stick scribbles](Brush-Artist-Refs-18-Blue-oil-stick-scribbles.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 1 % → 1 % | 2.9 px | 0.52 | 1.00 | 51 |
| heavy line | 2 % → 2 % | 5.5 px | 0.53 | 1.00 | 37 |
| pressure swell | 1 % → 1 % | 5.0 px | 0.53 | 1.00 | 28 |
| fast wave | 4 % → 4 % | 4.8 px | 0.53 | 1.00 | 108 |
| slow wave | 4 % → 4 % | 4.4 px | 0.53 | 1.00 | 68 |
| spiral | 7 % → 7 % | 4.5 px | 0.52 | 1.00 | 147 |
| loop | 3 % → 3 % | 4.5 px | 0.52 | 1.00 | 67 |
| tilted | 2 % → 2 % | 4.7 px | 0.53 | 1.00 | 41 |
| over the wet one | 3 % → 3 % | 4.7 px | 0.53 | 1.00 | 32 |
| long, no reload | 10 % → 10 % | 4.4 px | 0.53 | 1.00 | 207 | quarters: 0.06 → 0.06 → 0.06 → 0.06

Numbers say: light vs heavy: width 2.9 → 5.5 px, dark 0.52 → 0.53; the long stroke does not run out of paint.

## Brush Artist · Refs · #20 Orange-red crayon scribble
Pastel · 14 px · 15.2 s

![Brush Artist · Refs · #20 Orange-red crayon scribble](Brush-Artist-Refs-20-Orange-red-crayon-scribble.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 1 % → 1 % | 4.0 px | 0.53 | 1.00 | 42 |
| heavy line | 3 % → 3 % | 8.0 px | 0.53 | 1.00 | 38 |
| pressure swell | 2 % → 2 % | 7.6 px | 0.53 | 1.00 | 22 |
| fast wave | 6 % → 6 % | 7.2 px | 0.53 | 1.00 | 85 |
| slow wave | 6 % → 6 % | 6.6 px | 0.53 | 1.00 | 94 |
| spiral | 9 % → 9 % | 6.2 px | 0.53 | 1.00 | 136 |
| loop | 5 % → 5 % | 6.2 px | 0.53 | 1.00 | 74 |
| tilted | 2 % → 2 % | 5.6 px | 0.53 | 1.00 | 35 |
| over the wet one | 4 % → 4 % | 6.6 px | 0.53 | 1.00 | 42 |
| long, no reload | 13 % → 13 % | 5.7 px | 0.53 | 1.00 | 211 | quarters: 0.07 → 0.07 → 0.08 → 0.08

Numbers say: light vs heavy: width 4.0 → 8.0 px, dark 0.53 → 0.53; the long stroke does not run out of paint.

## Brush Artist · Refs · #21 Gritty black contours
Gouache · 12 px · 28.3 s

![Brush Artist · Refs · #21 Gritty black contours](Brush-Artist-Refs-21-Gritty-black-contours.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 1 % → 0 % | 3.3 px | 0.81 | 0.08 | 85 |
| heavy line | 2 % → 0 % | 5.2 px | 0.81 | 0.03 | 312 |
| pressure swell | 1 % → 0 % | 5.4 px | 0.81 | 0.04 | 222 |
| fast wave | 2 % → 0 % | 2.7 px | 0.81 | 0.01 | 732 |
| slow wave | 4 % → 0 % | 4.4 px | 0.81 | 0.04 | 254 |
| spiral | 5 % → 0 % | 3.1 px | 0.81 | 0.02 | 423 |
| loop | 3 % → 0 % | 4.1 px | 0.81 | 0.02 | 206 |
| tilted | 2 % → 2 % | 4.8 px | 0.81 | 0.93 | 139 |
| over the wet one | 3 % → 0 % | 4.7 px | 0.81 | 0.11 | 95 |
| long, no reload | 6 % → 0 % | 2.7 px | 0.81 | 0.06 | 527 | quarters: 0.09 → 0.06 → 0.05 → 0.04

Numbers say: light vs heavy: width 3.3 → 5.2 px, dark 0.81 → 0.81.

## Brush Artist · Refs · #22 Bold black brush poster
Ink · 20 px · 38.4 s

![Brush Artist · Refs · #22 Bold black brush poster](Brush-Artist-Refs-22-Bold-black-brush-poster.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 3 % → 5 % | 9.6 px | 0.79 | 1.64 | 88 |
| heavy line | 15 % → 15 % | 44.6 px | 0.88 | 0.99 | 275 |
| pressure swell | 9 % → 9 % | 31.9 px | 0.87 | 1.04 | 82 |
| fast wave | 27 % → 27 % | 31.7 px | 0.87 | 0.98 | 192 |
| slow wave | 22 % → 22 % | 25.4 px | 0.87 | 0.98 | 298 |
| spiral | 34 % → 32 % | 22.4 px | 0.87 | 0.94 | 328 |
| loop | 20 % → 20 % | 26.4 px | 0.88 | 1.00 | 160 |
| tilted | 8 % → 8 % | 23.1 px | 0.88 | 1.01 | 68 |
| over the wet one | 19 % → 19 % | 30.4 px | 0.88 | 1.00 | 64 |
| long, no reload | 45 % → 38 % | 20.3 px | 0.86 | 0.83 | 429 | quarters: 0.54 → 0.45 → 0.35 → 0.26

Numbers say: light vs heavy: width 9.6 → 44.6 px, dark 0.79 → 0.88; wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #23 Dry white on orange + black line
Gouache · 50 px · 31.7 s

![Brush Artist · Refs · #23 Dry white on orange + black line](Brush-Artist-Refs-23-Dry-white-on-orange-black-line.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 5 % → 0 % | 15.7 px | 0.42 | 0.02 | 114 |
| heavy line | 9 % → 0 % | 25.3 px | 0.42 | 0.00 | 317 |
| pressure swell | 6 % → 0 % | 23.8 px | 0.41 | 0.00 | 178 |
| fast wave | 12 % → 0 % | 13.7 px | 0.41 | 0.01 | 365 |
| slow wave | 19 % → 0 % | 21.6 px | 0.41 | 0.02 | 736 |
| spiral | 24 % → 0 % | 15.6 px | 0.40 | 0.01 | 695 |
| loop | 15 % → 1 % | 19.8 px | 0.40 | 0.04 | 508 |
| tilted | 6 % → 6 % | 17.5 px | 0.40 | 0.94 | 241 |
| over the wet one | 14 % → 1 % | 20.6 px | 0.40 | 0.09 | 186 |
| long, no reload | 27 % → 1 % | 12.3 px | 0.40 | 0.05 | 1242 | quarters: 0.02 → 0.03 → 0.03 → 0.03

Numbers say: light vs heavy: width 15.7 → 25.3 px, dark 0.42 → 0.42; the long stroke does not run out of paint.

## Brush Artist · Refs · #24 Picasso flat oil
Oil · 34 px · 25.1 s

![Brush Artist · Refs · #24 Picasso flat oil](Brush-Artist-Refs-24-Picasso-flat-oil.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 11 % → 11 % | 32.4 px | 0.40 | 1.00 | 253 |
| heavy line | 12 % → 12 % | 35.2 px | 0.40 | 1.00 | 317 |
| pressure swell | 9 % → 9 % | 34.5 px | 0.41 | 1.00 | 175 |
| fast wave | 30 % → 30 % | 34.2 px | 0.41 | 1.00 | 633 |
| slow wave | 30 % → 30 % | 35.0 px | 0.41 | 1.00 | 889 |
| spiral | 51 % → 51 % | 33.8 px | 0.40 | 1.00 | 872 |
| loop | 25 % → 25 % | 32.7 px | 0.41 | 1.00 | 396 |
| tilted | 11 % → 11 % | 32.1 px | 0.40 | 1.00 | 241 |
| over the wet one | 23 % → 23 % | 30.8 px | 0.40 | 1.00 | 164 |
| long, no reload | 62 % → 62 % | 27.6 px | 0.39 | 1.00 | 1224 | quarters: 0.28 → 0.28 → 0.26 → 0.24

Numbers say: light vs heavy: width 32.4 → 35.2 px, dark 0.40 → 0.40; pressure barely changes the width.

## Brush Artist · Refs · #25 Yellow heavy flat stroke
Heavy acrylic · 110 px · 59.1 s

![Brush Artist · Refs · #25 Yellow heavy flat stroke](Brush-Artist-Refs-25-Yellow-heavy-flat-stroke.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 35 % → 36 % | 101.5 px | 0.30 | 1.02 | 867 |
| heavy line | 36 % → 35 % | 105.1 px | 0.31 | 0.97 | 1057 |
| pressure swell | 28 % → 29 % | 105.4 px | 0.30 | 1.04 | 498 |
| fast wave | 73 % → 76 % | 83.8 px | 0.31 | 1.05 | 1745 |
| slow wave | 73 % → 72 % | 84.7 px | 0.30 | 0.98 | 3135 |
| spiral | 86 % → 83 % | 56.7 px | 0.29 | 0.97 | 3689 |
| loop | 65 % → 64 % | 83.6 px | 0.31 | 0.99 | 1467 |
| tilted | 26 % → 26 % | 71.5 px | 0.30 | 1.00 | 834 |
| over the wet one | 55 % → 54 % | 83.2 px | 0.30 | 0.97 | 718 |
| long, no reload | 98 % → 97 % | 44.1 px | 0.30 | 0.99 | 4261 | quarters: 0.00 → 0.00 → 0.00 → 0.00

Numbers say: light vs heavy: width 101.5 → 105.1 px, dark 0.30 → 0.31; pressure barely changes the width; the long stroke does not run out of paint.

## Brush Artist · Refs · #27 Orange impasto swatch
Heavy acrylic · 60 px · 41.6 s

![Brush Artist · Refs · #27 Orange impasto swatch](Brush-Artist-Refs-27-Orange-impasto-swatch.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 20 % → 19 % | 56.8 px | 0.34 | 0.97 | 453 |
| heavy line | 20 % → 20 % | 59.5 px | 0.34 | 0.97 | 497 |
| pressure swell | 16 % → 15 % | 59.6 px | 0.36 | 0.97 | 383 |
| fast wave | 48 % → 47 % | 55.1 px | 0.35 | 0.98 | 801 |
| slow wave | 48 % → 47 % | 55.9 px | 0.35 | 0.98 | 1487 |
| spiral | 69 % → 62 % | 45.5 px | 0.34 | 0.91 | 1453 |
| loop | 42 % → 40 % | 53.9 px | 0.35 | 0.97 | 700 |
| tilted | 16 % → 16 % | 44.0 px | 0.35 | 1.00 | 438 |
| over the wet one | 34 % → 33 % | 50.9 px | 0.35 | 0.96 | 371 |
| long, no reload | 85 % → 75 % | 38.1 px | 0.35 | 0.88 | 2613 | quarters: 0.33 → 0.31 → 0.30 → 0.26

Numbers say: light vs heavy: width 56.8 → 59.5 px, dark 0.34 → 0.34; pressure barely changes the width.

## Brush Artist · Refs · #28 Miles Davis black lines
Ink · 22 px · 44.6 s

![Brush Artist · Refs · #28 Miles Davis black lines](Brush-Artist-Refs-28-Miles-Davis-black-lines.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 4 % → 6 % | 12.3 px | 0.81 | 1.49 | 79 |
| heavy line | 17 % → 17 % | 49.0 px | 0.88 | 0.99 | 159 |
| pressure swell | 10 % → 10 % | 35.9 px | 0.87 | 1.03 | 93 |
| fast wave | 31 % → 30 % | 35.5 px | 0.87 | 0.98 | 376 |
| slow wave | 25 % → 25 % | 28.7 px | 0.87 | 0.99 | 350 |
| spiral | 39 % → 37 % | 25.5 px | 0.87 | 0.95 | 439 |
| loop | 23 % → 23 % | 29.6 px | 0.88 | 1.00 | 243 |
| tilted | 9 % → 9 % | 25.3 px | 0.88 | 1.01 | 105 |
| over the wet one | 21 % → 21 % | 34.1 px | 0.88 | 1.00 | 124 |
| long, no reload | 51 % → 43 % | 22.9 px | 0.86 | 0.84 | 638 | quarters: 0.59 → 0.51 → 0.40 → 0.31

Numbers say: light vs heavy: width 12.3 → 49.0 px, dark 0.81 → 0.88.

## Brush Artist · Refs · #29 Shrigley magenta asterisk
Watercolor · 70 px · 41.2 s

![Brush Artist · Refs · #29 Shrigley magenta asterisk](Brush-Artist-Refs-29-Shrigley-magenta-asterisk.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 10 % → 13 % | 28.0 px | 0.65 | 1.36 | 96 |
| heavy line | 17 % → 18 % | 50.3 px | 0.64 | 1.03 | 186 |
| pressure swell | 11 % → 12 % | 41.1 px | 0.65 | 1.13 | 134 |
| fast wave | 38 % → 38 % | 43.8 px | 0.64 | 1.01 | 365 |
| slow wave | 35 % → 39 % | 41.0 px | 0.65 | 1.10 | 487 |
| spiral | 61 % → 61 % | 40.0 px | 0.64 | 1.01 | 618 |
| loop | 31 % → 32 % | 40.2 px | 0.65 | 1.03 | 287 |
| tilted | 18 % → 18 % | 49.0 px | 0.65 | 1.00 | 238 |
| over the wet one | 31 % → 34 % | 38.4 px | 0.65 | 1.07 | 200 |
| long, no reload | 75 % → 75 % | 33.6 px | 0.64 | 1.00 | 1296 | quarters: 0.55 → 0.53 → 0.52 → 0.49

Numbers say: light vs heavy: width 28.0 → 50.3 px, dark 0.65 → 0.64; the long stroke does not run out of paint.

## Brush Artist · Refs · #30 Red gouache face patch
Gouache · 60 px · 49.9 s

![Brush Artist · Refs · #30 Red gouache face patch](Brush-Artist-Refs-30-Red-gouache-face-patch.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 16 % → 15 % | 47.0 px | 0.49 | 0.91 | 189 |
| heavy line | 25 % → 20 % | 74.0 px | 0.49 | 0.80 | 291 |
| pressure swell | 19 % → 17 % | 72.7 px | 0.49 | 0.86 | 220 |
| fast wave | 49 % → 28 % | 56.2 px | 0.49 | 0.58 | 757 |
| slow wave | 48 % → 28 % | 55.4 px | 0.49 | 0.59 | 1079 |
| spiral | 60 % → 28 % | 39.4 px | 0.49 | 0.47 | 1332 |
| loop | 40 % → 29 % | 51.6 px | 0.49 | 0.74 | 432 |
| tilted | 16 % → 17 % | 46.0 px | 0.49 | 1.00 | 268 |
| over the wet one | 36 % → 32 % | 55.3 px | 0.49 | 0.89 | 221 |
| long, no reload | 67 % → 30 % | 30.1 px | 0.49 | 0.44 | 1475 | quarters: 0.43 → 0.39 → 0.32 → 0.26

Numbers say: light vs heavy: width 47.0 → 74.0 px, dark 0.49 → 0.49.

## Brush Artist · Refs · #31 Warhol blotted line
Ink · 6 px · 26.0 s

![Brush Artist · Refs · #31 Warhol blotted line](Brush-Artist-Refs-31-Warhol-blotted-line.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 1 % → 3 % | 2.7 px | 0.75 | 3.30 | 51 |
| heavy line | 7 % → 7 % | 20.7 px | 0.83 | 0.98 | 100 |
| pressure swell | 4 % → 4 % | 14.8 px | 0.84 | 1.12 | 57 |
| fast wave | 12 % → 9 % | 13.9 px | 0.82 | 0.76 | 165 |
| slow wave | 10 % → 8 % | 11.2 px | 0.80 | 0.84 | 164 |
| spiral | 15 % → 8 % | 9.7 px | 0.80 | 0.57 | 282 |
| loop | 9 % → 9 % | 11.9 px | 0.80 | 0.93 | 177 |
| tilted | 3 % → 3 % | 8.8 px | 0.84 | 1.03 | 68 |
| over the wet one | 8 % → 8 % | 14.4 px | 0.84 | 1.02 | 72 |
| long, no reload | 21 % → 9 % | 9.6 px | 0.78 | 0.43 | 296 | quarters: 0.25 → 0.13 → 0.05 → 0.01

Numbers say: light vs heavy: width 2.7 → 20.7 px, dark 0.75 → 0.83; wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #32 Thick orange swipes
Heavy acrylic · 90 px · 42.2 s

![Brush Artist · Refs · #32 Thick orange swipes](Brush-Artist-Refs-32-Thick-orange-swipes.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 29 % → 29 % | 83.1 px | 0.38 | 1.00 | 361 |
| heavy line | 30 % → 29 % | 86.4 px | 0.38 | 0.97 | 322 |
| pressure swell | 23 % → 23 % | 86.5 px | 0.38 | 1.01 | 238 |
| fast wave | 63 % → 65 % | 73.1 px | 0.38 | 1.03 | 854 |
| slow wave | 64 % → 63 % | 73.5 px | 0.38 | 0.98 | 1769 |
| spiral | 79 % → 77 % | 52.2 px | 0.38 | 0.98 | 2019 |
| loop | 57 % → 56 % | 73.4 px | 0.38 | 0.99 | 1106 |
| tilted | 21 % → 21 % | 59.3 px | 0.38 | 1.00 | 534 |
| over the wet one | 47 % → 45 % | 71.0 px | 0.38 | 0.97 | 460 |
| long, no reload | 95 % → 93 % | 42.8 px | 0.38 | 0.98 | 2616 | quarters: 0.38 → 0.38 → 0.37 → 0.35

Numbers say: light vs heavy: width 83.1 → 86.4 px, dark 0.38 → 0.38; pressure barely changes the width; the long stroke does not run out of paint.

## Brush Artist · Refs · #33 Red wet-in-wet band
Watercolor · 80 px · 65.8 s

![Brush Artist · Refs · #33 Red wet-in-wet band](Brush-Artist-Refs-33-Red-wet-in-wet-band.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 20 % → 35 % | 57.8 px | 0.54 | 1.75 | 132 |
| heavy line | 30 % → 42 % | 86.1 px | 0.58 | 1.41 | 337 |
| pressure swell | 19 % → 27 % | 71.8 px | 0.61 | 1.42 | 174 |
| fast wave | 59 % → 75 % | 68.1 px | 0.61 | 1.28 | 453 |
| slow wave | 57 % → 73 % | 66.2 px | 0.63 | 1.28 | 1374 |
| spiral | 76 % → 86 % | 49.9 px | 0.64 | 1.14 | 1067 |
| loop | 52 % → 67 % | 67.4 px | 0.62 | 1.28 | 501 |
| tilted | 25 % → 26 % | 68.7 px | 0.59 | 1.07 | 363 |
| over the wet one | 49 % → 71 % | 69.5 px | 0.59 | 1.44 | 263 |
| long, no reload | 95 % → 99 % | 42.6 px | 0.67 | 1.04 | 2892 | quarters: 0.68 → 0.68 → 0.68 → 0.63

Numbers say: light vs heavy: width 57.8 → 86.1 px, dark 0.54 → 0.58; the long stroke does not run out of paint; wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #34 Magenta oil patches
Oil · 60 px · 28.6 s

![Brush Artist · Refs · #34 Magenta oil patches](Brush-Artist-Refs-34-Magenta-oil-patches.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 19 % → 19 % | 55.9 px | 0.61 | 1.00 | 292 |
| heavy line | 21 % → 21 % | 59.9 px | 0.61 | 1.00 | 278 |
| pressure swell | 16 % → 16 % | 58.9 px | 0.62 | 1.01 | 204 |
| fast wave | 48 % → 49 % | 55.5 px | 0.62 | 1.02 | 634 |
| slow wave | 48 % → 48 % | 55.8 px | 0.62 | 1.00 | 1224 |
| spiral | 70 % → 70 % | 46.3 px | 0.62 | 1.00 | 1349 |
| loop | 42 % → 42 % | 54.3 px | 0.62 | 1.00 | 767 |
| tilted | 17 % → 17 % | 46.9 px | 0.61 | 1.00 | 385 |
| over the wet one | 35 % → 35 % | 50.1 px | 0.61 | 1.00 | 405 |
| long, no reload | 86 % → 86 % | 38.7 px | 0.62 | 1.00 | 2225 | quarters: 0.59 → 0.58 → 0.57 → 0.52

Numbers say: light vs heavy: width 55.9 → 59.9 px, dark 0.61 → 0.61; pressure barely changes the width; the long stroke does not run out of paint.

## Brush Artist · Refs · #35 Red band with runs
Watercolor · 70 px · 60.7 s

![Brush Artist · Refs · #35 Red band with runs](Brush-Artist-Refs-35-Red-band-with-runs.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 21 % → 38 % | 60.9 px | 0.44 | 1.80 | 126 |
| heavy line | 30 % → 45 % | 87.5 px | 0.47 | 1.49 | 243 |
| pressure swell | 17 % → 25 % | 63.3 px | 0.53 | 1.49 | 139 |
| fast wave | 57 % → 74 % | 65.6 px | 0.50 | 1.31 | 695 |
| slow wave | 54 % → 72 % | 62.2 px | 0.54 | 1.33 | 945 |
| spiral | 75 % → 90 % | 49.3 px | 0.55 | 1.20 | 907 |
| loop | 55 % → 77 % | 71.4 px | 0.50 | 1.39 | 362 |
| tilted | 25 % → 29 % | 70.1 px | 0.49 | 1.17 | 303 |
| over the wet one | 51 % → 78 % | 71.2 px | 0.49 | 1.53 | 219 |
| long, no reload | 93 % → 99 % | 41.8 px | 0.58 | 1.06 | 1907 | quarters: 0.60 → 0.60 → 0.59 → 0.56

Numbers say: light vs heavy: width 60.9 → 87.5 px, dark 0.44 → 0.47; the long stroke does not run out of paint; wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #36 Magenta letters flat brush
Gouache · 36 px · 40.7 s

![Brush Artist · Refs · #36 Magenta letters flat brush](Brush-Artist-Refs-36-Magenta-letters-flat-brush.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 10 % → 10 % | 29.1 px | 0.45 | 0.98 | 79 |
| heavy line | 17 % → 14 % | 49.1 px | 0.45 | 0.85 | 138 |
| pressure swell | 13 % → 12 % | 49.4 px | 0.45 | 0.89 | 82 |
| fast wave | 35 % → 19 % | 41.0 px | 0.45 | 0.54 | 303 |
| slow wave | 35 % → 19 % | 40.0 px | 0.45 | 0.54 | 612 |
| spiral | 46 % → 19 % | 30.5 px | 0.45 | 0.42 | 699 |
| loop | 27 % → 20 % | 35.4 px | 0.45 | 0.72 | 273 |
| tilted | 11 % → 11 % | 30.0 px | 0.45 | 1.00 | 184 |
| over the wet one | 24 % → 23 % | 38.1 px | 0.45 | 0.92 | 130 |
| long, no reload | 47 % → 19 % | 20.9 px | 0.45 | 0.40 | 769 | quarters: 0.29 → 0.26 → 0.22 → 0.18

Numbers say: light vs heavy: width 29.1 → 49.1 px, dark 0.45 → 0.45.

## Brush Artist · Refs · #37 Oil still life dabs
Oil · 40 px · 19.5 s

![Brush Artist · Refs · #37 Oil still life dabs](Brush-Artist-Refs-37-Oil-still-life-dabs.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 13 % → 13 % | 38.0 px | 0.38 | 1.00 | 192 |
| heavy line | 14 % → 14 % | 41.1 px | 0.38 | 1.00 | 183 |
| pressure swell | 11 % → 11 % | 40.2 px | 0.40 | 1.00 | 143 |
| fast wave | 34 % → 34 % | 39.9 px | 0.39 | 1.00 | 611 |
| slow wave | 35 % → 35 % | 40.2 px | 0.39 | 1.00 | 1177 |
| spiral | 59 % → 59 % | 38.7 px | 0.38 | 1.00 | 774 |
| loop | 29 % → 29 % | 37.8 px | 0.39 | 1.00 | 508 |
| tilted | 13 % → 13 % | 36.3 px | 0.39 | 1.00 | 202 |
| over the wet one | 26 % → 26 % | 35.8 px | 0.39 | 1.00 | 149 |
| long, no reload | 69 % → 69 % | 30.9 px | 0.37 | 1.00 | 1248 | quarters: 0.31 → 0.30 → 0.28 → 0.24

Numbers say: light vs heavy: width 38.0 → 41.1 px, dark 0.38 → 0.38; pressure barely changes the width.

## Brush Artist · Refs · #38 Sanguine drawing
Pastel · 6 px · 12.8 s

![Brush Artist · Refs · #38 Sanguine drawing](Brush-Artist-Refs-38-Sanguine-drawing.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 1 % → 1 % | 2.0 px | 0.61 | 1.00 | 25 |
| heavy line | 1 % → 1 % | 3.5 px | 0.62 | 1.00 | 17 |
| pressure swell | 1 % → 1 % | 3.3 px | 0.62 | 1.00 | 14 |
| fast wave | 3 % → 3 % | 3.2 px | 0.61 | 1.00 | 53 |
| slow wave | 3 % → 3 % | 3.0 px | 0.61 | 1.00 | 62 |
| spiral | 4 % → 4 % | 2.9 px | 0.61 | 1.00 | 80 |
| loop | 2 % → 2 % | 3.0 px | 0.61 | 1.00 | 70 |
| tilted | 1 % → 1 % | 3.4 px | 0.62 | 1.00 | 46 |
| over the wet one | 2 % → 2 % | 2.9 px | 0.62 | 1.00 | 35 |
| long, no reload | 7 % → 7 % | 3.0 px | 0.61 | 1.00 | 181 | quarters: 0.04 → 0.05 → 0.05 → 0.05

Numbers say: light vs heavy: width 2.0 → 3.5 px, dark 0.61 → 0.62; the long stroke does not run out of paint.

## Brush Artist · Refs · #39 Very thick impasto
Heavy acrylic · 60 px · 25.2 s

![Brush Artist · Refs · #39 Very thick impasto](Brush-Artist-Refs-39-Very-thick-impasto.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 20 % → 19 % | 56.9 px | 0.60 | 0.97 | 214 |
| heavy line | 21 % → 20 % | 59.6 px | 0.60 | 0.97 | 218 |
| pressure swell | 16 % → 15 % | 59.7 px | 0.62 | 0.97 | 152 |
| fast wave | 48 % → 47 % | 55.2 px | 0.62 | 0.98 | 879 |
| slow wave | 49 % → 47 % | 56.0 px | 0.62 | 0.98 | 1243 |
| spiral | 69 % → 65 % | 45.6 px | 0.62 | 0.93 | 1136 |
| loop | 42 % → 41 % | 54.0 px | 0.62 | 0.97 | 433 |
| tilted | 16 % → 16 % | 44.1 px | 0.61 | 1.00 | 305 |
| over the wet one | 34 % → 33 % | 51.0 px | 0.61 | 0.97 | 215 |
| long, no reload | 85 % → 79 % | 38.3 px | 0.62 | 0.93 | 1297 | quarters: 0.58 → 0.57 → 0.55 → 0.52

Numbers say: light vs heavy: width 56.9 → 59.6 px, dark 0.60 → 0.60; pressure barely changes the width; the long stroke does not run out of paint.

## Brush Artist · Refs · #40 Watercolour blooms
Watercolor · 90 px · 52.3 s

![Brush Artist · Refs · #40 Watercolour blooms](Brush-Artist-Refs-40-Watercolour-blooms.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 23 % → 38 % | 65.7 px | 0.09 | 1.68 | 159 |
| heavy line | 34 % → 46 % | 97.7 px | 0.10 | 1.36 | 337 |
| pressure swell | 23 % → 30 % | 84.4 px | 0.12 | 1.34 | 200 |
| fast wave | 64 % → 79 % | 74.5 px | 0.11 | 1.23 | 509 |
| slow wave | 63 % → 77 % | 72.9 px | 0.15 | 1.22 | 968 |
| spiral | 80 % → 89 % | 52.6 px | 0.15 | 1.12 | 1234 |
| loop | 57 % → 70 % | 73.8 px | 0.13 | 1.24 | 426 |
| tilted | 27 % → 29 % | 76.6 px | 0.12 | 1.07 | 349 |
| over the wet one | 55 % → 77 % | 77.1 px | 0.12 | 1.40 | 244 |
| long, no reload | 97 % → 100 % | 43.6 px | 0.17 | 1.02 | 1604 | quarters: 0.21 → 0.19 → 0.17 → 0.12

Numbers say: light vs heavy: width 65.7 → 97.7 px, dark 0.09 → 0.10; wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #41 Coloured pencil hatching
Pastel · 4 px · 9.9 s

![Brush Artist · Refs · #41 Coloured pencil hatching](Brush-Artist-Refs-41-Coloured-pencil-hatching.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 1 % → 1 % | 1.6 px | 0.42 | 1.00 | 16 |
| heavy line | 1 % → 1 % | 2.6 px | 0.43 | 1.00 | 16 |
| pressure swell | 1 % → 1 % | 2.1 px | 0.43 | 1.00 | 9 |
| fast wave | 2 % → 2 % | 2.2 px | 0.42 | 1.00 | 32 |
| slow wave | 2 % → 2 % | 2.1 px | 0.43 | 1.00 | 34 |
| spiral | 3 % → 3 % | 2.1 px | 0.43 | 1.00 | 62 |
| loop | 2 % → 2 % | 2.2 px | 0.43 | 1.00 | 31 |
| tilted | 1 % → 1 % | 3.0 px | 0.42 | 1.00 | 17 |
| over the wet one | 2 % → 2 % | 2.2 px | 0.42 | 1.00 | 15 |
| long, no reload | 5 % → 5 % | 2.3 px | 0.43 | 1.00 | 94 | quarters: 0.02 → 0.02 → 0.02 → 0.03

Numbers say: light vs heavy: width 1.6 → 2.6 px, dark 0.42 → 0.43; the long stroke does not run out of paint.

## Brush Artist · Refs · #42 Oil pastel shaggy
Pastel · 18 px · 11.1 s

![Brush Artist · Refs · #42 Oil pastel shaggy](Brush-Artist-Refs-42-Oil-pastel-shaggy.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 2 % → 2 % | 5.1 px | 0.35 | 1.00 | 21 |
| heavy line | 4 % → 4 % | 10.7 px | 0.36 | 1.00 | 31 |
| pressure swell | 3 % → 3 % | 9.5 px | 0.36 | 1.00 | 20 |
| fast wave | 8 % → 8 % | 9.0 px | 0.36 | 1.00 | 70 |
| slow wave | 7 % → 7 % | 8.2 px | 0.36 | 1.00 | 115 |
| spiral | 12 % → 12 % | 7.7 px | 0.36 | 1.00 | 142 |
| loop | 6 % → 6 % | 7.9 px | 0.36 | 1.00 | 73 |
| tilted | 2 % → 2 % | 6.9 px | 0.36 | 1.00 | 38 |
| over the wet one | 6 % → 6 % | 8.5 px | 0.36 | 1.00 | 37 |
| long, no reload | 15 % → 15 % | 6.9 px | 0.36 | 1.00 | 183 | quarters: 0.00 → 0.00 → 0.00 → 0.00

Numbers say: light vs heavy: width 5.1 → 10.7 px, dark 0.35 → 0.36; the long stroke does not run out of paint.

## Brush Artist · Refs · #43 Dragged black ink blocks
Gouache · 70 px · 30.0 s

![Brush Artist · Refs · #43 Dragged black ink blocks](Brush-Artist-Refs-43-Dragged-black-ink-blocks.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 11 % → 0 % | 31.1 px | 0.65 | 0.03 | 147 |
| heavy line | 16 % → 1 % | 46.9 px | 0.65 | 0.08 | 511 |
| pressure swell | 12 % → 1 % | 44.8 px | 0.65 | 0.11 | 294 |
| fast wave | 22 % → 2 % | 25.8 px | 0.65 | 0.09 | 692 |
| slow wave | 34 % → 4 % | 39.7 px | 0.65 | 0.13 | 1055 |
| spiral | 40 % → 4 % | 26.3 px | 0.65 | 0.11 | 1045 |
| loop | 28 % → 4 % | 36.5 px | 0.65 | 0.14 | 491 |
| tilted | 10 % → 10 % | 28.3 px | 0.65 | 0.98 | 260 |
| over the wet one | 24 % → 9 % | 40.0 px | 0.65 | 0.36 | 274 |
| long, no reload | 47 % → 8 % | 20.9 px | 0.65 | 0.16 | 1594 | quarters: 0.45 → 0.36 → 0.28 → 0.23

Numbers say: light vs heavy: width 31.1 → 46.9 px, dark 0.65 → 0.65.

## Brush Artist · Refs · #44 Blue looping ribbon
Oil · 80 px · 26.8 s

![Brush Artist · Refs · #44 Blue looping ribbon](Brush-Artist-Refs-44-Blue-looping-ribbon.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 26 % → 27 % | 75.0 px | 0.72 | 1.04 | 300 |
| heavy line | 27 % → 27 % | 79.6 px | 0.72 | 1.00 | 413 |
| pressure swell | 21 % → 22 % | 78.2 px | 0.72 | 1.03 | 246 |
| fast wave | 61 % → 64 % | 70.3 px | 0.73 | 1.05 | 860 |
| slow wave | 61 % → 61 % | 70.0 px | 0.73 | 1.00 | 1410 |
| spiral | 78 % → 78 % | 51.3 px | 0.73 | 1.00 | 1626 |
| loop | 54 % → 54 % | 69.7 px | 0.73 | 1.00 | 903 |
| tilted | 21 % → 21 % | 57.3 px | 0.72 | 1.00 | 525 |
| over the wet one | 44 % → 44 % | 64.9 px | 0.72 | 1.00 | 314 |
| long, no reload | 96 % → 96 % | 42.8 px | 0.73 | 1.00 | 2146 | quarters: 0.72 → 0.73 → 0.73 → 0.69

Numbers say: light vs heavy: width 75.0 → 79.6 px, dark 0.72 → 0.72; pressure barely changes the width; the long stroke does not run out of paint.

## Brush Artist · Refs · #45 Soft pastel pepper
Pastel · 40 px · 12.0 s

![Brush Artist · Refs · #45 Soft pastel pepper](Brush-Artist-Refs-45-Soft-pastel-pepper.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 4 % → 4 % | 11.3 px | 0.53 | 1.00 | 45 |
| heavy line | 8 % → 8 % | 23.0 px | 0.53 | 1.00 | 49 |
| pressure swell | 5 % → 5 % | 19.5 px | 0.53 | 1.00 | 40 |
| fast wave | 17 % → 17 % | 19.4 px | 0.53 | 1.00 | 125 |
| slow wave | 15 % → 15 % | 17.1 px | 0.53 | 1.00 | 221 |
| spiral | 25 % → 25 % | 16.3 px | 0.53 | 1.00 | 224 |
| loop | 12 % → 12 % | 16.1 px | 0.53 | 1.00 | 112 |
| tilted | 5 % → 5 % | 12.8 px | 0.53 | 1.00 | 63 |
| over the wet one | 11 % → 11 % | 17.7 px | 0.53 | 1.00 | 51 |
| long, no reload | 30 % → 30 % | 13.6 px | 0.53 | 1.00 | 320 | quarters: 0.18 → 0.18 → 0.18 → 0.18

Numbers say: light vs heavy: width 11.3 → 23.0 px, dark 0.53 → 0.53; the long stroke does not run out of paint.

## Brush Artist · Refs · #46 Red-brown ink lips
Watercolor · 50 px · 44.6 s

![Brush Artist · Refs · #46 Red-brown ink lips](Brush-Artist-Refs-46-Red-brown-ink-lips.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 12 % → 26 % | 35.0 px | 0.63 | 2.13 | 67 |
| heavy line | 19 % → 32 % | 55.3 px | 0.63 | 1.67 | 100 |
| pressure swell | 12 % → 21 % | 43.9 px | 0.67 | 1.77 | 69 |
| fast wave | 41 % → 62 % | 47.2 px | 0.66 | 1.52 | 207 |
| slow wave | 39 % → 60 % | 44.9 px | 0.69 | 1.55 | 352 |
| spiral | 63 % → 77 % | 41.8 px | 0.70 | 1.22 | 373 |
| loop | 35 % → 54 % | 45.3 px | 0.67 | 1.54 | 284 |
| tilted | 16 % → 17 % | 44.3 px | 0.65 | 1.10 | 132 |
| over the wet one | 34 % → 53 % | 49.4 px | 0.65 | 1.58 | 86 |
| long, no reload | 79 % → 96 % | 35.4 px | 0.70 | 1.21 | 997 | quarters: 0.71 → 0.71 → 0.70 → 0.66

Numbers say: light vs heavy: width 35.0 → 55.3 px, dark 0.63 → 0.63; the long stroke does not run out of paint; wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #47 Pink knife slabs
Heavy acrylic · 90 px · 33.1 s

![Brush Artist · Refs · #47 Pink knife slabs](Brush-Artist-Refs-47-Pink-knife-slabs.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 28 % → 27 % | 81.1 px | 0.29 | 0.97 | 206 |
| heavy line | 29 % → 28 % | 83.5 px | 0.29 | 0.97 | 230 |
| pressure swell | 22 % → 22 % | 83.4 px | 0.29 | 1.01 | 153 |
| fast wave | 61 % → 60 % | 70.3 px | 0.28 | 0.99 | 538 |
| slow wave | 61 % → 59 % | 71.0 px | 0.27 | 0.96 | 1189 |
| spiral | 76 % → 57 % | 50.1 px | 0.27 | 0.76 | 1043 |
| loop | 55 % → 54 % | 71.8 px | 0.28 | 0.97 | 618 |
| tilted | 21 % → 21 % | 59.3 px | 0.29 | 1.00 | 502 |
| over the wet one | 46 % → 44 % | 68.0 px | 0.29 | 0.96 | 466 |
| long, no reload | 92 % → 76 % | 41.4 px | 0.26 | 0.82 | 1715 | quarters: 0.00 → 0.00 → 0.00 → 0.00

Numbers say: light vs heavy: width 81.1 → 83.5 px, dark 0.29 → 0.29; pressure barely changes the width; the long stroke does not run out of paint.

## Brush Artist · Refs · #48 Black bands with drips
Gouache · 70 px · 46.0 s

![Brush Artist · Refs · #48 Black bands with drips](Brush-Artist-Refs-48-Black-bands-with-drips.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 20 % → 18 % | 58.9 px | 0.68 | 0.90 | 290 |
| heavy line | 30 % → 26 % | 86.3 px | 0.68 | 0.86 | 422 |
| pressure swell | 23 % → 21 % | 86.6 px | 0.68 | 0.91 | 154 |
| fast wave | 55 % → 37 % | 63.8 px | 0.68 | 0.67 | 572 |
| slow wave | 55 % → 36 % | 63.2 px | 0.68 | 0.66 | 1576 |
| spiral | 65 % → 35 % | 43.0 px | 0.68 | 0.53 | 913 |
| loop | 46 % → 38 % | 60.0 px | 0.68 | 0.82 | 515 |
| tilted | 20 % → 20 % | 55.8 px | 0.68 | 1.01 | 282 |
| over the wet one | 43 % → 39 % | 65.0 px | 0.68 | 0.90 | 213 |
| long, no reload | 75 % → 37 % | 33.6 px | 0.68 | 0.50 | 1478 | quarters: 0.63 → 0.60 → 0.53 → 0.44

Numbers say: light vs heavy: width 58.9 → 86.3 px, dark 0.68 → 0.68.

## Brush Artist · Refs · #49 Magenta letters round brush
Ink · 30 px · 29.4 s

![Brush Artist · Refs · #49 Magenta letters round brush](Brush-Artist-Refs-49-Magenta-letters-round-brush.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 6 % → 8 % | 17.5 px | 0.50 | 1.29 | 64 |
| heavy line | 21 % → 21 % | 62.0 px | 0.51 | 0.99 | 110 |
| pressure swell | 12 % → 13 % | 46.3 px | 0.52 | 1.02 | 72 |
| fast wave | 39 % → 38 % | 44.8 px | 0.51 | 0.99 | 211 |
| slow wave | 32 % → 31 % | 36.7 px | 0.51 | 0.99 | 351 |
| spiral | 50 % → 49 % | 33.2 px | 0.51 | 0.97 | 296 |
| loop | 29 % → 29 % | 37.8 px | 0.51 | 1.00 | 197 |
| tilted | 11 % → 11 % | 31.0 px | 0.52 | 1.01 | 102 |
| over the wet one | 26 % → 26 % | 42.0 px | 0.52 | 1.01 | 100 |
| long, no reload | 62 % → 56 % | 27.7 px | 0.50 | 0.91 | 449 | quarters: 0.41 → 0.36 → 0.30 → 0.25

Numbers say: light vs heavy: width 17.5 → 62.0 px, dark 0.50 → 0.51.

## Brush Artist · Refs · #50 Thick swipes on photo
Heavy acrylic · 40 px · 17.1 s

![Brush Artist · Refs · #50 Thick swipes on photo](Brush-Artist-Refs-50-Thick-swipes-on-photo.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 13 % → 13 % | 38.1 px | 0.27 | 0.96 | 121 |
| heavy line | 14 % → 13 % | 40.2 px | 0.27 | 0.96 | 117 |
| pressure swell | 11 % → 10 % | 40.1 px | 0.25 | 0.95 | 90 |
| fast wave | 33 % → 31 % | 38.3 px | 0.25 | 0.93 | 302 |
| slow wave | 34 % → 32 % | 39.1 px | 0.26 | 0.95 | 505 |
| spiral | 58 % → 46 % | 38.5 px | 0.25 | 0.80 | 512 |
| loop | 28 % → 27 % | 36.9 px | 0.26 | 0.95 | 266 |
| tilted | 12 % → 12 % | 34.1 px | 0.26 | 1.00 | 138 |
| over the wet one | 25 % → 24 % | 35.3 px | 0.26 | 0.95 | 124 |
| long, no reload | 66 % → 46 % | 29.6 px | 0.24 | 0.69 | 747 | quarters: 0.00 → 0.00 → 0.00 → 0.00

Numbers say: light vs heavy: width 38.1 → 40.2 px, dark 0.27 → 0.27; pressure barely changes the width; the long stroke does not run out of paint.

## Brush Artist · Refs · Drag #e8b4a8
Gouache · 40 px · 19.2 s

![Brush Artist · Refs · Drag #e8b4a8](Brush-Artist-Refs-Drag-e8b4a8.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 2 % → 0 % | 5.0 px | 0.00 | 0.00 | 98 |
| heavy line | 3 % → 0 % | 8.7 px | 0.00 | 0.00 | 108 |
| pressure swell | 2 % → 0 % | 9.1 px | 0.00 | 0.00 | 77 |
| fast wave | 3 % → 0 % | 3.4 px | 0.00 | 0.00 | 259 |
| slow wave | 9 % → 0 % | 10.9 px | 0.00 | 0.00 | 489 |
| spiral | 10 % → 0 % | 6.9 px | 0.00 | 0.00 | 474 |
| loop | 6 % → 0 % | 7.9 px | 0.34 | 0.01 | 244 |
| tilted | 2 % → 2 % | 6.3 px | 0.34 | 0.89 | 136 |
| over the wet one | 5 % → 0 % | 8.2 px | 0.34 | 0.02 | 127 |
| long, no reload | 12 % → 0 % | 5.4 px | 0.34 | 0.01 | 716 | quarters: 0.01 → 0.01 → 0.01 → 0.01

Numbers say: light vs heavy: width 5.0 → 8.7 px, dark 0.00 → 0.00; the long stroke does not run out of paint.

## Brush Artist · Refs · Drag #e8e4e0
Gouache · 40 px · 19.9 s

![Brush Artist · Refs · Drag #e8e4e0](Brush-Artist-Refs-Drag-e8e4e0.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 2 % → 0 % | 5.0 px | 0.00 | 0.00 | 122 |
| heavy line | 3 % → 0 % | 8.7 px | 0.00 | 0.00 | 116 |
| pressure swell | 2 % → 0 % | 9.1 px | 0.00 | 0.00 | 81 |
| fast wave | 3 % → 0 % | 3.4 px | 0.00 | 0.00 | 270 |
| slow wave | 9 % → 0 % | 10.9 px | 0.00 | 0.00 | 523 |
| spiral | 10 % → 0 % | 6.9 px | 0.00 | 0.00 | 644 |
| loop | 6 % → 0 % | 7.9 px | 0.42 | 0.01 | 245 |
| tilted | 2 % → 2 % | 6.3 px | 0.42 | 0.89 | 129 |
| over the wet one | 5 % → 0 % | 8.2 px | 0.42 | 0.02 | 114 |
| long, no reload | 12 % → 0 % | 5.4 px | 0.43 | 0.01 | 708 | quarters: 0.01 → 0.01 → 0.01 → 0.01

Numbers say: light vs heavy: width 5.0 → 8.7 px, dark 0.00 → 0.00; the long stroke does not run out of paint.

## Brush Artist · Refs · Finger
Pastel · 36 px · 24.1 s · over bands of wet oil paint and oil pastel in turn (it works on paint already there: look at what it does to the bands; covered counts the bands too)

![Brush Artist · Refs · Finger](Brush-Artist-Refs-Finger.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 25 % → 25 % | 73.8 px | 0.80 | 1.00 | 54 |
| heavy line | 27 % → 27 % | 78.6 px | 0.80 | 1.00 | 51 |
| pressure swell | 26 % → 26 % | 97.7 px | 0.80 | 1.00 | 38 |
| fast wave | 32 % → 32 % | 37.3 px | 0.78 | 1.00 | 126 |
| slow wave | 31 % → 31 % | 36.3 px | 0.78 | 1.00 | 248 |
| spiral | 38 % → 38 % | 25.2 px | 0.76 | 1.00 | 224 |
| loop | 30 % → 30 % | 39.4 px | 0.78 | 1.00 | 118 |
| tilted | 26 % → 26 % | 73.4 px | 0.78 | 1.00 | 65 |
| over the wet one | 29 % → 29 % | 6.8 px | 0.78 | 1.00 | 52 |
| long, no reload | 41 % → 41 % | 18.2 px | 0.76 | 1.00 | 320 | quarters: 0.25 → 0.37 → 0.34 → 0.39

Numbers say: light vs heavy: width 73.8 → 78.6 px, dark 0.80 → 0.80; pressure barely changes the width; the long stroke does not run out of paint.

## Brush Artist · Ink — wash
Watercolor · 38 px · 31.9 s

![Brush Artist · Ink — wash](Brush-Artist-Ink-wash.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 11 % → 11 % | 31.6 px | 0.38 | 1.04 | 85 |
| heavy line | 19 % → 19 % | 54.3 px | 0.32 | 1.03 | 96 |
| pressure swell | 12 % → 12 % | 45.1 px | 0.36 | 1.04 | 60 |
| fast wave | 39 % → 41 % | 45.5 px | 0.30 | 1.04 | 192 |
| slow wave | 37 % → 38 % | 42.9 px | 0.37 | 1.03 | 438 |
| spiral | 58 % → 60 % | 38.5 px | 0.30 | 1.04 | 314 |
| loop | 32 % → 33 % | 41.9 px | 0.35 | 1.02 | 273 |
| tilted | 13 % → 14 % | 36.9 px | 0.38 | 1.04 | 178 |
| over the wet one | 29 % → 30 % | 42.7 px | 0.38 | 1.04 | 136 |
| long, no reload | 67 % → 71 % | 29.9 px | 0.29 | 1.07 | 451 | quarters: 0.33 → 0.26 → 0.19 → 0.12

Numbers say: light vs heavy: width 31.6 → 54.3 px, dark 0.38 → 0.32.

## Brush Artist · Ink — brush line
Ink · 16 px · 25.8 s

![Brush Artist · Ink — brush line](Brush-Artist-Ink-brush-line.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 3 % → 5 % | 7.7 px | 0.78 | 1.81 | 86 |
| heavy line | 13 % → 13 % | 39.0 px | 0.88 | 0.99 | 144 |
| pressure swell | 8 % → 8 % | 28.4 px | 0.87 | 1.05 | 50 |
| fast wave | 24 % → 23 % | 28.0 px | 0.87 | 0.96 | 146 |
| slow wave | 20 % → 19 % | 22.6 px | 0.87 | 0.97 | 222 |
| spiral | 30 % → 27 % | 20.1 px | 0.86 | 0.89 | 255 |
| loop | 18 % → 18 % | 23.6 px | 0.88 | 1.00 | 129 |
| tilted | 7 % → 7 % | 20.5 px | 0.88 | 1.01 | 64 |
| over the wet one | 17 % → 17 % | 26.8 px | 0.88 | 1.00 | 63 |
| long, no reload | 42 % → 30 % | 18.9 px | 0.85 | 0.71 | 444 | quarters: 0.49 → 0.40 → 0.30 → 0.20

Numbers say: light vs heavy: width 7.7 → 39.0 px, dark 0.78 → 0.88; wet paint spreads well beyond the stroke.

## Brush Artist · Ink — dry brush
Gouache · 30 px · 19.6 s

![Brush Artist · Ink — dry brush](Brush-Artist-Ink-dry-brush.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 3 % → 0 % | 9.2 px | 0.77 | 0.00 | 60 |
| heavy line | 5 % → 0 % | 14.0 px | 0.00 | 0.00 | 115 |
| pressure swell | 4 % → 0 % | 13.5 px | 0.77 | 0.01 | 112 |
| fast wave | 7 % → 0 % | 8.0 px | 0.77 | 0.00 | 272 |
| slow wave | 11 % → 0 % | 12.2 px | 0.77 | 0.01 | 374 |
| spiral | 14 % → 0 % | 9.2 px | 0.77 | 0.01 | 357 |
| loop | 9 % → 0 % | 11.1 px | 0.77 | 0.02 | 224 |
| tilted | 4 % → 4 % | 11.2 px | 0.77 | 0.94 | 97 |
| over the wet one | 8 % → 1 % | 12.2 px | 0.77 | 0.10 | 97 |
| long, no reload | 16 % → 1 % | 7.2 px | 0.77 | 0.03 | 555 | quarters: 0.21 → 0.15 → 0.12 → 0.11

Numbers say: light vs heavy: width 9.2 → 14.0 px, dark 0.77 → 0.00.

## Brush Artist · Watercolour — blue
Watercolor · 40 px · 28.4 s

![Brush Artist · Watercolour — blue](Brush-Artist-Watercolour-blue.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 6 % → 10 % | 16.7 px | 0.25 | 1.71 | 31 |
| heavy line | 11 % → 12 % | 31.5 px | 0.25 | 1.13 | 76 |
| pressure swell | 7 % → 9 % | 25.4 px | 0.26 | 1.32 | 46 |
| fast wave | 24 % → 25 % | 27.8 px | 0.24 | 1.06 | 134 |
| slow wave | 22 % → 27 % | 25.9 px | 0.26 | 1.22 | 223 |
| spiral | 38 % → 41 % | 25.2 px | 0.22 | 1.08 | 215 |
| loop | 20 % → 22 % | 25.3 px | 0.26 | 1.13 | 122 |
| tilted | 12 % → 12 % | 33.3 px | 0.26 | 1.00 | 87 |
| over the wet one | 21 % → 24 % | 24.7 px | 0.26 | 1.15 | 58 |
| long, no reload | 52 % → 54 % | 23.1 px | 0.22 | 1.04 | 431 | quarters: 0.18 → 0.14 → 0.11 → 0.08

Numbers say: light vs heavy: width 16.7 → 31.5 px, dark 0.25 → 0.25; wet paint spreads well beyond the stroke.

## Brush Artist · Watercolour — violet
Watercolor · 40 px · 28.4 s

![Brush Artist · Watercolour — violet](Brush-Artist-Watercolour-violet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 6 % → 10 % | 16.7 px | 0.40 | 1.71 | 38 |
| heavy line | 11 % → 12 % | 31.5 px | 0.40 | 1.13 | 90 |
| pressure swell | 7 % → 9 % | 25.4 px | 0.41 | 1.32 | 39 |
| fast wave | 24 % → 25 % | 27.8 px | 0.38 | 1.06 | 138 |
| slow wave | 22 % → 27 % | 25.9 px | 0.41 | 1.22 | 225 |
| spiral | 38 % → 41 % | 25.2 px | 0.36 | 1.08 | 219 |
| loop | 20 % → 22 % | 25.3 px | 0.40 | 1.13 | 117 |
| tilted | 12 % → 12 % | 33.3 px | 0.40 | 1.00 | 92 |
| over the wet one | 21 % → 24 % | 24.7 px | 0.40 | 1.15 | 56 |
| long, no reload | 52 % → 54 % | 23.1 px | 0.34 | 1.04 | 480 | quarters: 0.28 → 0.22 → 0.18 → 0.14

Numbers say: light vs heavy: width 16.7 → 31.5 px, dark 0.40 → 0.40; wet paint spreads well beyond the stroke.

## Brush Artist · Watercolour — teal
Watercolor · 40 px · 28.9 s

![Brush Artist · Watercolour — teal](Brush-Artist-Watercolour-teal.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 6 % → 10 % | 16.7 px | 0.16 | 1.71 | 39 |
| heavy line | 11 % → 12 % | 31.5 px | 0.16 | 1.13 | 66 |
| pressure swell | 7 % → 9 % | 25.4 px | 0.17 | 1.32 | 47 |
| fast wave | 24 % → 25 % | 27.8 px | 0.15 | 1.06 | 137 |
| slow wave | 22 % → 27 % | 25.9 px | 0.17 | 1.22 | 224 |
| spiral | 38 % → 41 % | 25.2 px | 0.15 | 1.08 | 217 |
| loop | 20 % → 22 % | 25.3 px | 0.16 | 1.13 | 127 |
| tilted | 12 % → 12 % | 33.3 px | 0.16 | 1.00 | 95 |
| over the wet one | 21 % → 24 % | 24.7 px | 0.16 | 1.15 | 113 |
| long, no reload | 52 % → 54 % | 23.1 px | 0.14 | 1.04 | 516 | quarters: 0.11 → 0.09 → 0.07 → 0.06

Numbers say: light vs heavy: width 16.7 → 31.5 px, dark 0.16 → 0.16; wet paint spreads well beyond the stroke.

## Brush Artist · Gouache
Gouache · 30 px · 37.0 s

![Brush Artist · Gouache](Brush-Artist-Gouache.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 8 % → 8 % | 24.4 px | 0.27 | 0.97 | 87 |
| heavy line | 15 % → 12 % | 42.9 px | 0.27 | 0.78 | 145 |
| pressure swell | 11 % → 9 % | 41.1 px | 0.27 | 0.85 | 80 |
| fast wave | 30 % → 14 % | 35.0 px | 0.26 | 0.45 | 331 |
| slow wave | 29 % → 14 % | 34.0 px | 0.26 | 0.47 | 484 |
| spiral | 40 % → 14 % | 26.7 px | 0.26 | 0.35 | 483 |
| loop | 24 % → 15 % | 30.6 px | 0.26 | 0.62 | 236 |
| tilted | 10 % → 10 % | 27.5 px | 0.27 | 1.01 | 127 |
| over the wet one | 22 % → 19 % | 32.8 px | 0.27 | 0.89 | 108 |
| long, no reload | 43 % → 15 % | 19.1 px | 0.26 | 0.35 | 662 | quarters: 0.01 → 0.01 → 0.01 → 0.01

Numbers say: light vs heavy: width 24.4 → 42.9 px, dark 0.27 → 0.27; the long stroke does not run out of paint.

## Brush Artist · Oil — bristle
Oil · 30 px · 20.1 s

![Brush Artist · Oil — bristle](Brush-Artist-Oil-bristle.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 9 % → 9 % | 26.3 px | 0.53 | 1.00 | 157 |
| heavy line | 10 % → 10 % | 28.6 px | 0.54 | 1.00 | 173 |
| pressure swell | 8 % → 8 % | 28.3 px | 0.55 | 1.00 | 106 |
| fast wave | 24 % → 24 % | 27.3 px | 0.55 | 1.00 | 752 |
| slow wave | 25 % → 25 % | 28.3 px | 0.55 | 1.00 | 983 |
| spiral | 39 % → 39 % | 25.6 px | 0.54 | 1.00 | 715 |
| loop | 20 % → 20 % | 26.3 px | 0.54 | 1.00 | 402 |
| tilted | 11 % → 11 % | 29.9 px | 0.53 | 1.00 | 241 |
| over the wet one | 20 % → 20 % | 25.5 px | 0.53 | 1.00 | 157 |
| long, no reload | 50 % → 50 % | 22.4 px | 0.54 | 1.00 | 1086 | quarters: 0.32 → 0.30 → 0.29 → 0.28

Numbers say: light vs heavy: width 26.3 → 28.6 px, dark 0.53 → 0.54; pressure barely changes the width; the long stroke does not run out of paint.

## Brush Artist · Charcoal — stick
Charcoal · 28 px · 13.7 s

![Brush Artist · Charcoal — stick](Brush-Artist-Charcoal-stick.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 3 % → 3 % | 8.4 px | 0.85 | 1.00 | 45 |
| heavy line | 6 % → 6 % | 17.8 px | 0.85 | 1.00 | 27 |
| pressure swell | 4 % → 4 % | 13.9 px | 0.85 | 1.00 | 54 |
| fast wave | 12 % → 12 % | 14.0 px | 0.85 | 1.00 | 114 |
| slow wave | 11 % → 11 % | 12.5 px | 0.85 | 1.00 | 135 |
| spiral | 19 % → 19 % | 12.7 px | 0.85 | 1.00 | 188 |
| loop | 10 % → 10 % | 12.8 px | 0.85 | 1.00 | 46 |
| tilted | 4 % → 4 % | 10.9 px | 0.85 | 1.00 | 42 |
| over the wet one | 9 % → 9 % | 13.5 px | 0.85 | 1.00 | 30 |
| long, no reload | 27 % → 27 % | 12.2 px | 0.85 | 1.00 | 160 | quarters: 0.26 → 0.25 → 0.26 → 0.27

Numbers say: light vs heavy: width 8.4 → 17.8 px, dark 0.85 → 0.85; the long stroke does not run out of paint.

## Brush Artist · Charcoal — stick B
Charcoal · 36 px · 14.5 s

![Brush Artist · Charcoal — stick B](Brush-Artist-Charcoal-stick-B.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 4 % → 4 % | 10.5 px | 0.85 | 1.00 | 53 |
| heavy line | 7 % → 7 % | 21.1 px | 0.85 | 1.00 | 54 |
| pressure swell | 4 % → 4 % | 16.5 px | 0.85 | 1.00 | 55 |
| fast wave | 15 % → 15 % | 16.8 px | 0.85 | 1.00 | 110 |
| slow wave | 13 % → 13 % | 14.7 px | 0.85 | 1.00 | 205 |
| spiral | 23 % → 23 % | 15.0 px | 0.85 | 1.00 | 220 |
| loop | 11 % → 11 % | 14.8 px | 0.85 | 1.00 | 55 |
| tilted | 4 % → 4 % | 12.3 px | 0.85 | 1.00 | 41 |
| over the wet one | 10 % → 10 % | 15.9 px | 0.85 | 1.00 | 26 |
| long, no reload | 31 % → 31 % | 13.9 px | 0.85 | 1.00 | 158 | quarters: 0.30 → 0.28 → 0.29 → 0.30

Numbers say: light vs heavy: width 10.5 → 21.1 px, dark 0.85 → 0.85; the long stroke does not run out of paint.

## Brush Artist · Charcoal — stick C
Charcoal · 22 px · 9.9 s

![Brush Artist · Charcoal — stick C](Brush-Artist-Charcoal-stick-C.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 2 % → 2 % | 6.9 px | 0.85 | 1.00 | 18 |
| heavy line | 5 % → 5 % | 15.3 px | 0.85 | 1.00 | 17 |
| pressure swell | 3 % → 3 % | 12.2 px | 0.85 | 1.00 | 17 |
| fast wave | 10 % → 10 % | 12.1 px | 0.85 | 1.00 | 45 |
| slow wave | 9 % → 9 % | 10.8 px | 0.85 | 1.00 | 64 |
| spiral | 17 % → 17 % | 11.0 px | 0.85 | 1.00 | 72 |
| loop | 9 % → 9 % | 11.4 px | 0.85 | 1.00 | 36 |
| tilted | 4 % → 4 % | 9.9 px | 0.85 | 1.00 | 25 |
| over the wet one | 8 % → 8 % | 11.7 px | 0.85 | 1.00 | 17 |
| long, no reload | 24 % → 24 % | 11.0 px | 0.85 | 1.00 | 102 | quarters: 0.24 → 0.22 → 0.23 → 0.24

Numbers say: light vs heavy: width 6.9 → 15.3 px, dark 0.85 → 0.85; the long stroke does not run out of paint.

## Brush Artist · Refs · #01 Henry Ward peach cloud — own sheet
own sheet 600 × 600 · Gouache · 44 px · 14.6 s

![Brush Artist · Refs · #01 Henry Ward peach cloud — own sheet](Brush-Artist-Refs-01-Henry-Ward-peach-cloud-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 14 % → 39 % | 40.5 px | 0.59 | 2.74 | 227 |
| stroke 2 | 24 % → 58 % | 79.5 px | 0.59 | 2.40 | 177 |
| stroke 3 | 28 % → 56 % | 81.3 px | 0.59 | 2.01 | 208 |
| stroke 4 | 30 % → 63 % | 99.7 px | 0.59 | 2.05 | 139 |
| stroke 5 | 30 % → 55 % | 86.0 px | 0.59 | 1.86 | 159 |
| stroke 6 | 30 % → 42 % | 91.1 px | 0.59 | 1.42 | 141 |
| stroke 7 | 16 % → 53 % | 38.9 px | 0.59 | 3.38 | 147 |
| stroke 8 | 18 % → 49 % | 44.8 px | 0.59 | 2.76 | 168 |
| stroke 9 | 21 % → 50 % | 54.2 px | 0.59 | 2.39 | 159 |
| stroke 10 | 23 % → 51 % | 61.9 px | 0.59 | 2.21 | 158 |
| stroke 11 | 25 % → 54 % | 72.0 px | 0.59 | 2.11 | 156 |
| stroke 12 | 29 % → 56 % | 88.0 px | 0.59 | 1.92 | 149 |
| stroke 13 | 37 % → 59 % | 108.0 px | 0.59 | 1.59 | 187 |
| stroke 14 | 40 % → 61 % | 113.8 px | 0.59 | 1.54 | 159 |
| stroke 15 | 53 % → 67 % | 156.4 px | 0.59 | 1.27 | 168 |
| stroke 16 | 54 % → 68 % | 164.9 px | 0.59 | 1.24 | 147 |
| stroke 17 | 55 % → 69 % | 155.8 px | 0.59 | 1.24 | 157 |
| stroke 18 | 57 % → 67 % | 164.8 px | 0.59 | 1.19 | 156 |
| stroke 19 | 58 % → 66 % | 163.9 px | 0.59 | 1.13 | 155 |
| stroke 20 | 58 % → 63 % | 167.5 px | 0.59 | 1.09 | 159 |
| stroke 21 | 58 % → 60 % | 168.2 px | 0.59 | 1.04 | 160 |
| stroke 22 | 59 % → 61 % | 173.1 px | 0.59 | 1.03 | 172 |
| stroke 23 | 59 % → 59 % | 167.7 px | 0.59 | 1.00 | 248 |
| stroke 24 | 63 % → 62 % | 187.3 px | 0.59 | 0.99 | 214 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #02 Henry Ward cream strokes — own sheet
own sheet 600 × 600 · Gouache · 46 px · 9.2 s

![Brush Artist · Refs · #02 Henry Ward cream strokes — own sheet](Brush-Artist-Refs-02-Henry-Ward-cream-strokes-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 18 % → 32 % | 37.3 px | 0.70 | 1.77 | 334 |
| stroke 2 | 28 % → 37 % | 72.5 px | 0.70 | 1.34 | 210 |
| stroke 3 | 27 % → 44 % | 68.7 px | 0.71 | 1.64 | 220 |
| stroke 4 | 29 % → 41 % | 71.2 px | 0.71 | 1.42 | 225 |
| stroke 5 | 35 % → 45 % | 85.0 px | 0.71 | 1.29 | 220 |
| stroke 6 | 28 % → 39 % | 66.8 px | 0.70 | 1.42 | 208 |
| stroke 7 | 29 % → 27 % | 74.4 px | 0.70 | 0.92 | 211 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #03 Henry Ward navy contours — own sheet
own sheet 600 × 600 · Heavy acrylic · 22 px · 2.7 s

![Brush Artist · Refs · #03 Henry Ward navy contours — own sheet](Brush-Artist-Refs-03-Henry-Ward-navy-contours-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 11 % → 18 % | 23.1 px | 0.69 | 1.56 | 125 |
| stroke 2 | 20 % → 23 % | 28.3 px | 0.69 | 1.14 | 119 |
| stroke 3 | 23 % → 23 % | 33.4 px | 0.69 | 1.01 | 168 |
| stroke 4 | 23 % → 21 % | 50.8 px | 0.69 | 0.92 | 197 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #04 Henry Ward grey cloud — own sheet
own sheet 600 × 600 · Gouache · 50 px · 15.4 s

![Brush Artist · Refs · #04 Henry Ward grey cloud — own sheet](Brush-Artist-Refs-04-Henry-Ward-grey-cloud-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 14 % → 48 % | 42.2 px | 0.40 | 3.32 | 278 |
| stroke 2 | 19 % → 50 % | 53.3 px | 0.40 | 2.68 | 290 |
| stroke 3 | 27 % → 57 % | 75.3 px | 0.40 | 2.11 | 285 |
| stroke 4 | 30 % → 60 % | 88.0 px | 0.40 | 1.98 | 296 |
| stroke 5 | 36 % → 66 % | 110.1 px | 0.40 | 1.83 | 309 |
| stroke 6 | 40 % → 70 % | 129.7 px | 0.40 | 1.77 | 207 |
| stroke 7 | 46 % → 77 % | 134.2 px | 0.40 | 1.67 | 216 |
| stroke 8 | 45 % → 77 % | 133.7 px | 0.40 | 1.70 | 215 |
| stroke 9 | 45 % → 77 % | 133.8 px | 0.40 | 1.72 | 206 |
| stroke 10 | 46 % → 77 % | 148.0 px | 0.40 | 1.67 | 206 |
| stroke 11 | 46 % → 77 % | 130.7 px | 0.40 | 1.67 | 210 |
| stroke 12 | 47 % → 76 % | 141.7 px | 0.40 | 1.63 | 210 |
| stroke 13 | 46 % → 77 % | 131.3 px | 0.40 | 1.67 | 210 |
| stroke 14 | 47 % → 77 % | 139.7 px | 0.40 | 1.64 | 213 |
| stroke 15 | 46 % → 72 % | 133.2 px | 0.40 | 1.56 | 218 |
| stroke 16 | 47 % → 70 % | 143.4 px | 0.40 | 1.47 | 221 |
| stroke 17 | 45 % → 61 % | 130.9 px | 0.40 | 1.33 | 213 |
| stroke 18 | 45 % → 56 % | 149.2 px | 0.40 | 1.24 | 195 |
| stroke 19 | 46 % → 47 % | 136.3 px | 0.40 | 1.03 | 206 |
| stroke 20 | 47 % → 46 % | 148.0 px | 0.40 | 0.99 | 205 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #05 Henry Ward green in rust loops — own sheet
own sheet 600 × 600 · Heavy acrylic · 20 px · 2.7 s

![Brush Artist · Refs · #05 Henry Ward green in rust loops — own sheet](Brush-Artist-Refs-05-Henry-Ward-green-in-rust-loops-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 12 % → 19 % | 20.9 px | 0.02 | 1.60 | 140 |
| stroke 2 | 12 % → 11 % | 23.6 px | 0.02 | 0.93 | 195 |
| stroke 3 | 23 % → 21 % | 41.5 px | 0.02 | 0.93 | 159 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #06 Henry Ward scrubbed grey — own sheet
own sheet 600 × 600 · Gouache · 50 px · 16.1 s

![Brush Artist · Refs · #06 Henry Ward scrubbed grey — own sheet](Brush-Artist-Refs-06-Henry-Ward-scrubbed-grey-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 17 % → 54 % | 42.0 px | 0.40 | 3.16 | 213 |
| stroke 2 | 22 % → 56 % | 58.8 px | 0.40 | 2.55 | 216 |
| stroke 3 | 28 % → 61 % | 87.1 px | 0.40 | 2.13 | 202 |
| stroke 4 | 29 % → 61 % | 92.8 px | 0.40 | 2.06 | 206 |
| stroke 5 | 42 % → 75 % | 127.0 px | 0.40 | 1.78 | 216 |
| stroke 6 | 45 % → 76 % | 138.6 px | 0.40 | 1.67 | 208 |
| stroke 7 | 47 % → 77 % | 133.9 px | 0.40 | 1.64 | 216 |
| stroke 8 | 47 % → 77 % | 147.9 px | 0.40 | 1.65 | 206 |
| stroke 9 | 45 % → 77 % | 137.9 px | 0.40 | 1.71 | 199 |
| stroke 10 | 45 % → 77 % | 147.0 px | 0.40 | 1.70 | 199 |
| stroke 11 | 46 % → 77 % | 136.1 px | 0.40 | 1.66 | 206 |
| stroke 12 | 47 % → 77 % | 143.2 px | 0.40 | 1.64 | 209 |
| stroke 13 | 45 % → 77 % | 127.5 px | 0.40 | 1.71 | 214 |
| stroke 14 | 44 % → 76 % | 130.2 px | 0.40 | 1.72 | 217 |
| stroke 15 | 45 % → 77 % | 128.6 px | 0.40 | 1.71 | 218 |
| stroke 16 | 46 % → 77 % | 146.4 px | 0.40 | 1.68 | 199 |
| stroke 17 | 45 % → 70 % | 134.2 px | 0.40 | 1.55 | 210 |
| stroke 18 | 47 % → 67 % | 141.3 px | 0.40 | 1.44 | 216 |
| stroke 19 | 45 % → 61 % | 134.0 px | 0.40 | 1.36 | 215 |
| stroke 20 | 45 % → 59 % | 141.3 px | 0.40 | 1.30 | 216 |
| stroke 21 | 45 % → 50 % | 131.4 px | 0.40 | 1.11 | 219 |
| stroke 22 | 46 % → 45 % | 151.0 px | 0.40 | 0.99 | 198 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #07 Henry Ward blue L + black zigzag — own sheet
own sheet 600 × 600 · Heavy acrylic · 34 px · 1.9 s

![Brush Artist · Refs · #07 Henry Ward blue L + black zigzag — own sheet](Brush-Artist-Refs-07-Henry-Ward-blue-L-black-zigzag-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 15 % → 17 % | 35.6 px | 0.59 | 1.14 | 110 |
| stroke 2 | 17 % → 16 % | 42.8 px | 0.59 | 0.93 | 85 |

## Brush Artist · Refs · #08 Henry Ward olive bands — own sheet
own sheet 600 × 600 · Gouache · 34 px · 5.1 s

![Brush Artist · Refs · #08 Henry Ward olive bands — own sheet](Brush-Artist-Refs-08-Henry-Ward-olive-bands-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 9 % → 7 % | 17.9 px | 0.59 | 0.82 | 153 |
| stroke 2 | 15 % → 9 % | 32.8 px | 0.59 | 0.63 | 156 |
| stroke 3 | 13 % → 13 % | 26.4 px | 0.59 | 1.02 | 165 |
| stroke 4 | 15 % → 11 % | 31.5 px | 0.59 | 0.78 | 170 |
| stroke 5 | 20 % → 14 % | 40.1 px | 0.59 | 0.71 | 165 |
| stroke 6 | 13 % → 7 % | 24.2 px | 0.59 | 0.52 | 160 |

## Brush Artist · Refs · #09 Henry Ward white loops — own sheet
own sheet 600 × 600 · Gouache · 46 px · 9.0 s

![Brush Artist · Refs · #09 Henry Ward white loops — own sheet](Brush-Artist-Refs-09-Henry-Ward-white-loops-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 23 % → 4 % | 12.2 px | 0.07 | 0.17 | 1668 |
| stroke 2 | 26 % → 4 % | 26.2 px | 0.07 | 0.14 | 1149 |
| stroke 3 | 34 % → 4 % | 31.4 px | 0.07 | 0.12 | 1000 |
| stroke 4 | 3 % → 1 % | 6.1 px | 0.06 | 0.22 | 148 |
| stroke 5 | 4 % → 2 % | 12.1 px | 0.08 | 0.38 | 155 |
| stroke 6 | 7 % → 4 % | 18.2 px | 0.07 | 0.65 | 162 |
| stroke 7 | 14 % → 4 % | 36.3 px | 0.07 | 0.31 | 168 |
| stroke 8 | 2 % → 0 % | 3.0 px | 0.05 | 0.06 | 151 |

## Brush Artist · Refs · #10 Henry Ward maroon loops — own sheet
own sheet 600 × 600 · Heavy acrylic · 30 px · 3.0 s

![Brush Artist · Refs · #10 Henry Ward maroon loops — own sheet](Brush-Artist-Refs-10-Henry-Ward-maroon-loops-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 12 % → 28 % | 28.7 px | 0.72 | 2.39 | 223 |
| stroke 2 | 22 % → 40 % | 48.5 px | 0.72 | 1.87 | 126 |
| stroke 3 | 29 % → 37 % | 58.5 px | 0.72 | 1.27 | 157 |
| stroke 4 | 41 % → 40 % | 92.8 px | 0.72 | 0.96 | 106 |
| stroke 5 | 34 % → 32 % | 85.9 px | 0.72 | 0.93 | 141 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #11 Henry Ward purple spun balls — own sheet
own sheet 600 × 600 · Heavy acrylic · 36 px · 2.7 s

![Brush Artist · Refs · #11 Henry Ward purple spun balls — own sheet](Brush-Artist-Refs-11-Henry-Ward-purple-spun-balls-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 24 % → 35 % | 26.5 px | 0.68 | 1.43 | 221 |
| stroke 2 | 35 % → 46 % | 38.2 px | 0.68 | 1.33 | 227 |
| stroke 3 | 36 % → 34 % | 39.2 px | 0.68 | 0.97 | 222 |

## Brush Artist · Refs · #12 Henry Ward black-olive cage — own sheet
own sheet 600 × 600 · Gouache · 28 px · 5.1 s

![Brush Artist · Refs · #12 Henry Ward black-olive cage — own sheet](Brush-Artist-Refs-12-Henry-Ward-black-olive-cage-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 7 % → 12 % | 13.4 px | 0.60 | 1.68 | 201 |
| stroke 2 | 7 % → 12 % | 16.3 px | 0.60 | 1.80 | 173 |
| stroke 3 | 15 % → 16 % | 24.2 px | 0.60 | 1.03 | 219 |
| stroke 4 | 16 % → 15 % | 32.2 px | 0.60 | 0.92 | 124 |
| stroke 5 | 16 % → 11 % | 29.0 px | 0.60 | 0.68 | 131 |
| stroke 6 | 25 % → 16 % | 48.3 px | 0.60 | 0.65 | 167 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #13 Henry Ward blue streaky form — own sheet
own sheet 600 × 600 · Gouache · 50 px · 13.3 s

![Brush Artist · Refs · #13 Henry Ward blue streaky form — own sheet](Brush-Artist-Refs-13-Henry-Ward-blue-streaky-form-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 14 % → 8 % | 42.7 px | 0.04 | 0.56 | 203 |
| stroke 2 | 20 % → 7 % | 61.3 px | 0.04 | 0.36 | 212 |
| stroke 3 | 31 % → 8 % | 88.7 px | 0.04 | 0.25 | 210 |
| stroke 4 | 31 % → 7 % | 99.6 px | 0.04 | 0.23 | 206 |
| stroke 5 | 45 % → 8 % | 130.2 px | 0.04 | 0.18 | 215 |
| stroke 6 | 45 % → 9 % | 129.6 px | 0.04 | 0.20 | 242 |
| stroke 7 | 46 % → 10 % | 136.7 px | 0.04 | 0.22 | 219 |
| stroke 8 | 47 % → 8 % | 143.3 px | 0.03 | 0.18 | 212 |
| stroke 9 | 46 % → 7 % | 142.0 px | 0.03 | 0.16 | 208 |
| stroke 10 | 46 % → 7 % | 152.6 px | 0.03 | 0.16 | 246 |
| stroke 11 | 44 % → 5 % | 136.4 px | 0.03 | 0.11 | 291 |
| stroke 12 | 45 % → 6 % | 135.8 px | 0.03 | 0.14 | 285 |
| stroke 13 | 45 % → 7 % | 138.8 px | 0.04 | 0.17 | 276 |
| stroke 14 | 43 % → 7 % | 129.4 px | 0.04 | 0.16 | 297 |
| stroke 15 | 44 % → 7 % | 125.8 px | 0.04 | 0.17 | 217 |
| stroke 16 | 46 % → 7 % | 137.2 px | 0.04 | 0.16 | 213 |
| stroke 17 | 55 % → 4 % | 137.1 px | 0.04 | 0.08 | 213 |
| stroke 18 | 58 % → 4 % | 140.1 px | 0.04 | 0.08 | 213 |
| stroke 19 | 64 % → 5 % | 130.9 px | 0.04 | 0.08 | 211 |
| stroke 20 | 72 % → 5 % | 137.6 px | 0.04 | 0.08 | 271 |
| stroke 21 | 1 % → 0 % | 2.9 px | 0.04 | 0.02 | 158 |
| stroke 22 | 12 % → 7 % | 34.1 px | 0.04 | 0.61 | 230 |
| stroke 23 | 23 % → 8 % | 70.4 px | 0.04 | 0.35 | 191 |
| stroke 24 | 14 % → 5 % | 38.0 px | 0.03 | 0.35 | 196 |
| stroke 25 | 18 % → 6 % | 46.1 px | 0.04 | 0.31 | 189 |

## Brush Artist · Refs · #14 Henry Ward olive totem — own sheet
own sheet 600 × 600 · Heavy acrylic · 48 px · 7.1 s

![Brush Artist · Refs · #14 Henry Ward olive totem — own sheet](Brush-Artist-Refs-14-Henry-Ward-olive-totem-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 18 % → 46 % | 46.9 px | 0.38 | 2.58 | 131 |
| stroke 2 | 21 % → 50 % | 64.4 px | 0.38 | 2.44 | 120 |
| stroke 3 | 29 % → 52 % | 100.6 px | 0.38 | 1.78 | 122 |
| stroke 4 | 30 % → 55 % | 113.7 px | 0.38 | 1.80 | 126 |
| stroke 5 | 39 % → 63 % | 135.6 px | 0.38 | 1.63 | 116 |
| stroke 6 | 39 % → 65 % | 150.4 px | 0.38 | 1.68 | 127 |
| stroke 7 | 37 % → 61 % | 124.3 px | 0.38 | 1.66 | 128 |
| stroke 8 | 37 % → 63 % | 142.4 px | 0.38 | 1.69 | 126 |
| stroke 9 | 38 % → 63 % | 130.9 px | 0.38 | 1.67 | 123 |
| stroke 10 | 38 % → 62 % | 141.0 px | 0.38 | 1.62 | 138 |
| stroke 11 | 40 % → 65 % | 143.8 px | 0.38 | 1.61 | 120 |
| stroke 12 | 38 % → 65 % | 144.2 px | 0.38 | 1.70 | 128 |
| stroke 13 | 39 % → 66 % | 135.5 px | 0.38 | 1.72 | 114 |
| stroke 14 | 37 % → 62 % | 134.5 px | 0.38 | 1.68 | 135 |
| stroke 15 | 40 % → 66 % | 136.9 px | 0.38 | 1.65 | 120 |
| stroke 16 | 38 % → 64 % | 138.8 px | 0.38 | 1.66 | 134 |
| stroke 17 | 38 % → 62 % | 126.2 px | 0.38 | 1.65 | 155 |
| stroke 18 | 40 % → 66 % | 154.9 px | 0.38 | 1.64 | 197 |
| stroke 19 | 40 % → 60 % | 137.9 px | 0.38 | 1.52 | 167 |
| stroke 20 | 41 % → 55 % | 144.4 px | 0.38 | 1.34 | 190 |
| stroke 21 | 46 % → 55 % | 137.7 px | 0.38 | 1.18 | 150 |
| stroke 22 | 54 % → 53 % | 146.7 px | 0.38 | 0.99 | 171 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #15 Ultramarine brush script — own sheet
own sheet 600 × 600 · Ink · 4 px · 8.8 s

![Brush Artist · Refs · #15 Ultramarine brush script — own sheet](Brush-Artist-Refs-15-Ultramarine-brush-script-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 40 % → 42 % | 8.9 px | 0.66 | 1.05 | 64 |
| stroke 2 | 40 % → 42 % | 8.9 px | 0.66 | 1.06 | 70 |
| stroke 3 | 40 % → 42 % | 9.5 px | 0.74 | 1.06 | 36 |
| stroke 4 | 42 % → 45 % | 10.1 px | 0.74 | 1.08 | 28 |
| stroke 5 | 44 % → 48 % | 9.7 px | 0.73 | 1.08 | 36 |
| stroke 6 | 42 % → 44 % | 9.5 px | 0.65 | 1.05 | 60 |
| stroke 7 | 43 % → 47 % | 9.2 px | 0.72 | 1.08 | 38 |
| stroke 8 | 38 % → 41 % | 9.3 px | 0.68 | 1.05 | 69 |
| stroke 9 | 40 % → 42 % | 9.2 px | 0.69 | 1.06 | 53 |
| stroke 10 | 36 % → 38 % | 9.9 px | 0.68 | 1.05 | 59 |
| stroke 11 | 42 % → 45 % | 9.6 px | 0.70 | 1.06 | 50 |
| stroke 12 | 39 % → 41 % | 9.4 px | 0.66 | 1.05 | 67 |
| stroke 13 | 45 % → 48 % | 10.2 px | 0.71 | 1.06 | 41 |
| stroke 14 | 38 % → 41 % | 9.9 px | 0.73 | 1.07 | 29 |
| stroke 15 | 37 % → 39 % | 9.1 px | 0.69 | 1.06 | 43 |
| stroke 16 | 42 % → 45 % | 9.4 px | 0.72 | 1.06 | 27 |
| stroke 17 | 41 % → 44 % | 7.1 px | 0.71 | 1.08 | 47 |
| stroke 18 | 43 % → 45 % | 9.2 px | 0.73 | 1.06 | 25 |
| stroke 19 | 39 % → 41 % | 8.9 px | 0.66 | 1.05 | 55 |
| stroke 20 | 41 % → 43 % | 9.4 px | 0.71 | 1.06 | 32 |
| stroke 21 | 40 % → 43 % | 9.9 px | 0.70 | 1.06 | 36 |
| stroke 22 | 42 % → 44 % | 8.5 px | 0.65 | 1.05 | 53 |
| stroke 23 | 40 % → 43 % | 10.1 px | 0.73 | 1.07 | 22 |
| stroke 24 | 38 % → 41 % | 8.8 px | 0.73 | 1.07 | 32 |
| stroke 25 | 41 % → 43 % | 9.8 px | 0.72 | 1.07 | 29 |
| stroke 26 | 46 % → 49 % | 9.3 px | 0.68 | 1.05 | 44 |
| stroke 27 | 43 % → 45 % | 8.8 px | 0.63 | 1.05 | 57 |
| stroke 28 | 44 % → 46 % | 9.1 px | 0.70 | 1.06 | 38 |
| stroke 29 | 36 % → 39 % | 10.6 px | 0.72 | 1.08 | 25 |
| stroke 30 | 39 % → 41 % | 8.7 px | 0.71 | 1.04 | 38 |
| stroke 31 | 43 % → 46 % | 10.3 px | 0.75 | 1.07 | 20 |
| stroke 32 | 42 % → 46 % | 9.5 px | 0.73 | 1.09 | 25 |
| stroke 33 | 35 % → 38 % | 10.9 px | 0.72 | 1.08 | 21 |
| stroke 34 | 40 % → 43 % | 9.8 px | 0.73 | 1.08 | 22 |
| stroke 35 | 36 % → 37 % | 9.4 px | 0.65 | 1.05 | 49 |

## Brush Artist · Refs · #18 Blue oil-stick scribbles — own sheet
own sheet 600 × 600 · Pastel · 10 px · 3.3 s

![Brush Artist · Refs · #18 Blue oil-stick scribbles — own sheet](Brush-Artist-Refs-18-Blue-oil-stick-scribbles-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 15 % → 31 % | 3.8 px | 0.49 | 2.11 | 165 |
| stroke 2 | 13 % → 37 % | 3.6 px | 0.49 | 2.73 | 187 |
| stroke 3 | 16 % → 26 % | 5.8 px | 0.49 | 1.66 | 212 |
| stroke 4 | 15 % → 29 % | 8.0 px | 0.49 | 1.88 | 255 |
| stroke 5 | 29 % → 34 % | 8.4 px | 0.49 | 1.19 | 194 |
| stroke 6 | 25 % → 26 % | 9.4 px | 0.49 | 1.02 | 177 |
| stroke 7 | 26 % → 32 % | 8.3 px | 0.49 | 1.24 | 163 |
| stroke 8 | 30 % → 30 % | 17.0 px | 0.49 | 1.00 | 168 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #20 Orange-red crayon scribble — own sheet
own sheet 600 × 600 · Pastel · 14 px · 2.7 s

![Brush Artist · Refs · #20 Orange-red crayon scribble — own sheet](Brush-Artist-Refs-20-Orange-red-crayon-scribble-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 8 % → 18 % | 5.5 px | 0.59 | 2.46 | 186 |
| stroke 2 | 9 % → 23 % | 6.8 px | 0.59 | 2.48 | 162 |
| stroke 3 | 13 % → 21 % | 8.5 px | 0.59 | 1.64 | 150 |
| stroke 4 | 24 % → 32 % | 8.9 px | 0.59 | 1.34 | 175 |
| stroke 5 | 27 % → 27 % | 7.7 px | 0.59 | 1.00 | 160 |
| stroke 6 | 22 % → 22 % | 16.8 px | 0.59 | 1.00 | 175 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #21 Gritty black contours — own sheet
own sheet 600 × 600 · Gouache · 12 px · 4.5 s

![Brush Artist · Refs · #21 Gritty black contours — own sheet](Brush-Artist-Refs-21-Gritty-black-contours-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 4 % → 5 % | 4.7 px | 0.37 | 1.13 | 145 |
| stroke 2 | 4 % → 3 % | 7.3 px | 0.37 | 0.60 | 171 |
| stroke 3 | 7 % → 4 % | 6.2 px | 0.37 | 0.56 | 112 |
| stroke 4 | 9 % → 4 % | 10.7 px | 0.37 | 0.51 | 126 |
| stroke 5 | 10 % → 4 % | 12.7 px | 0.37 | 0.42 | 90 |

## Brush Artist · Refs · #22 Bold black brush poster — own sheet
own sheet 600 × 600 · Ink · 20 px · 5.2 s

![Brush Artist · Refs · #22 Bold black brush poster — own sheet](Brush-Artist-Refs-22-Bold-black-brush-poster-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 22 % → 27 % | 36.4 px | 0.94 | 1.20 | 102 |
| stroke 2 | 27 % → 37 % | 41.5 px | 0.95 | 1.36 | 29 |
| stroke 3 | 28 % → 28 % | 43.6 px | 0.95 | 1.00 | 45 |
| stroke 4 | 27 % → 39 % | 53.8 px | 0.94 | 1.42 | 61 |
| stroke 5 | 25 % → 25 % | 43.0 px | 0.94 | 1.00 | 82 |

## Brush Artist · Refs · #23 Dry white on orange + black line — own sheet
own sheet 600 × 600 · Gouache · 50 px · 8.4 s

![Brush Artist · Refs · #23 Dry white on orange + black line — own sheet](Brush-Artist-Refs-23-Dry-white-on-orange-black-line-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 5 % → 10 % | 18.7 px | 0.42 | 1.89 | 143 |
| stroke 2 | 7 % → 9 % | 24.3 px | 0.42 | 1.35 | 175 |
| stroke 3 | 10 % → 10 % | 39.0 px | 0.42 | 0.92 | 145 |
| stroke 4 | 12 % → 11 % | 45.8 px | 0.42 | 0.95 | 153 |
| stroke 5 | 17 % → 14 % | 60.0 px | 0.42 | 0.82 | 152 |
| stroke 6 | 17 % → 15 % | 70.6 px | 0.42 | 0.86 | 151 |
| stroke 7 | 14 % → 14 % | 52.6 px | 0.41 | 1.00 | 152 |
| stroke 8 | 14 % → 13 % | 55.2 px | 0.41 | 0.91 | 260 |
| stroke 9 | 15 % → 14 % | 54.3 px | 0.41 | 0.93 | 226 |
| stroke 10 | 14 % → 14 % | 56.6 px | 0.41 | 0.97 | 203 |
| stroke 11 | 16 % → 15 % | 60.6 px | 0.41 | 0.92 | 214 |
| stroke 12 | 16 % → 15 % | 63.4 px | 0.41 | 0.94 | 222 |
| stroke 13 | 17 % → 16 % | 61.2 px | 0.41 | 0.97 | 151 |
| stroke 14 | 16 % → 16 % | 63.9 px | 0.41 | 0.97 | 152 |
| stroke 15 | 16 % → 14 % | 59.9 px | 0.41 | 0.87 | 138 |
| stroke 16 | 15 % → 12 % | 61.4 px | 0.41 | 0.78 | 143 |
| stroke 17 | 16 % → 11 % | 56.7 px | 0.41 | 0.68 | 158 |
| stroke 18 | 19 % → 11 % | 69.3 px | 0.41 | 0.60 | 131 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #24 Picasso flat oil — own sheet
own sheet 600 × 600 · Oil · 34 px · 5.0 s

![Brush Artist · Refs · #24 Picasso flat oil — own sheet](Brush-Artist-Refs-24-Picasso-flat-oil-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 16 % → 45 % | 34.7 px | 0.23 | 2.74 | 156 |
| stroke 2 | 20 % → 48 % | 47.2 px | 0.24 | 2.40 | 129 |
| stroke 3 | 29 % → 59 % | 62.5 px | 0.23 | 2.07 | 127 |
| stroke 4 | 37 % → 65 % | 83.2 px | 0.23 | 1.76 | 136 |
| stroke 5 | 43 % → 71 % | 94.5 px | 0.23 | 1.65 | 131 |
| stroke 6 | 44 % → 66 % | 102.1 px | 0.23 | 1.50 | 127 |
| stroke 7 | 45 % → 66 % | 94.8 px | 0.23 | 1.46 | 141 |
| stroke 8 | 44 % → 66 % | 107.0 px | 0.23 | 1.50 | 127 |
| stroke 9 | 37 % → 62 % | 81.5 px | 0.23 | 1.67 | 120 |
| stroke 10 | 39 % → 62 % | 93.1 px | 0.23 | 1.58 | 129 |
| stroke 11 | 37 % → 60 % | 78.6 px | 0.23 | 1.62 | 136 |
| stroke 12 | 38 % → 61 % | 91.1 px | 0.23 | 1.60 | 126 |
| stroke 13 | 38 % → 68 % | 84.4 px | 0.23 | 1.76 | 127 |
| stroke 14 | 39 % → 69 % | 88.9 px | 0.23 | 1.75 | 130 |
| stroke 15 | 39 % → 62 % | 83.3 px | 0.23 | 1.58 | 128 |
| stroke 16 | 38 % → 55 % | 88.0 px | 0.23 | 1.43 | 137 |
| stroke 17 | 43 % → 48 % | 90.0 px | 0.23 | 1.12 | 135 |
| stroke 18 | 42 % → 42 % | 102.7 px | 0.23 | 1.00 | 129 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #25 Yellow heavy flat stroke — own sheet
own sheet 600 × 600 · Heavy acrylic · 110 px · 2.8 s

![Brush Artist · Refs · #25 Yellow heavy flat stroke — own sheet](Brush-Artist-Refs-25-Yellow-heavy-flat-stroke-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 18 % → 18 % | 104.2 px | 0.17 | 0.98 | 612 |

## Brush Artist · Refs · #27 Orange impasto swatch — own sheet
own sheet 600 × 600 · Heavy acrylic · 60 px · 2.9 s

![Brush Artist · Refs · #27 Orange impasto swatch — own sheet](Brush-Artist-Refs-27-Orange-impasto-swatch-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 8 % → 21 % | 61.8 px | 0.33 | 2.60 | 66 |
| stroke 2 | 7 % → 33 % | 62.5 px | 0.33 | 4.67 | 47 |
| stroke 3 | 25 % → 36 % | 245.5 px | 0.33 | 1.40 | 37 |
| stroke 4 | 10 % → 12 % | 69.6 px | 0.33 | 1.25 | 58 |
| stroke 5 | 17 % → 33 % | 63.5 px | 0.33 | 1.90 | 64 |
| stroke 6 | 18 % → 31 % | 145.1 px | 0.33 | 1.79 | 56 |
| stroke 7 | 8 % → 15 % | 70.2 px | 0.33 | 1.86 | 46 |
| stroke 8 | 33 % → 34 % | 337.1 px | 0.33 | 1.04 | 41 |
| stroke 9 | 38 % → 37 % | 185.4 px | 0.33 | 0.98 | 64 |
| stroke 10 | 33 % → 33 % | 304.7 px | 0.33 | 0.98 | 45 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #28 Miles Davis black lines — own sheet
own sheet 600 × 600 · Ink · 22 px · 7.7 s

![Brush Artist · Refs · #28 Miles Davis black lines — own sheet](Brush-Artist-Refs-28-Miles-Davis-black-lines-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 22 % → 32 % | 36.6 px | 0.88 | 1.42 | 162 |
| stroke 2 | 28 % → 49 % | 38.3 px | 0.88 | 1.73 | 121 |
| stroke 3 | 39 % → 44 % | 75.1 px | 0.88 | 1.12 | 99 |
| stroke 4 | 42 % → 48 % | 83.7 px | 0.88 | 1.15 | 154 |
| stroke 5 | 55 % → 55 % | 109.9 px | 0.88 | 1.00 | 118 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #29 Shrigley magenta asterisk — own sheet
own sheet 600 × 600 · Watercolor · 70 px · 7.7 s

![Brush Artist · Refs · #29 Shrigley magenta asterisk — own sheet](Brush-Artist-Refs-29-Shrigley-magenta-asterisk-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 13 % → 37 % | 46.6 px | 0.72 | 2.85 | 158 |
| stroke 2 | 12 % → 12 % | 87.1 px | 0.71 | 1.00 | 172 |
| stroke 3 | 28 % → 37 % | 100.9 px | 0.72 | 1.31 | 177 |
| stroke 4 | 23 % → 23 % | 163.9 px | 0.71 | 1.02 | 181 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #30 Red gouache face patch — own sheet
own sheet 600 × 600 · Gouache · 60 px · 12.7 s

![Brush Artist · Refs · #30 Red gouache face patch — own sheet](Brush-Artist-Refs-30-Red-gouache-face-patch-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 12 % → 37 % | 51.5 px | 0.53 | 3.22 | 146 |
| stroke 2 | 15 % → 40 % | 74.6 px | 0.53 | 2.72 | 174 |
| stroke 3 | 24 % → 50 % | 116.0 px | 0.53 | 2.06 | 186 |
| stroke 4 | 27 % → 51 % | 134.1 px | 0.53 | 1.93 | 197 |
| stroke 5 | 34 % → 60 % | 159.9 px | 0.53 | 1.77 | 218 |
| stroke 6 | 35 % → 61 % | 178.3 px | 0.53 | 1.76 | 218 |
| stroke 7 | 34 % → 59 % | 160.9 px | 0.54 | 1.73 | 221 |
| stroke 8 | 34 % → 56 % | 162.5 px | 0.53 | 1.65 | 437 |
| stroke 9 | 36 % → 60 % | 173.1 px | 0.53 | 1.66 | 429 |
| stroke 10 | 38 % → 62 % | 196.8 px | 0.53 | 1.63 | 353 |
| stroke 11 | 37 % → 61 % | 182.5 px | 0.53 | 1.66 | 327 |
| stroke 12 | 36 % → 58 % | 178.3 px | 0.53 | 1.62 | 269 |
| stroke 13 | 33 % → 46 % | 156.5 px | 0.53 | 1.39 | 145 |
| stroke 14 | 33 % → 41 % | 157.7 px | 0.53 | 1.25 | 177 |
| stroke 15 | 33 % → 37 % | 153.4 px | 0.53 | 1.12 | 160 |
| stroke 16 | 39 % → 39 % | 184.9 px | 0.53 | 0.99 | 142 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #31 Warhol blotted line — own sheet
own sheet 600 × 600 · Ink · 6 px · 4.3 s

![Brush Artist · Refs · #31 Warhol blotted line — own sheet](Brush-Artist-Refs-31-Warhol-blotted-line-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 21 % → 42 % | 15.8 px | 0.82 | 1.98 | 83 |
| stroke 2 | 17 % → 23 % | 15.9 px | 0.82 | 1.34 | 71 |
| stroke 3 | 24 % → 25 % | 25.1 px | 0.81 | 1.02 | 77 |
| stroke 4 | 31 % → 40 % | 31.9 px | 0.82 | 1.28 | 49 |
| stroke 5 | 35 % → 44 % | 36.4 px | 0.82 | 1.23 | 72 |
| stroke 6 | 32 % → 33 % | 26.7 px | 0.81 | 1.03 | 68 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #32 Thick orange swipes — own sheet
own sheet 600 × 600 · Heavy acrylic · 90 px · 3.3 s

![Brush Artist · Refs · #32 Thick orange swipes — own sheet](Brush-Artist-Refs-32-Thick-orange-swipes-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 14 % → 27 % | 86.0 px | 0.03 | 1.90 | 299 |
| stroke 2 | 26 % → 38 % | 176.9 px | 0.03 | 1.43 | 276 |
| stroke 3 | 28 % → 27 % | 177.5 px | 0.03 | 0.98 | 264 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #33 Red wet-in-wet band — own sheet
own sheet 600 × 600 · Watercolor · 80 px · 8.9 s

![Brush Artist · Refs · #33 Red wet-in-wet band — own sheet](Brush-Artist-Refs-33-Red-wet-in-wet-band-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 23 % → 57 % | 88.3 px | 0.62 | 2.47 | 341 |
| stroke 2 | 30 % → 52 % | 243.8 px | 0.62 | 1.73 | 89 |
| stroke 3 | 37 % → 54 % | 356.6 px | 0.62 | 1.47 | 90 |
| stroke 4 | 42 % → 60 % | 412.3 px | 0.63 | 1.43 | 84 |
| stroke 5 | 42 % → 55 % | 354.6 px | 0.62 | 1.33 | 104 |
| stroke 6 | 42 % → 47 % | 322.0 px | 0.61 | 1.12 | 99 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #34 Magenta oil patches — own sheet
own sheet 600 × 600 · Oil · 60 px · 4.1 s

![Brush Artist · Refs · #34 Magenta oil patches — own sheet](Brush-Artist-Refs-34-Magenta-oil-patches-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 9 % → 42 % | 62.0 px | 0.13 | 4.82 | 94 |
| stroke 2 | 9 % → 29 % | 62.8 px | 0.13 | 3.15 | 73 |
| stroke 3 | 7 % → 35 % | 62.3 px | 0.13 | 4.72 | 65 |
| stroke 4 | 16 % → 20 % | 132.0 px | 0.12 | 1.27 | 56 |
| stroke 5 | 23 % → 33 % | 124.6 px | 0.13 | 1.43 | 90 |
| stroke 6 | 20 % → 38 % | 171.5 px | 0.13 | 1.90 | 62 |
| stroke 7 | 30 % → 35 % | 237.9 px | 0.13 | 1.18 | 69 |
| stroke 8 | 33 % → 39 % | 235.1 px | 0.13 | 1.18 | 85 |
| stroke 9 | 25 % → 26 % | 159.7 px | 0.13 | 1.07 | 88 |
| stroke 10 | 29 % → 29 % | 257.3 px | 0.13 | 1.00 | 66 |
| stroke 11 | 36 % → 36 % | 324.7 px | 0.13 | 1.00 | 61 |
| stroke 12 | 26 % → 26 % | 184.5 px | 0.13 | 1.00 | 64 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #35 Red band with runs — own sheet
own sheet 600 × 600 · Watercolor · 70 px · 6.0 s

![Brush Artist · Refs · #35 Red band with runs — own sheet](Brush-Artist-Refs-35-Red-band-with-runs-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 25 % → 37 % | 93.7 px | 0.51 | 1.48 | 330 |

## Brush Artist · Refs · #36 Magenta letters flat brush — own sheet
own sheet 600 × 600 · Gouache · 36 px · 10.6 s

![Brush Artist · Refs · #36 Magenta letters flat brush — own sheet](Brush-Artist-Refs-36-Magenta-letters-flat-brush-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 20 % → 39 % | 59.1 px | 0.50 | 1.95 | 33 |
| stroke 2 | 20 % → 32 % | 46.7 px | 0.50 | 1.59 | 32 |
| stroke 3 | 29 % → 54 % | 86.9 px | 0.50 | 1.86 | 33 |
| stroke 4 | 26 % → 44 % | 51.3 px | 0.50 | 1.67 | 105 |
| stroke 5 | 33 % → 55 % | 96.2 px | 0.50 | 1.67 | 70 |
| stroke 6 | 42 % → 56 % | 242.7 px | 0.50 | 1.33 | 15 |
| stroke 7 | 30 % → 44 % | 56.8 px | 0.50 | 1.45 | 108 |
| stroke 8 | 31 % → 53 % | 98.5 px | 0.50 | 1.68 | 62 |
| stroke 9 | 38 % → 51 % | 158.3 px | 0.50 | 1.33 | 29 |
| stroke 10 | 37 % → 64 % | 106.7 px | 0.50 | 1.72 | 70 |
| stroke 11 | 39 % → 62 % | 225.8 px | 0.50 | 1.58 | 16 |
| stroke 12 | 43 % → 56 % | 81.9 px | 0.50 | 1.29 | 141 |
| stroke 13 | 33 % → 46 % | 117.7 px | 0.50 | 1.43 | 49 |
| stroke 14 | 35 % → 52 % | 134.5 px | 0.50 | 1.47 | 44 |
| stroke 15 | 38 % → 56 % | 108.6 px | 0.50 | 1.49 | 103 |
| stroke 16 | 41 % → 50 % | 232.0 px | 0.50 | 1.23 | 16 |
| stroke 17 | 44 % → 52 % | 81.7 px | 0.50 | 1.19 | 140 |
| stroke 18 | 27 % → 36 % | 97.6 px | 0.50 | 1.35 | 30 |
| stroke 19 | 40 % → 39 % | 117.2 px | 0.50 | 0.96 | 34 |
| stroke 20 | 45 % → 45 % | 132.3 px | 0.50 | 0.99 | 39 |
| stroke 21 | 41 % → 39 % | 78.7 px | 0.50 | 0.96 | 80 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #37 Oil still life dabs — own sheet
own sheet 600 × 600 · Oil · 40 px · 3.4 s

![Brush Artist · Refs · #37 Oil still life dabs — own sheet](Brush-Artist-Refs-37-Oil-still-life-dabs-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 7 % → 7 % | 44.1 px | 0.39 | 1.00 | 30 |
| stroke 2 | 6 % → 27 % | 44.4 px | 0.39 | 4.43 | 22 |
| stroke 3 | 12 % → 36 % | 92.6 px | 0.39 | 3.01 | 18 |
| stroke 4 | 9 % → 9 % | 42.8 px | 0.39 | 1.00 | 39 |
| stroke 5 | 6 % → 10 % | 43.2 px | 0.39 | 1.71 | 21 |
| stroke 6 | 13 % → 31 % | 83.4 px | 0.39 | 2.32 | 28 |
| stroke 7 | 11 % → 24 % | 115.5 px | 0.39 | 2.18 | 13 |
| stroke 8 | 8 % → 14 % | 89.7 px | 0.39 | 1.63 | 14 |
| stroke 9 | 13 % → 14 % | 68.1 px | 0.38 | 1.09 | 34 |
| stroke 10 | 21 % → 25 % | 106.5 px | 0.39 | 1.20 | 36 |
| stroke 11 | 24 % → 28 % | 201.7 px | 0.39 | 1.17 | 19 |
| stroke 12 | 21 % → 21 % | 227.4 px | 0.39 | 1.01 | 13 |
| stroke 13 | 16 % → 16 % | 167.7 px | 0.40 | 1.00 | 14 |
| stroke 14 | 16 % → 16 % | 132.7 px | 0.39 | 1.00 | 17 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #38 Sanguine drawing — own sheet
own sheet 600 × 600 · Pastel · 6 px · 2.2 s

![Brush Artist · Refs · #38 Sanguine drawing — own sheet](Brush-Artist-Refs-38-Sanguine-drawing-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 3 % → 14 % | 2.9 px | 0.57 | 5.29 | 7 |
| stroke 2 | 3 % → 7 % | 2.9 px | 0.57 | 2.89 | 6 |
| stroke 3 | 3 % → 9 % | 2.9 px | 0.57 | 3.40 | 6 |
| stroke 4 | 2 % → 17 % | 2.7 px | 0.57 | 7.20 | 6 |
| stroke 5 | 2 % → 7 % | 2.7 px | 0.57 | 3.03 | 6 |
| stroke 6 | 3 % → 19 % | 3.4 px | 0.57 | 6.31 | 6 |
| stroke 7 | 5 % → 14 % | 5.2 px | 0.57 | 3.07 | 8 |
| stroke 8 | 4 % → 16 % | 4.7 px | 0.57 | 3.79 | 6 |
| stroke 9 | 3 % → 7 % | 2.9 px | 0.57 | 2.66 | 6 |
| stroke 10 | 4 % → 16 % | 4.7 px | 0.57 | 3.83 | 6 |
| stroke 11 | 3 % → 4 % | 2.9 px | 0.57 | 1.61 | 6 |
| stroke 12 | 4 % → 15 % | 4.8 px | 0.57 | 3.58 | 6 |
| stroke 13 | 8 % → 17 % | 8.9 px | 0.57 | 2.23 | 6 |
| stroke 14 | 4 % → 14 % | 4.9 px | 0.57 | 3.19 | 6 |
| stroke 15 | 9 % → 18 % | 10.7 px | 0.57 | 1.86 | 6 |
| stroke 16 | 6 % → 16 % | 6.6 px | 0.57 | 2.71 | 7 |
| stroke 17 | 4 % → 9 % | 4.4 px | 0.57 | 2.25 | 6 |
| stroke 18 | 3 % → 5 % | 2.9 px | 0.57 | 1.85 | 9 |
| stroke 19 | 6 % → 16 % | 6.9 px | 0.57 | 2.68 | 6 |
| stroke 20 | 8 % → 14 % | 9.2 px | 0.57 | 1.70 | 6 |
| stroke 21 | 4 % → 4 % | 4.3 px | 0.57 | 1.00 | 6 |
| stroke 22 | 8 % → 13 % | 8.6 px | 0.57 | 1.79 | 6 |
| stroke 23 | 7 % → 12 % | 8.3 px | 0.57 | 1.61 | 6 |
| stroke 24 | 4 % → 7 % | 4.7 px | 0.57 | 1.71 | 6 |
| stroke 25 | 8 % → 14 % | 8.7 px | 0.57 | 1.84 | 7 |
| stroke 26 | 6 % → 8 % | 6.5 px | 0.57 | 1.34 | 6 |
| stroke 27 | 4 % → 4 % | 4.3 px | 0.57 | 1.10 | 6 |
| stroke 28 | 7 % → 11 % | 8.2 px | 0.57 | 1.59 | 6 |
| stroke 29 | 8 % → 17 % | 8.8 px | 0.57 | 2.21 | 6 |
| stroke 30 | 13 % → 17 % | 14.9 px | 0.57 | 1.29 | 6 |
| stroke 31 | 5 % → 6 % | 5.4 px | 0.57 | 1.29 | 6 |
| stroke 32 | 10 % → 13 % | 11.8 px | 0.57 | 1.24 | 6 |
| stroke 33 | 7 % → 8 % | 8.5 px | 0.57 | 1.07 | 6 |
| stroke 34 | 11 % → 14 % | 12.0 px | 0.57 | 1.36 | 6 |
| stroke 35 | 9 % → 14 % | 10.0 px | 0.57 | 1.61 | 6 |
| stroke 36 | 10 % → 13 % | 11.4 px | 0.57 | 1.26 | 6 |
| stroke 37 | 9 % → 16 % | 10.5 px | 0.57 | 1.71 | 6 |
| stroke 38 | 13 % → 19 % | 14.8 px | 0.57 | 1.48 | 6 |
| stroke 39 | 14 % → 17 % | 15.7 px | 0.57 | 1.21 | 6 |
| stroke 40 | 6 % → 7 % | 7.2 px | 0.57 | 1.14 | 6 |
| stroke 41 | 16 % → 16 % | 17.7 px | 0.57 | 1.01 | 6 |
| stroke 42 | 14 % → 16 % | 15.2 px | 0.57 | 1.17 | 6 |
| stroke 43 | 10 % → 12 % | 11.6 px | 0.57 | 1.17 | 6 |
| stroke 44 | 12 % → 15 % | 14.3 px | 0.57 | 1.22 | 6 |
| stroke 45 | 2 % → 2 % | 2.7 px | 0.57 | 1.00 | 6 |
| stroke 46 | 16 % → 16 % | 18.5 px | 0.57 | 1.00 | 6 |
| stroke 47 | 13 % → 13 % | 15.0 px | 0.57 | 1.00 | 6 |
| stroke 48 | 12 % → 13 % | 14.3 px | 0.57 | 1.07 | 6 |
| stroke 49 | 19 % → 19 % | 21.5 px | 0.57 | 1.00 | 6 |
| stroke 50 | 10 % → 10 % | 11.6 px | 0.57 | 1.00 | 6 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #39 Very thick impasto — own sheet
own sheet 600 × 600 · Heavy acrylic · 60 px · 4.3 s

![Brush Artist · Refs · #39 Very thick impasto — own sheet](Brush-Artist-Refs-39-Very-thick-impasto-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 26 % → 37 % | 59.6 px | 0.43 | 1.42 | 256 |
| stroke 2 | 31 % → 48 % | 93.9 px | 0.44 | 1.54 | 261 |
| stroke 3 | 37 % → 49 % | 124.6 px | 0.43 | 1.33 | 238 |
| stroke 4 | 31 % → 44 % | 90.9 px | 0.44 | 1.41 | 270 |
| stroke 5 | 42 % → 41 % | 104.2 px | 0.44 | 0.98 | 262 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #40 Watercolour blooms — own sheet
own sheet 600 × 600 · Watercolor · 90 px · 6.3 s

![Brush Artist · Refs · #40 Watercolour blooms — own sheet](Brush-Artist-Refs-40-Watercolour-blooms-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 21 % → 26 % | 93.0 px | 0.12 | 1.25 | 632 |

## Brush Artist · Refs · #41 Coloured pencil hatching — own sheet
own sheet 600 × 600 · Pastel · 4 px · 2.5 s

![Brush Artist · Refs · #41 Coloured pencil hatching — own sheet](Brush-Artist-Refs-41-Coloured-pencil-hatching-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 3 % → 13 % | 2.2 px | 0.35 | 4.64 | 5 |
| stroke 2 | 3 % → 7 % | 2.3 px | 0.35 | 2.29 | 4 |
| stroke 3 | 2 % → 11 % | 1.9 px | 0.35 | 4.38 | 4 |
| stroke 4 | 3 % → 19 % | 2.1 px | 0.35 | 6.73 | 4 |
| stroke 5 | 4 % → 7 % | 2.9 px | 0.35 | 1.83 | 4 |
| stroke 6 | 3 % → 13 % | 2.3 px | 0.35 | 4.19 | 4 |
| stroke 7 | 3 % → 15 % | 2.6 px | 0.35 | 4.43 | 4 |
| stroke 8 | 3 % → 12 % | 2.1 px | 0.35 | 4.20 | 4 |
| stroke 9 | 5 % → 11 % | 3.6 px | 0.35 | 2.27 | 5 |
| stroke 10 | 5 % → 15 % | 3.8 px | 0.35 | 2.99 | 5 |
| stroke 11 | 4 % → 13 % | 3.0 px | 0.35 | 3.28 | 4 |
| stroke 12 | 3 % → 3 % | 2.1 px | 0.35 | 1.00 | 4 |
| stroke 13 | 7 % → 17 % | 5.2 px | 0.35 | 2.45 | 4 |
| stroke 14 | 3 % → 13 % | 2.4 px | 0.35 | 4.19 | 4 |
| stroke 15 | 6 % → 12 % | 4.4 px | 0.35 | 2.09 | 4 |
| stroke 16 | 7 % → 11 % | 5.1 px | 0.35 | 1.61 | 4 |
| stroke 17 | 3 % → 3 % | 2.1 px | 0.35 | 1.00 | 4 |
| stroke 18 | 5 % → 8 % | 3.6 px | 0.35 | 1.65 | 4 |
| stroke 19 | 5 % → 13 % | 3.8 px | 0.35 | 2.72 | 4 |
| stroke 20 | 5 % → 14 % | 3.7 px | 0.35 | 2.92 | 5 |
| stroke 21 | 4 % → 13 % | 3.2 px | 0.35 | 3.20 | 4 |
| stroke 22 | 9 % → 16 % | 6.8 px | 0.35 | 1.77 | 4 |
| stroke 23 | 9 % → 13 % | 6.5 px | 0.35 | 1.55 | 4 |
| stroke 24 | 6 % → 14 % | 4.7 px | 0.35 | 2.18 | 4 |
| stroke 25 | 5 % → 10 % | 3.5 px | 0.35 | 2.27 | 6 |
| stroke 26 | 3 % → 6 % | 2.7 px | 0.35 | 1.81 | 4 |
| stroke 27 | 3 % → 7 % | 2.3 px | 0.35 | 2.26 | 5 |
| stroke 28 | 6 % → 10 % | 4.5 px | 0.35 | 1.70 | 4 |
| stroke 29 | 3 % → 13 % | 2.4 px | 0.35 | 4.21 | 4 |
| stroke 30 | 6 % → 9 % | 4.4 px | 0.35 | 1.46 | 4 |
| stroke 31 | 7 % → 14 % | 5.1 px | 0.35 | 2.14 | 4 |
| stroke 32 | 3 % → 6 % | 2.5 px | 0.35 | 1.79 | 4 |
| stroke 33 | 6 % → 11 % | 5.0 px | 0.35 | 1.67 | 4 |
| stroke 34 | 3 % → 6 % | 2.6 px | 0.35 | 1.73 | 4 |
| stroke 35 | 7 % → 14 % | 5.0 px | 0.35 | 2.09 | 4 |
| stroke 36 | 5 % → 5 % | 3.7 px | 0.35 | 1.01 | 4 |
| stroke 37 | 7 % → 15 % | 5.2 px | 0.35 | 2.15 | 4 |
| stroke 38 | 8 % → 13 % | 5.8 px | 0.35 | 1.66 | 4 |
| stroke 39 | 7 % → 11 % | 5.1 px | 0.35 | 1.67 | 4 |
| stroke 40 | 8 % → 18 % | 6.2 px | 0.35 | 2.21 | 4 |
| stroke 41 | 9 % → 13 % | 6.9 px | 0.35 | 1.48 | 4 |
| stroke 42 | 10 % → 17 % | 7.7 px | 0.35 | 1.73 | 4 |
| stroke 43 | 5 % → 9 % | 3.9 px | 0.35 | 1.66 | 4 |
| stroke 44 | 10 % → 13 % | 7.3 px | 0.35 | 1.40 | 4 |
| stroke 45 | 13 % → 18 % | 9.9 px | 0.35 | 1.35 | 4 |
| stroke 46 | 5 % → 7 % | 3.6 px | 0.34 | 1.41 | 4 |
| stroke 47 | 11 % → 13 % | 8.0 px | 0.35 | 1.20 | 4 |
| stroke 48 | 12 % → 16 % | 9.2 px | 0.35 | 1.34 | 4 |
| stroke 49 | 6 % → 9 % | 4.2 px | 0.35 | 1.66 | 4 |
| stroke 50 | 7 % → 7 % | 5.2 px | 0.34 | 1.00 | 4 |
| stroke 51 | 8 % → 15 % | 6.4 px | 0.35 | 1.74 | 4 |
| stroke 52 | 12 % → 14 % | 9.1 px | 0.35 | 1.19 | 4 |
| stroke 53 | 11 % → 14 % | 8.1 px | 0.35 | 1.36 | 4 |
| stroke 54 | 10 % → 14 % | 7.4 px | 0.35 | 1.47 | 4 |
| stroke 55 | 11 % → 14 % | 8.2 px | 0.35 | 1.33 | 4 |
| stroke 56 | 11 % → 12 % | 8.4 px | 0.35 | 1.11 | 4 |
| stroke 57 | 9 % → 13 % | 7.1 px | 0.35 | 1.37 | 5 |
| stroke 58 | 10 % → 11 % | 7.7 px | 0.35 | 1.14 | 6 |
| stroke 59 | 11 % → 13 % | 8.4 px | 0.35 | 1.18 | 4 |
| stroke 60 | 16 % → 20 % | 11.9 px | 0.35 | 1.26 | 4 |
| stroke 61 | 19 % → 20 % | 14.5 px | 0.35 | 1.04 | 4 |
| stroke 62 | 10 % → 10 % | 7.3 px | 0.35 | 1.00 | 4 |
| stroke 63 | 11 % → 12 % | 8.7 px | 0.35 | 1.07 | 4 |
| stroke 64 | 14 % → 14 % | 10.7 px | 0.35 | 1.02 | 4 |
| stroke 65 | 15 % → 15 % | 11.5 px | 0.35 | 1.00 | 4 |
| stroke 66 | 14 % → 14 % | 10.7 px | 0.35 | 1.00 | 4 |
| stroke 67 | 12 % → 12 % | 8.8 px | 0.35 | 1.06 | 4 |
| stroke 68 | 5 % → 9 % | 3.6 px | 0.35 | 1.88 | 4 |
| stroke 69 | 5 % → 5 % | 4.1 px | 0.35 | 1.00 | 4 |
| stroke 70 | 10 % → 13 % | 7.4 px | 0.35 | 1.28 | 4 |
| stroke 71 | 9 % → 11 % | 7.1 px | 0.35 | 1.15 | 4 |
| stroke 72 | 5 % → 7 % | 4.2 px | 0.35 | 1.23 | 4 |
| stroke 73 | 12 % → 12 % | 9.3 px | 0.35 | 1.00 | 4 |
| stroke 74 | 14 % → 14 % | 10.8 px | 0.35 | 1.00 | 4 |
| stroke 75 | 15 % → 15 % | 11.4 px | 0.35 | 1.00 | 4 |
| stroke 76 | 14 % → 14 % | 10.5 px | 0.35 | 1.00 | 4 |
| stroke 77 | 7 % → 10 % | 5.4 px | 0.35 | 1.34 | 5 |
| stroke 78 | 9 % → 9 % | 7.0 px | 0.35 | 1.00 | 4 |
| stroke 79 | 7 % → 7 % | 5.7 px | 0.35 | 1.00 | 4 |
| stroke 80 | 11 % → 11 % | 8.3 px | 0.35 | 1.00 | 5 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #42 Oil pastel shaggy — own sheet
own sheet 600 × 600 · Pastel · 18 px · 3.4 s

![Brush Artist · Refs · #42 Oil pastel shaggy — own sheet](Brush-Artist-Refs-42-Oil-pastel-shaggy-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 5 % → 27 % | 8.0 px | 0.28 | 5.73 | 10 |
| stroke 2 | 5 % → 24 % | 8.6 px | 0.28 | 4.69 | 9 |
| stroke 3 | 5 % → 29 % | 8.9 px | 0.28 | 5.42 | 10 |
| stroke 4 | 5 % → 11 % | 8.8 px | 0.28 | 2.08 | 10 |
| stroke 5 | 6 % → 11 % | 9.9 px | 0.28 | 1.85 | 10 |
| stroke 6 | 8 % → 37 % | 13.9 px | 0.29 | 4.44 | 9 |
| stroke 7 | 11 % → 31 % | 17.6 px | 0.28 | 2.90 | 10 |
| stroke 8 | 7 % → 38 % | 11.4 px | 0.28 | 5.55 | 13 |
| stroke 9 | 8 % → 21 % | 13.9 px | 0.28 | 2.53 | 16 |
| stroke 10 | 8 % → 18 % | 13.2 px | 0.28 | 2.32 | 12 |
| stroke 11 | 6 % → 27 % | 9.4 px | 0.28 | 4.74 | 12 |
| stroke 12 | 8 % → 19 % | 13.6 px | 0.28 | 2.29 | 11 |
| stroke 13 | 13 % → 24 % | 21.0 px | 0.28 | 1.92 | 15 |
| stroke 14 | 5 % → 23 % | 7.9 px | 0.28 | 4.77 | 13 |
| stroke 15 | 5 % → 24 % | 9.0 px | 0.29 | 4.38 | 11 |
| stroke 16 | 9 % → 21 % | 15.7 px | 0.29 | 2.18 | 11 |
| stroke 17 | 17 % → 39 % | 27.9 px | 0.29 | 2.34 | 10 |
| stroke 18 | 14 % → 25 % | 22.8 px | 0.29 | 1.79 | 9 |
| stroke 19 | 15 % → 32 % | 24.9 px | 0.28 | 2.09 | 11 |
| stroke 20 | 21 % → 39 % | 35.1 px | 0.28 | 1.85 | 10 |
| stroke 21 | 9 % → 16 % | 14.4 px | 0.28 | 1.88 | 10 |
| stroke 22 | 14 % → 17 % | 23.9 px | 0.28 | 1.20 | 9 |
| stroke 23 | 12 % → 17 % | 20.6 px | 0.29 | 1.34 | 10 |
| stroke 24 | 18 % → 26 % | 30.0 px | 0.29 | 1.44 | 9 |
| stroke 25 | 20 % → 34 % | 32.6 px | 0.28 | 1.74 | 9 |
| stroke 26 | 6 % → 14 % | 9.2 px | 0.28 | 2.43 | 10 |
| stroke 27 | 18 % → 26 % | 30.4 px | 0.29 | 1.41 | 9 |
| stroke 28 | 14 % → 24 % | 23.7 px | 0.28 | 1.68 | 9 |
| stroke 29 | 9 % → 27 % | 14.9 px | 0.29 | 3.01 | 9 |
| stroke 30 | 15 % → 36 % | 24.9 px | 0.29 | 2.43 | 9 |
| stroke 31 | 14 % → 17 % | 23.3 px | 0.28 | 1.23 | 10 |
| stroke 32 | 16 % → 29 % | 27.0 px | 0.29 | 1.82 | 10 |
| stroke 33 | 15 % → 16 % | 24.5 px | 0.29 | 1.09 | 10 |
| stroke 34 | 19 % → 27 % | 31.4 px | 0.28 | 1.44 | 10 |
| stroke 35 | 26 % → 36 % | 42.5 px | 0.28 | 1.40 | 10 |
| stroke 36 | 25 % → 34 % | 41.0 px | 0.28 | 1.36 | 9 |
| stroke 37 | 12 % → 12 % | 19.3 px | 0.28 | 1.03 | 9 |
| stroke 38 | 19 % → 25 % | 31.7 px | 0.28 | 1.30 | 9 |
| stroke 39 | 16 % → 22 % | 27.3 px | 0.28 | 1.37 | 9 |
| stroke 40 | 22 % → 31 % | 36.6 px | 0.28 | 1.38 | 9 |
| stroke 41 | 32 % → 36 % | 53.1 px | 0.28 | 1.12 | 10 |
| stroke 42 | 23 % → 30 % | 38.1 px | 0.29 | 1.29 | 9 |
| stroke 43 | 12 % → 12 % | 20.3 px | 0.28 | 1.00 | 10 |
| stroke 44 | 30 % → 37 % | 48.9 px | 0.28 | 1.26 | 13 |
| stroke 45 | 16 % → 16 % | 26.2 px | 0.28 | 1.00 | 10 |
| stroke 46 | 29 % → 34 % | 47.9 px | 0.29 | 1.15 | 10 |
| stroke 47 | 38 % → 41 % | 62.0 px | 0.28 | 1.10 | 9 |
| stroke 48 | 29 % → 36 % | 47.8 px | 0.29 | 1.27 | 10 |
| stroke 49 | 27 % → 30 % | 45.1 px | 0.29 | 1.11 | 11 |
| stroke 50 | 38 % → 40 % | 63.4 px | 0.28 | 1.06 | 10 |
| stroke 51 | 16 % → 16 % | 26.0 px | 0.28 | 1.00 | 9 |
| stroke 52 | 37 % → 38 % | 62.4 px | 0.29 | 1.01 | 10 |
| stroke 53 | 22 % → 26 % | 36.9 px | 0.28 | 1.18 | 10 |
| stroke 54 | 17 % → 19 % | 29.0 px | 0.29 | 1.09 | 10 |
| stroke 55 | 15 % → 15 % | 25.0 px | 0.28 | 1.00 | 10 |
| stroke 56 | 13 % → 14 % | 21.6 px | 0.28 | 1.08 | 10 |
| stroke 57 | 23 % → 23 % | 37.7 px | 0.29 | 1.00 | 9 |
| stroke 58 | 28 % → 29 % | 46.1 px | 0.28 | 1.05 | 9 |
| stroke 59 | 40 % → 40 % | 67.3 px | 0.28 | 1.00 | 9 |
| stroke 60 | 22 % → 22 % | 35.6 px | 0.28 | 1.00 | 9 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #43 Dragged black ink blocks — own sheet
own sheet 600 × 600 · Gouache · 70 px · 8.0 s

![Brush Artist · Refs · #43 Dragged black ink blocks — own sheet](Brush-Artist-Refs-43-Dragged-black-ink-blocks-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 16 % → 12 % | 37.3 px | 0.46 | 0.73 | 505 |
| stroke 2 | 16 % → 13 % | 58.0 px | 0.46 | 0.78 | 858 |
| stroke 3 | 20 % → 16 % | 72.4 px | 0.46 | 0.79 | 488 |
| stroke 4 | 20 % → 16 % | 70.6 px | 0.46 | 0.77 | 427 |
| stroke 5 | 24 % → 14 % | 56.0 px | 0.46 | 0.57 | 423 |

## Brush Artist · Refs · #44 Blue looping ribbon — own sheet
own sheet 600 × 600 · Oil · 80 px · 5.4 s

![Brush Artist · Refs · #44 Blue looping ribbon — own sheet](Brush-Artist-Refs-44-Blue-looping-ribbon-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 32 % → 32 % | 42.2 px | 0.78 | 1.00 | 3275 |

## Brush Artist · Refs · #45 Soft pastel pepper — own sheet
own sheet 600 × 600 · Pastel · 40 px · 4.5 s

![Brush Artist · Refs · #45 Soft pastel pepper — own sheet](Brush-Artist-Refs-45-Soft-pastel-pepper-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 10 % → 39 % | 11.3 px | 0.49 | 3.75 | 493 |
| stroke 2 | 18 % → 34 % | 21.3 px | 0.49 | 1.87 | 365 |
| stroke 3 | 25 % → 37 % | 17.6 px | 0.49 | 1.46 | 308 |
| stroke 4 | 24 % → 35 % | 30.5 px | 0.49 | 1.43 | 338 |
| stroke 5 | 30 % → 30 % | 21.2 px | 0.49 | 1.00 | 219 |
| stroke 6 | 36 % → 44 % | 23.0 px | 0.48 | 1.23 | 293 |
| stroke 7 | 39 % → 43 % | 21.6 px | 0.48 | 1.10 | 340 |
| stroke 8 | 44 % → 44 % | 44.4 px | 0.49 | 1.00 | 305 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #46 Red-brown ink lips — own sheet
own sheet 600 × 600 · Watercolor · 50 px · 4.7 s

![Brush Artist · Refs · #46 Red-brown ink lips — own sheet](Brush-Artist-Refs-46-Red-brown-ink-lips-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 13 % → 25 % | 52.3 px | 0.60 | 1.97 | 94 |
| stroke 2 | 16 % → 29 % | 71.0 px | 0.56 | 1.78 | 75 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #47 Pink knife slabs — own sheet
own sheet 600 × 600 · Heavy acrylic · 90 px · 4.2 s

![Brush Artist · Refs · #47 Pink knife slabs — own sheet](Brush-Artist-Refs-47-Pink-knife-slabs-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 17 % → 32 % | 83.2 px | 0.11 | 1.94 | 268 |
| stroke 2 | 29 % → 43 % | 165.7 px | 0.11 | 1.46 | 265 |
| stroke 3 | 29 % → 43 % | 165.7 px | 0.11 | 1.47 | 264 |
| stroke 4 | 39 % → 38 % | 165.7 px | 0.11 | 0.98 | 265 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #48 Black bands with drips — own sheet
own sheet 600 × 600 · Gouache · 70 px · 11.2 s

![Brush Artist · Refs · #48 Black bands with drips — own sheet](Brush-Artist-Refs-48-Black-bands-with-drips-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 24 % → 38 % | 62.3 px | 0.39 | 1.57 | 490 |
| stroke 2 | 36 % → 50 % | 116.8 px | 0.39 | 1.39 | 452 |
| stroke 3 | 39 % → 51 % | 120.8 px | 0.39 | 1.32 | 441 |
| stroke 4 | 41 % → 39 % | 119.9 px | 0.39 | 0.96 | 425 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #49 Magenta letters round brush — own sheet
own sheet 600 × 600 · Ink · 30 px · 9.7 s

![Brush Artist · Refs · #49 Magenta letters round brush — own sheet](Brush-Artist-Refs-49-Magenta-letters-round-brush-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 27 % → 46 % | 64.3 px | 0.52 | 1.69 | 29 |
| stroke 2 | 29 % → 40 % | 52.5 px | 0.53 | 1.39 | 31 |
| stroke 3 | 41 % → 67 % | 96.4 px | 0.52 | 1.64 | 28 |
| stroke 4 | 34 % → 52 % | 53.7 px | 0.52 | 1.55 | 102 |
| stroke 5 | 40 % → 66 % | 94.8 px | 0.52 | 1.65 | 68 |
| stroke 6 | 54 % → 70 % | 231.2 px | 0.52 | 1.29 | 15 |
| stroke 7 | 41 % → 56 % | 63.9 px | 0.52 | 1.35 | 104 |
| stroke 8 | 36 % → 61 % | 91.9 px | 0.53 | 1.72 | 60 |
| stroke 9 | 49 % → 60 % | 152.9 px | 0.53 | 1.24 | 24 |
| stroke 10 | 42 % → 72 % | 100.5 px | 0.52 | 1.71 | 67 |
| stroke 11 | 52 % → 72 % | 219.5 px | 0.52 | 1.39 | 15 |
| stroke 12 | 53 % → 68 % | 82.2 px | 0.52 | 1.29 | 104 |
| stroke 13 | 42 % → 54 % | 116.0 px | 0.53 | 1.29 | 42 |
| stroke 14 | 45 % → 69 % | 131.9 px | 0.53 | 1.52 | 36 |
| stroke 15 | 43 % → 63 % | 102.4 px | 0.52 | 1.46 | 102 |
| stroke 16 | 52 % → 61 % | 220.2 px | 0.52 | 1.18 | 23 |
| stroke 17 | 53 % → 64 % | 82.3 px | 0.52 | 1.19 | 148 |
| stroke 18 | 36 % → 44 % | 99.6 px | 0.52 | 1.21 | 40 |
| stroke 19 | 54 % → 53 % | 123.8 px | 0.52 | 0.99 | 34 |
| stroke 20 | 54 % → 54 % | 125.3 px | 0.52 | 1.00 | 37 |
| stroke 21 | 49 % → 49 % | 81.3 px | 0.52 | 1.00 | 94 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #50 Thick swipes on photo — own sheet
own sheet 600 × 600 · Heavy acrylic · 40 px · 3.1 s

![Brush Artist · Refs · #50 Thick swipes on photo — own sheet](Brush-Artist-Refs-50-Thick-swipes-on-photo-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 9 % → 21 % | 42.7 px | 0.33 | 2.34 | 34 |
| stroke 2 | 9 % → 16 % | 42.4 px | 0.33 | 1.79 | 27 |
| stroke 3 | 10 % → 11 % | 41.8 px | 0.33 | 1.06 | 39 |
| stroke 4 | 11 % → 18 % | 42.6 px | 0.33 | 1.64 | 32 |
| stroke 5 | 11 % → 10 % | 41.9 px | 0.33 | 0.95 | 34 |
| stroke 6 | 17 % → 21 % | 97.3 px | 0.32 | 1.20 | 27 |
| stroke 7 | 22 % → 26 % | 92.7 px | 0.33 | 1.18 | 38 |
| stroke 8 | 21 % → 21 % | 119.6 px | 0.33 | 0.97 | 29 |
| stroke 9 | 9 % → 10 % | 42.0 px | 0.32 | 1.09 | 36 |
| stroke 10 | 22 % → 21 % | 73.6 px | 0.32 | 0.96 | 37 |
| stroke 11 | 9 % → 8 % | 42.6 px | 0.33 | 0.95 | 30 |
| stroke 12 | 17 % → 16 % | 93.0 px | 0.33 | 0.96 | 20 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Ink — dry brush — own sheet
own sheet 600 × 600 · Gouache · 30 px · 3.0 s

![Brush Artist · Ink — dry brush — own sheet](Brush-Artist-Ink-dry-brush-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| ear | 6 % → 3 % | 7.8 px | 0.86 | 0.44 | 512 |
| drag0 | 6 % → 8 % | 10.2 px | 0.86 | 1.39 | 118 |
| drag1 | 8 % → 8 % | 16.5 px | 0.86 | 1.02 | 99 |
| drag2 | 10 % → 9 % | 22.5 px | 0.86 | 0.87 | 83 |
| drag3 | 12 % → 9 % | 29.4 px | 0.86 | 0.78 | 66 |

## Brush Artist · Watercolour — blue — own sheet
own sheet 600 × 600 · Watercolor · 40 px · 9.8 s

![Brush Artist · Watercolour — blue — own sheet](Brush-Artist-Watercolour-blue-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| s0 | 7 % → 23 % | 28.4 px | 0.25 | 3.20 | 39 |
| s1 | 5 % → 32 % | 9.9 px | 0.38 | 5.85 | 50 |
| s2 | 10 % → 18 % | 43.5 px | 0.19 | 1.75 | 34 |
| s3 | 9 % → 17 % | 26.3 px | 0.28 | 1.85 | 46 |
| s4 | 14 % → 29 % | 37.9 px | 0.36 | 2.11 | 58 |
| s5 | 19 % → 29 % | 38.9 px | 0.37 | 1.52 | 61 |
| s6 | 17 % → 21 % | 47.6 px | 0.27 | 1.22 | 52 |
| s7 | 24 % → 35 % | 31.9 px | 0.37 | 1.44 | 42 |
| s8 | 20 % → 24 % | 77.5 px | 0.27 | 1.18 | 51 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Charcoal — stick — own sheet
own sheet 600 × 600 · Charcoal · 28 px · 1.2 s

![Brush Artist · Charcoal — stick — own sheet](Brush-Artist-Charcoal-stick-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| finger0 | 9 % → 18 % | 15.5 px | 0.83 | 2.01 | 28 |
| tip0 | 8 % → 14 % | 22.1 px | 0.83 | 1.75 | 8 |
| finger1 | 17 % → 29 % | 29.4 px | 0.83 | 1.74 | 26 |
| tip1 | 15 % → 21 % | 39.1 px | 0.83 | 1.42 | 8 |
| finger2 | 17 % → 25 % | 29.5 px | 0.83 | 1.53 | 25 |
| tip2 | 14 % → 20 % | 39.0 px | 0.83 | 1.41 | 8 |
| finger3 | 16 % → 19 % | 29.3 px | 0.83 | 1.16 | 25 |
| tip3 | 15 % → 15 % | 39.0 px | 0.83 | 1.00 | 8 |
| cig0 | 25 % → 35 % | 54.8 px | 0.83 | 1.41 | 10 |
| cig1 | 26 % → 35 % | 58.8 px | 0.83 | 1.32 | 9 |
| cig2 | 28 % → 35 % | 63.2 px | 0.83 | 1.22 | 9 |
| cig3 | 30 % → 34 % | 67.3 px | 0.83 | 1.14 | 10 |
| cig4 | 32 % → 34 % | 71.5 px | 0.83 | 1.06 | 10 |
| cig5 | 34 % → 34 % | 75.3 px | 0.83 | 1.00 | 10 |

Numbers say: wet paint spreads well beyond the stroke.

