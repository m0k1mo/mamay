![All brushes](contact.png)

# Brush Lab — 148 brushes · Nov 3, 2026 at 9:23 PM

Every sheet: 1500 × 600, ten strokes in a 5 × 2 grid — 1. light line · 2. heavy line · 3. pressure swell · 4. fast wave · 5. slow wave · 6. spiral · 7. loop · 8. tilted · 9. over the wet one · 10. long, no reload (cell 8 holds «tilted» and «over the wet one» crossed). The CPU reference of Mamay's paint engine; the wet layer settles 20 s at the end.

Columns: **covered** = share of the cell with paint right after the stroke → after settling; **width** = painted area of the stroke ÷ its length (px); **dark** = mean darkness of the painted pixels above the paper's own grain (0 = paper, 1 = black); **spread** = how far wet paint went beyond the stroke (1.0 = stayed); **ms** = the stroke on the CPU; long stroke: paint in each quarter of its length (it should run out: wet → streaks → dry tail).

## Ink Line
Ink · 12 px · 29.1 s

![Ink Line](Ink-Line.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 1 % → 4 % | 4.3 px | 0.55 | 2.44 | 85 |
| heavy line | 5 % → 6 % | 15.7 px | 0.68 | 1.13 | 72 |
| pressure swell | 3 % → 4 % | 11.3 px | 0.64 | 1.40 | 61 |
| fast wave | 10 % → 11 % | 11.2 px | 0.59 | 1.11 | 223 |
| slow wave | 8 % → 10 % | 9.6 px | 0.57 | 1.16 | 181 |
| spiral | 14 % → 15 % | 8.9 px | 0.50 | 1.07 | 257 |
| loop | 8 % → 9 % | 10.6 px | 0.61 | 1.16 | 131 |
| tilted | 5 % → 5 % | 14.4 px | 0.65 | 1.05 | 83 |
| over the wet one | 10 % → 11 % | 12.5 px | 0.65 | 1.15 | 76 |
| long, no reload | 18 % → 17 % | 8.1 px | 0.47 | 0.96 | 331 | quarters: 0.22 → 0.09 → 0.04 → 0.02

Numbers say: light vs heavy: width 4.3 → 15.7 px, dark 0.55 → 0.68; wet paint spreads well beyond the stroke.

## Dense Ink
Ink · 14 px · 30.2 s

![Dense Ink](Dense-Ink.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 5 % → 7 % | 15.2 px | 0.72 | 1.26 | 94 |
| heavy line | 7 % → 7 % | 19.1 px | 0.73 | 1.09 | 79 |
| pressure swell | 5 % → 6 % | 17.9 px | 0.72 | 1.17 | 72 |
| fast wave | 13 % → 13 % | 15.3 px | 0.69 | 1.01 | 250 |
| slow wave | 12 % → 12 % | 13.6 px | 0.67 | 1.04 | 168 |
| spiral | 18 % → 15 % | 12.2 px | 0.65 | 0.80 | 315 |
| loop | 11 % → 12 % | 14.8 px | 0.69 | 1.08 | 148 |
| tilted | 5 % → 6 % | 14.6 px | 0.72 | 1.07 | 94 |
| over the wet one | 12 % → 13 % | 17.7 px | 0.72 | 1.11 | 60 |
| long, no reload | 23 % → 15 % | 10.1 px | 0.64 | 0.66 | 361 | quarters: 0.30 → 0.12 → 0.04 → 0.02

Numbers say: light vs heavy: width 15.2 → 19.1 px, dark 0.72 → 0.73.

## Transparent Wash
Watercolor · 22 px · 30.8 s

![Transparent Wash](Transparent-Wash.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 2 % → 5 % | 6.9 px | 0.27 | 2.25 | 77 |
| heavy line | 7 % → 9 % | 20.4 px | 0.27 | 1.22 | 62 |
| pressure swell | 4 % → 6 % | 15.2 px | 0.28 | 1.54 | 53 |
| fast wave | 14 % → 16 % | 16.1 px | 0.20 | 1.17 | 210 |
| slow wave | 12 % → 15 % | 13.7 px | 0.21 | 1.28 | 275 |
| spiral | 18 % → 22 % | 11.9 px | 0.16 | 1.23 | 249 |
| loop | 11 % → 13 % | 14.5 px | 0.22 | 1.20 | 148 |
| tilted | 8 % → 8 % | 21.1 px | 0.24 | 1.06 | 71 |
| over the wet one | 13 % → 16 % | 16.4 px | 0.24 | 1.18 | 50 |
| long, no reload | 26 % → 32 % | 11.6 px | 0.13 | 1.22 | 318 | quarters: 0.11 → 0.04 → 0.02 → 0.01

Numbers say: light vs heavy: width 6.9 → 20.4 px, dark 0.27 → 0.27; wet paint spreads well beyond the stroke.

## Dry Brush
Gouache · 24 px · 23.7 s

![Dry Brush](Dry-Brush.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 5 % → 0 % | 14.0 px | 0.65 | 0.09 | 68 |
| heavy line | 6 % → 0 % | 18.6 px | 0.65 | 0.02 | 122 |
| pressure swell | 5 % → 0 % | 18.2 px | 0.65 | 0.08 | 76 |
| fast wave | 6 % → 1 % | 7.3 px | 0.65 | 0.08 | 195 |
| slow wave | 7 % → 0 % | 8.1 px | 0.65 | 0.06 | 309 |
| spiral | 7 % → 0 % | 4.6 px | 0.65 | 0.07 | 279 |
| loop | 10 % → 0 % | 12.4 px | 0.65 | 0.04 | 167 |
| tilted | 4 % → 3 % | 10.6 px | 0.65 | 0.88 | 91 |
| over the wet one | 9 % → 1 % | 14.5 px | 0.65 | 0.12 | 74 |
| long, no reload | 6 % → 1 % | 2.9 px | 0.65 | 0.14 | 417 | quarters: 0.12 → 0.00 → 0.00 → 0.00

Numbers say: light vs heavy: width 14.0 → 18.6 px, dark 0.65 → 0.65.

## Wax Crayon
Wax · 8 px · 11.9 s

![Wax Crayon](Wax-Crayon.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 1 % → 1 % | 2.5 px | 0.71 | 1.00 | 22 |
| heavy line | 1 % → 1 % | 3.9 px | 0.69 | 1.00 | 23 |
| pressure swell | 1 % → 1 % | 3.3 px | 0.70 | 1.00 | 14 |
| fast wave | 3 % → 3 % | 3.5 px | 0.69 | 1.00 | 42 |
| slow wave | 3 % → 3 % | 3.4 px | 0.70 | 1.00 | 57 |
| spiral | 5 % → 5 % | 3.3 px | 0.70 | 1.00 | 103 |
| loop | 3 % → 3 % | 3.3 px | 0.70 | 1.00 | 65 |
| tilted | 2 % → 2 % | 5.6 px | 0.68 | 1.00 | 32 |
| over the wet one | 3 % → 3 % | 3.6 px | 0.68 | 1.00 | 28 |
| long, no reload | 7 % → 7 % | 3.3 px | 0.70 | 1.00 | 160 | quarters: 0.06 → 0.06 → 0.06 → 0.06

Numbers say: light vs heavy: width 2.5 → 3.9 px, dark 0.71 → 0.69; the long stroke does not run out of paint.

## Oil Pastel
Wax · 12 px · 12.3 s

![Oil Pastel](Oil-Pastel.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 1 % → 1 % | 4.0 px | 0.68 | 1.00 | 29 |
| heavy line | 2 % → 2 % | 6.5 px | 0.68 | 1.00 | 46 |
| pressure swell | 2 % → 2 % | 5.7 px | 0.69 | 1.00 | 37 |
| fast wave | 5 % → 5 % | 5.7 px | 0.68 | 1.00 | 87 |
| slow wave | 5 % → 5 % | 5.5 px | 0.68 | 1.00 | 86 |
| spiral | 8 % → 8 % | 5.5 px | 0.68 | 1.00 | 124 |
| loop | 4 % → 4 % | 5.6 px | 0.68 | 1.00 | 68 |
| tilted | 2 % → 2 % | 6.8 px | 0.68 | 1.00 | 53 |
| over the wet one | 5 % → 5 % | 5.8 px | 0.68 | 1.00 | 33 |
| long, no reload | 13 % → 13 % | 5.6 px | 0.68 | 1.00 | 190 | quarters: 0.10 → 0.09 → 0.10 → 0.10

Numbers say: light vs heavy: width 4.0 → 6.5 px, dark 0.68 → 0.68; the long stroke does not run out of paint.

## Charcoal
Charcoal · 5 px · 11.4 s

![Charcoal](Charcoal.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 1 % → 1 % | 2.0 px | 0.74 | 1.00 | 28 |
| heavy line | 1 % → 1 % | 3.0 px | 0.74 | 1.00 | 13 |
| pressure swell | 1 % → 1 % | 2.7 px | 0.74 | 1.00 | 13 |
| fast wave | 2 % → 2 % | 2.7 px | 0.73 | 1.00 | 43 |
| slow wave | 2 % → 2 % | 2.6 px | 0.74 | 1.00 | 39 |
| spiral | 4 % → 4 % | 2.5 px | 0.74 | 1.00 | 68 |
| loop | 2 % → 2 % | 2.6 px | 0.74 | 1.00 | 35 |
| tilted | 2 % → 2 % | 4.3 px | 0.72 | 1.00 | 40 |
| over the wet one | 2 % → 2 % | 2.4 px | 0.72 | 1.00 | 12 |
| long, no reload | 6 % → 6 % | 2.7 px | 0.73 | 1.00 | 92 | quarters: 0.05 → 0.05 → 0.05 → 0.05

Numbers say: light vs heavy: width 2.0 → 3.0 px, dark 0.74 → 0.74; the long stroke does not run out of paint.

## Impasto
Heavy acrylic · 22 px · 17.8 s

![Impasto](Impasto.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 8 % → 8 % | 24.1 px | 0.71 | 0.93 | 74 |
| heavy line | 10 % → 9 % | 28.8 px | 0.70 | 0.94 | 118 |
| pressure swell | 7 % → 7 % | 28.1 px | 0.72 | 0.94 | 78 |
| fast wave | 20 % → 13 % | 23.5 px | 0.71 | 0.64 | 211 |
| slow wave | 21 % → 14 % | 24.5 px | 0.71 | 0.66 | 301 |
| spiral | 30 % → 14 % | 20.0 px | 0.71 | 0.46 | 326 |
| loop | 18 % → 14 % | 23.9 px | 0.71 | 0.77 | 172 |
| tilted | 8 % → 8 % | 21.8 px | 0.70 | 1.00 | 97 |
| over the wet one | 17 % → 15 % | 25.4 px | 0.70 | 0.91 | 90 |
| long, no reload | 34 % → 14 % | 15.2 px | 0.71 | 0.41 | 434 | quarters: 0.38 → 0.21 → 0.10 → 0.03

Numbers say: light vs heavy: width 24.1 → 28.8 px, dark 0.71 → 0.70.

## Oil Round
Oil · 18 px · 22.3 s

![Oil Round](Oil-Round.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 2 % → 2 % | 7.2 px | 0.75 | 1.00 | 92 |
| heavy line | 7 % → 7 % | 19.3 px | 0.73 | 1.00 | 144 |
| pressure swell | 4 % → 4 % | 13.7 px | 0.72 | 1.00 | 76 |
| fast wave | 11 % → 11 % | 12.7 px | 0.65 | 1.00 | 176 |
| slow wave | 8 % → 8 % | 9.0 px | 0.57 | 1.00 | 212 |
| spiral | 10 % → 10 % | 6.6 px | 0.50 | 1.00 | 282 |
| loop | 5 % → 5 % | 7.1 px | 0.45 | 1.00 | 127 |
| tilted | 4 % → 4 % | 10.1 px | 0.52 | 1.00 | 82 |
| over the wet one | 6 % → 6 % | 7.4 px | 0.52 | 1.00 | 59 |
| long, no reload | 15 % → 15 % | 6.8 px | 0.42 | 1.00 | 469 | quarters: 0.08 → 0.08 → 0.07 → 0.06

Numbers say: light vs heavy: width 7.2 → 19.3 px, dark 0.75 → 0.73.

## Palette Knife
Oil · 20 px · 21.5 s

![Palette Knife](Palette-Knife.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 8 % → 8 % | 21.9 px | 0.67 | 1.00 | 25 |
| heavy line | 8 % → 8 % | 22.5 px | 0.73 | 1.00 | 21 |
| pressure swell | 6 % → 6 % | 22.4 px | 0.74 | 1.00 | 8 |
| fast wave | 17 % → 17 % | 19.3 px | 0.49 | 1.00 | 41 |
| slow wave | 17 % → 17 % | 19.9 px | 0.43 | 1.00 | 61 |
| spiral | 18 % → 18 % | 11.7 px | 0.45 | 1.00 | 56 |
| loop | 16 % → 16 % | 21.0 px | 0.58 | 1.00 | 24 |
| tilted | 5 % → 5 % | 15.0 px | 0.72 | 1.00 | 13 |
| over the wet one | 13 % → 13 % | 21.0 px | 0.72 | 1.00 | 11 |
| long, no reload | 17 % → 17 % | 7.5 px | 0.47 | 1.00 | 72 | quarters: 0.29 → 0.05 → 0.00 → 0.00

Numbers say: light vs heavy: width 21.9 → 22.5 px, dark 0.67 → 0.73; pressure barely changes the width.

## Water
Watercolor · 20 px · 44.3 s · over bands of wet oil paint and oil pastel in turn (it works on paint already there: look at what it does to the bands; covered counts the bands too)

![Water](Water.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 25 % → 27 % | 73.8 px | 0.80 | 1.06 | 33 |
| heavy line | 24 % → 25 % | 69.8 px | 0.81 | 1.04 | 99 |
| pressure swell | 24 % → 25 % | 89.6 px | 0.81 | 1.03 | 73 |
| fast wave | 24 % → 26 % | 27.7 px | 0.81 | 1.07 | 147 |
| slow wave | 24 % → 25 % | 27.7 px | 0.81 | 1.06 | 189 |
| spiral | 24 % → 26 % | 15.9 px | 0.81 | 1.07 | 246 |
| loop | 24 % → 25 % | 31.1 px | 0.81 | 1.03 | 127 |
| tilted | 24 % → 24 % | 67.0 px | 0.81 | 1.00 | 77 |
| over the wet one | 24 % → 25 % | 0.0 px | 0.81 | 1.06 | 56 |
| long, no reload | 24 % → 26 % | 10.7 px | 0.81 | 1.08 | 381 | quarters: 0.21 → 0.27 → 0.18 → 0.27

Numbers say: light vs heavy: width 73.8 → 69.8 px, dark 0.80 → 0.81; pressure barely changes the width; the long stroke does not run out of paint.

## Blender
Pastel · 16 px · 26.5 s · over bands of wet oil paint and oil pastel in turn (it works on paint already there: look at what it does to the bands; covered counts the bands too)

![Blender](Blender.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 24 % → 24 % | 70.7 px | 0.81 | 1.00 | 41 |
| heavy line | 25 % → 25 % | 72.1 px | 0.80 | 1.00 | 63 |
| pressure swell | 24 % → 24 % | 91.3 px | 0.81 | 1.00 | 38 |
| fast wave | 26 % → 26 % | 30.0 px | 0.79 | 1.00 | 106 |
| slow wave | 26 % → 26 % | 29.9 px | 0.80 | 1.00 | 111 |
| spiral | 28 % → 28 % | 18.7 px | 0.77 | 1.00 | 172 |
| loop | 25 % → 25 % | 32.9 px | 0.80 | 1.00 | 87 |
| tilted | 25 % → 25 % | 70.1 px | 0.79 | 1.00 | 52 |
| over the wet one | 26 % → 26 % | 1.8 px | 0.79 | 1.00 | 45 |
| long, no reload | 30 % → 30 % | 13.7 px | 0.76 | 1.00 | 268 | quarters: 0.20 → 0.28 → 0.23 → 0.30

Numbers say: light vs heavy: width 70.7 → 72.1 px, dark 0.81 → 0.80; pressure barely changes the width; the long stroke does not run out of paint.

## Eraser
Eraser · 16 px · 26.7 s · over bands of wet oil paint and oil pastel in turn (it works on paint already there: look at what it does to the bands; covered counts the bands too)

![Eraser](Eraser.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 24 % → 24 % | 69.5 px | 0.82 | 1.00 | 54 |
| heavy line | 23 % → 23 % | 67.9 px | 0.82 | 1.00 | 86 |
| pressure swell | 23 % → 23 % | 87.3 px | 0.82 | 1.00 | 37 |
| fast wave | 22 % → 22 % | 25.7 px | 0.82 | 1.00 | 109 |
| slow wave | 22 % → 22 % | 25.7 px | 0.82 | 1.00 | 123 |
| spiral | 22 % → 22 % | 14.4 px | 0.82 | 1.00 | 235 |
| loop | 22 % → 22 % | 28.6 px | 0.82 | 1.00 | 90 |
| tilted | 23 % → 23 % | 65.1 px | 0.82 | 1.00 | 59 |
| over the wet one | 23 % → 23 % | 0.0 px | 0.82 | 1.00 | 41 |
| long, no reload | 20 % → 20 % | 8.9 px | 0.82 | 1.00 | 275 | quarters: 0.15 → 0.20 → 0.15 → 0.20

Numbers say: light vs heavy: width 69.5 → 67.9 px, dark 0.82 → 0.82; pressure barely changes the width; the long stroke does not run out of paint.

## Fan
Gouache · 30 px · 39.1 s

![Fan](Fan.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 9 % → 3 % | 25.7 px | 0.63 | 0.37 | 37 |
| heavy line | 11 % → 4 % | 31.0 px | 0.63 | 0.39 | 65 |
| pressure swell | 8 % → 5 % | 31.7 px | 0.63 | 0.55 | 41 |
| fast wave | 18 % → 5 % | 20.3 px | 0.63 | 0.26 | 198 |
| slow wave | 18 % → 5 % | 21.1 px | 0.63 | 0.25 | 301 |
| spiral | 24 % → 5 % | 15.8 px | 0.63 | 0.20 | 218 |
| loop | 17 % → 5 % | 22.7 px | 0.63 | 0.29 | 120 |
| tilted | 5 % → 6 % | 15.1 px | 0.63 | 1.05 | 48 |
| over the wet one | 16 % → 8 % | 29.8 px | 0.63 | 0.50 | 53 |
| long, no reload | 23 % → 5 % | 10.1 px | 0.63 | 0.22 | 341 | quarters: 0.29 → 0.07 → 0.01 → 0.00

Numbers say: light vs heavy: width 25.7 → 31.0 px, dark 0.63 → 0.63.

## Sponge
Gouache · 30 px · 38.9 s

![Sponge](Sponge.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 4 % → 0 % | 11.4 px | 0.62 | 0.12 | 48 |
| heavy line | 12 % → 2 % | 35.4 px | 0.62 | 0.14 | 90 |
| pressure swell | 7 % → 2 % | 27.9 px | 0.62 | 0.27 | 56 |
| fast wave | 20 % → 4 % | 23.2 px | 0.62 | 0.19 | 223 |
| slow wave | 21 % → 4 % | 23.7 px | 0.62 | 0.18 | 350 |
| spiral | 28 % → 4 % | 18.3 px | 0.62 | 0.14 | 275 |
| loop | 18 % → 5 % | 23.0 px | 0.62 | 0.29 | 150 |
| tilted | 7 % → 7 % | 18.2 px | 0.62 | 1.04 | 118 |
| over the wet one | 16 % → 6 % | 27.8 px | 0.62 | 0.37 | 76 |
| long, no reload | 29 % → 5 % | 12.9 px | 0.62 | 0.17 | 389 | quarters: 0.29 → 0.13 → 0.07 → 0.04

Numbers say: light vs heavy: width 11.4 → 35.4 px, dark 0.62 → 0.62.

## Ink — sumi brush
Watercolor · 22 px · 42.1 s

![Ink — sumi brush](Ink-sumi-brush.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 8 % → 9 % | 23.8 px | 0.77 | 1.13 | 113 |
| heavy line | 13 % → 13 % | 38.0 px | 0.72 | 1.01 | 124 |
| pressure swell | 9 % → 10 % | 34.5 px | 0.75 | 1.05 | 58 |
| fast wave | 27 % → 28 % | 31.7 px | 0.58 | 1.03 | 245 |
| slow wave | 25 % → 26 % | 29.0 px | 0.61 | 1.05 | 332 |
| spiral | 37 % → 38 % | 24.3 px | 0.51 | 1.03 | 355 |
| loop | 22 % → 22 % | 28.2 px | 0.66 | 1.03 | 181 |
| tilted | 9 % → 9 % | 24.7 px | 0.73 | 1.03 | 94 |
| over the wet one | 20 % → 21 % | 31.1 px | 0.73 | 1.03 | 129 |
| long, no reload | 42 % → 43 % | 18.9 px | 0.46 | 1.02 | 688 | quarters: 0.47 → 0.23 → 0.11 → 0.06

Numbers say: light vs heavy: width 23.8 → 38.0 px, dark 0.77 → 0.72.

## Ink — wash
Watercolor · 40 px · 45.1 s

![Ink — wash](Ink-wash.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 13 % → 13 % | 36.5 px | 0.17 | 1.04 | 105 |
| heavy line | 18 % → 19 % | 53.5 px | 0.13 | 1.04 | 113 |
| pressure swell | 12 % → 13 % | 46.6 px | 0.16 | 1.05 | 186 |
| fast wave | 40 % → 42 % | 45.9 px | 0.12 | 1.06 | 398 |
| slow wave | 38 % → 40 % | 43.6 px | 0.17 | 1.06 | 490 |
| spiral | 58 % → 62 % | 38.5 px | 0.12 | 1.06 | 495 |
| loop | 33 % → 34 % | 42.9 px | 0.15 | 1.03 | 276 |
| tilted | 14 % → 14 % | 38.1 px | 0.17 | 1.03 | 135 |
| over the wet one | 29 % → 31 % | 43.2 px | 0.17 | 1.06 | 116 |
| long, no reload | 66 % → 75 % | 29.8 px | 0.12 | 1.12 | 714 | quarters: 0.16 → 0.11 → 0.07 → 0.04

Numbers say: light vs heavy: width 36.5 → 53.5 px, dark 0.17 → 0.13.

## Ink — dry brush
Ink · 30 px · 32.2 s

![Ink — dry brush](Ink-dry-brush.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 9 % → 7 % | 25.2 px | 0.81 | 0.79 | 133 |
| heavy line | 10 % → 8 % | 29.6 px | 0.80 | 0.76 | 188 |
| pressure swell | 7 % → 6 % | 27.9 px | 0.81 | 0.85 | 204 |
| fast wave | 21 % → 8 % | 24.2 px | 0.79 | 0.40 | 474 |
| slow wave | 18 % → 7 % | 20.3 px | 0.79 | 0.39 | 554 |
| spiral | 24 % → 8 % | 15.6 px | 0.78 | 0.34 | 552 |
| loop | 19 % → 8 % | 24.3 px | 0.78 | 0.45 | 326 |
| tilted | 8 % → 8 % | 22.2 px | 0.78 | 1.02 | 165 |
| over the wet one | 17 % → 14 % | 25.9 px | 0.78 | 0.81 | 117 |
| long, no reload | 20 % → 8 % | 9.1 px | 0.79 | 0.41 | 670 | quarters: 0.32 → 0.02 → 0.00 → 0.00

Numbers say: light vs heavy: width 25.2 → 29.6 px, dark 0.81 → 0.80.

## Ink — nib
Watercolor · 5 px · 29.2 s

![Ink — nib](Ink-nib.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 2 % → 5 % | 5.4 px | 0.86 | 2.45 | 40 |
| heavy line | 2 % → 5 % | 6.4 px | 0.86 | 2.33 | 39 |
| pressure swell | 2 % → 4 % | 6.2 px | 0.86 | 2.52 | 33 |
| fast wave | 5 % → 8 % | 5.8 px | 0.82 | 1.65 | 102 |
| slow wave | 5 % → 8 % | 5.6 px | 0.82 | 1.73 | 86 |
| spiral | 7 % → 11 % | 4.8 px | 0.75 | 1.45 | 161 |
| loop | 4 % → 8 % | 5.6 px | 0.84 | 1.75 | 80 |
| tilted | 4 % → 4 % | 10.1 px | 0.85 | 1.04 | 42 |
| over the wet one | 6 % → 9 % | 6.3 px | 0.85 | 1.61 | 34 |
| long, no reload | 9 % → 12 % | 4.0 px | 0.70 | 1.37 | 226 | quarters: 0.23 → 0.08 → 0.04 → 0.02

Numbers say: light vs heavy: width 5.4 → 6.4 px, dark 0.86 → 0.86; wet paint spreads well beyond the stroke.

## 0.45 · Dry brush
Gouache · 34 px · 32.5 s

![0.45 · Dry brush](0-45-Dry-brush.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 10 % → 3 % | 29.4 px | 0.67 | 0.27 | 162 |
| heavy line | 11 % → 3 % | 31.6 px | 0.67 | 0.29 | 162 |
| pressure swell | 8 % → 3 % | 31.5 px | 0.67 | 0.41 | 121 |
| fast wave | 19 % → 3 % | 22.5 px | 0.67 | 0.18 | 385 |
| slow wave | 20 % → 4 % | 23.2 px | 0.67 | 0.18 | 650 |
| spiral | 21 % → 3 % | 14.1 px | 0.67 | 0.16 | 644 |
| loop | 20 % → 4 % | 26.1 px | 0.67 | 0.20 | 340 |
| tilted | 9 % → 8 % | 24.0 px | 0.67 | 0.98 | 209 |
| over the wet one | 19 % → 6 % | 28.2 px | 0.67 | 0.34 | 194 |
| long, no reload | 20 % → 4 % | 9.1 px | 0.67 | 0.19 | 1153 | quarters: 0.36 → 0.10 → 0.00 → 0.00

Numbers say: light vs heavy: width 29.4 → 31.6 px, dark 0.67 → 0.67; pressure barely changes the width.

## Dry pastel
Pastel · 26 px · 14.9 s

![Dry pastel](Dry-pastel.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 3 % → 3 % | 8.3 px | 0.38 | 1.00 | 46 |
| heavy line | 5 % → 5 % | 13.2 px | 0.39 | 1.00 | 41 |
| pressure swell | 3 % → 3 % | 11.7 px | 0.38 | 1.00 | 38 |
| fast wave | 10 % → 10 % | 11.9 px | 0.39 | 1.00 | 119 |
| slow wave | 10 % → 10 % | 11.3 px | 0.39 | 1.00 | 203 |
| spiral | 15 % → 15 % | 9.6 px | 0.39 | 1.00 | 180 |
| loop | 7 % → 7 % | 9.4 px | 0.39 | 1.00 | 87 |
| tilted | 3 % → 3 % | 8.3 px | 0.38 | 1.00 | 72 |
| over the wet one | 7 % → 7 % | 11.1 px | 0.38 | 1.00 | 46 |
| long, no reload | 18 % → 18 % | 8.2 px | 0.39 | 1.00 | 239 | quarters: 0.08 → 0.08 → 0.08 → 0.07

Numbers say: light vs heavy: width 8.3 → 13.2 px, dark 0.38 → 0.39; the long stroke does not run out of paint.

## 0.45 · Charcoal
Charcoal · 18 px · 14.5 s

![0.45 · Charcoal](0-45-Charcoal.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 2 % → 2 % | 6.5 px | 0.80 | 1.00 | 26 |
| heavy line | 3 % → 3 % | 9.2 px | 0.80 | 1.00 | 33 |
| pressure swell | 2 % → 2 % | 8.8 px | 0.80 | 1.00 | 35 |
| fast wave | 7 % → 7 % | 8.5 px | 0.80 | 1.00 | 100 |
| slow wave | 7 % → 7 % | 8.0 px | 0.80 | 1.00 | 108 |
| spiral | 12 % → 12 % | 7.9 px | 0.80 | 1.00 | 142 |
| loop | 6 % → 6 % | 8.1 px | 0.80 | 1.00 | 91 |
| tilted | 3 % → 3 % | 7.5 px | 0.80 | 1.00 | 68 |
| over the wet one | 6 % → 6 % | 7.9 px | 0.80 | 1.00 | 36 |
| long, no reload | 17 % → 17 % | 7.8 px | 0.80 | 1.00 | 135 | quarters: 0.15 → 0.16 → 0.15 → 0.16

Numbers say: light vs heavy: width 6.5 → 9.2 px, dark 0.80 → 0.80; the long stroke does not run out of paint.

## Watercolour — wash
Watercolor · 50 px · 48.1 s

![Watercolour — wash](Watercolour-wash.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 15 % → 16 % | 43.3 px | 0.03 | 1.05 | 117 |
| heavy line | 21 % → 22 % | 62.1 px | 0.03 | 1.04 | 159 |
| pressure swell | 14 % → 15 % | 54.3 px | 0.03 | 1.04 | 103 |
| fast wave | 47 % → 49 % | 53.8 px | 0.02 | 1.04 | 438 |
| slow wave | 45 % → 46 % | 52.0 px | 0.04 | 1.03 | 817 |
| spiral | 64 % → 66 % | 42.5 px | 0.03 | 1.03 | 644 |
| loop | 39 % → 40 % | 50.3 px | 0.03 | 1.02 | 301 |
| tilted | 17 % → 17 % | 47.3 px | 0.04 | 1.03 | 334 |
| over the wet one | 35 % → 36 % | 49.0 px | 0.04 | 1.04 | 145 |
| long, no reload | 79 % → 84 % | 35.5 px | 0.03 | 1.06 | 1116 | quarters: 0.04 → 0.03 → 0.02 → 0.01

Numbers say: light vs heavy: width 43.3 → 62.1 px, dark 0.03 → 0.03.

## Watercolour — wet-in-wet
Watercolor · 44 px · 50.5 s

![Watercolour — wet-in-wet](Watercolour-wet-in-wet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 13 % → 19 % | 36.6 px | 0.05 | 1.51 | 142 |
| heavy line | 18 % → 20 % | 52.4 px | 0.05 | 1.09 | 191 |
| pressure swell | 12 % → 15 % | 44.9 px | 0.06 | 1.26 | 128 |
| fast wave | 40 % → 45 % | 45.9 px | 0.05 | 1.13 | 405 |
| slow wave | 39 % → 45 % | 45.0 px | 0.07 | 1.15 | 496 |
| spiral | 62 % → 67 % | 40.8 px | 0.06 | 1.08 | 545 |
| loop | 33 % → 37 % | 43.2 px | 0.06 | 1.12 | 368 |
| tilted | 14 % → 14 % | 39.1 px | 0.06 | 1.03 | 165 |
| over the wet one | 29 % → 37 % | 41.7 px | 0.06 | 1.28 | 105 |
| long, no reload | 75 % → 84 % | 33.6 px | 0.06 | 1.12 | 742 | quarters: 0.07 → 0.06 → 0.04 → 0.03

Numbers say: light vs heavy: width 36.6 → 52.4 px, dark 0.05 → 0.05; wet paint spreads well beyond the stroke.

## Watercolour — glaze
Watercolor · 38 px · 45.1 s

![Watercolour — glaze](Watercolour-glaze.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 12 % → 13 % | 35.2 px | 0.03 | 1.05 | 84 |
| heavy line | 18 % → 19 % | 52.2 px | 0.02 | 1.06 | 113 |
| pressure swell | 12 % → 13 % | 44.6 px | 0.02 | 1.07 | 117 |
| fast wave | 37 % → 40 % | 42.4 px | 0.02 | 1.08 | 354 |
| slow wave | 35 % → 37 % | 40.2 px | 0.02 | 1.08 | 408 |
| spiral | 54 % → 59 % | 35.9 px | 0.02 | 1.09 | 447 |
| loop | 32 % → 33 % | 40.8 px | 0.02 | 1.05 | 225 |
| tilted | 13 % → 14 % | 37.0 px | 0.03 | 1.03 | 157 |
| over the wet one | 28 % → 30 % | 41.7 px | 0.03 | 1.06 | 112 |
| long, no reload | 60 % → 69 % | 26.8 px | 0.02 | 1.15 | 696 | quarters: 0.02 → 0.01 → 0.01 → 0.00

Numbers say: light vs heavy: width 35.2 → 52.2 px, dark 0.03 → 0.02.

## Watercolour — granulating
Watercolor · 44 px · 47.8 s

![Watercolour — granulating](Watercolour-granulating.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 14 % → 14 % | 40.5 px | 0.05 | 1.03 | 141 |
| heavy line | 20 % → 21 % | 59.2 px | 0.04 | 1.02 | 192 |
| pressure swell | 14 % → 14 % | 51.3 px | 0.05 | 1.02 | 133 |
| fast wave | 44 % → 45 % | 50.3 px | 0.04 | 1.04 | 368 |
| slow wave | 40 % → 42 % | 46.0 px | 0.06 | 1.06 | 676 |
| spiral | 59 % → 63 % | 38.7 px | 0.04 | 1.07 | 723 |
| loop | 36 % → 37 % | 46.9 px | 0.05 | 1.02 | 394 |
| tilted | 15 % → 16 % | 43.1 px | 0.06 | 1.03 | 165 |
| over the wet one | 32 % → 33 % | 46.6 px | 0.06 | 1.04 | 119 |
| long, no reload | 68 % → 76 % | 30.3 px | 0.04 | 1.12 | 869 | quarters: 0.06 → 0.04 → 0.02 → 0.02

Numbers say: light vs heavy: width 40.5 → 59.2 px, dark 0.05 → 0.04.

## Watercolour — dry brush
Watercolor · 36 px · 37.6 s

![Watercolour — dry brush](Watercolour-dry-brush.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 9 % → 9 % | 24.9 px | 0.07 | 1.09 | 143 |
| heavy line | 13 % → 13 % | 36.7 px | 0.06 | 0.99 | 162 |
| pressure swell | 10 % → 10 % | 36.4 px | 0.06 | 1.04 | 144 |
| fast wave | 24 % → 19 % | 27.3 px | 0.05 | 0.82 | 343 |
| slow wave | 22 % → 17 % | 25.2 px | 0.05 | 0.78 | 585 |
| spiral | 29 % → 20 % | 19.3 px | 0.05 | 0.67 | 567 |
| loop | 19 % → 18 % | 24.6 px | 0.05 | 0.94 | 278 |
| tilted | 9 % → 10 % | 24.3 px | 0.06 | 1.10 | 475 |
| over the wet one | 20 % → 20 % | 31.7 px | 0.06 | 0.99 | 248 |
| long, no reload | 28 % → 19 % | 12.4 px | 0.05 | 0.70 | 977 | quarters: 0.03 → 0.01 → 0.00 → 0.00

Numbers say: light vs heavy: width 24.9 → 36.7 px, dark 0.07 → 0.06.

## Gouache
Gouache · 30 px · 35.3 s

![Gouache](Gouache.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 8 % → 5 % | 24.4 px | 0.28 | 0.64 | 112 |
| heavy line | 14 % → 6 % | 39.7 px | 0.28 | 0.47 | 114 |
| pressure swell | 10 % → 6 % | 38.6 px | 0.28 | 0.60 | 87 |
| fast wave | 28 % → 7 % | 32.2 px | 0.28 | 0.25 | 278 |
| slow wave | 27 % → 8 % | 31.4 px | 0.28 | 0.29 | 533 |
| spiral | 38 % → 8 % | 24.8 px | 0.27 | 0.22 | 469 |
| loop | 22 % → 8 % | 28.6 px | 0.28 | 0.35 | 600 |
| tilted | 9 % → 9 % | 23.8 px | 0.27 | 1.01 | 238 |
| over the wet one | 20 % → 13 % | 31.1 px | 0.27 | 0.66 | 162 |
| long, no reload | 40 % → 9 % | 17.9 px | 0.27 | 0.24 | 651 | quarters: 0.01 → 0.01 → 0.02 → 0.02

Numbers say: light vs heavy: width 24.4 → 39.7 px, dark 0.28 → 0.28; the long stroke does not run out of paint.

## Oil — alla prima
Oil · 30 px · 18.3 s

![Oil — alla prima](Oil-alla-prima.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 10 % → 10 % | 27.6 px | 0.51 | 1.00 | 156 |
| heavy line | 10 % → 10 % | 30.4 px | 0.51 | 1.00 | 135 |
| pressure swell | 8 % → 8 % | 29.9 px | 0.53 | 1.00 | 104 |
| fast wave | 24 % → 24 % | 28.1 px | 0.51 | 1.00 | 360 |
| slow wave | 26 % → 26 % | 29.6 px | 0.51 | 1.00 | 422 |
| spiral | 40 % → 40 % | 26.4 px | 0.51 | 1.00 | 434 |
| loop | 21 % → 21 % | 27.7 px | 0.52 | 1.00 | 260 |
| tilted | 11 % → 11 % | 30.4 px | 0.51 | 1.00 | 151 |
| over the wet one | 20 % → 20 % | 26.6 px | 0.51 | 1.00 | 114 |
| long, no reload | 49 % → 49 % | 22.0 px | 0.50 | 1.00 | 788 | quarters: 0.32 → 0.29 → 0.26 → 0.22

Numbers say: light vs heavy: width 27.6 → 30.4 px, dark 0.51 → 0.51; pressure barely changes the width.

## Oil — impasto
Oil · 34 px · 25.4 s

![Oil — impasto](Oil-impasto.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 12 % → 12 % | 33.5 px | 0.24 | 1.00 | 150 |
| heavy line | 13 % → 13 % | 36.4 px | 0.23 | 1.00 | 163 |
| pressure swell | 10 % → 10 % | 35.9 px | 0.26 | 1.00 | 87 |
| fast wave | 30 % → 30 % | 35.1 px | 0.24 | 1.00 | 311 |
| slow wave | 31 % → 31 % | 35.8 px | 0.24 | 1.00 | 532 |
| spiral | 52 % → 52 % | 34.1 px | 0.22 | 1.00 | 588 |
| loop | 26 % → 26 % | 33.7 px | 0.24 | 1.00 | 387 |
| tilted | 12 % → 12 % | 32.8 px | 0.24 | 1.00 | 193 |
| over the wet one | 23 % → 23 % | 32.0 px | 0.24 | 1.00 | 174 |
| long, no reload | 60 % → 60 % | 27.0 px | 0.22 | 1.00 | 995 | quarters: 0.18 → 0.16 → 0.13 → 0.10

Numbers say: light vs heavy: width 33.5 → 36.4 px, dark 0.24 → 0.23; pressure barely changes the width.

## Oil — glaze
Oil · 40 px · 20.9 s

![Oil — glaze](Oil-glaze.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 9 % → 9 % | 25.4 px | 0.50 | 1.00 | 110 |
| heavy line | 13 % → 13 % | 36.3 px | 0.49 | 1.00 | 135 |
| pressure swell | 9 % → 9 % | 35.3 px | 0.50 | 1.00 | 108 |
| fast wave | 26 % → 26 % | 30.1 px | 0.48 | 1.00 | 289 |
| slow wave | 29 % → 29 % | 33.7 px | 0.49 | 1.00 | 586 |
| spiral | 44 % → 44 % | 29.0 px | 0.49 | 1.00 | 618 |
| loop | 23 % → 23 % | 30.2 px | 0.50 | 1.00 | 355 |
| tilted | 10 % → 10 % | 28.9 px | 0.50 | 1.00 | 224 |
| over the wet one | 22 % → 22 % | 31.6 px | 0.50 | 1.00 | 159 |
| long, no reload | 51 % → 51 % | 22.7 px | 0.49 | 1.00 | 958 | quarters: 0.33 → 0.29 → 0.26 → 0.22

Numbers say: light vs heavy: width 25.4 → 36.3 px, dark 0.50 → 0.49.

## Oil — scumble
Oil · 36 px · 20.6 s

![Oil — scumble](Oil-scumble.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 11 % → 11 % | 33.1 px | 0.28 | 1.00 | 167 |
| heavy line | 12 % → 12 % | 36.1 px | 0.28 | 1.00 | 181 |
| pressure swell | 9 % → 9 % | 35.5 px | 0.28 | 1.00 | 155 |
| fast wave | 26 % → 26 % | 29.6 px | 0.19 | 1.00 | 580 |
| slow wave | 27 % → 27 % | 30.9 px | 0.18 | 1.00 | 705 |
| spiral | 41 % → 41 % | 27.1 px | 0.13 | 1.00 | 949 |
| loop | 24 % → 24 % | 30.7 px | 0.20 | 1.00 | 518 |
| tilted | 11 % → 11 % | 30.5 px | 0.25 | 1.00 | 233 |
| over the wet one | 22 % → 22 % | 31.5 px | 0.25 | 1.00 | 195 |
| long, no reload | 45 % → 45 % | 20.3 px | 0.12 | 1.00 | 1261 | quarters: 0.00 → 0.00 → 0.00 → 0.00

Numbers say: light vs heavy: width 33.1 → 36.1 px, dark 0.28 → 0.28; pressure barely changes the width.

## Acrylic — heavy body
Heavy acrylic · 30 px · 19.2 s

![Acrylic — heavy body](Acrylic-heavy-body.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 10 % → 9 % | 29.0 px | 0.51 | 0.90 | 220 |
| heavy line | 11 % → 10 % | 31.2 px | 0.51 | 0.92 | 169 |
| pressure swell | 8 % → 8 % | 30.8 px | 0.53 | 0.94 | 111 |
| fast wave | 23 % → 15 % | 26.5 px | 0.52 | 0.64 | 373 |
| slow wave | 24 % → 16 % | 27.8 px | 0.51 | 0.64 | 627 |
| spiral | 35 % → 15 % | 23.3 px | 0.51 | 0.43 | 537 |
| loop | 21 % → 16 % | 26.9 px | 0.51 | 0.76 | 267 |
| tilted | 9 % → 9 % | 24.9 px | 0.51 | 0.99 | 142 |
| over the wet one | 19 % → 17 % | 27.8 px | 0.51 | 0.89 | 127 |
| long, no reload | 39 % → 16 % | 17.3 px | 0.51 | 0.41 | 634 | quarters: 0.29 → 0.20 → 0.12 → 0.04

Numbers say: light vs heavy: width 29.0 → 31.2 px, dark 0.51 → 0.51; pressure barely changes the width.

## Acrylic — fluid
Watercolor · 36 px · 39.6 s

![Acrylic — fluid](Acrylic-fluid.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 12 % → 12 % | 34.3 px | 0.08 | 1.02 | 129 |
| heavy line | 18 % → 18 % | 51.6 px | 0.07 | 1.01 | 111 |
| pressure swell | 12 % → 12 % | 44.8 px | 0.08 | 1.01 | 81 |
| fast wave | 37 % → 38 % | 42.6 px | 0.07 | 1.02 | 280 |
| slow wave | 34 % → 35 % | 39.2 px | 0.07 | 1.03 | 358 |
| spiral | 52 % → 53 % | 34.2 px | 0.07 | 1.03 | 494 |
| loop | 30 % → 31 % | 39.4 px | 0.07 | 1.02 | 236 |
| tilted | 12 % → 12 % | 32.6 px | 0.08 | 1.04 | 151 |
| over the wet one | 27 % → 28 % | 43.2 px | 0.08 | 1.02 | 117 |
| long, no reload | 56 % → 58 % | 25.3 px | 0.06 | 1.04 | 818 | quarters: 0.06 → 0.05 → 0.03 → 0.02

Numbers say: light vs heavy: width 34.3 → 51.6 px, dark 0.08 → 0.07.

## Acrylic — palette knife
Heavy acrylic · 42 px · 25.8 s

![Acrylic — palette knife](Acrylic-palette-knife.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 15 % → 15 % | 44.0 px | 0.39 | 0.98 | 79 |
| heavy line | 15 % → 15 % | 44.2 px | 0.40 | 0.97 | 31 |
| pressure swell | 12 % → 12 % | 43.5 px | 0.42 | 0.99 | 14 |
| fast wave | 36 % → 20 % | 41.9 px | 0.36 | 0.56 | 65 |
| slow wave | 37 % → 21 % | 42.6 px | 0.37 | 0.57 | 112 |
| spiral | 50 % → 18 % | 32.7 px | 0.37 | 0.37 | 114 |
| loop | 32 % → 24 % | 41.2 px | 0.36 | 0.75 | 76 |
| tilted | 12 % → 12 % | 33.6 px | 0.39 | 1.00 | 28 |
| over the wet one | 26 % → 25 % | 39.7 px | 0.39 | 0.97 | 74 |
| long, no reload | 57 % → 21 % | 25.6 px | 0.34 | 0.36 | 333 | quarters: 0.00 → 0.00 → 0.00 → 0.01

Numbers say: light vs heavy: width 44.0 → 44.2 px, dark 0.39 → 0.40; pressure barely changes the width; the long stroke does not run out of paint.

## Finger on oil
Oil · 30 px · 18.7 s

![Finger on oil](Finger-on-oil.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 8 % → 8 % | 23.8 px | 0.41 | 1.00 | 77 |
| heavy line | 13 % → 13 % | 36.6 px | 0.39 | 1.00 | 88 |
| pressure swell | 9 % → 9 % | 33.4 px | 0.41 | 1.00 | 58 |
| fast wave | 22 % → 22 % | 26.0 px | 0.35 | 1.00 | 150 |
| slow wave | 24 % → 24 % | 27.9 px | 0.35 | 1.00 | 564 |
| spiral | 36 % → 36 % | 23.5 px | 0.28 | 1.00 | 662 |
| loop | 21 % → 21 % | 27.4 px | 0.36 | 1.00 | 349 |
| tilted | 10 % → 10 % | 26.5 px | 0.40 | 1.00 | 189 |
| over the wet one | 20 % → 20 % | 29.4 px | 0.40 | 1.00 | 225 |
| long, no reload | 37 % → 37 % | 16.4 px | 0.26 | 1.00 | 604 | quarters: 0.23 → 0.11 → 0.05 → 0.02

Numbers say: light vs heavy: width 23.8 → 36.6 px, dark 0.41 → 0.39.

## Palette knife — oil
Oil · 44 px · 23.2 s

![Palette knife — oil](Palette-knife-oil.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 16 % → 16 % | 45.6 px | 0.36 | 1.00 | 37 |
| heavy line | 16 % → 16 % | 46.3 px | 0.38 | 1.00 | 49 |
| pressure swell | 12 % → 12 % | 45.2 px | 0.38 | 1.00 | 23 |
| fast wave | 39 % → 39 % | 44.9 px | 0.34 | 1.01 | 96 |
| slow wave | 39 % → 39 % | 45.4 px | 0.35 | 1.00 | 119 |
| spiral | 62 % → 62 % | 40.9 px | 0.27 | 1.00 | 147 |
| loop | 34 % → 34 % | 43.8 px | 0.35 | 1.00 | 55 |
| tilted | 13 % → 13 % | 36.6 px | 0.37 | 1.00 | 33 |
| over the wet one | 28 % → 28 % | 40.8 px | 0.37 | 1.00 | 35 |
| long, no reload | 74 % → 74 % | 33.1 px | 0.25 | 1.00 | 163 | quarters: 0.00 → 0.00 → 0.00 → 0.00

Numbers say: light vs heavy: width 45.6 → 46.3 px, dark 0.36 → 0.38; pressure barely changes the width; the long stroke does not run out of paint.

## 0.45 · Sponge
Watercolor · 46 px · 38.1 s

![0.45 · Sponge](0-45-Sponge.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 23 % → 15 % | 66.4 px | 0.02 | 0.67 | 57 |
| heavy line | 28 % → 23 % | 81.1 px | 0.02 | 0.81 | 89 |
| pressure swell | 20 % → 16 % | 76.7 px | 0.03 | 0.76 | 58 |
| fast wave | 46 % → 32 % | 53.0 px | 0.03 | 0.70 | 172 |
| slow wave | 53 % → 46 % | 60.7 px | 0.04 | 0.87 | 323 |
| spiral | 65 % → 53 % | 42.6 px | 0.04 | 0.82 | 312 |
| loop | 46 % → 40 % | 60.1 px | 0.04 | 0.86 | 220 |
| tilted | 16 % → 17 % | 43.8 px | 0.05 | 1.07 | 149 |
| over the wet one | 40 % → 35 % | 67.3 px | 0.05 | 0.89 | 113 |
| long, no reload | 74 % → 65 % | 33.2 px | 0.04 | 0.88 | 865 | quarters: 0.05 → 0.04 → 0.03 → 0.02

Numbers say: light vs heavy: width 66.4 → 81.1 px, dark 0.02 → 0.02.

## 0.45 · Eraser
Eraser · 30 px · 25.7 s · over bands of wet oil paint and oil pastel in turn (it works on paint already there: look at what it does to the bands; covered counts the bands too)

![0.45 · Eraser](0-45-Eraser.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 24 % → 24 % | 69.2 px | 0.82 | 1.00 | 46 |
| heavy line | 23 % → 23 % | 67.4 px | 0.81 | 1.00 | 60 |
| pressure swell | 23 % → 23 % | 86.7 px | 0.82 | 1.00 | 40 |
| fast wave | 21 % → 21 % | 24.7 px | 0.81 | 1.00 | 178 |
| slow wave | 20 % → 20 % | 23.5 px | 0.82 | 1.00 | 338 |
| spiral | 20 % → 20 % | 13.5 px | 0.79 | 1.00 | 335 |
| loop | 21 % → 21 % | 27.8 px | 0.80 | 1.00 | 240 |
| tilted | 23 % → 23 % | 64.8 px | 0.81 | 1.00 | 134 |
| over the wet one | 22 % → 22 % | 0.0 px | 0.81 | 1.00 | 114 |
| long, no reload | 17 % → 17 % | 7.5 px | 0.79 | 1.00 | 407 | quarters: 0.13 → 0.16 → 0.13 → 0.17

Numbers say: light vs heavy: width 69.2 → 67.4 px, dark 0.82 → 0.81; pressure barely changes the width; the long stroke does not run out of paint.

## Lift wet paint
Eraser · 30 px · 21.3 s · over bands of wet oil paint and oil pastel in turn (it works on paint already there: look at what it does to the bands; covered counts the bands too)

![Lift wet paint](Lift-wet-paint.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 24 % → 24 % | 70.1 px | 0.82 | 1.00 | 72 |
| heavy line | 24 % → 24 % | 69.8 px | 0.82 | 1.00 | 58 |
| pressure swell | 24 % → 24 % | 89.5 px | 0.82 | 1.00 | 32 |
| fast wave | 24 % → 24 % | 27.7 px | 0.82 | 1.00 | 104 |
| slow wave | 24 % → 24 % | 27.7 px | 0.82 | 1.00 | 180 |
| spiral | 24 % → 24 % | 15.9 px | 0.82 | 1.00 | 210 |
| loop | 24 % → 24 % | 31.1 px | 0.82 | 1.00 | 92 |
| tilted | 24 % → 24 % | 66.8 px | 0.82 | 1.00 | 49 |
| over the wet one | 24 % → 24 % | 0.0 px | 0.82 | 1.00 | 44 |
| long, no reload | 24 % → 24 % | 10.7 px | 0.82 | 1.00 | 339 | quarters: 0.18 → 0.24 → 0.17 → 0.24

Numbers say: light vs heavy: width 70.1 → 69.8 px, dark 0.82 → 0.82; pressure barely changes the width; the long stroke does not run out of paint.

## Sgraffito
Eraser · 10 px · 21.4 s · over bands of wet oil paint and oil pastel in turn (it works on paint already there: look at what it does to the bands; covered counts the bands too)

![Sgraffito](Sgraffito.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 24 % → 24 % | 69.5 px | 0.81 | 1.00 | 10 |
| heavy line | 24 % → 24 % | 69.5 px | 0.82 | 1.00 | 9 |
| pressure swell | 24 % → 24 % | 89.5 px | 0.82 | 1.00 | 6 |
| fast wave | 24 % → 24 % | 27.4 px | 0.82 | 1.00 | 19 |
| slow wave | 24 % → 24 % | 27.4 px | 0.81 | 1.00 | 19 |
| spiral | 24 % → 24 % | 15.7 px | 0.81 | 1.00 | 35 |
| loop | 24 % → 24 % | 30.9 px | 0.82 | 1.00 | 19 |
| tilted | 24 % → 24 % | 66.6 px | 0.82 | 1.00 | 8 |
| over the wet one | 24 % → 24 % | 0.0 px | 0.82 | 1.00 | 7 |
| long, no reload | 24 % → 24 % | 10.6 px | 0.82 | 1.00 | 50 | quarters: 0.17 → 0.24 → 0.17 → 0.24

Numbers say: light vs heavy: width 69.5 → 69.5 px, dark 0.81 → 0.82; pressure barely changes the width; the long stroke does not run out of paint.

## Brush Artist · Refs · #01 Henry Ward peach cloud
Gouache · 44 px · 53.5 s

![Brush Artist · Refs · #01 Henry Ward peach cloud](Brush-Artist-Refs-01-Henry-Ward-peach-cloud.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 15 % → 12 % | 42.2 px | 0.32 | 0.80 | 134 |
| heavy line | 16 % → 13 % | 45.5 px | 0.32 | 0.84 | 150 |
| pressure swell | 12 % → 10 % | 44.0 px | 0.32 | 0.87 | 137 |
| fast wave | 37 % → 18 % | 43.1 px | 0.32 | 0.48 | 500 |
| slow wave | 37 % → 18 % | 43.1 px | 0.32 | 0.48 | 811 |
| spiral | 59 % → 19 % | 39.1 px | 0.32 | 0.32 | 892 |
| loop | 32 % → 19 % | 41.3 px | 0.32 | 0.60 | 581 |
| tilted | 13 % → 13 % | 36.7 px | 0.32 | 0.99 | 262 |
| over the wet one | 27 % → 23 % | 38.9 px | 0.32 | 0.85 | 209 |
| long, no reload | 69 % → 20 % | 30.8 px | 0.32 | 0.29 | 2161 | quarters: 0.01 → 0.01 → 0.01 → 0.02

Numbers say: light vs heavy: width 42.2 → 45.5 px, dark 0.32 → 0.32; pressure barely changes the width; the long stroke does not run out of paint.

## Brush Artist · Refs · #02 Henry Ward cream strokes
Gouache · 46 px · 50.8 s

![Brush Artist · Refs · #02 Henry Ward cream strokes](Brush-Artist-Refs-02-Henry-Ward-cream-strokes.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 14 % → 13 % | 40.8 px | 0.41 | 0.90 | 217 |
| heavy line | 15 % → 14 % | 43.9 px | 0.41 | 0.92 | 184 |
| pressure swell | 11 % → 11 % | 42.8 px | 0.41 | 0.94 | 138 |
| fast wave | 36 % → 18 % | 41.0 px | 0.40 | 0.50 | 534 |
| slow wave | 36 % → 18 % | 41.1 px | 0.40 | 0.49 | 864 |
| spiral | 58 % → 19 % | 38.1 px | 0.40 | 0.33 | 1138 |
| loop | 31 % → 20 % | 39.7 px | 0.40 | 0.64 | 707 |
| tilted | 13 % → 13 % | 36.9 px | 0.41 | 0.99 | 403 |
| over the wet one | 27 % → 23 % | 37.9 px | 0.41 | 0.86 | 365 |
| long, no reload | 67 % → 21 % | 30.1 px | 0.40 | 0.31 | 1545 | quarters: 0.01 → 0.01 → 0.01 → 0.02

Numbers say: light vs heavy: width 40.8 → 43.9 px, dark 0.41 → 0.41; pressure barely changes the width; the long stroke does not run out of paint.

## Brush Artist · Refs · #03 Henry Ward navy contours
Heavy acrylic · 22 px · 23.7 s

![Brush Artist · Refs · #03 Henry Ward navy contours](Brush-Artist-Refs-03-Henry-Ward-navy-contours.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 7 % → 7 % | 21.6 px | 0.70 | 0.94 | 151 |
| heavy line | 8 % → 8 % | 23.5 px | 0.70 | 0.95 | 131 |
| pressure swell | 6 % → 6 % | 23.2 px | 0.73 | 0.94 | 88 |
| fast wave | 19 % → 12 % | 21.8 px | 0.72 | 0.66 | 274 |
| slow wave | 19 % → 13 % | 22.5 px | 0.72 | 0.69 | 647 |
| spiral | 30 % → 13 % | 19.5 px | 0.72 | 0.45 | 834 |
| loop | 17 % → 13 % | 21.5 px | 0.72 | 0.81 | 396 |
| tilted | 8 % → 8 % | 22.6 px | 0.71 | 1.00 | 254 |
| over the wet one | 16 % → 14 % | 21.4 px | 0.71 | 0.89 | 185 |
| long, no reload | 34 % → 13 % | 15.1 px | 0.72 | 0.40 | 727 | quarters: 0.35 → 0.29 → 0.20 → 0.08

Numbers say: light vs heavy: width 21.6 → 23.5 px, dark 0.70 → 0.70; pressure barely changes the width.

## Brush Artist · Refs · #04 Henry Ward grey cloud
Gouache · 50 px · 47.4 s

![Brush Artist · Refs · #04 Henry Ward grey cloud](Brush-Artist-Refs-04-Henry-Ward-grey-cloud.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 16 % → 14 % | 46.7 px | 0.31 | 0.85 | 352 |
| heavy line | 17 % → 15 % | 50.2 px | 0.31 | 0.89 | 368 |
| pressure swell | 13 % → 12 % | 48.7 px | 0.31 | 0.91 | 244 |
| fast wave | 40 % → 20 % | 46.5 px | 0.31 | 0.50 | 700 |
| slow wave | 40 % → 20 % | 46.5 px | 0.31 | 0.49 | 1173 |
| spiral | 61 % → 21 % | 40.0 px | 0.31 | 0.34 | 1126 |
| loop | 35 % → 22 % | 45.2 px | 0.31 | 0.64 | 483 |
| tilted | 14 % → 14 % | 40.0 px | 0.31 | 0.99 | 499 |
| over the wet one | 30 % → 26 % | 42.8 px | 0.31 | 0.87 | 371 |
| long, no reload | 73 % → 23 % | 32.7 px | 0.31 | 0.31 | 1577 | quarters: 0.01 → 0.01 → 0.01 → 0.02

Numbers say: light vs heavy: width 46.7 → 50.2 px, dark 0.31 → 0.31; pressure barely changes the width; the long stroke does not run out of paint.

## Brush Artist · Refs · #05 Henry Ward green in rust loops
Heavy acrylic · 20 px · 17.4 s

![Brush Artist · Refs · #05 Henry Ward green in rust loops](Brush-Artist-Refs-05-Henry-Ward-green-in-rust-loops.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 7 % → 6 % | 19.5 px | 0.55 | 0.94 | 134 |
| heavy line | 7 % → 7 % | 21.4 px | 0.55 | 0.94 | 111 |
| pressure swell | 6 % → 5 % | 21.5 px | 0.57 | 0.92 | 83 |
| fast wave | 17 % → 11 % | 19.8 px | 0.56 | 0.64 | 316 |
| slow wave | 18 % → 12 % | 20.4 px | 0.56 | 0.66 | 473 |
| spiral | 27 % → 11 % | 17.9 px | 0.55 | 0.42 | 371 |
| loop | 15 % → 12 % | 19.5 px | 0.55 | 0.80 | 183 |
| tilted | 8 % → 8 % | 21.7 px | 0.56 | 1.00 | 102 |
| over the wet one | 15 % → 13 % | 19.3 px | 0.56 | 0.87 | 121 |
| long, no reload | 30 % → 12 % | 13.4 px | 0.56 | 0.39 | 560 | quarters: 0.25 → 0.18 → 0.10 → 0.02

Numbers say: light vs heavy: width 19.5 → 21.4 px, dark 0.55 → 0.55; pressure barely changes the width.

## Brush Artist · Refs · #06 Henry Ward scrubbed grey
Gouache · 50 px · 42.6 s

![Brush Artist · Refs · #06 Henry Ward scrubbed grey](Brush-Artist-Refs-06-Henry-Ward-scrubbed-grey.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 16 % → 14 % | 46.7 px | 0.33 | 0.85 | 250 |
| heavy line | 17 % → 15 % | 50.2 px | 0.33 | 0.89 | 260 |
| pressure swell | 13 % → 12 % | 48.7 px | 0.33 | 0.91 | 174 |
| fast wave | 40 % → 20 % | 46.5 px | 0.33 | 0.50 | 485 |
| slow wave | 40 % → 20 % | 46.5 px | 0.33 | 0.49 | 969 |
| spiral | 61 % → 21 % | 40.0 px | 0.33 | 0.34 | 1379 |
| loop | 35 % → 22 % | 45.2 px | 0.32 | 0.64 | 463 |
| tilted | 14 % → 14 % | 40.0 px | 0.33 | 0.99 | 240 |
| over the wet one | 30 % → 26 % | 42.8 px | 0.33 | 0.87 | 193 |
| long, no reload | 73 % → 23 % | 32.7 px | 0.32 | 0.31 | 1282 | quarters: 0.01 → 0.01 → 0.01 → 0.02

Numbers say: light vs heavy: width 46.7 → 50.2 px, dark 0.33 → 0.33; pressure barely changes the width; the long stroke does not run out of paint.

## Brush Artist · Refs · #07 Henry Ward blue L + black zigzag
Heavy acrylic · 34 px · 21.2 s

![Brush Artist · Refs · #07 Henry Ward blue L + black zigzag](Brush-Artist-Refs-07-Henry-Ward-blue-L-black-zigzag.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 11 % → 11 % | 33.2 px | 0.57 | 0.93 | 117 |
| heavy line | 12 % → 12 % | 35.8 px | 0.57 | 0.93 | 119 |
| pressure swell | 9 % → 9 % | 35.2 px | 0.59 | 0.94 | 75 |
| fast wave | 29 % → 20 % | 33.6 px | 0.59 | 0.69 | 345 |
| slow wave | 30 % → 21 % | 34.2 px | 0.58 | 0.72 | 569 |
| spiral | 47 % → 22 % | 31.3 px | 0.58 | 0.46 | 948 |
| loop | 25 % → 21 % | 32.7 px | 0.58 | 0.82 | 393 |
| tilted | 11 % → 11 % | 29.9 px | 0.58 | 1.00 | 160 |
| over the wet one | 22 % → 20 % | 31.8 px | 0.58 | 0.91 | 137 |
| long, no reload | 53 % → 22 % | 23.8 px | 0.59 | 0.42 | 961 | quarters: 0.40 → 0.32 → 0.21 → 0.10

Numbers say: light vs heavy: width 33.2 → 35.8 px, dark 0.57 → 0.57; pressure barely changes the width.

## Brush Artist · Refs · #08 Henry Ward olive bands
Gouache · 34 px · 27.3 s

![Brush Artist · Refs · #08 Henry Ward olive bands](Brush-Artist-Refs-08-Henry-Ward-olive-bands.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 8 % → 2 % | 24.7 px | 0.57 | 0.27 | 93 |
| heavy line | 12 % → 3 % | 33.9 px | 0.57 | 0.22 | 173 |
| pressure swell | 8 % → 3 % | 30.8 px | 0.57 | 0.38 | 95 |
| fast wave | 25 % → 4 % | 29.2 px | 0.57 | 0.15 | 493 |
| slow wave | 25 % → 4 % | 28.9 px | 0.57 | 0.15 | 1046 |
| spiral | 39 % → 4 % | 25.7 px | 0.57 | 0.10 | 569 |
| loop | 22 % → 5 % | 28.8 px | 0.57 | 0.21 | 254 |
| tilted | 10 % → 10 % | 28.6 px | 0.57 | 0.98 | 130 |
| over the wet one | 20 % → 8 % | 28.3 px | 0.57 | 0.40 | 127 |
| long, no reload | 45 % → 6 % | 20.0 px | 0.57 | 0.13 | 860 | quarters: 0.35 → 0.27 → 0.17 → 0.08

Numbers say: light vs heavy: width 24.7 → 33.9 px, dark 0.57 → 0.57.

## Brush Artist · Refs · #09 Henry Ward white loops
Gouache · 46 px · 41.4 s

![Brush Artist · Refs · #09 Henry Ward white loops](Brush-Artist-Refs-09-Henry-Ward-white-loops.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 14 % → 13 % | 40.8 px | 0.43 | 0.90 | 191 |
| heavy line | 15 % → 14 % | 43.9 px | 0.43 | 0.92 | 158 |
| pressure swell | 11 % → 11 % | 42.8 px | 0.44 | 0.94 | 115 |
| fast wave | 36 % → 18 % | 41.0 px | 0.43 | 0.50 | 504 |
| slow wave | 36 % → 18 % | 41.1 px | 0.43 | 0.49 | 705 |
| spiral | 58 % → 19 % | 38.1 px | 0.42 | 0.33 | 787 |
| loop | 31 % → 20 % | 39.7 px | 0.42 | 0.64 | 502 |
| tilted | 13 % → 13 % | 36.9 px | 0.43 | 0.99 | 217 |
| over the wet one | 27 % → 23 % | 37.9 px | 0.43 | 0.86 | 186 |
| long, no reload | 67 % → 21 % | 30.1 px | 0.42 | 0.31 | 1098 | quarters: 0.01 → 0.01 → 0.01 → 0.02

Numbers say: light vs heavy: width 40.8 → 43.9 px, dark 0.43 → 0.43; pressure barely changes the width; the long stroke does not run out of paint.

## Brush Artist · Refs · #10 Henry Ward maroon loops
Heavy acrylic · 30 px · 18.2 s

![Brush Artist · Refs · #10 Henry Ward maroon loops](Brush-Artist-Refs-10-Henry-Ward-maroon-loops.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 10 % → 9 % | 28.0 px | 0.71 | 0.94 | 113 |
| heavy line | 10 % → 10 % | 30.3 px | 0.71 | 0.95 | 114 |
| pressure swell | 8 % → 8 % | 30.0 px | 0.73 | 0.94 | 63 |
| fast wave | 25 % → 17 % | 28.3 px | 0.73 | 0.71 | 292 |
| slow wave | 25 % → 18 % | 29.0 px | 0.73 | 0.73 | 419 |
| spiral | 39 % → 18 % | 26.0 px | 0.72 | 0.47 | 602 |
| loop | 21 % → 18 % | 27.6 px | 0.72 | 0.85 | 315 |
| tilted | 10 % → 10 % | 27.9 px | 0.72 | 1.00 | 168 |
| over the wet one | 20 % → 18 % | 27.0 px | 0.72 | 0.91 | 127 |
| long, no reload | 46 % → 18 % | 20.6 px | 0.73 | 0.40 | 581 | quarters: 0.44 → 0.38 → 0.31 → 0.22

Numbers say: light vs heavy: width 28.0 → 30.3 px, dark 0.71 → 0.71; pressure barely changes the width.

## Brush Artist · Refs · #11 Henry Ward purple spun balls
Heavy acrylic · 36 px · 22.8 s

![Brush Artist · Refs · #11 Henry Ward purple spun balls](Brush-Artist-Refs-11-Henry-Ward-purple-spun-balls.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 12 % → 11 % | 34.2 px | 0.71 | 0.96 | 123 |
| heavy line | 13 % → 12 % | 36.7 px | 0.71 | 0.95 | 122 |
| pressure swell | 10 % → 9 % | 36.2 px | 0.74 | 0.95 | 110 |
| fast wave | 30 % → 23 % | 34.6 px | 0.73 | 0.75 | 305 |
| slow wave | 30 % → 24 % | 35.0 px | 0.73 | 0.79 | 811 |
| spiral | 49 % → 25 % | 32.3 px | 0.73 | 0.50 | 805 |
| loop | 26 % → 23 % | 33.4 px | 0.73 | 0.88 | 347 |
| tilted | 11 % → 11 % | 31.2 px | 0.72 | 1.00 | 173 |
| over the wet one | 23 % → 21 % | 32.3 px | 0.72 | 0.93 | 135 |
| long, no reload | 55 % → 24 % | 24.8 px | 0.73 | 0.44 | 964 | quarters: 0.51 → 0.46 → 0.39 → 0.28

Numbers say: light vs heavy: width 34.2 → 36.7 px, dark 0.71 → 0.71; pressure barely changes the width.

## Brush Artist · Refs · #12 Henry Ward black-olive cage
Gouache · 28 px · 30.8 s

![Brush Artist · Refs · #12 Henry Ward black-olive cage](Brush-Artist-Refs-12-Henry-Ward-black-olive-cage.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 7 % → 3 % | 20.9 px | 0.61 | 0.35 | 70 |
| heavy line | 9 % → 4 % | 26.1 px | 0.61 | 0.41 | 180 |
| pressure swell | 6 % → 4 % | 23.9 px | 0.61 | 0.61 | 87 |
| fast wave | 20 % → 4 % | 23.7 px | 0.61 | 0.19 | 298 |
| slow wave | 20 % → 4 % | 23.3 px | 0.61 | 0.21 | 527 |
| spiral | 32 % → 4 % | 21.4 px | 0.61 | 0.14 | 513 |
| loop | 18 % → 5 % | 22.8 px | 0.61 | 0.28 | 257 |
| tilted | 9 % → 9 % | 25.4 px | 0.61 | 0.98 | 131 |
| over the wet one | 17 % → 8 % | 21.8 px | 0.61 | 0.46 | 97 |
| long, no reload | 39 % → 6 % | 17.6 px | 0.61 | 0.15 | 1053 | quarters: 0.31 → 0.26 → 0.19 → 0.10

Numbers say: light vs heavy: width 20.9 → 26.1 px, dark 0.61 → 0.61.

## Brush Artist · Refs · #13 Henry Ward blue streaky form
Gouache · 50 px · 45.2 s

![Brush Artist · Refs · #13 Henry Ward blue streaky form](Brush-Artist-Refs-13-Henry-Ward-blue-streaky-form.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 16 % → 14 % | 46.7 px | 0.33 | 0.85 | 314 |
| heavy line | 17 % → 15 % | 50.2 px | 0.33 | 0.89 | 253 |
| pressure swell | 13 % → 12 % | 48.7 px | 0.33 | 0.91 | 170 |
| fast wave | 40 % → 20 % | 46.5 px | 0.33 | 0.50 | 611 |
| slow wave | 40 % → 20 % | 46.5 px | 0.33 | 0.49 | 1179 |
| spiral | 61 % → 21 % | 40.0 px | 0.32 | 0.34 | 893 |
| loop | 35 % → 22 % | 45.2 px | 0.32 | 0.64 | 517 |
| tilted | 14 % → 14 % | 40.0 px | 0.33 | 0.99 | 209 |
| over the wet one | 30 % → 26 % | 42.8 px | 0.33 | 0.87 | 198 |
| long, no reload | 73 % → 23 % | 32.7 px | 0.32 | 0.31 | 1403 | quarters: 0.01 → 0.01 → 0.01 → 0.02

Numbers say: light vs heavy: width 46.7 → 50.2 px, dark 0.33 → 0.33; pressure barely changes the width; the long stroke does not run out of paint.

## Brush Artist · Refs · #14 Henry Ward olive totem
Heavy acrylic · 48 px · 25.5 s

![Brush Artist · Refs · #14 Henry Ward olive totem](Brush-Artist-Refs-14-Henry-Ward-olive-totem.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 15 % → 15 % | 44.8 px | 0.31 | 0.94 | 209 |
| heavy line | 16 % → 16 % | 47.7 px | 0.31 | 0.95 | 194 |
| pressure swell | 13 % → 12 % | 47.0 px | 0.32 | 0.95 | 120 |
| fast wave | 38 % → 30 % | 43.9 px | 0.30 | 0.79 | 544 |
| slow wave | 39 % → 31 % | 44.6 px | 0.30 | 0.81 | 1042 |
| spiral | 58 % → 32 % | 38.2 px | 0.30 | 0.55 | 1001 |
| loop | 33 % → 29 % | 42.7 px | 0.30 | 0.89 | 419 |
| tilted | 13 % → 13 % | 37.5 px | 0.31 | 1.00 | 196 |
| over the wet one | 28 % → 26 % | 41.2 px | 0.31 | 0.93 | 195 |
| long, no reload | 68 % → 33 % | 30.3 px | 0.30 | 0.49 | 1194 | quarters: 0.25 → 0.18 → 0.10 → 0.03

Numbers say: light vs heavy: width 44.8 → 47.7 px, dark 0.31 → 0.31; pressure barely changes the width.

## Brush Artist · Refs · #15 Ultramarine brush script
Ink · 4 px · 29.5 s

![Brush Artist · Refs · #15 Ultramarine brush script](Brush-Artist-Refs-15-Ultramarine-brush-script.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 1 % → 3 % | 2.2 px | 0.55 | 3.86 | 39 |
| heavy line | 6 % → 6 % | 16.6 px | 0.58 | 0.99 | 57 |
| pressure swell | 3 % → 4 % | 12.0 px | 0.64 | 1.15 | 43 |
| fast wave | 9 % → 7 % | 10.5 px | 0.55 | 0.82 | 93 |
| slow wave | 7 % → 7 % | 8.4 px | 0.54 | 0.93 | 130 |
| spiral | 11 % → 7 % | 7.2 px | 0.52 | 0.68 | 250 |
| loop | 7 % → 7 % | 9.2 px | 0.53 | 0.99 | 162 |
| tilted | 3 % → 3 % | 8.0 px | 0.62 | 1.02 | 62 |
| over the wet one | 7 % → 7 % | 11.4 px | 0.62 | 1.05 | 48 |
| long, no reload | 16 % → 8 % | 7.3 px | 0.50 | 0.49 | 262 | quarters: 0.14 → 0.04 → 0.01 → 0.00

Numbers say: light vs heavy: width 2.2 → 16.6 px, dark 0.55 → 0.58; wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #18 Blue oil-stick scribbles
Pastel · 10 px · 12.7 s

![Brush Artist · Refs · #18 Blue oil-stick scribbles](Brush-Artist-Refs-18-Blue-oil-stick-scribbles.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 1 % → 1 % | 2.9 px | 0.52 | 1.00 | 69 |
| heavy line | 2 % → 2 % | 5.5 px | 0.53 | 1.00 | 56 |
| pressure swell | 1 % → 1 % | 5.0 px | 0.53 | 1.00 | 27 |
| fast wave | 4 % → 4 % | 4.8 px | 0.53 | 1.00 | 64 |
| slow wave | 4 % → 4 % | 4.4 px | 0.53 | 1.00 | 74 |
| spiral | 7 % → 7 % | 4.5 px | 0.52 | 1.00 | 123 |
| loop | 3 % → 3 % | 4.5 px | 0.52 | 1.00 | 80 |
| tilted | 2 % → 2 % | 4.7 px | 0.53 | 1.00 | 46 |
| over the wet one | 3 % → 3 % | 4.7 px | 0.53 | 1.00 | 39 |
| long, no reload | 10 % → 10 % | 4.4 px | 0.53 | 1.00 | 287 | quarters: 0.06 → 0.06 → 0.06 → 0.06

Numbers say: light vs heavy: width 2.9 → 5.5 px, dark 0.52 → 0.53; the long stroke does not run out of paint.

## Brush Artist · Refs · #20 Orange-red crayon scribble
Pastel · 14 px · 12.1 s

![Brush Artist · Refs · #20 Orange-red crayon scribble](Brush-Artist-Refs-20-Orange-red-crayon-scribble.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 1 % → 1 % | 4.0 px | 0.53 | 1.00 | 23 |
| heavy line | 3 % → 3 % | 8.0 px | 0.53 | 1.00 | 26 |
| pressure swell | 2 % → 2 % | 7.6 px | 0.53 | 1.00 | 19 |
| fast wave | 6 % → 6 % | 7.2 px | 0.53 | 1.00 | 80 |
| slow wave | 6 % → 6 % | 6.6 px | 0.53 | 1.00 | 72 |
| spiral | 9 % → 9 % | 6.2 px | 0.53 | 1.00 | 153 |
| loop | 5 % → 5 % | 6.2 px | 0.53 | 1.00 | 76 |
| tilted | 2 % → 2 % | 5.6 px | 0.53 | 1.00 | 43 |
| over the wet one | 4 % → 4 % | 6.6 px | 0.53 | 1.00 | 27 |
| long, no reload | 13 % → 13 % | 5.7 px | 0.53 | 1.00 | 262 | quarters: 0.07 → 0.07 → 0.08 → 0.08

Numbers say: light vs heavy: width 4.0 → 8.0 px, dark 0.53 → 0.53; the long stroke does not run out of paint.

## Brush Artist · Refs · #21 Gritty black contours
Gouache · 12 px · 22.7 s

![Brush Artist · Refs · #21 Gritty black contours](Brush-Artist-Refs-21-Gritty-black-contours.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 3 % → 0 % | 8.8 px | 0.79 | 0.12 | 69 |
| heavy line | 4 % → 0 % | 11.9 px | 0.79 | 0.10 | 220 |
| pressure swell | 3 % → 0 % | 11.6 px | 0.79 | 0.15 | 113 |
| fast wave | 7 % → 1 % | 8.5 px | 0.79 | 0.10 | 259 |
| slow wave | 8 % → 1 % | 9.0 px | 0.79 | 0.09 | 241 |
| spiral | 9 % → 1 % | 6.0 px | 0.79 | 0.10 | 397 |
| loop | 8 % → 1 % | 9.9 px | 0.79 | 0.09 | 184 |
| tilted | 4 % → 4 % | 10.8 px | 0.79 | 0.90 | 126 |
| over the wet one | 7 % → 1 % | 9.7 px | 0.79 | 0.17 | 86 |
| long, no reload | 7 % → 1 % | 3.3 px | 0.79 | 0.12 | 531 | quarters: 0.20 → 0.07 → 0.00 → 0.00

Numbers say: light vs heavy: width 8.8 → 11.9 px, dark 0.79 → 0.79.

## Brush Artist · Refs · #22 Bold black brush poster
Ink · 20 px · 29.5 s

![Brush Artist · Refs · #22 Bold black brush poster](Brush-Artist-Refs-22-Bold-black-brush-poster.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 3 % → 5 % | 9.5 px | 0.79 | 1.63 | 50 |
| heavy line | 15 % → 15 % | 44.6 px | 0.88 | 0.99 | 127 |
| pressure swell | 9 % → 9 % | 31.9 px | 0.87 | 1.04 | 79 |
| fast wave | 27 % → 26 % | 31.2 px | 0.87 | 0.98 | 244 |
| slow wave | 22 % → 21 % | 25.2 px | 0.87 | 0.98 | 265 |
| spiral | 34 % → 32 % | 22.2 px | 0.87 | 0.94 | 257 |
| loop | 20 % → 20 % | 26.2 px | 0.88 | 1.00 | 132 |
| tilted | 8 % → 8 % | 22.7 px | 0.88 | 1.01 | 67 |
| over the wet one | 19 % → 19 % | 30.5 px | 0.88 | 1.00 | 63 |
| long, no reload | 45 % → 38 % | 20.2 px | 0.86 | 0.84 | 534 | quarters: 0.54 → 0.45 → 0.35 → 0.27

Numbers say: light vs heavy: width 9.5 → 44.6 px, dark 0.79 → 0.88; wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #23 Dry white on orange + black line
Gouache · 50 px · 26.7 s

![Brush Artist · Refs · #23 Dry white on orange + black line](Brush-Artist-Refs-23-Dry-white-on-orange-black-line.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 12 % → 2 % | 35.1 px | 0.39 | 0.13 | 114 |
| heavy line | 16 % → 2 % | 46.9 px | 0.39 | 0.11 | 271 |
| pressure swell | 11 % → 2 % | 42.6 px | 0.39 | 0.19 | 124 |
| fast wave | 34 % → 3 % | 39.7 px | 0.39 | 0.09 | 457 |
| slow wave | 34 % → 3 % | 39.0 px | 0.39 | 0.10 | 1045 |
| spiral | 49 % → 4 % | 32.6 px | 0.38 | 0.07 | 732 |
| loop | 30 % → 4 % | 39.1 px | 0.38 | 0.12 | 355 |
| tilted | 13 % → 12 % | 34.9 px | 0.38 | 0.98 | 204 |
| over the wet one | 26 % → 7 % | 38.0 px | 0.38 | 0.27 | 194 |
| long, no reload | 58 % → 5 % | 26.1 px | 0.38 | 0.09 | 1035 | quarters: 0.02 → 0.02 → 0.03 → 0.04

Numbers say: light vs heavy: width 35.1 → 46.9 px, dark 0.39 → 0.39; the long stroke does not run out of paint.

## Brush Artist · Refs · #24 Picasso flat oil
Oil · 34 px · 17.1 s

![Brush Artist · Refs · #24 Picasso flat oil](Brush-Artist-Refs-24-Picasso-flat-oil.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 11 % → 11 % | 32.4 px | 0.40 | 1.00 | 116 |
| heavy line | 12 % → 12 % | 35.2 px | 0.40 | 1.00 | 122 |
| pressure swell | 9 % → 9 % | 34.4 px | 0.41 | 1.00 | 96 |
| fast wave | 30 % → 30 % | 34.2 px | 0.41 | 1.00 | 328 |
| slow wave | 30 % → 30 % | 35.0 px | 0.41 | 1.00 | 887 |
| spiral | 51 % → 51 % | 33.8 px | 0.40 | 1.00 | 928 |
| loop | 25 % → 25 % | 32.6 px | 0.41 | 1.00 | 306 |
| tilted | 11 % → 11 % | 32.0 px | 0.41 | 1.00 | 172 |
| over the wet one | 23 % → 23 % | 30.8 px | 0.41 | 1.00 | 153 |
| long, no reload | 62 % → 62 % | 27.6 px | 0.39 | 1.00 | 784 | quarters: 0.28 → 0.28 → 0.26 → 0.24

Numbers say: light vs heavy: width 32.4 → 35.2 px, dark 0.40 → 0.40; pressure barely changes the width.

## Brush Artist · Refs · #25 Yellow heavy flat stroke
Heavy acrylic · 110 px · 38.7 s

![Brush Artist · Refs · #25 Yellow heavy flat stroke](Brush-Artist-Refs-25-Yellow-heavy-flat-stroke.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 35 % → 36 % | 101.5 px | 0.30 | 1.02 | 407 |
| heavy line | 36 % → 35 % | 105.1 px | 0.31 | 0.97 | 424 |
| pressure swell | 28 % → 29 % | 105.4 px | 0.30 | 1.04 | 288 |
| fast wave | 73 % → 76 % | 83.8 px | 0.31 | 1.05 | 1246 |
| slow wave | 73 % → 72 % | 84.7 px | 0.30 | 0.98 | 2030 |
| spiral | 86 % → 83 % | 56.7 px | 0.29 | 0.97 | 2394 |
| loop | 65 % → 64 % | 83.6 px | 0.31 | 0.99 | 1051 |
| tilted | 26 % → 26 % | 71.5 px | 0.30 | 1.00 | 542 |
| over the wet one | 55 % → 54 % | 83.2 px | 0.30 | 0.97 | 539 |
| long, no reload | 98 % → 97 % | 44.1 px | 0.29 | 0.99 | 2485 | quarters: 0.00 → 0.00 → 0.00 → 0.00

Numbers say: light vs heavy: width 101.5 → 105.1 px, dark 0.30 → 0.31; pressure barely changes the width; the long stroke does not run out of paint.

## Brush Artist · Refs · #27 Orange impasto swatch
Heavy acrylic · 60 px · 26.1 s

![Brush Artist · Refs · #27 Orange impasto swatch](Brush-Artist-Refs-27-Orange-impasto-swatch.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 20 % → 19 % | 56.8 px | 0.34 | 0.97 | 212 |
| heavy line | 20 % → 20 % | 59.5 px | 0.34 | 0.97 | 199 |
| pressure swell | 16 % → 15 % | 59.6 px | 0.36 | 0.97 | 170 |
| fast wave | 48 % → 46 % | 55.0 px | 0.35 | 0.98 | 836 |
| slow wave | 48 % → 47 % | 55.9 px | 0.35 | 0.98 | 1204 |
| spiral | 69 % → 62 % | 45.5 px | 0.34 | 0.91 | 1002 |
| loop | 42 % → 40 % | 53.9 px | 0.35 | 0.97 | 536 |
| tilted | 16 % → 16 % | 44.0 px | 0.35 | 1.00 | 238 |
| over the wet one | 34 % → 33 % | 50.9 px | 0.35 | 0.96 | 272 |
| long, no reload | 85 % → 75 % | 38.1 px | 0.35 | 0.88 | 1186 | quarters: 0.33 → 0.31 → 0.29 → 0.26

Numbers say: light vs heavy: width 56.8 → 59.5 px, dark 0.34 → 0.34; pressure barely changes the width.

## Brush Artist · Refs · #28 Miles Davis black lines
Ink · 22 px · 28.9 s

![Brush Artist · Refs · #28 Miles Davis black lines](Brush-Artist-Refs-28-Miles-Davis-black-lines.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 4 % → 6 % | 12.2 px | 0.81 | 1.48 | 53 |
| heavy line | 17 % → 17 % | 49.1 px | 0.88 | 0.99 | 91 |
| pressure swell | 10 % → 10 % | 35.9 px | 0.87 | 1.03 | 51 |
| fast wave | 30 % → 30 % | 35.0 px | 0.87 | 0.98 | 165 |
| slow wave | 25 % → 25 % | 28.5 px | 0.87 | 0.99 | 285 |
| spiral | 38 % → 37 % | 25.3 px | 0.87 | 0.96 | 338 |
| loop | 23 % → 23 % | 29.4 px | 0.88 | 1.00 | 141 |
| tilted | 9 % → 9 % | 25.0 px | 0.88 | 1.01 | 74 |
| over the wet one | 21 % → 21 % | 34.1 px | 0.88 | 1.00 | 60 |
| long, no reload | 51 % → 43 % | 22.7 px | 0.86 | 0.85 | 376 | quarters: 0.59 → 0.51 → 0.40 → 0.31

Numbers say: light vs heavy: width 12.2 → 49.1 px, dark 0.81 → 0.88.

## Brush Artist · Refs · #29 Shrigley magenta asterisk
Watercolor · 70 px · 31.3 s

![Brush Artist · Refs · #29 Shrigley magenta asterisk](Brush-Artist-Refs-29-Shrigley-magenta-asterisk.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 10 % → 13 % | 28.0 px | 0.65 | 1.36 | 69 |
| heavy line | 17 % → 18 % | 50.3 px | 0.64 | 1.03 | 166 |
| pressure swell | 11 % → 12 % | 41.1 px | 0.65 | 1.13 | 106 |
| fast wave | 38 % → 38 % | 43.7 px | 0.64 | 1.00 | 272 |
| slow wave | 35 % → 39 % | 41.0 px | 0.65 | 1.10 | 422 |
| spiral | 61 % → 61 % | 40.0 px | 0.64 | 1.01 | 412 |
| loop | 31 % → 32 % | 40.2 px | 0.65 | 1.03 | 224 |
| tilted | 18 % → 18 % | 49.0 px | 0.65 | 1.00 | 199 |
| over the wet one | 31 % → 34 % | 38.4 px | 0.65 | 1.07 | 110 |
| long, no reload | 75 % → 75 % | 33.5 px | 0.64 | 1.00 | 727 | quarters: 0.55 → 0.53 → 0.52 → 0.49

Numbers say: light vs heavy: width 28.0 → 50.3 px, dark 0.65 → 0.64; the long stroke does not run out of paint.

## Brush Artist · Refs · #30 Red gouache face patch
Gouache · 60 px · 35.3 s

![Brush Artist · Refs · #30 Red gouache face patch](Brush-Artist-Refs-30-Red-gouache-face-patch.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 16 % → 15 % | 46.9 px | 0.49 | 0.91 | 140 |
| heavy line | 25 % → 20 % | 73.8 px | 0.49 | 0.80 | 260 |
| pressure swell | 19 % → 17 % | 72.6 px | 0.49 | 0.86 | 143 |
| fast wave | 48 % → 28 % | 55.1 px | 0.49 | 0.58 | 420 |
| slow wave | 48 % → 28 % | 55.3 px | 0.49 | 0.59 | 820 |
| spiral | 59 % → 28 % | 39.1 px | 0.49 | 0.48 | 948 |
| loop | 40 % → 29 % | 51.3 px | 0.49 | 0.74 | 369 |
| tilted | 16 % → 16 % | 45.7 px | 0.49 | 1.01 | 211 |
| over the wet one | 36 % → 32 % | 55.3 px | 0.49 | 0.88 | 164 |
| long, no reload | 67 % → 30 % | 30.0 px | 0.49 | 0.45 | 1005 | quarters: 0.43 → 0.38 → 0.32 → 0.26

Numbers say: light vs heavy: width 46.9 → 73.8 px, dark 0.49 → 0.49.

## Brush Artist · Refs · #31 Warhol blotted line
Ink · 6 px · 20.7 s

![Brush Artist · Refs · #31 Warhol blotted line](Brush-Artist-Refs-31-Warhol-blotted-line.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 1 % → 3 % | 2.6 px | 0.75 | 3.30 | 36 |
| heavy line | 7 % → 7 % | 20.6 px | 0.83 | 0.97 | 61 |
| pressure swell | 4 % → 4 % | 14.8 px | 0.84 | 1.12 | 35 |
| fast wave | 12 % → 9 % | 13.8 px | 0.82 | 0.77 | 109 |
| slow wave | 10 % → 8 % | 11.2 px | 0.80 | 0.85 | 116 |
| spiral | 15 % → 9 % | 9.7 px | 0.80 | 0.58 | 218 |
| loop | 9 % → 9 % | 11.9 px | 0.80 | 0.94 | 180 |
| tilted | 3 % → 3 % | 8.6 px | 0.84 | 1.04 | 60 |
| over the wet one | 8 % → 8 % | 14.5 px | 0.84 | 1.02 | 61 |
| long, no reload | 21 % → 9 % | 9.6 px | 0.78 | 0.43 | 285 | quarters: 0.25 → 0.13 → 0.05 → 0.01

Numbers say: light vs heavy: width 2.6 → 20.6 px, dark 0.75 → 0.83; wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #32 Thick orange swipes
Heavy acrylic · 90 px · 29.6 s

![Brush Artist · Refs · #32 Thick orange swipes](Brush-Artist-Refs-32-Thick-orange-swipes.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 29 % → 29 % | 83.1 px | 0.38 | 1.00 | 294 |
| heavy line | 30 % → 29 % | 86.4 px | 0.38 | 0.97 | 280 |
| pressure swell | 23 % → 23 % | 86.5 px | 0.38 | 1.01 | 202 |
| fast wave | 63 % → 65 % | 73.1 px | 0.38 | 1.03 | 726 |
| slow wave | 64 % → 63 % | 73.5 px | 0.38 | 0.98 | 1264 |
| spiral | 79 % → 77 % | 52.2 px | 0.38 | 0.98 | 1227 |
| loop | 57 % → 56 % | 73.4 px | 0.38 | 0.99 | 630 |
| tilted | 21 % → 21 % | 59.3 px | 0.38 | 1.00 | 454 |
| over the wet one | 47 % → 45 % | 71.0 px | 0.38 | 0.97 | 404 |
| long, no reload | 95 % → 93 % | 42.8 px | 0.38 | 0.97 | 1706 | quarters: 0.38 → 0.38 → 0.37 → 0.35

Numbers say: light vs heavy: width 83.1 → 86.4 px, dark 0.38 → 0.38; pressure barely changes the width; the long stroke does not run out of paint.

## Brush Artist · Refs · #33 Red wet-in-wet band
Watercolor · 80 px · 45.7 s

![Brush Artist · Refs · #33 Red wet-in-wet band](Brush-Artist-Refs-33-Red-wet-in-wet-band.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 19 % → 30 % | 55.6 px | 0.59 | 1.58 | 111 |
| heavy line | 29 % → 38 % | 83.7 px | 0.59 | 1.33 | 202 |
| pressure swell | 19 % → 27 % | 71.5 px | 0.61 | 1.40 | 123 |
| fast wave | 58 % → 73 % | 67.4 px | 0.61 | 1.26 | 392 |
| slow wave | 57 % → 71 % | 65.7 px | 0.63 | 1.25 | 680 |
| spiral | 75 % → 84 % | 49.5 px | 0.64 | 1.12 | 867 |
| loop | 51 % → 62 % | 66.4 px | 0.63 | 1.21 | 337 |
| tilted | 24 % → 25 % | 66.3 px | 0.60 | 1.03 | 253 |
| over the wet one | 48 % → 66 % | 66.6 px | 0.60 | 1.38 | 168 |
| long, no reload | 95 % → 99 % | 42.4 px | 0.66 | 1.05 | 1056 | quarters: 0.68 → 0.68 → 0.68 → 0.63

Numbers say: light vs heavy: width 55.6 → 83.7 px, dark 0.59 → 0.59; the long stroke does not run out of paint; wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #34 Magenta oil patches
Oil · 60 px · 22.2 s

![Brush Artist · Refs · #34 Magenta oil patches](Brush-Artist-Refs-34-Magenta-oil-patches.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 19 % → 19 % | 55.8 px | 0.61 | 1.00 | 189 |
| heavy line | 21 % → 21 % | 59.9 px | 0.61 | 1.00 | 230 |
| pressure swell | 16 % → 16 % | 58.9 px | 0.62 | 1.01 | 149 |
| fast wave | 48 % → 49 % | 55.4 px | 0.62 | 1.02 | 527 |
| slow wave | 48 % → 48 % | 55.8 px | 0.62 | 1.00 | 905 |
| spiral | 70 % → 70 % | 46.3 px | 0.62 | 1.00 | 936 |
| loop | 42 % → 42 % | 54.3 px | 0.62 | 1.00 | 465 |
| tilted | 17 % → 17 % | 46.8 px | 0.61 | 1.00 | 244 |
| over the wet one | 35 % → 35 % | 50.1 px | 0.61 | 1.00 | 213 |
| long, no reload | 86 % → 86 % | 38.7 px | 0.62 | 1.00 | 1765 | quarters: 0.59 → 0.58 → 0.57 → 0.52

Numbers say: light vs heavy: width 55.8 → 59.9 px, dark 0.61 → 0.61; pressure barely changes the width; the long stroke does not run out of paint.

## Brush Artist · Refs · #35 Red band with runs
Watercolor · 70 px · 55.0 s

![Brush Artist · Refs · #35 Red band with runs](Brush-Artist-Refs-35-Red-band-with-runs.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 17 % → 32 % | 48.3 px | 0.49 | 1.91 | 87 |
| heavy line | 25 % → 39 % | 73.9 px | 0.51 | 1.55 | 171 |
| pressure swell | 17 % → 25 % | 63.0 px | 0.55 | 1.47 | 174 |
| fast wave | 54 % → 72 % | 61.8 px | 0.52 | 1.34 | 770 |
| slow wave | 52 % → 70 % | 59.8 px | 0.55 | 1.35 | 568 |
| spiral | 72 % → 88 % | 47.3 px | 0.56 | 1.22 | 546 |
| loop | 47 % → 68 % | 61.0 px | 0.53 | 1.44 | 275 |
| tilted | 21 % → 22 % | 57.7 px | 0.51 | 1.06 | 203 |
| over the wet one | 43 % → 67 % | 62.0 px | 0.51 | 1.57 | 138 |
| long, no reload | 92 % → 98 % | 41.3 px | 0.59 | 1.07 | 804 | quarters: 0.60 → 0.60 → 0.59 → 0.56

Numbers say: light vs heavy: width 48.3 → 73.9 px, dark 0.49 → 0.51; the long stroke does not run out of paint; wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #36 Magenta letters flat brush
Gouache · 36 px · 39.5 s

![Brush Artist · Refs · #36 Magenta letters flat brush](Brush-Artist-Refs-36-Magenta-letters-flat-brush.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 10 % → 10 % | 29.0 px | 0.45 | 0.98 | 78 |
| heavy line | 17 % → 14 % | 49.1 px | 0.45 | 0.85 | 101 |
| pressure swell | 13 % → 12 % | 49.4 px | 0.45 | 0.89 | 69 |
| fast wave | 35 % → 19 % | 40.3 px | 0.45 | 0.54 | 219 |
| slow wave | 35 % → 19 % | 39.9 px | 0.45 | 0.54 | 380 |
| spiral | 46 % → 19 % | 30.4 px | 0.45 | 0.42 | 369 |
| loop | 27 % → 20 % | 35.3 px | 0.45 | 0.72 | 190 |
| tilted | 11 % → 11 % | 29.8 px | 0.45 | 1.00 | 120 |
| over the wet one | 24 % → 22 % | 38.1 px | 0.45 | 0.92 | 92 |
| long, no reload | 46 % → 19 % | 20.8 px | 0.45 | 0.40 | 670 | quarters: 0.29 → 0.25 → 0.22 → 0.18

Numbers say: light vs heavy: width 29.0 → 49.1 px, dark 0.45 → 0.45.

## Brush Artist · Refs · #37 Oil still life dabs
Oil · 40 px · 21.7 s

![Brush Artist · Refs · #37 Oil still life dabs](Brush-Artist-Refs-37-Oil-still-life-dabs.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 13 % → 13 % | 38.0 px | 0.38 | 1.00 | 149 |
| heavy line | 14 % → 14 % | 41.1 px | 0.38 | 1.00 | 179 |
| pressure swell | 11 % → 11 % | 40.2 px | 0.40 | 1.00 | 115 |
| fast wave | 34 % → 34 % | 39.8 px | 0.39 | 1.00 | 460 |
| slow wave | 35 % → 35 % | 40.2 px | 0.39 | 1.00 | 825 |
| spiral | 59 % → 59 % | 38.7 px | 0.38 | 1.00 | 829 |
| loop | 29 % → 29 % | 37.8 px | 0.39 | 1.00 | 406 |
| tilted | 13 % → 13 % | 36.3 px | 0.39 | 1.00 | 216 |
| over the wet one | 26 % → 26 % | 35.8 px | 0.39 | 1.00 | 197 |
| long, no reload | 69 % → 69 % | 30.9 px | 0.37 | 1.00 | 1315 | quarters: 0.31 → 0.30 → 0.28 → 0.24

Numbers say: light vs heavy: width 38.0 → 41.1 px, dark 0.38 → 0.38; pressure barely changes the width.

## Brush Artist · Refs · #38 Sanguine drawing
Pastel · 6 px · 12.1 s

![Brush Artist · Refs · #38 Sanguine drawing](Brush-Artist-Refs-38-Sanguine-drawing.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 1 % → 1 % | 2.0 px | 0.61 | 1.00 | 62 |
| heavy line | 1 % → 1 % | 3.5 px | 0.62 | 1.00 | 61 |
| pressure swell | 1 % → 1 % | 3.3 px | 0.62 | 1.00 | 29 |
| fast wave | 3 % → 3 % | 3.2 px | 0.61 | 1.00 | 87 |
| slow wave | 3 % → 3 % | 3.0 px | 0.61 | 1.00 | 59 |
| spiral | 4 % → 4 % | 2.9 px | 0.61 | 1.00 | 76 |
| loop | 2 % → 2 % | 3.0 px | 0.61 | 1.00 | 46 |
| tilted | 1 % → 1 % | 3.4 px | 0.62 | 1.00 | 41 |
| over the wet one | 2 % → 2 % | 2.9 px | 0.62 | 1.00 | 23 |
| long, no reload | 7 % → 7 % | 3.0 px | 0.61 | 1.00 | 131 | quarters: 0.04 → 0.05 → 0.05 → 0.05

Numbers say: light vs heavy: width 2.0 → 3.5 px, dark 0.61 → 0.62; the long stroke does not run out of paint.

## Brush Artist · Refs · #39 Very thick impasto
Heavy acrylic · 60 px · 29.1 s

![Brush Artist · Refs · #39 Very thick impasto](Brush-Artist-Refs-39-Very-thick-impasto.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 20 % → 19 % | 56.9 px | 0.60 | 0.97 | 208 |
| heavy line | 21 % → 20 % | 59.6 px | 0.60 | 0.97 | 194 |
| pressure swell | 16 % → 15 % | 59.7 px | 0.62 | 0.97 | 156 |
| fast wave | 48 % → 47 % | 55.2 px | 0.62 | 0.98 | 649 |
| slow wave | 49 % → 47 % | 56.0 px | 0.62 | 0.98 | 1250 |
| spiral | 69 % → 65 % | 45.6 px | 0.62 | 0.93 | 888 |
| loop | 42 % → 41 % | 54.0 px | 0.62 | 0.97 | 478 |
| tilted | 16 % → 16 % | 44.0 px | 0.61 | 1.00 | 392 |
| over the wet one | 34 % → 33 % | 51.0 px | 0.61 | 0.97 | 309 |
| long, no reload | 85 % → 79 % | 38.3 px | 0.62 | 0.92 | 1399 | quarters: 0.58 → 0.57 → 0.55 → 0.52

Numbers say: light vs heavy: width 56.9 → 59.6 px, dark 0.60 → 0.60; pressure barely changes the width; the long stroke does not run out of paint.

## Brush Artist · Refs · #40 Watercolour blooms
Watercolor · 90 px · 62.9 s

![Brush Artist · Refs · #40 Watercolour blooms](Brush-Artist-Refs-40-Watercolour-blooms.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 22 % → 33 % | 63.3 px | 0.10 | 1.51 | 144 |
| heavy line | 33 % → 41 % | 94.9 px | 0.11 | 1.26 | 412 |
| pressure swell | 22 % → 30 % | 84.1 px | 0.12 | 1.33 | 214 |
| fast wave | 64 % → 78 % | 73.9 px | 0.11 | 1.22 | 503 |
| slow wave | 63 % → 75 % | 72.3 px | 0.16 | 1.20 | 868 |
| spiral | 79 % → 86 % | 52.0 px | 0.15 | 1.09 | 1040 |
| loop | 56 % → 65 % | 72.5 px | 0.13 | 1.17 | 462 |
| tilted | 26 % → 27 % | 73.1 px | 0.13 | 1.03 | 353 |
| over the wet one | 53 % → 71 % | 73.8 px | 0.13 | 1.35 | 248 |
| long, no reload | 97 % → 100 % | 43.4 px | 0.16 | 1.03 | 1800 | quarters: 0.21 → 0.19 → 0.16 → 0.12

Numbers say: light vs heavy: width 63.3 → 94.9 px, dark 0.10 → 0.11; wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #41 Coloured pencil hatching
Pastel · 4 px · 9.9 s

![Brush Artist · Refs · #41 Coloured pencil hatching](Brush-Artist-Refs-41-Coloured-pencil-hatching.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 1 % → 1 % | 1.6 px | 0.42 | 1.00 | 18 |
| heavy line | 1 % → 1 % | 2.6 px | 0.43 | 1.00 | 13 |
| pressure swell | 1 % → 1 % | 2.1 px | 0.43 | 1.00 | 9 |
| fast wave | 2 % → 2 % | 2.2 px | 0.42 | 1.00 | 31 |
| slow wave | 2 % → 2 % | 2.1 px | 0.43 | 1.00 | 30 |
| spiral | 3 % → 3 % | 2.1 px | 0.43 | 1.00 | 55 |
| loop | 2 % → 2 % | 2.2 px | 0.43 | 1.00 | 27 |
| tilted | 1 % → 1 % | 3.0 px | 0.42 | 1.00 | 15 |
| over the wet one | 2 % → 2 % | 2.2 px | 0.42 | 1.00 | 13 |
| long, no reload | 5 % → 5 % | 2.3 px | 0.43 | 1.00 | 78 | quarters: 0.02 → 0.02 → 0.02 → 0.03

Numbers say: light vs heavy: width 1.6 → 2.6 px, dark 0.42 → 0.43; the long stroke does not run out of paint.

## Brush Artist · Refs · #42 Oil pastel shaggy
Pastel · 18 px · 14.5 s

![Brush Artist · Refs · #42 Oil pastel shaggy](Brush-Artist-Refs-42-Oil-pastel-shaggy.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 2 % → 2 % | 5.1 px | 0.35 | 1.00 | 20 |
| heavy line | 4 % → 4 % | 10.7 px | 0.36 | 1.00 | 40 |
| pressure swell | 3 % → 3 % | 9.5 px | 0.36 | 1.00 | 32 |
| fast wave | 8 % → 8 % | 9.0 px | 0.36 | 1.00 | 114 |
| slow wave | 7 % → 7 % | 8.2 px | 0.36 | 1.00 | 189 |
| spiral | 12 % → 12 % | 7.7 px | 0.36 | 1.00 | 221 |
| loop | 6 % → 6 % | 7.9 px | 0.36 | 1.00 | 87 |
| tilted | 2 % → 2 % | 6.9 px | 0.36 | 1.00 | 39 |
| over the wet one | 6 % → 6 % | 8.5 px | 0.36 | 1.00 | 34 |
| long, no reload | 15 % → 15 % | 6.9 px | 0.36 | 1.00 | 233 | quarters: 0.00 → 0.00 → 0.00 → 0.00

Numbers say: light vs heavy: width 5.1 → 10.7 px, dark 0.35 → 0.36; the long stroke does not run out of paint.

## Brush Artist · Refs · #43 Dragged black ink blocks
Gouache · 70 px · 40.5 s

![Brush Artist · Refs · #43 Dragged black ink blocks](Brush-Artist-Refs-43-Dragged-black-ink-blocks.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 19 % → 5 % | 54.9 px | 0.57 | 0.28 | 251 |
| heavy line | 24 % → 9 % | 69.0 px | 0.57 | 0.38 | 567 |
| pressure swell | 17 % → 9 % | 63.4 px | 0.57 | 0.53 | 271 |
| fast wave | 51 % → 11 % | 58.7 px | 0.57 | 0.21 | 1184 |
| slow wave | 50 % → 10 % | 58.1 px | 0.57 | 0.20 | 1117 |
| spiral | 65 % → 14 % | 42.6 px | 0.57 | 0.22 | 1278 |
| loop | 45 % → 12 % | 58.1 px | 0.57 | 0.27 | 529 |
| tilted | 17 % → 16 % | 46.4 px | 0.57 | 0.98 | 325 |
| over the wet one | 37 % → 20 % | 55.6 px | 0.57 | 0.56 | 255 |
| long, no reload | 82 % → 17 % | 36.6 px | 0.57 | 0.21 | 1863 | quarters: 0.54 → 0.52 → 0.47 → 0.40

Numbers say: light vs heavy: width 54.9 → 69.0 px, dark 0.57 → 0.57.

## Brush Artist · Refs · #44 Blue looping ribbon
Oil · 80 px · 33.9 s

![Brush Artist · Refs · #44 Blue looping ribbon](Brush-Artist-Refs-44-Blue-looping-ribbon.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 26 % → 27 % | 74.9 px | 0.72 | 1.04 | 624 |
| heavy line | 27 % → 27 % | 79.6 px | 0.72 | 1.00 | 487 |
| pressure swell | 21 % → 21 % | 78.1 px | 0.72 | 1.03 | 244 |
| fast wave | 61 % → 64 % | 70.3 px | 0.73 | 1.05 | 875 |
| slow wave | 61 % → 61 % | 70.0 px | 0.73 | 1.00 | 1815 |
| spiral | 78 % → 78 % | 51.3 px | 0.73 | 1.00 | 1669 |
| loop | 54 % → 54 % | 69.7 px | 0.73 | 1.00 | 901 |
| tilted | 21 % → 21 % | 57.3 px | 0.72 | 1.00 | 454 |
| over the wet one | 44 % → 44 % | 64.9 px | 0.72 | 1.00 | 377 |
| long, no reload | 96 % → 96 % | 42.8 px | 0.73 | 1.00 | 3491 | quarters: 0.72 → 0.73 → 0.73 → 0.69

Numbers say: light vs heavy: width 74.9 → 79.6 px, dark 0.72 → 0.72; pressure barely changes the width; the long stroke does not run out of paint.

## Brush Artist · Refs · #45 Soft pastel pepper
Pastel · 40 px · 14.9 s

![Brush Artist · Refs · #45 Soft pastel pepper](Brush-Artist-Refs-45-Soft-pastel-pepper.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 4 % → 4 % | 11.3 px | 0.53 | 1.00 | 56 |
| heavy line | 8 % → 8 % | 23.0 px | 0.53 | 1.00 | 135 |
| pressure swell | 5 % → 5 % | 19.5 px | 0.53 | 1.00 | 38 |
| fast wave | 17 % → 17 % | 19.4 px | 0.53 | 1.00 | 158 |
| slow wave | 15 % → 15 % | 17.1 px | 0.53 | 1.00 | 346 |
| spiral | 25 % → 25 % | 16.3 px | 0.53 | 1.00 | 320 |
| loop | 12 % → 12 % | 16.1 px | 0.53 | 1.00 | 237 |
| tilted | 5 % → 5 % | 12.8 px | 0.53 | 1.00 | 177 |
| over the wet one | 11 % → 11 % | 17.7 px | 0.53 | 1.00 | 101 |
| long, no reload | 30 % → 30 % | 13.6 px | 0.53 | 1.00 | 683 | quarters: 0.18 → 0.18 → 0.18 → 0.18

Numbers say: light vs heavy: width 11.3 → 23.0 px, dark 0.53 → 0.53; the long stroke does not run out of paint.

## Brush Artist · Refs · #46 Red-brown ink lips
Watercolor · 50 px · 55.9 s

![Brush Artist · Refs · #46 Red-brown ink lips](Brush-Artist-Refs-46-Red-brown-ink-lips.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 12 % → 23 % | 33.6 px | 0.67 | 2.00 | 98 |
| heavy line | 19 % → 30 % | 54.1 px | 0.65 | 1.59 | 158 |
| pressure swell | 12 % → 20 % | 43.7 px | 0.67 | 1.73 | 145 |
| fast wave | 40 % → 60 % | 46.7 px | 0.66 | 1.48 | 461 |
| slow wave | 39 % → 58 % | 44.6 px | 0.69 | 1.52 | 526 |
| spiral | 63 % → 75 % | 41.6 px | 0.70 | 1.19 | 518 |
| loop | 35 % → 51 % | 44.9 px | 0.68 | 1.48 | 243 |
| tilted | 16 % → 17 % | 43.6 px | 0.67 | 1.07 | 168 |
| over the wet one | 33 % → 51 % | 47.6 px | 0.67 | 1.55 | 123 |
| long, no reload | 78 % → 95 % | 35.2 px | 0.70 | 1.21 | 756 | quarters: 0.71 → 0.71 → 0.70 → 0.64

Numbers say: light vs heavy: width 33.6 → 54.1 px, dark 0.67 → 0.65; the long stroke does not run out of paint; wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #47 Pink knife slabs
Heavy acrylic · 90 px · 39.5 s

![Brush Artist · Refs · #47 Pink knife slabs](Brush-Artist-Refs-47-Pink-knife-slabs.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 28 % → 27 % | 81.1 px | 0.29 | 0.97 | 337 |
| heavy line | 29 % → 28 % | 83.5 px | 0.29 | 0.97 | 329 |
| pressure swell | 22 % → 22 % | 83.4 px | 0.29 | 1.01 | 308 |
| fast wave | 61 % → 60 % | 70.2 px | 0.28 | 0.98 | 1075 |
| slow wave | 61 % → 59 % | 71.0 px | 0.27 | 0.96 | 1361 |
| spiral | 76 % → 58 % | 50.0 px | 0.27 | 0.76 | 1213 |
| loop | 55 % → 54 % | 71.7 px | 0.28 | 0.97 | 696 |
| tilted | 21 % → 21 % | 59.3 px | 0.29 | 1.00 | 364 |
| over the wet one | 46 % → 44 % | 68.0 px | 0.29 | 0.96 | 325 |
| long, no reload | 92 % → 76 % | 41.3 px | 0.26 | 0.83 | 1841 | quarters: 0.00 → 0.00 → 0.00 → 0.00

Numbers say: light vs heavy: width 81.1 → 83.5 px, dark 0.29 → 0.29; pressure barely changes the width; the long stroke does not run out of paint.

## Brush Artist · Refs · #48 Black bands with drips
Gouache · 70 px · 54.9 s

![Brush Artist · Refs · #48 Black bands with drips](Brush-Artist-Refs-48-Black-bands-with-drips.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 19 % → 18 % | 54.6 px | 0.69 | 0.93 | 268 |
| heavy line | 29 % → 24 % | 83.0 px | 0.69 | 0.84 | 526 |
| pressure swell | 23 % → 21 % | 86.1 px | 0.69 | 0.92 | 342 |
| fast wave | 53 % → 36 % | 61.8 px | 0.69 | 0.68 | 700 |
| slow wave | 53 % → 36 % | 61.7 px | 0.69 | 0.67 | 1244 |
| spiral | 64 % → 35 % | 41.9 px | 0.69 | 0.55 | 1179 |
| loop | 45 % → 36 % | 57.8 px | 0.69 | 0.81 | 630 |
| tilted | 19 % → 19 % | 52.3 px | 0.69 | 1.00 | 557 |
| over the wet one | 41 % → 38 % | 62.4 px | 0.69 | 0.92 | 789 |
| long, no reload | 74 % → 37 % | 33.3 px | 0.69 | 0.50 | 1830 | quarters: 0.64 → 0.61 → 0.54 → 0.45

Numbers say: light vs heavy: width 54.6 → 83.0 px, dark 0.69 → 0.69.

## Brush Artist · Refs · #49 Magenta letters round brush
Ink · 30 px · 36.7 s

![Brush Artist · Refs · #49 Magenta letters round brush](Brush-Artist-Refs-49-Magenta-letters-round-brush.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 6 % → 8 % | 17.5 px | 0.50 | 1.28 | 46 |
| heavy line | 21 % → 21 % | 62.0 px | 0.51 | 0.99 | 210 |
| pressure swell | 12 % → 13 % | 46.3 px | 0.52 | 1.01 | 114 |
| fast wave | 38 % → 38 % | 44.3 px | 0.51 | 0.99 | 251 |
| slow wave | 32 % → 31 % | 36.4 px | 0.51 | 0.99 | 375 |
| spiral | 50 % → 48 % | 32.8 px | 0.51 | 0.97 | 417 |
| loop | 29 % → 29 % | 37.6 px | 0.51 | 1.00 | 226 |
| tilted | 11 % → 11 % | 30.7 px | 0.52 | 1.01 | 103 |
| over the wet one | 26 % → 26 % | 42.1 px | 0.52 | 1.01 | 95 |
| long, no reload | 61 % → 56 % | 27.5 px | 0.51 | 0.92 | 595 | quarters: 0.41 → 0.36 → 0.30 → 0.25

Numbers say: light vs heavy: width 17.5 → 62.0 px, dark 0.50 → 0.51.

## Brush Artist · Refs · #50 Thick swipes on photo
Heavy acrylic · 40 px · 22.9 s

![Brush Artist · Refs · #50 Thick swipes on photo](Brush-Artist-Refs-50-Thick-swipes-on-photo.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 13 % → 13 % | 38.1 px | 0.26 | 0.96 | 138 |
| heavy line | 14 % → 13 % | 40.2 px | 0.27 | 0.96 | 128 |
| pressure swell | 11 % → 10 % | 40.1 px | 0.25 | 0.95 | 95 |
| fast wave | 33 % → 31 % | 38.3 px | 0.25 | 0.93 | 382 |
| slow wave | 34 % → 32 % | 39.1 px | 0.26 | 0.95 | 603 |
| spiral | 58 % → 47 % | 38.5 px | 0.24 | 0.80 | 617 |
| loop | 28 % → 27 % | 36.9 px | 0.26 | 0.95 | 262 |
| tilted | 12 % → 12 % | 34.0 px | 0.26 | 1.00 | 145 |
| over the wet one | 25 % → 24 % | 35.3 px | 0.26 | 0.95 | 178 |
| long, no reload | 66 % → 46 % | 29.6 px | 0.24 | 0.69 | 1006 | quarters: 0.00 → 0.00 → 0.00 → 0.00

Numbers say: light vs heavy: width 38.1 → 40.2 px, dark 0.26 → 0.27; pressure barely changes the width; the long stroke does not run out of paint.

## Brush Artist · Refs · Finger
Pastel · 36 px · 25.5 s · over bands of wet oil paint and oil pastel in turn (it works on paint already there: look at what it does to the bands; covered counts the bands too)

![Brush Artist · Refs · Finger](Brush-Artist-Refs-Finger.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 27 % → 27 % | 79.5 px | 0.78 | 1.00 | 39 |
| heavy line | 30 % → 30 % | 87.1 px | 0.76 | 1.00 | 57 |
| pressure swell | 28 % → 28 % | 103.6 px | 0.78 | 1.00 | 40 |
| fast wave | 36 % → 36 % | 41.8 px | 0.72 | 1.00 | 130 |
| slow wave | 35 % → 35 % | 40.3 px | 0.72 | 1.00 | 258 |
| spiral | 43 % → 43 % | 28.7 px | 0.68 | 1.00 | 259 |
| loop | 33 % → 33 % | 42.9 px | 0.73 | 1.00 | 145 |
| tilted | 28 % → 28 % | 77.0 px | 0.74 | 1.00 | 74 |
| over the wet one | 32 % → 32 % | 13.1 px | 0.74 | 1.00 | 63 |
| long, no reload | 48 % → 48 % | 21.5 px | 0.66 | 1.00 | 539 | quarters: 0.33 → 0.35 → 0.33 → 0.37

Numbers say: light vs heavy: width 79.5 → 87.1 px, dark 0.78 → 0.76; pressure barely changes the width; the long stroke does not run out of paint.

## Brush Artist · Ink — wash
Watercolor · 38 px · 42.2 s

![Brush Artist · Ink — wash](Brush-Artist-Ink-wash.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 11 % → 11 % | 31.6 px | 0.38 | 1.03 | 79 |
| heavy line | 19 % → 19 % | 54.3 px | 0.32 | 1.03 | 101 |
| pressure swell | 12 % → 12 % | 45.1 px | 0.36 | 1.04 | 104 |
| fast wave | 39 % → 41 % | 44.7 px | 0.30 | 1.05 | 269 |
| slow wave | 37 % → 38 % | 42.6 px | 0.37 | 1.04 | 409 |
| spiral | 57 % → 60 % | 37.9 px | 0.30 | 1.04 | 340 |
| loop | 32 % → 33 % | 41.8 px | 0.34 | 1.02 | 204 |
| tilted | 13 % → 14 % | 36.8 px | 0.38 | 1.04 | 125 |
| over the wet one | 29 % → 30 % | 42.8 px | 0.38 | 1.04 | 100 |
| long, no reload | 65 % → 70 % | 29.2 px | 0.29 | 1.08 | 524 | quarters: 0.33 → 0.26 → 0.18 → 0.11

Numbers say: light vs heavy: width 31.6 → 54.3 px, dark 0.38 → 0.32.

## Brush Artist · Ink — brush line
Ink · 16 px · 32.5 s

![Brush Artist · Ink — brush line](Brush-Artist-Ink-brush-line.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 3 % → 5 % | 7.7 px | 0.78 | 1.80 | 75 |
| heavy line | 13 % → 13 % | 39.0 px | 0.88 | 0.99 | 123 |
| pressure swell | 8 % → 8 % | 28.4 px | 0.87 | 1.05 | 50 |
| fast wave | 24 % → 23 % | 27.6 px | 0.87 | 0.96 | 153 |
| slow wave | 19 % → 19 % | 22.5 px | 0.87 | 0.97 | 186 |
| spiral | 30 % → 27 % | 19.9 px | 0.86 | 0.90 | 330 |
| loop | 18 % → 18 % | 23.4 px | 0.88 | 1.00 | 167 |
| tilted | 7 % → 7 % | 20.1 px | 0.88 | 1.01 | 95 |
| over the wet one | 17 % → 17 % | 26.8 px | 0.88 | 1.00 | 73 |
| long, no reload | 42 % → 31 % | 18.8 px | 0.85 | 0.73 | 477 | quarters: 0.49 → 0.40 → 0.30 → 0.21

Numbers say: light vs heavy: width 7.7 → 39.0 px, dark 0.78 → 0.88; wet paint spreads well beyond the stroke.

## Brush Artist · Ink — dry brush
Gouache · 30 px · 27.6 s

![Brush Artist · Ink — dry brush](Brush-Artist-Ink-dry-brush.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 7 % → 1 % | 21.8 px | 0.71 | 0.11 | 95 |
| heavy line | 10 % → 1 % | 27.7 px | 0.71 | 0.10 | 132 |
| pressure swell | 7 % → 2 % | 25.5 px | 0.71 | 0.23 | 95 |
| fast wave | 21 % → 2 % | 24.2 px | 0.71 | 0.09 | 320 |
| slow wave | 21 % → 2 % | 23.9 px | 0.71 | 0.08 | 499 |
| spiral | 31 % → 2 % | 20.6 px | 0.71 | 0.06 | 829 |
| loop | 18 % → 2 % | 23.9 px | 0.71 | 0.13 | 433 |
| tilted | 9 % → 8 % | 24.1 px | 0.71 | 0.96 | 241 |
| over the wet one | 17 % → 4 % | 22.8 px | 0.71 | 0.24 | 165 |
| long, no reload | 31 % → 3 % | 14.0 px | 0.71 | 0.09 | 950 | quarters: 0.38 → 0.32 → 0.22 → 0.09

Numbers say: light vs heavy: width 21.8 → 27.7 px, dark 0.71 → 0.71.

## Brush Artist · Watercolour — blue
Watercolor · 40 px · 35.1 s

![Brush Artist · Watercolour — blue](Brush-Artist-Watercolour-blue.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 6 % → 10 % | 16.7 px | 0.25 | 1.70 | 41 |
| heavy line | 11 % → 12 % | 31.5 px | 0.25 | 1.13 | 72 |
| pressure swell | 7 % → 9 % | 25.4 px | 0.26 | 1.32 | 49 |
| fast wave | 24 % → 25 % | 27.8 px | 0.24 | 1.05 | 176 |
| slow wave | 22 % → 27 % | 25.9 px | 0.26 | 1.22 | 293 |
| spiral | 38 % → 41 % | 25.1 px | 0.22 | 1.08 | 358 |
| loop | 20 % → 22 % | 25.3 px | 0.26 | 1.13 | 184 |
| tilted | 12 % → 12 % | 33.3 px | 0.26 | 1.00 | 99 |
| over the wet one | 21 % → 24 % | 24.7 px | 0.26 | 1.15 | 82 |
| long, no reload | 51 % → 54 % | 23.0 px | 0.22 | 1.04 | 490 | quarters: 0.18 → 0.14 → 0.11 → 0.08

Numbers say: light vs heavy: width 16.7 → 31.5 px, dark 0.25 → 0.25; wet paint spreads well beyond the stroke.

## Brush Artist · Watercolour — violet
Watercolor · 40 px · 34.4 s

![Brush Artist · Watercolour — violet](Brush-Artist-Watercolour-violet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 6 % → 10 % | 16.7 px | 0.40 | 1.70 | 32 |
| heavy line | 11 % → 12 % | 31.5 px | 0.40 | 1.13 | 85 |
| pressure swell | 7 % → 9 % | 25.4 px | 0.41 | 1.32 | 59 |
| fast wave | 24 % → 25 % | 27.8 px | 0.38 | 1.05 | 168 |
| slow wave | 22 % → 27 % | 25.9 px | 0.40 | 1.22 | 316 |
| spiral | 38 % → 41 % | 25.1 px | 0.36 | 1.08 | 264 |
| loop | 20 % → 22 % | 25.3 px | 0.40 | 1.13 | 147 |
| tilted | 12 % → 12 % | 33.3 px | 0.40 | 1.00 | 125 |
| over the wet one | 21 % → 24 % | 24.7 px | 0.40 | 1.15 | 73 |
| long, no reload | 51 % → 54 % | 23.0 px | 0.34 | 1.04 | 436 | quarters: 0.28 → 0.22 → 0.17 → 0.14

Numbers say: light vs heavy: width 16.7 → 31.5 px, dark 0.40 → 0.40; wet paint spreads well beyond the stroke.

## Brush Artist · Watercolour — teal
Watercolor · 40 px · 35.5 s

![Brush Artist · Watercolour — teal](Brush-Artist-Watercolour-teal.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 6 % → 10 % | 16.7 px | 0.16 | 1.70 | 45 |
| heavy line | 11 % → 12 % | 31.5 px | 0.16 | 1.13 | 90 |
| pressure swell | 7 % → 9 % | 25.4 px | 0.17 | 1.32 | 69 |
| fast wave | 24 % → 25 % | 27.8 px | 0.15 | 1.05 | 207 |
| slow wave | 22 % → 27 % | 25.9 px | 0.17 | 1.22 | 354 |
| spiral | 38 % → 41 % | 25.1 px | 0.15 | 1.08 | 320 |
| loop | 20 % → 22 % | 25.3 px | 0.16 | 1.13 | 153 |
| tilted | 12 % → 12 % | 33.3 px | 0.16 | 1.00 | 207 |
| over the wet one | 21 % → 24 % | 24.7 px | 0.16 | 1.15 | 81 |
| long, no reload | 51 % → 54 % | 23.0 px | 0.14 | 1.04 | 476 | quarters: 0.11 → 0.09 → 0.07 → 0.06

Numbers say: light vs heavy: width 16.7 → 31.5 px, dark 0.16 → 0.16; wet paint spreads well beyond the stroke.

## Brush Artist · Gouache
Gouache · 30 px · 41.0 s

![Brush Artist · Gouache](Brush-Artist-Gouache.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 8 % → 8 % | 24.4 px | 0.27 | 0.97 | 85 |
| heavy line | 15 % → 11 % | 42.8 px | 0.27 | 0.78 | 96 |
| pressure swell | 11 % → 9 % | 41.0 px | 0.27 | 0.84 | 72 |
| fast wave | 30 % → 13 % | 34.4 px | 0.26 | 0.45 | 248 |
| slow wave | 29 % → 14 % | 33.9 px | 0.26 | 0.46 | 461 |
| spiral | 40 % → 14 % | 26.6 px | 0.26 | 0.35 | 434 |
| loop | 23 % → 15 % | 30.4 px | 0.26 | 0.62 | 284 |
| tilted | 10 % → 10 % | 27.1 px | 0.26 | 1.01 | 112 |
| over the wet one | 21 % → 19 % | 32.8 px | 0.26 | 0.89 | 112 |
| long, no reload | 43 % → 15 % | 19.1 px | 0.26 | 0.35 | 600 | quarters: 0.01 → 0.01 → 0.01 → 0.01

Numbers say: light vs heavy: width 24.4 → 42.8 px, dark 0.27 → 0.27; the long stroke does not run out of paint.

## Brush Artist · Oil — bristle
Oil · 30 px · 19.7 s

![Brush Artist · Oil — bristle](Brush-Artist-Oil-bristle.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 9 % → 9 % | 26.3 px | 0.54 | 1.00 | 120 |
| heavy line | 10 % → 10 % | 28.6 px | 0.54 | 1.00 | 193 |
| pressure swell | 8 % → 8 % | 28.2 px | 0.55 | 1.00 | 153 |
| fast wave | 24 % → 24 % | 27.3 px | 0.55 | 1.00 | 547 |
| slow wave | 25 % → 25 % | 28.3 px | 0.55 | 1.00 | 669 |
| spiral | 39 % → 39 % | 25.6 px | 0.54 | 1.00 | 671 |
| loop | 20 % → 20 % | 26.3 px | 0.54 | 1.00 | 347 |
| tilted | 11 % → 11 % | 29.9 px | 0.53 | 1.00 | 154 |
| over the wet one | 20 % → 20 % | 25.5 px | 0.53 | 1.00 | 145 |
| long, no reload | 50 % → 50 % | 22.4 px | 0.54 | 1.00 | 840 | quarters: 0.32 → 0.30 → 0.29 → 0.28

Numbers say: light vs heavy: width 26.3 → 28.6 px, dark 0.54 → 0.54; pressure barely changes the width; the long stroke does not run out of paint.

## Brush Artist · Charcoal — stick
Charcoal · 28 px · 12.6 s

![Brush Artist · Charcoal — stick](Brush-Artist-Charcoal-stick.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 3 % → 3 % | 8.4 px | 0.85 | 1.00 | 28 |
| heavy line | 6 % → 6 % | 17.8 px | 0.85 | 1.00 | 28 |
| pressure swell | 4 % → 4 % | 13.9 px | 0.85 | 1.00 | 20 |
| fast wave | 12 % → 12 % | 14.0 px | 0.85 | 1.00 | 55 |
| slow wave | 11 % → 11 % | 12.5 px | 0.85 | 1.00 | 117 |
| spiral | 19 % → 19 % | 12.7 px | 0.85 | 1.00 | 82 |
| loop | 10 % → 10 % | 12.8 px | 0.85 | 1.00 | 48 |
| tilted | 4 % → 4 % | 10.9 px | 0.85 | 1.00 | 36 |
| over the wet one | 9 % → 9 % | 13.5 px | 0.85 | 1.00 | 24 |
| long, no reload | 27 % → 27 % | 12.2 px | 0.85 | 1.00 | 163 | quarters: 0.26 → 0.25 → 0.26 → 0.27

Numbers say: light vs heavy: width 8.4 → 17.8 px, dark 0.85 → 0.85; the long stroke does not run out of paint.

## Brush Artist · Charcoal — stick B
Charcoal · 36 px · 14.5 s

![Brush Artist · Charcoal — stick B](Brush-Artist-Charcoal-stick-B.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 4 % → 4 % | 10.5 px | 0.85 | 1.00 | 37 |
| heavy line | 7 % → 7 % | 21.1 px | 0.85 | 1.00 | 57 |
| pressure swell | 4 % → 4 % | 16.5 px | 0.85 | 1.00 | 61 |
| fast wave | 15 % → 15 % | 16.8 px | 0.85 | 1.00 | 139 |
| slow wave | 13 % → 13 % | 14.7 px | 0.85 | 1.00 | 240 |
| spiral | 23 % → 23 % | 15.0 px | 0.85 | 1.00 | 273 |
| loop | 11 % → 11 % | 14.8 px | 0.85 | 1.00 | 126 |
| tilted | 4 % → 4 % | 12.3 px | 0.85 | 1.00 | 103 |
| over the wet one | 10 % → 10 % | 15.9 px | 0.85 | 1.00 | 62 |
| long, no reload | 31 % → 31 % | 13.9 px | 0.85 | 1.00 | 199 | quarters: 0.30 → 0.28 → 0.29 → 0.30

Numbers say: light vs heavy: width 10.5 → 21.1 px, dark 0.85 → 0.85; the long stroke does not run out of paint.

## Brush Artist · Charcoal — stick C
Charcoal · 22 px · 13.2 s

![Brush Artist · Charcoal — stick C](Brush-Artist-Charcoal-stick-C.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 2 % → 2 % | 6.9 px | 0.85 | 1.00 | 48 |
| heavy line | 5 % → 5 % | 15.3 px | 0.85 | 1.00 | 28 |
| pressure swell | 3 % → 3 % | 12.2 px | 0.85 | 1.00 | 30 |
| fast wave | 10 % → 10 % | 12.1 px | 0.85 | 1.00 | 96 |
| slow wave | 9 % → 9 % | 10.8 px | 0.85 | 1.00 | 73 |
| spiral | 17 % → 17 % | 11.0 px | 0.85 | 1.00 | 92 |
| loop | 9 % → 9 % | 11.4 px | 0.85 | 1.00 | 43 |
| tilted | 4 % → 4 % | 9.9 px | 0.85 | 1.00 | 32 |
| over the wet one | 8 % → 8 % | 11.7 px | 0.85 | 1.00 | 22 |
| long, no reload | 24 % → 24 % | 11.0 px | 0.85 | 1.00 | 126 | quarters: 0.24 → 0.22 → 0.23 → 0.24

Numbers say: light vs heavy: width 6.9 → 15.3 px, dark 0.85 → 0.85; the long stroke does not run out of paint.

## Brush Artist · Refs · #01 Henry Ward peach cloud — own sheet
own sheet 600 × 600 · Gouache · 44 px · 18.1 s

![Brush Artist · Refs · #01 Henry Ward peach cloud — own sheet](Brush-Artist-Refs-01-Henry-Ward-peach-cloud-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 16 % → 43 % | 45.1 px | 0.59 | 2.70 | 352 |
| stroke 2 | 27 % → 63 % | 88.6 px | 0.59 | 2.33 | 229 |
| stroke 3 | 31 % → 62 % | 90.6 px | 0.59 | 1.99 | 197 |
| stroke 4 | 34 % → 68 % | 109.8 px | 0.59 | 2.03 | 196 |
| stroke 5 | 33 % → 59 % | 95.9 px | 0.59 | 1.80 | 273 |
| stroke 6 | 33 % → 46 % | 100.5 px | 0.59 | 1.40 | 177 |
| stroke 7 | 18 % → 54 % | 44.9 px | 0.60 | 2.99 | 199 |
| stroke 8 | 19 % → 50 % | 48.5 px | 0.60 | 2.61 | 169 |
| stroke 9 | 23 % → 51 % | 58.2 px | 0.60 | 2.27 | 155 |
| stroke 10 | 25 % → 52 % | 67.0 px | 0.60 | 2.08 | 254 |
| stroke 11 | 27 % → 55 % | 77.1 px | 0.60 | 2.00 | 174 |
| stroke 12 | 31 % → 57 % | 93.0 px | 0.60 | 1.85 | 183 |
| stroke 13 | 39 % → 60 % | 113.7 px | 0.60 | 1.53 | 224 |
| stroke 14 | 41 % → 62 % | 118.3 px | 0.60 | 1.50 | 188 |
| stroke 15 | 55 % → 68 % | 163.9 px | 0.59 | 1.23 | 187 |
| stroke 16 | 57 % → 69 % | 171.7 px | 0.59 | 1.22 | 224 |
| stroke 17 | 57 % → 70 % | 160.2 px | 0.60 | 1.22 | 216 |
| stroke 18 | 58 % → 68 % | 169.1 px | 0.60 | 1.17 | 174 |
| stroke 19 | 60 % → 67 % | 167.7 px | 0.59 | 1.12 | 286 |
| stroke 20 | 59 % → 64 % | 170.4 px | 0.59 | 1.08 | 330 |
| stroke 21 | 59 % → 61 % | 171.3 px | 0.59 | 1.03 | 285 |
| stroke 22 | 60 % → 62 % | 176.0 px | 0.59 | 1.03 | 302 |
| stroke 23 | 60 % → 60 % | 171.0 px | 0.59 | 1.00 | 275 |
| stroke 24 | 64 % → 63 % | 190.6 px | 0.59 | 1.00 | 206 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #02 Henry Ward cream strokes — own sheet
own sheet 600 × 600 · Gouache · 46 px · 12.6 s

![Brush Artist · Refs · #02 Henry Ward cream strokes — own sheet](Brush-Artist-Refs-02-Henry-Ward-cream-strokes-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 21 % → 39 % | 42.9 px | 0.71 | 1.87 | 426 |
| stroke 2 | 32 % → 45 % | 84.2 px | 0.71 | 1.40 | 308 |
| stroke 3 | 31 % → 52 % | 79.7 px | 0.72 | 1.68 | 268 |
| stroke 4 | 34 % → 49 % | 83.3 px | 0.71 | 1.45 | 235 |
| stroke 5 | 39 % → 52 % | 96.5 px | 0.72 | 1.33 | 270 |
| stroke 6 | 32 % → 46 % | 76.7 px | 0.71 | 1.47 | 231 |
| stroke 7 | 34 % → 32 % | 86.2 px | 0.71 | 0.95 | 243 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #03 Henry Ward navy contours — own sheet
own sheet 600 × 600 · Heavy acrylic · 22 px · 3.1 s

![Brush Artist · Refs · #03 Henry Ward navy contours — own sheet](Brush-Artist-Refs-03-Henry-Ward-navy-contours-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 11 % → 18 % | 23.1 px | 0.69 | 1.56 | 190 |
| stroke 2 | 20 % → 23 % | 28.3 px | 0.69 | 1.14 | 106 |
| stroke 3 | 23 % → 23 % | 33.4 px | 0.69 | 1.01 | 155 |
| stroke 4 | 23 % → 21 % | 50.8 px | 0.69 | 0.92 | 153 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #04 Henry Ward grey cloud — own sheet
own sheet 600 × 600 · Gouache · 50 px · 18.2 s

![Brush Artist · Refs · #04 Henry Ward grey cloud — own sheet](Brush-Artist-Refs-04-Henry-Ward-grey-cloud-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 17 % → 49 % | 48.9 px | 0.40 | 2.96 | 299 |
| stroke 2 | 20 % → 51 % | 57.9 px | 0.40 | 2.54 | 302 |
| stroke 3 | 29 % → 58 % | 81.5 px | 0.40 | 2.00 | 310 |
| stroke 4 | 32 % → 62 % | 93.4 px | 0.40 | 1.92 | 357 |
| stroke 5 | 38 % → 68 % | 116.0 px | 0.40 | 1.78 | 397 |
| stroke 6 | 41 % → 72 % | 135.7 px | 0.40 | 1.74 | 362 |
| stroke 7 | 48 % → 78 % | 140.2 px | 0.40 | 1.63 | 406 |
| stroke 8 | 46 % → 78 % | 137.7 px | 0.40 | 1.68 | 336 |
| stroke 9 | 47 % → 78 % | 142.1 px | 0.40 | 1.65 | 310 |
| stroke 10 | 48 % → 78 % | 153.4 px | 0.40 | 1.64 | 274 |
| stroke 11 | 48 % → 78 % | 135.7 px | 0.40 | 1.63 | 249 |
| stroke 12 | 49 % → 78 % | 147.0 px | 0.40 | 1.60 | 217 |
| stroke 13 | 48 % → 78 % | 137.3 px | 0.40 | 1.63 | 215 |
| stroke 14 | 49 % → 78 % | 144.8 px | 0.40 | 1.61 | 228 |
| stroke 15 | 49 % → 74 % | 140.0 px | 0.40 | 1.52 | 269 |
| stroke 16 | 49 % → 71 % | 148.6 px | 0.40 | 1.46 | 258 |
| stroke 17 | 48 % → 62 % | 137.0 px | 0.40 | 1.31 | 262 |
| stroke 18 | 47 % → 58 % | 154.0 px | 0.40 | 1.24 | 262 |
| stroke 19 | 48 % → 48 % | 142.0 px | 0.40 | 1.02 | 220 |
| stroke 20 | 48 % → 48 % | 152.3 px | 0.40 | 0.99 | 211 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #05 Henry Ward green in rust loops — own sheet
own sheet 600 × 600 · Heavy acrylic · 20 px · 2.4 s

![Brush Artist · Refs · #05 Henry Ward green in rust loops — own sheet](Brush-Artist-Refs-05-Henry-Ward-green-in-rust-loops-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 12 % → 19 % | 20.9 px | 0.02 | 1.60 | 134 |
| stroke 2 | 12 % → 11 % | 23.5 px | 0.02 | 0.93 | 159 |
| stroke 3 | 23 % → 21 % | 41.5 px | 0.02 | 0.93 | 136 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #06 Henry Ward scrubbed grey — own sheet
own sheet 600 × 600 · Gouache · 50 px · 20.9 s

![Brush Artist · Refs · #06 Henry Ward scrubbed grey — own sheet](Brush-Artist-Refs-06-Henry-Ward-scrubbed-grey-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 20 % → 56 % | 48.6 px | 0.40 | 2.83 | 234 |
| stroke 2 | 24 % → 58 % | 64.3 px | 0.40 | 2.41 | 223 |
| stroke 3 | 31 % → 63 % | 93.7 px | 0.40 | 2.04 | 215 |
| stroke 4 | 31 % → 63 % | 98.4 px | 0.40 | 2.01 | 245 |
| stroke 5 | 45 % → 78 % | 136.2 px | 0.40 | 1.71 | 248 |
| stroke 6 | 48 % → 78 % | 145.5 px | 0.40 | 1.64 | 275 |
| stroke 7 | 49 % → 78 % | 139.4 px | 0.40 | 1.61 | 282 |
| stroke 8 | 48 % → 78 % | 152.1 px | 0.40 | 1.63 | 281 |
| stroke 9 | 47 % → 78 % | 144.8 px | 0.40 | 1.67 | 282 |
| stroke 10 | 47 % → 79 % | 152.5 px | 0.40 | 1.68 | 365 |
| stroke 11 | 48 % → 79 % | 141.3 px | 0.40 | 1.63 | 382 |
| stroke 12 | 48 % → 79 % | 147.5 px | 0.40 | 1.63 | 399 |
| stroke 13 | 47 % → 78 % | 133.4 px | 0.40 | 1.66 | 351 |
| stroke 14 | 46 % → 78 % | 135.2 px | 0.40 | 1.69 | 293 |
| stroke 15 | 47 % → 78 % | 134.5 px | 0.40 | 1.67 | 278 |
| stroke 16 | 48 % → 78 % | 152.3 px | 0.40 | 1.65 | 204 |
| stroke 17 | 48 % → 72 % | 141.4 px | 0.40 | 1.52 | 280 |
| stroke 18 | 49 % → 70 % | 147.0 px | 0.40 | 1.43 | 269 |
| stroke 19 | 47 % → 63 % | 139.2 px | 0.40 | 1.36 | 298 |
| stroke 20 | 47 % → 61 % | 146.4 px | 0.40 | 1.30 | 281 |
| stroke 21 | 47 % → 52 % | 137.0 px | 0.40 | 1.10 | 272 |
| stroke 22 | 47 % → 47 % | 156.1 px | 0.40 | 0.99 | 250 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #07 Henry Ward blue L + black zigzag — own sheet
own sheet 600 × 600 · Heavy acrylic · 34 px · 2.6 s

![Brush Artist · Refs · #07 Henry Ward blue L + black zigzag — own sheet](Brush-Artist-Refs-07-Henry-Ward-blue-L-black-zigzag-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 15 % → 17 % | 35.6 px | 0.59 | 1.14 | 136 |
| stroke 2 | 17 % → 16 % | 42.8 px | 0.59 | 0.93 | 97 |

## Brush Artist · Refs · #08 Henry Ward olive bands — own sheet
own sheet 600 × 600 · Gouache · 34 px · 7.7 s

![Brush Artist · Refs · #08 Henry Ward olive bands — own sheet](Brush-Artist-Refs-08-Henry-Ward-olive-bands-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 16 % → 16 % | 32.3 px | 0.57 | 1.03 | 255 |
| stroke 2 | 27 % → 21 % | 61.7 px | 0.57 | 0.76 | 298 |
| stroke 3 | 24 % → 29 % | 50.1 px | 0.57 | 1.23 | 320 |
| stroke 4 | 28 % → 26 % | 61.0 px | 0.57 | 0.91 | 347 |
| stroke 5 | 36 % → 31 % | 73.5 px | 0.57 | 0.87 | 226 |
| stroke 6 | 25 % → 15 % | 46.3 px | 0.57 | 0.61 | 218 |

## Brush Artist · Refs · #09 Henry Ward white loops — own sheet
own sheet 600 × 600 · Gouache · 46 px · 11.8 s

![Brush Artist · Refs · #09 Henry Ward white loops — own sheet](Brush-Artist-Refs-09-Henry-Ward-white-loops-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 29 % → 42 % | 15.7 px | 0.16 | 1.41 | 1423 |
| stroke 2 | 37 % → 36 % | 36.9 px | 0.17 | 0.97 | 1465 |
| stroke 3 | 43 % → 38 % | 39.6 px | 0.17 | 0.88 | 1233 |

## Brush Artist · Refs · #10 Henry Ward maroon loops — own sheet
own sheet 600 × 600 · Heavy acrylic · 30 px · 4.1 s

![Brush Artist · Refs · #10 Henry Ward maroon loops — own sheet](Brush-Artist-Refs-10-Henry-Ward-maroon-loops-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 12 % → 28 % | 28.7 px | 0.72 | 2.39 | 264 |
| stroke 2 | 22 % → 40 % | 48.5 px | 0.72 | 1.87 | 165 |
| stroke 3 | 29 % → 37 % | 58.5 px | 0.72 | 1.27 | 209 |
| stroke 4 | 41 % → 39 % | 92.8 px | 0.72 | 0.96 | 164 |
| stroke 5 | 34 % → 32 % | 85.8 px | 0.72 | 0.93 | 218 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #11 Henry Ward purple spun balls — own sheet
own sheet 600 × 600 · Heavy acrylic · 36 px · 4.1 s

![Brush Artist · Refs · #11 Henry Ward purple spun balls — own sheet](Brush-Artist-Refs-11-Henry-Ward-purple-spun-balls-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 24 % → 35 % | 26.5 px | 0.68 | 1.43 | 328 |
| stroke 2 | 35 % → 46 % | 38.2 px | 0.68 | 1.33 | 441 |
| stroke 3 | 36 % → 34 % | 39.2 px | 0.68 | 0.97 | 402 |

## Brush Artist · Refs · #12 Henry Ward black-olive cage — own sheet
own sheet 600 × 600 · Gouache · 28 px · 5.9 s

![Brush Artist · Refs · #12 Henry Ward black-olive cage — own sheet](Brush-Artist-Refs-12-Henry-Ward-black-olive-cage-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 13 % → 21 % | 24.3 px | 0.59 | 1.64 | 283 |
| stroke 2 | 13 % → 22 % | 29.9 px | 0.59 | 1.76 | 202 |
| stroke 3 | 27 % → 28 % | 43.0 px | 0.59 | 1.04 | 263 |
| stroke 4 | 28 % → 27 % | 55.3 px | 0.59 | 0.98 | 136 |
| stroke 5 | 28 % → 18 % | 51.1 px | 0.59 | 0.65 | 133 |
| stroke 6 | 44 % → 30 % | 84.4 px | 0.59 | 0.68 | 193 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #13 Henry Ward blue streaky form — own sheet
own sheet 600 × 600 · Gouache · 50 px · 17.7 s

![Brush Artist · Refs · #13 Henry Ward blue streaky form — own sheet](Brush-Artist-Refs-13-Henry-Ward-blue-streaky-form-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 16 % → 48 % | 48.7 px | 0.05 | 3.02 | 240 |
| stroke 2 | 22 % → 52 % | 67.0 px | 0.05 | 2.38 | 268 |
| stroke 3 | 33 % → 64 % | 95.7 px | 0.05 | 1.93 | 241 |
| stroke 4 | 33 % → 64 % | 105.8 px | 0.05 | 1.96 | 231 |
| stroke 5 | 48 % → 78 % | 138.8 px | 0.05 | 1.64 | 223 |
| stroke 6 | 47 % → 79 % | 135.4 px | 0.05 | 1.66 | 228 |
| stroke 7 | 49 % → 78 % | 144.3 px | 0.05 | 1.60 | 254 |
| stroke 8 | 49 % → 78 % | 149.4 px | 0.05 | 1.58 | 231 |
| stroke 9 | 48 % → 78 % | 150.1 px | 0.05 | 1.61 | 201 |
| stroke 10 | 48 % → 78 % | 159.4 px | 0.05 | 1.60 | 233 |
| stroke 11 | 46 % → 78 % | 142.9 px | 0.05 | 1.67 | 244 |
| stroke 12 | 48 % → 78 % | 142.7 px | 0.05 | 1.63 | 227 |
| stroke 13 | 47 % → 77 % | 145.1 px | 0.05 | 1.66 | 204 |
| stroke 14 | 45 % → 77 % | 134.5 px | 0.05 | 1.71 | 242 |
| stroke 15 | 46 % → 76 % | 132.5 px | 0.06 | 1.65 | 256 |
| stroke 16 | 48 % → 75 % | 142.0 px | 0.06 | 1.58 | 235 |
| stroke 17 | 58 % → 75 % | 144.8 px | 0.06 | 1.29 | 273 |
| stroke 18 | 60 % → 75 % | 145.4 px | 0.06 | 1.25 | 246 |
| stroke 19 | 67 % → 74 % | 136.1 px | 0.06 | 1.11 | 294 |
| stroke 20 | 75 % → 74 % | 143.2 px | 0.06 | 0.99 | 290 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #14 Henry Ward olive totem — own sheet
own sheet 600 × 600 · Heavy acrylic · 48 px · 7.9 s

![Brush Artist · Refs · #14 Henry Ward olive totem — own sheet](Brush-Artist-Refs-14-Henry-Ward-olive-totem-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 18 % → 46 % | 46.9 px | 0.38 | 2.58 | 146 |
| stroke 2 | 21 % → 50 % | 64.3 px | 0.38 | 2.44 | 138 |
| stroke 3 | 29 % → 52 % | 100.6 px | 0.38 | 1.78 | 149 |
| stroke 4 | 30 % → 54 % | 113.7 px | 0.38 | 1.80 | 168 |
| stroke 5 | 39 % → 63 % | 135.6 px | 0.38 | 1.63 | 133 |
| stroke 6 | 39 % → 65 % | 150.4 px | 0.38 | 1.68 | 122 |
| stroke 7 | 37 % → 61 % | 124.3 px | 0.38 | 1.66 | 136 |
| stroke 8 | 37 % → 63 % | 142.4 px | 0.38 | 1.69 | 130 |
| stroke 9 | 38 % → 63 % | 130.9 px | 0.38 | 1.67 | 132 |
| stroke 10 | 38 % → 62 % | 141.0 px | 0.38 | 1.62 | 134 |
| stroke 11 | 40 % → 65 % | 143.7 px | 0.38 | 1.60 | 139 |
| stroke 12 | 38 % → 65 % | 144.2 px | 0.38 | 1.70 | 156 |
| stroke 13 | 39 % → 66 % | 135.5 px | 0.38 | 1.72 | 138 |
| stroke 14 | 37 % → 62 % | 134.5 px | 0.38 | 1.68 | 145 |
| stroke 15 | 40 % → 66 % | 136.9 px | 0.38 | 1.65 | 122 |
| stroke 16 | 38 % → 64 % | 138.8 px | 0.38 | 1.66 | 135 |
| stroke 17 | 38 % → 62 % | 126.2 px | 0.38 | 1.65 | 135 |
| stroke 18 | 40 % → 66 % | 154.9 px | 0.38 | 1.64 | 123 |
| stroke 19 | 40 % → 60 % | 137.9 px | 0.38 | 1.52 | 136 |
| stroke 20 | 41 % → 55 % | 144.4 px | 0.38 | 1.34 | 149 |
| stroke 21 | 46 % → 55 % | 137.7 px | 0.38 | 1.18 | 146 |
| stroke 22 | 54 % → 53 % | 146.7 px | 0.38 | 0.99 | 168 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #15 Ultramarine brush script — own sheet
own sheet 600 × 600 · Ink · 4 px · 11.0 s

![Brush Artist · Refs · #15 Ultramarine brush script — own sheet](Brush-Artist-Refs-15-Ultramarine-brush-script-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 39 % → 42 % | 8.9 px | 0.67 | 1.05 | 49 |
| stroke 2 | 40 % → 42 % | 8.8 px | 0.66 | 1.06 | 57 |
| stroke 3 | 40 % → 42 % | 9.5 px | 0.73 | 1.06 | 41 |
| stroke 4 | 42 % → 45 % | 10.1 px | 0.74 | 1.08 | 27 |
| stroke 5 | 44 % → 48 % | 9.7 px | 0.73 | 1.08 | 29 |
| stroke 6 | 42 % → 44 % | 9.4 px | 0.65 | 1.04 | 68 |
| stroke 7 | 43 % → 46 % | 9.2 px | 0.72 | 1.08 | 33 |
| stroke 8 | 38 % → 40 % | 9.2 px | 0.68 | 1.06 | 49 |
| stroke 9 | 40 % → 42 % | 9.2 px | 0.69 | 1.06 | 49 |
| stroke 10 | 36 % → 38 % | 9.8 px | 0.68 | 1.05 | 60 |
| stroke 11 | 42 % → 45 % | 9.5 px | 0.70 | 1.06 | 62 |
| stroke 12 | 39 % → 41 % | 9.4 px | 0.66 | 1.05 | 63 |
| stroke 13 | 45 % → 48 % | 10.2 px | 0.71 | 1.06 | 51 |
| stroke 14 | 38 % → 41 % | 9.8 px | 0.72 | 1.06 | 36 |
| stroke 15 | 37 % → 39 % | 9.1 px | 0.69 | 1.06 | 53 |
| stroke 16 | 42 % → 45 % | 9.4 px | 0.72 | 1.06 | 44 |
| stroke 17 | 41 % → 44 % | 7.1 px | 0.71 | 1.08 | 52 |
| stroke 18 | 43 % → 45 % | 9.2 px | 0.73 | 1.06 | 33 |
| stroke 19 | 39 % → 41 % | 8.8 px | 0.66 | 1.05 | 57 |
| stroke 20 | 40 % → 43 % | 9.4 px | 0.71 | 1.06 | 32 |
| stroke 21 | 40 % → 43 % | 9.9 px | 0.70 | 1.06 | 35 |
| stroke 22 | 42 % → 44 % | 8.4 px | 0.65 | 1.06 | 73 |
| stroke 23 | 40 % → 43 % | 10.1 px | 0.73 | 1.07 | 22 |
| stroke 24 | 38 % → 40 % | 8.7 px | 0.73 | 1.07 | 32 |
| stroke 25 | 40 % → 43 % | 9.8 px | 0.72 | 1.07 | 37 |
| stroke 26 | 46 % → 48 % | 9.2 px | 0.68 | 1.05 | 64 |
| stroke 27 | 42 % → 45 % | 8.8 px | 0.63 | 1.05 | 112 |
| stroke 28 | 44 % → 46 % | 9.1 px | 0.70 | 1.06 | 56 |
| stroke 29 | 36 % → 39 % | 10.6 px | 0.72 | 1.08 | 41 |
| stroke 30 | 39 % → 40 % | 8.6 px | 0.71 | 1.04 | 79 |
| stroke 31 | 43 % → 46 % | 10.3 px | 0.75 | 1.07 | 23 |
| stroke 32 | 42 % → 45 % | 9.4 px | 0.73 | 1.09 | 45 |
| stroke 33 | 35 % → 38 % | 10.8 px | 0.72 | 1.08 | 45 |
| stroke 34 | 40 % → 43 % | 9.7 px | 0.73 | 1.07 | 42 |
| stroke 35 | 35 % → 37 % | 9.3 px | 0.65 | 1.05 | 63 |

## Brush Artist · Refs · #18 Blue oil-stick scribbles — own sheet
own sheet 600 × 600 · Pastel · 10 px · 4.3 s

![Brush Artist · Refs · #18 Blue oil-stick scribbles — own sheet](Brush-Artist-Refs-18-Blue-oil-stick-scribbles-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 15 % → 31 % | 3.8 px | 0.49 | 2.11 | 233 |
| stroke 2 | 13 % → 37 % | 3.6 px | 0.49 | 2.73 | 325 |
| stroke 3 | 16 % → 26 % | 5.8 px | 0.49 | 1.66 | 277 |
| stroke 4 | 15 % → 29 % | 8.0 px | 0.49 | 1.88 | 303 |
| stroke 5 | 29 % → 34 % | 8.4 px | 0.49 | 1.19 | 232 |
| stroke 6 | 25 % → 26 % | 9.4 px | 0.49 | 1.02 | 214 |
| stroke 7 | 26 % → 32 % | 8.3 px | 0.49 | 1.24 | 182 |
| stroke 8 | 30 % → 30 % | 17.0 px | 0.49 | 1.00 | 230 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #20 Orange-red crayon scribble — own sheet
own sheet 600 × 600 · Pastel · 14 px · 3.2 s

![Brush Artist · Refs · #20 Orange-red crayon scribble — own sheet](Brush-Artist-Refs-20-Orange-red-crayon-scribble-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 8 % → 18 % | 5.5 px | 0.59 | 2.46 | 193 |
| stroke 2 | 9 % → 23 % | 6.8 px | 0.59 | 2.48 | 191 |
| stroke 3 | 13 % → 21 % | 8.5 px | 0.59 | 1.64 | 202 |
| stroke 4 | 24 % → 32 % | 8.9 px | 0.59 | 1.34 | 173 |
| stroke 5 | 27 % → 27 % | 7.7 px | 0.59 | 1.00 | 176 |
| stroke 6 | 22 % → 22 % | 16.8 px | 0.59 | 1.00 | 218 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #21 Gritty black contours — own sheet
own sheet 600 × 600 · Gouache · 12 px · 6.9 s

![Brush Artist · Refs · #21 Gritty black contours — own sheet](Brush-Artist-Refs-21-Gritty-black-contours-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 10 % → 8 % | 10.6 px | 0.36 | 0.84 | 161 |
| stroke 2 | 9 % → 5 % | 15.4 px | 0.36 | 0.57 | 229 |
| stroke 3 | 14 % → 4 % | 12.9 px | 0.36 | 0.28 | 128 |
| stroke 4 | 16 % → 8 % | 19.7 px | 0.36 | 0.50 | 138 |
| stroke 5 | 18 % → 8 % | 21.5 px | 0.36 | 0.47 | 117 |

## Brush Artist · Refs · #22 Bold black brush poster — own sheet
own sheet 600 × 600 · Ink · 20 px · 8.5 s

![Brush Artist · Refs · #22 Bold black brush poster — own sheet](Brush-Artist-Refs-22-Bold-black-brush-poster-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 22 % → 27 % | 36.3 px | 0.94 | 1.20 | 126 |
| stroke 2 | 27 % → 37 % | 41.4 px | 0.95 | 1.36 | 32 |
| stroke 3 | 28 % → 28 % | 43.6 px | 0.94 | 1.00 | 62 |
| stroke 4 | 27 % → 39 % | 53.8 px | 0.94 | 1.42 | 62 |
| stroke 5 | 25 % → 25 % | 42.9 px | 0.94 | 1.00 | 80 |

## Brush Artist · Refs · #23 Dry white on orange + black line — own sheet
own sheet 600 × 600 · Gouache · 50 px · 14.2 s

![Brush Artist · Refs · #23 Dry white on orange + black line — own sheet](Brush-Artist-Refs-23-Dry-white-on-orange-black-line-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 13 % → 35 % | 44.0 px | 0.44 | 2.78 | 159 |
| stroke 2 | 15 % → 32 % | 53.3 px | 0.44 | 2.13 | 225 |
| stroke 3 | 22 % → 35 % | 82.6 px | 0.44 | 1.59 | 183 |
| stroke 4 | 24 % → 39 % | 95.4 px | 0.44 | 1.61 | 214 |
| stroke 5 | 35 % → 47 % | 126.2 px | 0.44 | 1.36 | 184 |
| stroke 6 | 36 % → 51 % | 146.8 px | 0.44 | 1.43 | 160 |
| stroke 7 | 31 % → 50 % | 118.1 px | 0.44 | 1.61 | 160 |
| stroke 8 | 31 % → 48 % | 122.2 px | 0.44 | 1.52 | 165 |
| stroke 9 | 31 % → 48 % | 117.4 px | 0.44 | 1.54 | 185 |
| stroke 10 | 32 % → 49 % | 127.1 px | 0.43 | 1.51 | 216 |
| stroke 11 | 35 % → 51 % | 129.9 px | 0.43 | 1.48 | 298 |
| stroke 12 | 35 % → 50 % | 135.5 px | 0.44 | 1.45 | 277 |
| stroke 13 | 36 % → 53 % | 134.7 px | 0.43 | 1.45 | 787 |
| stroke 14 | 35 % → 52 % | 137.7 px | 0.43 | 1.48 | 609 |
| stroke 15 | 35 % → 47 % | 132.2 px | 0.43 | 1.33 | 445 |
| stroke 16 | 34 % → 41 % | 135.8 px | 0.43 | 1.19 | 346 |
| stroke 17 | 34 % → 34 % | 119.2 px | 0.43 | 1.01 | 178 |
| stroke 18 | 41 % → 36 % | 149.1 px | 0.43 | 0.88 | 169 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #24 Picasso flat oil — own sheet
own sheet 600 × 600 · Oil · 34 px · 7.2 s

![Brush Artist · Refs · #24 Picasso flat oil — own sheet](Brush-Artist-Refs-24-Picasso-flat-oil-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 16 % → 45 % | 34.7 px | 0.23 | 2.74 | 446 |
| stroke 2 | 20 % → 48 % | 47.2 px | 0.24 | 2.40 | 339 |
| stroke 3 | 29 % → 59 % | 62.5 px | 0.23 | 2.07 | 281 |
| stroke 4 | 37 % → 65 % | 83.1 px | 0.23 | 1.76 | 171 |
| stroke 5 | 43 % → 71 % | 94.5 px | 0.23 | 1.65 | 165 |
| stroke 6 | 44 % → 66 % | 102.1 px | 0.23 | 1.50 | 176 |
| stroke 7 | 45 % → 66 % | 94.8 px | 0.23 | 1.46 | 142 |
| stroke 8 | 44 % → 66 % | 106.9 px | 0.23 | 1.50 | 166 |
| stroke 9 | 37 % → 62 % | 81.5 px | 0.23 | 1.67 | 167 |
| stroke 10 | 39 % → 62 % | 93.1 px | 0.23 | 1.58 | 173 |
| stroke 11 | 37 % → 60 % | 78.6 px | 0.23 | 1.62 | 148 |
| stroke 12 | 38 % → 61 % | 91.1 px | 0.23 | 1.60 | 193 |
| stroke 13 | 38 % → 67 % | 84.4 px | 0.23 | 1.76 | 160 |
| stroke 14 | 39 % → 69 % | 88.9 px | 0.23 | 1.75 | 160 |
| stroke 15 | 39 % → 62 % | 83.3 px | 0.23 | 1.58 | 199 |
| stroke 16 | 38 % → 55 % | 87.9 px | 0.23 | 1.43 | 162 |
| stroke 17 | 43 % → 48 % | 90.0 px | 0.23 | 1.12 | 170 |
| stroke 18 | 42 % → 42 % | 102.6 px | 0.23 | 1.00 | 163 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #25 Yellow heavy flat stroke — own sheet
own sheet 600 × 600 · Heavy acrylic · 110 px · 3.4 s

![Brush Artist · Refs · #25 Yellow heavy flat stroke — own sheet](Brush-Artist-Refs-25-Yellow-heavy-flat-stroke-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 18 % → 18 % | 104.2 px | 0.17 | 0.98 | 735 |

## Brush Artist · Refs · #27 Orange impasto swatch — own sheet
own sheet 600 × 600 · Heavy acrylic · 60 px · 3.8 s

![Brush Artist · Refs · #27 Orange impasto swatch — own sheet](Brush-Artist-Refs-27-Orange-impasto-swatch-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 8 % → 21 % | 61.8 px | 0.33 | 2.60 | 85 |
| stroke 2 | 7 % → 33 % | 62.5 px | 0.33 | 4.67 | 64 |
| stroke 3 | 25 % → 36 % | 245.4 px | 0.33 | 1.40 | 53 |
| stroke 4 | 10 % → 12 % | 69.5 px | 0.33 | 1.25 | 63 |
| stroke 5 | 17 % → 33 % | 63.5 px | 0.33 | 1.90 | 85 |
| stroke 6 | 18 % → 31 % | 145.0 px | 0.33 | 1.79 | 78 |
| stroke 7 | 8 % → 15 % | 70.2 px | 0.33 | 1.86 | 49 |
| stroke 8 | 33 % → 34 % | 337.0 px | 0.33 | 1.04 | 68 |
| stroke 9 | 38 % → 37 % | 185.4 px | 0.33 | 0.98 | 88 |
| stroke 10 | 33 % → 33 % | 304.7 px | 0.33 | 0.98 | 57 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #28 Miles Davis black lines — own sheet
own sheet 600 × 600 · Ink · 22 px · 7.9 s

![Brush Artist · Refs · #28 Miles Davis black lines — own sheet](Brush-Artist-Refs-28-Miles-Davis-black-lines-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 22 % → 32 % | 36.4 px | 0.88 | 1.42 | 216 |
| stroke 2 | 28 % → 48 % | 38.1 px | 0.88 | 1.73 | 153 |
| stroke 3 | 39 % → 44 % | 75.0 px | 0.88 | 1.12 | 133 |
| stroke 4 | 42 % → 48 % | 83.5 px | 0.88 | 1.15 | 175 |
| stroke 5 | 55 % → 55 % | 109.6 px | 0.88 | 1.00 | 158 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #29 Shrigley magenta asterisk — own sheet
own sheet 600 × 600 · Watercolor · 70 px · 8.0 s

![Brush Artist · Refs · #29 Shrigley magenta asterisk — own sheet](Brush-Artist-Refs-29-Shrigley-magenta-asterisk-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 13 % → 37 % | 46.6 px | 0.72 | 2.85 | 190 |
| stroke 2 | 12 % → 12 % | 87.1 px | 0.71 | 1.00 | 198 |
| stroke 3 | 28 % → 37 % | 100.9 px | 0.72 | 1.31 | 254 |
| stroke 4 | 23 % → 23 % | 163.9 px | 0.71 | 1.02 | 209 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #30 Red gouache face patch — own sheet
own sheet 600 × 600 · Gouache · 60 px · 13.5 s

![Brush Artist · Refs · #30 Red gouache face patch — own sheet](Brush-Artist-Refs-30-Red-gouache-face-patch-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 12 % → 37 % | 51.5 px | 0.53 | 3.23 | 191 |
| stroke 2 | 15 % → 40 % | 74.5 px | 0.53 | 2.72 | 217 |
| stroke 3 | 24 % → 50 % | 115.9 px | 0.53 | 2.06 | 170 |
| stroke 4 | 27 % → 51 % | 134.0 px | 0.53 | 1.93 | 160 |
| stroke 5 | 34 % → 60 % | 159.9 px | 0.53 | 1.77 | 208 |
| stroke 6 | 35 % → 61 % | 178.2 px | 0.53 | 1.76 | 250 |
| stroke 7 | 34 % → 59 % | 160.8 px | 0.53 | 1.73 | 246 |
| stroke 8 | 34 % → 56 % | 162.4 px | 0.53 | 1.65 | 252 |
| stroke 9 | 36 % → 60 % | 173.0 px | 0.53 | 1.66 | 268 |
| stroke 10 | 38 % → 62 % | 196.7 px | 0.53 | 1.64 | 288 |
| stroke 11 | 37 % → 61 % | 182.4 px | 0.53 | 1.66 | 286 |
| stroke 12 | 36 % → 58 % | 178.3 px | 0.53 | 1.62 | 204 |
| stroke 13 | 33 % → 46 % | 156.5 px | 0.53 | 1.39 | 186 |
| stroke 14 | 33 % → 41 % | 157.6 px | 0.53 | 1.25 | 266 |
| stroke 15 | 33 % → 37 % | 153.3 px | 0.53 | 1.12 | 234 |
| stroke 16 | 39 % → 39 % | 184.8 px | 0.53 | 0.99 | 158 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #31 Warhol blotted line — own sheet
own sheet 600 × 600 · Ink · 6 px · 5.1 s

![Brush Artist · Refs · #31 Warhol blotted line — own sheet](Brush-Artist-Refs-31-Warhol-blotted-line-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 21 % → 42 % | 15.7 px | 0.82 | 1.98 | 120 |
| stroke 2 | 17 % → 23 % | 15.8 px | 0.82 | 1.34 | 92 |
| stroke 3 | 24 % → 25 % | 25.0 px | 0.82 | 1.02 | 96 |
| stroke 4 | 31 % → 40 % | 31.7 px | 0.82 | 1.28 | 51 |
| stroke 5 | 35 % → 43 % | 36.3 px | 0.82 | 1.23 | 74 |
| stroke 6 | 32 % → 33 % | 26.5 px | 0.81 | 1.03 | 94 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #32 Thick orange swipes — own sheet
own sheet 600 × 600 · Heavy acrylic · 90 px · 3.9 s

![Brush Artist · Refs · #32 Thick orange swipes — own sheet](Brush-Artist-Refs-32-Thick-orange-swipes-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 14 % → 27 % | 86.0 px | 0.03 | 1.90 | 390 |
| stroke 2 | 26 % → 38 % | 176.9 px | 0.03 | 1.43 | 385 |
| stroke 3 | 28 % → 27 % | 177.5 px | 0.03 | 0.98 | 343 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #33 Red wet-in-wet band — own sheet
own sheet 600 × 600 · Watercolor · 80 px · 11.2 s

![Brush Artist · Refs · #33 Red wet-in-wet band — own sheet](Brush-Artist-Refs-33-Red-wet-in-wet-band-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 23 % → 56 % | 88.2 px | 0.62 | 2.41 | 333 |
| stroke 2 | 30 % → 51 % | 243.8 px | 0.62 | 1.69 | 101 |
| stroke 3 | 37 % → 53 % | 355.7 px | 0.62 | 1.45 | 96 |
| stroke 4 | 42 % → 60 % | 410.7 px | 0.63 | 1.41 | 92 |
| stroke 5 | 42 % → 54 % | 352.8 px | 0.62 | 1.31 | 107 |
| stroke 6 | 42 % → 46 % | 320.2 px | 0.61 | 1.10 | 104 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #34 Magenta oil patches — own sheet
own sheet 600 × 600 · Oil · 60 px · 5.3 s

![Brush Artist · Refs · #34 Magenta oil patches — own sheet](Brush-Artist-Refs-34-Magenta-oil-patches-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 9 % → 42 % | 61.9 px | 0.13 | 4.82 | 92 |
| stroke 2 | 9 % → 29 % | 62.8 px | 0.13 | 3.15 | 74 |
| stroke 3 | 7 % → 35 % | 62.3 px | 0.13 | 4.71 | 66 |
| stroke 4 | 16 % → 20 % | 132.0 px | 0.12 | 1.27 | 57 |
| stroke 5 | 23 % → 33 % | 124.6 px | 0.13 | 1.43 | 106 |
| stroke 6 | 20 % → 38 % | 171.4 px | 0.13 | 1.90 | 66 |
| stroke 7 | 30 % → 35 % | 237.9 px | 0.13 | 1.18 | 76 |
| stroke 8 | 33 % → 39 % | 235.0 px | 0.13 | 1.18 | 104 |
| stroke 9 | 25 % → 26 % | 159.7 px | 0.13 | 1.07 | 100 |
| stroke 10 | 29 % → 29 % | 257.2 px | 0.13 | 1.00 | 72 |
| stroke 11 | 36 % → 36 % | 324.6 px | 0.13 | 1.00 | 67 |
| stroke 12 | 26 % → 26 % | 184.4 px | 0.13 | 1.00 | 70 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #35 Red band with runs — own sheet
own sheet 600 × 600 · Watercolor · 70 px · 7.0 s

![Brush Artist · Refs · #35 Red band with runs — own sheet](Brush-Artist-Refs-35-Red-band-with-runs-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 21 % → 32 % | 77.5 px | 0.50 | 1.54 | 269 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #36 Magenta letters flat brush — own sheet
own sheet 600 × 600 · Gouache · 36 px · 14.4 s

![Brush Artist · Refs · #36 Magenta letters flat brush — own sheet](Brush-Artist-Refs-36-Magenta-letters-flat-brush-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 20 % → 39 % | 59.1 px | 0.50 | 1.95 | 53 |
| stroke 2 | 20 % → 32 % | 46.7 px | 0.50 | 1.59 | 31 |
| stroke 3 | 29 % → 54 % | 86.9 px | 0.50 | 1.86 | 31 |
| stroke 4 | 26 % → 44 % | 51.2 px | 0.50 | 1.67 | 110 |
| stroke 5 | 33 % → 55 % | 96.1 px | 0.50 | 1.67 | 74 |
| stroke 6 | 42 % → 56 % | 242.5 px | 0.50 | 1.33 | 18 |
| stroke 7 | 30 % → 44 % | 56.7 px | 0.50 | 1.45 | 125 |
| stroke 8 | 31 % → 53 % | 98.5 px | 0.50 | 1.68 | 86 |
| stroke 9 | 38 % → 51 % | 158.3 px | 0.50 | 1.33 | 58 |
| stroke 10 | 37 % → 63 % | 106.7 px | 0.50 | 1.72 | 146 |
| stroke 11 | 39 % → 62 % | 225.9 px | 0.50 | 1.58 | 34 |
| stroke 12 | 43 % → 56 % | 81.8 px | 0.50 | 1.29 | 207 |
| stroke 13 | 33 % → 46 % | 117.7 px | 0.50 | 1.43 | 50 |
| stroke 14 | 35 % → 52 % | 134.5 px | 0.50 | 1.47 | 58 |
| stroke 15 | 38 % → 56 % | 108.5 px | 0.50 | 1.49 | 94 |
| stroke 16 | 41 % → 50 % | 231.8 px | 0.50 | 1.23 | 15 |
| stroke 17 | 44 % → 52 % | 81.6 px | 0.50 | 1.19 | 146 |
| stroke 18 | 27 % → 36 % | 97.6 px | 0.50 | 1.35 | 39 |
| stroke 19 | 40 % → 39 % | 117.2 px | 0.50 | 0.96 | 37 |
| stroke 20 | 45 % → 45 % | 132.3 px | 0.50 | 0.98 | 36 |
| stroke 21 | 41 % → 39 % | 78.6 px | 0.50 | 0.96 | 226 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #37 Oil still life dabs — own sheet
own sheet 600 × 600 · Oil · 40 px · 4.4 s

![Brush Artist · Refs · #37 Oil still life dabs — own sheet](Brush-Artist-Refs-37-Oil-still-life-dabs-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 7 % → 7 % | 44.1 px | 0.39 | 1.00 | 41 |
| stroke 2 | 6 % → 27 % | 44.4 px | 0.39 | 4.43 | 31 |
| stroke 3 | 12 % → 36 % | 92.6 px | 0.39 | 3.01 | 33 |
| stroke 4 | 9 % → 9 % | 42.7 px | 0.39 | 1.00 | 49 |
| stroke 5 | 6 % → 10 % | 43.2 px | 0.39 | 1.71 | 21 |
| stroke 6 | 13 % → 31 % | 83.4 px | 0.39 | 2.32 | 39 |
| stroke 7 | 11 % → 24 % | 115.5 px | 0.39 | 2.18 | 20 |
| stroke 8 | 8 % → 14 % | 89.6 px | 0.39 | 1.63 | 13 |
| stroke 9 | 13 % → 14 % | 68.1 px | 0.38 | 1.09 | 55 |
| stroke 10 | 21 % → 25 % | 106.5 px | 0.39 | 1.20 | 76 |
| stroke 11 | 24 % → 28 % | 201.6 px | 0.39 | 1.17 | 72 |
| stroke 12 | 21 % → 21 % | 227.4 px | 0.39 | 1.01 | 35 |
| stroke 13 | 16 % → 16 % | 167.7 px | 0.40 | 1.00 | 19 |
| stroke 14 | 16 % → 16 % | 132.7 px | 0.39 | 1.00 | 23 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #38 Sanguine drawing — own sheet
own sheet 600 × 600 · Pastel · 6 px · 2.6 s

![Brush Artist · Refs · #38 Sanguine drawing — own sheet](Brush-Artist-Refs-38-Sanguine-drawing-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 3 % → 14 % | 2.9 px | 0.57 | 5.29 | 18 |
| stroke 2 | 3 % → 7 % | 2.9 px | 0.57 | 2.89 | 8 |
| stroke 3 | 3 % → 9 % | 2.9 px | 0.57 | 3.40 | 6 |
| stroke 4 | 2 % → 17 % | 2.7 px | 0.57 | 7.20 | 6 |
| stroke 5 | 2 % → 7 % | 2.7 px | 0.57 | 3.03 | 6 |
| stroke 6 | 3 % → 19 % | 3.4 px | 0.57 | 6.31 | 6 |
| stroke 7 | 5 % → 14 % | 5.2 px | 0.57 | 3.07 | 6 |
| stroke 8 | 4 % → 16 % | 4.7 px | 0.57 | 3.79 | 10 |
| stroke 9 | 3 % → 7 % | 2.9 px | 0.57 | 2.66 | 6 |
| stroke 10 | 4 % → 16 % | 4.7 px | 0.57 | 3.83 | 10 |
| stroke 11 | 3 % → 4 % | 2.9 px | 0.57 | 1.61 | 11 |
| stroke 12 | 4 % → 15 % | 4.8 px | 0.57 | 3.58 | 7 |
| stroke 13 | 8 % → 17 % | 8.9 px | 0.57 | 2.23 | 8 |
| stroke 14 | 4 % → 14 % | 4.9 px | 0.57 | 3.19 | 6 |
| stroke 15 | 9 % → 18 % | 10.7 px | 0.57 | 1.86 | 7 |
| stroke 16 | 6 % → 16 % | 6.6 px | 0.57 | 2.71 | 6 |
| stroke 17 | 4 % → 9 % | 4.4 px | 0.57 | 2.25 | 6 |
| stroke 18 | 3 % → 5 % | 2.9 px | 0.57 | 1.85 | 6 |
| stroke 19 | 6 % → 16 % | 6.9 px | 0.57 | 2.68 | 8 |
| stroke 20 | 8 % → 14 % | 9.2 px | 0.57 | 1.70 | 6 |
| stroke 21 | 4 % → 4 % | 4.3 px | 0.57 | 1.00 | 7 |
| stroke 22 | 8 % → 13 % | 8.6 px | 0.57 | 1.79 | 14 |
| stroke 23 | 7 % → 12 % | 8.3 px | 0.57 | 1.61 | 6 |
| stroke 24 | 4 % → 7 % | 4.7 px | 0.57 | 1.71 | 7 |
| stroke 25 | 8 % → 14 % | 8.7 px | 0.57 | 1.84 | 9 |
| stroke 26 | 6 % → 8 % | 6.5 px | 0.57 | 1.34 | 7 |
| stroke 27 | 4 % → 4 % | 4.3 px | 0.57 | 1.10 | 7 |
| stroke 28 | 7 % → 11 % | 8.2 px | 0.57 | 1.59 | 8 |
| stroke 29 | 8 % → 17 % | 8.8 px | 0.57 | 2.21 | 8 |
| stroke 30 | 13 % → 17 % | 14.9 px | 0.57 | 1.29 | 9 |
| stroke 31 | 5 % → 6 % | 5.4 px | 0.57 | 1.29 | 6 |
| stroke 32 | 10 % → 13 % | 11.8 px | 0.57 | 1.24 | 6 |
| stroke 33 | 7 % → 8 % | 8.5 px | 0.57 | 1.07 | 8 |
| stroke 34 | 11 % → 14 % | 12.0 px | 0.57 | 1.36 | 7 |
| stroke 35 | 9 % → 14 % | 10.0 px | 0.57 | 1.61 | 6 |
| stroke 36 | 10 % → 13 % | 11.4 px | 0.57 | 1.26 | 6 |
| stroke 37 | 9 % → 16 % | 10.5 px | 0.57 | 1.71 | 7 |
| stroke 38 | 13 % → 19 % | 14.8 px | 0.57 | 1.48 | 7 |
| stroke 39 | 14 % → 17 % | 15.7 px | 0.57 | 1.21 | 12 |
| stroke 40 | 6 % → 7 % | 7.2 px | 0.57 | 1.14 | 7 |
| stroke 41 | 16 % → 16 % | 17.7 px | 0.57 | 1.01 | 9 |
| stroke 42 | 14 % → 16 % | 15.2 px | 0.57 | 1.17 | 7 |
| stroke 43 | 10 % → 12 % | 11.6 px | 0.57 | 1.17 | 12 |
| stroke 44 | 12 % → 15 % | 14.3 px | 0.57 | 1.22 | 6 |
| stroke 45 | 2 % → 2 % | 2.7 px | 0.57 | 1.00 | 8 |
| stroke 46 | 16 % → 16 % | 18.5 px | 0.57 | 1.00 | 6 |
| stroke 47 | 13 % → 13 % | 15.0 px | 0.57 | 1.00 | 6 |
| stroke 48 | 12 % → 13 % | 14.3 px | 0.57 | 1.07 | 7 |
| stroke 49 | 19 % → 19 % | 21.5 px | 0.57 | 1.00 | 6 |
| stroke 50 | 10 % → 10 % | 11.6 px | 0.57 | 1.00 | 7 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #39 Very thick impasto — own sheet
own sheet 600 × 600 · Heavy acrylic · 60 px · 6.3 s

![Brush Artist · Refs · #39 Very thick impasto — own sheet](Brush-Artist-Refs-39-Very-thick-impasto-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 26 % → 37 % | 59.6 px | 0.43 | 1.42 | 332 |
| stroke 2 | 31 % → 48 % | 93.9 px | 0.44 | 1.54 | 320 |
| stroke 3 | 37 % → 49 % | 124.6 px | 0.43 | 1.33 | 281 |
| stroke 4 | 31 % → 44 % | 90.9 px | 0.44 | 1.41 | 490 |
| stroke 5 | 42 % → 41 % | 104.2 px | 0.44 | 0.98 | 519 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #40 Watercolour blooms — own sheet
own sheet 600 × 600 · Watercolor · 90 px · 8.5 s

![Brush Artist · Refs · #40 Watercolour blooms — own sheet](Brush-Artist-Refs-40-Watercolour-blooms-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 21 % → 25 % | 92.4 px | 0.13 | 1.19 | 777 |

## Brush Artist · Refs · #41 Coloured pencil hatching — own sheet
own sheet 600 × 600 · Pastel · 4 px · 2.9 s

![Brush Artist · Refs · #41 Coloured pencil hatching — own sheet](Brush-Artist-Refs-41-Coloured-pencil-hatching-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 3 % → 13 % | 2.2 px | 0.35 | 4.64 | 7 |
| stroke 2 | 3 % → 7 % | 2.3 px | 0.35 | 2.29 | 4 |
| stroke 3 | 2 % → 11 % | 1.9 px | 0.35 | 4.38 | 4 |
| stroke 4 | 3 % → 19 % | 2.1 px | 0.35 | 6.73 | 4 |
| stroke 5 | 4 % → 7 % | 2.9 px | 0.35 | 1.83 | 5 |
| stroke 6 | 3 % → 13 % | 2.3 px | 0.35 | 4.19 | 4 |
| stroke 7 | 3 % → 15 % | 2.6 px | 0.35 | 4.43 | 4 |
| stroke 8 | 3 % → 12 % | 2.1 px | 0.35 | 4.20 | 5 |
| stroke 9 | 5 % → 11 % | 3.6 px | 0.35 | 2.27 | 5 |
| stroke 10 | 5 % → 15 % | 3.8 px | 0.35 | 2.99 | 7 |
| stroke 11 | 4 % → 13 % | 3.0 px | 0.35 | 3.28 | 5 |
| stroke 12 | 3 % → 3 % | 2.1 px | 0.35 | 1.00 | 9 |
| stroke 13 | 7 % → 17 % | 5.2 px | 0.35 | 2.45 | 7 |
| stroke 14 | 3 % → 13 % | 2.4 px | 0.35 | 4.19 | 5 |
| stroke 15 | 6 % → 12 % | 4.4 px | 0.35 | 2.09 | 8 |
| stroke 16 | 7 % → 11 % | 5.1 px | 0.35 | 1.61 | 8 |
| stroke 17 | 3 % → 3 % | 2.1 px | 0.35 | 1.00 | 6 |
| stroke 18 | 5 % → 8 % | 3.6 px | 0.35 | 1.65 | 4 |
| stroke 19 | 5 % → 13 % | 3.8 px | 0.35 | 2.72 | 8 |
| stroke 20 | 5 % → 14 % | 3.7 px | 0.35 | 2.92 | 9 |
| stroke 21 | 4 % → 13 % | 3.2 px | 0.35 | 3.20 | 5 |
| stroke 22 | 9 % → 16 % | 6.8 px | 0.35 | 1.77 | 10 |
| stroke 23 | 9 % → 13 % | 6.5 px | 0.35 | 1.55 | 5 |
| stroke 24 | 6 % → 14 % | 4.7 px | 0.35 | 2.18 | 5 |
| stroke 25 | 5 % → 10 % | 3.5 px | 0.35 | 2.27 | 4 |
| stroke 26 | 3 % → 6 % | 2.7 px | 0.35 | 1.81 | 4 |
| stroke 27 | 3 % → 7 % | 2.3 px | 0.35 | 2.26 | 4 |
| stroke 28 | 6 % → 10 % | 4.5 px | 0.35 | 1.70 | 5 |
| stroke 29 | 3 % → 13 % | 2.4 px | 0.35 | 4.21 | 12 |
| stroke 30 | 6 % → 9 % | 4.4 px | 0.35 | 1.46 | 13 |
| stroke 31 | 7 % → 14 % | 5.1 px | 0.35 | 2.14 | 5 |
| stroke 32 | 3 % → 6 % | 2.5 px | 0.35 | 1.79 | 6 |
| stroke 33 | 6 % → 11 % | 5.0 px | 0.35 | 1.67 | 7 |
| stroke 34 | 3 % → 6 % | 2.6 px | 0.35 | 1.73 | 6 |
| stroke 35 | 7 % → 14 % | 5.0 px | 0.35 | 2.09 | 6 |
| stroke 36 | 5 % → 5 % | 3.7 px | 0.35 | 1.01 | 4 |
| stroke 37 | 7 % → 15 % | 5.2 px | 0.35 | 2.15 | 8 |
| stroke 38 | 8 % → 13 % | 5.8 px | 0.35 | 1.66 | 4 |
| stroke 39 | 7 % → 11 % | 5.1 px | 0.35 | 1.67 | 4 |
| stroke 40 | 8 % → 18 % | 6.2 px | 0.35 | 2.21 | 5 |
| stroke 41 | 9 % → 13 % | 6.9 px | 0.35 | 1.48 | 5 |
| stroke 42 | 10 % → 17 % | 7.7 px | 0.35 | 1.73 | 5 |
| stroke 43 | 5 % → 9 % | 3.9 px | 0.35 | 1.66 | 6 |
| stroke 44 | 10 % → 13 % | 7.3 px | 0.35 | 1.40 | 4 |
| stroke 45 | 13 % → 18 % | 9.9 px | 0.35 | 1.35 | 5 |
| stroke 46 | 5 % → 7 % | 3.6 px | 0.34 | 1.41 | 6 |
| stroke 47 | 11 % → 13 % | 8.0 px | 0.35 | 1.20 | 9 |
| stroke 48 | 12 % → 16 % | 9.2 px | 0.35 | 1.34 | 5 |
| stroke 49 | 6 % → 9 % | 4.2 px | 0.35 | 1.66 | 5 |
| stroke 50 | 7 % → 7 % | 5.2 px | 0.34 | 1.00 | 5 |
| stroke 51 | 8 % → 15 % | 6.4 px | 0.35 | 1.74 | 6 |
| stroke 52 | 12 % → 14 % | 9.1 px | 0.35 | 1.19 | 5 |
| stroke 53 | 11 % → 14 % | 8.1 px | 0.35 | 1.36 | 5 |
| stroke 54 | 10 % → 14 % | 7.4 px | 0.35 | 1.47 | 5 |
| stroke 55 | 11 % → 14 % | 8.2 px | 0.35 | 1.33 | 5 |
| stroke 56 | 11 % → 12 % | 8.4 px | 0.35 | 1.11 | 7 |
| stroke 57 | 9 % → 13 % | 7.1 px | 0.35 | 1.37 | 8 |
| stroke 58 | 10 % → 11 % | 7.7 px | 0.35 | 1.14 | 8 |
| stroke 59 | 11 % → 13 % | 8.4 px | 0.35 | 1.18 | 5 |
| stroke 60 | 16 % → 20 % | 11.9 px | 0.35 | 1.26 | 5 |
| stroke 61 | 19 % → 20 % | 14.5 px | 0.35 | 1.04 | 5 |
| stroke 62 | 10 % → 10 % | 7.3 px | 0.35 | 1.00 | 6 |
| stroke 63 | 11 % → 12 % | 8.7 px | 0.35 | 1.07 | 5 |
| stroke 64 | 14 % → 14 % | 10.7 px | 0.35 | 1.02 | 4 |
| stroke 65 | 15 % → 15 % | 11.5 px | 0.35 | 1.00 | 6 |
| stroke 66 | 14 % → 14 % | 10.7 px | 0.35 | 1.00 | 5 |
| stroke 67 | 12 % → 12 % | 8.8 px | 0.35 | 1.06 | 4 |
| stroke 68 | 5 % → 9 % | 3.6 px | 0.35 | 1.88 | 4 |
| stroke 69 | 5 % → 5 % | 4.1 px | 0.35 | 1.00 | 4 |
| stroke 70 | 10 % → 13 % | 7.4 px | 0.35 | 1.28 | 4 |
| stroke 71 | 9 % → 11 % | 7.1 px | 0.35 | 1.15 | 5 |
| stroke 72 | 5 % → 7 % | 4.2 px | 0.35 | 1.23 | 5 |
| stroke 73 | 12 % → 12 % | 9.3 px | 0.35 | 1.00 | 4 |
| stroke 74 | 14 % → 14 % | 10.8 px | 0.35 | 1.00 | 5 |
| stroke 75 | 15 % → 15 % | 11.4 px | 0.35 | 1.00 | 5 |
| stroke 76 | 14 % → 14 % | 10.5 px | 0.35 | 1.00 | 6 |
| stroke 77 | 7 % → 10 % | 5.4 px | 0.35 | 1.34 | 7 |
| stroke 78 | 9 % → 9 % | 7.0 px | 0.35 | 1.00 | 5 |
| stroke 79 | 7 % → 7 % | 5.7 px | 0.35 | 1.00 | 5 |
| stroke 80 | 11 % → 11 % | 8.3 px | 0.35 | 1.00 | 5 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #42 Oil pastel shaggy — own sheet
own sheet 600 × 600 · Pastel · 18 px · 3.1 s

![Brush Artist · Refs · #42 Oil pastel shaggy — own sheet](Brush-Artist-Refs-42-Oil-pastel-shaggy-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 5 % → 27 % | 8.0 px | 0.28 | 5.73 | 22 |
| stroke 2 | 5 % → 24 % | 8.6 px | 0.28 | 4.69 | 12 |
| stroke 3 | 5 % → 29 % | 8.9 px | 0.28 | 5.42 | 21 |
| stroke 4 | 5 % → 11 % | 8.8 px | 0.28 | 2.08 | 13 |
| stroke 5 | 6 % → 11 % | 9.9 px | 0.28 | 1.85 | 17 |
| stroke 6 | 8 % → 37 % | 13.9 px | 0.29 | 4.44 | 11 |
| stroke 7 | 11 % → 31 % | 17.6 px | 0.28 | 2.90 | 18 |
| stroke 8 | 7 % → 38 % | 11.4 px | 0.28 | 5.55 | 10 |
| stroke 9 | 8 % → 21 % | 13.9 px | 0.28 | 2.53 | 11 |
| stroke 10 | 8 % → 18 % | 13.2 px | 0.28 | 2.32 | 10 |
| stroke 11 | 6 % → 27 % | 9.4 px | 0.28 | 4.74 | 10 |
| stroke 12 | 8 % → 19 % | 13.6 px | 0.28 | 2.29 | 10 |
| stroke 13 | 13 % → 24 % | 21.0 px | 0.28 | 1.92 | 11 |
| stroke 14 | 5 % → 23 % | 7.9 px | 0.28 | 4.77 | 12 |
| stroke 15 | 5 % → 24 % | 9.0 px | 0.29 | 4.38 | 20 |
| stroke 16 | 9 % → 21 % | 15.7 px | 0.29 | 2.18 | 14 |
| stroke 17 | 17 % → 39 % | 27.9 px | 0.29 | 2.34 | 17 |
| stroke 18 | 14 % → 25 % | 22.8 px | 0.29 | 1.79 | 11 |
| stroke 19 | 15 % → 32 % | 24.9 px | 0.28 | 2.09 | 13 |
| stroke 20 | 21 % → 39 % | 35.1 px | 0.28 | 1.85 | 10 |
| stroke 21 | 9 % → 16 % | 14.4 px | 0.28 | 1.88 | 11 |
| stroke 22 | 14 % → 17 % | 23.9 px | 0.28 | 1.20 | 16 |
| stroke 23 | 12 % → 17 % | 20.6 px | 0.29 | 1.34 | 10 |
| stroke 24 | 18 % → 26 % | 30.0 px | 0.29 | 1.44 | 10 |
| stroke 25 | 20 % → 34 % | 32.6 px | 0.28 | 1.74 | 16 |
| stroke 26 | 6 % → 14 % | 9.2 px | 0.28 | 2.43 | 12 |
| stroke 27 | 18 % → 26 % | 30.4 px | 0.29 | 1.41 | 11 |
| stroke 28 | 14 % → 24 % | 23.7 px | 0.28 | 1.68 | 13 |
| stroke 29 | 9 % → 27 % | 14.9 px | 0.29 | 3.01 | 12 |
| stroke 30 | 15 % → 36 % | 24.9 px | 0.29 | 2.43 | 15 |
| stroke 31 | 14 % → 17 % | 23.3 px | 0.28 | 1.23 | 12 |
| stroke 32 | 16 % → 29 % | 27.0 px | 0.29 | 1.82 | 13 |
| stroke 33 | 15 % → 16 % | 24.5 px | 0.29 | 1.09 | 15 |
| stroke 34 | 19 % → 27 % | 31.4 px | 0.28 | 1.44 | 12 |
| stroke 35 | 26 % → 36 % | 42.5 px | 0.28 | 1.40 | 10 |
| stroke 36 | 25 % → 34 % | 41.0 px | 0.28 | 1.36 | 10 |
| stroke 37 | 12 % → 12 % | 19.3 px | 0.28 | 1.03 | 11 |
| stroke 38 | 19 % → 25 % | 31.7 px | 0.28 | 1.30 | 12 |
| stroke 39 | 16 % → 22 % | 27.3 px | 0.28 | 1.37 | 10 |
| stroke 40 | 22 % → 31 % | 36.6 px | 0.28 | 1.38 | 10 |
| stroke 41 | 32 % → 36 % | 53.1 px | 0.28 | 1.12 | 12 |
| stroke 42 | 23 % → 30 % | 38.1 px | 0.29 | 1.29 | 12 |
| stroke 43 | 12 % → 12 % | 20.3 px | 0.28 | 1.00 | 12 |
| stroke 44 | 30 % → 37 % | 48.9 px | 0.28 | 1.26 | 13 |
| stroke 45 | 16 % → 16 % | 26.2 px | 0.28 | 1.00 | 10 |
| stroke 46 | 29 % → 34 % | 47.9 px | 0.29 | 1.15 | 11 |
| stroke 47 | 38 % → 41 % | 62.0 px | 0.28 | 1.10 | 11 |
| stroke 48 | 29 % → 36 % | 47.8 px | 0.29 | 1.27 | 11 |
| stroke 49 | 27 % → 30 % | 45.1 px | 0.29 | 1.11 | 10 |
| stroke 50 | 38 % → 40 % | 63.4 px | 0.28 | 1.06 | 12 |
| stroke 51 | 16 % → 16 % | 26.0 px | 0.28 | 1.00 | 10 |
| stroke 52 | 37 % → 38 % | 62.4 px | 0.29 | 1.01 | 12 |
| stroke 53 | 22 % → 26 % | 36.9 px | 0.28 | 1.18 | 10 |
| stroke 54 | 17 % → 19 % | 29.0 px | 0.29 | 1.09 | 17 |
| stroke 55 | 15 % → 15 % | 25.0 px | 0.28 | 1.00 | 11 |
| stroke 56 | 13 % → 14 % | 21.6 px | 0.28 | 1.08 | 14 |
| stroke 57 | 23 % → 23 % | 37.7 px | 0.29 | 1.00 | 10 |
| stroke 58 | 28 % → 29 % | 46.1 px | 0.28 | 1.05 | 11 |
| stroke 59 | 40 % → 40 % | 67.3 px | 0.28 | 1.00 | 10 |
| stroke 60 | 22 % → 22 % | 35.6 px | 0.28 | 1.00 | 10 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #43 Dragged black ink blocks — own sheet
own sheet 600 × 600 · Gouache · 70 px · 9.7 s

![Brush Artist · Refs · #43 Dragged black ink blocks — own sheet](Brush-Artist-Refs-43-Dragged-black-ink-blocks-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 29 % → 29 % | 66.4 px | 0.42 | 1.00 | 459 |
| stroke 2 | 30 % → 31 % | 105.8 px | 0.42 | 1.02 | 544 |
| stroke 3 | 37 % → 36 % | 132.0 px | 0.42 | 0.99 | 456 |
| stroke 4 | 37 % → 34 % | 128.9 px | 0.42 | 0.93 | 432 |
| stroke 5 | 44 % → 30 % | 103.8 px | 0.42 | 0.66 | 543 |

## Brush Artist · Refs · #44 Blue looping ribbon — own sheet
own sheet 600 × 600 · Oil · 80 px · 5.3 s

![Brush Artist · Refs · #44 Blue looping ribbon — own sheet](Brush-Artist-Refs-44-Blue-looping-ribbon-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 32 % → 32 % | 42.2 px | 0.78 | 1.00 | 2743 |

## Brush Artist · Refs · #45 Soft pastel pepper — own sheet
own sheet 600 × 600 · Pastel · 40 px · 4.7 s

![Brush Artist · Refs · #45 Soft pastel pepper — own sheet](Brush-Artist-Refs-45-Soft-pastel-pepper-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 10 % → 40 % | 11.3 px | 0.49 | 3.87 | 396 |
| stroke 2 | 18 % → 34 % | 21.3 px | 0.49 | 1.90 | 376 |
| stroke 3 | 25 % → 38 % | 17.6 px | 0.49 | 1.48 | 296 |
| stroke 4 | 24 % → 36 % | 30.5 px | 0.49 | 1.46 | 338 |
| stroke 5 | 30 % → 30 % | 21.2 px | 0.49 | 1.00 | 224 |
| stroke 6 | 39 % → 46 % | 24.6 px | 0.49 | 1.20 | 267 |
| stroke 7 | 41 % → 45 % | 22.6 px | 0.49 | 1.11 | 399 |
| stroke 8 | 45 % → 45 % | 45.8 px | 0.49 | 1.00 | 341 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #46 Red-brown ink lips — own sheet
own sheet 600 × 600 · Watercolor · 50 px · 5.8 s

![Brush Artist · Refs · #46 Red-brown ink lips — own sheet](Brush-Artist-Refs-46-Red-brown-ink-lips-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 12 % → 23 % | 51.9 px | 0.60 | 1.87 | 122 |
| stroke 2 | 16 % → 26 % | 68.2 px | 0.55 | 1.67 | 77 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #47 Pink knife slabs — own sheet
own sheet 600 × 600 · Heavy acrylic · 90 px · 5.2 s

![Brush Artist · Refs · #47 Pink knife slabs — own sheet](Brush-Artist-Refs-47-Pink-knife-slabs-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 17 % → 32 % | 83.2 px | 0.11 | 1.94 | 306 |
| stroke 2 | 29 % → 43 % | 165.7 px | 0.11 | 1.46 | 301 |
| stroke 3 | 29 % → 43 % | 165.6 px | 0.11 | 1.47 | 450 |
| stroke 4 | 39 % → 38 % | 165.6 px | 0.11 | 0.98 | 335 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #48 Black bands with drips — own sheet
own sheet 600 × 600 · Gouache · 70 px · 11.7 s

![Brush Artist · Refs · #48 Black bands with drips — own sheet](Brush-Artist-Refs-48-Black-bands-with-drips-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 23 % → 36 % | 58.8 px | 0.39 | 1.58 | 512 |
| stroke 2 | 34 % → 47 % | 108.3 px | 0.39 | 1.41 | 483 |
| stroke 3 | 36 % → 48 % | 112.5 px | 0.39 | 1.34 | 451 |
| stroke 4 | 38 % → 36 % | 111.4 px | 0.39 | 0.95 | 617 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #49 Magenta letters round brush — own sheet
own sheet 600 × 600 · Ink · 30 px · 11.3 s

![Brush Artist · Refs · #49 Magenta letters round brush — own sheet](Brush-Artist-Refs-49-Magenta-letters-round-brush-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 27 % → 46 % | 64.3 px | 0.52 | 1.69 | 35 |
| stroke 2 | 29 % → 40 % | 52.5 px | 0.53 | 1.39 | 29 |
| stroke 3 | 41 % → 67 % | 96.4 px | 0.52 | 1.64 | 27 |
| stroke 4 | 34 % → 52 % | 53.7 px | 0.52 | 1.55 | 107 |
| stroke 5 | 40 % → 66 % | 94.7 px | 0.52 | 1.65 | 71 |
| stroke 6 | 54 % → 70 % | 231.1 px | 0.52 | 1.29 | 17 |
| stroke 7 | 41 % → 56 % | 63.9 px | 0.52 | 1.35 | 117 |
| stroke 8 | 36 % → 61 % | 91.9 px | 0.53 | 1.72 | 60 |
| stroke 9 | 49 % → 60 % | 152.9 px | 0.53 | 1.24 | 24 |
| stroke 10 | 42 % → 72 % | 100.4 px | 0.52 | 1.71 | 84 |
| stroke 11 | 52 % → 72 % | 219.5 px | 0.52 | 1.39 | 16 |
| stroke 12 | 53 % → 68 % | 82.2 px | 0.52 | 1.29 | 111 |
| stroke 13 | 42 % → 54 % | 116.0 px | 0.53 | 1.29 | 60 |
| stroke 14 | 45 % → 69 % | 131.9 px | 0.53 | 1.52 | 38 |
| stroke 15 | 43 % → 63 % | 102.4 px | 0.52 | 1.46 | 100 |
| stroke 16 | 52 % → 61 % | 220.2 px | 0.52 | 1.18 | 28 |
| stroke 17 | 53 % → 64 % | 82.2 px | 0.52 | 1.19 | 108 |
| stroke 18 | 36 % → 44 % | 99.6 px | 0.52 | 1.21 | 51 |
| stroke 19 | 54 % → 53 % | 123.8 px | 0.52 | 0.99 | 36 |
| stroke 20 | 54 % → 54 % | 125.3 px | 0.52 | 1.00 | 29 |
| stroke 21 | 49 % → 49 % | 81.3 px | 0.52 | 1.00 | 96 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #50 Thick swipes on photo — own sheet
own sheet 600 × 600 · Heavy acrylic · 40 px · 3.3 s

![Brush Artist · Refs · #50 Thick swipes on photo — own sheet](Brush-Artist-Refs-50-Thick-swipes-on-photo-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 9 % → 21 % | 42.6 px | 0.33 | 2.35 | 36 |
| stroke 2 | 9 % → 16 % | 42.4 px | 0.33 | 1.79 | 29 |
| stroke 3 | 10 % → 11 % | 41.8 px | 0.33 | 1.06 | 41 |
| stroke 4 | 11 % → 18 % | 42.6 px | 0.33 | 1.64 | 39 |
| stroke 5 | 11 % → 10 % | 41.8 px | 0.33 | 0.95 | 35 |
| stroke 6 | 17 % → 21 % | 97.3 px | 0.32 | 1.20 | 27 |
| stroke 7 | 22 % → 26 % | 92.7 px | 0.33 | 1.18 | 37 |
| stroke 8 | 21 % → 21 % | 119.6 px | 0.33 | 0.97 | 37 |
| stroke 9 | 9 % → 10 % | 42.0 px | 0.32 | 1.09 | 38 |
| stroke 10 | 22 % → 21 % | 73.6 px | 0.32 | 0.96 | 37 |
| stroke 11 | 9 % → 8 % | 42.6 px | 0.33 | 0.95 | 30 |
| stroke 12 | 17 % → 16 % | 93.0 px | 0.33 | 0.96 | 24 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Ink — dry brush — own sheet
own sheet 600 × 600 · Gouache · 30 px · 3.7 s

![Brush Artist · Ink — dry brush — own sheet](Brush-Artist-Ink-dry-brush-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| ear | 13 % → 4 % | 16.7 px | 0.82 | 0.32 | 606 |
| drag0 | 14 % → 16 % | 25.0 px | 0.82 | 1.22 | 201 |
| drag1 | 17 % → 18 % | 35.3 px | 0.82 | 1.02 | 133 |
| drag2 | 20 % → 18 % | 45.7 px | 0.82 | 0.91 | 145 |
| drag3 | 22 % → 19 % | 56.9 px | 0.82 | 0.84 | 90 |

## Brush Artist · Watercolour — blue — own sheet
own sheet 600 × 600 · Watercolor · 40 px · 10.3 s

![Brush Artist · Watercolour — blue — own sheet](Brush-Artist-Watercolour-blue-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| s0 | 7 % → 23 % | 28.4 px | 0.25 | 3.20 | 44 |
| s1 | 5 % → 32 % | 9.9 px | 0.38 | 5.84 | 43 |
| s2 | 10 % → 18 % | 43.5 px | 0.19 | 1.75 | 50 |
| s3 | 9 % → 17 % | 26.3 px | 0.28 | 1.85 | 70 |
| s4 | 14 % → 29 % | 37.9 px | 0.36 | 2.11 | 66 |
| s5 | 19 % → 29 % | 38.9 px | 0.37 | 1.51 | 65 |
| s6 | 17 % → 21 % | 47.6 px | 0.27 | 1.22 | 52 |
| s7 | 24 % → 35 % | 31.9 px | 0.37 | 1.44 | 40 |
| s8 | 20 % → 23 % | 77.5 px | 0.27 | 1.18 | 43 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Charcoal — stick — own sheet
own sheet 600 × 600 · Charcoal · 28 px · 1.1 s

![Brush Artist · Charcoal — stick — own sheet](Brush-Artist-Charcoal-stick-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| finger0 | 9 % → 18 % | 15.5 px | 0.83 | 2.01 | 37 |
| tip0 | 8 % → 14 % | 22.1 px | 0.83 | 1.75 | 15 |
| finger1 | 17 % → 29 % | 29.4 px | 0.83 | 1.74 | 27 |
| tip1 | 15 % → 21 % | 39.1 px | 0.83 | 1.42 | 8 |
| finger2 | 17 % → 25 % | 29.5 px | 0.83 | 1.53 | 25 |
| tip2 | 14 % → 20 % | 39.0 px | 0.83 | 1.41 | 8 |
| finger3 | 16 % → 19 % | 29.3 px | 0.83 | 1.16 | 25 |
| tip3 | 15 % → 15 % | 39.0 px | 0.83 | 1.00 | 8 |
| cig0 | 25 % → 35 % | 54.8 px | 0.83 | 1.41 | 9 |
| cig1 | 26 % → 35 % | 58.8 px | 0.83 | 1.32 | 9 |
| cig2 | 28 % → 35 % | 63.2 px | 0.83 | 1.22 | 10 |
| cig3 | 30 % → 34 % | 67.3 px | 0.83 | 1.14 | 9 |
| cig4 | 32 % → 34 % | 71.5 px | 0.83 | 1.06 | 9 |
| cig5 | 34 % → 34 % | 75.3 px | 0.83 | 1.00 | 9 |

Numbers say: wet paint spreads well beyond the stroke.

