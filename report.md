![All brushes](contact.png)

# Brush Lab — 158 brushes · 3 Nov 2026 at 18:47

Every sheet: 1500 × 600, ten strokes in a 5 × 2 grid — 1. light line · 2. heavy line · 3. pressure swell · 4. fast wave · 5. slow wave · 6. spiral · 7. loop · 8. tilted · 9. over the wet one · 10. long, no reload (cell 8 holds «tilted» and «over the wet one» crossed). The CPU reference of Mamay's paint engine; the wet layer settles 20 s at the end.

Columns: **covered** = share of the cell with paint right after the stroke → after settling; **width** = painted area of the stroke ÷ its length (px); **dark** = mean darkness of the painted pixels above the paper's own grain (0 = paper, 1 = black); **spread** = how far wet paint went beyond the stroke (1.0 = stayed); **ms** = the stroke on the CPU; long stroke: paint in each quarter of its length (it should run out: wet → streaks → dry tail).

## Ink Line
Ink · 12 px · 23.1 s

![Ink Line](Ink-Line.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 1 % → 4 % | 4.3 px | 0.55 | 2.44 | 76 |
| heavy line | 5 % → 6 % | 15.7 px | 0.68 | 1.13 | 51 |
| pressure swell | 3 % → 4 % | 11.3 px | 0.64 | 1.40 | 30 |
| fast wave | 10 % → 11 % | 11.2 px | 0.59 | 1.11 | 149 |
| slow wave | 8 % → 10 % | 9.6 px | 0.57 | 1.16 | 128 |
| spiral | 14 % → 15 % | 8.9 px | 0.50 | 1.07 | 192 |
| loop | 8 % → 9 % | 10.6 px | 0.61 | 1.16 | 76 |
| tilted | 5 % → 5 % | 14.4 px | 0.65 | 1.05 | 56 |
| over the wet one | 10 % → 11 % | 12.5 px | 0.65 | 1.15 | 45 |
| long, no reload | 18 % → 17 % | 8.1 px | 0.47 | 0.96 | 274 | quarters: 0.22 → 0.09 → 0.04 → 0.02

Numbers say: light vs heavy: width 4.3 → 15.7 px, dark 0.55 → 0.68; wet paint spreads well beyond the stroke.

## Dense Ink
Ink · 14 px · 23.7 s

![Dense Ink](Dense-Ink.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 5 % → 7 % | 15.2 px | 0.72 | 1.26 | 42 |
| heavy line | 7 % → 7 % | 19.1 px | 0.73 | 1.09 | 73 |
| pressure swell | 5 % → 6 % | 17.9 px | 0.72 | 1.17 | 40 |
| fast wave | 13 % → 13 % | 15.3 px | 0.69 | 1.01 | 165 |
| slow wave | 12 % → 12 % | 13.6 px | 0.67 | 1.04 | 162 |
| spiral | 18 % → 15 % | 12.2 px | 0.65 | 0.80 | 220 |
| loop | 11 % → 12 % | 14.8 px | 0.69 | 1.08 | 110 |
| tilted | 5 % → 6 % | 14.6 px | 0.72 | 1.07 | 63 |
| over the wet one | 12 % → 13 % | 17.7 px | 0.72 | 1.11 | 65 |
| long, no reload | 23 % → 15 % | 10.1 px | 0.64 | 0.66 | 310 | quarters: 0.30 → 0.12 → 0.04 → 0.02

Numbers say: light vs heavy: width 15.2 → 19.1 px, dark 0.72 → 0.73.

## Transparent Wash
Watercolor · 22 px · 24.2 s

![Transparent Wash](Transparent-Wash.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 2 % → 5 % | 6.9 px | 0.27 | 2.25 | 75 |
| heavy line | 7 % → 9 % | 20.4 px | 0.27 | 1.22 | 46 |
| pressure swell | 4 % → 6 % | 15.2 px | 0.28 | 1.54 | 30 |
| fast wave | 14 % → 16 % | 16.1 px | 0.20 | 1.17 | 148 |
| slow wave | 12 % → 15 % | 13.7 px | 0.21 | 1.28 | 175 |
| spiral | 18 % → 22 % | 11.9 px | 0.16 | 1.23 | 169 |
| loop | 11 % → 13 % | 14.5 px | 0.22 | 1.20 | 82 |
| tilted | 8 % → 8 % | 21.1 px | 0.24 | 1.06 | 53 |
| over the wet one | 13 % → 16 % | 16.4 px | 0.24 | 1.18 | 46 |
| long, no reload | 26 % → 32 % | 11.6 px | 0.13 | 1.22 | 257 | quarters: 0.11 → 0.04 → 0.02 → 0.01

Numbers say: light vs heavy: width 6.9 → 20.4 px, dark 0.27 → 0.27; wet paint spreads well beyond the stroke.

## Dry Brush
Gouache · 24 px · 19.7 s

![Dry Brush](Dry-Brush.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 5 % → 0 % | 14.0 px | 0.65 | 0.09 | 112 |
| heavy line | 6 % → 0 % | 18.6 px | 0.65 | 0.02 | 91 |
| pressure swell | 5 % → 0 % | 18.2 px | 0.65 | 0.08 | 44 |
| fast wave | 6 % → 1 % | 7.3 px | 0.65 | 0.08 | 142 |
| slow wave | 7 % → 0 % | 8.1 px | 0.65 | 0.06 | 228 |
| spiral | 7 % → 0 % | 4.6 px | 0.65 | 0.07 | 233 |
| loop | 10 % → 0 % | 12.4 px | 0.65 | 0.04 | 114 |
| tilted | 4 % → 3 % | 10.6 px | 0.65 | 0.88 | 66 |
| over the wet one | 9 % → 1 % | 14.5 px | 0.65 | 0.12 | 52 |
| long, no reload | 6 % → 1 % | 2.9 px | 0.65 | 0.14 | 295 | quarters: 0.12 → 0.00 → 0.00 → 0.00

Numbers say: light vs heavy: width 14.0 → 18.6 px, dark 0.65 → 0.65.

## Wax Crayon
Wax · 8 px · 9.2 s

![Wax Crayon](Wax-Crayon.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 1 % → 1 % | 2.5 px | 0.71 | 1.00 | 58 |
| heavy line | 1 % → 1 % | 3.9 px | 0.69 | 1.00 | 10 |
| pressure swell | 1 % → 1 % | 3.3 px | 0.70 | 1.00 | 7 |
| fast wave | 3 % → 3 % | 3.5 px | 0.69 | 1.00 | 41 |
| slow wave | 3 % → 3 % | 3.4 px | 0.70 | 1.00 | 34 |
| spiral | 5 % → 5 % | 3.3 px | 0.70 | 1.00 | 71 |
| loop | 3 % → 3 % | 3.3 px | 0.70 | 1.00 | 46 |
| tilted | 2 % → 2 % | 5.6 px | 0.68 | 1.00 | 22 |
| over the wet one | 3 % → 3 % | 3.6 px | 0.68 | 1.00 | 12 |
| long, no reload | 7 % → 7 % | 3.3 px | 0.70 | 1.00 | 120 | quarters: 0.06 → 0.06 → 0.06 → 0.06

Numbers say: light vs heavy: width 2.5 → 3.9 px, dark 0.71 → 0.69; the long stroke does not run out of paint.

## Oil Pastel
Wax · 12 px · 9.4 s

![Oil Pastel](Oil-Pastel.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 1 % → 1 % | 4.0 px | 0.68 | 1.00 | 63 |
| heavy line | 2 % → 2 % | 6.5 px | 0.68 | 1.00 | 22 |
| pressure swell | 2 % → 2 % | 5.7 px | 0.69 | 1.00 | 19 |
| fast wave | 5 % → 5 % | 5.7 px | 0.68 | 1.00 | 54 |
| slow wave | 5 % → 5 % | 5.5 px | 0.68 | 1.00 | 53 |
| spiral | 8 % → 8 % | 5.5 px | 0.68 | 1.00 | 98 |
| loop | 4 % → 4 % | 5.6 px | 0.68 | 1.00 | 103 |
| tilted | 2 % → 2 % | 6.8 px | 0.68 | 1.00 | 34 |
| over the wet one | 5 % → 5 % | 5.8 px | 0.68 | 1.00 | 14 |
| long, no reload | 13 % → 13 % | 5.6 px | 0.68 | 1.00 | 179 | quarters: 0.10 → 0.09 → 0.10 → 0.10

Numbers say: light vs heavy: width 4.0 → 6.5 px, dark 0.68 → 0.68; the long stroke does not run out of paint.

## Charcoal
Charcoal · 5 px · 8.9 s

![Charcoal](Charcoal.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 1 % → 1 % | 2.0 px | 0.74 | 1.00 | 25 |
| heavy line | 1 % → 1 % | 3.0 px | 0.74 | 1.00 | 12 |
| pressure swell | 1 % → 1 % | 2.7 px | 0.74 | 1.00 | 11 |
| fast wave | 2 % → 2 % | 2.7 px | 0.73 | 1.00 | 31 |
| slow wave | 2 % → 2 % | 2.6 px | 0.74 | 1.00 | 32 |
| spiral | 4 % → 4 % | 2.5 px | 0.74 | 1.00 | 58 |
| loop | 2 % → 2 % | 2.6 px | 0.74 | 1.00 | 25 |
| tilted | 2 % → 2 % | 4.3 px | 0.72 | 1.00 | 16 |
| over the wet one | 2 % → 2 % | 2.4 px | 0.72 | 1.00 | 13 |
| long, no reload | 6 % → 6 % | 2.7 px | 0.73 | 1.00 | 56 | quarters: 0.05 → 0.05 → 0.05 → 0.05

Numbers say: light vs heavy: width 2.0 → 3.0 px, dark 0.74 → 0.74; the long stroke does not run out of paint.

## Impasto
Heavy acrylic · 22 px · 13.9 s

![Impasto](Impasto.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 8 % → 8 % | 24.1 px | 0.71 | 0.93 | 132 |
| heavy line | 10 % → 9 % | 28.8 px | 0.70 | 0.94 | 90 |
| pressure swell | 7 % → 7 % | 28.1 px | 0.72 | 0.94 | 50 |
| fast wave | 20 % → 13 % | 23.5 px | 0.71 | 0.64 | 140 |
| slow wave | 21 % → 14 % | 24.5 px | 0.71 | 0.66 | 271 |
| spiral | 30 % → 14 % | 20.0 px | 0.71 | 0.46 | 246 |
| loop | 18 % → 14 % | 23.9 px | 0.71 | 0.77 | 137 |
| tilted | 8 % → 8 % | 21.8 px | 0.70 | 1.00 | 72 |
| over the wet one | 17 % → 15 % | 25.4 px | 0.70 | 0.91 | 65 |
| long, no reload | 34 % → 14 % | 15.2 px | 0.71 | 0.41 | 339 | quarters: 0.38 → 0.21 → 0.10 → 0.03

Numbers say: light vs heavy: width 24.1 → 28.8 px, dark 0.71 → 0.70.

## Oil Round
Oil · 18 px · 16.4 s

![Oil Round](Oil-Round.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 2 % → 2 % | 7.2 px | 0.75 | 1.00 | 110 |
| heavy line | 7 % → 7 % | 19.3 px | 0.73 | 1.00 | 68 |
| pressure swell | 4 % → 4 % | 13.7 px | 0.72 | 1.00 | 24 |
| fast wave | 11 % → 11 % | 12.7 px | 0.65 | 1.00 | 132 |
| slow wave | 8 % → 8 % | 9.0 px | 0.57 | 1.00 | 142 |
| spiral | 10 % → 10 % | 6.6 px | 0.50 | 1.00 | 211 |
| loop | 5 % → 5 % | 7.1 px | 0.45 | 1.00 | 99 |
| tilted | 4 % → 4 % | 10.1 px | 0.52 | 1.00 | 55 |
| over the wet one | 6 % → 6 % | 7.4 px | 0.52 | 1.00 | 37 |
| long, no reload | 15 % → 15 % | 6.8 px | 0.42 | 1.00 | 296 | quarters: 0.08 → 0.08 → 0.07 → 0.06

Numbers say: light vs heavy: width 7.2 → 19.3 px, dark 0.75 → 0.73.

## Palette Knife
Oil · 20 px · 15.7 s

![Palette Knife](Palette-Knife.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 8 % → 8 % | 21.9 px | 0.67 | 1.00 | 71 |
| heavy line | 8 % → 8 % | 22.5 px | 0.73 | 1.00 | 18 |
| pressure swell | 6 % → 6 % | 22.4 px | 0.74 | 1.00 | 7 |
| fast wave | 17 % → 17 % | 19.3 px | 0.49 | 1.00 | 22 |
| slow wave | 17 % → 17 % | 19.9 px | 0.43 | 1.00 | 45 |
| spiral | 18 % → 18 % | 11.7 px | 0.45 | 1.00 | 53 |
| loop | 16 % → 16 % | 21.0 px | 0.58 | 1.00 | 24 |
| tilted | 5 % → 5 % | 15.0 px | 0.72 | 1.00 | 6 |
| over the wet one | 13 % → 13 % | 21.0 px | 0.72 | 1.00 | 19 |
| long, no reload | 17 % → 17 % | 7.5 px | 0.47 | 1.00 | 45 | quarters: 0.29 → 0.05 → 0.00 → 0.00

Numbers say: light vs heavy: width 21.9 → 22.5 px, dark 0.67 → 0.73; pressure barely changes the width.

## Water
Watercolor · 20 px · 33.9 s · over bands of wet oil paint and oil pastel in turn (it works on paint already there: look at what it does to the bands; covered counts the bands too)

![Water](Water.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 25 % → 27 % | 73.8 px | 0.80 | 1.06 | 15 |
| heavy line | 24 % → 25 % | 69.8 px | 0.81 | 1.04 | 53 |
| pressure swell | 24 % → 25 % | 89.6 px | 0.81 | 1.03 | 33 |
| fast wave | 24 % → 26 % | 27.7 px | 0.81 | 1.07 | 93 |
| slow wave | 24 % → 25 % | 27.7 px | 0.81 | 1.06 | 133 |
| spiral | 24 % → 26 % | 15.9 px | 0.81 | 1.07 | 154 |
| loop | 24 % → 25 % | 31.1 px | 0.81 | 1.03 | 81 |
| tilted | 24 % → 24 % | 67.0 px | 0.81 | 1.00 | 54 |
| over the wet one | 24 % → 25 % | 0.0 px | 0.81 | 1.06 | 36 |
| long, no reload | 24 % → 26 % | 10.7 px | 0.81 | 1.08 | 233 | quarters: 0.21 → 0.27 → 0.18 → 0.27

Numbers say: light vs heavy: width 73.8 → 69.8 px, dark 0.80 → 0.81; pressure barely changes the width; the long stroke does not run out of paint.

## Blender
Pastel · 16 px · 19.1 s · over bands of wet oil paint and oil pastel in turn (it works on paint already there: look at what it does to the bands; covered counts the bands too)

![Blender](Blender.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 24 % → 24 % | 70.7 px | 0.81 | 1.00 | 15 |
| heavy line | 25 % → 25 % | 72.1 px | 0.80 | 1.00 | 26 |
| pressure swell | 24 % → 24 % | 91.3 px | 0.81 | 1.00 | 31 |
| fast wave | 26 % → 26 % | 30.0 px | 0.79 | 1.00 | 63 |
| slow wave | 26 % → 26 % | 29.9 px | 0.80 | 1.00 | 74 |
| spiral | 28 % → 28 % | 18.7 px | 0.77 | 1.00 | 96 |
| loop | 25 % → 25 % | 32.9 px | 0.80 | 1.00 | 70 |
| tilted | 25 % → 25 % | 70.1 px | 0.79 | 1.00 | 40 |
| over the wet one | 26 % → 26 % | 1.8 px | 0.79 | 1.00 | 32 |
| long, no reload | 30 % → 30 % | 13.7 px | 0.76 | 1.00 | 175 | quarters: 0.20 → 0.28 → 0.23 → 0.30

Numbers say: light vs heavy: width 70.7 → 72.1 px, dark 0.81 → 0.80; pressure barely changes the width; the long stroke does not run out of paint.

## Eraser
Eraser · 16 px · 18.5 s · over bands of wet oil paint and oil pastel in turn (it works on paint already there: look at what it does to the bands; covered counts the bands too)

![Eraser](Eraser.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 24 % → 24 % | 69.5 px | 0.82 | 1.00 | 20 |
| heavy line | 23 % → 23 % | 67.9 px | 0.82 | 1.00 | 34 |
| pressure swell | 23 % → 23 % | 87.3 px | 0.82 | 1.00 | 31 |
| fast wave | 22 % → 22 % | 25.7 px | 0.82 | 1.00 | 62 |
| slow wave | 22 % → 22 % | 25.7 px | 0.82 | 1.00 | 75 |
| spiral | 22 % → 22 % | 14.4 px | 0.82 | 1.00 | 116 |
| loop | 22 % → 22 % | 28.6 px | 0.82 | 1.00 | 72 |
| tilted | 23 % → 23 % | 65.1 px | 0.82 | 1.00 | 38 |
| over the wet one | 23 % → 23 % | 0.0 px | 0.82 | 1.00 | 45 |
| long, no reload | 20 % → 20 % | 8.9 px | 0.82 | 1.00 | 147 | quarters: 0.15 → 0.20 → 0.15 → 0.20

Numbers say: light vs heavy: width 69.5 → 67.9 px, dark 0.82 → 0.82; pressure barely changes the width; the long stroke does not run out of paint.

## Fan
Gouache · 30 px · 27.8 s

![Fan](Fan.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 9 % → 3 % | 25.7 px | 0.63 | 0.37 | 26 |
| heavy line | 11 % → 4 % | 31.0 px | 0.63 | 0.39 | 37 |
| pressure swell | 8 % → 5 % | 31.7 px | 0.63 | 0.55 | 30 |
| fast wave | 18 % → 5 % | 20.3 px | 0.63 | 0.26 | 88 |
| slow wave | 18 % → 5 % | 21.1 px | 0.63 | 0.25 | 153 |
| spiral | 24 % → 5 % | 15.8 px | 0.63 | 0.20 | 158 |
| loop | 17 % → 5 % | 22.7 px | 0.63 | 0.29 | 80 |
| tilted | 5 % → 6 % | 15.1 px | 0.63 | 1.05 | 43 |
| over the wet one | 16 % → 8 % | 29.8 px | 0.63 | 0.50 | 38 |
| long, no reload | 23 % → 5 % | 10.1 px | 0.63 | 0.22 | 212 | quarters: 0.29 → 0.07 → 0.01 → 0.00

Numbers say: light vs heavy: width 25.7 → 31.0 px, dark 0.63 → 0.63.

## Sponge
Gouache · 30 px · 27.6 s

![Sponge](Sponge.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 4 % → 0 % | 11.4 px | 0.62 | 0.12 | 26 |
| heavy line | 12 % → 2 % | 35.4 px | 0.62 | 0.14 | 61 |
| pressure swell | 7 % → 2 % | 27.9 px | 0.62 | 0.27 | 30 |
| fast wave | 20 % → 4 % | 23.2 px | 0.62 | 0.19 | 96 |
| slow wave | 21 % → 4 % | 23.7 px | 0.62 | 0.18 | 200 |
| spiral | 28 % → 4 % | 18.3 px | 0.62 | 0.14 | 169 |
| loop | 18 % → 5 % | 23.0 px | 0.62 | 0.29 | 94 |
| tilted | 7 % → 7 % | 18.2 px | 0.62 | 1.04 | 92 |
| over the wet one | 16 % → 6 % | 27.8 px | 0.62 | 0.37 | 52 |
| long, no reload | 29 % → 5 % | 12.9 px | 0.62 | 0.17 | 269 | quarters: 0.29 → 0.13 → 0.07 → 0.04

Numbers say: light vs heavy: width 11.4 → 35.4 px, dark 0.62 → 0.62.

## Ink — sumi brush
Watercolor · 22 px · 25.5 s

![Ink — sumi brush](Ink-sumi-brush.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 6 % → 6 % | 18.4 px | 0.43 | 0.99 | 53 |
| heavy line | 10 % → 10 % | 30.2 px | 0.37 | 0.99 | 72 |
| pressure swell | 7 % → 7 % | 27.7 px | 0.42 | 0.99 | 43 |
| fast wave | 20 % → 16 % | 23.6 px | 0.31 | 0.79 | 139 |
| slow wave | 19 % → 17 % | 22.4 px | 0.36 | 0.89 | 221 |
| spiral | 29 % → 20 % | 18.9 px | 0.31 | 0.71 | 262 |
| loop | 17 % → 17 % | 22.4 px | 0.35 | 0.97 | 128 |
| tilted | 6 % → 7 % | 16.4 px | 0.39 | 1.16 | 53 |
| over the wet one | 16 % → 15 % | 28.0 px | 0.39 | 0.95 | 53 |
| long, no reload | 34 % → 23 % | 15.1 px | 0.31 | 0.68 | 383 | quarters: 0.22 → 0.10 → 0.06 → 0.04

Numbers say: light vs heavy: width 18.4 → 30.2 px, dark 0.43 → 0.37.

## Ink — wash
Watercolor · 40 px · 28.9 s

![Ink — wash](Ink-wash.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 7 % → 9 % | 20.6 px | 0.05 | 1.21 | 168 |
| heavy line | 10 % → 12 % | 30.2 px | 0.04 | 1.11 | 73 |
| pressure swell | 7 % → 8 % | 25.9 px | 0.05 | 1.20 | 61 |
| fast wave | 21 % → 23 % | 24.7 px | 0.04 | 1.07 | 178 |
| slow wave | 20 % → 23 % | 23.5 px | 0.06 | 1.15 | 303 |
| spiral | 33 % → 35 % | 21.8 px | 0.05 | 1.05 | 285 |
| loop | 19 % → 22 % | 24.0 px | 0.05 | 1.17 | 174 |
| tilted | 7 % → 8 % | 19.6 px | 0.06 | 1.20 | 117 |
| over the wet one | 17 % → 19 % | 28.3 px | 0.06 | 1.11 | 85 |
| long, no reload | 38 % → 40 % | 17.1 px | 0.05 | 1.04 | 466 | quarters: 0.04 → 0.03 → 0.02 → 0.01

Numbers say: light vs heavy: width 20.6 → 30.2 px, dark 0.05 → 0.04.

## Ink — dry brush
Ink · 30 px · 23.9 s

![Ink — dry brush](Ink-dry-brush.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 9 % → 7 % | 25.2 px | 0.81 | 0.79 | 83 |
| heavy line | 10 % → 8 % | 29.6 px | 0.80 | 0.76 | 124 |
| pressure swell | 7 % → 6 % | 27.9 px | 0.81 | 0.85 | 71 |
| fast wave | 21 % → 8 % | 24.2 px | 0.79 | 0.40 | 231 |
| slow wave | 18 % → 7 % | 20.3 px | 0.79 | 0.39 | 366 |
| spiral | 24 % → 8 % | 15.6 px | 0.78 | 0.34 | 358 |
| loop | 19 % → 8 % | 24.3 px | 0.78 | 0.45 | 196 |
| tilted | 8 % → 8 % | 22.2 px | 0.78 | 1.02 | 130 |
| over the wet one | 17 % → 14 % | 25.9 px | 0.78 | 0.81 | 109 |
| long, no reload | 20 % → 8 % | 9.1 px | 0.79 | 0.41 | 576 | quarters: 0.32 → 0.02 → 0.00 → 0.00

Numbers say: light vs heavy: width 25.2 → 29.6 px, dark 0.81 → 0.80.

## Ink — nib
Watercolor · 5 px · 21.2 s

![Ink — nib](Ink-nib.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 1 % → 2 % | 4.3 px | 0.71 | 1.15 | 25 |
| heavy line | 2 % → 2 % | 5.0 px | 0.73 | 1.15 | 16 |
| pressure swell | 1 % → 2 % | 4.8 px | 0.74 | 1.19 | 24 |
| fast wave | 4 % → 3 % | 4.1 px | 0.65 | 0.96 | 59 |
| slow wave | 4 % → 4 % | 4.1 px | 0.65 | 1.06 | 65 |
| spiral | 5 % → 4 % | 3.4 px | 0.60 | 0.84 | 98 |
| loop | 3 % → 3 % | 4.1 px | 0.66 | 1.07 | 57 |
| tilted | 2 % → 2 % | 5.3 px | 0.63 | 1.22 | 26 |
| over the wet one | 4 % → 4 % | 5.8 px | 0.63 | 0.95 | 30 |
| long, no reload | 7 % → 5 % | 3.1 px | 0.60 | 0.70 | 171 | quarters: 0.09 → 0.04 → 0.02 → 0.02

Numbers say: light vs heavy: width 4.3 → 5.0 px, dark 0.71 → 0.73.

## 0.45 · Dry brush
Gouache · 34 px · 24.5 s

![0.45 · Dry brush](0-45-Dry-brush.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 10 % → 3 % | 29.4 px | 0.67 | 0.29 | 111 |
| heavy line | 11 % → 3 % | 31.6 px | 0.67 | 0.30 | 100 |
| pressure swell | 8 % → 3 % | 31.5 px | 0.67 | 0.41 | 87 |
| fast wave | 19 % → 3 % | 22.5 px | 0.67 | 0.18 | 312 |
| slow wave | 20 % → 4 % | 23.2 px | 0.67 | 0.18 | 500 |
| spiral | 21 % → 3 % | 14.1 px | 0.67 | 0.16 | 469 |
| loop | 20 % → 4 % | 26.1 px | 0.67 | 0.20 | 248 |
| tilted | 9 % → 8 % | 24.0 px | 0.67 | 0.98 | 150 |
| over the wet one | 19 % → 6 % | 28.2 px | 0.67 | 0.34 | 114 |
| long, no reload | 20 % → 4 % | 9.1 px | 0.67 | 0.19 | 703 | quarters: 0.36 → 0.10 → 0.00 → 0.00

Numbers say: light vs heavy: width 29.4 → 31.6 px, dark 0.67 → 0.67; pressure barely changes the width.

## Dry pastel
Pastel · 26 px · 10.4 s

![Dry pastel](Dry-pastel.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 3 % → 3 % | 8.3 px | 0.38 | 1.00 | 24 |
| heavy line | 5 % → 5 % | 13.2 px | 0.39 | 1.00 | 43 |
| pressure swell | 3 % → 3 % | 11.7 px | 0.38 | 1.00 | 27 |
| fast wave | 10 % → 10 % | 11.9 px | 0.39 | 1.00 | 95 |
| slow wave | 10 % → 10 % | 11.3 px | 0.39 | 1.00 | 156 |
| spiral | 15 % → 15 % | 9.6 px | 0.39 | 1.00 | 169 |
| loop | 7 % → 7 % | 9.4 px | 0.39 | 1.00 | 87 |
| tilted | 3 % → 3 % | 8.3 px | 0.38 | 1.00 | 44 |
| over the wet one | 7 % → 7 % | 11.1 px | 0.38 | 1.00 | 30 |
| long, no reload | 18 % → 18 % | 8.2 px | 0.39 | 1.00 | 221 | quarters: 0.08 → 0.08 → 0.08 → 0.07

Numbers say: light vs heavy: width 8.3 → 13.2 px, dark 0.38 → 0.39; the long stroke does not run out of paint.

## 0.45 · Charcoal
Charcoal · 18 px · 9.9 s

![0.45 · Charcoal](0-45-Charcoal.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 2 % → 2 % | 6.5 px | 0.80 | 1.00 | 46 |
| heavy line | 3 % → 3 % | 9.2 px | 0.80 | 1.00 | 27 |
| pressure swell | 2 % → 2 % | 8.8 px | 0.80 | 1.00 | 13 |
| fast wave | 7 % → 7 % | 8.5 px | 0.80 | 1.00 | 52 |
| slow wave | 7 % → 7 % | 8.0 px | 0.80 | 1.00 | 53 |
| spiral | 12 % → 12 % | 7.9 px | 0.80 | 1.00 | 74 |
| loop | 6 % → 6 % | 8.1 px | 0.80 | 1.00 | 40 |
| tilted | 3 % → 3 % | 7.5 px | 0.80 | 1.00 | 30 |
| over the wet one | 6 % → 6 % | 7.9 px | 0.80 | 1.00 | 18 |
| long, no reload | 17 % → 17 % | 7.8 px | 0.80 | 1.00 | 77 | quarters: 0.15 → 0.16 → 0.15 → 0.16

Numbers say: light vs heavy: width 6.5 → 9.2 px, dark 0.80 → 0.80; the long stroke does not run out of paint.

## Watercolour — wash
Watercolor · 50 px · 30.5 s

![Watercolour — wash](Watercolour-wash.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 8 % → 9 % | 23.5 px | 0.01 | 1.13 | 85 |
| heavy line | 13 % → 14 % | 37.2 px | 0.01 | 1.07 | 111 |
| pressure swell | 8 % → 9 % | 28.6 px | 0.01 | 1.12 | 81 |
| fast wave | 25 % → 27 % | 28.9 px | 0.01 | 1.10 | 269 |
| slow wave | 25 % → 28 % | 28.5 px | 0.01 | 1.13 | 407 |
| spiral | 38 % → 43 % | 25.1 px | 0.01 | 1.12 | 416 |
| loop | 22 % → 25 % | 28.3 px | 0.01 | 1.14 | 223 |
| tilted | 10 % → 11 % | 26.7 px | 0.01 | 1.13 | 167 |
| over the wet one | 20 % → 22 % | 29.3 px | 0.01 | 1.09 | 105 |
| long, no reload | 44 % → 49 % | 19.7 px | 0.01 | 1.12 | 683 | quarters: 0.01 → 0.01 → 0.00 → 0.00

Numbers say: light vs heavy: width 23.5 → 37.2 px, dark 0.01 → 0.01.

## Watercolour — wet-in-wet
Watercolor · 44 px · 29.1 s

![Watercolour — wet-in-wet](Watercolour-wet-in-wet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 7 % → 8 % | 19.2 px | 0.01 | 1.23 | 65 |
| heavy line | 11 % → 12 % | 30.8 px | 0.01 | 1.16 | 95 |
| pressure swell | 7 % → 8 % | 24.7 px | 0.01 | 1.19 | 64 |
| fast wave | 22 % → 26 % | 25.8 px | 0.01 | 1.15 | 204 |
| slow wave | 22 % → 25 % | 25.1 px | 0.01 | 1.17 | 347 |
| spiral | 35 % → 41 % | 23.1 px | 0.01 | 1.17 | 360 |
| loop | 19 % → 23 % | 25.2 px | 0.01 | 1.17 | 181 |
| tilted | 8 % → 9 % | 21.2 px | 0.01 | 1.15 | 123 |
| over the wet one | 16 % → 18 % | 24.7 px | 0.01 | 1.12 | 91 |
| long, no reload | 41 % → 48 % | 18.3 px | 0.01 | 1.18 | 522 | quarters: 0.01 → 0.00 → 0.00 → 0.00

Numbers say: light vs heavy: width 19.2 → 30.8 px, dark 0.01 → 0.01.

## Watercolour — glaze
Watercolor · 38 px · 27.3 s

![Watercolour — glaze](Watercolour-glaze.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 7 % → 8 % | 19.2 px | 0.01 | 1.17 | 78 |
| heavy line | 11 % → 13 % | 32.3 px | 0.01 | 1.15 | 75 |
| pressure swell | 6 % → 8 % | 23.9 px | 0.01 | 1.21 | 58 |
| fast wave | 19 % → 22 % | 22.3 px | 0.01 | 1.14 | 184 |
| slow wave | 19 % → 22 % | 21.9 px | 0.01 | 1.16 | 309 |
| spiral | 30 % → 32 % | 19.9 px | 0.01 | 1.06 | 326 |
| loop | 18 % → 22 % | 23.8 px | 0.01 | 1.20 | 204 |
| tilted | 7 % → 8 % | 19.2 px | 0.01 | 1.18 | 103 |
| over the wet one | 16 % → 18 % | 25.9 px | 0.01 | 1.14 | 75 |
| long, no reload | 34 % → 36 % | 15.4 px | 0.01 | 1.04 | 458 | quarters: 0.01 → 0.00 → 0.00 → 0.00

Numbers say: light vs heavy: width 19.2 → 32.3 px, dark 0.01 → 0.01.

## Watercolour — granulating
Watercolor · 44 px · 27.4 s

![Watercolour — granulating](Watercolour-granulating.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 7 % → 7 % | 19.3 px | 0.01 | 1.05 | 80 |
| heavy line | 11 % → 11 % | 31.0 px | 0.01 | 1.02 | 88 |
| pressure swell | 7 % → 7 % | 25.9 px | 0.01 | 1.05 | 69 |
| fast wave | 21 % → 20 % | 24.0 px | 0.01 | 0.99 | 214 |
| slow wave | 21 % → 21 % | 24.3 px | 0.02 | 1.02 | 362 |
| spiral | 34 % → 35 % | 22.5 px | 0.01 | 1.03 | 324 |
| loop | 17 % → 18 % | 22.5 px | 0.02 | 1.04 | 173 |
| tilted | 8 % → 8 % | 22.0 px | 0.02 | 1.08 | 107 |
| over the wet one | 17 % → 18 % | 26.4 px | 0.02 | 1.04 | 78 |
| long, no reload | 39 % → 39 % | 17.4 px | 0.02 | 1.01 | 540 | quarters: 0.01 → 0.01 → 0.01 → 0.00

Numbers say: light vs heavy: width 19.3 → 31.0 px, dark 0.01 → 0.01.

## Watercolour — dry brush
Watercolor · 36 px · 24.2 s

![Watercolour — dry brush](Watercolour-dry-brush.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 5 % → 5 % | 15.5 px | 0.06 | 0.88 | 87 |
| heavy line | 9 % → 7 % | 24.9 px | 0.05 | 0.80 | 101 |
| pressure swell | 6 % → 5 % | 22.3 px | 0.06 | 0.89 | 58 |
| fast wave | 19 % → 11 % | 21.9 px | 0.04 | 0.58 | 246 |
| slow wave | 18 % → 10 % | 20.6 px | 0.05 | 0.55 | 400 |
| spiral | 23 % → 11 % | 15.2 px | 0.04 | 0.46 | 428 |
| loop | 15 % → 11 % | 19.5 px | 0.05 | 0.73 | 233 |
| tilted | 7 % → 7 % | 18.2 px | 0.05 | 1.08 | 105 |
| over the wet one | 14 % → 13 % | 21.8 px | 0.05 | 0.88 | 96 |
| long, no reload | 21 % → 12 % | 9.6 px | 0.05 | 0.57 | 706 | quarters: 0.02 → 0.01 → 0.00 → 0.00

Numbers say: light vs heavy: width 15.5 → 24.9 px, dark 0.06 → 0.05.

## Gouache
Gouache · 30 px · 24.9 s

![Gouache](Gouache.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 8 % → 5 % | 24.4 px | 0.14 | 0.64 | 77 |
| heavy line | 14 % → 6 % | 39.7 px | 0.14 | 0.47 | 82 |
| pressure swell | 10 % → 6 % | 38.6 px | 0.14 | 0.60 | 68 |
| fast wave | 28 % → 7 % | 32.2 px | 0.14 | 0.25 | 223 |
| slow wave | 27 % → 8 % | 31.4 px | 0.14 | 0.29 | 333 |
| spiral | 38 % → 8 % | 24.8 px | 0.14 | 0.22 | 325 |
| loop | 22 % → 8 % | 28.6 px | 0.14 | 0.35 | 183 |
| tilted | 9 % → 9 % | 23.8 px | 0.14 | 1.01 | 90 |
| over the wet one | 20 % → 13 % | 31.1 px | 0.14 | 0.66 | 73 |
| long, no reload | 40 % → 9 % | 17.9 px | 0.14 | 0.24 | 443 | quarters: 0.07 → 0.04 → 0.01 → 0.01

Numbers say: light vs heavy: width 24.4 → 39.7 px, dark 0.14 → 0.14.

## Oil — alla prima
Oil · 30 px · 17.9 s

![Oil — alla prima](Oil-alla-prima.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 9 % → 9 % | 27.6 px | 0.51 | 1.00 | 91 |
| heavy line | 10 % → 10 % | 30.3 px | 0.51 | 1.00 | 85 |
| pressure swell | 8 % → 8 % | 29.8 px | 0.53 | 1.00 | 68 |
| fast wave | 24 % → 24 % | 28.1 px | 0.51 | 1.00 | 205 |
| slow wave | 26 % → 26 % | 29.5 px | 0.51 | 1.00 | 384 |
| spiral | 40 % → 40 % | 26.4 px | 0.50 | 1.00 | 383 |
| loop | 21 % → 21 % | 27.6 px | 0.52 | 1.00 | 199 |
| tilted | 11 % → 11 % | 30.4 px | 0.51 | 1.00 | 96 |
| over the wet one | 20 % → 20 % | 26.5 px | 0.51 | 1.00 | 72 |
| long, no reload | 49 % → 49 % | 22.0 px | 0.50 | 1.00 | 556 | quarters: 0.32 → 0.28 → 0.25 → 0.22

Numbers say: light vs heavy: width 27.6 → 30.3 px, dark 0.51 → 0.51; pressure barely changes the width.

## Oil — impasto
Oil · 34 px · 18.7 s

![Oil — impasto](Oil-impasto.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 12 % → 12 % | 33.4 px | 0.25 | 1.00 | 114 |
| heavy line | 12 % → 12 % | 36.3 px | 0.25 | 1.00 | 106 |
| pressure swell | 10 % → 10 % | 35.9 px | 0.26 | 1.00 | 70 |
| fast wave | 30 % → 30 % | 35.1 px | 0.25 | 1.00 | 247 |
| slow wave | 31 % → 31 % | 35.7 px | 0.25 | 1.00 | 432 |
| spiral | 52 % → 52 % | 34.0 px | 0.23 | 1.00 | 493 |
| loop | 26 % → 26 % | 33.7 px | 0.24 | 1.00 | 360 |
| tilted | 12 % → 12 % | 32.8 px | 0.26 | 1.00 | 130 |
| over the wet one | 23 % → 23 % | 31.9 px | 0.26 | 1.00 | 107 |
| long, no reload | 60 % → 60 % | 26.9 px | 0.22 | 1.00 | 682 | quarters: 0.18 → 0.16 → 0.13 → 0.10

Numbers say: light vs heavy: width 33.4 → 36.3 px, dark 0.25 → 0.25; pressure barely changes the width.

## Oil — glaze
Oil · 40 px · 14.7 s

![Oil — glaze](Oil-glaze.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 9 % → 9 % | 25.4 px | 0.50 | 1.00 | 84 |
| heavy line | 13 % → 13 % | 36.3 px | 0.49 | 1.00 | 106 |
| pressure swell | 9 % → 9 % | 35.3 px | 0.50 | 1.00 | 97 |
| fast wave | 26 % → 26 % | 30.1 px | 0.48 | 1.00 | 283 |
| slow wave | 29 % → 29 % | 33.7 px | 0.49 | 1.00 | 578 |
| spiral | 44 % → 44 % | 29.0 px | 0.49 | 1.00 | 432 |
| loop | 23 % → 23 % | 30.2 px | 0.50 | 1.00 | 218 |
| tilted | 10 % → 10 % | 28.9 px | 0.50 | 1.00 | 123 |
| over the wet one | 22 % → 22 % | 31.6 px | 0.50 | 1.00 | 105 |
| long, no reload | 51 % → 51 % | 22.7 px | 0.49 | 1.00 | 629 | quarters: 0.33 → 0.29 → 0.26 → 0.22

Numbers say: light vs heavy: width 25.4 → 36.3 px, dark 0.50 → 0.49.

## Oil — scumble
Oil · 36 px · 19.7 s

![Oil — scumble](Oil-scumble.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 11 % → 11 % | 33.1 px | 0.08 | 1.00 | 112 |
| heavy line | 12 % → 12 % | 36.1 px | 0.07 | 1.00 | 125 |
| pressure swell | 9 % → 9 % | 35.5 px | 0.07 | 1.00 | 83 |
| fast wave | 26 % → 26 % | 29.6 px | 0.06 | 1.00 | 324 |
| slow wave | 27 % → 27 % | 30.9 px | 0.05 | 1.00 | 661 |
| spiral | 41 % → 41 % | 27.1 px | 0.04 | 1.00 | 659 |
| loop | 24 % → 24 % | 30.6 px | 0.06 | 1.00 | 254 |
| tilted | 11 % → 11 % | 30.4 px | 0.07 | 1.00 | 150 |
| over the wet one | 22 % → 22 % | 31.4 px | 0.07 | 1.00 | 149 |
| long, no reload | 45 % → 45 % | 20.3 px | 0.04 | 1.00 | 776 | quarters: 0.04 → 0.02 → 0.01 → 0.00

Numbers say: light vs heavy: width 33.1 → 36.1 px, dark 0.08 → 0.07; pressure barely changes the width.

## Acrylic — heavy body
Heavy acrylic · 30 px · 14.0 s

![Acrylic — heavy body](Acrylic-heavy-body.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 10 % → 9 % | 28.9 px | 0.51 | 0.91 | 95 |
| heavy line | 11 % → 10 % | 31.1 px | 0.51 | 0.93 | 89 |
| pressure swell | 8 % → 8 % | 30.7 px | 0.53 | 0.94 | 65 |
| fast wave | 23 % → 15 % | 26.5 px | 0.52 | 0.64 | 201 |
| slow wave | 24 % → 16 % | 27.7 px | 0.51 | 0.65 | 387 |
| spiral | 35 % → 15 % | 23.3 px | 0.51 | 0.43 | 350 |
| loop | 21 % → 16 % | 26.9 px | 0.51 | 0.76 | 187 |
| tilted | 9 % → 9 % | 24.9 px | 0.52 | 0.99 | 105 |
| over the wet one | 19 % → 17 % | 27.7 px | 0.52 | 0.89 | 106 |
| long, no reload | 39 % → 16 % | 17.3 px | 0.51 | 0.41 | 573 | quarters: 0.29 → 0.20 → 0.12 → 0.04

Numbers say: light vs heavy: width 28.9 → 31.1 px, dark 0.51 → 0.51; pressure barely changes the width.

## Acrylic — fluid
Watercolor · 36 px · 27.2 s

![Acrylic — fluid](Acrylic-fluid.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 8 % → 8 % | 22.6 px | 0.06 | 1.03 | 61 |
| heavy line | 12 % → 12 % | 35.0 px | 0.05 | 0.99 | 76 |
| pressure swell | 7 % → 7 % | 27.4 px | 0.06 | 0.99 | 56 |
| fast wave | 25 % → 24 % | 28.7 px | 0.05 | 0.95 | 184 |
| slow wave | 23 % → 23 % | 26.9 px | 0.06 | 1.01 | 309 |
| spiral | 36 % → 35 % | 23.6 px | 0.05 | 0.97 | 344 |
| loop | 21 % → 22 % | 27.2 px | 0.06 | 1.03 | 179 |
| tilted | 8 % → 9 % | 22.5 px | 0.06 | 1.12 | 103 |
| over the wet one | 19 % → 19 % | 30.7 px | 0.06 | 1.01 | 77 |
| long, no reload | 41 % → 40 % | 18.3 px | 0.05 | 0.98 | 443 | quarters: 0.04 → 0.03 → 0.02 → 0.01

Numbers say: light vs heavy: width 22.6 → 35.0 px, dark 0.06 → 0.05.

## Acrylic — palette knife
Heavy acrylic · 42 px · 19.1 s

![Acrylic — palette knife](Acrylic-palette-knife.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 15 % → 15 % | 44.0 px | 0.06 | 0.98 | 23 |
| heavy line | 15 % → 15 % | 44.2 px | 0.05 | 0.97 | 23 |
| pressure swell | 12 % → 12 % | 43.5 px | 0.07 | 0.99 | 6 |
| fast wave | 36 % → 20 % | 41.9 px | 0.06 | 0.56 | 56 |
| slow wave | 37 % → 21 % | 42.6 px | 0.06 | 0.57 | 91 |
| spiral | 50 % → 18 % | 32.8 px | 0.07 | 0.37 | 116 |
| loop | 32 % → 24 % | 41.2 px | 0.06 | 0.75 | 62 |
| tilted | 12 % → 12 % | 33.6 px | 0.06 | 1.00 | 26 |
| over the wet one | 26 % → 25 % | 39.7 px | 0.06 | 0.97 | 21 |
| long, no reload | 57 % → 21 % | 25.7 px | 0.06 | 0.36 | 156 | quarters: 0.04 → 0.02 → 0.00 → 0.00

Numbers say: light vs heavy: width 44.0 → 44.2 px, dark 0.06 → 0.05; pressure barely changes the width.

## Finger on oil
Oil · 30 px · 13.5 s

![Finger on oil](Finger-on-oil.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 8 % → 8 % | 23.7 px | 0.40 | 1.00 | 50 |
| heavy line | 13 % → 13 % | 36.5 px | 0.38 | 1.00 | 57 |
| pressure swell | 9 % → 9 % | 33.3 px | 0.41 | 1.00 | 36 |
| fast wave | 22 % → 22 % | 26.0 px | 0.35 | 1.00 | 141 |
| slow wave | 24 % → 24 % | 27.8 px | 0.35 | 1.00 | 243 |
| spiral | 36 % → 36 % | 23.5 px | 0.27 | 1.00 | 226 |
| loop | 21 % → 21 % | 27.3 px | 0.36 | 1.00 | 138 |
| tilted | 9 % → 9 % | 26.4 px | 0.39 | 1.00 | 81 |
| over the wet one | 20 % → 20 % | 29.3 px | 0.39 | 1.00 | 56 |
| long, no reload | 36 % → 36 % | 16.3 px | 0.26 | 1.00 | 349 | quarters: 0.23 → 0.11 → 0.05 → 0.02

Numbers say: light vs heavy: width 23.7 → 36.5 px, dark 0.40 → 0.38.

## Palette knife — oil
Oil · 44 px · 18.7 s

![Palette knife — oil](Palette-knife-oil.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 16 % → 16 % | 45.6 px | 0.12 | 1.00 | 33 |
| heavy line | 16 % → 16 % | 46.3 px | 0.11 | 1.00 | 31 |
| pressure swell | 12 % → 12 % | 45.2 px | 0.12 | 1.00 | 11 |
| fast wave | 39 % → 39 % | 44.9 px | 0.11 | 1.00 | 56 |
| slow wave | 39 % → 39 % | 45.4 px | 0.11 | 1.00 | 133 |
| spiral | 62 % → 62 % | 40.9 px | 0.08 | 1.00 | 109 |
| loop | 34 % → 34 % | 43.8 px | 0.11 | 1.00 | 62 |
| tilted | 13 % → 13 % | 36.6 px | 0.11 | 1.00 | 23 |
| over the wet one | 28 % → 28 % | 40.8 px | 0.11 | 1.00 | 26 |
| long, no reload | 74 % → 74 % | 33.1 px | 0.08 | 1.00 | 131 | quarters: 0.10 → 0.07 → 0.05 → 0.04

Numbers say: light vs heavy: width 45.6 → 46.3 px, dark 0.12 → 0.11; pressure barely changes the width.

## 0.45 · Sponge
Watercolor · 46 px · 21.5 s

![0.45 · Sponge](0-45-Sponge.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 9 % → 0 % | 26.5 px | 0.00 | 0.00 | 41 |
| heavy line | 12 % → 0 % | 35.5 px | 0.00 | 0.00 | 77 |
| pressure swell | 8 % → 0 % | 30.7 px | 0.01 | 0.05 | 50 |
| fast wave | 18 % → 0 % | 20.4 px | 0.01 | 0.02 | 164 |
| slow wave | 25 % → 3 % | 29.0 px | 0.02 | 0.14 | 296 |
| spiral | 31 % → 5 % | 20.2 px | 0.02 | 0.17 | 276 |
| loop | 21 % → 2 % | 27.1 px | 0.02 | 0.12 | 145 |
| tilted | 8 % → 10 % | 23.1 px | 0.05 | 1.17 | 99 |
| over the wet one | 19 % → 6 % | 29.5 px | 0.05 | 0.31 | 88 |
| long, no reload | 36 % → 8 % | 16.1 px | 0.02 | 0.22 | 407 | quarters: 0.01 → 0.01 → 0.01 → 0.01

Numbers say: light vs heavy: width 26.5 → 35.5 px, dark 0.00 → 0.00.

## 0.45 · Eraser
Eraser · 30 px · 19.7 s · over bands of wet oil paint and oil pastel in turn (it works on paint already there: look at what it does to the bands; covered counts the bands too)

![0.45 · Eraser](0-45-Eraser.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 24 % → 24 % | 69.2 px | 0.82 | 1.00 | 50 |
| heavy line | 23 % → 23 % | 67.4 px | 0.81 | 1.00 | 49 |
| pressure swell | 23 % → 23 % | 86.7 px | 0.82 | 1.00 | 32 |
| fast wave | 21 % → 21 % | 24.7 px | 0.81 | 1.00 | 108 |
| slow wave | 20 % → 20 % | 23.5 px | 0.82 | 1.00 | 208 |
| spiral | 20 % → 20 % | 13.5 px | 0.79 | 1.00 | 207 |
| loop | 21 % → 21 % | 27.8 px | 0.80 | 1.00 | 111 |
| tilted | 23 % → 23 % | 64.8 px | 0.81 | 1.00 | 39 |
| over the wet one | 22 % → 22 % | 0.0 px | 0.81 | 1.00 | 46 |
| long, no reload | 17 % → 17 % | 7.5 px | 0.79 | 1.00 | 323 | quarters: 0.13 → 0.16 → 0.13 → 0.17

Numbers say: light vs heavy: width 69.2 → 67.4 px, dark 0.82 → 0.81; pressure barely changes the width; the long stroke does not run out of paint.

## Lift wet paint
Eraser · 30 px · 19.7 s · over bands of wet oil paint and oil pastel in turn (it works on paint already there: look at what it does to the bands; covered counts the bands too)

![Lift wet paint](Lift-wet-paint.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 24 % → 24 % | 70.1 px | 0.82 | 1.00 | 34 |
| heavy line | 24 % → 24 % | 69.8 px | 0.82 | 1.00 | 40 |
| pressure swell | 24 % → 24 % | 89.5 px | 0.82 | 1.00 | 28 |
| fast wave | 24 % → 24 % | 27.7 px | 0.82 | 1.00 | 103 |
| slow wave | 24 % → 24 % | 27.7 px | 0.82 | 1.00 | 167 |
| spiral | 24 % → 24 % | 15.9 px | 0.82 | 1.00 | 153 |
| loop | 24 % → 24 % | 31.1 px | 0.82 | 1.00 | 89 |
| tilted | 24 % → 24 % | 66.8 px | 0.82 | 1.00 | 56 |
| over the wet one | 24 % → 24 % | 0.0 px | 0.82 | 1.00 | 32 |
| long, no reload | 24 % → 24 % | 10.7 px | 0.82 | 1.00 | 230 | quarters: 0.18 → 0.24 → 0.17 → 0.24

Numbers say: light vs heavy: width 70.1 → 69.8 px, dark 0.82 → 0.82; pressure barely changes the width; the long stroke does not run out of paint.

## Sgraffito
Eraser · 10 px · 19.1 s · over bands of wet oil paint and oil pastel in turn (it works on paint already there: look at what it does to the bands; covered counts the bands too)

![Sgraffito](Sgraffito.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 24 % → 24 % | 69.5 px | 0.81 | 1.00 | 8 |
| heavy line | 24 % → 24 % | 69.5 px | 0.82 | 1.00 | 10 |
| pressure swell | 24 % → 24 % | 89.5 px | 0.82 | 1.00 | 3 |
| fast wave | 24 % → 24 % | 27.4 px | 0.82 | 1.00 | 29 |
| slow wave | 24 % → 24 % | 27.4 px | 0.81 | 1.00 | 27 |
| spiral | 24 % → 24 % | 15.7 px | 0.81 | 1.00 | 39 |
| loop | 24 % → 24 % | 30.9 px | 0.82 | 1.00 | 23 |
| tilted | 24 % → 24 % | 66.6 px | 0.82 | 1.00 | 5 |
| over the wet one | 24 % → 24 % | 0.0 px | 0.82 | 1.00 | 12 |
| long, no reload | 24 % → 24 % | 10.6 px | 0.82 | 1.00 | 61 | quarters: 0.17 → 0.24 → 0.17 → 0.24

Numbers say: light vs heavy: width 69.5 → 69.5 px, dark 0.81 → 0.82; pressure barely changes the width; the long stroke does not run out of paint.

## Brush Artist · Refs · #01 Henry Ward peach cloud
Gouache · 44 px · 35.2 s

![Brush Artist · Refs · #01 Henry Ward peach cloud](Brush-Artist-Refs-01-Henry-Ward-peach-cloud.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 15 % → 13 % | 42.3 px | 0.10 | 0.87 | 130 |
| heavy line | 16 % → 14 % | 45.7 px | 0.10 | 0.91 | 138 |
| pressure swell | 12 % → 11 % | 44.3 px | 0.10 | 0.92 | 91 |
| fast wave | 38 % → 25 % | 43.9 px | 0.10 | 0.65 | 349 |
| slow wave | 38 % → 26 % | 43.6 px | 0.10 | 0.68 | 633 |
| spiral | 61 % → 28 % | 40.2 px | 0.10 | 0.46 | 649 |
| loop | 32 % → 26 % | 41.6 px | 0.10 | 0.81 | 327 |
| tilted | 13 % → 13 % | 36.8 px | 0.10 | 1.00 | 167 |
| over the wet one | 27 % → 26 % | 39.2 px | 0.10 | 0.95 | 150 |
| long, no reload | 72 % → 28 % | 32.2 px | 0.10 | 0.40 | 930 | quarters: 0.08 → 0.07 → 0.06 → 0.03

Numbers say: light vs heavy: width 42.3 → 45.7 px, dark 0.10 → 0.10; pressure barely changes the width.

## Brush Artist · Refs · #02 Henry Ward cream strokes
Gouache · 46 px · 38.2 s

![Brush Artist · Refs · #02 Henry Ward cream strokes](Brush-Artist-Refs-02-Henry-Ward-cream-strokes.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 14 % → 13 % | 41.4 px | 0.02 | 0.94 | 145 |
| heavy line | 15 % → 15 % | 44.5 px | 0.02 | 0.96 | 133 |
| pressure swell | 12 % → 11 % | 43.9 px | 0.01 | 0.95 | 101 |
| fast wave | 36 % → 25 % | 41.9 px | 0.02 | 0.69 | 360 |
| slow wave | 36 % → 25 % | 41.8 px | 0.02 | 0.70 | 660 |
| spiral | 59 % → 28 % | 39.2 px | 0.02 | 0.46 | 648 |
| loop | 31 % → 27 % | 40.3 px | 0.02 | 0.86 | 286 |
| tilted | 13 % → 13 % | 37.3 px | 0.02 | 1.00 | 195 |
| over the wet one | 27 % → 26 % | 38.4 px | 0.02 | 0.96 | 154 |
| long, no reload | 70 % → 29 % | 31.3 px | 0.02 | 0.41 | 854 | quarters: 0.01 → 0.02 → 0.02 → 0.01

Numbers say: light vs heavy: width 41.4 → 44.5 px, dark 0.02 → 0.02; pressure barely changes the width; the long stroke does not run out of paint.

## Brush Artist · Refs · #03 Henry Ward navy contours
Heavy acrylic · 22 px · 13.8 s

![Brush Artist · Refs · #03 Henry Ward navy contours](Brush-Artist-Refs-03-Henry-Ward-navy-contours.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 7 % → 7 % | 21.5 px | 0.70 | 0.94 | 67 |
| heavy line | 8 % → 8 % | 23.4 px | 0.70 | 0.95 | 70 |
| pressure swell | 6 % → 6 % | 23.2 px | 0.73 | 0.94 | 48 |
| fast wave | 19 % → 12 % | 21.8 px | 0.72 | 0.66 | 191 |
| slow wave | 19 % → 13 % | 22.4 px | 0.72 | 0.69 | 300 |
| spiral | 30 % → 13 % | 19.5 px | 0.72 | 0.45 | 327 |
| loop | 17 % → 13 % | 21.4 px | 0.72 | 0.81 | 155 |
| tilted | 8 % → 8 % | 22.6 px | 0.71 | 1.00 | 112 |
| over the wet one | 16 % → 14 % | 21.2 px | 0.71 | 0.89 | 63 |
| long, no reload | 34 % → 14 % | 15.1 px | 0.72 | 0.40 | 450 | quarters: 0.35 → 0.29 → 0.20 → 0.08

Numbers say: light vs heavy: width 21.5 → 23.4 px, dark 0.70 → 0.70; pressure barely changes the width.

## Brush Artist · Refs · #04 Henry Ward grey cloud
Gouache · 50 px · 40.5 s

![Brush Artist · Refs · #04 Henry Ward grey cloud](Brush-Artist-Refs-04-Henry-Ward-grey-cloud.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 16 % → 15 % | 47.1 px | 0.11 | 0.90 | 125 |
| heavy line | 17 % → 16 % | 50.6 px | 0.11 | 0.94 | 179 |
| pressure swell | 13 % → 12 % | 49.2 px | 0.11 | 0.94 | 123 |
| fast wave | 41 % → 28 % | 47.4 px | 0.11 | 0.67 | 419 |
| slow wave | 41 % → 28 % | 47.2 px | 0.11 | 0.69 | 667 |
| spiral | 63 % → 30 % | 41.3 px | 0.11 | 0.48 | 708 |
| loop | 35 % → 29 % | 45.6 px | 0.11 | 0.84 | 354 |
| tilted | 14 % → 14 % | 40.3 px | 0.11 | 1.00 | 202 |
| over the wet one | 30 % → 29 % | 43.2 px | 0.11 | 0.96 | 172 |
| long, no reload | 76 % → 32 % | 33.9 px | 0.11 | 0.43 | 1046 | quarters: 0.09 → 0.08 → 0.06 → 0.03

Numbers say: light vs heavy: width 47.1 → 50.6 px, dark 0.11 → 0.11; pressure barely changes the width.

## Brush Artist · Refs · #05 Henry Ward green in rust loops
Heavy acrylic · 20 px · 13.0 s

![Brush Artist · Refs · #05 Henry Ward green in rust loops](Brush-Artist-Refs-05-Henry-Ward-green-in-rust-loops.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 7 % → 6 % | 19.5 px | 0.55 | 0.94 | 77 |
| heavy line | 7 % → 7 % | 21.2 px | 0.55 | 0.94 | 73 |
| pressure swell | 6 % → 5 % | 21.5 px | 0.57 | 0.92 | 68 |
| fast wave | 17 % → 11 % | 19.7 px | 0.56 | 0.64 | 163 |
| slow wave | 18 % → 12 % | 20.3 px | 0.56 | 0.66 | 285 |
| spiral | 27 % → 12 % | 17.9 px | 0.55 | 0.42 | 328 |
| loop | 15 % → 12 % | 19.5 px | 0.55 | 0.80 | 142 |
| tilted | 8 % → 8 % | 21.7 px | 0.56 | 1.00 | 85 |
| over the wet one | 15 % → 13 % | 19.1 px | 0.56 | 0.87 | 72 |
| long, no reload | 30 % → 12 % | 13.4 px | 0.56 | 0.39 | 380 | quarters: 0.25 → 0.18 → 0.10 → 0.02

Numbers say: light vs heavy: width 19.5 → 21.2 px, dark 0.55 → 0.55; pressure barely changes the width.

## Brush Artist · Refs · #06 Henry Ward scrubbed grey
Gouache · 50 px · 40.2 s

![Brush Artist · Refs · #06 Henry Ward scrubbed grey](Brush-Artist-Refs-06-Henry-Ward-scrubbed-grey.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 16 % → 15 % | 47.1 px | 0.09 | 0.90 | 153 |
| heavy line | 17 % → 16 % | 50.6 px | 0.09 | 0.94 | 163 |
| pressure swell | 13 % → 12 % | 49.2 px | 0.09 | 0.94 | 104 |
| fast wave | 41 % → 28 % | 47.4 px | 0.09 | 0.67 | 522 |
| slow wave | 41 % → 28 % | 47.2 px | 0.09 | 0.69 | 680 |
| spiral | 63 % → 30 % | 41.3 px | 0.09 | 0.48 | 749 |
| loop | 35 % → 29 % | 45.6 px | 0.09 | 0.84 | 350 |
| tilted | 14 % → 14 % | 40.3 px | 0.09 | 1.00 | 187 |
| over the wet one | 30 % → 29 % | 43.2 px | 0.09 | 0.96 | 166 |
| long, no reload | 76 % → 32 % | 33.9 px | 0.09 | 0.43 | 997 | quarters: 0.08 → 0.07 → 0.05 → 0.03

Numbers say: light vs heavy: width 47.1 → 50.6 px, dark 0.09 → 0.09; pressure barely changes the width.

## Brush Artist · Refs · #07 Henry Ward blue L + black zigzag
Heavy acrylic · 34 px · 15.0 s

![Brush Artist · Refs · #07 Henry Ward blue L + black zigzag](Brush-Artist-Refs-07-Henry-Ward-blue-L-black-zigzag.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 11 % → 11 % | 33.1 px | 0.57 | 0.93 | 105 |
| heavy line | 12 % → 11 % | 35.7 px | 0.57 | 0.93 | 104 |
| pressure swell | 9 % → 9 % | 35.2 px | 0.59 | 0.94 | 78 |
| fast wave | 29 % → 20 % | 33.6 px | 0.59 | 0.69 | 252 |
| slow wave | 30 % → 21 % | 34.1 px | 0.58 | 0.73 | 410 |
| spiral | 47 % → 22 % | 31.3 px | 0.58 | 0.46 | 404 |
| loop | 25 % → 21 % | 32.7 px | 0.58 | 0.82 | 224 |
| tilted | 11 % → 11 % | 29.8 px | 0.58 | 1.00 | 136 |
| over the wet one | 22 % → 20 % | 31.7 px | 0.58 | 0.91 | 100 |
| long, no reload | 53 % → 22 % | 23.8 px | 0.59 | 0.42 | 595 | quarters: 0.40 → 0.32 → 0.21 → 0.10

Numbers say: light vs heavy: width 33.1 → 35.7 px, dark 0.57 → 0.57; pressure barely changes the width.

## Brush Artist · Refs · #08 Henry Ward olive bands
Gouache · 34 px · 24.0 s

![Brush Artist · Refs · #08 Henry Ward olive bands](Brush-Artist-Refs-08-Henry-Ward-olive-bands.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 8 % → 2 % | 24.7 px | 0.57 | 0.27 | 58 |
| heavy line | 12 % → 3 % | 33.9 px | 0.57 | 0.22 | 127 |
| pressure swell | 8 % → 3 % | 30.8 px | 0.57 | 0.38 | 77 |
| fast wave | 25 % → 4 % | 29.2 px | 0.57 | 0.15 | 249 |
| slow wave | 25 % → 4 % | 28.9 px | 0.57 | 0.15 | 406 |
| spiral | 39 % → 4 % | 25.7 px | 0.57 | 0.10 | 405 |
| loop | 22 % → 5 % | 28.8 px | 0.57 | 0.21 | 224 |
| tilted | 10 % → 10 % | 28.6 px | 0.57 | 0.98 | 107 |
| over the wet one | 20 % → 8 % | 28.3 px | 0.57 | 0.40 | 212 |
| long, no reload | 45 % → 6 % | 20.0 px | 0.57 | 0.13 | 588 | quarters: 0.35 → 0.27 → 0.17 → 0.08

Numbers say: light vs heavy: width 24.7 → 33.9 px, dark 0.57 → 0.57.

## Brush Artist · Refs · #09 Henry Ward white loops
Gouache · 46 px · 39.1 s

![Brush Artist · Refs · #09 Henry Ward white loops](Brush-Artist-Refs-09-Henry-Ward-white-loops.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 14 % → 13 % | 41.4 px | 0.01 | 0.94 | 136 |
| heavy line | 15 % → 15 % | 44.5 px | 0.02 | 0.96 | 130 |
| pressure swell | 12 % → 11 % | 43.9 px | 0.02 | 0.95 | 102 |
| fast wave | 36 % → 25 % | 41.9 px | 0.01 | 0.69 | 358 |
| slow wave | 36 % → 25 % | 41.8 px | 0.01 | 0.70 | 602 |
| spiral | 59 % → 28 % | 39.2 px | 0.01 | 0.46 | 635 |
| loop | 31 % → 27 % | 40.3 px | 0.01 | 0.86 | 314 |
| tilted | 13 % → 13 % | 37.3 px | 0.01 | 1.00 | 188 |
| over the wet one | 27 % → 26 % | 38.4 px | 0.01 | 0.96 | 157 |
| long, no reload | 70 % → 29 % | 31.3 px | 0.01 | 0.41 | 904 | quarters: 0.00 → 0.01 → 0.02 → 0.01

Numbers say: light vs heavy: width 41.4 → 44.5 px, dark 0.01 → 0.02; pressure barely changes the width; the long stroke does not run out of paint.

## Brush Artist · Refs · #10 Henry Ward maroon loops
Heavy acrylic · 30 px · 13.8 s

![Brush Artist · Refs · #10 Henry Ward maroon loops](Brush-Artist-Refs-10-Henry-Ward-maroon-loops.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 10 % → 9 % | 28.0 px | 0.70 | 0.94 | 78 |
| heavy line | 10 % → 10 % | 30.2 px | 0.69 | 0.95 | 81 |
| pressure swell | 8 % → 8 % | 30.0 px | 0.73 | 0.94 | 64 |
| fast wave | 24 % → 17 % | 28.3 px | 0.73 | 0.71 | 205 |
| slow wave | 25 % → 18 % | 29.0 px | 0.73 | 0.73 | 366 |
| spiral | 39 % → 18 % | 26.0 px | 0.72 | 0.47 | 355 |
| loop | 21 % → 18 % | 27.6 px | 0.72 | 0.85 | 173 |
| tilted | 10 % → 10 % | 27.9 px | 0.72 | 1.00 | 105 |
| over the wet one | 20 % → 18 % | 26.8 px | 0.72 | 0.91 | 89 |
| long, no reload | 46 % → 18 % | 20.6 px | 0.73 | 0.40 | 527 | quarters: 0.44 → 0.38 → 0.31 → 0.22

Numbers say: light vs heavy: width 28.0 → 30.2 px, dark 0.70 → 0.69; pressure barely changes the width.

## Brush Artist · Refs · #11 Henry Ward purple spun balls
Heavy acrylic · 36 px · 16.9 s

![Brush Artist · Refs · #11 Henry Ward purple spun balls](Brush-Artist-Refs-11-Henry-Ward-purple-spun-balls.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 12 % → 11 % | 34.1 px | 0.70 | 0.96 | 100 |
| heavy line | 13 % → 12 % | 36.6 px | 0.70 | 0.96 | 95 |
| pressure swell | 10 % → 9 % | 36.2 px | 0.74 | 0.95 | 68 |
| fast wave | 30 % → 23 % | 34.6 px | 0.73 | 0.75 | 258 |
| slow wave | 30 % → 24 % | 35.0 px | 0.73 | 0.79 | 455 |
| spiral | 49 % → 25 % | 32.3 px | 0.73 | 0.50 | 427 |
| loop | 26 % → 23 % | 33.4 px | 0.73 | 0.88 | 227 |
| tilted | 11 % → 11 % | 31.2 px | 0.72 | 1.00 | 132 |
| over the wet one | 23 % → 21 % | 32.1 px | 0.72 | 0.93 | 106 |
| long, no reload | 55 % → 24 % | 24.8 px | 0.73 | 0.44 | 657 | quarters: 0.51 → 0.46 → 0.39 → 0.28

Numbers say: light vs heavy: width 34.1 → 36.6 px, dark 0.70 → 0.70; pressure barely changes the width.

## Brush Artist · Refs · #12 Henry Ward black-olive cage
Gouache · 28 px · 26.1 s

![Brush Artist · Refs · #12 Henry Ward black-olive cage](Brush-Artist-Refs-12-Henry-Ward-black-olive-cage.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 7 % → 3 % | 20.9 px | 0.61 | 0.35 | 54 |
| heavy line | 9 % → 4 % | 26.1 px | 0.61 | 0.41 | 107 |
| pressure swell | 6 % → 4 % | 23.9 px | 0.61 | 0.61 | 65 |
| fast wave | 20 % → 4 % | 23.7 px | 0.61 | 0.19 | 195 |
| slow wave | 20 % → 4 % | 23.3 px | 0.61 | 0.21 | 323 |
| spiral | 32 % → 4 % | 21.4 px | 0.61 | 0.14 | 341 |
| loop | 18 % → 5 % | 22.8 px | 0.61 | 0.28 | 160 |
| tilted | 9 % → 9 % | 25.4 px | 0.61 | 0.98 | 116 |
| over the wet one | 17 % → 8 % | 21.8 px | 0.61 | 0.46 | 99 |
| long, no reload | 39 % → 6 % | 17.6 px | 0.61 | 0.15 | 731 | quarters: 0.31 → 0.26 → 0.19 → 0.10

Numbers say: light vs heavy: width 20.9 → 26.1 px, dark 0.61 → 0.61.

## Brush Artist · Refs · #13 Henry Ward blue streaky form
Gouache · 50 px · 41.4 s

![Brush Artist · Refs · #13 Henry Ward blue streaky form](Brush-Artist-Refs-13-Henry-Ward-blue-streaky-form.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 16 % → 15 % | 47.1 px | 0.09 | 0.90 | 146 |
| heavy line | 17 % → 16 % | 50.6 px | 0.09 | 0.94 | 159 |
| pressure swell | 13 % → 12 % | 49.2 px | 0.09 | 0.94 | 135 |
| fast wave | 41 % → 28 % | 47.4 px | 0.09 | 0.67 | 558 |
| slow wave | 41 % → 28 % | 47.2 px | 0.09 | 0.69 | 1084 |
| spiral | 63 % → 30 % | 41.3 px | 0.09 | 0.48 | 1041 |
| loop | 35 % → 29 % | 45.6 px | 0.09 | 0.84 | 425 |
| tilted | 14 % → 14 % | 40.3 px | 0.09 | 1.00 | 238 |
| over the wet one | 30 % → 29 % | 43.2 px | 0.09 | 0.96 | 187 |
| long, no reload | 76 % → 32 % | 33.9 px | 0.09 | 0.43 | 1268 | quarters: 0.08 → 0.07 → 0.05 → 0.03

Numbers say: light vs heavy: width 47.1 → 50.6 px, dark 0.09 → 0.09; pressure barely changes the width.

## Brush Artist · Refs · #14 Henry Ward olive totem
Heavy acrylic · 48 px · 21.9 s

![Brush Artist · Refs · #14 Henry Ward olive totem](Brush-Artist-Refs-14-Henry-Ward-olive-totem.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 15 % → 15 % | 44.8 px | 0.31 | 0.94 | 132 |
| heavy line | 16 % → 16 % | 47.7 px | 0.31 | 0.95 | 208 |
| pressure swell | 13 % → 12 % | 47.0 px | 0.32 | 0.95 | 114 |
| fast wave | 38 % → 30 % | 43.9 px | 0.30 | 0.79 | 586 |
| slow wave | 39 % → 31 % | 44.5 px | 0.30 | 0.81 | 829 |
| spiral | 58 % → 32 % | 38.1 px | 0.30 | 0.55 | 892 |
| loop | 33 % → 29 % | 42.6 px | 0.30 | 0.89 | 332 |
| tilted | 13 % → 13 % | 37.5 px | 0.31 | 1.00 | 215 |
| over the wet one | 28 % → 26 % | 41.1 px | 0.31 | 0.93 | 214 |
| long, no reload | 67 % → 33 % | 30.3 px | 0.30 | 0.49 | 1052 | quarters: 0.25 → 0.18 → 0.10 → 0.03

Numbers say: light vs heavy: width 44.8 → 47.7 px, dark 0.31 → 0.31; pressure barely changes the width.

## Brush Artist · Refs · #15 Ultramarine brush script
Ink · 10 px · 27.6 s

![Brush Artist · Refs · #15 Ultramarine brush script](Brush-Artist-Refs-15-Ultramarine-brush-script.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 2 % → 5 % | 5.0 px | 0.53 | 2.62 | 40 |
| heavy line | 10 % → 10 % | 29.6 px | 0.66 | 1.00 | 88 |
| pressure swell | 6 % → 6 % | 20.8 px | 0.68 | 1.12 | 73 |
| fast wave | 18 % → 17 % | 20.2 px | 0.59 | 0.95 | 208 |
| slow wave | 14 % → 14 % | 16.1 px | 0.59 | 1.00 | 157 |
| spiral | 22 % → 18 % | 14.5 px | 0.54 | 0.82 | 272 |
| loop | 13 % → 14 % | 17.4 px | 0.61 | 1.02 | 146 |
| tilted | 6 % → 6 % | 15.5 px | 0.68 | 1.01 | 113 |
| over the wet one | 13 % → 13 % | 20.5 px | 0.68 | 1.04 | 73 |
| long, no reload | 33 % → 20 % | 14.8 px | 0.52 | 0.59 | 580 | quarters: 0.30 → 0.14 → 0.05 → 0.02

Numbers say: light vs heavy: width 5.0 → 29.6 px, dark 0.53 → 0.66; wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #18 Blue oil-stick scribbles
Pastel · 10 px · 11.1 s

![Brush Artist · Refs · #18 Blue oil-stick scribbles](Brush-Artist-Refs-18-Blue-oil-stick-scribbles.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 1 % → 1 % | 2.9 px | 0.52 | 1.00 | 28 |
| heavy line | 2 % → 2 % | 5.5 px | 0.53 | 1.00 | 43 |
| pressure swell | 1 % → 1 % | 5.0 px | 0.53 | 1.00 | 18 |
| fast wave | 4 % → 4 % | 4.8 px | 0.53 | 1.00 | 74 |
| slow wave | 4 % → 4 % | 4.4 px | 0.53 | 1.00 | 79 |
| spiral | 7 % → 7 % | 4.5 px | 0.52 | 1.00 | 167 |
| loop | 3 % → 3 % | 4.5 px | 0.52 | 1.00 | 77 |
| tilted | 2 % → 2 % | 4.7 px | 0.53 | 1.00 | 37 |
| over the wet one | 3 % → 3 % | 4.7 px | 0.53 | 1.00 | 33 |
| long, no reload | 10 % → 10 % | 4.4 px | 0.53 | 1.00 | 193 | quarters: 0.06 → 0.06 → 0.06 → 0.06

Numbers say: light vs heavy: width 2.9 → 5.5 px, dark 0.52 → 0.53; the long stroke does not run out of paint.

## Brush Artist · Refs · #20 Orange-red crayon scribble
Pastel · 14 px · 11.1 s

![Brush Artist · Refs · #20 Orange-red crayon scribble](Brush-Artist-Refs-20-Orange-red-crayon-scribble.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 1 % → 1 % | 4.0 px | 0.53 | 1.00 | 30 |
| heavy line | 3 % → 3 % | 8.0 px | 0.53 | 1.00 | 44 |
| pressure swell | 2 % → 2 % | 7.6 px | 0.53 | 1.00 | 31 |
| fast wave | 6 % → 6 % | 7.2 px | 0.53 | 1.00 | 109 |
| slow wave | 6 % → 6 % | 6.6 px | 0.53 | 1.00 | 97 |
| spiral | 9 % → 9 % | 6.2 px | 0.53 | 1.00 | 202 |
| loop | 5 % → 5 % | 6.2 px | 0.53 | 1.00 | 72 |
| tilted | 2 % → 2 % | 5.6 px | 0.53 | 1.00 | 35 |
| over the wet one | 4 % → 4 % | 6.6 px | 0.53 | 1.00 | 29 |
| long, no reload | 13 % → 13 % | 5.7 px | 0.53 | 1.00 | 188 | quarters: 0.07 → 0.07 → 0.08 → 0.08

Numbers say: light vs heavy: width 4.0 → 8.0 px, dark 0.53 → 0.53; the long stroke does not run out of paint.

## Brush Artist · Refs · #21 Gritty black contours
Gouache · 12 px · 22.5 s

![Brush Artist · Refs · #21 Gritty black contours](Brush-Artist-Refs-21-Gritty-black-contours.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 3 % → 0 % | 8.8 px | 0.79 | 0.12 | 66 |
| heavy line | 4 % → 0 % | 11.9 px | 0.79 | 0.10 | 168 |
| pressure swell | 3 % → 0 % | 11.6 px | 0.79 | 0.15 | 75 |
| fast wave | 7 % → 1 % | 8.5 px | 0.79 | 0.10 | 234 |
| slow wave | 8 % → 1 % | 9.0 px | 0.79 | 0.09 | 224 |
| spiral | 9 % → 1 % | 6.0 px | 0.79 | 0.10 | 404 |
| loop | 8 % → 1 % | 9.9 px | 0.79 | 0.09 | 191 |
| tilted | 4 % → 4 % | 10.8 px | 0.79 | 0.90 | 70 |
| over the wet one | 7 % → 1 % | 9.7 px | 0.79 | 0.17 | 93 |
| long, no reload | 7 % → 1 % | 3.3 px | 0.79 | 0.12 | 508 | quarters: 0.20 → 0.07 → 0.00 → 0.00

Numbers say: light vs heavy: width 8.8 → 11.9 px, dark 0.79 → 0.79.

## Brush Artist · Refs · #22 Bold black brush poster
Ink · 20 px · 27.1 s

![Brush Artist · Refs · #22 Bold black brush poster](Brush-Artist-Refs-22-Bold-black-brush-poster.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 3 % → 5 % | 9.5 px | 0.79 | 1.63 | 22 |
| heavy line | 15 % → 15 % | 44.6 px | 0.88 | 0.99 | 106 |
| pressure swell | 9 % → 9 % | 31.9 px | 0.87 | 1.04 | 60 |
| fast wave | 27 % → 26 % | 31.2 px | 0.87 | 0.98 | 161 |
| slow wave | 22 % → 21 % | 25.2 px | 0.87 | 0.98 | 177 |
| spiral | 34 % → 32 % | 22.2 px | 0.87 | 0.94 | 253 |
| loop | 20 % → 20 % | 26.2 px | 0.88 | 1.00 | 144 |
| tilted | 8 % → 8 % | 22.7 px | 0.88 | 1.01 | 73 |
| over the wet one | 19 % → 19 % | 30.5 px | 0.88 | 1.00 | 57 |
| long, no reload | 45 % → 38 % | 20.2 px | 0.86 | 0.84 | 370 | quarters: 0.54 → 0.45 → 0.35 → 0.27

Numbers say: light vs heavy: width 9.5 → 44.6 px, dark 0.79 → 0.88; wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #23 Dry white on orange + black line
Gouache · 50 px · 25.2 s

![Brush Artist · Refs · #23 Dry white on orange + black line](Brush-Artist-Refs-23-Dry-white-on-orange-black-line.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 12 % → 2 % | 35.1 px | 0.01 | 0.13 | 96 |
| heavy line | 16 % → 2 % | 46.9 px | 0.00 | 0.11 | 237 |
| pressure swell | 11 % → 2 % | 42.6 px | 0.01 | 0.19 | 121 |
| fast wave | 34 % → 3 % | 39.7 px | 0.00 | 0.09 | 388 |
| slow wave | 34 % → 3 % | 39.0 px | 0.00 | 0.10 | 658 |
| spiral | 49 % → 4 % | 32.6 px | 0.00 | 0.07 | 654 |
| loop | 30 % → 4 % | 39.1 px | 0.00 | 0.12 | 340 |
| tilted | 13 % → 12 % | 34.9 px | 0.01 | 0.98 | 187 |
| over the wet one | 26 % → 7 % | 38.0 px | 0.01 | 0.27 | 167 |
| long, no reload | 58 % → 5 % | 26.1 px | 0.01 | 0.09 | 1063 | quarters: 0.01 → 0.01 → 0.00 → 0.00

Numbers say: light vs heavy: width 35.1 → 46.9 px, dark 0.01 → 0.00.

## Brush Artist · Refs · #24 Picasso flat oil
Oil · 34 px · 19.6 s

![Brush Artist · Refs · #24 Picasso flat oil](Brush-Artist-Refs-24-Picasso-flat-oil.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 11 % → 11 % | 32.2 px | 0.39 | 1.00 | 127 |
| heavy line | 12 % → 12 % | 35.0 px | 0.39 | 1.00 | 136 |
| pressure swell | 9 % → 9 % | 34.4 px | 0.41 | 1.00 | 74 |
| fast wave | 30 % → 30 % | 34.2 px | 0.41 | 1.00 | 332 |
| slow wave | 30 % → 30 % | 34.9 px | 0.41 | 1.00 | 498 |
| spiral | 51 % → 51 % | 33.7 px | 0.40 | 1.00 | 607 |
| loop | 25 % → 25 % | 32.6 px | 0.41 | 1.00 | 269 |
| tilted | 11 % → 11 % | 32.0 px | 0.41 | 1.00 | 151 |
| over the wet one | 22 % → 22 % | 30.7 px | 0.41 | 1.00 | 127 |
| long, no reload | 61 % → 61 % | 27.6 px | 0.39 | 1.00 | 793 | quarters: 0.28 → 0.28 → 0.26 → 0.24

Numbers say: light vs heavy: width 32.2 → 35.0 px, dark 0.39 → 0.39; pressure barely changes the width.

## Brush Artist · Refs · #25 Yellow heavy flat stroke
Heavy acrylic · 110 px · 35.7 s

![Brush Artist · Refs · #25 Yellow heavy flat stroke](Brush-Artist-Refs-25-Yellow-heavy-flat-stroke.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 35 % → 36 % | 101.3 px | 0.17 | 1.02 | 398 |
| heavy line | 36 % → 35 % | 105.0 px | 0.17 | 0.97 | 454 |
| pressure swell | 28 % → 29 % | 105.4 px | 0.17 | 1.04 | 289 |
| fast wave | 72 % → 76 % | 83.8 px | 0.17 | 1.05 | 1179 |
| slow wave | 73 % → 72 % | 84.7 px | 0.18 | 0.98 | 1817 |
| spiral | 86 % → 83 % | 56.7 px | 0.17 | 0.97 | 1922 |
| loop | 65 % → 64 % | 83.6 px | 0.17 | 0.99 | 1078 |
| tilted | 26 % → 26 % | 71.5 px | 0.17 | 1.00 | 537 |
| over the wet one | 55 % → 54 % | 83.1 px | 0.17 | 0.97 | 455 |
| long, no reload | 98 % → 97 % | 44.1 px | 0.17 | 0.99 | 2663 | quarters: 0.18 → 0.17 → 0.17 → 0.16

Numbers say: light vs heavy: width 101.3 → 105.0 px, dark 0.17 → 0.17; pressure barely changes the width; the long stroke does not run out of paint.

## Brush Artist · Refs · #27 Orange impasto swatch
Heavy acrylic · 60 px · 25.8 s

![Brush Artist · Refs · #27 Orange impasto swatch](Brush-Artist-Refs-27-Orange-impasto-swatch.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 20 % → 19 % | 56.7 px | 0.35 | 0.97 | 201 |
| heavy line | 20 % → 20 % | 59.3 px | 0.35 | 0.97 | 215 |
| pressure swell | 16 % → 15 % | 59.6 px | 0.36 | 0.97 | 119 |
| fast wave | 48 % → 46 % | 55.0 px | 0.35 | 0.98 | 492 |
| slow wave | 48 % → 47 % | 55.8 px | 0.36 | 0.98 | 865 |
| spiral | 69 % → 62 % | 45.5 px | 0.35 | 0.91 | 776 |
| loop | 42 % → 40 % | 53.8 px | 0.35 | 0.97 | 458 |
| tilted | 16 % → 16 % | 44.0 px | 0.36 | 1.00 | 225 |
| over the wet one | 34 % → 33 % | 50.6 px | 0.36 | 0.97 | 197 |
| long, no reload | 85 % → 75 % | 38.1 px | 0.35 | 0.88 | 1464 | quarters: 0.33 → 0.31 → 0.29 → 0.26

Numbers say: light vs heavy: width 56.7 → 59.3 px, dark 0.35 → 0.35; pressure barely changes the width.

## Brush Artist · Refs · #28 Miles Davis black lines
Ink · 22 px · 28.2 s

![Brush Artist · Refs · #28 Miles Davis black lines](Brush-Artist-Refs-28-Miles-Davis-black-lines.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 4 % → 6 % | 12.2 px | 0.81 | 1.48 | 37 |
| heavy line | 17 % → 17 % | 49.1 px | 0.88 | 0.99 | 84 |
| pressure swell | 10 % → 10 % | 35.9 px | 0.87 | 1.03 | 49 |
| fast wave | 30 % → 30 % | 35.0 px | 0.87 | 0.98 | 157 |
| slow wave | 25 % → 25 % | 28.5 px | 0.87 | 0.99 | 231 |
| spiral | 38 % → 37 % | 25.3 px | 0.87 | 0.96 | 250 |
| loop | 23 % → 23 % | 29.4 px | 0.88 | 1.00 | 113 |
| tilted | 9 % → 9 % | 25.0 px | 0.88 | 1.01 | 101 |
| over the wet one | 21 % → 21 % | 34.1 px | 0.88 | 1.00 | 68 |
| long, no reload | 51 % → 43 % | 22.7 px | 0.86 | 0.85 | 417 | quarters: 0.59 → 0.51 → 0.40 → 0.31

Numbers say: light vs heavy: width 12.2 → 49.1 px, dark 0.81 → 0.88.

## Brush Artist · Refs · #29 Shrigley magenta asterisk
Watercolor · 70 px · 31.8 s

![Brush Artist · Refs · #29 Shrigley magenta asterisk](Brush-Artist-Refs-29-Shrigley-magenta-asterisk.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 10 % → 13 % | 28.0 px | 0.45 | 1.36 | 60 |
| heavy line | 17 % → 18 % | 50.3 px | 0.44 | 1.03 | 137 |
| pressure swell | 11 % → 12 % | 41.1 px | 0.47 | 1.13 | 84 |
| fast wave | 38 % → 38 % | 43.7 px | 0.41 | 1.00 | 290 |
| slow wave | 35 % → 39 % | 41.0 px | 0.46 | 1.10 | 462 |
| spiral | 61 % → 61 % | 40.0 px | 0.40 | 1.01 | 630 |
| loop | 31 % → 32 % | 40.2 px | 0.45 | 1.03 | 275 |
| tilted | 18 % → 18 % | 49.0 px | 0.46 | 1.00 | 206 |
| over the wet one | 31 % → 34 % | 38.4 px | 0.46 | 1.07 | 116 |
| long, no reload | 75 % → 75 % | 33.5 px | 0.40 | 1.00 | 687 | quarters: 0.41 → 0.36 → 0.29 → 0.23

Numbers say: light vs heavy: width 28.0 → 50.3 px, dark 0.45 → 0.44.

## Brush Artist · Refs · #30 Red gouache face patch
Gouache · 60 px · 38.1 s

![Brush Artist · Refs · #30 Red gouache face patch](Brush-Artist-Refs-30-Red-gouache-face-patch.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 16 % → 15 % | 46.9 px | 0.49 | 0.91 | 142 |
| heavy line | 25 % → 20 % | 73.8 px | 0.49 | 0.80 | 237 |
| pressure swell | 19 % → 17 % | 72.6 px | 0.49 | 0.86 | 184 |
| fast wave | 48 % → 28 % | 55.1 px | 0.49 | 0.58 | 455 |
| slow wave | 48 % → 28 % | 55.3 px | 0.49 | 0.59 | 774 |
| spiral | 59 % → 28 % | 39.1 px | 0.49 | 0.48 | 702 |
| loop | 40 % → 29 % | 51.3 px | 0.49 | 0.74 | 440 |
| tilted | 16 % → 16 % | 45.7 px | 0.49 | 1.01 | 215 |
| over the wet one | 36 % → 32 % | 55.3 px | 0.49 | 0.88 | 199 |
| long, no reload | 67 % → 30 % | 30.0 px | 0.49 | 0.45 | 1043 | quarters: 0.43 → 0.38 → 0.32 → 0.26

Numbers say: light vs heavy: width 46.9 → 73.8 px, dark 0.49 → 0.49.

## Brush Artist · Refs · #31 Warhol blotted line
Ink · 6 px · 21.7 s

![Brush Artist · Refs · #31 Warhol blotted line](Brush-Artist-Refs-31-Warhol-blotted-line.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 1 % → 3 % | 2.6 px | 0.75 | 3.30 | 28 |
| heavy line | 7 % → 7 % | 20.6 px | 0.83 | 0.97 | 58 |
| pressure swell | 4 % → 4 % | 14.8 px | 0.84 | 1.12 | 35 |
| fast wave | 12 % → 9 % | 13.8 px | 0.82 | 0.77 | 123 |
| slow wave | 10 % → 8 % | 11.2 px | 0.80 | 0.85 | 134 |
| spiral | 15 % → 9 % | 9.7 px | 0.80 | 0.58 | 239 |
| loop | 9 % → 9 % | 11.9 px | 0.80 | 0.94 | 89 |
| tilted | 3 % → 3 % | 8.6 px | 0.84 | 1.04 | 41 |
| over the wet one | 8 % → 8 % | 14.5 px | 0.84 | 1.02 | 44 |
| long, no reload | 21 % → 9 % | 9.6 px | 0.78 | 0.43 | 284 | quarters: 0.25 → 0.13 → 0.05 → 0.01

Numbers say: light vs heavy: width 2.6 → 20.6 px, dark 0.75 → 0.83; wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #32 Thick orange swipes
Heavy acrylic · 90 px · 31.0 s

![Brush Artist · Refs · #32 Thick orange swipes](Brush-Artist-Refs-32-Thick-orange-swipes.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 29 % → 29 % | 82.9 px | 0.38 | 1.00 | 276 |
| heavy line | 30 % → 29 % | 86.3 px | 0.38 | 0.97 | 247 |
| pressure swell | 23 % → 23 % | 86.5 px | 0.38 | 1.01 | 187 |
| fast wave | 63 % → 65 % | 73.1 px | 0.38 | 1.03 | 832 |
| slow wave | 64 % → 63 % | 73.5 px | 0.39 | 0.98 | 1308 |
| spiral | 79 % → 77 % | 52.2 px | 0.38 | 0.98 | 1361 |
| loop | 57 % → 56 % | 73.4 px | 0.38 | 0.99 | 679 |
| tilted | 21 % → 21 % | 59.3 px | 0.38 | 1.00 | 361 |
| over the wet one | 47 % → 45 % | 70.7 px | 0.38 | 0.97 | 333 |
| long, no reload | 95 % → 93 % | 42.7 px | 0.38 | 0.98 | 2002 | quarters: 0.38 → 0.38 → 0.37 → 0.35

Numbers say: light vs heavy: width 82.9 → 86.3 px, dark 0.38 → 0.38; pressure barely changes the width; the long stroke does not run out of paint.

## Brush Artist · Refs · #33 Red wet-in-wet band
Watercolor · 80 px · 39.2 s

![Brush Artist · Refs · #33 Red wet-in-wet band](Brush-Artist-Refs-33-Red-wet-in-wet-band.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 21 % → 21 % | 60.7 px | 0.34 | 1.01 | 128 |
| heavy line | 30 % → 30 % | 88.4 px | 0.33 | 0.98 | 211 |
| pressure swell | 20 % → 21 % | 75.9 px | 0.36 | 1.03 | 136 |
| fast wave | 61 % → 64 % | 71.0 px | 0.30 | 1.04 | 433 |
| slow wave | 60 % → 60 % | 68.9 px | 0.41 | 1.00 | 737 |
| spiral | 75 % → 75 % | 49.7 px | 0.38 | 1.00 | 798 |
| loop | 52 % → 52 % | 67.5 px | 0.36 | 1.00 | 384 |
| tilted | 24 % → 24 % | 67.8 px | 0.37 | 1.00 | 285 |
| over the wet one | 48 % → 50 % | 66.6 px | 0.37 | 1.04 | 172 |
| long, no reload | 95 % → 96 % | 42.8 px | 0.37 | 1.00 | 1091 | quarters: 0.45 → 0.42 → 0.37 → 0.28

Numbers say: light vs heavy: width 60.7 → 88.4 px, dark 0.34 → 0.33.

## Brush Artist · Refs · #34 Magenta oil patches
Oil · 60 px · 23.6 s

![Brush Artist · Refs · #34 Magenta oil patches](Brush-Artist-Refs-34-Magenta-oil-patches.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 19 % → 19 % | 55.6 px | 0.59 | 1.00 | 191 |
| heavy line | 21 % → 21 % | 59.7 px | 0.59 | 1.00 | 190 |
| pressure swell | 16 % → 16 % | 58.8 px | 0.62 | 1.01 | 136 |
| fast wave | 48 % → 49 % | 55.4 px | 0.62 | 1.02 | 546 |
| slow wave | 48 % → 48 % | 55.8 px | 0.62 | 1.00 | 941 |
| spiral | 70 % → 70 % | 46.3 px | 0.62 | 1.00 | 966 |
| loop | 42 % → 42 % | 54.2 px | 0.62 | 1.00 | 513 |
| tilted | 17 % → 17 % | 46.8 px | 0.62 | 1.00 | 233 |
| over the wet one | 35 % → 35 % | 50.0 px | 0.62 | 1.00 | 242 |
| long, no reload | 86 % → 86 % | 38.7 px | 0.62 | 1.00 | 1389 | quarters: 0.59 → 0.58 → 0.57 → 0.52

Numbers say: light vs heavy: width 55.6 → 59.7 px, dark 0.59 → 0.59; pressure barely changes the width; the long stroke does not run out of paint.

## Brush Artist · Refs · #35 Red band with runs
Watercolor · 70 px · 36.7 s

![Brush Artist · Refs · #35 Red band with runs](Brush-Artist-Refs-35-Red-band-with-runs.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 18 % → 19 % | 53.2 px | 0.26 | 1.05 | 115 |
| heavy line | 27 % → 27 % | 78.7 px | 0.25 | 0.99 | 192 |
| pressure swell | 18 % → 18 % | 67.0 px | 0.28 | 1.02 | 111 |
| fast wave | 56 % → 56 % | 64.8 px | 0.24 | 1.00 | 385 |
| slow wave | 54 % → 55 % | 62.6 px | 0.33 | 1.01 | 603 |
| spiral | 72 % → 72 % | 47.6 px | 0.30 | 0.99 | 618 |
| loop | 48 % → 48 % | 61.7 px | 0.28 | 1.01 | 339 |
| tilted | 22 % → 22 % | 60.5 px | 0.30 | 1.00 | 241 |
| over the wet one | 43 % → 45 % | 59.7 px | 0.30 | 1.05 | 136 |
| long, no reload | 93 % → 92 % | 41.6 px | 0.29 | 0.99 | 950 | quarters: 0.34 → 0.32 → 0.27 → 0.21

Numbers say: light vs heavy: width 53.2 → 78.7 px, dark 0.26 → 0.25.

## Brush Artist · Refs · #36 Magenta letters flat brush
Gouache · 36 px · 34.3 s

![Brush Artist · Refs · #36 Magenta letters flat brush](Brush-Artist-Refs-36-Magenta-letters-flat-brush.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 10 % → 10 % | 29.0 px | 0.45 | 0.98 | 79 |
| heavy line | 17 % → 14 % | 49.1 px | 0.45 | 0.85 | 115 |
| pressure swell | 13 % → 12 % | 49.4 px | 0.45 | 0.89 | 125 |
| fast wave | 35 % → 19 % | 40.3 px | 0.45 | 0.54 | 237 |
| slow wave | 35 % → 19 % | 39.9 px | 0.45 | 0.54 | 401 |
| spiral | 46 % → 19 % | 30.4 px | 0.45 | 0.42 | 393 |
| loop | 27 % → 20 % | 35.3 px | 0.45 | 0.72 | 191 |
| tilted | 11 % → 11 % | 29.8 px | 0.45 | 1.00 | 108 |
| over the wet one | 24 % → 22 % | 38.1 px | 0.45 | 0.92 | 85 |
| long, no reload | 46 % → 19 % | 20.8 px | 0.45 | 0.40 | 605 | quarters: 0.29 → 0.25 → 0.22 → 0.18

Numbers say: light vs heavy: width 29.0 → 49.1 px, dark 0.45 → 0.45.

## Brush Artist · Refs · #37 Oil still life dabs
Oil · 40 px · 20.7 s

![Brush Artist · Refs · #37 Oil still life dabs](Brush-Artist-Refs-37-Oil-still-life-dabs.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 13 % → 13 % | 37.9 px | 0.39 | 1.00 | 152 |
| heavy line | 14 % → 14 % | 41.1 px | 0.38 | 1.00 | 158 |
| pressure swell | 11 % → 11 % | 40.2 px | 0.40 | 1.00 | 92 |
| fast wave | 34 % → 34 % | 39.8 px | 0.40 | 1.00 | 391 |
| slow wave | 35 % → 35 % | 40.2 px | 0.39 | 1.00 | 650 |
| spiral | 59 % → 59 % | 38.7 px | 0.38 | 1.00 | 610 |
| loop | 29 % → 29 % | 37.8 px | 0.39 | 1.00 | 321 |
| tilted | 13 % → 13 % | 35.8 px | 0.39 | 1.00 | 163 |
| over the wet one | 26 % → 26 % | 35.6 px | 0.39 | 1.00 | 140 |
| long, no reload | 69 % → 69 % | 30.9 px | 0.37 | 1.00 | 904 | quarters: 0.31 → 0.30 → 0.28 → 0.24

Numbers say: light vs heavy: width 37.9 → 41.1 px, dark 0.39 → 0.38; pressure barely changes the width.

## Brush Artist · Refs · #38 Sanguine drawing
Pastel · 6 px · 9.3 s

![Brush Artist · Refs · #38 Sanguine drawing](Brush-Artist-Refs-38-Sanguine-drawing.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 1 % → 1 % | 2.0 px | 0.61 | 1.00 | 27 |
| heavy line | 1 % → 1 % | 3.5 px | 0.62 | 1.00 | 20 |
| pressure swell | 1 % → 1 % | 3.3 px | 0.62 | 1.00 | 7 |
| fast wave | 3 % → 3 % | 3.2 px | 0.61 | 1.00 | 41 |
| slow wave | 3 % → 3 % | 3.0 px | 0.61 | 1.00 | 42 |
| spiral | 4 % → 4 % | 2.9 px | 0.61 | 1.00 | 86 |
| loop | 2 % → 2 % | 3.0 px | 0.61 | 1.00 | 38 |
| tilted | 1 % → 1 % | 3.4 px | 0.62 | 1.00 | 12 |
| over the wet one | 2 % → 2 % | 2.9 px | 0.62 | 1.00 | 22 |
| long, no reload | 7 % → 7 % | 3.0 px | 0.61 | 1.00 | 107 | quarters: 0.04 → 0.05 → 0.05 → 0.05

Numbers say: light vs heavy: width 2.0 → 3.5 px, dark 0.61 → 0.62; the long stroke does not run out of paint.

## Brush Artist · Refs · #39 Very thick impasto
Heavy acrylic · 60 px · 23.3 s

![Brush Artist · Refs · #39 Very thick impasto](Brush-Artist-Refs-39-Very-thick-impasto.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 20 % → 19 % | 56.8 px | 0.61 | 0.97 | 186 |
| heavy line | 20 % → 20 % | 59.4 px | 0.61 | 0.97 | 209 |
| pressure swell | 16 % → 15 % | 59.6 px | 0.62 | 0.97 | 139 |
| fast wave | 48 % → 47 % | 55.2 px | 0.62 | 0.98 | 516 |
| slow wave | 48 % → 47 % | 56.0 px | 0.62 | 0.98 | 828 |
| spiral | 69 % → 65 % | 45.6 px | 0.62 | 0.93 | 817 |
| loop | 42 % → 41 % | 54.0 px | 0.62 | 0.97 | 468 |
| tilted | 16 % → 16 % | 44.0 px | 0.62 | 1.00 | 249 |
| over the wet one | 34 % → 33 % | 50.7 px | 0.62 | 0.97 | 195 |
| long, no reload | 85 % → 79 % | 38.3 px | 0.62 | 0.93 | 1254 | quarters: 0.58 → 0.57 → 0.55 → 0.52

Numbers say: light vs heavy: width 56.8 → 59.4 px, dark 0.61 → 0.61; pressure barely changes the width; the long stroke does not run out of paint.

## Brush Artist · Refs · #40 Watercolour blooms
Watercolor · 90 px · 44.9 s

![Brush Artist · Refs · #40 Watercolour blooms](Brush-Artist-Refs-40-Watercolour-blooms.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 23 % → 24 % | 68.2 px | 0.24 | 1.02 | 151 |
| heavy line | 34 % → 33 % | 98.4 px | 0.24 | 0.98 | 323 |
| pressure swell | 23 % → 24 % | 85.3 px | 0.26 | 1.04 | 169 |
| fast wave | 66 % → 69 % | 76.7 px | 0.23 | 1.04 | 537 |
| slow wave | 65 % → 65 % | 74.7 px | 0.31 | 1.00 | 874 |
| spiral | 79 % → 79 % | 52.0 px | 0.29 | 1.00 | 931 |
| loop | 57 % → 57 % | 73.7 px | 0.27 | 1.00 | 463 |
| tilted | 26 % → 26 % | 73.8 px | 0.27 | 1.00 | 343 |
| over the wet one | 53 % → 55 % | 73.9 px | 0.27 | 1.05 | 204 |
| long, no reload | 97 % → 97 % | 43.5 px | 0.29 | 1.00 | 1277 | quarters: 0.35 → 0.33 → 0.29 → 0.22

Numbers say: light vs heavy: width 68.2 → 98.4 px, dark 0.24 → 0.24.

## Brush Artist · Refs · #41 Coloured pencil hatching
Pastel · 4 px · 10.1 s

![Brush Artist · Refs · #41 Coloured pencil hatching](Brush-Artist-Refs-41-Coloured-pencil-hatching.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 1 % → 1 % | 1.6 px | 0.42 | 1.00 | 18 |
| heavy line | 1 % → 1 % | 2.6 px | 0.43 | 1.00 | 20 |
| pressure swell | 1 % → 1 % | 2.1 px | 0.43 | 1.00 | 5 |
| fast wave | 2 % → 2 % | 2.2 px | 0.42 | 1.00 | 30 |
| slow wave | 2 % → 2 % | 2.1 px | 0.43 | 1.00 | 38 |
| spiral | 3 % → 3 % | 2.1 px | 0.43 | 1.00 | 67 |
| loop | 2 % → 2 % | 2.2 px | 0.43 | 1.00 | 26 |
| tilted | 1 % → 1 % | 3.0 px | 0.42 | 1.00 | 13 |
| over the wet one | 2 % → 2 % | 2.2 px | 0.42 | 1.00 | 15 |
| long, no reload | 5 % → 5 % | 2.3 px | 0.43 | 1.00 | 101 | quarters: 0.02 → 0.02 → 0.02 → 0.03

Numbers say: light vs heavy: width 1.6 → 2.6 px, dark 0.42 → 0.43; the long stroke does not run out of paint.

## Brush Artist · Refs · #42 Oil pastel shaggy
Pastel · 18 px · 10.4 s

![Brush Artist · Refs · #42 Oil pastel shaggy](Brush-Artist-Refs-42-Oil-pastel-shaggy.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 2 % → 2 % | 5.1 px | 0.07 | 1.00 | 32 |
| heavy line | 4 % → 4 % | 10.7 px | 0.08 | 1.00 | 26 |
| pressure swell | 3 % → 3 % | 9.5 px | 0.08 | 1.00 | 23 |
| fast wave | 8 % → 8 % | 9.0 px | 0.08 | 1.00 | 80 |
| slow wave | 7 % → 7 % | 8.2 px | 0.08 | 1.00 | 80 |
| spiral | 12 % → 12 % | 7.7 px | 0.08 | 1.00 | 89 |
| loop | 6 % → 6 % | 7.9 px | 0.08 | 1.00 | 62 |
| tilted | 2 % → 2 % | 6.9 px | 0.08 | 1.00 | 25 |
| over the wet one | 6 % → 6 % | 8.5 px | 0.08 | 1.00 | 22 |
| long, no reload | 15 % → 15 % | 6.9 px | 0.08 | 1.00 | 190 | quarters: 0.01 → 0.01 → 0.01 → 0.01

Numbers say: light vs heavy: width 5.1 → 10.7 px, dark 0.07 → 0.08; the long stroke does not run out of paint.

## Brush Artist · Refs · #43 Dragged black ink blocks
Gouache · 70 px · 36.3 s

![Brush Artist · Refs · #43 Dragged black ink blocks](Brush-Artist-Refs-43-Dragged-black-ink-blocks.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 19 % → 5 % | 54.9 px | 0.57 | 0.28 | 118 |
| heavy line | 24 % → 9 % | 69.0 px | 0.57 | 0.38 | 262 |
| pressure swell | 17 % → 9 % | 63.4 px | 0.57 | 0.53 | 185 |
| fast wave | 51 % → 11 % | 58.7 px | 0.57 | 0.21 | 568 |
| slow wave | 50 % → 10 % | 58.1 px | 0.57 | 0.20 | 1172 |
| spiral | 65 % → 14 % | 42.6 px | 0.57 | 0.22 | 1053 |
| loop | 45 % → 12 % | 58.1 px | 0.57 | 0.27 | 652 |
| tilted | 17 % → 16 % | 46.4 px | 0.57 | 0.98 | 382 |
| over the wet one | 37 % → 20 % | 55.6 px | 0.57 | 0.56 | 230 |
| long, no reload | 82 % → 17 % | 36.6 px | 0.57 | 0.21 | 2610 | quarters: 0.54 → 0.52 → 0.47 → 0.40

Numbers say: light vs heavy: width 54.9 → 69.0 px, dark 0.57 → 0.57.

## Brush Artist · Refs · #44 Blue looping ribbon
Oil · 80 px · 31.3 s

![Brush Artist · Refs · #44 Blue looping ribbon](Brush-Artist-Refs-44-Blue-looping-ribbon.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 26 % → 27 % | 74.8 px | 0.71 | 1.04 | 259 |
| heavy line | 27 % → 27 % | 79.6 px | 0.71 | 1.00 | 309 |
| pressure swell | 21 % → 21 % | 78.1 px | 0.72 | 1.03 | 307 |
| fast wave | 61 % → 64 % | 70.3 px | 0.73 | 1.05 | 1107 |
| slow wave | 61 % → 61 % | 70.0 px | 0.73 | 1.00 | 1503 |
| spiral | 78 % → 78 % | 51.3 px | 0.73 | 1.00 | 1783 |
| loop | 54 % → 54 % | 69.7 px | 0.72 | 1.00 | 657 |
| tilted | 20 % → 20 % | 57.2 px | 0.71 | 1.00 | 571 |
| over the wet one | 44 % → 44 % | 64.9 px | 0.71 | 1.00 | 500 |
| long, no reload | 96 % → 96 % | 42.8 px | 0.73 | 1.00 | 2656 | quarters: 0.72 → 0.72 → 0.72 → 0.69

Numbers say: light vs heavy: width 74.8 → 79.6 px, dark 0.71 → 0.71; pressure barely changes the width; the long stroke does not run out of paint.

## Brush Artist · Refs · #45 Soft pastel pepper
Pastel · 40 px · 12.7 s

![Brush Artist · Refs · #45 Soft pastel pepper](Brush-Artist-Refs-45-Soft-pastel-pepper.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 4 % → 4 % | 11.3 px | 0.53 | 1.00 | 46 |
| heavy line | 8 % → 8 % | 23.0 px | 0.53 | 1.00 | 48 |
| pressure swell | 5 % → 5 % | 19.5 px | 0.53 | 1.00 | 37 |
| fast wave | 17 % → 17 % | 19.4 px | 0.53 | 1.00 | 179 |
| slow wave | 15 % → 15 % | 17.1 px | 0.53 | 1.00 | 241 |
| spiral | 25 % → 25 % | 16.3 px | 0.53 | 1.00 | 273 |
| loop | 12 % → 12 % | 16.1 px | 0.53 | 1.00 | 104 |
| tilted | 5 % → 5 % | 12.8 px | 0.53 | 1.00 | 56 |
| over the wet one | 11 % → 11 % | 17.7 px | 0.53 | 1.00 | 52 |
| long, no reload | 30 % → 30 % | 13.6 px | 0.53 | 1.00 | 363 | quarters: 0.18 → 0.18 → 0.18 → 0.18

Numbers say: light vs heavy: width 11.3 → 23.0 px, dark 0.53 → 0.53; the long stroke does not run out of paint.

## Brush Artist · Refs · #46 Red-brown ink lips
Watercolor · 70 px · 41.1 s

![Brush Artist · Refs · #46 Red-brown ink lips](Brush-Artist-Refs-46-Red-brown-ink-lips.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 18 % → 18 % | 53.2 px | 0.51 | 1.00 | 128 |
| heavy line | 27 % → 27 % | 78.7 px | 0.49 | 0.98 | 239 |
| pressure swell | 18 % → 18 % | 67.0 px | 0.53 | 1.01 | 122 |
| fast wave | 56 % → 58 % | 64.8 px | 0.46 | 1.03 | 478 |
| slow wave | 54 % → 54 % | 62.6 px | 0.58 | 1.00 | 727 |
| spiral | 72 % → 72 % | 47.6 px | 0.54 | 1.00 | 673 |
| loop | 48 % → 48 % | 61.7 px | 0.53 | 1.00 | 440 |
| tilted | 22 % → 22 % | 60.5 px | 0.54 | 1.00 | 239 |
| over the wet one | 43 % → 44 % | 59.9 px | 0.54 | 1.03 | 177 |
| long, no reload | 93 % → 93 % | 41.6 px | 0.52 | 1.00 | 1006 | quarters: 0.59 → 0.57 → 0.51 → 0.40

Numbers say: light vs heavy: width 53.2 → 78.7 px, dark 0.51 → 0.49.

## Brush Artist · Refs · #47 Pink knife slabs
Heavy acrylic · 90 px · 32.7 s

![Brush Artist · Refs · #47 Pink knife slabs](Brush-Artist-Refs-47-Pink-knife-slabs.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 28 % → 27 % | 81.0 px | 0.17 | 0.97 | 192 |
| heavy line | 29 % → 28 % | 83.4 px | 0.17 | 0.97 | 262 |
| pressure swell | 22 % → 22 % | 83.4 px | 0.18 | 1.01 | 214 |
| fast wave | 61 % → 60 % | 70.1 px | 0.17 | 0.98 | 687 |
| slow wave | 61 % → 59 % | 70.9 px | 0.17 | 0.96 | 1001 |
| spiral | 76 % → 58 % | 50.0 px | 0.16 | 0.76 | 1428 |
| loop | 55 % → 54 % | 71.7 px | 0.17 | 0.97 | 555 |
| tilted | 21 % → 21 % | 59.3 px | 0.17 | 1.00 | 301 |
| over the wet one | 46 % → 44 % | 67.9 px | 0.17 | 0.96 | 262 |
| long, no reload | 92 % → 76 % | 41.3 px | 0.16 | 0.83 | 1872 | quarters: 0.18 → 0.16 → 0.14 → 0.09

Numbers say: light vs heavy: width 81.0 → 83.4 px, dark 0.17 → 0.17; pressure barely changes the width.

## Brush Artist · Refs · #48 Black bands with drips
Gouache · 70 px · 44.7 s

![Brush Artist · Refs · #48 Black bands with drips](Brush-Artist-Refs-48-Black-bands-with-drips.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 19 % → 18 % | 54.6 px | 0.69 | 0.93 | 175 |
| heavy line | 29 % → 24 % | 83.0 px | 0.69 | 0.84 | 447 |
| pressure swell | 23 % → 21 % | 86.1 px | 0.69 | 0.92 | 233 |
| fast wave | 53 % → 36 % | 61.8 px | 0.69 | 0.68 | 584 |
| slow wave | 53 % → 36 % | 61.7 px | 0.69 | 0.67 | 1008 |
| spiral | 64 % → 35 % | 41.9 px | 0.69 | 0.55 | 923 |
| loop | 45 % → 36 % | 57.8 px | 0.69 | 0.81 | 519 |
| tilted | 19 % → 19 % | 52.3 px | 0.69 | 1.00 | 292 |
| over the wet one | 41 % → 38 % | 62.4 px | 0.69 | 0.92 | 301 |
| long, no reload | 74 % → 37 % | 33.3 px | 0.69 | 0.50 | 1428 | quarters: 0.64 → 0.61 → 0.54 → 0.45

Numbers say: light vs heavy: width 54.6 → 83.0 px, dark 0.69 → 0.69.

## Brush Artist · Refs · #49 Magenta letters round brush
Ink · 30 px · 34.4 s

![Brush Artist · Refs · #49 Magenta letters round brush](Brush-Artist-Refs-49-Magenta-letters-round-brush.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 6 % → 8 % | 17.5 px | 0.50 | 1.28 | 44 |
| heavy line | 21 % → 21 % | 62.0 px | 0.51 | 0.99 | 143 |
| pressure swell | 12 % → 13 % | 46.3 px | 0.52 | 1.01 | 90 |
| fast wave | 38 % → 38 % | 44.3 px | 0.51 | 0.99 | 659 |
| slow wave | 32 % → 31 % | 36.4 px | 0.51 | 0.99 | 321 |
| spiral | 50 % → 48 % | 32.8 px | 0.51 | 0.97 | 341 |
| loop | 29 % → 29 % | 37.6 px | 0.51 | 1.00 | 171 |
| tilted | 11 % → 11 % | 30.7 px | 0.52 | 1.01 | 105 |
| over the wet one | 26 % → 26 % | 42.1 px | 0.52 | 1.01 | 107 |
| long, no reload | 61 % → 56 % | 27.5 px | 0.51 | 0.92 | 493 | quarters: 0.41 → 0.36 → 0.30 → 0.25

Numbers say: light vs heavy: width 17.5 → 62.0 px, dark 0.50 → 0.51.

## Brush Artist · Refs · #50 Thick swipes on photo
Heavy acrylic · 40 px · 20.9 s

![Brush Artist · Refs · #50 Thick swipes on photo](Brush-Artist-Refs-50-Thick-swipes-on-photo.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 13 % → 13 % | 38.0 px | 0.21 | 0.96 | 170 |
| heavy line | 14 % → 13 % | 40.1 px | 0.21 | 0.96 | 248 |
| pressure swell | 11 % → 10 % | 40.1 px | 0.22 | 0.95 | 111 |
| fast wave | 33 % → 31 % | 38.3 px | 0.21 | 0.93 | 325 |
| slow wave | 34 % → 32 % | 39.1 px | 0.20 | 0.95 | 586 |
| spiral | 58 % → 47 % | 38.5 px | 0.20 | 0.80 | 550 |
| loop | 28 % → 27 % | 36.8 px | 0.20 | 0.95 | 303 |
| tilted | 12 % → 12 % | 34.0 px | 0.22 | 1.00 | 165 |
| over the wet one | 25 % → 24 % | 35.2 px | 0.22 | 0.95 | 138 |
| long, no reload | 66 % → 46 % | 29.5 px | 0.20 | 0.70 | 870 | quarters: 0.16 → 0.13 → 0.11 → 0.07

Numbers say: light vs heavy: width 38.0 → 40.1 px, dark 0.21 → 0.21; pressure barely changes the width.

## Brush Artist · Refs · Ground #22403f
Gouache · 130 px · 66.6 s

![Brush Artist · Refs · Ground #22403f](Brush-Artist-Refs-Ground-22403f.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 42 % → 40 % | 122.8 px | 0.52 | 0.94 | 1082 |
| heavy line | 47 % → 42 % | 136.0 px | 0.52 | 0.90 | 588 |
| pressure swell | 43 % → 42 % | 162.8 px | 0.52 | 0.97 | 455 |
| fast wave | 83 % → 82 % | 95.8 px | 0.52 | 0.98 | 1858 |
| slow wave | 83 % → 76 % | 96.3 px | 0.52 | 0.91 | 2989 |
| spiral | 88 % → 84 % | 57.7 px | 0.52 | 0.96 | 2663 |
| loop | 66 % → 64 % | 85.6 px | 0.52 | 0.96 | 1588 |
| tilted | 37 % → 36 % | 102.0 px | 0.52 | 1.00 | 877 |
| over the wet one | 72 % → 69 % | 99.4 px | 0.52 | 0.96 | 840 |
| long, no reload | 98 % → 93 % | 44.0 px | 0.52 | 0.94 | 3727 | quarters: 0.52 → 0.52 → 0.52 → 0.50

Numbers say: light vs heavy: width 122.8 → 136.0 px, dark 0.52 → 0.52; pressure barely changes the width; the long stroke does not run out of paint.

## Brush Artist · Refs · Ground #2b2f1c
Gouache · 130 px · 65.7 s

![Brush Artist · Refs · Ground #2b2f1c](Brush-Artist-Refs-Ground-2b2f1c.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 42 % → 40 % | 122.8 px | 0.56 | 0.94 | 587 |
| heavy line | 47 % → 42 % | 136.0 px | 0.56 | 0.90 | 635 |
| pressure swell | 43 % → 42 % | 162.8 px | 0.56 | 0.97 | 419 |
| fast wave | 83 % → 82 % | 95.8 px | 0.56 | 0.98 | 1760 |
| slow wave | 83 % → 76 % | 96.3 px | 0.56 | 0.91 | 2775 |
| spiral | 88 % → 84 % | 57.7 px | 0.56 | 0.96 | 3102 |
| loop | 66 % → 64 % | 85.6 px | 0.56 | 0.96 | 1596 |
| tilted | 37 % → 36 % | 102.0 px | 0.56 | 1.00 | 969 |
| over the wet one | 72 % → 69 % | 99.4 px | 0.56 | 0.96 | 609 |
| long, no reload | 98 % → 93 % | 44.0 px | 0.56 | 0.94 | 3753 | quarters: 0.56 → 0.56 → 0.56 → 0.55

Numbers say: light vs heavy: width 122.8 → 136.0 px, dark 0.56 → 0.56; pressure barely changes the width; the long stroke does not run out of paint.

## Brush Artist · Refs · Ground #e8b4a8
Gouache · 130 px · 65.8 s

![Brush Artist · Refs · Ground #e8b4a8](Brush-Artist-Refs-Ground-e8b4a8.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 42 % → 40 % | 122.8 px | 0.10 | 0.94 | 623 |
| heavy line | 47 % → 42 % | 136.0 px | 0.10 | 0.90 | 951 |
| pressure swell | 43 % → 42 % | 162.8 px | 0.10 | 0.97 | 565 |
| fast wave | 83 % → 82 % | 95.8 px | 0.10 | 0.98 | 1672 |
| slow wave | 83 % → 76 % | 96.3 px | 0.10 | 0.91 | 2874 |
| spiral | 88 % → 84 % | 57.7 px | 0.10 | 0.96 | 2262 |
| loop | 66 % → 64 % | 85.6 px | 0.10 | 0.96 | 1280 |
| tilted | 37 % → 36 % | 102.0 px | 0.10 | 1.00 | 707 |
| over the wet one | 72 % → 69 % | 99.4 px | 0.10 | 0.96 | 532 |
| long, no reload | 98 % → 93 % | 44.0 px | 0.10 | 0.94 | 3068 | quarters: 0.10 → 0.11 → 0.11 → 0.10

Numbers say: light vs heavy: width 122.8 → 136.0 px, dark 0.10 → 0.10; pressure barely changes the width; the long stroke does not run out of paint.

## Brush Artist · Refs · Ground #d8d4c8
Gouache · 130 px · 64.6 s

![Brush Artist · Refs · Ground #d8d4c8](Brush-Artist-Refs-Ground-d8d4c8.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 42 % → 40 % | 122.8 px | 0.05 | 0.94 | 566 |
| heavy line | 47 % → 42 % | 136.0 px | 0.05 | 0.90 | 817 |
| pressure swell | 43 % → 42 % | 162.8 px | 0.05 | 0.97 | 554 |
| fast wave | 83 % → 82 % | 95.8 px | 0.05 | 0.98 | 1595 |
| slow wave | 83 % → 76 % | 96.3 px | 0.05 | 0.91 | 2733 |
| spiral | 88 % → 84 % | 57.7 px | 0.05 | 0.96 | 2246 |
| loop | 66 % → 64 % | 85.6 px | 0.05 | 0.96 | 1136 |
| tilted | 37 % → 36 % | 102.0 px | 0.05 | 1.00 | 654 |
| over the wet one | 72 % → 69 % | 99.4 px | 0.05 | 0.96 | 500 |
| long, no reload | 98 % → 93 % | 44.0 px | 0.05 | 0.94 | 2952 | quarters: 0.05 → 0.05 → 0.05 → 0.05

Numbers say: light vs heavy: width 122.8 → 136.0 px, dark 0.05 → 0.05; pressure barely changes the width; the long stroke does not run out of paint.

## Brush Artist · Refs · Ground #f06040
Gouache · 130 px · 65.9 s

![Brush Artist · Refs · Ground #f06040](Brush-Artist-Refs-Ground-f06040.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 42 % → 40 % | 122.8 px | 0.34 | 0.94 | 827 |
| heavy line | 47 % → 42 % | 136.0 px | 0.34 | 0.90 | 719 |
| pressure swell | 43 % → 42 % | 162.8 px | 0.34 | 0.97 | 473 |
| fast wave | 83 % → 82 % | 95.8 px | 0.34 | 0.98 | 1650 |
| slow wave | 83 % → 76 % | 96.3 px | 0.34 | 0.91 | 2685 |
| spiral | 88 % → 84 % | 57.7 px | 0.34 | 0.96 | 2234 |
| loop | 66 % → 64 % | 85.6 px | 0.34 | 0.96 | 1284 |
| tilted | 37 % → 36 % | 102.0 px | 0.34 | 1.00 | 693 |
| over the wet one | 72 % → 69 % | 99.4 px | 0.34 | 0.96 | 512 |
| long, no reload | 98 % → 93 % | 44.0 px | 0.34 | 0.94 | 3158 | quarters: 0.35 → 0.35 → 0.34 → 0.33

Numbers say: light vs heavy: width 122.8 → 136.0 px, dark 0.34 → 0.34; pressure barely changes the width; the long stroke does not run out of paint.

## Brush Artist · Refs · Ground #e85a10
Gouache · 130 px · 64.7 s

![Brush Artist · Refs · Ground #e85a10](Brush-Artist-Refs-Ground-e85a10.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 42 % → 40 % | 122.8 px | 0.37 | 0.94 | 690 |
| heavy line | 47 % → 42 % | 136.0 px | 0.37 | 0.90 | 725 |
| pressure swell | 43 % → 42 % | 162.8 px | 0.37 | 0.97 | 464 |
| fast wave | 83 % → 82 % | 95.8 px | 0.37 | 0.98 | 1610 |
| slow wave | 83 % → 76 % | 96.3 px | 0.37 | 0.91 | 2446 |
| spiral | 88 % → 84 % | 57.7 px | 0.37 | 0.96 | 2294 |
| loop | 66 % → 64 % | 85.6 px | 0.37 | 0.96 | 1217 |
| tilted | 37 % → 36 % | 102.0 px | 0.37 | 1.00 | 647 |
| over the wet one | 72 % → 69 % | 99.4 px | 0.37 | 0.96 | 570 |
| long, no reload | 98 % → 93 % | 44.0 px | 0.37 | 0.94 | 3189 | quarters: 0.37 → 0.37 → 0.37 → 0.36

Numbers say: light vs heavy: width 122.8 → 136.0 px, dark 0.37 → 0.37; pressure barely changes the width; the long stroke does not run out of paint.

## Brush Artist · Refs · Ground #8c8c88
Gouache · 130 px · 66.6 s

![Brush Artist · Refs · Ground #8c8c88](Brush-Artist-Refs-Ground-8c8c88.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 42 % → 40 % | 122.8 px | 0.24 | 0.94 | 580 |
| heavy line | 47 % → 42 % | 136.0 px | 0.24 | 0.90 | 639 |
| pressure swell | 43 % → 42 % | 162.8 px | 0.24 | 0.97 | 556 |
| fast wave | 83 % → 82 % | 95.8 px | 0.24 | 0.98 | 1431 |
| slow wave | 83 % → 76 % | 96.3 px | 0.24 | 0.91 | 2331 |
| spiral | 88 % → 84 % | 57.7 px | 0.24 | 0.96 | 2285 |
| loop | 66 % → 64 % | 85.6 px | 0.24 | 0.96 | 1178 |
| tilted | 37 % → 36 % | 102.0 px | 0.23 | 1.00 | 665 |
| over the wet one | 72 % → 69 % | 99.4 px | 0.23 | 0.96 | 529 |
| long, no reload | 98 % → 93 % | 44.0 px | 0.24 | 0.94 | 3934 | quarters: 0.24 → 0.24 → 0.24 → 0.22

Numbers say: light vs heavy: width 122.8 → 136.0 px, dark 0.24 → 0.24; pressure barely changes the width; the long stroke does not run out of paint.

## Brush Artist · Refs · Ground #f0c020
Gouache · 130 px · 65.4 s

![Brush Artist · Refs · Ground #f0c020](Brush-Artist-Refs-Ground-f0c020.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 42 % → 40 % | 122.8 px | 0.12 | 0.94 | 564 |
| heavy line | 47 % → 42 % | 136.0 px | 0.12 | 0.90 | 515 |
| pressure swell | 43 % → 42 % | 162.8 px | 0.12 | 0.97 | 419 |
| fast wave | 83 % → 82 % | 95.8 px | 0.12 | 0.98 | 1325 |
| slow wave | 83 % → 76 % | 96.3 px | 0.12 | 0.91 | 2278 |
| spiral | 88 % → 84 % | 57.7 px | 0.12 | 0.96 | 2132 |
| loop | 66 % → 64 % | 85.6 px | 0.12 | 0.96 | 1225 |
| tilted | 37 % → 36 % | 102.0 px | 0.12 | 1.00 | 863 |
| over the wet one | 72 % → 69 % | 99.4 px | 0.12 | 0.96 | 551 |
| long, no reload | 98 % → 93 % | 44.0 px | 0.12 | 0.94 | 3470 | quarters: 0.12 → 0.12 → 0.13 → 0.12

Numbers say: light vs heavy: width 122.8 → 136.0 px, dark 0.12 → 0.12; pressure barely changes the width; the long stroke does not run out of paint.

## Brush Artist · Refs · Ground #e8dcc4
Gouache · 130 px · 66.3 s

![Brush Artist · Refs · Ground #e8dcc4](Brush-Artist-Refs-Ground-e8dcc4.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 42 % → 40 % | 122.8 px | 0.03 | 0.94 | 486 |
| heavy line | 47 % → 42 % | 136.0 px | 0.03 | 0.90 | 535 |
| pressure swell | 43 % → 42 % | 162.8 px | 0.03 | 0.97 | 425 |
| fast wave | 83 % → 82 % | 95.8 px | 0.03 | 0.98 | 1454 |
| slow wave | 83 % → 76 % | 96.3 px | 0.03 | 0.91 | 2457 |
| spiral | 88 % → 84 % | 57.7 px | 0.03 | 0.96 | 2329 |
| loop | 66 % → 64 % | 85.6 px | 0.03 | 0.96 | 1623 |
| tilted | 37 % → 36 % | 102.0 px | 0.03 | 1.00 | 823 |
| over the wet one | 72 % → 69 % | 99.4 px | 0.03 | 0.96 | 663 |
| long, no reload | 98 % → 93 % | 44.0 px | 0.03 | 0.94 | 3585 | quarters: 0.03 → 0.03 → 0.03 → 0.03

Numbers say: light vs heavy: width 122.8 → 136.0 px, dark 0.03 → 0.03; pressure barely changes the width; the long stroke does not run out of paint.

## Brush Artist · Refs · Ground #f0a020
Gouache · 130 px · 68.1 s

![Brush Artist · Refs · Ground #f0a020](Brush-Artist-Refs-Ground-f0a020.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 42 % → 40 % | 122.8 px | 0.19 | 0.94 | 468 |
| heavy line | 47 % → 42 % | 136.0 px | 0.19 | 0.90 | 495 |
| pressure swell | 43 % → 42 % | 162.8 px | 0.19 | 0.97 | 412 |
| fast wave | 83 % → 82 % | 95.8 px | 0.19 | 0.98 | 1637 |
| slow wave | 83 % → 76 % | 96.3 px | 0.19 | 0.91 | 2632 |
| spiral | 88 % → 84 % | 57.7 px | 0.19 | 0.96 | 2447 |
| loop | 66 % → 64 % | 85.6 px | 0.19 | 0.96 | 1278 |
| tilted | 37 % → 36 % | 102.0 px | 0.19 | 1.00 | 744 |
| over the wet one | 72 % → 69 % | 99.4 px | 0.19 | 0.96 | 568 |
| long, no reload | 98 % → 93 % | 44.0 px | 0.19 | 0.94 | 3650 | quarters: 0.18 → 0.19 → 0.19 → 0.18

Numbers say: light vs heavy: width 122.8 → 136.0 px, dark 0.19 → 0.19; pressure barely changes the width; the long stroke does not run out of paint.

## Brush Artist · Refs · Ground #ff6a10
Gouache · 130 px · 67.6 s

![Brush Artist · Refs · Ground #ff6a10](Brush-Artist-Refs-Ground-ff6a10.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 42 % → 40 % | 122.8 px | 0.36 | 0.94 | 580 |
| heavy line | 47 % → 42 % | 136.0 px | 0.36 | 0.90 | 692 |
| pressure swell | 43 % → 42 % | 162.8 px | 0.36 | 0.97 | 492 |
| fast wave | 83 % → 82 % | 95.8 px | 0.36 | 0.98 | 1525 |
| slow wave | 83 % → 76 % | 96.3 px | 0.36 | 0.91 | 3143 |
| spiral | 88 % → 84 % | 57.7 px | 0.36 | 0.96 | 2796 |
| loop | 66 % → 64 % | 85.6 px | 0.36 | 0.96 | 1285 |
| tilted | 37 % → 36 % | 102.0 px | 0.36 | 1.00 | 1011 |
| over the wet one | 72 % → 69 % | 99.4 px | 0.36 | 0.96 | 678 |
| long, no reload | 98 % → 93 % | 44.0 px | 0.36 | 0.94 | 3570 | quarters: 0.36 → 0.36 → 0.36 → 0.35

Numbers say: light vs heavy: width 122.8 → 136.0 px, dark 0.36 → 0.36; pressure barely changes the width; the long stroke does not run out of paint.

## Brush Artist · Ink — wash
Watercolor · 38 px · 33.0 s

![Brush Artist · Ink — wash](Brush-Artist-Ink-wash.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 11 % → 11 % | 31.6 px | 0.39 | 1.03 | 64 |
| heavy line | 19 % → 19 % | 54.3 px | 0.32 | 1.03 | 98 |
| pressure swell | 12 % → 12 % | 45.1 px | 0.37 | 1.04 | 58 |
| fast wave | 39 % → 41 % | 44.7 px | 0.30 | 1.05 | 189 |
| slow wave | 37 % → 38 % | 42.6 px | 0.37 | 1.04 | 332 |
| spiral | 57 % → 60 % | 37.9 px | 0.30 | 1.04 | 314 |
| loop | 32 % → 33 % | 41.8 px | 0.35 | 1.02 | 168 |
| tilted | 13 % → 14 % | 36.8 px | 0.38 | 1.04 | 127 |
| over the wet one | 29 % → 30 % | 42.8 px | 0.38 | 1.04 | 88 |
| long, no reload | 65 % → 70 % | 29.2 px | 0.29 | 1.08 | 690 | quarters: 0.34 → 0.26 → 0.18 → 0.12

Numbers say: light vs heavy: width 31.6 → 54.3 px, dark 0.39 → 0.32.

## Brush Artist · Ink — brush line
Ink · 16 px · 27.8 s

![Brush Artist · Ink — brush line](Brush-Artist-Ink-brush-line.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 3 % → 5 % | 7.7 px | 0.78 | 1.80 | 73 |
| heavy line | 13 % → 13 % | 39.0 px | 0.88 | 0.99 | 101 |
| pressure swell | 8 % → 8 % | 28.4 px | 0.87 | 1.05 | 121 |
| fast wave | 24 % → 23 % | 27.6 px | 0.87 | 0.96 | 258 |
| slow wave | 19 % → 19 % | 22.5 px | 0.87 | 0.97 | 338 |
| spiral | 30 % → 27 % | 19.9 px | 0.86 | 0.90 | 347 |
| loop | 18 % → 18 % | 23.4 px | 0.88 | 1.00 | 132 |
| tilted | 7 % → 7 % | 20.1 px | 0.88 | 1.01 | 58 |
| over the wet one | 17 % → 17 % | 26.8 px | 0.88 | 1.00 | 57 |
| long, no reload | 42 % → 31 % | 18.8 px | 0.85 | 0.73 | 387 | quarters: 0.49 → 0.40 → 0.30 → 0.21

Numbers say: light vs heavy: width 7.7 → 39.0 px, dark 0.78 → 0.88; wet paint spreads well beyond the stroke.

## Brush Artist · Ink — dry brush
Gouache · 30 px · 23.4 s

![Brush Artist · Ink — dry brush](Brush-Artist-Ink-dry-brush.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 7 % → 1 % | 21.8 px | 0.71 | 0.11 | 76 |
| heavy line | 10 % → 1 % | 27.7 px | 0.71 | 0.10 | 124 |
| pressure swell | 7 % → 2 % | 25.5 px | 0.71 | 0.23 | 103 |
| fast wave | 21 % → 2 % | 24.2 px | 0.71 | 0.09 | 277 |
| slow wave | 21 % → 2 % | 23.9 px | 0.71 | 0.08 | 531 |
| spiral | 31 % → 2 % | 20.6 px | 0.71 | 0.06 | 396 |
| loop | 18 % → 2 % | 23.9 px | 0.71 | 0.13 | 217 |
| tilted | 9 % → 8 % | 24.1 px | 0.71 | 0.96 | 118 |
| over the wet one | 17 % → 4 % | 22.8 px | 0.71 | 0.24 | 99 |
| long, no reload | 31 % → 3 % | 14.0 px | 0.71 | 0.09 | 587 | quarters: 0.38 → 0.32 → 0.22 → 0.09

Numbers say: light vs heavy: width 21.8 → 27.7 px, dark 0.71 → 0.71.

## Brush Artist · Watercolour — blue
Watercolor · 40 px · 28.9 s

![Brush Artist · Watercolour — blue](Brush-Artist-Watercolour-blue.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 6 % → 10 % | 16.7 px | 0.21 | 1.70 | 41 |
| heavy line | 11 % → 12 % | 31.5 px | 0.21 | 1.13 | 95 |
| pressure swell | 7 % → 9 % | 25.4 px | 0.22 | 1.32 | 49 |
| fast wave | 24 % → 25 % | 27.8 px | 0.20 | 1.05 | 183 |
| slow wave | 22 % → 27 % | 25.9 px | 0.22 | 1.22 | 240 |
| spiral | 38 % → 41 % | 25.1 px | 0.18 | 1.08 | 240 |
| loop | 20 % → 22 % | 25.3 px | 0.21 | 1.13 | 126 |
| tilted | 12 % → 12 % | 33.3 px | 0.21 | 1.00 | 88 |
| over the wet one | 21 % → 24 % | 24.7 px | 0.21 | 1.15 | 65 |
| long, no reload | 51 % → 54 % | 23.0 px | 0.18 | 1.04 | 329 | quarters: 0.15 → 0.11 → 0.09 → 0.07

Numbers say: light vs heavy: width 16.7 → 31.5 px, dark 0.21 → 0.21; wet paint spreads well beyond the stroke.

## Brush Artist · Watercolour — violet
Watercolor · 40 px · 28.9 s

![Brush Artist · Watercolour — violet](Brush-Artist-Watercolour-violet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 6 % → 10 % | 16.7 px | 0.16 | 1.70 | 37 |
| heavy line | 11 % → 12 % | 31.5 px | 0.16 | 1.13 | 76 |
| pressure swell | 7 % → 9 % | 25.4 px | 0.17 | 1.32 | 64 |
| fast wave | 24 % → 25 % | 27.8 px | 0.15 | 1.05 | 153 |
| slow wave | 22 % → 27 % | 25.9 px | 0.16 | 1.22 | 243 |
| spiral | 38 % → 41 % | 25.1 px | 0.14 | 1.08 | 249 |
| loop | 20 % → 22 % | 25.3 px | 0.16 | 1.13 | 116 |
| tilted | 12 % → 12 % | 33.3 px | 0.16 | 1.00 | 103 |
| over the wet one | 21 % → 24 % | 24.7 px | 0.16 | 1.15 | 59 |
| long, no reload | 51 % → 54 % | 23.0 px | 0.14 | 1.04 | 351 | quarters: 0.11 → 0.09 → 0.07 → 0.06

Numbers say: light vs heavy: width 16.7 → 31.5 px, dark 0.16 → 0.16; wet paint spreads well beyond the stroke.

## Brush Artist · Watercolour — teal
Watercolor · 40 px · 27.9 s

![Brush Artist · Watercolour — teal](Brush-Artist-Watercolour-teal.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 6 % → 10 % | 16.7 px | 0.29 | 1.70 | 32 |
| heavy line | 11 % → 12 % | 31.5 px | 0.29 | 1.13 | 64 |
| pressure swell | 7 % → 9 % | 25.4 px | 0.30 | 1.32 | 37 |
| fast wave | 24 % → 25 % | 27.8 px | 0.28 | 1.05 | 133 |
| slow wave | 22 % → 27 % | 25.9 px | 0.30 | 1.22 | 228 |
| spiral | 38 % → 41 % | 25.1 px | 0.26 | 1.08 | 206 |
| loop | 20 % → 22 % | 25.3 px | 0.30 | 1.13 | 110 |
| tilted | 12 % → 12 % | 33.3 px | 0.30 | 1.00 | 85 |
| over the wet one | 21 % → 24 % | 24.7 px | 0.30 | 1.15 | 45 |
| long, no reload | 51 % → 54 % | 23.0 px | 0.25 | 1.04 | 354 | quarters: 0.21 → 0.16 → 0.13 → 0.10

Numbers say: light vs heavy: width 16.7 → 31.5 px, dark 0.29 → 0.29; wet paint spreads well beyond the stroke.

## Brush Artist · Gouache
Gouache · 30 px · 32.2 s

![Brush Artist · Gouache](Brush-Artist-Gouache.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 8 % → 8 % | 24.4 px | 0.16 | 0.97 | 60 |
| heavy line | 15 % → 11 % | 42.8 px | 0.16 | 0.78 | 93 |
| pressure swell | 11 % → 9 % | 41.0 px | 0.16 | 0.84 | 62 |
| fast wave | 30 % → 13 % | 34.4 px | 0.16 | 0.45 | 193 |
| slow wave | 29 % → 14 % | 33.9 px | 0.16 | 0.46 | 310 |
| spiral | 40 % → 14 % | 26.6 px | 0.16 | 0.35 | 346 |
| loop | 23 % → 15 % | 30.4 px | 0.16 | 0.62 | 236 |
| tilted | 10 % → 10 % | 27.1 px | 0.16 | 1.01 | 113 |
| over the wet one | 21 % → 19 % | 32.8 px | 0.16 | 0.89 | 96 |
| long, no reload | 43 % → 15 % | 19.1 px | 0.16 | 0.35 | 502 | quarters: 0.10 → 0.07 → 0.04 → 0.02

Numbers say: light vs heavy: width 24.4 → 42.8 px, dark 0.16 → 0.16.

## Brush Artist · Oil — bristle
Oil · 30 px · 20.4 s

![Brush Artist · Oil — bristle](Brush-Artist-Oil-bristle.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 9 % → 9 % | 26.2 px | 0.54 | 1.00 | 88 |
| heavy line | 10 % → 10 % | 28.5 px | 0.54 | 1.00 | 84 |
| pressure swell | 8 % → 8 % | 28.2 px | 0.55 | 1.00 | 87 |
| fast wave | 24 % → 24 % | 27.3 px | 0.55 | 1.00 | 257 |
| slow wave | 24 % → 24 % | 28.2 px | 0.55 | 1.00 | 439 |
| spiral | 39 % → 39 % | 25.6 px | 0.54 | 1.00 | 496 |
| loop | 20 % → 20 % | 26.2 px | 0.54 | 1.00 | 250 |
| tilted | 11 % → 11 % | 29.9 px | 0.54 | 1.00 | 167 |
| over the wet one | 20 % → 20 % | 25.2 px | 0.54 | 1.00 | 170 |
| long, no reload | 50 % → 50 % | 22.4 px | 0.54 | 1.00 | 693 | quarters: 0.32 → 0.30 → 0.29 → 0.28

Numbers say: light vs heavy: width 26.2 → 28.5 px, dark 0.54 → 0.54; pressure barely changes the width; the long stroke does not run out of paint.

## Brush Artist · Charcoal — stick
Charcoal · 28 px · 10.5 s

![Brush Artist · Charcoal — stick](Brush-Artist-Charcoal-stick.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 3 % → 3 % | 8.4 px | 0.85 | 1.00 | 35 |
| heavy line | 6 % → 6 % | 17.8 px | 0.85 | 1.00 | 25 |
| pressure swell | 4 % → 4 % | 13.9 px | 0.85 | 1.00 | 16 |
| fast wave | 12 % → 12 % | 14.0 px | 0.85 | 1.00 | 49 |
| slow wave | 11 % → 11 % | 12.5 px | 0.85 | 1.00 | 90 |
| spiral | 19 % → 19 % | 12.7 px | 0.85 | 1.00 | 104 |
| loop | 10 % → 10 % | 12.8 px | 0.85 | 1.00 | 55 |
| tilted | 4 % → 4 % | 10.9 px | 0.85 | 1.00 | 83 |
| over the wet one | 9 % → 9 % | 13.5 px | 0.85 | 1.00 | 24 |
| long, no reload | 27 % → 27 % | 12.2 px | 0.85 | 1.00 | 139 | quarters: 0.26 → 0.25 → 0.26 → 0.27

Numbers say: light vs heavy: width 8.4 → 17.8 px, dark 0.85 → 0.85; the long stroke does not run out of paint.

## Brush Artist · Charcoal — stick B
Charcoal · 36 px · 10.7 s

![Brush Artist · Charcoal — stick B](Brush-Artist-Charcoal-stick-B.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 4 % → 4 % | 10.5 px | 0.85 | 1.00 | 23 |
| heavy line | 7 % → 7 % | 21.1 px | 0.85 | 1.00 | 35 |
| pressure swell | 4 % → 4 % | 16.5 px | 0.85 | 1.00 | 22 |
| fast wave | 15 % → 15 % | 16.8 px | 0.85 | 1.00 | 72 |
| slow wave | 13 % → 13 % | 14.7 px | 0.85 | 1.00 | 109 |
| spiral | 23 % → 23 % | 15.0 px | 0.85 | 1.00 | 97 |
| loop | 11 % → 11 % | 14.8 px | 0.85 | 1.00 | 59 |
| tilted | 4 % → 4 % | 12.3 px | 0.85 | 1.00 | 48 |
| over the wet one | 10 % → 10 % | 15.9 px | 0.85 | 1.00 | 32 |
| long, no reload | 31 % → 31 % | 13.9 px | 0.85 | 1.00 | 159 | quarters: 0.30 → 0.28 → 0.29 → 0.30

Numbers say: light vs heavy: width 10.5 → 21.1 px, dark 0.85 → 0.85; the long stroke does not run out of paint.

## Brush Artist · Charcoal — stick C
Charcoal · 22 px · 10.1 s

![Brush Artist · Charcoal — stick C](Brush-Artist-Charcoal-stick-C.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 2 % → 2 % | 6.9 px | 0.85 | 1.00 | 13 |
| heavy line | 5 % → 5 % | 15.3 px | 0.85 | 1.00 | 26 |
| pressure swell | 3 % → 3 % | 12.2 px | 0.85 | 1.00 | 10 |
| fast wave | 10 % → 10 % | 12.1 px | 0.85 | 1.00 | 43 |
| slow wave | 9 % → 9 % | 10.8 px | 0.85 | 1.00 | 74 |
| spiral | 17 % → 17 % | 11.0 px | 0.85 | 1.00 | 63 |
| loop | 9 % → 9 % | 11.4 px | 0.85 | 1.00 | 29 |
| tilted | 4 % → 4 % | 9.9 px | 0.85 | 1.00 | 29 |
| over the wet one | 8 % → 8 % | 11.7 px | 0.85 | 1.00 | 20 |
| long, no reload | 24 % → 24 % | 11.0 px | 0.85 | 1.00 | 108 | quarters: 0.24 → 0.22 → 0.23 → 0.24

Numbers say: light vs heavy: width 6.9 → 15.3 px, dark 0.85 → 0.85; the long stroke does not run out of paint.

## Brush Artist · Refs · #01 Henry Ward peach cloud — own sheet
own sheet 600 × 600 · Gouache · 44 px · 75.9 s

![Brush Artist · Refs · #01 Henry Ward peach cloud — own sheet](Brush-Artist-Refs-01-Henry-Ward-peach-cloud-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 99 % → 99 % | 62.0 px | 0.00 | 1.00 | 1183 |
| stroke 2 | 100 % → 99 % | 88.9 px | 0.00 | 0.99 | 1350 |
| stroke 3 | 99 % → 99 % | 88.0 px | 0.00 | 1.00 | 1252 |
| stroke 4 | 100 % → 99 % | 85.6 px | 0.00 | 0.99 | 1193 |
| stroke 5 | 99 % → 98 % | 88.6 px | 0.00 | 0.99 | 1206 |
| stroke 6 | 100 % → 99 % | 87.2 px | 0.00 | 0.99 | 1231 |
| stroke 7 | 99 % → 99 % | 90.9 px | 0.00 | 1.00 | 1165 |
| stroke 8 | 100 % → 98 % | 88.7 px | 0.00 | 0.99 | 1066 |
| stroke 9 | 100 % → 98 % | 60.0 px | 0.00 | 0.98 | 831 |
| stroke 10 | 100 % → 100 % | 129.9 px | 0.00 | 1.00 | 158 |
| stroke 11 | 100 % → 100 % | 160.5 px | 0.00 | 1.00 | 152 |
| stroke 12 | 100 % → 100 % | 131.4 px | 0.00 | 1.00 | 149 |
| stroke 13 | 100 % → 100 % | 162.0 px | 0.00 | 1.00 | 136 |
| stroke 14 | 100 % → 100 % | 135.7 px | 0.00 | 1.00 | 159 |
| stroke 15 | 100 % → 100 % | 148.2 px | 0.00 | 1.00 | 159 |
| stroke 16 | 100 % → 100 % | 138.8 px | 0.00 | 1.00 | 165 |
| stroke 17 | 100 % → 100 % | 129.3 px | 0.00 | 1.00 | 198 |
| stroke 18 | 100 % → 100 % | 124.6 px | 0.00 | 1.00 | 189 |
| stroke 19 | 100 % → 100 % | 125.6 px | 0.00 | 1.00 | 209 |
| stroke 20 | 100 % → 100 % | 137.3 px | 0.00 | 1.00 | 209 |
| stroke 21 | 100 % → 100 % | 136.3 px | 0.00 | 1.00 | 182 |
| stroke 22 | 100 % → 100 % | 132.5 px | 0.00 | 1.00 | 177 |
| stroke 23 | 100 % → 100 % | 129.7 px | 0.00 | 1.00 | 210 |
| stroke 24 | 100 % → 100 % | 135.8 px | 0.00 | 1.00 | 162 |
| stroke 25 | 100 % → 100 % | 140.2 px | 0.00 | 1.00 | 175 |
| stroke 26 | 100 % → 100 % | 124.0 px | 0.00 | 1.00 | 199 |
| stroke 27 | 100 % → 100 % | 131.8 px | 0.00 | 1.00 | 180 |
| stroke 28 | 100 % → 100 % | 124.2 px | 0.00 | 1.00 | 192 |
| stroke 29 | 100 % → 100 % | 131.9 px | 0.00 | 1.00 | 180 |
| stroke 30 | 100 % → 100 % | 134.2 px | 0.00 | 1.00 | 178 |
| stroke 31 | 100 % → 100 % | 134.5 px | 0.00 | 1.00 | 199 |
| stroke 32 | 100 % → 100 % | 127.6 px | 0.00 | 1.00 | 219 |
| stroke 33 | 100 % → 100 % | 134.4 px | 0.00 | 1.00 | 180 |

## Brush Artist · Refs · #02 Henry Ward cream strokes — own sheet
own sheet 600 × 600 · Gouache · 46 px · 68.3 s

![Brush Artist · Refs · #02 Henry Ward cream strokes — own sheet](Brush-Artist-Refs-02-Henry-Ward-cream-strokes-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 95 % → 99 % | 58.8 px | 0.00 | 1.04 | 1012 |
| stroke 2 | 99 % → 99 % | 91.6 px | 0.00 | 1.00 | 1657 |
| stroke 3 | 98 % → 99 % | 89.0 px | 0.00 | 1.01 | 1204 |
| stroke 4 | 95 % → 99 % | 89.9 px | 0.00 | 1.04 | 1203 |
| stroke 5 | 98 % → 99 % | 90.2 px | 0.00 | 1.00 | 1059 |
| stroke 6 | 100 % → 99 % | 89.6 px | 0.00 | 1.00 | 1142 |
| stroke 7 | 99 % → 99 % | 93.0 px | 0.00 | 1.00 | 1083 |
| stroke 8 | 98 % → 99 % | 92.0 px | 0.00 | 1.00 | 1118 |
| stroke 9 | 100 % → 99 % | 61.8 px | 0.00 | 0.99 | 850 |
| stroke 10 | 100 % → 99 % | 129.9 px | 0.00 | 0.99 | 228 |
| stroke 11 | 100 % → 99 % | 142.3 px | 0.00 | 0.99 | 252 |
| stroke 12 | 100 % → 100 % | 138.5 px | 0.00 | 1.00 | 252 |
| stroke 13 | 100 % → 99 % | 137.9 px | 0.00 | 0.99 | 245 |
| stroke 14 | 100 % → 98 % | 129.1 px | 0.00 | 0.99 | 230 |
| stroke 15 | 100 % → 100 % | 121.4 px | 0.00 | 1.00 | 242 |
| stroke 16 | 100 % → 100 % | 128.5 px | 0.00 | 1.00 | 260 |

## Brush Artist · Refs · #03 Henry Ward navy contours — own sheet
own sheet 600 × 600 · Heavy acrylic · 22 px · 2.9 s

![Brush Artist · Refs · #03 Henry Ward navy contours — own sheet](Brush-Artist-Refs-03-Henry-Ward-navy-contours-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 15 % → 20 % | 23.1 px | 0.75 | 1.28 | 130 |
| stroke 2 | 28 % → 30 % | 26.3 px | 0.75 | 1.09 | 107 |
| stroke 3 | 28 % → 28 % | 29.4 px | 0.75 | 0.99 | 135 |
| stroke 4 | 26 % → 24 % | 45.9 px | 0.75 | 0.92 | 148 |

## Brush Artist · Refs · #04 Henry Ward grey cloud — own sheet
own sheet 600 × 600 · Gouache · 50 px · 15.1 s

![Brush Artist · Refs · #04 Henry Ward grey cloud — own sheet](Brush-Artist-Refs-04-Henry-Ward-grey-cloud-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 33 % → 59 % | 49.5 px | 0.12 | 1.81 | 225 |
| stroke 2 | 38 % → 64 % | 58.2 px | 0.12 | 1.68 | 284 |
| stroke 3 | 59 % → 82 % | 81.0 px | 0.12 | 1.39 | 260 |
| stroke 4 | 58 % → 83 % | 87.5 px | 0.12 | 1.41 | 248 |
| stroke 5 | 61 % → 86 % | 90.7 px | 0.12 | 1.41 | 219 |
| stroke 6 | 61 % → 89 % | 98.2 px | 0.12 | 1.45 | 203 |
| stroke 7 | 60 % → 84 % | 88.7 px | 0.12 | 1.39 | 273 |
| stroke 8 | 57 % → 84 % | 85.9 px | 0.12 | 1.48 | 218 |
| stroke 9 | 60 % → 86 % | 88.9 px | 0.12 | 1.44 | 269 |
| stroke 10 | 61 % → 88 % | 98.3 px | 0.12 | 1.44 | 255 |
| stroke 11 | 61 % → 86 % | 83.2 px | 0.12 | 1.40 | 240 |
| stroke 12 | 62 % → 86 % | 94.7 px | 0.12 | 1.38 | 241 |
| stroke 13 | 62 % → 86 % | 84.6 px | 0.12 | 1.39 | 240 |
| stroke 14 | 60 % → 84 % | 93.4 px | 0.12 | 1.39 | 209 |
| stroke 15 | 60 % → 83 % | 88.4 px | 0.12 | 1.38 | 240 |
| stroke 16 | 61 % → 84 % | 96.2 px | 0.12 | 1.38 | 247 |
| stroke 17 | 60 % → 84 % | 84.0 px | 0.12 | 1.41 | 221 |
| stroke 18 | 61 % → 84 % | 96.8 px | 0.12 | 1.39 | 224 |
| stroke 19 | 60 % → 62 % | 89.9 px | 0.12 | 1.03 | 255 |
| stroke 20 | 61 % → 61 % | 99.6 px | 0.12 | 0.99 | 249 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #05 Henry Ward green in rust loops — own sheet
own sheet 600 × 600 · Heavy acrylic · 20 px · 2.6 s

![Brush Artist · Refs · #05 Henry Ward green in rust loops — own sheet](Brush-Artist-Refs-05-Henry-Ward-green-in-rust-loops-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 16 % → 24 % | 20.9 px | 0.57 | 1.48 | 126 |
| stroke 2 | 15 % → 13 % | 22.7 px | 0.58 | 0.90 | 153 |
| stroke 3 | 25 % → 24 % | 37.1 px | 0.58 | 0.94 | 121 |

## Brush Artist · Refs · #06 Henry Ward scrubbed grey — own sheet
own sheet 600 × 600 · Gouache · 50 px · 16.2 s

![Brush Artist · Refs · #06 Henry Ward scrubbed grey — own sheet](Brush-Artist-Refs-06-Henry-Ward-scrubbed-grey-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 35 % → 59 % | 49.2 px | 0.10 | 1.71 | 341 |
| stroke 2 | 41 % → 66 % | 64.6 px | 0.10 | 1.58 | 252 |
| stroke 3 | 59 % → 89 % | 86.2 px | 0.10 | 1.51 | 207 |
| stroke 4 | 58 % → 88 % | 92.9 px | 0.10 | 1.51 | 252 |
| stroke 5 | 56 % → 86 % | 84.4 px | 0.10 | 1.53 | 222 |
| stroke 6 | 60 % → 86 % | 93.2 px | 0.10 | 1.44 | 219 |
| stroke 7 | 61 % → 85 % | 88.7 px | 0.10 | 1.38 | 209 |
| stroke 8 | 62 % → 88 % | 98.2 px | 0.10 | 1.43 | 223 |
| stroke 9 | 61 % → 89 % | 88.8 px | 0.10 | 1.46 | 220 |
| stroke 10 | 59 % → 89 % | 95.5 px | 0.10 | 1.50 | 213 |
| stroke 11 | 60 % → 84 % | 85.9 px | 0.10 | 1.42 | 202 |
| stroke 12 | 58 % → 83 % | 93.4 px | 0.10 | 1.43 | 231 |
| stroke 13 | 58 % → 83 % | 83.2 px | 0.10 | 1.44 | 207 |
| stroke 14 | 56 % → 84 % | 84.9 px | 0.10 | 1.49 | 206 |
| stroke 15 | 58 % → 85 % | 83.3 px | 0.10 | 1.46 | 225 |
| stroke 16 | 63 % → 90 % | 96.7 px | 0.10 | 1.44 | 233 |
| stroke 17 | 61 % → 86 % | 88.7 px | 0.10 | 1.42 | 216 |
| stroke 18 | 61 % → 85 % | 95.6 px | 0.10 | 1.39 | 237 |
| stroke 19 | 57 % → 85 % | 87.0 px | 0.10 | 1.49 | 195 |
| stroke 20 | 58 % → 84 % | 93.6 px | 0.10 | 1.45 | 206 |
| stroke 21 | 58 % → 68 % | 84.6 px | 0.10 | 1.17 | 306 |
| stroke 22 | 62 % → 61 % | 98.3 px | 0.10 | 0.99 | 224 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #07 Henry Ward blue L + black zigzag — own sheet
own sheet 600 × 600 · Heavy acrylic · 34 px · 2.0 s

![Brush Artist · Refs · #07 Henry Ward blue L + black zigzag — own sheet](Brush-Artist-Refs-07-Henry-Ward-blue-L-black-zigzag-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 30 % → 31 % | 35.6 px | 0.63 | 1.05 | 127 |
| stroke 2 | 31 % → 29 % | 38.6 px | 0.63 | 0.94 | 92 |

## Brush Artist · Refs · #08 Henry Ward olive bands — own sheet
own sheet 600 × 600 · Gouache · 34 px · 5.7 s

![Brush Artist · Refs · #08 Henry Ward olive bands — own sheet](Brush-Artist-Refs-08-Henry-Ward-olive-bands-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 33 % → 19 % | 32.3 px | 0.61 | 0.58 | 138 |
| stroke 2 | 37 % → 20 % | 44.3 px | 0.61 | 0.53 | 197 |
| stroke 3 | 30 % → 23 % | 32.4 px | 0.61 | 0.75 | 173 |
| stroke 4 | 38 % → 37 % | 44.3 px | 0.61 | 0.98 | 187 |
| stroke 5 | 50 % → 35 % | 52.4 px | 0.61 | 0.71 | 178 |
| stroke 6 | 36 % → 22 % | 32.2 px | 0.61 | 0.61 | 159 |

## Brush Artist · Refs · #09 Henry Ward white loops — own sheet
own sheet 600 × 600 · Gouache · 46 px · 66.5 s

![Brush Artist · Refs · #09 Henry Ward white loops — own sheet](Brush-Artist-Refs-09-Henry-Ward-white-loops-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 96 % → 99 % | 59.1 px | 0.00 | 1.03 | 862 |
| stroke 2 | 99 % → 100 % | 91.6 px | 0.00 | 1.01 | 1075 |
| stroke 3 | 97 % → 99 % | 89.3 px | 0.00 | 1.02 | 1103 |
| stroke 4 | 99 % → 99 % | 90.3 px | 0.00 | 1.00 | 1122 |
| stroke 5 | 97 % → 99 % | 89.4 px | 0.00 | 1.02 | 1131 |
| stroke 6 | 95 % → 99 % | 90.2 px | 0.00 | 1.05 | 1157 |
| stroke 7 | 99 % → 99 % | 92.7 px | 0.00 | 1.00 | 1108 |
| stroke 8 | 98 % → 99 % | 92.0 px | 0.00 | 1.01 | 1125 |
| stroke 9 | 100 % → 99 % | 64.4 px | 0.00 | 0.99 | 931 |
| stroke 10 | 100 % → 100 % | 31.6 px | 0.00 | 1.00 | 1100 |
| stroke 11 | 100 % → 100 % | 70.2 px | 0.00 | 1.00 | 1205 |
| stroke 12 | 100 % → 100 % | 58.2 px | 0.00 | 1.00 | 1051 |

## Brush Artist · Refs · #10 Henry Ward maroon loops — own sheet
own sheet 600 × 600 · Heavy acrylic · 30 px · 3.0 s

![Brush Artist · Refs · #10 Henry Ward maroon loops — own sheet](Brush-Artist-Refs-10-Henry-Ward-maroon-loops-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 16 % → 33 % | 28.6 px | 0.77 | 2.07 | 235 |
| stroke 2 | 29 % → 47 % | 46.0 px | 0.77 | 1.60 | 110 |
| stroke 3 | 40 % → 50 % | 54.7 px | 0.77 | 1.24 | 193 |
| stroke 4 | 45 % → 43 % | 64.1 px | 0.77 | 0.96 | 96 |
| stroke 5 | 41 % → 38 % | 70.6 px | 0.77 | 0.93 | 148 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #11 Henry Ward purple spun balls — own sheet
own sheet 600 × 600 · Heavy acrylic · 36 px · 65.2 s

![Brush Artist · Refs · #11 Henry Ward purple spun balls — own sheet](Brush-Artist-Refs-11-Henry-Ward-purple-spun-balls-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 100 % → 99 % | 54.7 px | 0.00 | 0.99 | 916 |
| stroke 2 | 100 % → 99 % | 73.2 px | 0.00 | 0.99 | 1204 |
| stroke 3 | 100 % → 99 % | 77.6 px | 0.00 | 0.99 | 1081 |
| stroke 4 | 100 % → 100 % | 75.0 px | 0.00 | 1.00 | 1042 |
| stroke 5 | 100 % → 99 % | 75.9 px | 0.00 | 0.99 | 999 |
| stroke 6 | 100 % → 99 % | 76.8 px | 0.07 | 0.99 | 1107 |
| stroke 7 | 100 % → 99 % | 75.0 px | 0.26 | 0.99 | 1139 |
| stroke 8 | 100 % → 99 % | 75.9 px | 0.31 | 0.99 | 1049 |
| stroke 9 | 100 % → 99 % | 55.6 px | 0.04 | 0.99 | 916 |
| stroke 10 | 100 % → 100 % | 49.5 px | 0.28 | 1.00 | 395 |
| stroke 11 | 100 % → 100 % | 48.8 px | 0.35 | 1.00 | 388 |
| stroke 12 | 100 % → 100 % | 48.7 px | 0.30 | 1.00 | 380 |

## Brush Artist · Refs · #12 Henry Ward black-olive cage — own sheet
own sheet 600 × 600 · Gouache · 28 px · 6.0 s

![Brush Artist · Refs · #12 Henry Ward black-olive cage — own sheet](Brush-Artist-Refs-12-Henry-Ward-black-olive-cage-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 18 % → 22 % | 24.3 px | 0.65 | 1.24 | 184 |
| stroke 2 | 16 % → 26 % | 27.7 px | 0.65 | 1.61 | 233 |
| stroke 3 | 34 % → 34 % | 40.4 px | 0.65 | 1.01 | 266 |
| stroke 4 | 34 % → 34 % | 42.8 px | 0.65 | 1.03 | 144 |
| stroke 5 | 34 % → 21 % | 43.1 px | 0.65 | 0.60 | 173 |
| stroke 6 | 52 % → 37 % | 67.3 px | 0.65 | 0.72 | 212 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #13 Henry Ward blue streaky form — own sheet
own sheet 600 × 600 · Gouache · 50 px · 16.0 s

![Brush Artist · Refs · #13 Henry Ward blue streaky form — own sheet](Brush-Artist-Refs-13-Henry-Ward-blue-streaky-form-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 34 % → 64 % | 49.1 px | 0.10 | 1.86 | 229 |
| stroke 2 | 42 % → 66 % | 67.5 px | 0.10 | 1.58 | 250 |
| stroke 3 | 60 % → 86 % | 85.2 px | 0.10 | 1.43 | 214 |
| stroke 4 | 60 % → 89 % | 97.8 px | 0.10 | 1.49 | 236 |
| stroke 5 | 61 % → 86 % | 86.7 px | 0.10 | 1.42 | 270 |
| stroke 6 | 56 % → 82 % | 86.1 px | 0.10 | 1.47 | 247 |
| stroke 7 | 62 % → 85 % | 92.3 px | 0.10 | 1.38 | 223 |
| stroke 8 | 62 % → 85 % | 96.3 px | 0.10 | 1.37 | 214 |
| stroke 9 | 62 % → 87 % | 94.7 px | 0.10 | 1.41 | 215 |
| stroke 10 | 63 % → 89 % | 102.4 px | 0.10 | 1.40 | 211 |
| stroke 11 | 58 % → 86 % | 87.3 px | 0.10 | 1.48 | 242 |
| stroke 12 | 58 % → 82 % | 91.0 px | 0.10 | 1.42 | 229 |
| stroke 13 | 61 % → 88 % | 89.4 px | 0.10 | 1.44 | 213 |
| stroke 14 | 54 % → 82 % | 83.9 px | 0.10 | 1.53 | 257 |
| stroke 15 | 57 % → 83 % | 82.3 px | 0.10 | 1.45 | 258 |
| stroke 16 | 56 % → 84 % | 90.5 px | 0.10 | 1.51 | 231 |
| stroke 17 | 61 % → 84 % | 93.7 px | 0.10 | 1.39 | 225 |
| stroke 18 | 61 % → 82 % | 95.3 px | 0.10 | 1.35 | 251 |
| stroke 19 | 68 % → 80 % | 84.6 px | 0.10 | 1.18 | 235 |
| stroke 20 | 78 % → 77 % | 93.1 px | 0.10 | 0.99 | 281 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #14 Henry Ward olive totem — own sheet
own sheet 600 × 600 · Heavy acrylic · 48 px · 7.4 s

![Brush Artist · Refs · #14 Henry Ward olive totem — own sheet](Brush-Artist-Refs-14-Henry-Ward-olive-totem-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 31 % → 50 % | 46.9 px | 0.33 | 1.58 | 159 |
| stroke 2 | 36 % → 62 % | 64.3 px | 0.33 | 1.71 | 120 |
| stroke 3 | 54 % → 76 % | 79.7 px | 0.34 | 1.42 | 138 |
| stroke 4 | 50 % → 73 % | 88.4 px | 0.34 | 1.46 | 144 |
| stroke 5 | 56 % → 78 % | 83.2 px | 0.33 | 1.39 | 128 |
| stroke 6 | 54 % → 81 % | 96.5 px | 0.34 | 1.50 | 144 |
| stroke 7 | 52 % → 75 % | 74.2 px | 0.34 | 1.45 | 128 |
| stroke 8 | 51 % → 77 % | 90.4 px | 0.34 | 1.53 | 157 |
| stroke 9 | 56 % → 81 % | 82.9 px | 0.34 | 1.44 | 126 |
| stroke 10 | 56 % → 78 % | 94.7 px | 0.34 | 1.40 | 138 |
| stroke 11 | 57 % → 79 % | 90.0 px | 0.34 | 1.38 | 154 |
| stroke 12 | 53 % → 80 % | 90.4 px | 0.34 | 1.53 | 142 |
| stroke 13 | 55 % → 83 % | 82.0 px | 0.34 | 1.51 | 126 |
| stroke 14 | 52 % → 76 % | 86.9 px | 0.34 | 1.48 | 144 |
| stroke 15 | 58 % → 82 % | 85.5 px | 0.34 | 1.41 | 127 |
| stroke 16 | 54 % → 80 % | 89.8 px | 0.34 | 1.47 | 135 |
| stroke 17 | 53 % → 78 % | 77.7 px | 0.34 | 1.45 | 144 |
| stroke 18 | 57 % → 84 % | 100.3 px | 0.34 | 1.47 | 145 |
| stroke 19 | 57 % → 80 % | 86.5 px | 0.34 | 1.41 | 153 |
| stroke 20 | 55 % → 76 % | 95.2 px | 0.34 | 1.40 | 181 |
| stroke 21 | 52 % → 67 % | 83.7 px | 0.34 | 1.30 | 111 |
| stroke 22 | 60 % → 59 % | 94.0 px | 0.34 | 0.98 | 162 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #15 Ultramarine brush script — own sheet
own sheet 600 × 600 · Ink · 10 px · 10.8 s

![Brush Artist · Refs · #15 Ultramarine brush script — own sheet](Brush-Artist-Refs-15-Ultramarine-brush-script-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 69 % → 72 % | 17.0 px | 0.70 | 1.05 | 75 |
| stroke 2 | 70 % → 72 % | 16.6 px | 0.69 | 1.04 | 113 |
| stroke 3 | 70 % → 74 % | 17.4 px | 0.69 | 1.05 | 81 |
| stroke 4 | 71 % → 72 % | 16.3 px | 0.66 | 1.01 | 97 |
| stroke 5 | 66 % → 69 % | 15.7 px | 0.67 | 1.04 | 119 |
| stroke 6 | 67 % → 71 % | 18.5 px | 0.70 | 1.05 | 80 |
| stroke 7 | 69 % → 71 % | 15.9 px | 0.67 | 1.04 | 122 |
| stroke 8 | 69 % → 71 % | 17.6 px | 0.70 | 1.02 | 75 |
| stroke 9 | 67 % → 70 % | 16.5 px | 0.68 | 1.05 | 114 |
| stroke 10 | 65 % → 69 % | 17.1 px | 0.69 | 1.05 | 72 |
| stroke 11 | 72 % → 75 % | 17.5 px | 0.69 | 1.04 | 97 |
| stroke 12 | 68 % → 69 % | 15.8 px | 0.67 | 1.01 | 115 |
| stroke 13 | 66 % → 69 % | 15.7 px | 0.67 | 1.04 | 110 |
| stroke 14 | 67 % → 71 % | 18.2 px | 0.70 | 1.05 | 51 |
| stroke 15 | 69 % → 73 % | 18.8 px | 0.71 | 1.05 | 62 |
| stroke 16 | 68 % → 72 % | 17.4 px | 0.70 | 1.04 | 75 |
| stroke 17 | 68 % → 69 % | 18.1 px | 0.70 | 1.02 | 41 |
| stroke 18 | 68 % → 71 % | 17.2 px | 0.70 | 1.05 | 59 |
| stroke 19 | 66 % → 71 % | 18.9 px | 0.71 | 1.07 | 53 |
| stroke 20 | 68 % → 72 % | 18.8 px | 0.71 | 1.06 | 60 |
| stroke 21 | 70 % → 73 % | 16.0 px | 0.67 | 1.03 | 86 |
| stroke 22 | 77 % → 79 % | 12.6 px | 0.70 | 1.02 | 112 |
| stroke 23 | 67 % → 71 % | 16.9 px | 0.70 | 1.05 | 79 |
| stroke 24 | 66 % → 69 % | 17.9 px | 0.71 | 1.05 | 58 |
| stroke 25 | 69 % → 72 % | 16.5 px | 0.68 | 1.04 | 126 |
| stroke 26 | 70 % → 71 % | 15.8 px | 0.66 | 1.01 | 144 |

## Brush Artist · Refs · #18 Blue oil-stick scribbles — own sheet
own sheet 600 × 600 · Pastel · 10 px · 3.4 s

![Brush Artist · Refs · #18 Blue oil-stick scribbles — own sheet](Brush-Artist-Refs-18-Blue-oil-stick-scribbles-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 18 % → 37 % | 3.8 px | 0.53 | 2.02 | 167 |
| stroke 2 | 16 % → 40 % | 3.6 px | 0.53 | 2.52 | 193 |
| stroke 3 | 18 % → 29 % | 5.8 px | 0.53 | 1.59 | 212 |
| stroke 4 | 17 % → 32 % | 7.8 px | 0.53 | 1.90 | 356 |
| stroke 5 | 32 % → 37 % | 7.8 px | 0.53 | 1.15 | 183 |
| stroke 6 | 30 % → 30 % | 9.2 px | 0.53 | 1.02 | 148 |
| stroke 7 | 28 % → 35 % | 7.5 px | 0.53 | 1.26 | 159 |
| stroke 8 | 33 % → 33 % | 16.3 px | 0.53 | 1.00 | 209 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #20 Orange-red crayon scribble — own sheet
own sheet 600 × 600 · Pastel · 14 px · 3.3 s

![Brush Artist · Refs · #20 Orange-red crayon scribble — own sheet](Brush-Artist-Refs-20-Orange-red-crayon-scribble-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 9 % → 20 % | 5.5 px | 0.53 | 2.30 | 235 |
| stroke 2 | 10 % → 25 % | 6.5 px | 0.53 | 2.49 | 197 |
| stroke 3 | 15 % → 25 % | 8.3 px | 0.53 | 1.61 | 171 |
| stroke 4 | 28 % → 35 % | 8.3 px | 0.53 | 1.25 | 179 |
| stroke 5 | 32 % → 32 % | 7.0 px | 0.53 | 1.00 | 185 |
| stroke 6 | 24 % → 24 % | 16.1 px | 0.53 | 1.00 | 216 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #21 Gritty black contours — own sheet
own sheet 600 × 600 · Gouache · 12 px · 63.2 s

![Brush Artist · Refs · #21 Gritty black contours — own sheet](Brush-Artist-Refs-21-Gritty-black-contours-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 100 % → 98 % | 31.8 px | 0.00 | 0.98 | 915 |
| stroke 2 | 100 % → 98 % | 33.5 px | 0.00 | 0.98 | 1310 |
| stroke 3 | 100 % → 99 % | 32.6 px | 0.00 | 0.99 | 1228 |
| stroke 4 | 100 % → 99 % | 31.8 px | 0.01 | 0.99 | 1143 |
| stroke 5 | 100 % → 98 % | 30.9 px | 0.04 | 0.98 | 1188 |
| stroke 6 | 100 % → 99 % | 34.4 px | 0.06 | 0.99 | 1170 |
| stroke 7 | 100 % → 99 % | 35.3 px | 0.03 | 0.99 | 1140 |
| stroke 8 | 100 % → 98 % | 34.4 px | 0.01 | 0.98 | 1566 |
| stroke 9 | 100 % → 98 % | 30.0 px | 0.00 | 0.98 | 1141 |
| stroke 10 | 100 % → 100 % | 89.0 px | 0.07 | 1.00 | 156 |
| stroke 11 | 100 % → 100 % | 139.6 px | 0.04 | 1.00 | 193 |
| stroke 12 | 100 % → 100 % | 68.3 px | 0.07 | 1.00 | 139 |
| stroke 13 | 100 % → 100 % | 97.7 px | 0.07 | 1.00 | 136 |
| stroke 14 | 100 % → 100 % | 93.8 px | 0.06 | 1.00 | 88 |

## Brush Artist · Refs · #22 Bold black brush poster — own sheet
own sheet 600 × 600 · Ink · 20 px · 5.6 s

![Brush Artist · Refs · #22 Bold black brush poster — own sheet](Brush-Artist-Refs-22-Bold-black-brush-poster-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 34 % → 37 % | 36.3 px | 0.89 | 1.10 | 148 |
| stroke 2 | 55 % → 66 % | 36.9 px | 0.89 | 1.21 | 27 |
| stroke 3 | 49 % → 49 % | 40.5 px | 0.89 | 1.00 | 60 |
| stroke 4 | 36 % → 43 % | 45.3 px | 0.89 | 1.20 | 59 |
| stroke 5 | 35 % → 35 % | 40.5 px | 0.89 | 1.00 | 94 |

## Brush Artist · Refs · #23 Dry white on orange + black line — own sheet
own sheet 600 × 600 · Gouache · 50 px · 67.0 s

![Brush Artist · Refs · #23 Dry white on orange + black line — own sheet](Brush-Artist-Refs-23-Dry-white-on-orange-black-line-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 89 % → 99 % | 61.2 px | 0.00 | 1.12 | 954 |
| stroke 2 | 96 % → 99 % | 94.7 px | 0.00 | 1.04 | 1162 |
| stroke 3 | 92 % → 99 % | 93.5 px | 0.00 | 1.08 | 1235 |
| stroke 4 | 95 % → 99 % | 97.2 px | 0.00 | 1.04 | 1306 |
| stroke 5 | 95 % → 99 % | 93.7 px | 0.00 | 1.04 | 1221 |
| stroke 6 | 95 % → 99 % | 95.7 px | 0.00 | 1.04 | 1562 |
| stroke 7 | 96 % → 99 % | 93.4 px | 0.00 | 1.03 | 1523 |
| stroke 8 | 95 % → 99 % | 92.6 px | 0.00 | 1.05 | 1394 |
| stroke 9 | 100 % → 99 % | 67.9 px | 0.00 | 0.99 | 1000 |
| stroke 10 | 100 % → 100 % | 167.5 px | 0.00 | 1.00 | 169 |
| stroke 11 | 100 % → 100 % | 173.3 px | 0.00 | 1.00 | 189 |
| stroke 12 | 100 % → 100 % | 162.3 px | 0.00 | 1.00 | 167 |
| stroke 13 | 100 % → 100 % | 183.6 px | 0.00 | 1.00 | 164 |
| stroke 14 | 100 % → 100 % | 154.9 px | 0.00 | 1.00 | 175 |
| stroke 15 | 100 % → 100 % | 190.8 px | 0.00 | 1.00 | 181 |
| stroke 16 | 100 % → 100 % | 169.8 px | 0.00 | 1.00 | 183 |
| stroke 17 | 100 % → 100 % | 180.0 px | 0.00 | 1.00 | 181 |
| stroke 18 | 100 % → 100 % | 163.5 px | 0.00 | 1.00 | 176 |
| stroke 19 | 100 % → 100 % | 178.5 px | 0.00 | 1.00 | 172 |
| stroke 20 | 100 % → 100 % | 164.4 px | 0.00 | 1.00 | 165 |
| stroke 21 | 100 % → 100 % | 180.5 px | 0.00 | 1.00 | 179 |
| stroke 22 | 100 % → 100 % | 161.8 px | 0.00 | 1.00 | 179 |
| stroke 23 | 100 % → 100 % | 185.9 px | 0.00 | 1.00 | 190 |
| stroke 24 | 100 % → 100 % | 161.8 px | 0.00 | 1.00 | 180 |
| stroke 25 | 100 % → 100 % | 185.5 px | 0.00 | 1.00 | 187 |
| stroke 26 | 100 % → 100 % | 165.8 px | 0.00 | 1.00 | 189 |
| stroke 27 | 100 % → 100 % | 185.6 px | 0.00 | 1.00 | 171 |

## Brush Artist · Refs · #24 Picasso flat oil — own sheet
own sheet 600 × 600 · Oil · 34 px · 5.7 s

![Brush Artist · Refs · #24 Picasso flat oil — own sheet](Brush-Artist-Refs-24-Picasso-flat-oil-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 35 % → 60 % | 34.6 px | 0.41 | 1.73 | 122 |
| stroke 2 | 40 % → 66 % | 47.1 px | 0.42 | 1.65 | 130 |
| stroke 3 | 56 % → 84 % | 59.7 px | 0.42 | 1.50 | 156 |
| stroke 4 | 56 % → 82 % | 63.9 px | 0.42 | 1.47 | 152 |
| stroke 5 | 55 % → 86 % | 59.9 px | 0.42 | 1.56 | 124 |
| stroke 6 | 56 % → 85 % | 66.3 px | 0.42 | 1.52 | 136 |
| stroke 7 | 60 % → 75 % | 59.1 px | 0.42 | 1.23 | 140 |
| stroke 8 | 56 % → 72 % | 71.1 px | 0.42 | 1.28 | 159 |
| stroke 9 | 42 % → 67 % | 43.8 px | 0.41 | 1.61 | 137 |
| stroke 10 | 46 % → 69 % | 56.7 px | 0.42 | 1.49 | 144 |
| stroke 11 | 59 % → 73 % | 60.6 px | 0.42 | 1.24 | 143 |
| stroke 12 | 59 % → 78 % | 72.3 px | 0.42 | 1.31 | 181 |
| stroke 13 | 47 % → 72 % | 50.2 px | 0.41 | 1.55 | 151 |
| stroke 14 | 48 % → 75 % | 55.1 px | 0.41 | 1.54 | 147 |
| stroke 15 | 53 % → 82 % | 53.5 px | 0.42 | 1.56 | 122 |
| stroke 16 | 49 % → 78 % | 58.9 px | 0.42 | 1.59 | 162 |
| stroke 17 | 60 % → 71 % | 59.6 px | 0.42 | 1.18 | 157 |
| stroke 18 | 56 % → 56 % | 71.0 px | 0.42 | 1.00 | 197 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #25 Yellow heavy flat stroke — own sheet
own sheet 600 × 600 · Heavy acrylic · 110 px · 3.3 s

![Brush Artist · Refs · #25 Yellow heavy flat stroke — own sheet](Brush-Artist-Refs-25-Yellow-heavy-flat-stroke-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 35 % → 35 % | 104.2 px | 0.17 | 0.98 | 773 |

## Brush Artist · Refs · #27 Orange impasto swatch — own sheet
own sheet 600 × 600 · Heavy acrylic · 60 px · 3.8 s

![Brush Artist · Refs · #27 Orange impasto swatch — own sheet](Brush-Artist-Refs-27-Orange-impasto-swatch-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 23 % → 29 % | 61.8 px | 0.37 | 1.29 | 83 |
| stroke 2 | 19 % → 40 % | 62.5 px | 0.37 | 2.07 | 53 |
| stroke 3 | 26 % → 38 % | 94.9 px | 0.37 | 1.48 | 39 |
| stroke 4 | 22 % → 22 % | 62.5 px | 0.36 | 0.96 | 72 |
| stroke 5 | 32 % → 41 % | 62.2 px | 0.36 | 1.28 | 86 |
| stroke 6 | 39 % → 40 % | 112.2 px | 0.36 | 1.02 | 77 |
| stroke 7 | 19 % → 21 % | 63.8 px | 0.36 | 1.11 | 53 |
| stroke 8 | 42 % → 40 % | 143.3 px | 0.36 | 0.97 | 52 |
| stroke 9 | 49 % → 48 % | 97.7 px | 0.37 | 0.97 | 79 |
| stroke 10 | 28 % → 27 % | 87.2 px | 0.36 | 0.96 | 50 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #28 Miles Davis black lines — own sheet
own sheet 600 × 600 · Ink · 22 px · 7.1 s

![Brush Artist · Refs · #28 Miles Davis black lines — own sheet](Brush-Artist-Refs-28-Miles-Davis-black-lines-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 29 % → 36 % | 36.4 px | 0.89 | 1.26 | 187 |
| stroke 2 | 37 % → 57 % | 36.0 px | 0.89 | 1.52 | 143 |
| stroke 3 | 47 % → 48 % | 66.3 px | 0.89 | 1.02 | 130 |
| stroke 4 | 49 % → 58 % | 76.4 px | 0.89 | 1.16 | 240 |
| stroke 5 | 63 % → 64 % | 95.0 px | 0.89 | 1.00 | 159 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #29 Shrigley magenta asterisk — own sheet
own sheet 600 × 600 · Watercolor · 70 px · 7.4 s

![Brush Artist · Refs · #29 Shrigley magenta asterisk — own sheet](Brush-Artist-Refs-29-Shrigley-magenta-asterisk-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 25 % → 44 % | 46.6 px | 0.48 | 1.76 | 203 |
| stroke 2 | 17 % → 17 % | 86.5 px | 0.46 | 1.00 | 235 |
| stroke 3 | 37 % → 43 % | 69.5 px | 0.48 | 1.17 | 329 |
| stroke 4 | 32 % → 33 % | 162.9 px | 0.46 | 1.02 | 199 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #30 Red gouache face patch — own sheet
own sheet 600 × 600 · Gouache · 60 px · 12.4 s

![Brush Artist · Refs · #30 Red gouache face patch — own sheet](Brush-Artist-Refs-30-Red-gouache-face-patch-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 27 % → 51 % | 51.5 px | 0.59 | 1.89 | 199 |
| stroke 2 | 33 % → 57 % | 74.5 px | 0.59 | 1.74 | 183 |
| stroke 3 | 50 % → 77 % | 99.1 px | 0.59 | 1.54 | 210 |
| stroke 4 | 50 % → 77 % | 110.7 px | 0.59 | 1.54 | 207 |
| stroke 5 | 49 % → 78 % | 97.1 px | 0.59 | 1.61 | 190 |
| stroke 6 | 50 % → 80 % | 112.2 px | 0.59 | 1.59 | 246 |
| stroke 7 | 51 % → 78 % | 101.2 px | 0.59 | 1.53 | 240 |
| stroke 8 | 49 % → 76 % | 103.7 px | 0.59 | 1.55 | 292 |
| stroke 9 | 52 % → 80 % | 104.6 px | 0.59 | 1.53 | 218 |
| stroke 10 | 54 % → 76 % | 123.0 px | 0.59 | 1.39 | 265 |
| stroke 11 | 52 % → 74 % | 107.4 px | 0.59 | 1.43 | 204 |
| stroke 12 | 50 % → 74 % | 109.1 px | 0.59 | 1.48 | 177 |
| stroke 13 | 45 % → 72 % | 87.5 px | 0.59 | 1.61 | 171 |
| stroke 14 | 45 % → 63 % | 95.7 px | 0.59 | 1.42 | 185 |
| stroke 15 | 48 % → 58 % | 92.1 px | 0.59 | 1.21 | 328 |
| stroke 16 | 55 % → 54 % | 122.4 px | 0.59 | 0.99 | 178 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #31 Warhol blotted line — own sheet
own sheet 600 × 600 · Ink · 6 px · 5.7 s

![Brush Artist · Refs · #31 Warhol blotted line — own sheet](Brush-Artist-Refs-31-Warhol-blotted-line-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 24 % → 47 % | 15.7 px | 0.83 | 1.93 | 86 |
| stroke 2 | 19 % → 24 % | 15.8 px | 0.83 | 1.27 | 94 |
| stroke 3 | 27 % → 27 % | 24.7 px | 0.82 | 1.02 | 87 |
| stroke 4 | 31 % → 41 % | 27.9 px | 0.83 | 1.32 | 58 |
| stroke 5 | 38 % → 46 % | 34.7 px | 0.83 | 1.22 | 151 |
| stroke 6 | 35 % → 36 % | 25.2 px | 0.82 | 1.03 | 123 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #32 Thick orange swipes — own sheet
own sheet 600 × 600 · Heavy acrylic · 90 px · 59.5 s

![Brush Artist · Refs · #32 Thick orange swipes — own sheet](Brush-Artist-Refs-32-Thick-orange-swipes-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 60 % → 99 % | 60.8 px | 0.00 | 1.65 | 1079 |
| stroke 2 | 75 % → 99 % | 121.8 px | 0.02 | 1.32 | 1481 |
| stroke 3 | 76 % → 99 % | 129.3 px | 0.03 | 1.30 | 1198 |
| stroke 4 | 74 % → 99 % | 128.7 px | 0.04 | 1.33 | 1044 |
| stroke 5 | 75 % → 99 % | 128.6 px | 0.04 | 1.32 | 1007 |
| stroke 6 | 76 % → 99 % | 128.9 px | 0.05 | 1.30 | 1014 |
| stroke 7 | 77 % → 99 % | 129.4 px | 0.03 | 1.29 | 1006 |
| stroke 8 | 79 % → 99 % | 131.4 px | 0.03 | 1.25 | 982 |
| stroke 9 | 100 % → 99 % | 102.4 px | 0.01 | 0.99 | 836 |
| stroke 10 | 100 % → 100 % | 308.3 px | 0.03 | 1.00 | 356 |
| stroke 11 | 100 % → 100 % | 313.1 px | 0.04 | 1.00 | 302 |
| stroke 12 | 100 % → 100 % | 318.4 px | 0.04 | 1.00 | 274 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #33 Red wet-in-wet band — own sheet
own sheet 600 × 600 · Watercolor · 80 px · 7.5 s

![Brush Artist · Refs · #33 Red wet-in-wet band — own sheet](Brush-Artist-Refs-33-Red-wet-in-wet-band-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 45 % → 63 % | 92.3 px | 0.34 | 1.38 | 616 |
| stroke 2 | 50 % → 63 % | 180.2 px | 0.37 | 1.28 | 111 |
| stroke 3 | 61 % → 74 % | 234.0 px | 0.37 | 1.22 | 127 |
| stroke 4 | 62 % → 71 % | 228.8 px | 0.35 | 1.15 | 115 |
| stroke 5 | 57 % → 70 % | 201.2 px | 0.37 | 1.22 | 141 |
| stroke 6 | 61 % → 61 % | 212.9 px | 0.36 | 1.00 | 113 |

## Brush Artist · Refs · #34 Magenta oil patches — own sheet
own sheet 600 × 600 · Oil · 60 px · 4.6 s

![Brush Artist · Refs · #34 Magenta oil patches — own sheet](Brush-Artist-Refs-34-Magenta-oil-patches-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 24 % → 44 % | 61.9 px | 0.62 | 1.86 | 159 |
| stroke 2 | 22 % → 37 % | 62.8 px | 0.62 | 1.68 | 145 |
| stroke 3 | 21 % → 52 % | 62.3 px | 0.62 | 2.42 | 91 |
| stroke 4 | 31 % → 31 % | 97.0 px | 0.62 | 1.00 | 83 |
| stroke 5 | 28 % → 40 % | 61.7 px | 0.62 | 1.46 | 107 |
| stroke 6 | 27 % → 45 % | 80.2 px | 0.62 | 1.65 | 95 |
| stroke 7 | 29 % → 41 % | 82.2 px | 0.62 | 1.42 | 91 |
| stroke 8 | 52 % → 56 % | 134.7 px | 0.62 | 1.07 | 104 |
| stroke 9 | 34 % → 39 % | 87.4 px | 0.62 | 1.13 | 92 |
| stroke 10 | 48 % → 48 % | 152.6 px | 0.62 | 1.00 | 81 |
| stroke 11 | 61 % → 61 % | 185.1 px | 0.62 | 1.00 | 76 |
| stroke 12 | 35 % → 35 % | 104.1 px | 0.62 | 1.00 | 78 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #35 Red band with runs — own sheet
own sheet 600 × 600 · Watercolor · 70 px · 4.1 s

![Brush Artist · Refs · #35 Red band with runs — own sheet](Brush-Artist-Refs-35-Red-band-with-runs-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 41 % → 39 % | 82.9 px | 0.27 | 0.95 | 285 |

## Brush Artist · Refs · #36 Magenta letters flat brush — own sheet
own sheet 600 × 600 · Gouache · 36 px · 10.1 s

![Brush Artist · Refs · #36 Magenta letters flat brush — own sheet](Brush-Artist-Refs-36-Magenta-letters-flat-brush-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 46 % → 46 % | 59.1 px | 0.50 | 1.00 | 35 |
| stroke 2 | 38 % → 48 % | 39.7 px | 0.50 | 1.25 | 38 |
| stroke 3 | 56 % → 63 % | 72.2 px | 0.50 | 1.12 | 68 |
| stroke 4 | 45 % → 53 % | 44.9 px | 0.50 | 1.19 | 119 |
| stroke 5 | 41 % → 52 % | 61.1 px | 0.50 | 1.29 | 64 |
| stroke 6 | 78 % → 76 % | 153.6 px | 0.50 | 0.97 | 14 |
| stroke 7 | 43 % → 50 % | 42.1 px | 0.50 | 1.15 | 113 |
| stroke 8 | 39 % → 59 % | 63.5 px | 0.50 | 1.52 | 69 |
| stroke 9 | 54 % → 53 % | 82.8 px | 0.50 | 0.98 | 26 |
| stroke 10 | 42 % → 61 % | 63.1 px | 0.50 | 1.44 | 74 |
| stroke 11 | 78 % → 77 % | 153.6 px | 0.50 | 0.98 | 15 |
| stroke 12 | 58 % → 68 % | 57.2 px | 0.50 | 1.17 | 99 |
| stroke 13 | 43 % → 50 % | 58.9 px | 0.50 | 1.18 | 33 |
| stroke 14 | 52 % → 73 % | 74.9 px | 0.50 | 1.40 | 31 |
| stroke 15 | 44 % → 52 % | 66.5 px | 0.50 | 1.18 | 70 |
| stroke 16 | 78 % → 76 % | 153.3 px | 0.50 | 0.98 | 18 |
| stroke 17 | 53 % → 61 % | 51.3 px | 0.50 | 1.15 | 117 |
| stroke 18 | 40 % → 47 % | 54.9 px | 0.50 | 1.17 | 31 |
| stroke 19 | 65 % → 63 % | 81.6 px | 0.50 | 0.97 | 30 |
| stroke 20 | 56 % → 54 % | 70.5 px | 0.50 | 0.97 | 32 |
| stroke 21 | 47 % → 46 % | 53.9 px | 0.50 | 0.96 | 81 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #37 Oil still life dabs — own sheet
own sheet 600 × 600 · Oil · 40 px · 3.4 s

![Brush Artist · Refs · #37 Oil still life dabs — own sheet](Brush-Artist-Refs-37-Oil-still-life-dabs-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 20 % → 20 % | 44.0 px | 0.39 | 1.00 | 36 |
| stroke 2 | 18 % → 48 % | 44.4 px | 0.40 | 2.65 | 26 |
| stroke 3 | 23 % → 48 % | 59.8 px | 0.40 | 2.12 | 18 |
| stroke 4 | 22 % → 22 % | 42.7 px | 0.39 | 1.00 | 44 |
| stroke 5 | 17 % → 18 % | 43.2 px | 0.38 | 1.04 | 23 |
| stroke 6 | 37 % → 45 % | 83.3 px | 0.40 | 1.24 | 28 |
| stroke 7 | 16 % → 27 % | 54.8 px | 0.38 | 1.71 | 9 |
| stroke 8 | 14 % → 29 % | 47.9 px | 0.38 | 2.08 | 19 |
| stroke 9 | 23 % → 23 % | 43.9 px | 0.39 | 1.00 | 31 |
| stroke 10 | 31 % → 37 % | 58.3 px | 0.39 | 1.18 | 38 |
| stroke 11 | 39 % → 39 % | 109.7 px | 0.39 | 1.00 | 17 |
| stroke 12 | 31 % → 31 % | 109.5 px | 0.38 | 1.00 | 16 |
| stroke 13 | 17 % → 17 % | 59.0 px | 0.37 | 1.00 | 14 |
| stroke 14 | 35 % → 35 % | 91.9 px | 0.39 | 1.00 | 17 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #38 Sanguine drawing — own sheet
own sheet 600 × 600 · Pastel · 6 px · 2.1 s

![Brush Artist · Refs · #38 Sanguine drawing — own sheet](Brush-Artist-Refs-38-Sanguine-drawing-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 3 % → 14 % | 2.9 px | 0.61 | 4.35 | 4 |
| stroke 2 | 3 % → 7 % | 2.9 px | 0.61 | 2.23 | 4 |
| stroke 3 | 3 % → 9 % | 2.9 px | 0.61 | 2.76 | 8 |
| stroke 4 | 3 % → 19 % | 2.7 px | 0.61 | 6.27 | 3 |
| stroke 5 | 3 % → 8 % | 2.7 px | 0.61 | 2.71 | 8 |
| stroke 6 | 3 % → 20 % | 3.0 px | 0.61 | 6.20 | 5 |
| stroke 7 | 5 % → 15 % | 4.7 px | 0.61 | 2.84 | 6 |
| stroke 8 | 4 % → 15 % | 3.9 px | 0.61 | 3.43 | 3 |
| stroke 9 | 3 % → 7 % | 2.9 px | 0.61 | 2.30 | 7 |
| stroke 10 | 4 % → 17 % | 4.0 px | 0.61 | 3.83 | 4 |
| stroke 11 | 3 % → 5 % | 2.9 px | 0.61 | 1.49 | 3 |
| stroke 12 | 5 % → 16 % | 4.5 px | 0.61 | 3.20 | 7 |
| stroke 13 | 8 % → 18 % | 7.8 px | 0.61 | 2.10 | 5 |
| stroke 14 | 5 % → 15 % | 4.5 px | 0.62 | 2.96 | 4 |
| stroke 15 | 10 % → 18 % | 9.5 px | 0.61 | 1.71 | 8 |
| stroke 16 | 6 % → 16 % | 5.4 px | 0.61 | 2.74 | 3 |
| stroke 17 | 4 % → 9 % | 4.0 px | 0.61 | 2.07 | 4 |
| stroke 18 | 3 % → 5 % | 2.9 px | 0.61 | 1.68 | 3 |
| stroke 19 | 7 % → 17 % | 6.0 px | 0.61 | 2.63 | 10 |
| stroke 20 | 8 % → 15 % | 7.8 px | 0.61 | 1.72 | 7 |
| stroke 21 | 4 % → 4 % | 4.0 px | 0.61 | 1.00 | 4 |
| stroke 22 | 9 % → 14 % | 7.8 px | 0.62 | 1.66 | 3 |
| stroke 23 | 8 % → 12 % | 7.0 px | 0.61 | 1.52 | 7 |
| stroke 24 | 4 % → 7 % | 3.9 px | 0.61 | 1.55 | 3 |
| stroke 25 | 8 % → 15 % | 7.3 px | 0.61 | 1.86 | 4 |
| stroke 26 | 6 % → 8 % | 5.7 px | 0.61 | 1.26 | 3 |
| stroke 27 | 4 % → 4 % | 3.8 px | 0.61 | 1.05 | 5 |
| stroke 28 | 8 % → 12 % | 7.0 px | 0.61 | 1.56 | 4 |
| stroke 29 | 8 % → 17 % | 6.9 px | 0.61 | 2.22 | 7 |
| stroke 30 | 14 % → 18 % | 13.1 px | 0.61 | 1.25 | 4 |
| stroke 31 | 6 % → 7 % | 5.2 px | 0.61 | 1.23 | 5 |
| stroke 32 | 12 % → 13 % | 10.5 px | 0.61 | 1.15 | 3 |
| stroke 33 | 7 % → 8 % | 6.6 px | 0.61 | 1.06 | 5 |
| stroke 34 | 11 % → 14 % | 10.2 px | 0.61 | 1.28 | 4 |
| stroke 35 | 9 % → 15 % | 8.6 px | 0.61 | 1.56 | 4 |
| stroke 36 | 11 % → 13 % | 9.8 px | 0.61 | 1.27 | 3 |
| stroke 37 | 11 % → 17 % | 9.8 px | 0.61 | 1.64 | 4 |
| stroke 38 | 14 % → 21 % | 12.4 px | 0.61 | 1.51 | 4 |
| stroke 39 | 15 % → 18 % | 13.6 px | 0.61 | 1.22 | 7 |
| stroke 40 | 6 % → 7 % | 5.3 px | 0.61 | 1.16 | 4 |
| stroke 41 | 17 % → 17 % | 15.3 px | 0.61 | 1.00 | 7 |
| stroke 42 | 14 % → 16 % | 12.6 px | 0.61 | 1.16 | 4 |
| stroke 43 | 11 % → 13 % | 10.0 px | 0.61 | 1.18 | 4 |
| stroke 44 | 13 % → 16 % | 11.6 px | 0.61 | 1.23 | 3 |
| stroke 45 | 3 % → 3 % | 2.6 px | 0.61 | 1.00 | 6 |
| stroke 46 | 17 % → 17 % | 15.6 px | 0.61 | 1.00 | 3 |
| stroke 47 | 14 % → 14 % | 13.1 px | 0.61 | 1.00 | 7 |
| stroke 48 | 13 % → 14 % | 12.4 px | 0.62 | 1.04 | 4 |
| stroke 49 | 20 % → 20 % | 18.3 px | 0.61 | 1.00 | 7 |
| stroke 50 | 10 % → 10 % | 9.5 px | 0.61 | 1.00 | 7 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #39 Very thick impasto — own sheet
own sheet 600 × 600 · Heavy acrylic · 60 px · 55.2 s

![Brush Artist · Refs · #39 Very thick impasto — own sheet](Brush-Artist-Refs-39-Very-thick-impasto-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 84 % → 99 % | 62.8 px | 0.22 | 1.18 | 853 |
| stroke 2 | 87 % → 99 % | 101.6 px | 0.18 | 1.15 | 975 |
| stroke 3 | 88 % → 99 % | 101.6 px | 0.19 | 1.13 | 1017 |
| stroke 4 | 89 % → 99 % | 103.9 px | 0.29 | 1.12 | 1014 |
| stroke 5 | 88 % → 99 % | 104.4 px | 0.16 | 1.12 | 961 |
| stroke 6 | 89 % → 99 % | 104.7 px | 0.21 | 1.12 | 949 |
| stroke 7 | 89 % → 99 % | 104.7 px | 0.23 | 1.12 | 1137 |
| stroke 8 | 89 % → 99 % | 104.8 px | 0.17 | 1.12 | 1043 |
| stroke 9 | 100 % → 99 % | 75.0 px | 0.16 | 0.99 | 803 |
| stroke 10 | 100 % → 99 % | 156.8 px | 0.18 | 0.99 | 237 |
| stroke 11 | 100 % → 99 % | 162.7 px | 0.19 | 0.99 | 251 |
| stroke 12 | 100 % → 99 % | 180.0 px | 0.19 | 0.99 | 215 |
| stroke 13 | 100 % → 99 % | 153.1 px | 0.18 | 0.99 | 249 |
| stroke 14 | 100 % → 99 % | 168.3 px | 0.16 | 0.99 | 235 |

## Brush Artist · Refs · #40 Watercolour blooms — own sheet
own sheet 600 × 600 · Watercolor · 90 px · 5.4 s

![Brush Artist · Refs · #40 Watercolour blooms — own sheet](Brush-Artist-Refs-40-Watercolour-blooms-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 39 % → 39 % | 94.2 px | 0.26 | 1.00 | 808 |

## Brush Artist · Refs · #41 Coloured pencil hatching — own sheet
own sheet 600 × 600 · Pastel · 4 px · 52.8 s

![Brush Artist · Refs · #41 Coloured pencil hatching — own sheet](Brush-Artist-Refs-41-Coloured-pencil-hatching-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 100 % → 97 % | 16.8 px | 0.00 | 0.97 | 835 |
| stroke 2 | 100 % → 97 % | 15.0 px | 0.01 | 0.97 | 1087 |
| stroke 3 | 100 % → 98 % | 17.6 px | 0.02 | 0.98 | 1074 |
| stroke 4 | 100 % → 98 % | 16.8 px | 0.01 | 0.98 | 957 |
| stroke 5 | 100 % → 97 % | 16.8 px | 0.02 | 0.97 | 983 |
| stroke 6 | 100 % → 98 % | 19.4 px | 0.03 | 0.98 | 966 |
| stroke 7 | 100 % → 98 % | 18.5 px | 0.03 | 0.98 | 902 |
| stroke 8 | 100 % → 97 % | 19.4 px | 0.02 | 0.97 | 990 |
| stroke 9 | 100 % → 97 % | 17.6 px | 0.00 | 0.97 | 802 |
| stroke 10 | 100 % → 100 % | 63.9 px | 0.04 | 1.00 | 3 |
| stroke 11 | 100 % → 100 % | 62.9 px | 0.02 | 1.00 | 3 |
| stroke 12 | 100 % → 100 % | 63.9 px | 0.03 | 1.00 | 3 |
| stroke 13 | 100 % → 100 % | 64.0 px | 0.06 | 1.00 | 3 |
| stroke 14 | 100 % → 100 % | 63.9 px | 0.02 | 1.00 | 3 |
| stroke 15 | 100 % → 100 % | 62.9 px | 0.04 | 1.00 | 3 |
| stroke 16 | 100 % → 100 % | 62.8 px | 0.05 | 1.00 | 3 |
| stroke 17 | 100 % → 100 % | 62.9 px | 0.04 | 1.00 | 3 |
| stroke 18 | 100 % → 100 % | 62.4 px | 0.04 | 1.00 | 3 |
| stroke 19 | 100 % → 100 % | 63.5 px | 0.05 | 1.00 | 3 |
| stroke 20 | 100 % → 100 % | 64.0 px | 0.04 | 1.00 | 3 |
| stroke 21 | 100 % → 100 % | 62.9 px | 0.01 | 1.00 | 3 |
| stroke 22 | 100 % → 100 % | 62.9 px | 0.05 | 1.00 | 3 |
| stroke 23 | 100 % → 100 % | 63.9 px | 0.05 | 1.00 | 3 |
| stroke 24 | 100 % → 100 % | 62.9 px | 0.04 | 1.00 | 3 |
| stroke 25 | 100 % → 100 % | 62.9 px | 0.03 | 1.00 | 3 |
| stroke 26 | 100 % → 100 % | 64.0 px | 0.01 | 1.00 | 3 |
| stroke 27 | 100 % → 100 % | 64.0 px | 0.03 | 1.00 | 3 |
| stroke 28 | 100 % → 100 % | 64.0 px | 0.04 | 1.00 | 3 |
| stroke 29 | 100 % → 100 % | 63.9 px | 0.05 | 1.00 | 3 |
| stroke 30 | 100 % → 100 % | 63.9 px | 0.05 | 1.00 | 3 |
| stroke 31 | 100 % → 100 % | 64.0 px | 0.05 | 1.00 | 3 |
| stroke 32 | 100 % → 100 % | 62.9 px | 0.04 | 1.00 | 3 |
| stroke 33 | 100 % → 100 % | 62.5 px | 0.05 | 1.00 | 3 |
| stroke 34 | 100 % → 100 % | 63.9 px | 0.03 | 1.00 | 3 |
| stroke 35 | 100 % → 100 % | 64.0 px | 0.02 | 1.00 | 3 |
| stroke 36 | 100 % → 100 % | 63.4 px | 0.02 | 1.00 | 3 |
| stroke 37 | 100 % → 100 % | 64.0 px | 0.03 | 1.00 | 3 |
| stroke 38 | 100 % → 100 % | 62.4 px | 0.04 | 1.00 | 3 |
| stroke 39 | 100 % → 100 % | 62.9 px | 0.03 | 1.00 | 3 |
| stroke 40 | 100 % → 100 % | 64.0 px | 0.05 | 1.00 | 3 |
| stroke 41 | 100 % → 100 % | 63.9 px | 0.02 | 1.00 | 3 |
| stroke 42 | 100 % → 100 % | 64.0 px | 0.04 | 1.00 | 3 |
| stroke 43 | 100 % → 100 % | 64.0 px | 0.02 | 1.00 | 3 |
| stroke 44 | 100 % → 100 % | 63.9 px | 0.04 | 1.00 | 3 |
| stroke 45 | 100 % → 100 % | 62.9 px | 0.02 | 1.00 | 3 |
| stroke 46 | 100 % → 100 % | 62.8 px | 0.05 | 1.00 | 3 |
| stroke 47 | 100 % → 100 % | 63.8 px | 0.04 | 1.00 | 3 |
| stroke 48 | 100 % → 100 % | 64.0 px | 0.04 | 1.00 | 3 |
| stroke 49 | 100 % → 100 % | 62.8 px | 0.06 | 1.00 | 3 |
| stroke 50 | 100 % → 100 % | 62.8 px | 0.04 | 1.00 | 3 |
| stroke 51 | 100 % → 100 % | 63.5 px | 0.06 | 1.00 | 3 |
| stroke 52 | 100 % → 100 % | 62.8 px | 0.03 | 1.00 | 3 |
| stroke 53 | 100 % → 100 % | 63.9 px | 0.05 | 1.00 | 3 |
| stroke 54 | 100 % → 100 % | 63.4 px | 0.06 | 1.00 | 3 |
| stroke 55 | 100 % → 100 % | 62.9 px | 0.02 | 1.00 | 3 |
| stroke 56 | 100 % → 100 % | 62.9 px | 0.04 | 1.00 | 3 |
| stroke 57 | 100 % → 100 % | 62.9 px | 0.05 | 1.00 | 3 |
| stroke 58 | 100 % → 100 % | 63.9 px | 0.03 | 1.00 | 3 |
| stroke 59 | 100 % → 100 % | 62.9 px | 0.02 | 1.00 | 3 |
| stroke 60 | 100 % → 100 % | 62.9 px | 0.05 | 1.00 | 3 |
| stroke 61 | 100 % → 100 % | 64.0 px | 0.05 | 1.00 | 3 |
| stroke 62 | 100 % → 100 % | 62.9 px | 0.05 | 1.00 | 3 |
| stroke 63 | 100 % → 100 % | 63.9 px | 0.05 | 1.00 | 3 |
| stroke 64 | 100 % → 100 % | 64.0 px | 0.04 | 1.00 | 3 |
| stroke 65 | 100 % → 100 % | 64.0 px | 0.04 | 1.00 | 3 |
| stroke 66 | 100 % → 100 % | 62.9 px | 0.04 | 1.00 | 3 |
| stroke 67 | 100 % → 100 % | 64.0 px | 0.04 | 1.00 | 3 |
| stroke 68 | 100 % → 100 % | 62.4 px | 0.04 | 1.00 | 3 |
| stroke 69 | 100 % → 100 % | 63.0 px | 0.06 | 1.00 | 3 |
| stroke 70 | 100 % → 100 % | 62.8 px | 0.07 | 1.00 | 3 |
| stroke 71 | 100 % → 100 % | 63.9 px | 0.03 | 1.00 | 3 |
| stroke 72 | 100 % → 100 % | 64.0 px | 0.04 | 1.00 | 3 |
| stroke 73 | 100 % → 100 % | 62.9 px | 0.05 | 1.00 | 3 |
| stroke 74 | 100 % → 100 % | 63.8 px | 0.05 | 1.00 | 3 |
| stroke 75 | 100 % → 100 % | 64.0 px | 0.04 | 1.00 | 3 |
| stroke 76 | 100 % → 100 % | 62.9 px | 0.04 | 1.00 | 3 |
| stroke 77 | 100 % → 100 % | 63.9 px | 0.03 | 1.00 | 5 |
| stroke 78 | 100 % → 100 % | 62.8 px | 0.02 | 1.00 | 3 |
| stroke 79 | 100 % → 100 % | 62.9 px | 0.04 | 1.00 | 3 |
| stroke 80 | 100 % → 100 % | 62.9 px | 0.04 | 1.00 | 3 |
| stroke 81 | 100 % → 100 % | 64.0 px | 0.02 | 1.00 | 3 |
| stroke 82 | 100 % → 100 % | 63.9 px | 0.04 | 1.00 | 3 |
| stroke 83 | 100 % → 100 % | 62.4 px | 0.05 | 1.00 | 3 |
| stroke 84 | 100 % → 100 % | 62.4 px | 0.05 | 1.00 | 3 |
| stroke 85 | 100 % → 100 % | 62.8 px | 0.05 | 1.00 | 3 |
| stroke 86 | 100 % → 100 % | 62.9 px | 0.03 | 1.00 | 3 |
| stroke 87 | 100 % → 100 % | 63.9 px | 0.03 | 1.00 | 3 |
| stroke 88 | 100 % → 100 % | 62.9 px | 0.02 | 1.00 | 3 |
| stroke 89 | 100 % → 100 % | 63.5 px | 0.04 | 1.00 | 3 |

## Brush Artist · Refs · #42 Oil pastel shaggy — own sheet
own sheet 600 × 600 · Pastel · 18 px · 2.6 s

![Brush Artist · Refs · #42 Oil pastel shaggy — own sheet](Brush-Artist-Refs-42-Oil-pastel-shaggy-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 9 % → 20 % | 8.0 px | 0.07 | 2.21 | 8 |
| stroke 2 | 10 % → 26 % | 8.6 px | 0.08 | 2.58 | 8 |
| stroke 3 | 10 % → 33 % | 8.9 px | 0.08 | 3.29 | 12 |
| stroke 4 | 10 % → 21 % | 8.8 px | 0.08 | 2.08 | 6 |
| stroke 5 | 11 % → 21 % | 9.9 px | 0.08 | 1.84 | 12 |
| stroke 6 | 10 % → 31 % | 9.1 px | 0.08 | 3.00 | 6 |
| stroke 7 | 14 % → 40 % | 12.6 px | 0.08 | 2.79 | 6 |
| stroke 8 | 11 % → 44 % | 9.5 px | 0.08 | 3.98 | 10 |
| stroke 9 | 13 % → 22 % | 11.5 px | 0.08 | 1.69 | 7 |
| stroke 10 | 11 % → 19 % | 9.5 px | 0.08 | 1.77 | 9 |
| stroke 11 | 10 % → 28 % | 9.0 px | 0.08 | 2.72 | 8 |
| stroke 12 | 14 % → 19 % | 12.3 px | 0.08 | 1.36 | 12 |
| stroke 13 | 19 % → 30 % | 16.7 px | 0.08 | 1.60 | 6 |
| stroke 14 | 9 % → 20 % | 7.9 px | 0.08 | 2.25 | 12 |
| stroke 15 | 10 % → 36 % | 9.0 px | 0.08 | 3.51 | 6 |
| stroke 16 | 16 % → 34 % | 14.4 px | 0.08 | 2.06 | 12 |
| stroke 17 | 21 % → 39 % | 18.6 px | 0.08 | 1.82 | 6 |
| stroke 18 | 25 % → 35 % | 21.6 px | 0.08 | 1.42 | 8 |
| stroke 19 | 22 % → 40 % | 19.1 px | 0.08 | 1.79 | 10 |
| stroke 20 | 23 % → 42 % | 19.9 px | 0.08 | 1.81 | 11 |
| stroke 21 | 14 % → 20 % | 12.7 px | 0.08 | 1.41 | 8 |
| stroke 22 | 14 % → 16 % | 12.0 px | 0.07 | 1.14 | 6 |
| stroke 23 | 20 % → 27 % | 17.3 px | 0.08 | 1.34 | 11 |
| stroke 24 | 30 % → 35 % | 26.0 px | 0.08 | 1.20 | 6 |
| stroke 25 | 20 % → 33 % | 17.4 px | 0.08 | 1.67 | 9 |
| stroke 26 | 11 % → 22 % | 9.2 px | 0.07 | 2.04 | 9 |
| stroke 27 | 31 % → 36 % | 27.6 px | 0.08 | 1.15 | 6 |
| stroke 28 | 19 % → 30 % | 16.5 px | 0.08 | 1.60 | 9 |
| stroke 29 | 11 % → 29 % | 9.4 px | 0.08 | 2.75 | 9 |
| stroke 30 | 14 % → 38 % | 11.9 px | 0.08 | 2.79 | 7 |
| stroke 31 | 16 % → 16 % | 13.9 px | 0.07 | 1.00 | 6 |
| stroke 32 | 20 % → 33 % | 17.2 px | 0.08 | 1.70 | 11 |
| stroke 33 | 20 % → 21 % | 17.6 px | 0.08 | 1.03 | 11 |
| stroke 34 | 30 % → 36 % | 26.0 px | 0.08 | 1.20 | 6 |
| stroke 35 | 29 % → 37 % | 25.2 px | 0.08 | 1.27 | 11 |
| stroke 36 | 25 % → 27 % | 22.0 px | 0.07 | 1.05 | 12 |
| stroke 37 | 21 % → 21 % | 17.9 px | 0.07 | 1.00 | 10 |
| stroke 38 | 29 % → 34 % | 24.6 px | 0.08 | 1.20 | 11 |
| stroke 39 | 15 % → 25 % | 13.2 px | 0.07 | 1.64 | 11 |
| stroke 40 | 34 % → 41 % | 29.5 px | 0.08 | 1.21 | 9 |
| stroke 41 | 32 % → 34 % | 28.3 px | 0.08 | 1.04 | 12 |
| stroke 42 | 21 % → 30 % | 18.8 px | 0.08 | 1.39 | 7 |
| stroke 43 | 14 % → 14 % | 12.4 px | 0.08 | 1.00 | 11 |
| stroke 44 | 29 % → 39 % | 25.3 px | 0.08 | 1.35 | 12 |
| stroke 45 | 25 % → 25 % | 21.7 px | 0.07 | 1.00 | 13 |
| stroke 46 | 40 % → 45 % | 34.6 px | 0.08 | 1.12 | 9 |
| stroke 47 | 38 % → 45 % | 33.1 px | 0.08 | 1.17 | 9 |
| stroke 48 | 27 % → 30 % | 23.5 px | 0.08 | 1.12 | 8 |
| stroke 49 | 32 % → 34 % | 27.9 px | 0.08 | 1.06 | 10 |
| stroke 50 | 39 % → 42 % | 34.1 px | 0.08 | 1.08 | 10 |
| stroke 51 | 20 % → 20 % | 17.4 px | 0.08 | 1.00 | 6 |
| stroke 52 | 37 % → 37 % | 32.1 px | 0.08 | 1.00 | 12 |
| stroke 53 | 23 % → 23 % | 19.8 px | 0.08 | 1.02 | 8 |
| stroke 54 | 28 % → 31 % | 24.4 px | 0.08 | 1.10 | 11 |
| stroke 55 | 17 % → 17 % | 14.6 px | 0.08 | 1.00 | 6 |
| stroke 56 | 21 % → 21 % | 18.2 px | 0.08 | 1.00 | 12 |
| stroke 57 | 36 % → 36 % | 31.3 px | 0.08 | 1.00 | 9 |
| stroke 58 | 29 % → 29 % | 25.3 px | 0.08 | 1.00 | 7 |
| stroke 59 | 50 % → 50 % | 43.8 px | 0.08 | 1.00 | 12 |
| stroke 60 | 19 % → 19 % | 16.5 px | 0.08 | 1.00 | 20 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #43 Dragged black ink blocks — own sheet
own sheet 600 × 600 · Gouache · 70 px · 52.0 s

![Brush Artist · Refs · #43 Dragged black ink blocks — own sheet](Brush-Artist-Refs-43-Dragged-black-ink-blocks-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 74 % → 99 % | 63.1 px | 0.27 | 1.33 | 904 |
| stroke 2 | 81 % → 99 % | 111.0 px | 0.20 | 1.23 | 1002 |
| stroke 3 | 84 % → 99 % | 111.0 px | 0.18 | 1.18 | 1003 |
| stroke 4 | 83 % → 99 % | 111.9 px | 0.28 | 1.19 | 1035 |
| stroke 5 | 82 % → 99 % | 110.3 px | 0.19 | 1.21 | 998 |
| stroke 6 | 81 % → 99 % | 110.6 px | 0.27 | 1.22 | 981 |
| stroke 7 | 84 % → 99 % | 110.0 px | 0.20 | 1.18 | 1011 |
| stroke 8 | 81 % → 99 % | 110.7 px | 0.18 | 1.22 | 990 |
| stroke 9 | 100 % → 99 % | 86.5 px | 0.28 | 0.99 | 846 |
| stroke 10 | 100 % → 99 % | 145.3 px | 0.22 | 0.99 | 321 |
| stroke 11 | 100 % → 99 % | 189.3 px | 0.17 | 0.99 | 340 |
| stroke 12 | 100 % → 99 % | 188.7 px | 0.19 | 0.99 | 320 |
| stroke 13 | 100 % → 99 % | 182.4 px | 0.18 | 0.99 | 331 |
| stroke 14 | 100 % → 99 % | 152.9 px | 0.21 | 0.99 | 342 |

## Brush Artist · Refs · #44 Blue looping ribbon — own sheet
own sheet 600 × 600 · Oil · 80 px · 5.6 s

![Brush Artist · Refs · #44 Blue looping ribbon — own sheet](Brush-Artist-Refs-44-Blue-looping-ribbon-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 48 % → 48 % | 42.2 px | 0.73 | 1.00 | 2564 |

## Brush Artist · Refs · #45 Soft pastel pepper — own sheet
own sheet 600 × 600 · Pastel · 40 px · 3.0 s

![Brush Artist · Refs · #45 Soft pastel pepper — own sheet](Brush-Artist-Refs-45-Soft-pastel-pepper-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 15 % → 33 % | 11.3 px | 0.54 | 2.20 | 300 |
| stroke 2 | 25 % → 37 % | 20.6 px | 0.54 | 1.47 | 293 |
| stroke 3 | 34 % → 42 % | 13.8 px | 0.54 | 1.25 | 253 |
| stroke 4 | 32 % → 36 % | 27.8 px | 0.54 | 1.13 | 297 |
| stroke 5 | 37 % → 37 % | 13.9 px | 0.54 | 1.00 | 181 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #46 Red-brown ink lips — own sheet
own sheet 600 × 600 · Watercolor · 70 px · 4.6 s

![Brush Artist · Refs · #46 Red-brown ink lips — own sheet](Brush-Artist-Refs-46-Red-brown-ink-lips-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 30 % → 43 % | 78.1 px | 0.54 | 1.42 | 195 |
| stroke 2 | 45 % → 45 % | 119.4 px | 0.53 | 1.00 | 171 |

## Brush Artist · Refs · #47 Pink knife slabs — own sheet
own sheet 600 × 600 · Heavy acrylic · 90 px · 4.2 s

![Brush Artist · Refs · #47 Pink knife slabs — own sheet](Brush-Artist-Refs-47-Pink-knife-slabs-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 28 % → 34 % | 83.2 px | 0.18 | 1.18 | 274 |
| stroke 2 | 36 % → 41 % | 106.4 px | 0.18 | 1.13 | 275 |
| stroke 3 | 36 % → 41 % | 106.3 px | 0.18 | 1.14 | 276 |
| stroke 4 | 37 % → 36 % | 106.4 px | 0.18 | 0.97 | 267 |

## Brush Artist · Refs · #48 Black bands with drips — own sheet
own sheet 600 × 600 · Gouache · 70 px · 44.3 s

![Brush Artist · Refs · #48 Black bands with drips — own sheet](Brush-Artist-Refs-48-Black-bands-with-drips-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 75 % → 99 % | 62.0 px | 0.10 | 1.32 | 848 |
| stroke 2 | 81 % → 99 % | 110.7 px | 0.12 | 1.22 | 980 |
| stroke 3 | 82 % → 99 % | 111.0 px | 0.18 | 1.21 | 978 |
| stroke 4 | 84 % → 99 % | 113.5 px | 0.12 | 1.18 | 981 |
| stroke 5 | 81 % → 99 % | 111.0 px | 0.17 | 1.22 | 1010 |
| stroke 6 | 80 % → 99 % | 110.7 px | 0.12 | 1.23 | 989 |
| stroke 7 | 81 % → 99 % | 110.4 px | 0.13 | 1.21 | 963 |
| stroke 8 | 83 % → 99 % | 112.5 px | 0.12 | 1.18 | 958 |
| stroke 9 | 100 % → 99 % | 82.9 px | 0.01 | 0.99 | 703 |
| stroke 10 | 100 % → 99 % | 177.4 px | 0.11 | 0.99 | 313 |
| stroke 11 | 100 % → 99 % | 166.7 px | 0.12 | 0.99 | 310 |
| stroke 12 | 100 % → 99 % | 175.1 px | 0.11 | 0.99 | 320 |
| stroke 13 | 100 % → 99 % | 174.8 px | 0.11 | 0.99 | 314 |

## Brush Artist · Refs · #49 Magenta letters round brush — own sheet
own sheet 600 × 600 · Ink · 30 px · 9.0 s

![Brush Artist · Refs · #49 Magenta letters round brush — own sheet](Brush-Artist-Refs-49-Magenta-letters-round-brush-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 61 % → 65 % | 64.3 px | 0.52 | 1.06 | 26 |
| stroke 2 | 59 % → 63 % | 52.0 px | 0.53 | 1.07 | 36 |
| stroke 3 | 71 % → 80 % | 74.2 px | 0.53 | 1.13 | 27 |
| stroke 4 | 54 % → 64 % | 48.0 px | 0.52 | 1.18 | 106 |
| stroke 5 | 48 % → 65 % | 63.0 px | 0.52 | 1.35 | 68 |
| stroke 6 | 93 % → 94 % | 141.0 px | 0.53 | 1.01 | 17 |
| stroke 7 | 61 % → 70 % | 51.9 px | 0.52 | 1.14 | 111 |
| stroke 8 | 44 % → 72 % | 63.4 px | 0.53 | 1.61 | 65 |
| stroke 9 | 71 % → 71 % | 86.0 px | 0.53 | 1.00 | 25 |
| stroke 10 | 51 % → 72 % | 66.5 px | 0.52 | 1.42 | 73 |
| stroke 11 | 93 % → 94 % | 140.9 px | 0.53 | 1.01 | 19 |
| stroke 12 | 71 % → 83 % | 60.6 px | 0.52 | 1.18 | 112 |
| stroke 13 | 61 % → 65 % | 67.4 px | 0.53 | 1.05 | 33 |
| stroke 14 | 69 % → 92 % | 78.6 px | 0.53 | 1.33 | 35 |
| stroke 15 | 52 % → 63 % | 68.8 px | 0.52 | 1.20 | 66 |
| stroke 16 | 93 % → 93 % | 140.9 px | 0.53 | 1.00 | 20 |
| stroke 17 | 68 % → 76 % | 58.1 px | 0.52 | 1.12 | 110 |
| stroke 18 | 59 % → 62 % | 64.6 px | 0.52 | 1.05 | 35 |
| stroke 19 | 81 % → 80 % | 82.3 px | 0.53 | 0.99 | 31 |
| stroke 20 | 71 % → 70 % | 72.0 px | 0.52 | 1.00 | 26 |
| stroke 21 | 59 % → 59 % | 61.0 px | 0.52 | 1.00 | 86 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #50 Thick swipes on photo — own sheet
own sheet 600 × 600 · Heavy acrylic · 40 px · 2.8 s

![Brush Artist · Refs · #50 Thick swipes on photo — own sheet](Brush-Artist-Refs-50-Thick-swipes-on-photo-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 24 % → 27 % | 42.6 px | 0.23 | 1.12 | 31 |
| stroke 2 | 21 % → 28 % | 42.4 px | 0.23 | 1.33 | 28 |
| stroke 3 | 26 % → 24 % | 41.8 px | 0.23 | 0.95 | 39 |
| stroke 4 | 26 % → 24 % | 42.6 px | 0.23 | 0.94 | 34 |
| stroke 5 | 24 % → 22 % | 41.8 px | 0.23 | 0.95 | 38 |
| stroke 6 | 21 % → 19 % | 42.9 px | 0.22 | 0.94 | 24 |
| stroke 7 | 36 % → 37 % | 59.4 px | 0.23 | 1.02 | 35 |
| stroke 8 | 34 % → 33 % | 66.7 px | 0.23 | 0.97 | 37 |
| stroke 9 | 25 % → 23 % | 42.0 px | 0.23 | 0.95 | 31 |
| stroke 10 | 28 % → 27 % | 42.2 px | 0.22 | 0.95 | 42 |
| stroke 11 | 23 % → 21 % | 42.6 px | 0.23 | 0.95 | 31 |
| stroke 12 | 24 % → 23 % | 53.2 px | 0.22 | 0.95 | 17 |

## Brush Artist · Ink — dry brush — own sheet
own sheet 600 × 600 · Gouache · 30 px · 2.9 s

![Brush Artist · Ink — dry brush — own sheet](Brush-Artist-Ink-dry-brush-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| ear | 17 % → 4 % | 16.7 px | 0.77 | 0.24 | 475 |
| drag0 | 20 % → 24 % | 25.0 px | 0.77 | 1.22 | 120 |
| drag1 | 25 % → 25 % | 34.2 px | 0.77 | 1.02 | 105 |
| drag2 | 28 % → 25 % | 42.1 px | 0.77 | 0.92 | 89 |
| drag3 | 30 % → 26 % | 50.2 px | 0.77 | 0.87 | 70 |

## Brush Artist · Watercolour — blue — own sheet
own sheet 600 × 600 · Watercolor · 40 px · 8.8 s

![Brush Artist · Watercolour — blue — own sheet](Brush-Artist-Watercolour-blue-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| s0 | 14 % → 28 % | 28.4 px | 0.23 | 2.04 | 41 |
| s1 | 8 % → 36 % | 9.9 px | 0.21 | 4.46 | 44 |
| s2 | 12 % → 21 % | 28.5 px | 0.30 | 1.74 | 37 |
| s3 | 11 % → 18 % | 20.3 px | 0.23 | 1.68 | 45 |
| s4 | 17 % → 34 % | 36.6 px | 0.22 | 1.96 | 51 |
| s5 | 25 % → 33 % | 34.0 px | 0.27 | 1.32 | 53 |
| s6 | 25 % → 30 % | 39.5 px | 0.23 | 1.23 | 57 |
| s7 | 27 % → 34 % | 18.5 px | 0.17 | 1.28 | 36 |
| s8 | 21 % → 25 % | 44.1 px | 0.26 | 1.19 | 40 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Charcoal — stick — own sheet
own sheet 600 × 600 · Charcoal · 28 px · 1.0 s

![Brush Artist · Charcoal — stick — own sheet](Brush-Artist-Charcoal-stick-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| finger0 | 16 % → 21 % | 15.5 px | 0.85 | 1.33 | 33 |
| tip0 | 15 % → 22 % | 18.4 px | 0.85 | 1.47 | 5 |
| finger1 | 16 % → 26 % | 15.7 px | 0.85 | 1.64 | 35 |
| tip1 | 20 % → 27 % | 24.8 px | 0.85 | 1.34 | 10 |
| finger2 | 16 % → 24 % | 16.0 px | 0.85 | 1.45 | 27 |
| tip2 | 20 % → 27 % | 24.1 px | 0.85 | 1.34 | 5 |
| finger3 | 16 % → 18 % | 16.1 px | 0.85 | 1.12 | 21 |
| tip3 | 20 % → 20 % | 24.3 px | 0.85 | 1.00 | 17 |
| cig0 | 38 % → 50 % | 35.5 px | 0.85 | 1.32 | 8 |
| cig1 | 42 % → 55 % | 39.5 px | 0.85 | 1.30 | 6 |
| cig2 | 47 % → 60 % | 44.1 px | 0.85 | 1.27 | 12 |
| cig3 | 51 % → 60 % | 47.1 px | 0.85 | 1.20 | 9 |
| cig4 | 50 % → 55 % | 46.8 px | 0.85 | 1.10 | 12 |
| cig5 | 51 % → 51 % | 47.1 px | 0.85 | 1.00 | 7 |

Numbers say: wet paint spreads well beyond the stroke.

