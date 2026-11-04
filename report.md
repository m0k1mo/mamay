![All brushes](contact.png)

# Brush Lab — 150 brushes · Nov 4, 2026 at 7:46 AM

Every sheet: 1500 × 600, ten strokes in a 5 × 2 grid — 1. light line · 2. heavy line · 3. pressure swell · 4. fast wave · 5. slow wave · 6. spiral · 7. loop · 8. tilted · 9. over the wet one · 10. long, no reload (cell 8 holds «tilted» and «over the wet one» crossed). The CPU reference of Mamay's paint engine; the wet layer settles 20 s at the end.

Columns: **covered** = share of the cell with paint right after the stroke → after settling; **width** = painted area of the stroke ÷ its length (px); **dark** = mean darkness of the painted pixels above the paper's own grain (0 = paper, 1 = black); **spread** = how far wet paint went beyond the stroke (1.0 = stayed); **ms** = the stroke on the CPU; long stroke: paint in each quarter of its length (it should run out: wet → streaks → dry tail).

## Ink Line
Ink · 12 px · 27.9 s

![Ink Line](Ink-Line.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 1 % → 4 % | 4.3 px | 0.55 | 2.44 | 59 |
| heavy line | 5 % → 6 % | 15.7 px | 0.68 | 1.13 | 99 |
| pressure swell | 3 % → 4 % | 11.3 px | 0.64 | 1.40 | 103 |
| fast wave | 10 % → 11 % | 11.2 px | 0.59 | 1.11 | 216 |
| slow wave | 8 % → 10 % | 9.6 px | 0.57 | 1.16 | 158 |
| spiral | 14 % → 15 % | 8.9 px | 0.50 | 1.07 | 273 |
| loop | 8 % → 9 % | 10.6 px | 0.61 | 1.16 | 144 |
| tilted | 5 % → 5 % | 14.4 px | 0.65 | 1.05 | 81 |
| over the wet one | 10 % → 11 % | 12.5 px | 0.65 | 1.15 | 58 |
| long, no reload | 18 % → 17 % | 8.1 px | 0.47 | 0.96 | 414 | quarters: 0.22 → 0.09 → 0.04 → 0.02

Numbers say: light vs heavy: width 4.3 → 15.7 px, dark 0.55 → 0.68; wet paint spreads well beyond the stroke.

## Dense Ink
Ink · 14 px · 28.3 s

![Dense Ink](Dense-Ink.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 5 % → 7 % | 15.2 px | 0.72 | 1.26 | 74 |
| heavy line | 7 % → 7 % | 19.1 px | 0.73 | 1.09 | 163 |
| pressure swell | 5 % → 6 % | 17.9 px | 0.72 | 1.17 | 90 |
| fast wave | 13 % → 13 % | 15.3 px | 0.69 | 1.01 | 214 |
| slow wave | 12 % → 12 % | 13.6 px | 0.67 | 1.04 | 184 |
| spiral | 18 % → 15 % | 12.2 px | 0.65 | 0.80 | 317 |
| loop | 11 % → 12 % | 14.8 px | 0.69 | 1.08 | 172 |
| tilted | 5 % → 6 % | 14.6 px | 0.72 | 1.07 | 69 |
| over the wet one | 12 % → 13 % | 17.7 px | 0.72 | 1.11 | 67 |
| long, no reload | 23 % → 15 % | 10.1 px | 0.64 | 0.66 | 442 | quarters: 0.30 → 0.12 → 0.04 → 0.02

Numbers say: light vs heavy: width 15.2 → 19.1 px, dark 0.72 → 0.73.

## Transparent Wash
Watercolor · 22 px · 29.3 s

![Transparent Wash](Transparent-Wash.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 2 % → 5 % | 6.9 px | 0.27 | 2.25 | 61 |
| heavy line | 7 % → 9 % | 20.4 px | 0.27 | 1.22 | 94 |
| pressure swell | 4 % → 6 % | 15.2 px | 0.28 | 1.54 | 94 |
| fast wave | 14 % → 16 % | 16.1 px | 0.20 | 1.17 | 221 |
| slow wave | 12 % → 15 % | 13.7 px | 0.21 | 1.28 | 223 |
| spiral | 18 % → 22 % | 11.9 px | 0.16 | 1.23 | 249 |
| loop | 11 % → 13 % | 14.5 px | 0.22 | 1.20 | 143 |
| tilted | 8 % → 8 % | 21.1 px | 0.24 | 1.06 | 81 |
| over the wet one | 13 % → 16 % | 16.4 px | 0.24 | 1.18 | 63 |
| long, no reload | 26 % → 32 % | 11.6 px | 0.13 | 1.22 | 383 | quarters: 0.11 → 0.04 → 0.02 → 0.01

Numbers say: light vs heavy: width 6.9 → 20.4 px, dark 0.27 → 0.27; wet paint spreads well beyond the stroke.

## Dry Brush
Gouache · 24 px · 22.5 s

![Dry Brush](Dry-Brush.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 5 % → 0 % | 14.0 px | 0.65 | 0.09 | 58 |
| heavy line | 6 % → 0 % | 18.6 px | 0.65 | 0.02 | 97 |
| pressure swell | 5 % → 0 % | 18.2 px | 0.65 | 0.08 | 62 |
| fast wave | 6 % → 1 % | 7.3 px | 0.65 | 0.08 | 164 |
| slow wave | 7 % → 0 % | 8.1 px | 0.65 | 0.06 | 273 |
| spiral | 7 % → 0 % | 4.6 px | 0.65 | 0.07 | 259 |
| loop | 10 % → 0 % | 12.4 px | 0.65 | 0.04 | 145 |
| tilted | 4 % → 3 % | 10.6 px | 0.65 | 0.88 | 74 |
| over the wet one | 9 % → 1 % | 14.5 px | 0.65 | 0.12 | 66 |
| long, no reload | 6 % → 1 % | 2.9 px | 0.65 | 0.14 | 347 | quarters: 0.12 → 0.00 → 0.00 → 0.00

Numbers say: light vs heavy: width 14.0 → 18.6 px, dark 0.65 → 0.65.

## Wax Crayon
Wax · 8 px · 9.8 s

![Wax Crayon](Wax-Crayon.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 1 % → 1 % | 2.5 px | 0.71 | 1.00 | 25 |
| heavy line | 1 % → 1 % | 3.9 px | 0.69 | 1.00 | 34 |
| pressure swell | 1 % → 1 % | 3.3 px | 0.70 | 1.00 | 14 |
| fast wave | 3 % → 3 % | 3.5 px | 0.69 | 1.00 | 49 |
| slow wave | 3 % → 3 % | 3.4 px | 0.70 | 1.00 | 49 |
| spiral | 5 % → 5 % | 3.3 px | 0.70 | 1.00 | 87 |
| loop | 3 % → 3 % | 3.3 px | 0.70 | 1.00 | 47 |
| tilted | 2 % → 2 % | 5.6 px | 0.68 | 1.00 | 37 |
| over the wet one | 3 % → 3 % | 3.6 px | 0.68 | 1.00 | 23 |
| long, no reload | 7 % → 7 % | 3.3 px | 0.70 | 1.00 | 115 | quarters: 0.06 → 0.06 → 0.06 → 0.06

Numbers say: light vs heavy: width 2.5 → 3.9 px, dark 0.71 → 0.69; the long stroke does not run out of paint.

## Oil Pastel
Wax · 12 px · 10.8 s

![Oil Pastel](Oil-Pastel.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 1 % → 1 % | 4.0 px | 0.68 | 1.00 | 33 |
| heavy line | 2 % → 2 % | 6.5 px | 0.68 | 1.00 | 33 |
| pressure swell | 2 % → 2 % | 5.7 px | 0.69 | 1.00 | 20 |
| fast wave | 5 % → 5 % | 5.7 px | 0.68 | 1.00 | 86 |
| slow wave | 5 % → 5 % | 5.5 px | 0.68 | 1.00 | 61 |
| spiral | 8 % → 8 % | 5.5 px | 0.68 | 1.00 | 120 |
| loop | 4 % → 4 % | 5.6 px | 0.68 | 1.00 | 60 |
| tilted | 2 % → 2 % | 6.8 px | 0.68 | 1.00 | 41 |
| over the wet one | 5 % → 5 % | 5.8 px | 0.68 | 1.00 | 26 |
| long, no reload | 13 % → 13 % | 5.6 px | 0.68 | 1.00 | 163 | quarters: 0.10 → 0.09 → 0.10 → 0.10

Numbers say: light vs heavy: width 4.0 → 6.5 px, dark 0.68 → 0.68; the long stroke does not run out of paint.

## Charcoal
Charcoal · 5 px · 11.9 s

![Charcoal](Charcoal.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 1 % → 1 % | 2.0 px | 0.74 | 1.00 | 14 |
| heavy line | 1 % → 1 % | 3.0 px | 0.74 | 1.00 | 28 |
| pressure swell | 1 % → 1 % | 2.7 px | 0.74 | 1.00 | 25 |
| fast wave | 2 % → 2 % | 2.7 px | 0.73 | 1.00 | 73 |
| slow wave | 2 % → 2 % | 2.6 px | 0.74 | 1.00 | 73 |
| spiral | 4 % → 4 % | 2.5 px | 0.74 | 1.00 | 109 |
| loop | 2 % → 2 % | 2.6 px | 0.74 | 1.00 | 25 |
| tilted | 2 % → 2 % | 4.3 px | 0.72 | 1.00 | 18 |
| over the wet one | 2 % → 2 % | 2.4 px | 0.72 | 1.00 | 12 |
| long, no reload | 6 % → 6 % | 2.7 px | 0.73 | 1.00 | 73 | quarters: 0.05 → 0.05 → 0.05 → 0.05

Numbers say: light vs heavy: width 2.0 → 3.0 px, dark 0.74 → 0.74; the long stroke does not run out of paint.

## Impasto
Heavy acrylic · 22 px · 18.9 s

![Impasto](Impasto.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 8 % → 8 % | 24.1 px | 0.71 | 0.93 | 118 |
| heavy line | 10 % → 9 % | 28.8 px | 0.70 | 0.94 | 158 |
| pressure swell | 7 % → 7 % | 28.1 px | 0.72 | 0.94 | 54 |
| fast wave | 20 % → 13 % | 23.5 px | 0.71 | 0.64 | 163 |
| slow wave | 21 % → 14 % | 24.5 px | 0.71 | 0.66 | 303 |
| spiral | 30 % → 14 % | 20.0 px | 0.71 | 0.46 | 292 |
| loop | 18 % → 14 % | 23.9 px | 0.71 | 0.77 | 155 |
| tilted | 8 % → 8 % | 21.8 px | 0.70 | 1.00 | 82 |
| over the wet one | 17 % → 15 % | 25.4 px | 0.70 | 0.91 | 71 |
| long, no reload | 34 % → 14 % | 15.2 px | 0.71 | 0.41 | 471 | quarters: 0.38 → 0.21 → 0.10 → 0.03

Numbers say: light vs heavy: width 24.1 → 28.8 px, dark 0.71 → 0.70.

## Oil Round
Oil · 18 px · 24.3 s

![Oil Round](Oil-Round.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 2 % → 2 % | 7.2 px | 0.75 | 1.00 | 55 |
| heavy line | 7 % → 7 % | 19.3 px | 0.73 | 1.00 | 95 |
| pressure swell | 4 % → 4 % | 13.7 px | 0.72 | 1.00 | 71 |
| fast wave | 11 % → 11 % | 12.7 px | 0.65 | 1.00 | 288 |
| slow wave | 8 % → 8 % | 9.0 px | 0.57 | 1.00 | 297 |
| spiral | 10 % → 10 % | 6.6 px | 0.50 | 1.00 | 302 |
| loop | 5 % → 5 % | 7.1 px | 0.45 | 1.00 | 166 |
| tilted | 4 % → 4 % | 10.1 px | 0.52 | 1.00 | 82 |
| over the wet one | 6 % → 6 % | 7.4 px | 0.52 | 1.00 | 85 |
| long, no reload | 15 % → 15 % | 6.8 px | 0.42 | 1.00 | 458 | quarters: 0.08 → 0.08 → 0.07 → 0.06

Numbers say: light vs heavy: width 7.2 → 19.3 px, dark 0.75 → 0.73.

## Palette Knife
Oil · 20 px · 23.7 s

![Palette Knife](Palette-Knife.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 8 % → 8 % | 21.9 px | 0.67 | 1.00 | 13 |
| heavy line | 8 % → 8 % | 22.5 px | 0.73 | 1.00 | 15 |
| pressure swell | 6 % → 6 % | 22.4 px | 0.74 | 1.00 | 15 |
| fast wave | 17 % → 17 % | 19.3 px | 0.49 | 1.00 | 48 |
| slow wave | 17 % → 17 % | 19.9 px | 0.43 | 1.00 | 63 |
| spiral | 18 % → 18 % | 11.7 px | 0.45 | 1.00 | 70 |
| loop | 16 % → 16 % | 21.0 px | 0.58 | 1.00 | 40 |
| tilted | 5 % → 5 % | 15.0 px | 0.72 | 1.00 | 19 |
| over the wet one | 13 % → 13 % | 21.0 px | 0.72 | 1.00 | 11 |
| long, no reload | 17 % → 17 % | 7.5 px | 0.47 | 1.00 | 76 | quarters: 0.29 → 0.05 → 0.00 → 0.00

Numbers say: light vs heavy: width 21.9 → 22.5 px, dark 0.67 → 0.73; pressure barely changes the width.

## Water
Watercolor · 20 px · 48.0 s · over bands of wet oil paint and oil pastel in turn (it works on paint already there: look at what it does to the bands; covered counts the bands too)

![Water](Water.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 25 % → 27 % | 73.8 px | 0.80 | 1.06 | 44 |
| heavy line | 24 % → 25 % | 69.8 px | 0.81 | 1.04 | 71 |
| pressure swell | 24 % → 25 % | 89.6 px | 0.81 | 1.03 | 68 |
| fast wave | 24 % → 26 % | 27.7 px | 0.81 | 1.07 | 203 |
| slow wave | 24 % → 25 % | 27.7 px | 0.81 | 1.06 | 199 |
| spiral | 24 % → 26 % | 15.9 px | 0.81 | 1.07 | 321 |
| loop | 24 % → 25 % | 31.1 px | 0.81 | 1.03 | 143 |
| tilted | 24 % → 24 % | 67.0 px | 0.81 | 1.00 | 144 |
| over the wet one | 24 % → 25 % | 0.0 px | 0.81 | 1.06 | 99 |
| long, no reload | 24 % → 26 % | 10.7 px | 0.81 | 1.08 | 390 | quarters: 0.21 → 0.27 → 0.18 → 0.27

Numbers say: light vs heavy: width 73.8 → 69.8 px, dark 0.80 → 0.81; pressure barely changes the width; the long stroke does not run out of paint.

## Blender
Pastel · 16 px · 29.1 s · over bands of wet oil paint and oil pastel in turn (it works on paint already there: look at what it does to the bands; covered counts the bands too)

![Blender](Blender.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 24 % → 24 % | 70.7 px | 0.81 | 1.00 | 51 |
| heavy line | 25 % → 25 % | 72.1 px | 0.80 | 1.00 | 71 |
| pressure swell | 24 % → 24 % | 91.3 px | 0.81 | 1.00 | 37 |
| fast wave | 26 % → 26 % | 30.0 px | 0.79 | 1.00 | 138 |
| slow wave | 26 % → 26 % | 29.9 px | 0.80 | 1.00 | 121 |
| spiral | 28 % → 28 % | 18.7 px | 0.77 | 1.00 | 198 |
| loop | 25 % → 25 % | 32.9 px | 0.80 | 1.00 | 98 |
| tilted | 25 % → 25 % | 70.1 px | 0.79 | 1.00 | 71 |
| over the wet one | 26 % → 26 % | 1.8 px | 0.79 | 1.00 | 47 |
| long, no reload | 30 % → 30 % | 13.7 px | 0.76 | 1.00 | 312 | quarters: 0.20 → 0.28 → 0.23 → 0.30

Numbers say: light vs heavy: width 70.7 → 72.1 px, dark 0.81 → 0.80; pressure barely changes the width; the long stroke does not run out of paint.

## Eraser
Eraser · 16 px · 28.4 s · over bands of wet oil paint and oil pastel in turn (it works on paint already there: look at what it does to the bands; covered counts the bands too)

![Eraser](Eraser.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 24 % → 24 % | 69.5 px | 0.82 | 1.00 | 60 |
| heavy line | 23 % → 23 % | 67.9 px | 0.82 | 1.00 | 68 |
| pressure swell | 23 % → 23 % | 87.3 px | 0.82 | 1.00 | 41 |
| fast wave | 22 % → 22 % | 25.7 px | 0.82 | 1.00 | 109 |
| slow wave | 22 % → 22 % | 25.7 px | 0.82 | 1.00 | 185 |
| spiral | 22 % → 22 % | 14.4 px | 0.82 | 1.00 | 235 |
| loop | 22 % → 22 % | 28.6 px | 0.82 | 1.00 | 142 |
| tilted | 23 % → 23 % | 65.1 px | 0.82 | 1.00 | 67 |
| over the wet one | 23 % → 23 % | 0.0 px | 0.82 | 1.00 | 74 |
| long, no reload | 20 % → 20 % | 8.9 px | 0.82 | 1.00 | 321 | quarters: 0.15 → 0.20 → 0.15 → 0.20

Numbers say: light vs heavy: width 69.5 → 67.9 px, dark 0.82 → 0.82; pressure barely changes the width; the long stroke does not run out of paint.

## Fan
Gouache · 30 px · 35.3 s

![Fan](Fan.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 9 % → 3 % | 25.7 px | 0.63 | 0.37 | 115 |
| heavy line | 11 % → 4 % | 31.0 px | 0.63 | 0.39 | 99 |
| pressure swell | 8 % → 5 % | 31.7 px | 0.63 | 0.55 | 87 |
| fast wave | 18 % → 5 % | 20.3 px | 0.63 | 0.26 | 138 |
| slow wave | 18 % → 5 % | 21.1 px | 0.63 | 0.25 | 243 |
| spiral | 24 % → 5 % | 15.8 px | 0.63 | 0.20 | 236 |
| loop | 17 % → 5 % | 22.7 px | 0.63 | 0.29 | 186 |
| tilted | 5 % → 6 % | 15.1 px | 0.63 | 1.05 | 81 |
| over the wet one | 16 % → 8 % | 29.8 px | 0.63 | 0.50 | 131 |
| long, no reload | 23 % → 5 % | 10.1 px | 0.63 | 0.22 | 380 | quarters: 0.29 → 0.07 → 0.01 → 0.00

Numbers say: light vs heavy: width 25.7 → 31.0 px, dark 0.63 → 0.63.

## Sponge
Gouache · 30 px · 34.9 s

![Sponge](Sponge.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 4 % → 0 % | 11.4 px | 0.62 | 0.12 | 94 |
| heavy line | 12 % → 2 % | 35.4 px | 0.62 | 0.14 | 112 |
| pressure swell | 7 % → 2 % | 27.9 px | 0.62 | 0.27 | 80 |
| fast wave | 20 % → 4 % | 23.2 px | 0.62 | 0.19 | 161 |
| slow wave | 21 % → 4 % | 23.7 px | 0.62 | 0.18 | 284 |
| spiral | 28 % → 4 % | 18.3 px | 0.62 | 0.14 | 258 |
| loop | 18 % → 5 % | 23.0 px | 0.62 | 0.29 | 225 |
| tilted | 7 % → 7 % | 18.2 px | 0.62 | 1.04 | 236 |
| over the wet one | 16 % → 6 % | 27.8 px | 0.62 | 0.37 | 99 |
| long, no reload | 29 % → 5 % | 12.9 px | 0.62 | 0.17 | 427 | quarters: 0.29 → 0.13 → 0.07 → 0.04

Numbers say: light vs heavy: width 11.4 → 35.4 px, dark 0.62 → 0.62.

## Ink — sumi brush
Watercolor · 22 px · 34.4 s

![Ink — sumi brush](Ink-sumi-brush.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 8 % → 9 % | 23.9 px | 0.87 | 1.12 | 71 |
| heavy line | 13 % → 13 % | 38.1 px | 0.86 | 1.01 | 73 |
| pressure swell | 9 % → 10 % | 34.5 px | 0.87 | 1.05 | 61 |
| fast wave | 28 % → 28 % | 32.6 px | 0.81 | 1.01 | 216 |
| slow wave | 26 % → 26 % | 29.7 px | 0.83 | 1.03 | 507 |
| spiral | 38 % → 38 % | 25.3 px | 0.75 | 1.00 | 545 |
| loop | 22 % → 22 % | 28.5 px | 0.85 | 1.02 | 159 |
| tilted | 9 % → 9 % | 25.3 px | 0.86 | 1.01 | 100 |
| over the wet one | 20 % → 21 % | 30.7 px | 0.86 | 1.03 | 103 |
| long, no reload | 45 % → 43 % | 20.1 px | 0.69 | 0.97 | 720 | quarters: 0.55 → 0.41 → 0.24 → 0.15

Numbers say: light vs heavy: width 23.9 → 38.1 px, dark 0.87 → 0.86.

## Ink — wash
Watercolor · 40 px · 42.5 s

![Ink — wash](Ink-wash.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 13 % → 13 % | 37.3 px | 0.42 | 1.02 | 74 |
| heavy line | 19 % → 19 % | 55.2 px | 0.35 | 1.01 | 84 |
| pressure swell | 13 % → 13 % | 48.2 px | 0.40 | 1.02 | 63 |
| fast wave | 41 % → 42 % | 47.8 px | 0.32 | 1.02 | 223 |
| slow wave | 39 % → 40 % | 45.3 px | 0.42 | 1.02 | 455 |
| spiral | 60 % → 62 % | 39.7 px | 0.33 | 1.02 | 443 |
| loop | 34 % → 34 % | 43.8 px | 0.39 | 1.01 | 188 |
| tilted | 15 % → 15 % | 40.7 px | 0.43 | 1.01 | 124 |
| over the wet one | 30 % → 31 % | 43.4 px | 0.43 | 1.02 | 91 |
| long, no reload | 71 % → 75 % | 32.0 px | 0.31 | 1.05 | 979 | quarters: 0.40 → 0.29 → 0.19 → 0.12

Numbers say: light vs heavy: width 37.3 → 55.2 px, dark 0.42 → 0.35.

## Ink — dry brush
Ink · 30 px · 28.9 s

![Ink — dry brush](Ink-dry-brush.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 9 % → 7 % | 25.4 px | 0.81 | 0.78 | 95 |
| heavy line | 10 % → 8 % | 29.9 px | 0.79 | 0.75 | 122 |
| pressure swell | 7 % → 6 % | 28.1 px | 0.81 | 0.84 | 76 |
| fast wave | 21 % → 8 % | 24.3 px | 0.79 | 0.40 | 250 |
| slow wave | 17 % → 7 % | 20.2 px | 0.79 | 0.39 | 444 |
| spiral | 23 % → 8 % | 15.4 px | 0.78 | 0.34 | 492 |
| loop | 19 % → 8 % | 24.4 px | 0.78 | 0.44 | 201 |
| tilted | 8 % → 8 % | 22.7 px | 0.78 | 1.02 | 138 |
| over the wet one | 17 % → 14 % | 25.9 px | 0.78 | 0.81 | 94 |
| long, no reload | 20 % → 8 % | 9.0 px | 0.79 | 0.42 | 835 | quarters: 0.32 → 0.02 → 0.00 → 0.00

Numbers say: light vs heavy: width 25.4 → 29.9 px, dark 0.81 → 0.79.

## Ink — nib
Watercolor · 5 px · 29.0 s

![Ink — nib](Ink-nib.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 2 % → 5 % | 5.5 px | 0.89 | 2.46 | 43 |
| heavy line | 2 % → 5 % | 6.4 px | 0.89 | 2.33 | 51 |
| pressure swell | 2 % → 4 % | 6.2 px | 0.89 | 2.52 | 29 |
| fast wave | 5 % → 8 % | 5.9 px | 0.89 | 1.63 | 68 |
| slow wave | 5 % → 8 % | 5.7 px | 0.89 | 1.70 | 91 |
| spiral | 8 % → 11 % | 5.0 px | 0.87 | 1.41 | 127 |
| loop | 4 % → 8 % | 5.7 px | 0.89 | 1.73 | 61 |
| tilted | 4 % → 4 % | 10.3 px | 0.89 | 1.02 | 62 |
| over the wet one | 6 % → 9 % | 6.1 px | 0.89 | 1.61 | 49 |
| long, no reload | 9 % → 12 % | 4.2 px | 0.84 | 1.30 | 223 | quarters: 0.24 → 0.11 → 0.07 → 0.05

Numbers say: light vs heavy: width 5.5 → 6.4 px, dark 0.89 → 0.89; wet paint spreads well beyond the stroke.

## 0.45 · Dry brush
Gouache · 34 px · 33.4 s

![0.45 · Dry brush](0-45-Dry-brush.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 8 % → 2 % | 22.2 px | 0.68 | 0.29 | 231 |
| heavy line | 8 % → 3 % | 23.3 px | 0.68 | 0.31 | 245 |
| pressure swell | 6 % → 3 % | 24.3 px | 0.68 | 0.39 | 142 |
| fast wave | 13 % → 3 % | 15.3 px | 0.68 | 0.23 | 341 |
| slow wave | 16 % → 3 % | 18.3 px | 0.68 | 0.20 | 584 |
| spiral | 20 % → 3 % | 13.2 px | 0.68 | 0.15 | 565 |
| loop | 14 % → 4 % | 18.3 px | 0.68 | 0.26 | 282 |
| tilted | 6 % → 6 % | 17.9 px | 0.68 | 1.01 | 209 |
| over the wet one | 14 % → 6 % | 22.1 px | 0.68 | 0.41 | 178 |
| long, no reload | 21 % → 4 % | 9.3 px | 0.68 | 0.18 | 1227 | quarters: 0.28 → 0.14 → 0.07 → 0.03

Numbers say: light vs heavy: width 22.2 → 23.3 px, dark 0.68 → 0.68; pressure barely changes the width.

## Dry pastel
Pastel · 26 px · 15.1 s

![Dry pastel](Dry-pastel.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 3 % → 3 % | 8.3 px | 0.38 | 1.00 | 44 |
| heavy line | 5 % → 5 % | 13.2 px | 0.39 | 1.00 | 60 |
| pressure swell | 3 % → 3 % | 11.7 px | 0.38 | 1.00 | 28 |
| fast wave | 10 % → 10 % | 11.9 px | 0.39 | 1.00 | 122 |
| slow wave | 10 % → 10 % | 11.3 px | 0.39 | 1.00 | 234 |
| spiral | 15 % → 15 % | 9.6 px | 0.39 | 1.00 | 147 |
| loop | 7 % → 7 % | 9.4 px | 0.39 | 1.00 | 100 |
| tilted | 3 % → 3 % | 8.3 px | 0.38 | 1.00 | 46 |
| over the wet one | 7 % → 7 % | 11.1 px | 0.38 | 1.00 | 45 |
| long, no reload | 18 % → 18 % | 8.2 px | 0.39 | 1.00 | 242 | quarters: 0.08 → 0.08 → 0.08 → 0.07

Numbers say: light vs heavy: width 8.3 → 13.2 px, dark 0.38 → 0.39; the long stroke does not run out of paint.

## 0.45 · Charcoal
Charcoal · 18 px · 14.1 s

![0.45 · Charcoal](0-45-Charcoal.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 2 % → 2 % | 6.5 px | 0.80 | 1.00 | 48 |
| heavy line | 3 % → 3 % | 9.2 px | 0.80 | 1.00 | 57 |
| pressure swell | 2 % → 2 % | 8.8 px | 0.80 | 1.00 | 36 |
| fast wave | 7 % → 7 % | 8.5 px | 0.80 | 1.00 | 110 |
| slow wave | 7 % → 7 % | 8.0 px | 0.80 | 1.00 | 135 |
| spiral | 12 % → 12 % | 7.9 px | 0.80 | 1.00 | 184 |
| loop | 6 % → 6 % | 8.1 px | 0.80 | 1.00 | 95 |
| tilted | 3 % → 3 % | 7.5 px | 0.80 | 1.00 | 37 |
| over the wet one | 6 % → 6 % | 7.9 px | 0.80 | 1.00 | 21 |
| long, no reload | 17 % → 17 % | 7.8 px | 0.80 | 1.00 | 121 | quarters: 0.15 → 0.16 → 0.15 → 0.16

Numbers say: light vs heavy: width 6.5 → 9.2 px, dark 0.80 → 0.80; the long stroke does not run out of paint.

## Watercolour — wash
Watercolor · 50 px · 44.4 s

![Watercolour — wash](Watercolour-wash.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 16 % → 16 % | 45.5 px | 0.22 | 1.00 | 195 |
| heavy line | 22 % → 22 % | 64.9 px | 0.19 | 1.00 | 137 |
| pressure swell | 15 % → 15 % | 56.1 px | 0.22 | 1.01 | 84 |
| fast wave | 48 % → 49 % | 55.6 px | 0.19 | 1.01 | 401 |
| slow wave | 46 % → 46 % | 53.3 px | 0.24 | 1.00 | 520 |
| spiral | 66 % → 66 % | 43.7 px | 0.21 | 1.00 | 592 |
| loop | 40 % → 40 % | 51.4 px | 0.22 | 1.00 | 249 |
| tilted | 18 % → 18 % | 49.7 px | 0.23 | 1.00 | 209 |
| over the wet one | 36 % → 36 % | 49.6 px | 0.23 | 1.01 | 187 |
| long, no reload | 84 % → 84 % | 37.7 px | 0.20 | 1.00 | 952 | quarters: 0.24 → 0.20 → 0.16 → 0.12

Numbers say: light vs heavy: width 45.5 → 64.9 px, dark 0.22 → 0.19.

## Watercolour — wet-in-wet
Watercolor · 44 px · 45.0 s

![Watercolour — wet-in-wet](Watercolour-wet-in-wet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 13 % → 19 % | 38.4 px | 0.34 | 1.43 | 114 |
| heavy line | 19 % → 20 % | 54.6 px | 0.36 | 1.05 | 135 |
| pressure swell | 12 % → 15 % | 46.5 px | 0.37 | 1.22 | 104 |
| fast wave | 41 % → 45 % | 47.7 px | 0.35 | 1.09 | 275 |
| slow wave | 40 % → 45 % | 46.2 px | 0.42 | 1.12 | 432 |
| spiral | 63 % → 67 % | 41.5 px | 0.38 | 1.06 | 400 |
| loop | 34 % → 37 % | 44.4 px | 0.40 | 1.09 | 248 |
| tilted | 15 % → 16 % | 41.5 px | 0.38 | 1.06 | 229 |
| over the wet one | 31 % → 37 % | 43.9 px | 0.38 | 1.21 | 107 |
| long, no reload | 78 % → 84 % | 34.8 px | 0.37 | 1.08 | 1094 | quarters: 0.39 → 0.37 → 0.32 → 0.26

Numbers say: light vs heavy: width 38.4 → 54.6 px, dark 0.34 → 0.36.

## Watercolour — glaze
Watercolor · 38 px · 39.6 s

![Watercolour — glaze](Watercolour-glaze.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 13 % → 13 % | 36.6 px | 0.07 | 1.01 | 75 |
| heavy line | 19 % → 19 % | 55.4 px | 0.07 | 1.00 | 114 |
| pressure swell | 13 % → 13 % | 47.0 px | 0.07 | 1.01 | 57 |
| fast wave | 40 % → 40 % | 45.6 px | 0.07 | 1.01 | 222 |
| slow wave | 37 % → 37 % | 42.8 px | 0.07 | 1.01 | 499 |
| spiral | 59 % → 60 % | 38.8 px | 0.06 | 1.01 | 615 |
| loop | 33 % → 33 % | 42.6 px | 0.07 | 1.00 | 316 |
| tilted | 14 % → 14 % | 40.1 px | 0.07 | 1.00 | 200 |
| over the wet one | 30 % → 30 % | 42.3 px | 0.07 | 1.01 | 124 |
| long, no reload | 69 % → 70 % | 30.9 px | 0.06 | 1.01 | 676 | quarters: 0.06 → 0.05 → 0.03 → 0.02

Numbers say: light vs heavy: width 36.6 → 55.4 px, dark 0.07 → 0.07.

## Watercolour — granulating
Watercolor · 44 px · 39.2 s

![Watercolour — granulating](Watercolour-granulating.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 14 % → 14 % | 41.4 px | 0.35 | 1.00 | 80 |
| heavy line | 21 % → 21 % | 60.4 px | 0.31 | 1.00 | 103 |
| pressure swell | 14 % → 14 % | 52.2 px | 0.34 | 1.01 | 109 |
| fast wave | 45 % → 45 % | 51.7 px | 0.29 | 1.01 | 310 |
| slow wave | 42 % → 42 % | 48.2 px | 0.35 | 1.01 | 390 |
| spiral | 62 % → 63 % | 41.0 px | 0.30 | 1.01 | 400 |
| loop | 37 % → 37 % | 47.6 px | 0.33 | 1.00 | 216 |
| tilted | 16 % → 16 % | 45.5 px | 0.35 | 1.00 | 133 |
| over the wet one | 33 % → 33 % | 46.2 px | 0.35 | 1.01 | 91 |
| long, no reload | 75 % → 76 % | 33.6 px | 0.29 | 1.01 | 617 | quarters: 0.34 → 0.26 → 0.20 → 0.14

Numbers say: light vs heavy: width 41.4 → 60.4 px, dark 0.35 → 0.31.

## Watercolour — dry brush
Watercolor · 36 px · 33.3 s

![Watercolour — dry brush](Watercolour-dry-brush.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 10 % → 10 % | 28.0 px | 0.17 | 1.01 | 102 |
| heavy line | 14 % → 13 % | 40.1 px | 0.16 | 0.93 | 118 |
| pressure swell | 11 % → 11 % | 40.5 px | 0.16 | 0.98 | 84 |
| fast wave | 27 % → 20 % | 30.8 px | 0.13 | 0.74 | 283 |
| slow wave | 24 % → 17 % | 28.1 px | 0.14 | 0.71 | 661 |
| spiral | 34 % → 20 % | 22.4 px | 0.13 | 0.57 | 648 |
| loop | 21 % → 18 % | 27.2 px | 0.14 | 0.86 | 337 |
| tilted | 10 % → 10 % | 28.6 px | 0.16 | 1.00 | 156 |
| over the wet one | 22 % → 20 % | 31.4 px | 0.16 | 0.95 | 166 |
| long, no reload | 36 % → 19 % | 16.1 px | 0.14 | 0.54 | 776 | quarters: 0.09 → 0.03 → 0.01 → 0.00

Numbers say: light vs heavy: width 28.0 → 40.1 px, dark 0.17 → 0.16.

## Gouache
Gouache · 30 px · 31.7 s

![Gouache](Gouache.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 8 % → 6 % | 24.7 px | 0.28 | 0.66 | 79 |
| heavy line | 14 % → 7 % | 39.8 px | 0.28 | 0.49 | 91 |
| pressure swell | 10 % → 6 % | 38.8 px | 0.28 | 0.62 | 84 |
| fast wave | 28 % → 8 % | 32.8 px | 0.28 | 0.27 | 216 |
| slow wave | 27 % → 8 % | 31.6 px | 0.28 | 0.30 | 535 |
| spiral | 38 % → 8 % | 25.0 px | 0.28 | 0.22 | 374 |
| loop | 22 % → 8 % | 28.8 px | 0.28 | 0.36 | 226 |
| tilted | 9 % → 9 % | 24.6 px | 0.27 | 1.00 | 102 |
| over the wet one | 20 % → 13 % | 31.0 px | 0.27 | 0.67 | 105 |
| long, no reload | 40 % → 10 % | 17.9 px | 0.27 | 0.24 | 536 | quarters: 0.01 → 0.01 → 0.02 → 0.02

Numbers say: light vs heavy: width 24.7 → 39.8 px, dark 0.28 → 0.28; the long stroke does not run out of paint.

## Oil — alla prima
Oil · 30 px · 16.4 s

![Oil — alla prima](Oil-alla-prima.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 10 % → 10 % | 27.7 px | 0.51 | 1.00 | 159 |
| heavy line | 10 % → 10 % | 30.4 px | 0.51 | 1.00 | 185 |
| pressure swell | 8 % → 8 % | 29.9 px | 0.53 | 1.00 | 119 |
| fast wave | 25 % → 25 % | 29.1 px | 0.52 | 1.00 | 297 |
| slow wave | 26 % → 26 % | 29.9 px | 0.52 | 1.00 | 433 |
| spiral | 41 % → 41 % | 26.8 px | 0.51 | 1.00 | 448 |
| loop | 22 % → 22 % | 28.0 px | 0.52 | 1.00 | 207 |
| tilted | 11 % → 11 % | 31.1 px | 0.51 | 1.00 | 113 |
| over the wet one | 21 % → 21 % | 26.6 px | 0.51 | 1.00 | 95 |
| long, no reload | 50 % → 50 % | 22.3 px | 0.50 | 1.00 | 578 | quarters: 0.33 → 0.30 → 0.26 → 0.22

Numbers say: light vs heavy: width 27.7 → 30.4 px, dark 0.51 → 0.51; pressure barely changes the width.

## Oil — impasto
Oil · 34 px · 20.4 s

![Oil — impasto](Oil-impasto.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 12 % → 12 % | 33.5 px | 0.23 | 1.00 | 107 |
| heavy line | 13 % → 13 % | 36.3 px | 0.23 | 1.00 | 124 |
| pressure swell | 10 % → 10 % | 35.9 px | 0.25 | 1.00 | 87 |
| fast wave | 27 % → 27 % | 31.5 px | 0.23 | 1.00 | 272 |
| slow wave | 29 % → 29 % | 33.9 px | 0.23 | 1.00 | 470 |
| spiral | 46 % → 46 % | 30.0 px | 0.22 | 1.00 | 552 |
| loop | 25 % → 25 % | 32.2 px | 0.23 | 1.00 | 233 |
| tilted | 12 % → 12 % | 32.4 px | 0.24 | 1.00 | 152 |
| over the wet one | 23 % → 23 % | 31.5 px | 0.24 | 1.00 | 138 |
| long, no reload | 50 % → 50 % | 22.6 px | 0.22 | 1.00 | 779 | quarters: 0.18 → 0.13 → 0.10 → 0.08

Numbers say: light vs heavy: width 33.5 → 36.3 px, dark 0.23 → 0.23; pressure barely changes the width.

## Oil — glaze
Oil · 40 px · 18.2 s

![Oil — glaze](Oil-glaze.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 9 % → 9 % | 27.0 px | 0.50 | 1.00 | 99 |
| heavy line | 13 % → 13 % | 38.2 px | 0.49 | 1.00 | 129 |
| pressure swell | 10 % → 10 % | 36.6 px | 0.50 | 1.00 | 78 |
| fast wave | 29 % → 29 % | 33.5 px | 0.49 | 1.00 | 284 |
| slow wave | 30 % → 30 % | 34.5 px | 0.50 | 1.00 | 479 |
| spiral | 46 % → 46 % | 30.0 px | 0.49 | 1.00 | 525 |
| loop | 24 % → 24 % | 31.4 px | 0.50 | 1.00 | 316 |
| tilted | 11 % → 11 % | 30.3 px | 0.50 | 1.00 | 154 |
| over the wet one | 22 % → 22 % | 32.5 px | 0.50 | 1.00 | 136 |
| long, no reload | 52 % → 52 % | 23.5 px | 0.49 | 1.00 | 850 | quarters: 0.34 → 0.30 → 0.27 → 0.22

Numbers say: light vs heavy: width 27.0 → 38.2 px, dark 0.50 → 0.49.

## Oil — scumble
Oil · 36 px · 20.5 s

![Oil — scumble](Oil-scumble.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 9 % → 9 % | 26.5 px | 0.28 | 1.00 | 168 |
| heavy line | 9 % → 9 % | 26.0 px | 0.27 | 1.00 | 172 |
| pressure swell | 8 % → 8 % | 30.8 px | 0.25 | 1.00 | 100 |
| fast wave | 18 % → 18 % | 20.5 px | 0.22 | 1.00 | 347 |
| slow wave | 22 % → 22 % | 25.0 px | 0.21 | 1.00 | 612 |
| spiral | 31 % → 31 % | 20.6 px | 0.17 | 1.00 | 616 |
| loop | 18 % → 18 % | 23.1 px | 0.23 | 1.00 | 359 |
| tilted | 9 % → 9 % | 26.0 px | 0.25 | 1.00 | 217 |
| over the wet one | 19 % → 19 % | 26.4 px | 0.25 | 1.00 | 186 |
| long, no reload | 34 % → 34 % | 15.3 px | 0.15 | 1.00 | 1001 | quarters: 0.00 → 0.00 → 0.00 → 0.00

Numbers say: light vs heavy: width 26.5 → 26.0 px, dark 0.28 → 0.27; pressure barely changes the width.

## Acrylic — heavy body
Heavy acrylic · 30 px · 17.4 s

![Acrylic — heavy body](Acrylic-heavy-body.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 10 % → 9 % | 29.2 px | 0.51 | 0.92 | 152 |
| heavy line | 11 % → 10 % | 31.3 px | 0.51 | 0.93 | 126 |
| pressure swell | 8 % → 8 % | 30.8 px | 0.53 | 0.94 | 91 |
| fast wave | 23 % → 14 % | 26.7 px | 0.51 | 0.62 | 254 |
| slow wave | 24 % → 15 % | 27.8 px | 0.51 | 0.64 | 549 |
| spiral | 35 % → 15 % | 23.3 px | 0.51 | 0.42 | 662 |
| loop | 21 % → 16 % | 27.1 px | 0.51 | 0.76 | 380 |
| tilted | 9 % → 9 % | 25.5 px | 0.51 | 1.00 | 163 |
| over the wet one | 19 % → 17 % | 27.6 px | 0.51 | 0.90 | 120 |
| long, no reload | 38 % → 15 % | 17.2 px | 0.51 | 0.40 | 601 | quarters: 0.30 → 0.19 → 0.11 → 0.04

Numbers say: light vs heavy: width 29.2 → 31.3 px, dark 0.51 → 0.51; pressure barely changes the width.

## Acrylic — fluid
Watercolor · 36 px · 34.2 s

![Acrylic — fluid](Acrylic-fluid.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 12 % → 12 % | 34.8 px | 0.24 | 1.01 | 90 |
| heavy line | 18 % → 18 % | 52.6 px | 0.21 | 0.99 | 92 |
| pressure swell | 12 % → 12 % | 45.4 px | 0.23 | 1.00 | 64 |
| fast wave | 38 % → 38 % | 44.1 px | 0.19 | 0.98 | 313 |
| slow wave | 35 % → 35 % | 40.5 px | 0.22 | 1.00 | 592 |
| spiral | 55 % → 53 % | 36.0 px | 0.19 | 0.98 | 352 |
| loop | 31 % → 31 % | 40.2 px | 0.21 | 1.00 | 201 |
| tilted | 12 % → 12 % | 34.2 px | 0.24 | 1.00 | 100 |
| over the wet one | 27 % → 28 % | 42.3 px | 0.24 | 1.01 | 83 |
| long, no reload | 61 % → 58 % | 27.6 px | 0.19 | 0.95 | 470 | quarters: 0.20 → 0.14 → 0.09 → 0.06

Numbers say: light vs heavy: width 34.8 → 52.6 px, dark 0.24 → 0.21.

## Acrylic — palette knife
Heavy acrylic · 42 px · 18.8 s

![Acrylic — palette knife](Acrylic-palette-knife.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 15 % → 15 % | 44.0 px | 0.40 | 0.98 | 39 |
| heavy line | 15 % → 15 % | 44.2 px | 0.40 | 0.98 | 49 |
| pressure swell | 12 % → 11 % | 43.5 px | 0.42 | 0.99 | 21 |
| fast wave | 36 % → 20 % | 42.0 px | 0.37 | 0.55 | 100 |
| slow wave | 37 % → 21 % | 42.6 px | 0.37 | 0.57 | 196 |
| spiral | 49 % → 18 % | 32.5 px | 0.37 | 0.37 | 134 |
| loop | 32 % → 24 % | 41.2 px | 0.36 | 0.75 | 69 |
| tilted | 12 % → 12 % | 33.6 px | 0.39 | 1.00 | 39 |
| over the wet one | 26 % → 25 % | 39.7 px | 0.39 | 0.97 | 56 |
| long, no reload | 57 % → 21 % | 25.6 px | 0.35 | 0.36 | 203 | quarters: 0.00 → 0.00 → 0.00 → 0.01

Numbers say: light vs heavy: width 44.0 → 44.2 px, dark 0.40 → 0.40; pressure barely changes the width; the long stroke does not run out of paint.

## Finger on oil
Oil · 30 px · 16.7 s

![Finger on oil](Finger-on-oil.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 6 % → 6 % | 16.1 px | 0.39 | 1.00 | 74 |
| heavy line | 7 % → 7 % | 20.7 px | 0.38 | 1.00 | 63 |
| pressure swell | 6 % → 6 % | 21.5 px | 0.39 | 1.00 | 46 |
| fast wave | 11 % → 11 % | 13.2 px | 0.37 | 1.00 | 123 |
| slow wave | 17 % → 17 % | 19.2 px | 0.36 | 1.00 | 307 |
| spiral | 21 % → 21 % | 14.1 px | 0.34 | 1.00 | 225 |
| loop | 13 % → 13 % | 16.5 px | 0.37 | 1.00 | 120 |
| tilted | 7 % → 7 % | 20.7 px | 0.39 | 1.00 | 133 |
| over the wet one | 14 % → 14 % | 19.7 px | 0.39 | 1.00 | 60 |
| long, no reload | 22 % → 22 % | 9.9 px | 0.33 | 1.00 | 344 | quarters: 0.14 → 0.08 → 0.06 → 0.04

Numbers say: light vs heavy: width 16.1 → 20.7 px, dark 0.39 → 0.38.

## Palette knife — oil
Oil · 44 px · 20.6 s

![Palette knife — oil](Palette-knife-oil.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 16 % → 16 % | 45.7 px | 0.36 | 1.00 | 56 |
| heavy line | 16 % → 16 % | 46.3 px | 0.39 | 1.00 | 60 |
| pressure swell | 12 % → 12 % | 45.2 px | 0.38 | 1.00 | 20 |
| fast wave | 39 % → 39 % | 44.9 px | 0.35 | 1.01 | 78 |
| slow wave | 39 % → 39 % | 45.4 px | 0.35 | 1.00 | 149 |
| spiral | 62 % → 62 % | 40.9 px | 0.27 | 1.00 | 155 |
| loop | 34 % → 34 % | 43.8 px | 0.36 | 1.00 | 82 |
| tilted | 13 % → 13 % | 36.6 px | 0.38 | 1.00 | 30 |
| over the wet one | 28 % → 28 % | 40.8 px | 0.38 | 1.00 | 37 |
| long, no reload | 74 % → 74 % | 33.2 px | 0.25 | 1.00 | 251 | quarters: 0.00 → 0.00 → 0.00 → 0.00

Numbers say: light vs heavy: width 45.7 → 46.3 px, dark 0.36 → 0.39; pressure barely changes the width; the long stroke does not run out of paint.

## 0.45 · Sponge
Watercolor · 46 px · 40.6 s

![0.45 · Sponge](0-45-Sponge.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 27 % → 18 % | 78.2 px | 0.09 | 0.67 | 95 |
| heavy line | 32 % → 25 % | 91.7 px | 0.09 | 0.78 | 91 |
| pressure swell | 24 % → 17 % | 90.3 px | 0.11 | 0.71 | 69 |
| fast wave | 59 % → 43 % | 68.1 px | 0.10 | 0.73 | 188 |
| slow wave | 59 % → 48 % | 68.5 px | 0.13 | 0.80 | 309 |
| spiral | 75 % → 57 % | 49.3 px | 0.12 | 0.76 | 351 |
| loop | 53 % → 43 % | 68.6 px | 0.11 | 0.81 | 245 |
| tilted | 18 % → 18 % | 49.4 px | 0.15 | 1.00 | 196 |
| over the wet one | 44 % → 37 % | 74.4 px | 0.15 | 0.84 | 93 |
| long, no reload | 89 % → 71 % | 39.9 px | 0.13 | 0.79 | 626 | quarters: 0.13 → 0.12 → 0.10 → 0.07

Numbers say: light vs heavy: width 78.2 → 91.7 px, dark 0.09 → 0.09.

## 0.45 · Eraser
Eraser · 30 px · 24.6 s · over bands of wet oil paint and oil pastel in turn (it works on paint already there: look at what it does to the bands; covered counts the bands too)

![0.45 · Eraser](0-45-Eraser.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 24 % → 24 % | 69.2 px | 0.82 | 1.00 | 42 |
| heavy line | 23 % → 23 % | 67.4 px | 0.81 | 1.00 | 69 |
| pressure swell | 23 % → 23 % | 86.7 px | 0.82 | 1.00 | 55 |
| fast wave | 21 % → 21 % | 24.7 px | 0.81 | 1.00 | 225 |
| slow wave | 20 % → 20 % | 23.5 px | 0.82 | 1.00 | 288 |
| spiral | 20 % → 20 % | 13.5 px | 0.79 | 1.00 | 401 |
| loop | 21 % → 21 % | 27.8 px | 0.80 | 1.00 | 130 |
| tilted | 23 % → 23 % | 64.8 px | 0.81 | 1.00 | 90 |
| over the wet one | 22 % → 22 % | 0.0 px | 0.81 | 1.00 | 79 |
| long, no reload | 17 % → 17 % | 7.5 px | 0.79 | 1.00 | 366 | quarters: 0.13 → 0.16 → 0.13 → 0.17

Numbers say: light vs heavy: width 69.2 → 67.4 px, dark 0.82 → 0.81; pressure barely changes the width; the long stroke does not run out of paint.

## Lift wet paint
Eraser · 30 px · 26.6 s · over bands of wet oil paint and oil pastel in turn (it works on paint already there: look at what it does to the bands; covered counts the bands too)

![Lift wet paint](Lift-wet-paint.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 24 % → 24 % | 70.1 px | 0.82 | 1.00 | 45 |
| heavy line | 24 % → 24 % | 69.8 px | 0.82 | 1.00 | 52 |
| pressure swell | 24 % → 24 % | 89.5 px | 0.82 | 1.00 | 41 |
| fast wave | 24 % → 24 % | 27.7 px | 0.82 | 1.00 | 138 |
| slow wave | 24 % → 24 % | 27.7 px | 0.82 | 1.00 | 208 |
| spiral | 24 % → 24 % | 15.9 px | 0.82 | 1.00 | 227 |
| loop | 24 % → 24 % | 31.1 px | 0.82 | 1.00 | 117 |
| tilted | 24 % → 24 % | 66.8 px | 0.82 | 1.00 | 64 |
| over the wet one | 24 % → 24 % | 0.0 px | 0.82 | 1.00 | 49 |
| long, no reload | 24 % → 24 % | 10.7 px | 0.82 | 1.00 | 325 | quarters: 0.18 → 0.24 → 0.17 → 0.24

Numbers say: light vs heavy: width 70.1 → 69.8 px, dark 0.82 → 0.82; pressure barely changes the width; the long stroke does not run out of paint.

## Sgraffito
Eraser · 10 px · 25.1 s · over bands of wet oil paint and oil pastel in turn (it works on paint already there: look at what it does to the bands; covered counts the bands too)

![Sgraffito](Sgraffito.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 24 % → 24 % | 69.5 px | 0.81 | 1.00 | 8 |
| heavy line | 24 % → 24 % | 69.5 px | 0.82 | 1.00 | 7 |
| pressure swell | 24 % → 24 % | 89.5 px | 0.82 | 1.00 | 5 |
| fast wave | 24 % → 24 % | 27.4 px | 0.82 | 1.00 | 24 |
| slow wave | 24 % → 24 % | 27.4 px | 0.81 | 1.00 | 29 |
| spiral | 24 % → 24 % | 15.7 px | 0.81 | 1.00 | 65 |
| loop | 24 % → 24 % | 30.9 px | 0.82 | 1.00 | 30 |
| tilted | 24 % → 24 % | 66.6 px | 0.82 | 1.00 | 11 |
| over the wet one | 24 % → 24 % | 0.0 px | 0.82 | 1.00 | 8 |
| long, no reload | 24 % → 24 % | 10.6 px | 0.82 | 1.00 | 65 | quarters: 0.17 → 0.24 → 0.17 → 0.24

Numbers say: light vs heavy: width 69.5 → 69.5 px, dark 0.81 → 0.82; pressure barely changes the width; the long stroke does not run out of paint.

## Brush Artist · Refs · #01 Henry Ward peach cloud
Gouache · 44 px · 46.5 s

![Brush Artist · Refs · #01 Henry Ward peach cloud](Brush-Artist-Refs-01-Henry-Ward-peach-cloud.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 13 % → 9 % | 37.9 px | 0.33 | 0.68 | 175 |
| heavy line | 14 % → 10 % | 41.1 px | 0.33 | 0.74 | 197 |
| pressure swell | 11 % → 9 % | 41.0 px | 0.33 | 0.80 | 156 |
| fast wave | 25 % → 13 % | 29.2 px | 0.33 | 0.51 | 672 |
| slow wave | 30 % → 15 % | 34.6 px | 0.33 | 0.50 | 1045 |
| spiral | 41 % → 16 % | 27.0 px | 0.33 | 0.39 | 846 |
| loop | 25 % → 16 % | 33.0 px | 0.33 | 0.61 | 447 |
| tilted | 11 % → 11 % | 31.3 px | 0.33 | 1.00 | 244 |
| over the wet one | 24 % → 20 % | 36.1 px | 0.33 | 0.85 | 267 |
| long, no reload | 44 % → 18 % | 19.8 px | 0.33 | 0.41 | 1171 | quarters: 0.01 → 0.02 → 0.02 → 0.02

Numbers say: light vs heavy: width 37.9 → 41.1 px, dark 0.33 → 0.33; pressure barely changes the width; the long stroke does not run out of paint.

## Brush Artist · Refs · #02 Henry Ward cream strokes
Gouache · 46 px · 45.4 s

![Brush Artist · Refs · #02 Henry Ward cream strokes](Brush-Artist-Refs-02-Henry-Ward-cream-strokes.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 13 % → 10 % | 37.9 px | 0.41 | 0.73 | 247 |
| heavy line | 14 % → 12 % | 40.9 px | 0.41 | 0.82 | 196 |
| pressure swell | 11 % → 10 % | 41.1 px | 0.42 | 0.88 | 127 |
| fast wave | 25 % → 13 % | 28.7 px | 0.41 | 0.51 | 476 |
| slow wave | 29 % → 15 % | 34.0 px | 0.41 | 0.51 | 858 |
| spiral | 40 % → 16 % | 26.6 px | 0.41 | 0.40 | 801 |
| loop | 25 % → 16 % | 32.6 px | 0.41 | 0.64 | 424 |
| tilted | 11 % → 11 % | 30.7 px | 0.41 | 1.00 | 318 |
| over the wet one | 24 % → 21 % | 36.1 px | 0.41 | 0.86 | 297 |
| long, no reload | 44 % → 19 % | 19.6 px | 0.41 | 0.43 | 1239 | quarters: 0.01 → 0.02 → 0.03 → 0.03

Numbers say: light vs heavy: width 37.9 → 40.9 px, dark 0.41 → 0.41; pressure barely changes the width; the long stroke does not run out of paint.

## Brush Artist · Refs · #03 Henry Ward navy contours
Heavy acrylic · 22 px · 18.6 s

![Brush Artist · Refs · #03 Henry Ward navy contours](Brush-Artist-Refs-03-Henry-Ward-navy-contours.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 7 % → 7 % | 21.6 px | 0.70 | 0.94 | 99 |
| heavy line | 8 % → 8 % | 23.5 px | 0.70 | 0.95 | 104 |
| pressure swell | 6 % → 6 % | 23.2 px | 0.73 | 0.94 | 73 |
| fast wave | 19 % → 12 % | 21.9 px | 0.72 | 0.65 | 251 |
| slow wave | 19 % → 13 % | 22.5 px | 0.72 | 0.68 | 367 |
| spiral | 30 % → 13 % | 19.5 px | 0.72 | 0.45 | 491 |
| loop | 17 % → 13 % | 21.5 px | 0.72 | 0.81 | 219 |
| tilted | 8 % → 8 % | 22.7 px | 0.71 | 1.00 | 136 |
| over the wet one | 16 % → 14 % | 21.3 px | 0.71 | 0.89 | 122 |
| long, no reload | 34 % → 13 % | 15.1 px | 0.72 | 0.40 | 612 | quarters: 0.35 → 0.29 → 0.19 → 0.07

Numbers say: light vs heavy: width 21.6 → 23.5 px, dark 0.70 → 0.70; pressure barely changes the width.

## Brush Artist · Refs · #04 Henry Ward grey cloud
Gouache · 50 px · 48.9 s

![Brush Artist · Refs · #04 Henry Ward grey cloud](Brush-Artist-Refs-04-Henry-Ward-grey-cloud.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 15 % → 11 % | 43.6 px | 0.32 | 0.73 | 344 |
| heavy line | 16 % → 13 % | 46.9 px | 0.32 | 0.79 | 538 |
| pressure swell | 12 % → 10 % | 46.8 px | 0.32 | 0.84 | 149 |
| fast wave | 29 % → 15 % | 32.9 px | 0.32 | 0.52 | 539 |
| slow wave | 34 % → 17 % | 39.2 px | 0.32 | 0.51 | 878 |
| spiral | 44 % → 18 % | 28.7 px | 0.32 | 0.42 | 935 |
| loop | 29 % → 18 % | 37.7 px | 0.32 | 0.62 | 474 |
| tilted | 12 % → 12 % | 34.2 px | 0.32 | 1.00 | 318 |
| over the wet one | 27 % → 23 % | 41.1 px | 0.32 | 0.86 | 344 |
| long, no reload | 49 % → 21 % | 21.8 px | 0.32 | 0.44 | 1260 | quarters: 0.01 → 0.02 → 0.02 → 0.03

Numbers say: light vs heavy: width 43.6 → 46.9 px, dark 0.32 → 0.32; pressure barely changes the width; the long stroke does not run out of paint.

## Brush Artist · Refs · #05 Henry Ward green in rust loops
Heavy acrylic · 20 px · 17.5 s

![Brush Artist · Refs · #05 Henry Ward green in rust loops](Brush-Artist-Refs-05-Henry-Ward-green-in-rust-loops.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 7 % → 6 % | 19.5 px | 0.55 | 0.94 | 94 |
| heavy line | 7 % → 7 % | 21.4 px | 0.55 | 0.94 | 96 |
| pressure swell | 6 % → 5 % | 21.6 px | 0.57 | 0.92 | 69 |
| fast wave | 17 % → 11 % | 19.8 px | 0.56 | 0.64 | 246 |
| slow wave | 18 % → 12 % | 20.4 px | 0.55 | 0.65 | 347 |
| spiral | 27 % → 11 % | 17.9 px | 0.55 | 0.42 | 426 |
| loop | 15 % → 12 % | 19.5 px | 0.55 | 0.79 | 221 |
| tilted | 8 % → 8 % | 21.7 px | 0.55 | 1.00 | 153 |
| over the wet one | 15 % → 13 % | 19.3 px | 0.55 | 0.87 | 116 |
| long, no reload | 30 % → 12 % | 13.3 px | 0.56 | 0.39 | 646 | quarters: 0.25 → 0.18 → 0.10 → 0.02

Numbers say: light vs heavy: width 19.5 → 21.4 px, dark 0.55 → 0.55; pressure barely changes the width.

## Brush Artist · Refs · #06 Henry Ward scrubbed grey
Gouache · 50 px · 49.0 s

![Brush Artist · Refs · #06 Henry Ward scrubbed grey](Brush-Artist-Refs-06-Henry-Ward-scrubbed-grey.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 15 % → 11 % | 43.6 px | 0.34 | 0.73 | 192 |
| heavy line | 16 % → 13 % | 46.9 px | 0.34 | 0.79 | 228 |
| pressure swell | 12 % → 10 % | 46.8 px | 0.34 | 0.84 | 175 |
| fast wave | 29 % → 15 % | 32.9 px | 0.34 | 0.52 | 579 |
| slow wave | 34 % → 17 % | 39.2 px | 0.34 | 0.51 | 1141 |
| spiral | 44 % → 18 % | 28.7 px | 0.34 | 0.42 | 925 |
| loop | 29 % → 18 % | 37.7 px | 0.34 | 0.62 | 543 |
| tilted | 12 % → 12 % | 34.2 px | 0.34 | 1.00 | 307 |
| over the wet one | 27 % → 23 % | 41.1 px | 0.34 | 0.86 | 274 |
| long, no reload | 49 % → 21 % | 21.8 px | 0.34 | 0.44 | 1436 | quarters: 0.01 → 0.02 → 0.02 → 0.03

Numbers say: light vs heavy: width 43.6 → 46.9 px, dark 0.34 → 0.34; pressure barely changes the width; the long stroke does not run out of paint.

## Brush Artist · Refs · #07 Henry Ward blue L + black zigzag
Heavy acrylic · 34 px · 21.9 s

![Brush Artist · Refs · #07 Henry Ward blue L + black zigzag](Brush-Artist-Refs-07-Henry-Ward-blue-L-black-zigzag.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 11 % → 11 % | 33.2 px | 0.58 | 0.93 | 166 |
| heavy line | 12 % → 12 % | 35.9 px | 0.58 | 0.93 | 134 |
| pressure swell | 9 % → 9 % | 35.3 px | 0.59 | 0.94 | 90 |
| fast wave | 29 % → 20 % | 33.7 px | 0.58 | 0.68 | 349 |
| slow wave | 30 % → 21 % | 34.2 px | 0.58 | 0.72 | 626 |
| spiral | 47 % → 22 % | 31.3 px | 0.58 | 0.46 | 666 |
| loop | 25 % → 21 % | 32.7 px | 0.58 | 0.82 | 456 |
| tilted | 11 % → 11 % | 30.0 px | 0.58 | 1.00 | 239 |
| over the wet one | 22 % → 20 % | 31.8 px | 0.58 | 0.91 | 193 |
| long, no reload | 53 % → 22 % | 23.8 px | 0.59 | 0.42 | 952 | quarters: 0.40 → 0.32 → 0.21 → 0.10

Numbers say: light vs heavy: width 33.2 → 35.9 px, dark 0.58 → 0.58; pressure barely changes the width.

## Brush Artist · Refs · #08 Henry Ward olive bands
Gouache · 34 px · 32.7 s

![Brush Artist · Refs · #08 Henry Ward olive bands](Brush-Artist-Refs-08-Henry-Ward-olive-bands.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 4 % → 0 % | 12.2 px | 0.61 | 0.04 | 71 |
| heavy line | 7 % → 0 % | 19.3 px | 0.61 | 0.02 | 219 |
| pressure swell | 5 % → 0 % | 18.7 px | 0.61 | 0.03 | 108 |
| fast wave | 10 % → 0 % | 11.1 px | 0.61 | 0.02 | 330 |
| slow wave | 15 % → 1 % | 17.0 px | 0.61 | 0.06 | 801 |
| spiral | 19 % → 1 % | 12.7 px | 0.61 | 0.03 | 570 |
| loop | 12 % → 1 % | 15.3 px | 0.61 | 0.09 | 289 |
| tilted | 5 % → 5 % | 15.1 px | 0.61 | 0.96 | 168 |
| over the wet one | 11 % → 2 % | 16.9 px | 0.61 | 0.22 | 146 |
| long, no reload | 22 % → 2 % | 9.8 px | 0.61 | 0.09 | 925 | quarters: 0.21 → 0.15 → 0.11 → 0.09

Numbers say: light vs heavy: width 12.2 → 19.3 px, dark 0.61 → 0.61.

## Brush Artist · Refs · #09 Henry Ward white loops
Gouache · 46 px · 49.1 s

![Brush Artist · Refs · #09 Henry Ward white loops](Brush-Artist-Refs-09-Henry-Ward-white-loops.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 13 % → 10 % | 37.9 px | 0.44 | 0.73 | 202 |
| heavy line | 14 % → 12 % | 40.9 px | 0.44 | 0.82 | 239 |
| pressure swell | 11 % → 10 % | 41.1 px | 0.44 | 0.88 | 157 |
| fast wave | 25 % → 13 % | 28.7 px | 0.43 | 0.51 | 580 |
| slow wave | 29 % → 15 % | 34.0 px | 0.43 | 0.51 | 995 |
| spiral | 40 % → 16 % | 26.6 px | 0.43 | 0.40 | 1285 |
| loop | 25 % → 16 % | 32.6 px | 0.43 | 0.64 | 516 |
| tilted | 11 % → 11 % | 30.7 px | 0.44 | 1.00 | 449 |
| over the wet one | 24 % → 21 % | 36.1 px | 0.44 | 0.86 | 383 |
| long, no reload | 44 % → 19 % | 19.6 px | 0.43 | 0.43 | 1510 | quarters: 0.01 → 0.02 → 0.03 → 0.03

Numbers say: light vs heavy: width 37.9 → 40.9 px, dark 0.44 → 0.44; pressure barely changes the width; the long stroke does not run out of paint.

## Brush Artist · Refs · #10 Henry Ward maroon loops
Heavy acrylic · 30 px · 21.9 s

![Brush Artist · Refs · #10 Henry Ward maroon loops](Brush-Artist-Refs-10-Henry-Ward-maroon-loops.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 10 % → 9 % | 28.0 px | 0.71 | 0.94 | 287 |
| heavy line | 10 % → 10 % | 30.3 px | 0.71 | 0.95 | 240 |
| pressure swell | 8 % → 8 % | 30.0 px | 0.73 | 0.94 | 141 |
| fast wave | 25 % → 17 % | 28.4 px | 0.73 | 0.70 | 341 |
| slow wave | 25 % → 18 % | 29.0 px | 0.72 | 0.73 | 544 |
| spiral | 39 % → 18 % | 26.0 px | 0.72 | 0.47 | 496 |
| loop | 21 % → 18 % | 27.6 px | 0.72 | 0.85 | 261 |
| tilted | 10 % → 10 % | 28.0 px | 0.72 | 1.00 | 147 |
| over the wet one | 20 % → 18 % | 27.0 px | 0.72 | 0.91 | 188 |
| long, no reload | 46 % → 18 % | 20.5 px | 0.73 | 0.40 | 997 | quarters: 0.44 → 0.38 → 0.31 → 0.22

Numbers say: light vs heavy: width 28.0 → 30.3 px, dark 0.71 → 0.71; pressure barely changes the width.

## Brush Artist · Refs · #11 Henry Ward purple spun balls
Heavy acrylic · 36 px · 22.6 s

![Brush Artist · Refs · #11 Henry Ward purple spun balls](Brush-Artist-Refs-11-Henry-Ward-purple-spun-balls.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 12 % → 11 % | 34.2 px | 0.71 | 0.96 | 143 |
| heavy line | 13 % → 12 % | 36.7 px | 0.71 | 0.95 | 125 |
| pressure swell | 10 % → 9 % | 36.2 px | 0.74 | 0.95 | 128 |
| fast wave | 30 % → 22 % | 34.6 px | 0.73 | 0.75 | 399 |
| slow wave | 30 % → 24 % | 35.1 px | 0.73 | 0.79 | 630 |
| spiral | 49 % → 24 % | 32.3 px | 0.73 | 0.50 | 587 |
| loop | 26 % → 23 % | 33.4 px | 0.73 | 0.88 | 338 |
| tilted | 11 % → 11 % | 31.2 px | 0.73 | 1.00 | 160 |
| over the wet one | 23 % → 21 % | 32.3 px | 0.73 | 0.93 | 133 |
| long, no reload | 55 % → 24 % | 24.8 px | 0.73 | 0.44 | 947 | quarters: 0.51 → 0.46 → 0.39 → 0.28

Numbers say: light vs heavy: width 34.2 → 36.7 px, dark 0.71 → 0.71; pressure barely changes the width.

## Brush Artist · Refs · #12 Henry Ward black-olive cage
Gouache · 28 px · 28.2 s

![Brush Artist · Refs · #12 Henry Ward black-olive cage](Brush-Artist-Refs-12-Henry-Ward-black-olive-cage.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 3 % → 0 % | 10.1 px | 0.65 | 0.08 | 63 |
| heavy line | 5 % → 0 % | 15.3 px | 0.65 | 0.08 | 146 |
| pressure swell | 4 % → 0 % | 14.9 px | 0.65 | 0.10 | 85 |
| fast wave | 8 % → 0 % | 8.9 px | 0.65 | 0.04 | 213 |
| slow wave | 12 % → 1 % | 13.6 px | 0.65 | 0.09 | 492 |
| spiral | 16 % → 1 % | 10.4 px | 0.65 | 0.04 | 499 |
| loop | 9 % → 2 % | 12.3 px | 0.65 | 0.17 | 205 |
| tilted | 5 % → 4 % | 13.0 px | 0.65 | 0.95 | 143 |
| over the wet one | 9 % → 3 % | 13.2 px | 0.65 | 0.27 | 154 |
| long, no reload | 18 % → 2 % | 8.3 px | 0.65 | 0.12 | 1126 | quarters: 0.19 → 0.14 → 0.11 → 0.10

Numbers say: light vs heavy: width 10.1 → 15.3 px, dark 0.65 → 0.65.

## Brush Artist · Refs · #13 Henry Ward blue streaky form
Gouache · 50 px · 54.5 s

![Brush Artist · Refs · #13 Henry Ward blue streaky form](Brush-Artist-Refs-13-Henry-Ward-blue-streaky-form.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 15 % → 11 % | 43.6 px | 0.34 | 0.73 | 305 |
| heavy line | 16 % → 13 % | 46.9 px | 0.34 | 0.79 | 469 |
| pressure swell | 12 % → 10 % | 46.8 px | 0.34 | 0.84 | 189 |
| fast wave | 29 % → 15 % | 32.9 px | 0.34 | 0.52 | 488 |
| slow wave | 34 % → 17 % | 39.2 px | 0.34 | 0.51 | 787 |
| spiral | 44 % → 18 % | 28.7 px | 0.34 | 0.42 | 830 |
| loop | 29 % → 18 % | 37.7 px | 0.34 | 0.62 | 402 |
| tilted | 12 % → 12 % | 34.2 px | 0.34 | 1.00 | 218 |
| over the wet one | 27 % → 23 % | 41.1 px | 0.34 | 0.86 | 330 |
| long, no reload | 49 % → 21 % | 21.8 px | 0.33 | 0.44 | 1524 | quarters: 0.01 → 0.02 → 0.02 → 0.03

Numbers say: light vs heavy: width 43.6 → 46.9 px, dark 0.34 → 0.34; pressure barely changes the width; the long stroke does not run out of paint.

## Brush Artist · Refs · #14 Henry Ward olive totem
Heavy acrylic · 48 px · 24.7 s

![Brush Artist · Refs · #14 Henry Ward olive totem](Brush-Artist-Refs-14-Henry-Ward-olive-totem.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 15 % → 15 % | 44.9 px | 0.31 | 0.95 | 278 |
| heavy line | 16 % → 16 % | 47.7 px | 0.31 | 0.95 | 276 |
| pressure swell | 13 % → 12 % | 47.1 px | 0.32 | 0.95 | 218 |
| fast wave | 38 % → 30 % | 44.0 px | 0.30 | 0.78 | 469 |
| slow wave | 39 % → 31 % | 44.6 px | 0.30 | 0.81 | 682 |
| spiral | 58 % → 32 % | 38.2 px | 0.30 | 0.55 | 683 |
| loop | 33 % → 29 % | 42.7 px | 0.30 | 0.89 | 414 |
| tilted | 13 % → 13 % | 37.6 px | 0.31 | 1.00 | 207 |
| over the wet one | 28 % → 26 % | 41.2 px | 0.31 | 0.93 | 185 |
| long, no reload | 68 % → 33 % | 30.3 px | 0.30 | 0.49 | 1017 | quarters: 0.25 → 0.18 → 0.09 → 0.03

Numbers say: light vs heavy: width 44.9 → 47.7 px, dark 0.31 → 0.31; pressure barely changes the width.

## Brush Artist · Refs · #15 Ultramarine brush script
Ink · 4 px · 33.3 s

![Brush Artist · Refs · #15 Ultramarine brush script](Brush-Artist-Refs-15-Ultramarine-brush-script.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 1 % → 3 % | 2.2 px | 0.55 | 3.90 | 38 |
| heavy line | 6 % → 6 % | 16.7 px | 0.58 | 0.99 | 70 |
| pressure swell | 3 % → 4 % | 12.1 px | 0.64 | 1.15 | 34 |
| fast wave | 9 % → 7 % | 10.6 px | 0.54 | 0.81 | 129 |
| slow wave | 7 % → 7 % | 8.4 px | 0.54 | 0.93 | 141 |
| spiral | 11 % → 7 % | 7.2 px | 0.52 | 0.66 | 249 |
| loop | 7 % → 7 % | 9.2 px | 0.53 | 0.98 | 141 |
| tilted | 3 % → 3 % | 8.2 px | 0.62 | 1.02 | 53 |
| over the wet one | 7 % → 7 % | 11.5 px | 0.62 | 1.05 | 46 |
| long, no reload | 16 % → 8 % | 7.3 px | 0.50 | 0.48 | 493 | quarters: 0.15 → 0.04 → 0.01 → 0.00

Numbers say: light vs heavy: width 2.2 → 16.7 px, dark 0.55 → 0.58; wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #18 Blue oil-stick scribbles
Pastel · 10 px · 17.3 s

![Brush Artist · Refs · #18 Blue oil-stick scribbles](Brush-Artist-Refs-18-Blue-oil-stick-scribbles.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 1 % → 1 % | 2.9 px | 0.52 | 1.00 | 41 |
| heavy line | 2 % → 2 % | 5.5 px | 0.53 | 1.00 | 40 |
| pressure swell | 1 % → 1 % | 5.0 px | 0.53 | 1.00 | 43 |
| fast wave | 4 % → 4 % | 4.8 px | 0.53 | 1.00 | 98 |
| slow wave | 4 % → 4 % | 4.4 px | 0.53 | 1.00 | 77 |
| spiral | 7 % → 7 % | 4.5 px | 0.52 | 1.00 | 166 |
| loop | 3 % → 3 % | 4.5 px | 0.52 | 1.00 | 85 |
| tilted | 2 % → 2 % | 4.7 px | 0.53 | 1.00 | 52 |
| over the wet one | 3 % → 3 % | 4.7 px | 0.53 | 1.00 | 40 |
| long, no reload | 10 % → 10 % | 4.4 px | 0.53 | 1.00 | 280 | quarters: 0.06 → 0.06 → 0.06 → 0.06

Numbers say: light vs heavy: width 2.9 → 5.5 px, dark 0.52 → 0.53; the long stroke does not run out of paint.

## Brush Artist · Refs · #20 Orange-red crayon scribble
Pastel · 14 px · 16.8 s

![Brush Artist · Refs · #20 Orange-red crayon scribble](Brush-Artist-Refs-20-Orange-red-crayon-scribble.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 1 % → 1 % | 4.0 px | 0.53 | 1.00 | 40 |
| heavy line | 3 % → 3 % | 8.0 px | 0.53 | 1.00 | 46 |
| pressure swell | 2 % → 2 % | 7.6 px | 0.53 | 1.00 | 22 |
| fast wave | 6 % → 6 % | 7.2 px | 0.53 | 1.00 | 135 |
| slow wave | 6 % → 6 % | 6.6 px | 0.53 | 1.00 | 184 |
| spiral | 9 % → 9 % | 6.2 px | 0.53 | 1.00 | 166 |
| loop | 5 % → 5 % | 6.2 px | 0.53 | 1.00 | 129 |
| tilted | 2 % → 2 % | 5.6 px | 0.53 | 1.00 | 52 |
| over the wet one | 4 % → 4 % | 6.6 px | 0.53 | 1.00 | 45 |
| long, no reload | 13 % → 13 % | 5.7 px | 0.53 | 1.00 | 283 | quarters: 0.07 → 0.07 → 0.08 → 0.08

Numbers say: light vs heavy: width 4.0 → 8.0 px, dark 0.53 → 0.53; the long stroke does not run out of paint.

## Brush Artist · Refs · #21 Gritty black contours
Gouache · 12 px · 31.5 s

![Brush Artist · Refs · #21 Gritty black contours](Brush-Artist-Refs-21-Gritty-black-contours.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 1 % → 0 % | 3.3 px | 0.81 | 0.08 | 105 |
| heavy line | 2 % → 0 % | 5.2 px | 0.81 | 0.03 | 200 |
| pressure swell | 1 % → 0 % | 5.4 px | 0.81 | 0.04 | 174 |
| fast wave | 2 % → 0 % | 2.7 px | 0.81 | 0.01 | 336 |
| slow wave | 4 % → 0 % | 4.4 px | 0.81 | 0.04 | 342 |
| spiral | 5 % → 0 % | 3.1 px | 0.81 | 0.02 | 549 |
| loop | 3 % → 0 % | 4.1 px | 0.81 | 0.02 | 286 |
| tilted | 2 % → 2 % | 4.8 px | 0.81 | 0.93 | 164 |
| over the wet one | 3 % → 0 % | 4.7 px | 0.81 | 0.11 | 120 |
| long, no reload | 6 % → 0 % | 2.7 px | 0.81 | 0.06 | 764 | quarters: 0.09 → 0.06 → 0.05 → 0.04

Numbers say: light vs heavy: width 3.3 → 5.2 px, dark 0.81 → 0.81.

## Brush Artist · Refs · #22 Bold black brush poster
Ink · 20 px · 40.2 s

![Brush Artist · Refs · #22 Bold black brush poster](Brush-Artist-Refs-22-Bold-black-brush-poster.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 3 % → 5 % | 9.6 px | 0.79 | 1.64 | 74 |
| heavy line | 15 % → 15 % | 44.6 px | 0.88 | 0.99 | 136 |
| pressure swell | 9 % → 9 % | 31.9 px | 0.87 | 1.04 | 74 |
| fast wave | 27 % → 27 % | 31.7 px | 0.87 | 0.98 | 260 |
| slow wave | 22 % → 22 % | 25.4 px | 0.87 | 0.98 | 340 |
| spiral | 34 % → 32 % | 22.4 px | 0.87 | 0.94 | 428 |
| loop | 20 % → 20 % | 26.4 px | 0.88 | 1.00 | 207 |
| tilted | 8 % → 8 % | 23.1 px | 0.88 | 1.01 | 97 |
| over the wet one | 19 % → 19 % | 30.4 px | 0.88 | 1.00 | 91 |
| long, no reload | 45 % → 38 % | 20.3 px | 0.86 | 0.83 | 764 | quarters: 0.54 → 0.45 → 0.35 → 0.26

Numbers say: light vs heavy: width 9.6 → 44.6 px, dark 0.79 → 0.88; wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #23 Dry white on orange + black line
Gouache · 50 px · 35.7 s

![Brush Artist · Refs · #23 Dry white on orange + black line](Brush-Artist-Refs-23-Dry-white-on-orange-black-line.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 5 % → 0 % | 15.7 px | 0.42 | 0.02 | 156 |
| heavy line | 9 % → 0 % | 25.3 px | 0.42 | 0.00 | 305 |
| pressure swell | 6 % → 0 % | 23.8 px | 0.41 | 0.00 | 164 |
| fast wave | 12 % → 0 % | 13.7 px | 0.41 | 0.01 | 596 |
| slow wave | 19 % → 0 % | 21.6 px | 0.41 | 0.02 | 1538 |
| spiral | 24 % → 0 % | 15.6 px | 0.40 | 0.01 | 996 |
| loop | 15 % → 1 % | 19.8 px | 0.40 | 0.04 | 477 |
| tilted | 6 % → 6 % | 17.5 px | 0.40 | 0.94 | 219 |
| over the wet one | 14 % → 1 % | 20.6 px | 0.40 | 0.09 | 209 |
| long, no reload | 27 % → 1 % | 12.3 px | 0.40 | 0.05 | 1554 | quarters: 0.02 → 0.03 → 0.03 → 0.03

Numbers say: light vs heavy: width 15.7 → 25.3 px, dark 0.42 → 0.42; the long stroke does not run out of paint.

## Brush Artist · Refs · #24 Picasso flat oil
Oil · 34 px · 20.3 s

![Brush Artist · Refs · #24 Picasso flat oil](Brush-Artist-Refs-24-Picasso-flat-oil.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 11 % → 11 % | 32.4 px | 0.40 | 1.00 | 142 |
| heavy line | 12 % → 12 % | 35.2 px | 0.40 | 1.00 | 233 |
| pressure swell | 9 % → 9 % | 34.5 px | 0.41 | 1.00 | 105 |
| fast wave | 30 % → 30 % | 34.2 px | 0.41 | 1.00 | 377 |
| slow wave | 30 % → 30 % | 35.0 px | 0.41 | 1.00 | 800 |
| spiral | 51 % → 51 % | 33.8 px | 0.40 | 1.00 | 941 |
| loop | 25 % → 25 % | 32.7 px | 0.41 | 1.00 | 425 |
| tilted | 11 % → 11 % | 32.1 px | 0.40 | 1.00 | 226 |
| over the wet one | 23 % → 23 % | 30.8 px | 0.40 | 1.00 | 244 |
| long, no reload | 62 % → 62 % | 27.6 px | 0.39 | 1.00 | 1152 | quarters: 0.28 → 0.28 → 0.26 → 0.24

Numbers say: light vs heavy: width 32.4 → 35.2 px, dark 0.40 → 0.40; pressure barely changes the width.

## Brush Artist · Refs · #25 Yellow heavy flat stroke
Heavy acrylic · 110 px · 46.1 s

![Brush Artist · Refs · #25 Yellow heavy flat stroke](Brush-Artist-Refs-25-Yellow-heavy-flat-stroke.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 35 % → 36 % | 101.5 px | 0.30 | 1.02 | 597 |
| heavy line | 36 % → 35 % | 105.1 px | 0.31 | 0.97 | 615 |
| pressure swell | 28 % → 29 % | 105.4 px | 0.30 | 1.04 | 480 |
| fast wave | 73 % → 76 % | 83.8 px | 0.31 | 1.05 | 1114 |
| slow wave | 73 % → 72 % | 84.7 px | 0.30 | 0.98 | 2043 |
| spiral | 86 % → 83 % | 56.7 px | 0.29 | 0.97 | 2295 |
| loop | 65 % → 64 % | 83.6 px | 0.31 | 0.99 | 1274 |
| tilted | 26 % → 26 % | 71.5 px | 0.30 | 1.00 | 868 |
| over the wet one | 55 % → 54 % | 83.2 px | 0.30 | 0.97 | 776 |
| long, no reload | 98 % → 97 % | 44.1 px | 0.30 | 0.99 | 3266 | quarters: 0.00 → 0.00 → 0.00 → 0.00

Numbers say: light vs heavy: width 101.5 → 105.1 px, dark 0.30 → 0.31; pressure barely changes the width; the long stroke does not run out of paint.

## Brush Artist · Refs · #27 Orange impasto swatch
Heavy acrylic · 60 px · 32.2 s

![Brush Artist · Refs · #27 Orange impasto swatch](Brush-Artist-Refs-27-Orange-impasto-swatch.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 20 % → 19 % | 56.8 px | 0.34 | 0.97 | 359 |
| heavy line | 20 % → 20 % | 59.5 px | 0.34 | 0.97 | 226 |
| pressure swell | 16 % → 15 % | 59.6 px | 0.36 | 0.97 | 151 |
| fast wave | 48 % → 47 % | 55.1 px | 0.35 | 0.98 | 466 |
| slow wave | 48 % → 47 % | 55.9 px | 0.35 | 0.98 | 951 |
| spiral | 69 % → 62 % | 45.5 px | 0.34 | 0.91 | 1077 |
| loop | 42 % → 40 % | 53.9 px | 0.35 | 0.97 | 554 |
| tilted | 16 % → 16 % | 44.0 px | 0.35 | 1.00 | 394 |
| over the wet one | 34 % → 33 % | 50.9 px | 0.35 | 0.96 | 326 |
| long, no reload | 85 % → 75 % | 38.1 px | 0.35 | 0.88 | 2122 | quarters: 0.33 → 0.31 → 0.30 → 0.26

Numbers say: light vs heavy: width 56.8 → 59.5 px, dark 0.34 → 0.34; pressure barely changes the width.

## Brush Artist · Refs · #28 Miles Davis black lines
Ink · 22 px · 35.2 s

![Brush Artist · Refs · #28 Miles Davis black lines](Brush-Artist-Refs-28-Miles-Davis-black-lines.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 4 % → 6 % | 12.3 px | 0.81 | 1.49 | 60 |
| heavy line | 17 % → 17 % | 49.0 px | 0.88 | 0.99 | 95 |
| pressure swell | 10 % → 10 % | 35.9 px | 0.87 | 1.03 | 67 |
| fast wave | 31 % → 30 % | 35.5 px | 0.87 | 0.98 | 230 |
| slow wave | 25 % → 25 % | 28.7 px | 0.87 | 0.99 | 360 |
| spiral | 39 % → 37 % | 25.5 px | 0.87 | 0.95 | 446 |
| loop | 23 % → 23 % | 29.6 px | 0.88 | 1.00 | 282 |
| tilted | 9 % → 9 % | 25.3 px | 0.88 | 1.01 | 91 |
| over the wet one | 21 % → 21 % | 34.1 px | 0.88 | 1.00 | 77 |
| long, no reload | 51 % → 43 % | 22.9 px | 0.86 | 0.84 | 529 | quarters: 0.59 → 0.51 → 0.40 → 0.31

Numbers say: light vs heavy: width 12.3 → 49.0 px, dark 0.81 → 0.88.

## Brush Artist · Refs · #29 Shrigley magenta asterisk
Watercolor · 70 px · 40.8 s

![Brush Artist · Refs · #29 Shrigley magenta asterisk](Brush-Artist-Refs-29-Shrigley-magenta-asterisk.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 10 % → 13 % | 28.0 px | 0.65 | 1.36 | 84 |
| heavy line | 17 % → 18 % | 50.3 px | 0.64 | 1.03 | 183 |
| pressure swell | 11 % → 12 % | 41.1 px | 0.65 | 1.13 | 140 |
| fast wave | 38 % → 38 % | 43.8 px | 0.64 | 1.01 | 410 |
| slow wave | 35 % → 39 % | 41.0 px | 0.65 | 1.10 | 604 |
| spiral | 61 % → 61 % | 40.0 px | 0.64 | 1.01 | 633 |
| loop | 31 % → 32 % | 40.2 px | 0.65 | 1.03 | 340 |
| tilted | 18 % → 18 % | 49.0 px | 0.65 | 1.00 | 275 |
| over the wet one | 31 % → 34 % | 38.4 px | 0.65 | 1.07 | 166 |
| long, no reload | 75 % → 75 % | 33.6 px | 0.64 | 1.00 | 889 | quarters: 0.55 → 0.53 → 0.52 → 0.49

Numbers say: light vs heavy: width 28.0 → 50.3 px, dark 0.65 → 0.64; the long stroke does not run out of paint.

## Brush Artist · Refs · #30 Red gouache face patch
Gouache · 60 px · 46.4 s

![Brush Artist · Refs · #30 Red gouache face patch](Brush-Artist-Refs-30-Red-gouache-face-patch.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 16 % → 15 % | 47.0 px | 0.49 | 0.91 | 191 |
| heavy line | 25 % → 20 % | 74.0 px | 0.49 | 0.80 | 296 |
| pressure swell | 19 % → 17 % | 72.7 px | 0.49 | 0.86 | 197 |
| fast wave | 49 % → 28 % | 56.2 px | 0.49 | 0.58 | 547 |
| slow wave | 48 % → 28 % | 55.4 px | 0.49 | 0.59 | 1244 |
| spiral | 60 % → 28 % | 39.4 px | 0.49 | 0.47 | 949 |
| loop | 40 % → 29 % | 51.6 px | 0.49 | 0.74 | 478 |
| tilted | 16 % → 17 % | 46.0 px | 0.49 | 1.00 | 280 |
| over the wet one | 36 % → 32 % | 55.3 px | 0.49 | 0.89 | 201 |
| long, no reload | 67 % → 30 % | 30.1 px | 0.49 | 0.44 | 1346 | quarters: 0.43 → 0.39 → 0.32 → 0.26

Numbers say: light vs heavy: width 47.0 → 74.0 px, dark 0.49 → 0.49.

## Brush Artist · Refs · #31 Warhol blotted line
Ink · 6 px · 26.0 s

![Brush Artist · Refs · #31 Warhol blotted line](Brush-Artist-Refs-31-Warhol-blotted-line.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 1 % → 3 % | 2.7 px | 0.75 | 3.30 | 47 |
| heavy line | 7 % → 7 % | 20.7 px | 0.83 | 0.98 | 65 |
| pressure swell | 4 % → 4 % | 14.8 px | 0.84 | 1.12 | 50 |
| fast wave | 12 % → 9 % | 13.9 px | 0.82 | 0.76 | 188 |
| slow wave | 10 % → 8 % | 11.2 px | 0.80 | 0.84 | 206 |
| spiral | 15 % → 8 % | 9.7 px | 0.80 | 0.57 | 207 |
| loop | 9 % → 9 % | 11.9 px | 0.80 | 0.93 | 104 |
| tilted | 3 % → 3 % | 8.8 px | 0.84 | 1.03 | 65 |
| over the wet one | 8 % → 8 % | 14.4 px | 0.84 | 1.02 | 64 |
| long, no reload | 21 % → 9 % | 9.6 px | 0.78 | 0.43 | 368 | quarters: 0.25 → 0.13 → 0.05 → 0.01

Numbers say: light vs heavy: width 2.7 → 20.7 px, dark 0.75 → 0.83; wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #32 Thick orange swipes
Heavy acrylic · 90 px · 39.5 s

![Brush Artist · Refs · #32 Thick orange swipes](Brush-Artist-Refs-32-Thick-orange-swipes.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 29 % → 29 % | 83.1 px | 0.38 | 1.00 | 401 |
| heavy line | 30 % → 29 % | 86.4 px | 0.38 | 0.97 | 631 |
| pressure swell | 23 % → 23 % | 86.5 px | 0.38 | 1.01 | 401 |
| fast wave | 63 % → 65 % | 73.1 px | 0.38 | 1.03 | 892 |
| slow wave | 64 % → 63 % | 73.5 px | 0.38 | 0.98 | 1746 |
| spiral | 79 % → 77 % | 52.2 px | 0.38 | 0.98 | 1622 |
| loop | 57 % → 56 % | 73.4 px | 0.38 | 0.99 | 712 |
| tilted | 21 % → 21 % | 59.3 px | 0.38 | 1.00 | 751 |
| over the wet one | 47 % → 45 % | 71.0 px | 0.38 | 0.97 | 624 |
| long, no reload | 95 % → 93 % | 42.8 px | 0.38 | 0.98 | 2574 | quarters: 0.38 → 0.38 → 0.37 → 0.35

Numbers say: light vs heavy: width 83.1 → 86.4 px, dark 0.38 → 0.38; pressure barely changes the width; the long stroke does not run out of paint.

## Brush Artist · Refs · #33 Red wet-in-wet band
Watercolor · 80 px · 53.5 s

![Brush Artist · Refs · #33 Red wet-in-wet band](Brush-Artist-Refs-33-Red-wet-in-wet-band.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 19 % → 31 % | 55.6 px | 0.58 | 1.61 | 172 |
| heavy line | 29 % → 39 % | 83.7 px | 0.59 | 1.35 | 284 |
| pressure swell | 19 % → 27 % | 71.5 px | 0.61 | 1.42 | 165 |
| fast wave | 58 % → 74 % | 67.5 px | 0.61 | 1.27 | 626 |
| slow wave | 57 % → 72 % | 65.7 px | 0.63 | 1.26 | 773 |
| spiral | 75 % → 84 % | 49.6 px | 0.64 | 1.12 | 716 |
| loop | 51 % → 63 % | 66.4 px | 0.62 | 1.22 | 629 |
| tilted | 24 % → 25 % | 66.3 px | 0.60 | 1.03 | 317 |
| over the wet one | 48 % → 67 % | 66.6 px | 0.60 | 1.40 | 213 |
| long, no reload | 95 % → 99 % | 42.6 px | 0.66 | 1.04 | 1270 | quarters: 0.68 → 0.68 → 0.68 → 0.64

Numbers say: light vs heavy: width 55.6 → 83.7 px, dark 0.58 → 0.59; the long stroke does not run out of paint; wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #34 Magenta oil patches
Oil · 60 px · 24.7 s

![Brush Artist · Refs · #34 Magenta oil patches](Brush-Artist-Refs-34-Magenta-oil-patches.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 19 % → 19 % | 55.9 px | 0.61 | 1.00 | 198 |
| heavy line | 21 % → 21 % | 59.9 px | 0.61 | 1.00 | 286 |
| pressure swell | 16 % → 16 % | 58.9 px | 0.62 | 1.01 | 170 |
| fast wave | 48 % → 49 % | 55.5 px | 0.62 | 1.02 | 593 |
| slow wave | 48 % → 48 % | 55.8 px | 0.62 | 1.00 | 1067 |
| spiral | 70 % → 70 % | 46.3 px | 0.62 | 1.00 | 1045 |
| loop | 42 % → 42 % | 54.3 px | 0.62 | 1.00 | 550 |
| tilted | 17 % → 17 % | 46.9 px | 0.61 | 1.00 | 264 |
| over the wet one | 35 % → 35 % | 50.1 px | 0.61 | 1.00 | 211 |
| long, no reload | 86 % → 86 % | 38.7 px | 0.62 | 1.00 | 2196 | quarters: 0.59 → 0.58 → 0.57 → 0.52

Numbers say: light vs heavy: width 55.9 → 59.9 px, dark 0.61 → 0.61; pressure barely changes the width; the long stroke does not run out of paint.

## Brush Artist · Refs · #35 Red band with runs
Watercolor · 70 px · 54.7 s

![Brush Artist · Refs · #35 Red band with runs](Brush-Artist-Refs-35-Red-band-with-runs.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 17 % → 35 % | 48.3 px | 0.47 | 2.08 | 158 |
| heavy line | 25 % → 41 % | 73.9 px | 0.49 | 1.61 | 186 |
| pressure swell | 17 % → 25 % | 63.0 px | 0.53 | 1.50 | 128 |
| fast wave | 54 % → 73 % | 61.9 px | 0.51 | 1.37 | 344 |
| slow wave | 52 % → 71 % | 59.8 px | 0.54 | 1.38 | 700 |
| spiral | 72 % → 89 % | 47.4 px | 0.55 | 1.24 | 652 |
| loop | 47 % → 72 % | 61.4 px | 0.51 | 1.51 | 354 |
| tilted | 21 % → 22 % | 58.2 px | 0.50 | 1.06 | 227 |
| over the wet one | 43 % → 71 % | 62.1 px | 0.50 | 1.66 | 139 |
| long, no reload | 93 % → 98 % | 41.5 px | 0.58 | 1.06 | 1445 | quarters: 0.60 → 0.60 → 0.59 → 0.57

Numbers say: light vs heavy: width 48.3 → 73.9 px, dark 0.47 → 0.49; the long stroke does not run out of paint; wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #36 Magenta letters flat brush
Gouache · 36 px · 35.4 s

![Brush Artist · Refs · #36 Magenta letters flat brush](Brush-Artist-Refs-36-Magenta-letters-flat-brush.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 10 % → 10 % | 29.1 px | 0.45 | 0.98 | 76 |
| heavy line | 17 % → 14 % | 49.1 px | 0.45 | 0.85 | 112 |
| pressure swell | 13 % → 12 % | 49.4 px | 0.45 | 0.89 | 74 |
| fast wave | 35 % → 19 % | 41.0 px | 0.45 | 0.54 | 245 |
| slow wave | 35 % → 19 % | 40.0 px | 0.45 | 0.54 | 414 |
| spiral | 46 % → 19 % | 30.5 px | 0.45 | 0.42 | 381 |
| loop | 27 % → 20 % | 35.4 px | 0.45 | 0.72 | 199 |
| tilted | 11 % → 11 % | 30.0 px | 0.45 | 1.00 | 120 |
| over the wet one | 24 % → 23 % | 38.1 px | 0.45 | 0.92 | 144 |
| long, no reload | 47 % → 19 % | 20.9 px | 0.45 | 0.40 | 830 | quarters: 0.29 → 0.26 → 0.22 → 0.18

Numbers say: light vs heavy: width 29.1 → 49.1 px, dark 0.45 → 0.45.

## Brush Artist · Refs · #37 Oil still life dabs
Oil · 40 px · 16.8 s

![Brush Artist · Refs · #37 Oil still life dabs](Brush-Artist-Refs-37-Oil-still-life-dabs.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 13 % → 13 % | 38.0 px | 0.38 | 1.00 | 248 |
| heavy line | 14 % → 14 % | 41.1 px | 0.38 | 1.00 | 195 |
| pressure swell | 11 % → 11 % | 40.2 px | 0.40 | 1.00 | 141 |
| fast wave | 34 % → 34 % | 39.9 px | 0.39 | 1.00 | 442 |
| slow wave | 35 % → 35 % | 40.2 px | 0.39 | 1.00 | 717 |
| spiral | 59 % → 59 % | 38.7 px | 0.38 | 1.00 | 688 |
| loop | 29 % → 29 % | 37.8 px | 0.39 | 1.00 | 377 |
| tilted | 13 % → 13 % | 36.3 px | 0.39 | 1.00 | 196 |
| over the wet one | 26 % → 26 % | 35.8 px | 0.39 | 1.00 | 162 |
| long, no reload | 69 % → 69 % | 30.9 px | 0.37 | 1.00 | 1353 | quarters: 0.31 → 0.30 → 0.28 → 0.24

Numbers say: light vs heavy: width 38.0 → 41.1 px, dark 0.38 → 0.38; pressure barely changes the width.

## Brush Artist · Refs · #38 Sanguine drawing
Pastel · 6 px · 14.2 s

![Brush Artist · Refs · #38 Sanguine drawing](Brush-Artist-Refs-38-Sanguine-drawing.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 1 % → 1 % | 2.0 px | 0.61 | 1.00 | 15 |
| heavy line | 1 % → 1 % | 3.5 px | 0.62 | 1.00 | 41 |
| pressure swell | 1 % → 1 % | 3.3 px | 0.62 | 1.00 | 17 |
| fast wave | 3 % → 3 % | 3.2 px | 0.61 | 1.00 | 53 |
| slow wave | 3 % → 3 % | 3.0 px | 0.61 | 1.00 | 50 |
| spiral | 4 % → 4 % | 2.9 px | 0.61 | 1.00 | 144 |
| loop | 2 % → 2 % | 3.0 px | 0.61 | 1.00 | 78 |
| tilted | 1 % → 1 % | 3.4 px | 0.62 | 1.00 | 56 |
| over the wet one | 2 % → 2 % | 2.9 px | 0.62 | 1.00 | 31 |
| long, no reload | 7 % → 7 % | 3.0 px | 0.61 | 1.00 | 180 | quarters: 0.04 → 0.05 → 0.05 → 0.05

Numbers say: light vs heavy: width 2.0 → 3.5 px, dark 0.61 → 0.62; the long stroke does not run out of paint.

## Brush Artist · Refs · #39 Very thick impasto
Heavy acrylic · 60 px · 34.6 s

![Brush Artist · Refs · #39 Very thick impasto](Brush-Artist-Refs-39-Very-thick-impasto.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 20 % → 19 % | 56.9 px | 0.60 | 0.97 | 225 |
| heavy line | 21 % → 20 % | 59.6 px | 0.60 | 0.97 | 257 |
| pressure swell | 16 % → 15 % | 59.7 px | 0.62 | 0.97 | 176 |
| fast wave | 48 % → 47 % | 55.2 px | 0.62 | 0.98 | 640 |
| slow wave | 49 % → 47 % | 56.0 px | 0.62 | 0.98 | 1036 |
| spiral | 69 % → 65 % | 45.6 px | 0.62 | 0.93 | 1709 |
| loop | 42 % → 41 % | 54.0 px | 0.62 | 0.97 | 1130 |
| tilted | 16 % → 16 % | 44.1 px | 0.61 | 1.00 | 577 |
| over the wet one | 34 % → 33 % | 51.0 px | 0.61 | 0.97 | 433 |
| long, no reload | 85 % → 79 % | 38.3 px | 0.62 | 0.93 | 2011 | quarters: 0.58 → 0.57 → 0.55 → 0.52

Numbers say: light vs heavy: width 56.9 → 59.6 px, dark 0.60 → 0.60; pressure barely changes the width; the long stroke does not run out of paint.

## Brush Artist · Refs · #40 Watercolour blooms
Watercolor · 90 px · 71.6 s

![Brush Artist · Refs · #40 Watercolour blooms](Brush-Artist-Refs-40-Watercolour-blooms.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 22 % → 33 % | 63.3 px | 0.10 | 1.54 | 369 |
| heavy line | 33 % → 42 % | 94.9 px | 0.11 | 1.28 | 699 |
| pressure swell | 22 % → 30 % | 84.1 px | 0.12 | 1.34 | 240 |
| fast wave | 64 % → 79 % | 73.9 px | 0.11 | 1.23 | 707 |
| slow wave | 63 % → 76 % | 72.4 px | 0.16 | 1.21 | 1269 |
| spiral | 79 % → 87 % | 52.1 px | 0.15 | 1.10 | 1412 |
| loop | 56 % → 66 % | 72.5 px | 0.13 | 1.18 | 755 |
| tilted | 26 % → 27 % | 73.1 px | 0.13 | 1.03 | 471 |
| over the wet one | 53 % → 72 % | 73.8 px | 0.13 | 1.36 | 372 |
| long, no reload | 97 % → 100 % | 43.6 px | 0.17 | 1.02 | 2371 | quarters: 0.21 → 0.19 → 0.17 → 0.13

Numbers say: light vs heavy: width 63.3 → 94.9 px, dark 0.10 → 0.11; wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #41 Coloured pencil hatching
Pastel · 4 px · 13.7 s

![Brush Artist · Refs · #41 Coloured pencil hatching](Brush-Artist-Refs-41-Coloured-pencil-hatching.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 1 % → 1 % | 1.6 px | 0.42 | 1.00 | 28 |
| heavy line | 1 % → 1 % | 2.6 px | 0.43 | 1.00 | 21 |
| pressure swell | 1 % → 1 % | 2.1 px | 0.43 | 1.00 | 19 |
| fast wave | 2 % → 2 % | 2.2 px | 0.42 | 1.00 | 33 |
| slow wave | 2 % → 2 % | 2.1 px | 0.43 | 1.00 | 41 |
| spiral | 3 % → 3 % | 2.1 px | 0.43 | 1.00 | 106 |
| loop | 2 % → 2 % | 2.2 px | 0.43 | 1.00 | 47 |
| tilted | 1 % → 1 % | 3.0 px | 0.42 | 1.00 | 57 |
| over the wet one | 2 % → 2 % | 2.2 px | 0.42 | 1.00 | 13 |
| long, no reload | 5 % → 5 % | 2.3 px | 0.43 | 1.00 | 151 | quarters: 0.02 → 0.02 → 0.02 → 0.03

Numbers say: light vs heavy: width 1.6 → 2.6 px, dark 0.42 → 0.43; the long stroke does not run out of paint.

## Brush Artist · Refs · #42 Oil pastel shaggy
Pastel · 18 px · 15.3 s

![Brush Artist · Refs · #42 Oil pastel shaggy](Brush-Artist-Refs-42-Oil-pastel-shaggy.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 2 % → 2 % | 5.1 px | 0.35 | 1.00 | 75 |
| heavy line | 4 % → 4 % | 10.7 px | 0.36 | 1.00 | 51 |
| pressure swell | 3 % → 3 % | 9.5 px | 0.36 | 1.00 | 42 |
| fast wave | 8 % → 8 % | 9.0 px | 0.36 | 1.00 | 203 |
| slow wave | 7 % → 7 % | 8.2 px | 0.36 | 1.00 | 149 |
| spiral | 12 % → 12 % | 7.7 px | 0.36 | 1.00 | 187 |
| loop | 6 % → 6 % | 7.9 px | 0.36 | 1.00 | 103 |
| tilted | 2 % → 2 % | 6.9 px | 0.36 | 1.00 | 67 |
| over the wet one | 6 % → 6 % | 8.5 px | 0.36 | 1.00 | 42 |
| long, no reload | 15 % → 15 % | 6.9 px | 0.36 | 1.00 | 266 | quarters: 0.00 → 0.00 → 0.00 → 0.00

Numbers say: light vs heavy: width 5.1 → 10.7 px, dark 0.35 → 0.36; the long stroke does not run out of paint.

## Brush Artist · Refs · #43 Dragged black ink blocks
Gouache · 70 px · 39.2 s

![Brush Artist · Refs · #43 Dragged black ink blocks](Brush-Artist-Refs-43-Dragged-black-ink-blocks.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 11 % → 0 % | 31.1 px | 0.65 | 0.03 | 182 |
| heavy line | 16 % → 1 % | 46.9 px | 0.65 | 0.08 | 779 |
| pressure swell | 12 % → 1 % | 44.8 px | 0.65 | 0.11 | 375 |
| fast wave | 22 % → 2 % | 25.8 px | 0.65 | 0.09 | 755 |
| slow wave | 34 % → 4 % | 39.7 px | 0.65 | 0.13 | 1371 |
| spiral | 40 % → 4 % | 26.3 px | 0.65 | 0.11 | 1372 |
| loop | 28 % → 4 % | 36.5 px | 0.65 | 0.14 | 684 |
| tilted | 10 % → 10 % | 28.3 px | 0.65 | 0.98 | 415 |
| over the wet one | 24 % → 9 % | 40.0 px | 0.65 | 0.36 | 422 |
| long, no reload | 47 % → 8 % | 20.9 px | 0.65 | 0.16 | 1893 | quarters: 0.45 → 0.36 → 0.28 → 0.23

Numbers say: light vs heavy: width 31.1 → 46.9 px, dark 0.65 → 0.65.

## Brush Artist · Refs · #44 Blue looping ribbon
Oil · 80 px · 35.6 s

![Brush Artist · Refs · #44 Blue looping ribbon](Brush-Artist-Refs-44-Blue-looping-ribbon.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 26 % → 27 % | 75.0 px | 0.72 | 1.04 | 387 |
| heavy line | 27 % → 27 % | 79.6 px | 0.72 | 1.00 | 474 |
| pressure swell | 21 % → 22 % | 78.2 px | 0.72 | 1.03 | 303 |
| fast wave | 61 % → 64 % | 70.3 px | 0.73 | 1.05 | 1156 |
| slow wave | 61 % → 61 % | 70.0 px | 0.73 | 1.00 | 2559 |
| spiral | 78 % → 78 % | 51.3 px | 0.73 | 1.00 | 1984 |
| loop | 54 % → 54 % | 69.7 px | 0.73 | 1.00 | 900 |
| tilted | 21 % → 21 % | 57.3 px | 0.72 | 1.00 | 435 |
| over the wet one | 44 % → 44 % | 64.9 px | 0.72 | 1.00 | 418 |
| long, no reload | 96 % → 96 % | 42.8 px | 0.73 | 1.00 | 2694 | quarters: 0.72 → 0.73 → 0.73 → 0.69

Numbers say: light vs heavy: width 75.0 → 79.6 px, dark 0.72 → 0.72; pressure barely changes the width; the long stroke does not run out of paint.

## Brush Artist · Refs · #45 Soft pastel pepper
Pastel · 40 px · 13.6 s

![Brush Artist · Refs · #45 Soft pastel pepper](Brush-Artist-Refs-45-Soft-pastel-pepper.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 4 % → 4 % | 11.3 px | 0.53 | 1.00 | 84 |
| heavy line | 8 % → 8 % | 23.0 px | 0.53 | 1.00 | 57 |
| pressure swell | 5 % → 5 % | 19.5 px | 0.53 | 1.00 | 86 |
| fast wave | 17 % → 17 % | 19.4 px | 0.53 | 1.00 | 233 |
| slow wave | 15 % → 15 % | 17.1 px | 0.53 | 1.00 | 646 |
| spiral | 25 % → 25 % | 16.3 px | 0.53 | 1.00 | 487 |
| loop | 12 % → 12 % | 16.1 px | 0.53 | 1.00 | 200 |
| tilted | 5 % → 5 % | 12.8 px | 0.53 | 1.00 | 66 |
| over the wet one | 11 % → 11 % | 17.7 px | 0.53 | 1.00 | 54 |
| long, no reload | 30 % → 30 % | 13.6 px | 0.53 | 1.00 | 344 | quarters: 0.18 → 0.18 → 0.18 → 0.18

Numbers say: light vs heavy: width 11.3 → 23.0 px, dark 0.53 → 0.53; the long stroke does not run out of paint.

## Brush Artist · Refs · #46 Red-brown ink lips
Watercolor · 50 px · 47.0 s

![Brush Artist · Refs · #46 Red-brown ink lips](Brush-Artist-Refs-46-Red-brown-ink-lips.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 12 % → 24 % | 33.6 px | 0.66 | 2.05 | 60 |
| heavy line | 19 % → 30 % | 54.1 px | 0.64 | 1.62 | 104 |
| pressure swell | 12 % → 21 % | 43.7 px | 0.67 | 1.77 | 64 |
| fast wave | 40 % → 61 % | 46.7 px | 0.66 | 1.50 | 213 |
| slow wave | 39 % → 59 % | 44.6 px | 0.69 | 1.54 | 361 |
| spiral | 63 % → 76 % | 41.7 px | 0.70 | 1.20 | 469 |
| loop | 35 % → 52 % | 44.9 px | 0.67 | 1.50 | 326 |
| tilted | 16 % → 17 % | 43.6 px | 0.66 | 1.07 | 160 |
| over the wet one | 33 % → 52 % | 47.6 px | 0.66 | 1.58 | 111 |
| long, no reload | 79 % → 95 % | 35.4 px | 0.70 | 1.21 | 595 | quarters: 0.71 → 0.71 → 0.70 → 0.65

Numbers say: light vs heavy: width 33.6 → 54.1 px, dark 0.66 → 0.64; the long stroke does not run out of paint; wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #47 Pink knife slabs
Heavy acrylic · 90 px · 33.3 s

![Brush Artist · Refs · #47 Pink knife slabs](Brush-Artist-Refs-47-Pink-knife-slabs.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 28 % → 27 % | 81.1 px | 0.29 | 0.97 | 223 |
| heavy line | 29 % → 28 % | 83.5 px | 0.29 | 0.97 | 250 |
| pressure swell | 22 % → 22 % | 83.4 px | 0.29 | 1.01 | 159 |
| fast wave | 61 % → 60 % | 70.3 px | 0.28 | 0.99 | 575 |
| slow wave | 61 % → 59 % | 71.0 px | 0.27 | 0.96 | 1027 |
| spiral | 76 % → 57 % | 50.1 px | 0.27 | 0.76 | 1280 |
| loop | 55 % → 54 % | 71.8 px | 0.28 | 0.97 | 696 |
| tilted | 21 % → 21 % | 59.3 px | 0.29 | 1.00 | 377 |
| over the wet one | 46 % → 44 % | 68.0 px | 0.29 | 0.96 | 269 |
| long, no reload | 92 % → 76 % | 41.4 px | 0.26 | 0.82 | 1586 | quarters: 0.00 → 0.00 → 0.00 → 0.00

Numbers say: light vs heavy: width 81.1 → 83.5 px, dark 0.29 → 0.29; pressure barely changes the width; the long stroke does not run out of paint.

## Brush Artist · Refs · #48 Black bands with drips
Gouache · 70 px · 49.1 s

![Brush Artist · Refs · #48 Black bands with drips](Brush-Artist-Refs-48-Black-bands-with-drips.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 19 % → 18 % | 54.7 px | 0.68 | 0.94 | 228 |
| heavy line | 29 % → 24 % | 83.1 px | 0.68 | 0.85 | 306 |
| pressure swell | 23 % → 21 % | 86.1 px | 0.68 | 0.92 | 182 |
| fast wave | 54 % → 37 % | 62.8 px | 0.68 | 0.67 | 539 |
| slow wave | 54 % → 36 % | 61.9 px | 0.68 | 0.67 | 1077 |
| spiral | 64 % → 35 % | 42.2 px | 0.68 | 0.54 | 1102 |
| loop | 45 % → 37 % | 58.1 px | 0.68 | 0.82 | 437 |
| tilted | 19 % → 19 % | 52.5 px | 0.68 | 1.00 | 246 |
| over the wet one | 41 % → 38 % | 62.5 px | 0.68 | 0.92 | 281 |
| long, no reload | 74 % → 37 % | 33.4 px | 0.68 | 0.50 | 1334 | quarters: 0.64 → 0.61 → 0.54 → 0.44

Numbers say: light vs heavy: width 54.7 → 83.1 px, dark 0.68 → 0.68.

## Brush Artist · Refs · #49 Magenta letters round brush
Ink · 30 px · 37.2 s

![Brush Artist · Refs · #49 Magenta letters round brush](Brush-Artist-Refs-49-Magenta-letters-round-brush.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 6 % → 8 % | 17.5 px | 0.50 | 1.29 | 62 |
| heavy line | 21 % → 21 % | 62.0 px | 0.51 | 0.99 | 163 |
| pressure swell | 12 % → 13 % | 46.3 px | 0.52 | 1.02 | 87 |
| fast wave | 39 % → 38 % | 44.8 px | 0.51 | 0.99 | 256 |
| slow wave | 32 % → 31 % | 36.7 px | 0.51 | 0.99 | 454 |
| spiral | 50 % → 49 % | 33.2 px | 0.51 | 0.97 | 322 |
| loop | 29 % → 29 % | 37.8 px | 0.51 | 1.00 | 172 |
| tilted | 11 % → 11 % | 31.0 px | 0.52 | 1.01 | 89 |
| over the wet one | 26 % → 26 % | 42.0 px | 0.52 | 1.01 | 89 |
| long, no reload | 62 % → 56 % | 27.7 px | 0.50 | 0.91 | 598 | quarters: 0.41 → 0.36 → 0.30 → 0.25

Numbers say: light vs heavy: width 17.5 → 62.0 px, dark 0.50 → 0.51.

## Brush Artist · Refs · #50 Thick swipes on photo
Heavy acrylic · 40 px · 22.5 s

![Brush Artist · Refs · #50 Thick swipes on photo](Brush-Artist-Refs-50-Thick-swipes-on-photo.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 13 % → 13 % | 38.1 px | 0.27 | 0.96 | 144 |
| heavy line | 14 % → 13 % | 40.2 px | 0.27 | 0.96 | 164 |
| pressure swell | 11 % → 10 % | 40.1 px | 0.25 | 0.95 | 110 |
| fast wave | 33 % → 31 % | 38.3 px | 0.25 | 0.93 | 394 |
| slow wave | 34 % → 32 % | 39.1 px | 0.26 | 0.95 | 674 |
| spiral | 58 % → 46 % | 38.5 px | 0.25 | 0.80 | 722 |
| loop | 28 % → 27 % | 36.9 px | 0.26 | 0.95 | 368 |
| tilted | 12 % → 12 % | 34.1 px | 0.26 | 1.00 | 179 |
| over the wet one | 25 % → 24 % | 35.3 px | 0.26 | 0.95 | 118 |
| long, no reload | 66 % → 46 % | 29.6 px | 0.24 | 0.69 | 844 | quarters: 0.00 → 0.00 → 0.00 → 0.00

Numbers say: light vs heavy: width 38.1 → 40.2 px, dark 0.27 → 0.27; pressure barely changes the width; the long stroke does not run out of paint.

## Brush Artist · Refs · Drag #e8b4a8
Gouache · 40 px · 24.5 s

![Brush Artist · Refs · Drag #e8b4a8](Brush-Artist-Refs-Drag-e8b4a8.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 2 % → 0 % | 5.0 px | 0.00 | 0.00 | 98 |
| heavy line | 3 % → 0 % | 8.7 px | 0.00 | 0.00 | 214 |
| pressure swell | 2 % → 0 % | 9.1 px | 0.00 | 0.00 | 145 |
| fast wave | 3 % → 0 % | 3.4 px | 0.00 | 0.00 | 271 |
| slow wave | 9 % → 0 % | 10.9 px | 0.00 | 0.00 | 550 |
| spiral | 10 % → 0 % | 6.9 px | 0.00 | 0.00 | 601 |
| loop | 6 % → 0 % | 7.9 px | 0.34 | 0.01 | 339 |
| tilted | 2 % → 2 % | 6.3 px | 0.34 | 0.89 | 142 |
| over the wet one | 5 % → 0 % | 8.2 px | 0.34 | 0.02 | 166 |
| long, no reload | 12 % → 0 % | 5.4 px | 0.34 | 0.01 | 909 | quarters: 0.01 → 0.01 → 0.01 → 0.01

Numbers say: light vs heavy: width 5.0 → 8.7 px, dark 0.00 → 0.00; the long stroke does not run out of paint.

## Brush Artist · Refs · Drag #e8e4e0
Gouache · 40 px · 23.1 s

![Brush Artist · Refs · Drag #e8e4e0](Brush-Artist-Refs-Drag-e8e4e0.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 2 % → 0 % | 5.0 px | 0.00 | 0.00 | 146 |
| heavy line | 3 % → 0 % | 8.7 px | 0.00 | 0.00 | 167 |
| pressure swell | 2 % → 0 % | 9.1 px | 0.00 | 0.00 | 105 |
| fast wave | 3 % → 0 % | 3.4 px | 0.00 | 0.00 | 333 |
| slow wave | 9 % → 0 % | 10.9 px | 0.00 | 0.00 | 654 |
| spiral | 10 % → 0 % | 6.9 px | 0.00 | 0.00 | 479 |
| loop | 6 % → 0 % | 7.9 px | 0.42 | 0.01 | 262 |
| tilted | 2 % → 2 % | 6.3 px | 0.42 | 0.89 | 172 |
| over the wet one | 5 % → 0 % | 8.2 px | 0.42 | 0.02 | 206 |
| long, no reload | 12 % → 0 % | 5.4 px | 0.43 | 0.01 | 854 | quarters: 0.01 → 0.01 → 0.01 → 0.01

Numbers say: light vs heavy: width 5.0 → 8.7 px, dark 0.00 → 0.00; the long stroke does not run out of paint.

## Brush Artist · Refs · Finger
Pastel · 36 px · 24.9 s · over bands of wet oil paint and oil pastel in turn (it works on paint already there: look at what it does to the bands; covered counts the bands too)

![Brush Artist · Refs · Finger](Brush-Artist-Refs-Finger.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 25 % → 25 % | 73.8 px | 0.80 | 1.00 | 47 |
| heavy line | 27 % → 27 % | 78.6 px | 0.80 | 1.00 | 55 |
| pressure swell | 26 % → 26 % | 97.7 px | 0.80 | 1.00 | 39 |
| fast wave | 32 % → 32 % | 37.3 px | 0.78 | 1.00 | 153 |
| slow wave | 31 % → 31 % | 36.3 px | 0.78 | 1.00 | 312 |
| spiral | 38 % → 38 % | 25.2 px | 0.76 | 1.00 | 286 |
| loop | 30 % → 30 % | 39.4 px | 0.78 | 1.00 | 139 |
| tilted | 26 % → 26 % | 73.4 px | 0.78 | 1.00 | 89 |
| over the wet one | 29 % → 29 % | 6.8 px | 0.78 | 1.00 | 68 |
| long, no reload | 41 % → 41 % | 18.2 px | 0.76 | 1.00 | 529 | quarters: 0.25 → 0.37 → 0.34 → 0.39

Numbers say: light vs heavy: width 73.8 → 78.6 px, dark 0.80 → 0.80; pressure barely changes the width; the long stroke does not run out of paint.

## Brush Artist · Ink — wash
Watercolor · 38 px · 35.1 s

![Brush Artist · Ink — wash](Brush-Artist-Ink-wash.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 11 % → 11 % | 31.6 px | 0.38 | 1.04 | 81 |
| heavy line | 19 % → 19 % | 54.3 px | 0.32 | 1.03 | 145 |
| pressure swell | 12 % → 12 % | 45.1 px | 0.36 | 1.04 | 98 |
| fast wave | 39 % → 41 % | 45.5 px | 0.30 | 1.04 | 360 |
| slow wave | 37 % → 38 % | 42.9 px | 0.37 | 1.03 | 402 |
| spiral | 58 % → 60 % | 38.5 px | 0.30 | 1.04 | 380 |
| loop | 32 % → 33 % | 41.9 px | 0.35 | 1.02 | 208 |
| tilted | 13 % → 14 % | 36.9 px | 0.38 | 1.04 | 105 |
| over the wet one | 29 % → 30 % | 42.7 px | 0.38 | 1.04 | 105 |
| long, no reload | 67 % → 71 % | 29.9 px | 0.29 | 1.07 | 632 | quarters: 0.33 → 0.26 → 0.19 → 0.12

Numbers say: light vs heavy: width 31.6 → 54.3 px, dark 0.38 → 0.32.

## Brush Artist · Ink — brush line
Ink · 16 px · 27.6 s

![Brush Artist · Ink — brush line](Brush-Artist-Ink-brush-line.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 3 % → 5 % | 7.7 px | 0.78 | 1.81 | 44 |
| heavy line | 13 % → 13 % | 39.0 px | 0.88 | 0.99 | 112 |
| pressure swell | 8 % → 8 % | 28.4 px | 0.87 | 1.05 | 89 |
| fast wave | 24 % → 23 % | 28.0 px | 0.87 | 0.96 | 265 |
| slow wave | 20 % → 19 % | 22.6 px | 0.87 | 0.97 | 182 |
| spiral | 30 % → 27 % | 20.1 px | 0.86 | 0.89 | 260 |
| loop | 18 % → 18 % | 23.6 px | 0.88 | 1.00 | 128 |
| tilted | 7 % → 7 % | 20.5 px | 0.88 | 1.01 | 72 |
| over the wet one | 17 % → 17 % | 26.8 px | 0.88 | 1.00 | 63 |
| long, no reload | 42 % → 30 % | 18.9 px | 0.85 | 0.71 | 399 | quarters: 0.49 → 0.40 → 0.30 → 0.20

Numbers say: light vs heavy: width 7.7 → 39.0 px, dark 0.78 → 0.88; wet paint spreads well beyond the stroke.

## Brush Artist · Ink — dry brush
Gouache · 30 px · 19.9 s

![Brush Artist · Ink — dry brush](Brush-Artist-Ink-dry-brush.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 3 % → 0 % | 9.2 px | 0.77 | 0.00 | 77 |
| heavy line | 5 % → 0 % | 14.0 px | 0.00 | 0.00 | 118 |
| pressure swell | 4 % → 0 % | 13.5 px | 0.77 | 0.01 | 69 |
| fast wave | 7 % → 0 % | 8.0 px | 0.77 | 0.00 | 265 |
| slow wave | 11 % → 0 % | 12.2 px | 0.77 | 0.01 | 448 |
| spiral | 14 % → 0 % | 9.2 px | 0.77 | 0.01 | 382 |
| loop | 9 % → 0 % | 11.1 px | 0.77 | 0.02 | 199 |
| tilted | 4 % → 4 % | 11.2 px | 0.77 | 0.94 | 104 |
| over the wet one | 8 % → 1 % | 12.2 px | 0.77 | 0.10 | 98 |
| long, no reload | 16 % → 1 % | 7.2 px | 0.77 | 0.03 | 556 | quarters: 0.21 → 0.15 → 0.12 → 0.11

Numbers say: light vs heavy: width 9.2 → 14.0 px, dark 0.77 → 0.00.

## Brush Artist · Watercolour — blue
Watercolor · 40 px · 28.7 s

![Brush Artist · Watercolour — blue](Brush-Artist-Watercolour-blue.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 6 % → 10 % | 16.7 px | 0.25 | 1.71 | 33 |
| heavy line | 11 % → 12 % | 31.5 px | 0.25 | 1.13 | 66 |
| pressure swell | 7 % → 9 % | 25.4 px | 0.26 | 1.32 | 41 |
| fast wave | 24 % → 25 % | 27.8 px | 0.24 | 1.06 | 165 |
| slow wave | 22 % → 27 % | 25.9 px | 0.26 | 1.22 | 237 |
| spiral | 38 % → 41 % | 25.2 px | 0.22 | 1.08 | 320 |
| loop | 20 % → 22 % | 25.3 px | 0.26 | 1.13 | 165 |
| tilted | 12 % → 12 % | 33.3 px | 0.26 | 1.00 | 89 |
| over the wet one | 21 % → 24 % | 24.7 px | 0.26 | 1.15 | 59 |
| long, no reload | 52 % → 54 % | 23.1 px | 0.22 | 1.04 | 419 | quarters: 0.18 → 0.14 → 0.11 → 0.08

Numbers say: light vs heavy: width 16.7 → 31.5 px, dark 0.25 → 0.25; wet paint spreads well beyond the stroke.

## Brush Artist · Watercolour — violet
Watercolor · 40 px · 32.5 s

![Brush Artist · Watercolour — violet](Brush-Artist-Watercolour-violet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 6 % → 10 % | 16.7 px | 0.40 | 1.71 | 38 |
| heavy line | 11 % → 12 % | 31.5 px | 0.40 | 1.13 | 70 |
| pressure swell | 7 % → 9 % | 25.4 px | 0.41 | 1.32 | 41 |
| fast wave | 24 % → 25 % | 27.8 px | 0.38 | 1.06 | 143 |
| slow wave | 22 % → 27 % | 25.9 px | 0.41 | 1.22 | 287 |
| spiral | 38 % → 41 % | 25.2 px | 0.36 | 1.08 | 302 |
| loop | 20 % → 22 % | 25.3 px | 0.40 | 1.13 | 115 |
| tilted | 12 % → 12 % | 33.3 px | 0.40 | 1.00 | 89 |
| over the wet one | 21 % → 24 % | 24.7 px | 0.40 | 1.15 | 58 |
| long, no reload | 52 % → 54 % | 23.1 px | 0.34 | 1.04 | 342 | quarters: 0.28 → 0.22 → 0.18 → 0.14

Numbers say: light vs heavy: width 16.7 → 31.5 px, dark 0.40 → 0.40; wet paint spreads well beyond the stroke.

## Brush Artist · Watercolour — teal
Watercolor · 40 px · 28.4 s

![Brush Artist · Watercolour — teal](Brush-Artist-Watercolour-teal.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 6 % → 10 % | 16.7 px | 0.16 | 1.71 | 43 |
| heavy line | 11 % → 12 % | 31.5 px | 0.16 | 1.13 | 69 |
| pressure swell | 7 % → 9 % | 25.4 px | 0.17 | 1.32 | 43 |
| fast wave | 24 % → 25 % | 27.8 px | 0.15 | 1.06 | 134 |
| slow wave | 22 % → 27 % | 25.9 px | 0.17 | 1.22 | 222 |
| spiral | 38 % → 41 % | 25.2 px | 0.15 | 1.08 | 228 |
| loop | 20 % → 22 % | 25.3 px | 0.16 | 1.13 | 119 |
| tilted | 12 % → 12 % | 33.3 px | 0.16 | 1.00 | 98 |
| over the wet one | 21 % → 24 % | 24.7 px | 0.16 | 1.15 | 58 |
| long, no reload | 52 % → 54 % | 23.1 px | 0.14 | 1.04 | 340 | quarters: 0.11 → 0.09 → 0.07 → 0.06

Numbers say: light vs heavy: width 16.7 → 31.5 px, dark 0.16 → 0.16; wet paint spreads well beyond the stroke.

## Brush Artist · Gouache
Gouache · 30 px · 29.8 s

![Brush Artist · Gouache](Brush-Artist-Gouache.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 8 % → 8 % | 24.4 px | 0.27 | 0.97 | 107 |
| heavy line | 15 % → 12 % | 42.9 px | 0.27 | 0.78 | 132 |
| pressure swell | 11 % → 9 % | 41.1 px | 0.27 | 0.85 | 68 |
| fast wave | 30 % → 14 % | 35.0 px | 0.26 | 0.45 | 219 |
| slow wave | 29 % → 14 % | 34.0 px | 0.26 | 0.47 | 323 |
| spiral | 40 % → 14 % | 26.7 px | 0.26 | 0.35 | 321 |
| loop | 24 % → 15 % | 30.6 px | 0.26 | 0.62 | 162 |
| tilted | 10 % → 10 % | 27.5 px | 0.27 | 1.01 | 90 |
| over the wet one | 22 % → 19 % | 32.8 px | 0.27 | 0.89 | 75 |
| long, no reload | 43 % → 15 % | 19.1 px | 0.26 | 0.35 | 469 | quarters: 0.01 → 0.01 → 0.01 → 0.01

Numbers say: light vs heavy: width 24.4 → 42.9 px, dark 0.27 → 0.27; the long stroke does not run out of paint.

## Brush Artist · Oil — bristle
Oil · 30 px · 14.1 s

![Brush Artist · Oil — bristle](Brush-Artist-Oil-bristle.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 9 % → 9 % | 26.3 px | 0.53 | 1.00 | 104 |
| heavy line | 10 % → 10 % | 28.6 px | 0.54 | 1.00 | 136 |
| pressure swell | 8 % → 8 % | 28.3 px | 0.55 | 1.00 | 81 |
| fast wave | 24 % → 24 % | 27.3 px | 0.55 | 1.00 | 291 |
| slow wave | 25 % → 25 % | 28.3 px | 0.55 | 1.00 | 499 |
| spiral | 39 % → 39 % | 25.6 px | 0.54 | 1.00 | 494 |
| loop | 20 % → 20 % | 26.3 px | 0.54 | 1.00 | 256 |
| tilted | 11 % → 11 % | 29.9 px | 0.53 | 1.00 | 140 |
| over the wet one | 20 % → 20 % | 25.5 px | 0.53 | 1.00 | 135 |
| long, no reload | 50 % → 50 % | 22.4 px | 0.54 | 1.00 | 737 | quarters: 0.32 → 0.30 → 0.29 → 0.28

Numbers say: light vs heavy: width 26.3 → 28.6 px, dark 0.53 → 0.54; pressure barely changes the width; the long stroke does not run out of paint.

## Brush Artist · Charcoal — stick
Charcoal · 28 px · 9.8 s

![Brush Artist · Charcoal — stick](Brush-Artist-Charcoal-stick.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 3 % → 3 % | 8.4 px | 0.85 | 1.00 | 20 |
| heavy line | 6 % → 6 % | 17.8 px | 0.85 | 1.00 | 29 |
| pressure swell | 4 % → 4 % | 13.9 px | 0.85 | 1.00 | 16 |
| fast wave | 12 % → 12 % | 14.0 px | 0.85 | 1.00 | 48 |
| slow wave | 11 % → 11 % | 12.5 px | 0.85 | 1.00 | 85 |
| spiral | 19 % → 19 % | 12.7 px | 0.85 | 1.00 | 91 |
| loop | 10 % → 10 % | 12.8 px | 0.85 | 1.00 | 49 |
| tilted | 4 % → 4 % | 10.9 px | 0.85 | 1.00 | 30 |
| over the wet one | 9 % → 9 % | 13.5 px | 0.85 | 1.00 | 20 |
| long, no reload | 27 % → 27 % | 12.2 px | 0.85 | 1.00 | 119 | quarters: 0.26 → 0.25 → 0.26 → 0.27

Numbers say: light vs heavy: width 8.4 → 17.8 px, dark 0.85 → 0.85; the long stroke does not run out of paint.

## Brush Artist · Charcoal — stick B
Charcoal · 36 px · 9.9 s

![Brush Artist · Charcoal — stick B](Brush-Artist-Charcoal-stick-B.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 4 % → 4 % | 10.5 px | 0.85 | 1.00 | 26 |
| heavy line | 7 % → 7 % | 21.1 px | 0.85 | 1.00 | 42 |
| pressure swell | 4 % → 4 % | 16.5 px | 0.85 | 1.00 | 24 |
| fast wave | 15 % → 15 % | 16.8 px | 0.85 | 1.00 | 66 |
| slow wave | 13 % → 13 % | 14.7 px | 0.85 | 1.00 | 113 |
| spiral | 23 % → 23 % | 15.0 px | 0.85 | 1.00 | 114 |
| loop | 11 % → 11 % | 14.8 px | 0.85 | 1.00 | 57 |
| tilted | 4 % → 4 % | 12.3 px | 0.85 | 1.00 | 47 |
| over the wet one | 10 % → 10 % | 15.9 px | 0.85 | 1.00 | 38 |
| long, no reload | 31 % → 31 % | 13.9 px | 0.85 | 1.00 | 229 | quarters: 0.30 → 0.28 → 0.29 → 0.30

Numbers say: light vs heavy: width 10.5 → 21.1 px, dark 0.85 → 0.85; the long stroke does not run out of paint.

## Brush Artist · Charcoal — stick C
Charcoal · 22 px · 9.5 s

![Brush Artist · Charcoal — stick C](Brush-Artist-Charcoal-stick-C.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 2 % → 2 % | 6.9 px | 0.85 | 1.00 | 19 |
| heavy line | 5 % → 5 % | 15.3 px | 0.85 | 1.00 | 34 |
| pressure swell | 3 % → 3 % | 12.2 px | 0.85 | 1.00 | 13 |
| fast wave | 10 % → 10 % | 12.1 px | 0.85 | 1.00 | 41 |
| slow wave | 9 % → 9 % | 10.8 px | 0.85 | 1.00 | 64 |
| spiral | 17 % → 17 % | 11.0 px | 0.85 | 1.00 | 72 |
| loop | 9 % → 9 % | 11.4 px | 0.85 | 1.00 | 36 |
| tilted | 4 % → 4 % | 9.9 px | 0.85 | 1.00 | 25 |
| over the wet one | 8 % → 8 % | 11.7 px | 0.85 | 1.00 | 17 |
| long, no reload | 24 % → 24 % | 11.0 px | 0.85 | 1.00 | 107 | quarters: 0.24 → 0.22 → 0.23 → 0.24

Numbers say: light vs heavy: width 6.9 → 15.3 px, dark 0.85 → 0.85; the long stroke does not run out of paint.

## Brush Artist · Refs · #01 Henry Ward peach cloud — own sheet
own sheet 600 × 600 · Gouache · 44 px · 14.5 s

![Brush Artist · Refs · #01 Henry Ward peach cloud — own sheet](Brush-Artist-Refs-01-Henry-Ward-peach-cloud-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 14 % → 39 % | 40.5 px | 0.59 | 2.74 | 224 |
| stroke 2 | 24 % → 58 % | 79.5 px | 0.59 | 2.40 | 193 |
| stroke 3 | 28 % → 56 % | 81.3 px | 0.59 | 2.01 | 201 |
| stroke 4 | 30 % → 63 % | 99.7 px | 0.59 | 2.05 | 170 |
| stroke 5 | 30 % → 55 % | 86.0 px | 0.59 | 1.86 | 147 |
| stroke 6 | 30 % → 42 % | 91.1 px | 0.59 | 1.42 | 143 |
| stroke 7 | 16 % → 53 % | 38.9 px | 0.59 | 3.38 | 149 |
| stroke 8 | 18 % → 49 % | 44.8 px | 0.59 | 2.76 | 163 |
| stroke 9 | 21 % → 50 % | 54.2 px | 0.59 | 2.39 | 155 |
| stroke 10 | 23 % → 51 % | 61.9 px | 0.59 | 2.21 | 175 |
| stroke 11 | 25 % → 54 % | 72.0 px | 0.59 | 2.11 | 163 |
| stroke 12 | 29 % → 56 % | 88.0 px | 0.59 | 1.92 | 152 |
| stroke 13 | 37 % → 59 % | 108.0 px | 0.59 | 1.59 | 161 |
| stroke 14 | 40 % → 61 % | 113.8 px | 0.59 | 1.54 | 159 |
| stroke 15 | 53 % → 67 % | 156.4 px | 0.59 | 1.27 | 152 |
| stroke 16 | 54 % → 68 % | 164.9 px | 0.59 | 1.24 | 140 |
| stroke 17 | 55 % → 69 % | 155.8 px | 0.59 | 1.24 | 152 |
| stroke 18 | 57 % → 67 % | 164.8 px | 0.59 | 1.19 | 154 |
| stroke 19 | 58 % → 66 % | 163.9 px | 0.59 | 1.13 | 150 |
| stroke 20 | 58 % → 63 % | 167.5 px | 0.59 | 1.09 | 158 |
| stroke 21 | 58 % → 60 % | 168.2 px | 0.59 | 1.04 | 158 |
| stroke 22 | 59 % → 61 % | 173.1 px | 0.59 | 1.03 | 157 |
| stroke 23 | 59 % → 59 % | 167.7 px | 0.59 | 1.00 | 155 |
| stroke 24 | 63 % → 62 % | 187.3 px | 0.59 | 0.99 | 143 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #02 Henry Ward cream strokes — own sheet
own sheet 600 × 600 · Gouache · 46 px · 8.8 s

![Brush Artist · Refs · #02 Henry Ward cream strokes — own sheet](Brush-Artist-Refs-02-Henry-Ward-cream-strokes-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 18 % → 32 % | 37.3 px | 0.70 | 1.77 | 224 |
| stroke 2 | 28 % → 37 % | 72.5 px | 0.70 | 1.34 | 214 |
| stroke 3 | 27 % → 44 % | 68.7 px | 0.71 | 1.64 | 221 |
| stroke 4 | 29 % → 41 % | 71.2 px | 0.71 | 1.42 | 226 |
| stroke 5 | 35 % → 45 % | 85.0 px | 0.71 | 1.29 | 208 |
| stroke 6 | 28 % → 39 % | 66.8 px | 0.70 | 1.42 | 207 |
| stroke 7 | 29 % → 27 % | 74.4 px | 0.70 | 0.92 | 204 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #03 Henry Ward navy contours — own sheet
own sheet 600 × 600 · Heavy acrylic · 22 px · 2.4 s

![Brush Artist · Refs · #03 Henry Ward navy contours — own sheet](Brush-Artist-Refs-03-Henry-Ward-navy-contours-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 11 % → 18 % | 23.1 px | 0.69 | 1.56 | 117 |
| stroke 2 | 20 % → 23 % | 28.3 px | 0.69 | 1.14 | 100 |
| stroke 3 | 23 % → 23 % | 33.4 px | 0.69 | 1.01 | 122 |
| stroke 4 | 23 % → 21 % | 50.8 px | 0.69 | 0.92 | 146 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #04 Henry Ward grey cloud — own sheet
own sheet 600 × 600 · Gouache · 50 px · 14.5 s

![Brush Artist · Refs · #04 Henry Ward grey cloud — own sheet](Brush-Artist-Refs-04-Henry-Ward-grey-cloud-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 14 % → 48 % | 42.2 px | 0.40 | 3.32 | 202 |
| stroke 2 | 19 % → 50 % | 53.3 px | 0.40 | 2.68 | 218 |
| stroke 3 | 27 % → 57 % | 75.3 px | 0.40 | 2.11 | 221 |
| stroke 4 | 30 % → 60 % | 88.0 px | 0.40 | 1.98 | 228 |
| stroke 5 | 36 % → 66 % | 110.1 px | 0.40 | 1.83 | 215 |
| stroke 6 | 40 % → 70 % | 129.7 px | 0.40 | 1.77 | 209 |
| stroke 7 | 46 % → 77 % | 134.2 px | 0.40 | 1.67 | 231 |
| stroke 8 | 45 % → 77 % | 133.7 px | 0.40 | 1.70 | 226 |
| stroke 9 | 45 % → 77 % | 133.8 px | 0.40 | 1.72 | 230 |
| stroke 10 | 46 % → 77 % | 148.0 px | 0.40 | 1.67 | 210 |
| stroke 11 | 46 % → 77 % | 130.7 px | 0.40 | 1.67 | 231 |
| stroke 12 | 47 % → 76 % | 141.7 px | 0.40 | 1.63 | 239 |
| stroke 13 | 46 % → 77 % | 131.3 px | 0.40 | 1.67 | 275 |
| stroke 14 | 47 % → 77 % | 139.7 px | 0.40 | 1.64 | 285 |
| stroke 15 | 46 % → 72 % | 133.2 px | 0.40 | 1.56 | 309 |
| stroke 16 | 47 % → 70 % | 143.4 px | 0.40 | 1.47 | 252 |
| stroke 17 | 45 % → 61 % | 130.9 px | 0.40 | 1.33 | 210 |
| stroke 18 | 45 % → 56 % | 149.2 px | 0.40 | 1.24 | 196 |
| stroke 19 | 46 % → 47 % | 136.3 px | 0.40 | 1.03 | 209 |
| stroke 20 | 47 % → 46 % | 148.0 px | 0.40 | 0.99 | 214 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #05 Henry Ward green in rust loops — own sheet
own sheet 600 × 600 · Heavy acrylic · 20 px · 2.5 s

![Brush Artist · Refs · #05 Henry Ward green in rust loops — own sheet](Brush-Artist-Refs-05-Henry-Ward-green-in-rust-loops-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 12 % → 19 % | 20.9 px | 0.02 | 1.60 | 141 |
| stroke 2 | 12 % → 11 % | 23.6 px | 0.02 | 0.93 | 203 |
| stroke 3 | 23 % → 21 % | 41.5 px | 0.02 | 0.93 | 165 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #06 Henry Ward scrubbed grey — own sheet
own sheet 600 × 600 · Gouache · 50 px · 15.8 s

![Brush Artist · Refs · #06 Henry Ward scrubbed grey — own sheet](Brush-Artist-Refs-06-Henry-Ward-scrubbed-grey-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 17 % → 54 % | 42.0 px | 0.40 | 3.16 | 217 |
| stroke 2 | 22 % → 56 % | 58.8 px | 0.40 | 2.55 | 223 |
| stroke 3 | 28 % → 61 % | 87.1 px | 0.40 | 2.13 | 210 |
| stroke 4 | 29 % → 61 % | 92.8 px | 0.40 | 2.06 | 203 |
| stroke 5 | 42 % → 75 % | 127.0 px | 0.40 | 1.78 | 206 |
| stroke 6 | 45 % → 76 % | 138.6 px | 0.40 | 1.67 | 214 |
| stroke 7 | 47 % → 77 % | 133.9 px | 0.40 | 1.64 | 218 |
| stroke 8 | 47 % → 77 % | 147.9 px | 0.40 | 1.65 | 199 |
| stroke 9 | 45 % → 77 % | 137.9 px | 0.40 | 1.71 | 203 |
| stroke 10 | 45 % → 77 % | 147.0 px | 0.40 | 1.70 | 198 |
| stroke 11 | 46 % → 77 % | 136.1 px | 0.40 | 1.66 | 208 |
| stroke 12 | 47 % → 77 % | 143.2 px | 0.40 | 1.64 | 215 |
| stroke 13 | 45 % → 77 % | 127.5 px | 0.40 | 1.71 | 217 |
| stroke 14 | 44 % → 76 % | 130.2 px | 0.40 | 1.72 | 216 |
| stroke 15 | 45 % → 77 % | 128.6 px | 0.40 | 1.71 | 218 |
| stroke 16 | 46 % → 77 % | 146.4 px | 0.40 | 1.68 | 199 |
| stroke 17 | 45 % → 70 % | 134.2 px | 0.40 | 1.55 | 207 |
| stroke 18 | 47 % → 67 % | 141.3 px | 0.40 | 1.44 | 217 |
| stroke 19 | 45 % → 61 % | 134.0 px | 0.40 | 1.36 | 215 |
| stroke 20 | 45 % → 59 % | 141.3 px | 0.40 | 1.30 | 212 |
| stroke 21 | 45 % → 50 % | 131.4 px | 0.40 | 1.11 | 217 |
| stroke 22 | 46 % → 45 % | 151.0 px | 0.40 | 0.99 | 193 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #07 Henry Ward blue L + black zigzag — own sheet
own sheet 600 × 600 · Heavy acrylic · 34 px · 1.9 s

![Brush Artist · Refs · #07 Henry Ward blue L + black zigzag — own sheet](Brush-Artist-Refs-07-Henry-Ward-blue-L-black-zigzag-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 15 % → 17 % | 35.6 px | 0.59 | 1.14 | 113 |
| stroke 2 | 17 % → 16 % | 42.8 px | 0.59 | 0.93 | 89 |

## Brush Artist · Refs · #08 Henry Ward olive bands — own sheet
own sheet 600 × 600 · Gouache · 34 px · 5.0 s

![Brush Artist · Refs · #08 Henry Ward olive bands — own sheet](Brush-Artist-Refs-08-Henry-Ward-olive-bands-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 9 % → 7 % | 17.9 px | 0.59 | 0.82 | 155 |
| stroke 2 | 15 % → 9 % | 32.8 px | 0.59 | 0.63 | 157 |
| stroke 3 | 13 % → 13 % | 26.4 px | 0.59 | 1.02 | 156 |
| stroke 4 | 15 % → 11 % | 31.5 px | 0.59 | 0.78 | 165 |
| stroke 5 | 20 % → 14 % | 40.1 px | 0.59 | 0.71 | 168 |
| stroke 6 | 13 % → 7 % | 24.2 px | 0.59 | 0.52 | 153 |

## Brush Artist · Refs · #09 Henry Ward white loops — own sheet
own sheet 600 × 600 · Gouache · 46 px · 8.6 s

![Brush Artist · Refs · #09 Henry Ward white loops — own sheet](Brush-Artist-Refs-09-Henry-Ward-white-loops-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 23 % → 4 % | 12.2 px | 0.07 | 0.17 | 970 |
| stroke 2 | 26 % → 4 % | 26.2 px | 0.07 | 0.14 | 1207 |
| stroke 3 | 34 % → 4 % | 31.4 px | 0.07 | 0.12 | 1290 |
| stroke 4 | 3 % → 1 % | 6.1 px | 0.06 | 0.22 | 154 |
| stroke 5 | 4 % → 2 % | 12.1 px | 0.08 | 0.38 | 160 |
| stroke 6 | 7 % → 4 % | 18.2 px | 0.07 | 0.65 | 158 |
| stroke 7 | 14 % → 4 % | 36.3 px | 0.07 | 0.31 | 159 |
| stroke 8 | 2 % → 0 % | 3.0 px | 0.05 | 0.06 | 154 |

## Brush Artist · Refs · #10 Henry Ward maroon loops — own sheet
own sheet 600 × 600 · Heavy acrylic · 30 px · 3.5 s

![Brush Artist · Refs · #10 Henry Ward maroon loops — own sheet](Brush-Artist-Refs-10-Henry-Ward-maroon-loops-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 12 % → 28 % | 28.7 px | 0.72 | 2.39 | 209 |
| stroke 2 | 22 % → 40 % | 48.5 px | 0.72 | 1.87 | 120 |
| stroke 3 | 29 % → 37 % | 58.5 px | 0.72 | 1.27 | 155 |
| stroke 4 | 41 % → 40 % | 92.8 px | 0.72 | 0.96 | 104 |
| stroke 5 | 34 % → 32 % | 85.9 px | 0.72 | 0.93 | 143 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #11 Henry Ward purple spun balls — own sheet
own sheet 600 × 600 · Heavy acrylic · 36 px · 2.6 s

![Brush Artist · Refs · #11 Henry Ward purple spun balls — own sheet](Brush-Artist-Refs-11-Henry-Ward-purple-spun-balls-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 24 % → 35 % | 26.5 px | 0.68 | 1.43 | 226 |
| stroke 2 | 35 % → 46 % | 38.2 px | 0.68 | 1.33 | 222 |
| stroke 3 | 36 % → 34 % | 39.2 px | 0.68 | 0.97 | 219 |

## Brush Artist · Refs · #12 Henry Ward black-olive cage — own sheet
own sheet 600 × 600 · Gouache · 28 px · 4.9 s

![Brush Artist · Refs · #12 Henry Ward black-olive cage — own sheet](Brush-Artist-Refs-12-Henry-Ward-black-olive-cage-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 7 % → 12 % | 13.4 px | 0.60 | 1.68 | 200 |
| stroke 2 | 7 % → 12 % | 16.3 px | 0.60 | 1.80 | 172 |
| stroke 3 | 15 % → 16 % | 24.2 px | 0.60 | 1.03 | 230 |
| stroke 4 | 16 % → 15 % | 32.2 px | 0.60 | 0.92 | 124 |
| stroke 5 | 16 % → 11 % | 29.0 px | 0.60 | 0.68 | 132 |
| stroke 6 | 25 % → 16 % | 48.3 px | 0.60 | 0.65 | 163 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #13 Henry Ward blue streaky form — own sheet
own sheet 600 × 600 · Gouache · 50 px · 14.4 s

![Brush Artist · Refs · #13 Henry Ward blue streaky form — own sheet](Brush-Artist-Refs-13-Henry-Ward-blue-streaky-form-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 14 % → 8 % | 42.7 px | 0.04 | 0.56 | 210 |
| stroke 2 | 20 % → 7 % | 61.3 px | 0.04 | 0.36 | 209 |
| stroke 3 | 31 % → 8 % | 88.7 px | 0.04 | 0.25 | 211 |
| stroke 4 | 31 % → 7 % | 99.6 px | 0.04 | 0.23 | 199 |
| stroke 5 | 45 % → 8 % | 130.2 px | 0.04 | 0.18 | 226 |
| stroke 6 | 45 % → 9 % | 129.6 px | 0.04 | 0.20 | 224 |
| stroke 7 | 46 % → 10 % | 136.7 px | 0.04 | 0.22 | 215 |
| stroke 8 | 47 % → 8 % | 143.3 px | 0.03 | 0.18 | 213 |
| stroke 9 | 46 % → 7 % | 142.0 px | 0.03 | 0.16 | 203 |
| stroke 10 | 46 % → 7 % | 152.6 px | 0.03 | 0.16 | 199 |
| stroke 11 | 44 % → 5 % | 136.4 px | 0.03 | 0.11 | 211 |
| stroke 12 | 45 % → 6 % | 135.8 px | 0.03 | 0.14 | 219 |
| stroke 13 | 45 % → 7 % | 138.8 px | 0.04 | 0.17 | 198 |
| stroke 14 | 43 % → 7 % | 129.4 px | 0.04 | 0.16 | 222 |
| stroke 15 | 44 % → 7 % | 125.8 px | 0.04 | 0.17 | 216 |
| stroke 16 | 46 % → 7 % | 137.2 px | 0.04 | 0.16 | 244 |
| stroke 17 | 55 % → 4 % | 137.1 px | 0.04 | 0.08 | 276 |
| stroke 18 | 58 % → 4 % | 140.1 px | 0.04 | 0.08 | 291 |
| stroke 19 | 64 % → 5 % | 130.9 px | 0.04 | 0.08 | 287 |
| stroke 20 | 72 % → 5 % | 137.6 px | 0.04 | 0.08 | 278 |
| stroke 21 | 1 % → 0 % | 2.9 px | 0.04 | 0.02 | 133 |
| stroke 22 | 12 % → 7 % | 34.1 px | 0.04 | 0.61 | 180 |
| stroke 23 | 23 % → 8 % | 70.4 px | 0.04 | 0.35 | 262 |
| stroke 24 | 14 % → 5 % | 38.0 px | 0.03 | 0.35 | 343 |
| stroke 25 | 18 % → 6 % | 46.1 px | 0.04 | 0.31 | 366 |

## Brush Artist · Refs · #14 Henry Ward olive totem — own sheet
own sheet 600 × 600 · Heavy acrylic · 48 px · 6.9 s

![Brush Artist · Refs · #14 Henry Ward olive totem — own sheet](Brush-Artist-Refs-14-Henry-Ward-olive-totem-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 18 % → 46 % | 46.9 px | 0.38 | 2.58 | 137 |
| stroke 2 | 21 % → 50 % | 64.4 px | 0.38 | 2.44 | 119 |
| stroke 3 | 29 % → 52 % | 100.6 px | 0.38 | 1.78 | 124 |
| stroke 4 | 30 % → 55 % | 113.7 px | 0.38 | 1.80 | 125 |
| stroke 5 | 39 % → 63 % | 135.6 px | 0.38 | 1.63 | 113 |
| stroke 6 | 39 % → 65 % | 150.4 px | 0.38 | 1.68 | 120 |
| stroke 7 | 37 % → 61 % | 124.3 px | 0.38 | 1.66 | 123 |
| stroke 8 | 37 % → 63 % | 142.4 px | 0.38 | 1.69 | 129 |
| stroke 9 | 38 % → 63 % | 130.9 px | 0.38 | 1.67 | 130 |
| stroke 10 | 38 % → 62 % | 141.0 px | 0.38 | 1.62 | 123 |
| stroke 11 | 40 % → 65 % | 143.8 px | 0.38 | 1.61 | 117 |
| stroke 12 | 38 % → 65 % | 144.2 px | 0.38 | 1.70 | 120 |
| stroke 13 | 39 % → 66 % | 135.5 px | 0.38 | 1.72 | 111 |
| stroke 14 | 37 % → 62 % | 134.5 px | 0.38 | 1.68 | 137 |
| stroke 15 | 40 % → 66 % | 136.9 px | 0.38 | 1.65 | 117 |
| stroke 16 | 38 % → 64 % | 138.8 px | 0.38 | 1.66 | 126 |
| stroke 17 | 38 % → 62 % | 126.2 px | 0.38 | 1.65 | 129 |
| stroke 18 | 40 % → 66 % | 154.9 px | 0.38 | 1.64 | 120 |
| stroke 19 | 40 % → 60 % | 137.9 px | 0.38 | 1.52 | 124 |
| stroke 20 | 41 % → 55 % | 144.4 px | 0.38 | 1.34 | 130 |
| stroke 21 | 46 % → 55 % | 137.7 px | 0.38 | 1.18 | 122 |
| stroke 22 | 54 % → 53 % | 146.7 px | 0.38 | 0.99 | 123 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #15 Ultramarine brush script — own sheet
own sheet 600 × 600 · Ink · 4 px · 10.0 s

![Brush Artist · Refs · #15 Ultramarine brush script — own sheet](Brush-Artist-Refs-15-Ultramarine-brush-script-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 40 % → 42 % | 8.9 px | 0.66 | 1.05 | 50 |
| stroke 2 | 40 % → 42 % | 8.9 px | 0.66 | 1.06 | 50 |
| stroke 3 | 40 % → 42 % | 9.5 px | 0.74 | 1.06 | 29 |
| stroke 4 | 42 % → 45 % | 10.1 px | 0.74 | 1.08 | 16 |
| stroke 5 | 44 % → 48 % | 9.7 px | 0.73 | 1.08 | 26 |
| stroke 6 | 42 % → 44 % | 9.5 px | 0.65 | 1.05 | 52 |
| stroke 7 | 43 % → 47 % | 9.2 px | 0.72 | 1.08 | 32 |
| stroke 8 | 38 % → 41 % | 9.3 px | 0.68 | 1.05 | 45 |
| stroke 9 | 40 % → 42 % | 9.2 px | 0.69 | 1.06 | 41 |
| stroke 10 | 36 % → 38 % | 9.9 px | 0.68 | 1.05 | 43 |
| stroke 11 | 42 % → 45 % | 9.6 px | 0.70 | 1.06 | 38 |
| stroke 12 | 39 % → 41 % | 9.4 px | 0.66 | 1.05 | 47 |
| stroke 13 | 45 % → 48 % | 10.2 px | 0.71 | 1.06 | 29 |
| stroke 14 | 38 % → 41 % | 9.9 px | 0.73 | 1.07 | 24 |
| stroke 15 | 37 % → 39 % | 9.1 px | 0.69 | 1.06 | 41 |
| stroke 16 | 42 % → 45 % | 9.4 px | 0.72 | 1.06 | 28 |
| stroke 17 | 41 % → 44 % | 7.1 px | 0.71 | 1.08 | 43 |
| stroke 18 | 43 % → 45 % | 9.2 px | 0.73 | 1.06 | 26 |
| stroke 19 | 39 % → 41 % | 8.9 px | 0.66 | 1.05 | 54 |
| stroke 20 | 41 % → 43 % | 9.4 px | 0.71 | 1.06 | 32 |
| stroke 21 | 40 % → 43 % | 9.9 px | 0.70 | 1.06 | 34 |
| stroke 22 | 42 % → 44 % | 8.5 px | 0.65 | 1.05 | 58 |
| stroke 23 | 40 % → 43 % | 10.1 px | 0.73 | 1.07 | 34 |
| stroke 24 | 38 % → 41 % | 8.8 px | 0.73 | 1.07 | 38 |
| stroke 25 | 41 % → 43 % | 9.8 px | 0.72 | 1.07 | 45 |
| stroke 26 | 46 % → 49 % | 9.3 px | 0.68 | 1.05 | 56 |
| stroke 27 | 43 % → 45 % | 8.8 px | 0.63 | 1.05 | 72 |
| stroke 28 | 44 % → 46 % | 9.1 px | 0.70 | 1.06 | 53 |
| stroke 29 | 36 % → 39 % | 10.6 px | 0.72 | 1.08 | 29 |
| stroke 30 | 39 % → 41 % | 8.7 px | 0.71 | 1.04 | 55 |
| stroke 31 | 43 % → 46 % | 10.3 px | 0.75 | 1.07 | 29 |
| stroke 32 | 42 % → 46 % | 9.5 px | 0.73 | 1.09 | 31 |
| stroke 33 | 35 % → 38 % | 10.9 px | 0.72 | 1.08 | 28 |
| stroke 34 | 40 % → 43 % | 9.8 px | 0.73 | 1.08 | 27 |
| stroke 35 | 36 % → 37 % | 9.4 px | 0.65 | 1.05 | 65 |

## Brush Artist · Refs · #18 Blue oil-stick scribbles — own sheet
own sheet 600 × 600 · Pastel · 10 px · 4.3 s

![Brush Artist · Refs · #18 Blue oil-stick scribbles — own sheet](Brush-Artist-Refs-18-Blue-oil-stick-scribbles-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 15 % → 31 % | 3.8 px | 0.49 | 2.11 | 166 |
| stroke 2 | 13 % → 37 % | 3.6 px | 0.49 | 2.73 | 164 |
| stroke 3 | 16 % → 26 % | 5.8 px | 0.49 | 1.66 | 173 |
| stroke 4 | 15 % → 29 % | 8.0 px | 0.49 | 1.88 | 177 |
| stroke 5 | 29 % → 34 % | 8.4 px | 0.49 | 1.19 | 149 |
| stroke 6 | 25 % → 26 % | 9.4 px | 0.49 | 1.02 | 211 |
| stroke 7 | 26 % → 32 % | 8.3 px | 0.49 | 1.24 | 254 |
| stroke 8 | 30 % → 30 % | 17.0 px | 0.49 | 1.00 | 281 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #20 Orange-red crayon scribble — own sheet
own sheet 600 × 600 · Pastel · 14 px · 2.8 s

![Brush Artist · Refs · #20 Orange-red crayon scribble — own sheet](Brush-Artist-Refs-20-Orange-red-crayon-scribble-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 8 % → 18 % | 5.5 px | 0.59 | 2.46 | 191 |
| stroke 2 | 9 % → 23 % | 6.8 px | 0.59 | 2.48 | 180 |
| stroke 3 | 13 % → 21 % | 8.5 px | 0.59 | 1.64 | 154 |
| stroke 4 | 24 % → 32 % | 8.9 px | 0.59 | 1.34 | 177 |
| stroke 5 | 27 % → 27 % | 7.7 px | 0.59 | 1.00 | 177 |
| stroke 6 | 22 % → 22 % | 16.8 px | 0.59 | 1.00 | 190 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #21 Gritty black contours — own sheet
own sheet 600 × 600 · Gouache · 12 px · 4.7 s

![Brush Artist · Refs · #21 Gritty black contours — own sheet](Brush-Artist-Refs-21-Gritty-black-contours-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 4 % → 5 % | 4.7 px | 0.37 | 1.13 | 151 |
| stroke 2 | 4 % → 3 % | 7.3 px | 0.37 | 0.60 | 191 |
| stroke 3 | 7 % → 4 % | 6.2 px | 0.37 | 0.56 | 113 |
| stroke 4 | 9 % → 4 % | 10.7 px | 0.37 | 0.51 | 134 |
| stroke 5 | 10 % → 4 % | 12.7 px | 0.37 | 0.42 | 91 |

## Brush Artist · Refs · #22 Bold black brush poster — own sheet
own sheet 600 × 600 · Ink · 20 px · 6.3 s

![Brush Artist · Refs · #22 Bold black brush poster — own sheet](Brush-Artist-Refs-22-Bold-black-brush-poster-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 22 % → 27 % | 36.4 px | 0.94 | 1.20 | 103 |
| stroke 2 | 27 % → 37 % | 41.5 px | 0.95 | 1.36 | 24 |
| stroke 3 | 28 % → 28 % | 43.6 px | 0.95 | 1.00 | 43 |
| stroke 4 | 27 % → 39 % | 53.8 px | 0.94 | 1.42 | 62 |
| stroke 5 | 25 % → 25 % | 43.0 px | 0.94 | 1.00 | 81 |

## Brush Artist · Refs · #23 Dry white on orange + black line — own sheet
own sheet 600 × 600 · Gouache · 50 px · 9.9 s

![Brush Artist · Refs · #23 Dry white on orange + black line — own sheet](Brush-Artist-Refs-23-Dry-white-on-orange-black-line-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 5 % → 10 % | 18.7 px | 0.42 | 1.89 | 145 |
| stroke 2 | 7 % → 9 % | 24.3 px | 0.42 | 1.35 | 165 |
| stroke 3 | 10 % → 10 % | 39.0 px | 0.42 | 0.92 | 156 |
| stroke 4 | 12 % → 11 % | 45.8 px | 0.42 | 0.95 | 155 |
| stroke 5 | 17 % → 14 % | 60.0 px | 0.42 | 0.82 | 191 |
| stroke 6 | 17 % → 15 % | 70.6 px | 0.42 | 0.86 | 190 |
| stroke 7 | 14 % → 14 % | 52.6 px | 0.41 | 1.00 | 157 |
| stroke 8 | 14 % → 13 % | 55.2 px | 0.41 | 0.91 | 185 |
| stroke 9 | 15 % → 14 % | 54.3 px | 0.41 | 0.93 | 165 |
| stroke 10 | 14 % → 14 % | 56.6 px | 0.41 | 0.97 | 185 |
| stroke 11 | 16 % → 15 % | 60.6 px | 0.41 | 0.92 | 265 |
| stroke 12 | 16 % → 15 % | 63.4 px | 0.41 | 0.94 | 315 |
| stroke 13 | 17 % → 16 % | 61.2 px | 0.41 | 0.97 | 211 |
| stroke 14 | 16 % → 16 % | 63.9 px | 0.41 | 0.97 | 284 |
| stroke 15 | 16 % → 14 % | 59.9 px | 0.41 | 0.87 | 246 |
| stroke 16 | 15 % → 12 % | 61.4 px | 0.41 | 0.78 | 214 |
| stroke 17 | 16 % → 11 % | 56.7 px | 0.41 | 0.68 | 184 |
| stroke 18 | 19 % → 11 % | 69.3 px | 0.41 | 0.60 | 132 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #24 Picasso flat oil — own sheet
own sheet 600 × 600 · Oil · 34 px · 6.4 s

![Brush Artist · Refs · #24 Picasso flat oil — own sheet](Brush-Artist-Refs-24-Picasso-flat-oil-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 16 % → 45 % | 34.7 px | 0.23 | 2.74 | 193 |
| stroke 2 | 20 % → 48 % | 47.2 px | 0.24 | 2.40 | 228 |
| stroke 3 | 29 % → 59 % | 62.5 px | 0.23 | 2.07 | 223 |
| stroke 4 | 37 % → 65 % | 83.2 px | 0.23 | 1.76 | 317 |
| stroke 5 | 43 % → 71 % | 94.5 px | 0.23 | 1.65 | 185 |
| stroke 6 | 44 % → 66 % | 102.1 px | 0.23 | 1.50 | 198 |
| stroke 7 | 45 % → 66 % | 94.8 px | 0.23 | 1.46 | 212 |
| stroke 8 | 44 % → 66 % | 107.0 px | 0.23 | 1.50 | 147 |
| stroke 9 | 37 % → 62 % | 81.5 px | 0.23 | 1.67 | 133 |
| stroke 10 | 39 % → 62 % | 93.1 px | 0.23 | 1.58 | 133 |
| stroke 11 | 37 % → 60 % | 78.6 px | 0.23 | 1.62 | 145 |
| stroke 12 | 38 % → 61 % | 91.1 px | 0.23 | 1.60 | 131 |
| stroke 13 | 38 % → 68 % | 84.4 px | 0.23 | 1.76 | 141 |
| stroke 14 | 39 % → 69 % | 88.9 px | 0.23 | 1.75 | 144 |
| stroke 15 | 39 % → 62 % | 83.3 px | 0.23 | 1.58 | 135 |
| stroke 16 | 38 % → 55 % | 88.0 px | 0.23 | 1.43 | 157 |
| stroke 17 | 43 % → 48 % | 90.0 px | 0.23 | 1.12 | 146 |
| stroke 18 | 42 % → 42 % | 102.7 px | 0.23 | 1.00 | 156 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #25 Yellow heavy flat stroke — own sheet
own sheet 600 × 600 · Heavy acrylic · 110 px · 3.3 s

![Brush Artist · Refs · #25 Yellow heavy flat stroke — own sheet](Brush-Artist-Refs-25-Yellow-heavy-flat-stroke-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 18 % → 18 % | 104.2 px | 0.17 | 0.98 | 654 |

## Brush Artist · Refs · #27 Orange impasto swatch — own sheet
own sheet 600 × 600 · Heavy acrylic · 60 px · 3.7 s

![Brush Artist · Refs · #27 Orange impasto swatch — own sheet](Brush-Artist-Refs-27-Orange-impasto-swatch-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 8 % → 21 % | 61.8 px | 0.33 | 2.60 | 75 |
| stroke 2 | 7 % → 33 % | 62.5 px | 0.33 | 4.67 | 57 |
| stroke 3 | 25 % → 36 % | 245.5 px | 0.33 | 1.40 | 43 |
| stroke 4 | 10 % → 12 % | 69.6 px | 0.33 | 1.25 | 73 |
| stroke 5 | 17 % → 33 % | 63.5 px | 0.33 | 1.90 | 103 |
| stroke 6 | 18 % → 31 % | 145.1 px | 0.33 | 1.79 | 70 |
| stroke 7 | 8 % → 15 % | 70.2 px | 0.33 | 1.86 | 54 |
| stroke 8 | 33 % → 34 % | 337.1 px | 0.33 | 1.04 | 62 |
| stroke 9 | 38 % → 37 % | 185.4 px | 0.33 | 0.98 | 83 |
| stroke 10 | 33 % → 33 % | 304.7 px | 0.33 | 0.98 | 70 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #28 Miles Davis black lines — own sheet
own sheet 600 × 600 · Ink · 22 px · 7.3 s

![Brush Artist · Refs · #28 Miles Davis black lines — own sheet](Brush-Artist-Refs-28-Miles-Davis-black-lines-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 22 % → 32 % | 36.6 px | 0.88 | 1.42 | 212 |
| stroke 2 | 28 % → 49 % | 38.3 px | 0.88 | 1.73 | 198 |
| stroke 3 | 39 % → 44 % | 75.1 px | 0.88 | 1.12 | 133 |
| stroke 4 | 42 % → 48 % | 83.7 px | 0.88 | 1.15 | 224 |
| stroke 5 | 55 % → 55 % | 109.9 px | 0.88 | 1.00 | 153 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #29 Shrigley magenta asterisk — own sheet
own sheet 600 × 600 · Watercolor · 70 px · 7.4 s

![Brush Artist · Refs · #29 Shrigley magenta asterisk — own sheet](Brush-Artist-Refs-29-Shrigley-magenta-asterisk-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 13 % → 37 % | 46.6 px | 0.72 | 2.85 | 196 |
| stroke 2 | 12 % → 12 % | 87.1 px | 0.71 | 1.00 | 279 |
| stroke 3 | 28 % → 37 % | 100.9 px | 0.72 | 1.31 | 239 |
| stroke 4 | 23 % → 23 % | 163.9 px | 0.71 | 1.02 | 211 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #30 Red gouache face patch — own sheet
own sheet 600 × 600 · Gouache · 60 px · 14.7 s

![Brush Artist · Refs · #30 Red gouache face patch — own sheet](Brush-Artist-Refs-30-Red-gouache-face-patch-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 12 % → 37 % | 51.5 px | 0.53 | 3.22 | 173 |
| stroke 2 | 15 % → 40 % | 74.6 px | 0.53 | 2.72 | 163 |
| stroke 3 | 24 % → 50 % | 116.0 px | 0.53 | 2.06 | 154 |
| stroke 4 | 27 % → 51 % | 134.1 px | 0.53 | 1.93 | 163 |
| stroke 5 | 34 % → 60 % | 159.9 px | 0.53 | 1.77 | 164 |
| stroke 6 | 35 % → 61 % | 178.3 px | 0.53 | 1.76 | 168 |
| stroke 7 | 34 % → 59 % | 160.9 px | 0.54 | 1.73 | 163 |
| stroke 8 | 34 % → 56 % | 162.5 px | 0.53 | 1.65 | 193 |
| stroke 9 | 36 % → 60 % | 173.1 px | 0.53 | 1.66 | 285 |
| stroke 10 | 38 % → 62 % | 196.8 px | 0.53 | 1.63 | 266 |
| stroke 11 | 37 % → 61 % | 182.5 px | 0.53 | 1.66 | 281 |
| stroke 12 | 36 % → 58 % | 178.3 px | 0.53 | 1.62 | 349 |
| stroke 13 | 33 % → 46 % | 156.5 px | 0.53 | 1.39 | 291 |
| stroke 14 | 33 % → 41 % | 157.7 px | 0.53 | 1.25 | 250 |
| stroke 15 | 33 % → 37 % | 153.4 px | 0.53 | 1.12 | 214 |
| stroke 16 | 39 % → 39 % | 184.9 px | 0.53 | 0.99 | 166 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #31 Warhol blotted line — own sheet
own sheet 600 × 600 · Ink · 6 px · 6.4 s

![Brush Artist · Refs · #31 Warhol blotted line — own sheet](Brush-Artist-Refs-31-Warhol-blotted-line-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 21 % → 42 % | 15.8 px | 0.82 | 1.98 | 132 |
| stroke 2 | 17 % → 23 % | 15.9 px | 0.82 | 1.34 | 142 |
| stroke 3 | 24 % → 25 % | 25.1 px | 0.81 | 1.02 | 115 |
| stroke 4 | 31 % → 40 % | 31.9 px | 0.82 | 1.28 | 70 |
| stroke 5 | 35 % → 44 % | 36.4 px | 0.82 | 1.23 | 104 |
| stroke 6 | 32 % → 33 % | 26.7 px | 0.81 | 1.03 | 109 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #32 Thick orange swipes — own sheet
own sheet 600 × 600 · Heavy acrylic · 90 px · 4.9 s

![Brush Artist · Refs · #32 Thick orange swipes — own sheet](Brush-Artist-Refs-32-Thick-orange-swipes-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 14 % → 27 % | 86.0 px | 0.03 | 1.90 | 602 |
| stroke 2 | 26 % → 38 % | 176.9 px | 0.03 | 1.43 | 390 |
| stroke 3 | 28 % → 27 % | 177.5 px | 0.03 | 0.98 | 360 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #33 Red wet-in-wet band — own sheet
own sheet 600 × 600 · Watercolor · 80 px · 11.4 s

![Brush Artist · Refs · #33 Red wet-in-wet band — own sheet](Brush-Artist-Refs-33-Red-wet-in-wet-band-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 23 % → 56 % | 88.2 px | 0.61 | 2.43 | 533 |
| stroke 2 | 30 % → 51 % | 243.6 px | 0.62 | 1.71 | 138 |
| stroke 3 | 37 % → 54 % | 356.4 px | 0.61 | 1.46 | 107 |
| stroke 4 | 42 % → 60 % | 412.0 px | 0.63 | 1.42 | 138 |
| stroke 5 | 42 % → 55 % | 354.0 px | 0.62 | 1.32 | 107 |
| stroke 6 | 42 % → 47 % | 321.5 px | 0.61 | 1.10 | 169 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #34 Magenta oil patches — own sheet
own sheet 600 × 600 · Oil · 60 px · 5.9 s

![Brush Artist · Refs · #34 Magenta oil patches — own sheet](Brush-Artist-Refs-34-Magenta-oil-patches-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 9 % → 42 % | 62.0 px | 0.13 | 4.82 | 125 |
| stroke 2 | 9 % → 29 % | 62.8 px | 0.13 | 3.15 | 128 |
| stroke 3 | 7 % → 35 % | 62.3 px | 0.13 | 4.72 | 93 |
| stroke 4 | 16 % → 20 % | 132.0 px | 0.12 | 1.27 | 72 |
| stroke 5 | 23 % → 33 % | 124.6 px | 0.13 | 1.43 | 114 |
| stroke 6 | 20 % → 38 % | 171.5 px | 0.13 | 1.90 | 68 |
| stroke 7 | 30 % → 35 % | 237.9 px | 0.13 | 1.18 | 113 |
| stroke 8 | 33 % → 39 % | 235.1 px | 0.13 | 1.18 | 109 |
| stroke 9 | 25 % → 26 % | 159.7 px | 0.13 | 1.07 | 93 |
| stroke 10 | 29 % → 29 % | 257.3 px | 0.13 | 1.00 | 93 |
| stroke 11 | 36 % → 36 % | 324.7 px | 0.13 | 1.00 | 90 |
| stroke 12 | 26 % → 26 % | 184.5 px | 0.13 | 1.00 | 96 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #35 Red band with runs — own sheet
own sheet 600 × 600 · Watercolor · 70 px · 6.9 s

![Brush Artist · Refs · #35 Red band with runs — own sheet](Brush-Artist-Refs-35-Red-band-with-runs-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 21 % → 33 % | 77.5 px | 0.50 | 1.59 | 501 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #36 Magenta letters flat brush — own sheet
own sheet 600 × 600 · Gouache · 36 px · 11.6 s

![Brush Artist · Refs · #36 Magenta letters flat brush — own sheet](Brush-Artist-Refs-36-Magenta-letters-flat-brush-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 20 % → 39 % | 59.1 px | 0.50 | 1.95 | 44 |
| stroke 2 | 20 % → 32 % | 46.7 px | 0.50 | 1.59 | 55 |
| stroke 3 | 29 % → 54 % | 86.9 px | 0.50 | 1.86 | 38 |
| stroke 4 | 26 % → 44 % | 51.3 px | 0.50 | 1.67 | 152 |
| stroke 5 | 33 % → 55 % | 96.2 px | 0.50 | 1.67 | 93 |
| stroke 6 | 42 % → 56 % | 242.7 px | 0.50 | 1.33 | 22 |
| stroke 7 | 30 % → 44 % | 56.8 px | 0.50 | 1.45 | 116 |
| stroke 8 | 31 % → 53 % | 98.5 px | 0.50 | 1.68 | 71 |
| stroke 9 | 38 % → 51 % | 158.3 px | 0.50 | 1.33 | 31 |
| stroke 10 | 37 % → 64 % | 106.7 px | 0.50 | 1.72 | 80 |
| stroke 11 | 39 % → 62 % | 225.8 px | 0.50 | 1.58 | 16 |
| stroke 12 | 43 % → 56 % | 81.9 px | 0.50 | 1.29 | 110 |
| stroke 13 | 33 % → 46 % | 117.7 px | 0.50 | 1.43 | 35 |
| stroke 14 | 35 % → 52 % | 134.5 px | 0.50 | 1.47 | 30 |
| stroke 15 | 38 % → 56 % | 108.6 px | 0.50 | 1.49 | 72 |
| stroke 16 | 41 % → 50 % | 232.0 px | 0.50 | 1.23 | 15 |
| stroke 17 | 44 % → 52 % | 81.7 px | 0.50 | 1.19 | 117 |
| stroke 18 | 27 % → 36 % | 97.6 px | 0.50 | 1.35 | 64 |
| stroke 19 | 40 % → 39 % | 117.2 px | 0.50 | 0.96 | 51 |
| stroke 20 | 45 % → 45 % | 132.3 px | 0.50 | 0.99 | 41 |
| stroke 21 | 41 % → 39 % | 78.7 px | 0.50 | 0.96 | 117 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #37 Oil still life dabs — own sheet
own sheet 600 × 600 · Oil · 40 px · 3.7 s

![Brush Artist · Refs · #37 Oil still life dabs — own sheet](Brush-Artist-Refs-37-Oil-still-life-dabs-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 7 % → 7 % | 44.1 px | 0.39 | 1.00 | 38 |
| stroke 2 | 6 % → 27 % | 44.4 px | 0.39 | 4.43 | 30 |
| stroke 3 | 12 % → 36 % | 92.6 px | 0.39 | 3.01 | 29 |
| stroke 4 | 9 % → 9 % | 42.8 px | 0.39 | 1.00 | 56 |
| stroke 5 | 6 % → 10 % | 43.2 px | 0.39 | 1.71 | 35 |
| stroke 6 | 13 % → 31 % | 83.4 px | 0.39 | 2.32 | 36 |
| stroke 7 | 11 % → 24 % | 115.5 px | 0.39 | 2.18 | 17 |
| stroke 8 | 8 % → 14 % | 89.7 px | 0.39 | 1.63 | 14 |
| stroke 9 | 13 % → 14 % | 68.1 px | 0.38 | 1.09 | 57 |
| stroke 10 | 21 % → 25 % | 106.5 px | 0.39 | 1.20 | 45 |
| stroke 11 | 24 % → 28 % | 201.7 px | 0.39 | 1.17 | 30 |
| stroke 12 | 21 % → 21 % | 227.4 px | 0.39 | 1.01 | 14 |
| stroke 13 | 16 % → 16 % | 167.7 px | 0.40 | 1.00 | 23 |
| stroke 14 | 16 % → 16 % | 132.7 px | 0.39 | 1.00 | 20 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #38 Sanguine drawing — own sheet
own sheet 600 × 600 · Pastel · 6 px · 2.2 s

![Brush Artist · Refs · #38 Sanguine drawing — own sheet](Brush-Artist-Refs-38-Sanguine-drawing-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 3 % → 14 % | 2.9 px | 0.57 | 5.29 | 9 |
| stroke 2 | 3 % → 7 % | 2.9 px | 0.57 | 2.89 | 7 |
| stroke 3 | 3 % → 9 % | 2.9 px | 0.57 | 3.40 | 7 |
| stroke 4 | 2 % → 17 % | 2.7 px | 0.57 | 7.20 | 7 |
| stroke 5 | 2 % → 7 % | 2.7 px | 0.57 | 3.03 | 7 |
| stroke 6 | 3 % → 19 % | 3.4 px | 0.57 | 6.31 | 7 |
| stroke 7 | 5 % → 14 % | 5.2 px | 0.57 | 3.07 | 7 |
| stroke 8 | 4 % → 16 % | 4.7 px | 0.57 | 3.79 | 6 |
| stroke 9 | 3 % → 7 % | 2.9 px | 0.57 | 2.66 | 6 |
| stroke 10 | 4 % → 16 % | 4.7 px | 0.57 | 3.83 | 7 |
| stroke 11 | 3 % → 4 % | 2.9 px | 0.57 | 1.61 | 7 |
| stroke 12 | 4 % → 15 % | 4.8 px | 0.57 | 3.58 | 12 |
| stroke 13 | 8 % → 17 % | 8.9 px | 0.57 | 2.23 | 11 |
| stroke 14 | 4 % → 14 % | 4.9 px | 0.57 | 3.19 | 7 |
| stroke 15 | 9 % → 18 % | 10.7 px | 0.57 | 1.86 | 6 |
| stroke 16 | 6 % → 16 % | 6.6 px | 0.57 | 2.71 | 12 |
| stroke 17 | 4 % → 9 % | 4.4 px | 0.57 | 2.25 | 6 |
| stroke 18 | 3 % → 5 % | 2.9 px | 0.57 | 1.85 | 6 |
| stroke 19 | 6 % → 16 % | 6.9 px | 0.57 | 2.68 | 7 |
| stroke 20 | 8 % → 14 % | 9.2 px | 0.57 | 1.70 | 6 |
| stroke 21 | 4 % → 4 % | 4.3 px | 0.57 | 1.00 | 6 |
| stroke 22 | 8 % → 13 % | 8.6 px | 0.57 | 1.79 | 6 |
| stroke 23 | 7 % → 12 % | 8.3 px | 0.57 | 1.61 | 6 |
| stroke 24 | 4 % → 7 % | 4.7 px | 0.57 | 1.71 | 6 |
| stroke 25 | 8 % → 14 % | 8.7 px | 0.57 | 1.84 | 6 |
| stroke 26 | 6 % → 8 % | 6.5 px | 0.57 | 1.34 | 8 |
| stroke 27 | 4 % → 4 % | 4.3 px | 0.57 | 1.10 | 6 |
| stroke 28 | 7 % → 11 % | 8.2 px | 0.57 | 1.59 | 7 |
| stroke 29 | 8 % → 17 % | 8.8 px | 0.57 | 2.21 | 7 |
| stroke 30 | 13 % → 17 % | 14.9 px | 0.57 | 1.29 | 6 |
| stroke 31 | 5 % → 6 % | 5.4 px | 0.57 | 1.29 | 6 |
| stroke 32 | 10 % → 13 % | 11.8 px | 0.57 | 1.24 | 12 |
| stroke 33 | 7 % → 8 % | 8.5 px | 0.57 | 1.07 | 6 |
| stroke 34 | 11 % → 14 % | 12.0 px | 0.57 | 1.36 | 9 |
| stroke 35 | 9 % → 14 % | 10.0 px | 0.57 | 1.61 | 9 |
| stroke 36 | 10 % → 13 % | 11.4 px | 0.57 | 1.26 | 6 |
| stroke 37 | 9 % → 16 % | 10.5 px | 0.57 | 1.71 | 9 |
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
own sheet 600 × 600 · Heavy acrylic · 60 px · 4.7 s

![Brush Artist · Refs · #39 Very thick impasto — own sheet](Brush-Artist-Refs-39-Very-thick-impasto-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 26 % → 37 % | 59.6 px | 0.43 | 1.42 | 277 |
| stroke 2 | 31 % → 48 % | 93.9 px | 0.44 | 1.54 | 321 |
| stroke 3 | 37 % → 49 % | 124.6 px | 0.43 | 1.33 | 252 |
| stroke 4 | 31 % → 44 % | 90.9 px | 0.44 | 1.41 | 272 |
| stroke 5 | 42 % → 41 % | 104.2 px | 0.44 | 0.98 | 271 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #40 Watercolour blooms — own sheet
own sheet 600 × 600 · Watercolor · 90 px · 6.6 s

![Brush Artist · Refs · #40 Watercolour blooms — own sheet](Brush-Artist-Refs-40-Watercolour-blooms-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 21 % → 25 % | 92.4 px | 0.13 | 1.20 | 694 |

## Brush Artist · Refs · #41 Coloured pencil hatching — own sheet
own sheet 600 × 600 · Pastel · 4 px · 2.7 s

![Brush Artist · Refs · #41 Coloured pencil hatching — own sheet](Brush-Artist-Refs-41-Coloured-pencil-hatching-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 3 % → 13 % | 2.2 px | 0.35 | 4.64 | 10 |
| stroke 2 | 3 % → 7 % | 2.3 px | 0.35 | 2.29 | 7 |
| stroke 3 | 2 % → 11 % | 1.9 px | 0.35 | 4.38 | 7 |
| stroke 4 | 3 % → 19 % | 2.1 px | 0.35 | 6.73 | 7 |
| stroke 5 | 4 % → 7 % | 2.9 px | 0.35 | 1.83 | 5 |
| stroke 6 | 3 % → 13 % | 2.3 px | 0.35 | 4.19 | 7 |
| stroke 7 | 3 % → 15 % | 2.6 px | 0.35 | 4.43 | 6 |
| stroke 8 | 3 % → 12 % | 2.1 px | 0.35 | 4.20 | 5 |
| stroke 9 | 5 % → 11 % | 3.6 px | 0.35 | 2.27 | 6 |
| stroke 10 | 5 % → 15 % | 3.8 px | 0.35 | 2.99 | 5 |
| stroke 11 | 4 % → 13 % | 3.0 px | 0.35 | 3.28 | 6 |
| stroke 12 | 3 % → 3 % | 2.1 px | 0.35 | 1.00 | 5 |
| stroke 13 | 7 % → 17 % | 5.2 px | 0.35 | 2.45 | 4 |
| stroke 14 | 3 % → 13 % | 2.4 px | 0.35 | 4.19 | 5 |
| stroke 15 | 6 % → 12 % | 4.4 px | 0.35 | 2.09 | 6 |
| stroke 16 | 7 % → 11 % | 5.1 px | 0.35 | 1.61 | 6 |
| stroke 17 | 3 % → 3 % | 2.1 px | 0.35 | 1.00 | 6 |
| stroke 18 | 5 % → 8 % | 3.6 px | 0.35 | 1.65 | 6 |
| stroke 19 | 5 % → 13 % | 3.8 px | 0.35 | 2.72 | 7 |
| stroke 20 | 5 % → 14 % | 3.7 px | 0.35 | 2.92 | 7 |
| stroke 21 | 4 % → 13 % | 3.2 px | 0.35 | 3.20 | 7 |
| stroke 22 | 9 % → 16 % | 6.8 px | 0.35 | 1.77 | 5 |
| stroke 23 | 9 % → 13 % | 6.5 px | 0.35 | 1.55 | 6 |
| stroke 24 | 6 % → 14 % | 4.7 px | 0.35 | 2.18 | 6 |
| stroke 25 | 5 % → 10 % | 3.5 px | 0.35 | 2.27 | 7 |
| stroke 26 | 3 % → 6 % | 2.7 px | 0.35 | 1.81 | 6 |
| stroke 27 | 3 % → 7 % | 2.3 px | 0.35 | 2.26 | 6 |
| stroke 28 | 6 % → 10 % | 4.5 px | 0.35 | 1.70 | 7 |
| stroke 29 | 3 % → 13 % | 2.4 px | 0.35 | 4.21 | 6 |
| stroke 30 | 6 % → 9 % | 4.4 px | 0.35 | 1.46 | 6 |
| stroke 31 | 7 % → 14 % | 5.1 px | 0.35 | 2.14 | 6 |
| stroke 32 | 3 % → 6 % | 2.5 px | 0.35 | 1.79 | 6 |
| stroke 33 | 6 % → 11 % | 5.0 px | 0.35 | 1.67 | 5 |
| stroke 34 | 3 % → 6 % | 2.6 px | 0.35 | 1.73 | 6 |
| stroke 35 | 7 % → 14 % | 5.0 px | 0.35 | 2.09 | 7 |
| stroke 36 | 5 % → 5 % | 3.7 px | 0.35 | 1.01 | 6 |
| stroke 37 | 7 % → 15 % | 5.2 px | 0.35 | 2.15 | 8 |
| stroke 38 | 8 % → 13 % | 5.8 px | 0.35 | 1.66 | 6 |
| stroke 39 | 7 % → 11 % | 5.1 px | 0.35 | 1.67 | 5 |
| stroke 40 | 8 % → 18 % | 6.2 px | 0.35 | 2.21 | 4 |
| stroke 41 | 9 % → 13 % | 6.9 px | 0.35 | 1.48 | 5 |
| stroke 42 | 10 % → 17 % | 7.7 px | 0.35 | 1.73 | 5 |
| stroke 43 | 5 % → 9 % | 3.9 px | 0.35 | 1.66 | 5 |
| stroke 44 | 10 % → 13 % | 7.3 px | 0.35 | 1.40 | 5 |
| stroke 45 | 13 % → 18 % | 9.9 px | 0.35 | 1.35 | 5 |
| stroke 46 | 5 % → 7 % | 3.6 px | 0.34 | 1.41 | 6 |
| stroke 47 | 11 % → 13 % | 8.0 px | 0.35 | 1.20 | 5 |
| stroke 48 | 12 % → 16 % | 9.2 px | 0.35 | 1.34 | 5 |
| stroke 49 | 6 % → 9 % | 4.2 px | 0.35 | 1.66 | 5 |
| stroke 50 | 7 % → 7 % | 5.2 px | 0.34 | 1.00 | 5 |
| stroke 51 | 8 % → 15 % | 6.4 px | 0.35 | 1.74 | 7 |
| stroke 52 | 12 % → 14 % | 9.1 px | 0.35 | 1.19 | 5 |
| stroke 53 | 11 % → 14 % | 8.1 px | 0.35 | 1.36 | 5 |
| stroke 54 | 10 % → 14 % | 7.4 px | 0.35 | 1.47 | 6 |
| stroke 55 | 11 % → 14 % | 8.2 px | 0.35 | 1.33 | 5 |
| stroke 56 | 11 % → 12 % | 8.4 px | 0.35 | 1.11 | 5 |
| stroke 57 | 9 % → 13 % | 7.1 px | 0.35 | 1.37 | 6 |
| stroke 58 | 10 % → 11 % | 7.7 px | 0.35 | 1.14 | 5 |
| stroke 59 | 11 % → 13 % | 8.4 px | 0.35 | 1.18 | 4 |
| stroke 60 | 16 % → 20 % | 11.9 px | 0.35 | 1.26 | 6 |
| stroke 61 | 19 % → 20 % | 14.5 px | 0.35 | 1.04 | 6 |
| stroke 62 | 10 % → 10 % | 7.3 px | 0.35 | 1.00 | 5 |
| stroke 63 | 11 % → 12 % | 8.7 px | 0.35 | 1.07 | 5 |
| stroke 64 | 14 % → 14 % | 10.7 px | 0.35 | 1.02 | 7 |
| stroke 65 | 15 % → 15 % | 11.5 px | 0.35 | 1.00 | 7 |
| stroke 66 | 14 % → 14 % | 10.7 px | 0.35 | 1.00 | 9 |
| stroke 67 | 12 % → 12 % | 8.8 px | 0.35 | 1.06 | 6 |
| stroke 68 | 5 % → 9 % | 3.6 px | 0.35 | 1.88 | 6 |
| stroke 69 | 5 % → 5 % | 4.1 px | 0.35 | 1.00 | 8 |
| stroke 70 | 10 % → 13 % | 7.4 px | 0.35 | 1.28 | 6 |
| stroke 71 | 9 % → 11 % | 7.1 px | 0.35 | 1.15 | 5 |
| stroke 72 | 5 % → 7 % | 4.2 px | 0.35 | 1.23 | 4 |
| stroke 73 | 12 % → 12 % | 9.3 px | 0.35 | 1.00 | 4 |
| stroke 74 | 14 % → 14 % | 10.8 px | 0.35 | 1.00 | 6 |
| stroke 75 | 15 % → 15 % | 11.4 px | 0.35 | 1.00 | 5 |
| stroke 76 | 14 % → 14 % | 10.5 px | 0.35 | 1.00 | 5 |
| stroke 77 | 7 % → 10 % | 5.4 px | 0.35 | 1.34 | 5 |
| stroke 78 | 9 % → 9 % | 7.0 px | 0.35 | 1.00 | 6 |
| stroke 79 | 7 % → 7 % | 5.7 px | 0.35 | 1.00 | 4 |
| stroke 80 | 11 % → 11 % | 8.3 px | 0.35 | 1.00 | 8 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #42 Oil pastel shaggy — own sheet
own sheet 600 × 600 · Pastel · 18 px · 2.7 s

![Brush Artist · Refs · #42 Oil pastel shaggy — own sheet](Brush-Artist-Refs-42-Oil-pastel-shaggy-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 5 % → 27 % | 8.0 px | 0.28 | 5.73 | 14 |
| stroke 2 | 5 % → 24 % | 8.6 px | 0.28 | 4.69 | 11 |
| stroke 3 | 5 % → 29 % | 8.9 px | 0.28 | 5.42 | 11 |
| stroke 4 | 5 % → 11 % | 8.8 px | 0.28 | 2.08 | 11 |
| stroke 5 | 6 % → 11 % | 9.9 px | 0.28 | 1.85 | 11 |
| stroke 6 | 8 % → 37 % | 13.9 px | 0.29 | 4.44 | 15 |
| stroke 7 | 11 % → 31 % | 17.6 px | 0.28 | 2.90 | 13 |
| stroke 8 | 7 % → 38 % | 11.4 px | 0.28 | 5.55 | 12 |
| stroke 9 | 8 % → 21 % | 13.9 px | 0.28 | 2.53 | 14 |
| stroke 10 | 8 % → 18 % | 13.2 px | 0.28 | 2.32 | 13 |
| stroke 11 | 6 % → 27 % | 9.4 px | 0.28 | 4.74 | 11 |
| stroke 12 | 8 % → 19 % | 13.6 px | 0.28 | 2.29 | 10 |
| stroke 13 | 13 % → 24 % | 21.0 px | 0.28 | 1.92 | 13 |
| stroke 14 | 5 % → 23 % | 7.9 px | 0.28 | 4.77 | 14 |
| stroke 15 | 5 % → 24 % | 9.0 px | 0.29 | 4.38 | 12 |
| stroke 16 | 9 % → 21 % | 15.7 px | 0.29 | 2.18 | 11 |
| stroke 17 | 17 % → 39 % | 27.9 px | 0.29 | 2.34 | 13 |
| stroke 18 | 14 % → 25 % | 22.8 px | 0.29 | 1.79 | 18 |
| stroke 19 | 15 % → 32 % | 24.9 px | 0.28 | 2.09 | 12 |
| stroke 20 | 21 % → 39 % | 35.1 px | 0.28 | 1.85 | 12 |
| stroke 21 | 9 % → 16 % | 14.4 px | 0.28 | 1.88 | 15 |
| stroke 22 | 14 % → 17 % | 23.9 px | 0.28 | 1.20 | 11 |
| stroke 23 | 12 % → 17 % | 20.6 px | 0.29 | 1.34 | 11 |
| stroke 24 | 18 % → 26 % | 30.0 px | 0.29 | 1.44 | 12 |
| stroke 25 | 20 % → 34 % | 32.6 px | 0.28 | 1.74 | 11 |
| stroke 26 | 6 % → 14 % | 9.2 px | 0.28 | 2.43 | 12 |
| stroke 27 | 18 % → 26 % | 30.4 px | 0.29 | 1.41 | 12 |
| stroke 28 | 14 % → 24 % | 23.7 px | 0.28 | 1.68 | 12 |
| stroke 29 | 9 % → 27 % | 14.9 px | 0.29 | 3.01 | 17 |
| stroke 30 | 15 % → 36 % | 24.9 px | 0.29 | 2.43 | 13 |
| stroke 31 | 14 % → 17 % | 23.3 px | 0.28 | 1.23 | 15 |
| stroke 32 | 16 % → 29 % | 27.0 px | 0.29 | 1.82 | 14 |
| stroke 33 | 15 % → 16 % | 24.5 px | 0.29 | 1.09 | 18 |
| stroke 34 | 19 % → 27 % | 31.4 px | 0.28 | 1.44 | 12 |
| stroke 35 | 26 % → 36 % | 42.5 px | 0.28 | 1.40 | 13 |
| stroke 36 | 25 % → 34 % | 41.0 px | 0.28 | 1.36 | 13 |
| stroke 37 | 12 % → 12 % | 19.3 px | 0.28 | 1.03 | 12 |
| stroke 38 | 19 % → 25 % | 31.7 px | 0.28 | 1.30 | 14 |
| stroke 39 | 16 % → 22 % | 27.3 px | 0.28 | 1.37 | 12 |
| stroke 40 | 22 % → 31 % | 36.6 px | 0.28 | 1.38 | 10 |
| stroke 41 | 32 % → 36 % | 53.1 px | 0.28 | 1.12 | 9 |
| stroke 42 | 23 % → 30 % | 38.1 px | 0.29 | 1.29 | 9 |
| stroke 43 | 12 % → 12 % | 20.3 px | 0.28 | 1.00 | 9 |
| stroke 44 | 30 % → 37 % | 48.9 px | 0.28 | 1.26 | 9 |
| stroke 45 | 16 % → 16 % | 26.2 px | 0.28 | 1.00 | 10 |
| stroke 46 | 29 % → 34 % | 47.9 px | 0.29 | 1.15 | 10 |
| stroke 47 | 38 % → 41 % | 62.0 px | 0.28 | 1.10 | 9 |
| stroke 48 | 29 % → 36 % | 47.8 px | 0.29 | 1.27 | 9 |
| stroke 49 | 27 % → 30 % | 45.1 px | 0.29 | 1.11 | 10 |
| stroke 50 | 38 % → 40 % | 63.4 px | 0.28 | 1.06 | 9 |
| stroke 51 | 16 % → 16 % | 26.0 px | 0.28 | 1.00 | 9 |
| stroke 52 | 37 % → 38 % | 62.4 px | 0.29 | 1.01 | 9 |
| stroke 53 | 22 % → 26 % | 36.9 px | 0.28 | 1.18 | 10 |
| stroke 54 | 17 % → 19 % | 29.0 px | 0.29 | 1.09 | 10 |
| stroke 55 | 15 % → 15 % | 25.0 px | 0.28 | 1.00 | 9 |
| stroke 56 | 13 % → 14 % | 21.6 px | 0.28 | 1.08 | 9 |
| stroke 57 | 23 % → 23 % | 37.7 px | 0.29 | 1.00 | 10 |
| stroke 58 | 28 % → 29 % | 46.1 px | 0.28 | 1.05 | 9 |
| stroke 59 | 40 % → 40 % | 67.3 px | 0.28 | 1.00 | 9 |
| stroke 60 | 22 % → 22 % | 35.6 px | 0.28 | 1.00 | 10 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #43 Dragged black ink blocks — own sheet
own sheet 600 × 600 · Gouache · 70 px · 6.9 s

![Brush Artist · Refs · #43 Dragged black ink blocks — own sheet](Brush-Artist-Refs-43-Dragged-black-ink-blocks-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 16 % → 12 % | 37.3 px | 0.46 | 0.73 | 372 |
| stroke 2 | 16 % → 13 % | 58.0 px | 0.46 | 0.78 | 404 |
| stroke 3 | 20 % → 16 % | 72.4 px | 0.46 | 0.79 | 377 |
| stroke 4 | 20 % → 16 % | 70.6 px | 0.46 | 0.77 | 385 |
| stroke 5 | 24 % → 14 % | 56.0 px | 0.46 | 0.57 | 407 |

## Brush Artist · Refs · #44 Blue looping ribbon — own sheet
own sheet 600 × 600 · Oil · 80 px · 4.4 s

![Brush Artist · Refs · #44 Blue looping ribbon — own sheet](Brush-Artist-Refs-44-Blue-looping-ribbon-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 32 % → 32 % | 42.2 px | 0.78 | 1.00 | 2333 |

## Brush Artist · Refs · #45 Soft pastel pepper — own sheet
own sheet 600 × 600 · Pastel · 40 px · 4.1 s

![Brush Artist · Refs · #45 Soft pastel pepper — own sheet](Brush-Artist-Refs-45-Soft-pastel-pepper-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 10 % → 39 % | 11.3 px | 0.49 | 3.75 | 323 |
| stroke 2 | 18 % → 34 % | 21.3 px | 0.49 | 1.87 | 302 |
| stroke 3 | 25 % → 37 % | 17.6 px | 0.49 | 1.46 | 279 |
| stroke 4 | 24 % → 35 % | 30.5 px | 0.49 | 1.43 | 309 |
| stroke 5 | 30 % → 30 % | 21.2 px | 0.49 | 1.00 | 205 |
| stroke 6 | 36 % → 44 % | 23.0 px | 0.48 | 1.23 | 290 |
| stroke 7 | 39 % → 43 % | 21.6 px | 0.48 | 1.10 | 333 |
| stroke 8 | 44 % → 44 % | 44.4 px | 0.49 | 1.00 | 307 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #46 Red-brown ink lips — own sheet
own sheet 600 × 600 · Watercolor · 50 px · 4.9 s

![Brush Artist · Refs · #46 Red-brown ink lips — own sheet](Brush-Artist-Refs-46-Red-brown-ink-lips-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 12 % → 24 % | 51.9 px | 0.59 | 1.91 | 90 |
| stroke 2 | 15 % → 27 % | 67.9 px | 0.54 | 1.73 | 71 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #47 Pink knife slabs — own sheet
own sheet 600 × 600 · Heavy acrylic · 90 px · 4.3 s

![Brush Artist · Refs · #47 Pink knife slabs — own sheet](Brush-Artist-Refs-47-Pink-knife-slabs-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 17 % → 32 % | 83.2 px | 0.11 | 1.94 | 256 |
| stroke 2 | 29 % → 43 % | 165.7 px | 0.11 | 1.46 | 267 |
| stroke 3 | 29 % → 43 % | 165.7 px | 0.11 | 1.47 | 262 |
| stroke 4 | 39 % → 38 % | 165.7 px | 0.11 | 0.98 | 272 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #48 Black bands with drips — own sheet
own sheet 600 × 600 · Gouache · 70 px · 9.8 s

![Brush Artist · Refs · #48 Black bands with drips — own sheet](Brush-Artist-Refs-48-Black-bands-with-drips-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 23 % → 36 % | 59.0 px | 0.39 | 1.58 | 461 |
| stroke 2 | 34 % → 48 % | 108.7 px | 0.39 | 1.41 | 424 |
| stroke 3 | 36 % → 48 % | 112.8 px | 0.39 | 1.34 | 616 |
| stroke 4 | 38 % → 36 % | 111.8 px | 0.39 | 0.95 | 567 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #49 Magenta letters round brush — own sheet
own sheet 600 × 600 · Ink · 30 px · 9.8 s

![Brush Artist · Refs · #49 Magenta letters round brush — own sheet](Brush-Artist-Refs-49-Magenta-letters-round-brush-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 27 % → 46 % | 64.3 px | 0.52 | 1.69 | 39 |
| stroke 2 | 29 % → 40 % | 52.5 px | 0.53 | 1.39 | 45 |
| stroke 3 | 41 % → 67 % | 96.4 px | 0.52 | 1.64 | 46 |
| stroke 4 | 34 % → 52 % | 53.7 px | 0.52 | 1.55 | 145 |
| stroke 5 | 40 % → 66 % | 94.8 px | 0.52 | 1.65 | 86 |
| stroke 6 | 54 % → 70 % | 231.2 px | 0.52 | 1.29 | 23 |
| stroke 7 | 41 % → 56 % | 63.9 px | 0.52 | 1.35 | 127 |
| stroke 8 | 36 % → 61 % | 91.9 px | 0.53 | 1.72 | 71 |
| stroke 9 | 49 % → 60 % | 152.9 px | 0.53 | 1.24 | 41 |
| stroke 10 | 42 % → 72 % | 100.5 px | 0.52 | 1.71 | 87 |
| stroke 11 | 52 % → 72 % | 219.5 px | 0.52 | 1.39 | 20 |
| stroke 12 | 53 % → 68 % | 82.2 px | 0.52 | 1.29 | 105 |
| stroke 13 | 42 % → 54 % | 116.0 px | 0.53 | 1.29 | 30 |
| stroke 14 | 45 % → 69 % | 131.9 px | 0.53 | 1.52 | 30 |
| stroke 15 | 43 % → 63 % | 102.4 px | 0.52 | 1.46 | 67 |
| stroke 16 | 52 % → 61 % | 220.2 px | 0.52 | 1.18 | 15 |
| stroke 17 | 53 % → 64 % | 82.3 px | 0.52 | 1.19 | 107 |
| stroke 18 | 36 % → 44 % | 99.6 px | 0.52 | 1.21 | 30 |
| stroke 19 | 54 % → 53 % | 123.8 px | 0.52 | 0.99 | 28 |
| stroke 20 | 54 % → 54 % | 125.3 px | 0.52 | 1.00 | 28 |
| stroke 21 | 49 % → 49 % | 81.3 px | 0.52 | 1.00 | 78 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #50 Thick swipes on photo — own sheet
own sheet 600 × 600 · Heavy acrylic · 40 px · 3.0 s

![Brush Artist · Refs · #50 Thick swipes on photo — own sheet](Brush-Artist-Refs-50-Thick-swipes-on-photo-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 9 % → 21 % | 42.7 px | 0.33 | 2.34 | 47 |
| stroke 2 | 9 % → 16 % | 42.4 px | 0.33 | 1.79 | 34 |
| stroke 3 | 10 % → 11 % | 41.8 px | 0.33 | 1.06 | 56 |
| stroke 4 | 11 % → 18 % | 42.6 px | 0.33 | 1.64 | 47 |
| stroke 5 | 11 % → 10 % | 41.9 px | 0.33 | 0.95 | 38 |
| stroke 6 | 17 % → 21 % | 97.3 px | 0.32 | 1.20 | 29 |
| stroke 7 | 22 % → 26 % | 92.7 px | 0.33 | 1.18 | 52 |
| stroke 8 | 21 % → 21 % | 119.6 px | 0.33 | 0.97 | 32 |
| stroke 9 | 9 % → 10 % | 42.0 px | 0.32 | 1.09 | 53 |
| stroke 10 | 22 % → 21 % | 73.6 px | 0.32 | 0.96 | 54 |
| stroke 11 | 9 % → 8 % | 42.6 px | 0.33 | 0.95 | 39 |
| stroke 12 | 17 % → 16 % | 93.0 px | 0.33 | 0.96 | 27 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Ink — dry brush — own sheet
own sheet 600 × 600 · Gouache · 30 px · 2.9 s

![Brush Artist · Ink — dry brush — own sheet](Brush-Artist-Ink-dry-brush-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| ear | 6 % → 3 % | 7.8 px | 0.86 | 0.44 | 465 |
| drag0 | 6 % → 8 % | 10.2 px | 0.86 | 1.39 | 116 |
| drag1 | 8 % → 8 % | 16.5 px | 0.86 | 1.02 | 98 |
| drag2 | 10 % → 9 % | 22.5 px | 0.86 | 0.87 | 87 |
| drag3 | 12 % → 9 % | 29.4 px | 0.86 | 0.78 | 67 |

## Brush Artist · Watercolour — blue — own sheet
own sheet 600 × 600 · Watercolor · 40 px · 10.3 s

![Brush Artist · Watercolour — blue — own sheet](Brush-Artist-Watercolour-blue-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| s0 | 7 % → 23 % | 28.4 px | 0.25 | 3.20 | 39 |
| s1 | 5 % → 32 % | 9.9 px | 0.38 | 5.85 | 39 |
| s2 | 10 % → 18 % | 43.5 px | 0.19 | 1.75 | 36 |
| s3 | 9 % → 17 % | 26.3 px | 0.28 | 1.85 | 47 |
| s4 | 14 % → 29 % | 37.9 px | 0.36 | 2.11 | 73 |
| s5 | 19 % → 29 % | 38.9 px | 0.37 | 1.52 | 56 |
| s6 | 17 % → 21 % | 47.6 px | 0.27 | 1.22 | 77 |
| s7 | 24 % → 35 % | 31.9 px | 0.37 | 1.44 | 51 |
| s8 | 20 % → 24 % | 77.5 px | 0.27 | 1.18 | 45 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Charcoal — stick — own sheet
own sheet 600 × 600 · Charcoal · 28 px · 1.3 s

![Brush Artist · Charcoal — stick — own sheet](Brush-Artist-Charcoal-stick-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| finger0 | 9 % → 18 % | 15.5 px | 0.83 | 2.01 | 30 |
| tip0 | 8 % → 14 % | 22.1 px | 0.83 | 1.75 | 9 |
| finger1 | 17 % → 29 % | 29.4 px | 0.83 | 1.74 | 29 |
| tip1 | 15 % → 21 % | 39.1 px | 0.83 | 1.42 | 9 |
| finger2 | 17 % → 25 % | 29.5 px | 0.83 | 1.53 | 31 |
| tip2 | 14 % → 20 % | 39.0 px | 0.83 | 1.41 | 9 |
| finger3 | 16 % → 19 % | 29.3 px | 0.83 | 1.16 | 25 |
| tip3 | 15 % → 15 % | 39.0 px | 0.83 | 1.00 | 10 |
| cig0 | 25 % → 35 % | 54.8 px | 0.83 | 1.41 | 10 |
| cig1 | 26 % → 35 % | 58.8 px | 0.83 | 1.32 | 10 |
| cig2 | 28 % → 35 % | 63.2 px | 0.83 | 1.22 | 10 |
| cig3 | 30 % → 34 % | 67.3 px | 0.83 | 1.14 | 10 |
| cig4 | 32 % → 34 % | 71.5 px | 0.83 | 1.06 | 10 |
| cig5 | 34 % → 34 % | 75.3 px | 0.83 | 1.00 | 12 |

Numbers say: wet paint spreads well beyond the stroke.

