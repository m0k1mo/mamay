![All brushes](contact.png)

# Brush Lab — 158 brushes · 3 Nov 2026 at 19:23

Every sheet: 1500 × 600, ten strokes in a 5 × 2 grid — 1. light line · 2. heavy line · 3. pressure swell · 4. fast wave · 5. slow wave · 6. spiral · 7. loop · 8. tilted · 9. over the wet one · 10. long, no reload (cell 8 holds «tilted» and «over the wet one» crossed). The CPU reference of Mamay's paint engine; the wet layer settles 20 s at the end.

Columns: **covered** = share of the cell with paint right after the stroke → after settling; **width** = painted area of the stroke ÷ its length (px); **dark** = mean darkness of the painted pixels above the paper's own grain (0 = paper, 1 = black); **spread** = how far wet paint went beyond the stroke (1.0 = stayed); **ms** = the stroke on the CPU; long stroke: paint in each quarter of its length (it should run out: wet → streaks → dry tail).

## Ink Line
Ink · 12 px · 24.7 s

![Ink Line](Ink-Line.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 1 % → 4 % | 4.3 px | 0.55 | 2.44 | 26 |
| heavy line | 5 % → 6 % | 15.7 px | 0.68 | 1.13 | 64 |
| pressure swell | 3 % → 4 % | 11.3 px | 0.64 | 1.40 | 48 |
| fast wave | 10 % → 11 % | 11.2 px | 0.59 | 1.11 | 137 |
| slow wave | 8 % → 10 % | 9.6 px | 0.57 | 1.16 | 112 |
| spiral | 14 % → 15 % | 8.9 px | 0.50 | 1.07 | 154 |
| loop | 8 % → 9 % | 10.6 px | 0.61 | 1.16 | 95 |
| tilted | 5 % → 5 % | 14.4 px | 0.65 | 1.05 | 46 |
| over the wet one | 10 % → 11 % | 12.5 px | 0.65 | 1.15 | 51 |
| long, no reload | 18 % → 17 % | 8.1 px | 0.47 | 0.96 | 271 | quarters: 0.22 → 0.09 → 0.04 → 0.02

Numbers say: light vs heavy: width 4.3 → 15.7 px, dark 0.55 → 0.68; wet paint spreads well beyond the stroke.

## Dense Ink
Ink · 14 px · 25.6 s

![Dense Ink](Dense-Ink.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 5 % → 7 % | 15.2 px | 0.72 | 1.26 | 41 |
| heavy line | 7 % → 7 % | 19.1 px | 0.73 | 1.09 | 76 |
| pressure swell | 5 % → 6 % | 17.9 px | 0.72 | 1.17 | 54 |
| fast wave | 13 % → 13 % | 15.3 px | 0.69 | 1.01 | 170 |
| slow wave | 12 % → 12 % | 13.6 px | 0.67 | 1.04 | 153 |
| spiral | 18 % → 15 % | 12.2 px | 0.65 | 0.80 | 266 |
| loop | 11 % → 12 % | 14.8 px | 0.69 | 1.08 | 120 |
| tilted | 5 % → 6 % | 14.6 px | 0.72 | 1.07 | 51 |
| over the wet one | 12 % → 13 % | 17.7 px | 0.72 | 1.11 | 57 |
| long, no reload | 23 % → 15 % | 10.1 px | 0.64 | 0.66 | 306 | quarters: 0.30 → 0.12 → 0.04 → 0.02

Numbers say: light vs heavy: width 15.2 → 19.1 px, dark 0.72 → 0.73.

## Transparent Wash
Watercolor · 22 px · 27.3 s

![Transparent Wash](Transparent-Wash.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 2 % → 5 % | 6.9 px | 0.27 | 2.25 | 35 |
| heavy line | 7 % → 9 % | 20.4 px | 0.27 | 1.22 | 67 |
| pressure swell | 4 % → 6 % | 15.2 px | 0.28 | 1.54 | 43 |
| fast wave | 14 % → 16 % | 16.1 px | 0.20 | 1.17 | 166 |
| slow wave | 12 % → 15 % | 13.7 px | 0.21 | 1.28 | 172 |
| spiral | 18 % → 22 % | 11.9 px | 0.16 | 1.23 | 183 |
| loop | 11 % → 13 % | 14.5 px | 0.22 | 1.20 | 103 |
| tilted | 8 % → 8 % | 21.1 px | 0.24 | 1.06 | 56 |
| over the wet one | 13 % → 16 % | 16.4 px | 0.24 | 1.18 | 52 |
| long, no reload | 26 % → 32 % | 11.6 px | 0.13 | 1.22 | 257 | quarters: 0.11 → 0.04 → 0.02 → 0.01

Numbers say: light vs heavy: width 6.9 → 20.4 px, dark 0.27 → 0.27; wet paint spreads well beyond the stroke.

## Dry Brush
Gouache · 24 px · 20.5 s

![Dry Brush](Dry-Brush.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 5 % → 0 % | 14.0 px | 0.65 | 0.09 | 60 |
| heavy line | 6 % → 0 % | 18.6 px | 0.65 | 0.02 | 88 |
| pressure swell | 5 % → 0 % | 18.2 px | 0.65 | 0.08 | 71 |
| fast wave | 6 % → 1 % | 7.3 px | 0.65 | 0.08 | 166 |
| slow wave | 7 % → 0 % | 8.1 px | 0.65 | 0.06 | 221 |
| spiral | 7 % → 0 % | 4.6 px | 0.65 | 0.07 | 249 |
| loop | 10 % → 0 % | 12.4 px | 0.65 | 0.04 | 128 |
| tilted | 4 % → 3 % | 10.6 px | 0.65 | 0.88 | 68 |
| over the wet one | 9 % → 1 % | 14.5 px | 0.65 | 0.12 | 55 |
| long, no reload | 6 % → 1 % | 2.9 px | 0.65 | 0.14 | 313 | quarters: 0.12 → 0.00 → 0.00 → 0.00

Numbers say: light vs heavy: width 14.0 → 18.6 px, dark 0.65 → 0.65.

## Wax Crayon
Wax · 8 px · 9.9 s

![Wax Crayon](Wax-Crayon.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 1 % → 1 % | 2.5 px | 0.71 | 1.00 | 18 |
| heavy line | 1 % → 1 % | 3.9 px | 0.69 | 1.00 | 20 |
| pressure swell | 1 % → 1 % | 3.3 px | 0.70 | 1.00 | 12 |
| fast wave | 3 % → 3 % | 3.5 px | 0.69 | 1.00 | 92 |
| slow wave | 3 % → 3 % | 3.4 px | 0.70 | 1.00 | 87 |
| spiral | 5 % → 5 % | 3.3 px | 0.70 | 1.00 | 157 |
| loop | 3 % → 3 % | 3.3 px | 0.70 | 1.00 | 69 |
| tilted | 2 % → 2 % | 5.6 px | 0.68 | 1.00 | 23 |
| over the wet one | 3 % → 3 % | 3.6 px | 0.68 | 1.00 | 34 |
| long, no reload | 7 % → 7 % | 3.3 px | 0.70 | 1.00 | 139 | quarters: 0.06 → 0.06 → 0.06 → 0.06

Numbers say: light vs heavy: width 2.5 → 3.9 px, dark 0.71 → 0.69; the long stroke does not run out of paint.

## Oil Pastel
Wax · 12 px · 9.9 s

![Oil Pastel](Oil-Pastel.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 1 % → 1 % | 4.0 px | 0.68 | 1.00 | 20 |
| heavy line | 2 % → 2 % | 6.5 px | 0.68 | 1.00 | 45 |
| pressure swell | 2 % → 2 % | 5.7 px | 0.69 | 1.00 | 18 |
| fast wave | 5 % → 5 % | 5.7 px | 0.68 | 1.00 | 102 |
| slow wave | 5 % → 5 % | 5.5 px | 0.68 | 1.00 | 75 |
| spiral | 8 % → 8 % | 5.5 px | 0.68 | 1.00 | 167 |
| loop | 4 % → 4 % | 5.6 px | 0.68 | 1.00 | 89 |
| tilted | 2 % → 2 % | 6.8 px | 0.68 | 1.00 | 41 |
| over the wet one | 5 % → 5 % | 5.8 px | 0.68 | 1.00 | 17 |
| long, no reload | 13 % → 13 % | 5.6 px | 0.68 | 1.00 | 193 | quarters: 0.10 → 0.09 → 0.10 → 0.10

Numbers say: light vs heavy: width 4.0 → 6.5 px, dark 0.68 → 0.68; the long stroke does not run out of paint.

## Charcoal
Charcoal · 5 px · 9.7 s

![Charcoal](Charcoal.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 1 % → 1 % | 2.0 px | 0.74 | 1.00 | 15 |
| heavy line | 1 % → 1 % | 3.0 px | 0.74 | 1.00 | 13 |
| pressure swell | 1 % → 1 % | 2.7 px | 0.74 | 1.00 | 9 |
| fast wave | 2 % → 2 % | 2.7 px | 0.73 | 1.00 | 61 |
| slow wave | 2 % → 2 % | 2.6 px | 0.74 | 1.00 | 54 |
| spiral | 4 % → 4 % | 2.5 px | 0.74 | 1.00 | 154 |
| loop | 2 % → 2 % | 2.6 px | 0.74 | 1.00 | 73 |
| tilted | 2 % → 2 % | 4.3 px | 0.72 | 1.00 | 15 |
| over the wet one | 2 % → 2 % | 2.4 px | 0.72 | 1.00 | 19 |
| long, no reload | 6 % → 6 % | 2.7 px | 0.73 | 1.00 | 116 | quarters: 0.05 → 0.05 → 0.05 → 0.05

Numbers say: light vs heavy: width 2.0 → 3.0 px, dark 0.74 → 0.74; the long stroke does not run out of paint.

## Impasto
Heavy acrylic · 22 px · 14.8 s

![Impasto](Impasto.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 8 % → 8 % | 24.1 px | 0.71 | 0.93 | 48 |
| heavy line | 10 % → 9 % | 28.8 px | 0.70 | 0.94 | 112 |
| pressure swell | 7 % → 7 % | 28.1 px | 0.72 | 0.94 | 56 |
| fast wave | 20 % → 13 % | 23.5 px | 0.71 | 0.64 | 189 |
| slow wave | 21 % → 14 % | 24.5 px | 0.71 | 0.66 | 280 |
| spiral | 30 % → 14 % | 20.0 px | 0.71 | 0.46 | 265 |
| loop | 18 % → 14 % | 23.9 px | 0.71 | 0.77 | 140 |
| tilted | 8 % → 8 % | 21.8 px | 0.70 | 1.00 | 89 |
| over the wet one | 17 % → 15 % | 25.4 px | 0.70 | 0.91 | 67 |
| long, no reload | 34 % → 14 % | 15.2 px | 0.71 | 0.41 | 377 | quarters: 0.38 → 0.21 → 0.10 → 0.03

Numbers say: light vs heavy: width 24.1 → 28.8 px, dark 0.71 → 0.70.

## Oil Round
Oil · 18 px · 17.5 s

![Oil Round](Oil-Round.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 2 % → 2 % | 7.2 px | 0.75 | 1.00 | 46 |
| heavy line | 7 % → 7 % | 19.3 px | 0.73 | 1.00 | 73 |
| pressure swell | 4 % → 4 % | 13.7 px | 0.72 | 1.00 | 60 |
| fast wave | 11 % → 11 % | 12.7 px | 0.65 | 1.00 | 178 |
| slow wave | 8 % → 8 % | 9.0 px | 0.57 | 1.00 | 175 |
| spiral | 10 % → 10 % | 6.6 px | 0.50 | 1.00 | 220 |
| loop | 5 % → 5 % | 7.1 px | 0.45 | 1.00 | 118 |
| tilted | 4 % → 4 % | 10.1 px | 0.52 | 1.00 | 68 |
| over the wet one | 6 % → 6 % | 7.4 px | 0.52 | 1.00 | 53 |
| long, no reload | 15 % → 15 % | 6.8 px | 0.42 | 1.00 | 359 | quarters: 0.08 → 0.08 → 0.07 → 0.06

Numbers say: light vs heavy: width 7.2 → 19.3 px, dark 0.75 → 0.73.

## Palette Knife
Oil · 20 px · 17.0 s

![Palette Knife](Palette-Knife.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 8 % → 8 % | 21.9 px | 0.67 | 1.00 | 21 |
| heavy line | 8 % → 8 % | 22.5 px | 0.73 | 1.00 | 9 |
| pressure swell | 6 % → 6 % | 22.4 px | 0.74 | 1.00 | 16 |
| fast wave | 17 % → 17 % | 19.3 px | 0.49 | 1.00 | 41 |
| slow wave | 17 % → 17 % | 19.9 px | 0.43 | 1.00 | 75 |
| spiral | 18 % → 18 % | 11.7 px | 0.45 | 1.00 | 51 |
| loop | 16 % → 16 % | 21.0 px | 0.58 | 1.00 | 33 |
| tilted | 5 % → 5 % | 15.0 px | 0.72 | 1.00 | 17 |
| over the wet one | 13 % → 13 % | 21.0 px | 0.72 | 1.00 | 18 |
| long, no reload | 17 % → 17 % | 7.5 px | 0.47 | 1.00 | 76 | quarters: 0.29 → 0.05 → 0.00 → 0.00

Numbers say: light vs heavy: width 21.9 → 22.5 px, dark 0.67 → 0.73; pressure barely changes the width.

## Water
Watercolor · 20 px · 36.7 s · over bands of wet oil paint and oil pastel in turn (it works on paint already there: look at what it does to the bands; covered counts the bands too)

![Water](Water.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 25 % → 27 % | 73.8 px | 0.80 | 1.06 | 23 |
| heavy line | 24 % → 25 % | 69.8 px | 0.81 | 1.04 | 59 |
| pressure swell | 24 % → 25 % | 89.6 px | 0.81 | 1.03 | 36 |
| fast wave | 24 % → 26 % | 27.7 px | 0.81 | 1.07 | 147 |
| slow wave | 24 % → 25 % | 27.7 px | 0.81 | 1.06 | 209 |
| spiral | 24 % → 26 % | 15.9 px | 0.81 | 1.07 | 184 |
| loop | 24 % → 25 % | 31.1 px | 0.81 | 1.03 | 170 |
| tilted | 24 % → 24 % | 67.0 px | 0.81 | 1.00 | 72 |
| over the wet one | 24 % → 25 % | 0.0 px | 0.81 | 1.06 | 46 |
| long, no reload | 24 % → 26 % | 10.7 px | 0.81 | 1.08 | 233 | quarters: 0.21 → 0.27 → 0.18 → 0.27

Numbers say: light vs heavy: width 73.8 → 69.8 px, dark 0.80 → 0.81; pressure barely changes the width; the long stroke does not run out of paint.

## Blender
Pastel · 16 px · 22.5 s · over bands of wet oil paint and oil pastel in turn (it works on paint already there: look at what it does to the bands; covered counts the bands too)

![Blender](Blender.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 24 % → 24 % | 70.7 px | 0.81 | 1.00 | 26 |
| heavy line | 25 % → 25 % | 72.1 px | 0.80 | 1.00 | 38 |
| pressure swell | 24 % → 24 % | 91.3 px | 0.81 | 1.00 | 27 |
| fast wave | 26 % → 26 % | 30.0 px | 0.79 | 1.00 | 90 |
| slow wave | 26 % → 26 % | 29.9 px | 0.80 | 1.00 | 147 |
| spiral | 28 % → 28 % | 18.7 px | 0.77 | 1.00 | 124 |
| loop | 25 % → 25 % | 32.9 px | 0.80 | 1.00 | 82 |
| tilted | 25 % → 25 % | 70.1 px | 0.79 | 1.00 | 50 |
| over the wet one | 26 % → 26 % | 1.8 px | 0.79 | 1.00 | 46 |
| long, no reload | 30 % → 30 % | 13.7 px | 0.76 | 1.00 | 184 | quarters: 0.20 → 0.28 → 0.23 → 0.30

Numbers say: light vs heavy: width 70.7 → 72.1 px, dark 0.81 → 0.80; pressure barely changes the width; the long stroke does not run out of paint.

## Eraser
Eraser · 16 px · 22.2 s · over bands of wet oil paint and oil pastel in turn (it works on paint already there: look at what it does to the bands; covered counts the bands too)

![Eraser](Eraser.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 24 % → 24 % | 69.5 px | 0.82 | 1.00 | 19 |
| heavy line | 23 % → 23 % | 67.9 px | 0.82 | 1.00 | 46 |
| pressure swell | 23 % → 23 % | 87.3 px | 0.82 | 1.00 | 26 |
| fast wave | 22 % → 22 % | 25.7 px | 0.82 | 1.00 | 85 |
| slow wave | 22 % → 22 % | 25.7 px | 0.82 | 1.00 | 119 |
| spiral | 22 % → 22 % | 14.4 px | 0.82 | 1.00 | 131 |
| loop | 22 % → 22 % | 28.6 px | 0.82 | 1.00 | 112 |
| tilted | 23 % → 23 % | 65.1 px | 0.82 | 1.00 | 50 |
| over the wet one | 23 % → 23 % | 0.0 px | 0.82 | 1.00 | 56 |
| long, no reload | 20 % → 20 % | 8.9 px | 0.82 | 1.00 | 183 | quarters: 0.15 → 0.20 → 0.15 → 0.20

Numbers say: light vs heavy: width 69.5 → 67.9 px, dark 0.82 → 0.82; pressure barely changes the width; the long stroke does not run out of paint.

## Fan
Gouache · 30 px · 30.7 s

![Fan](Fan.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 9 % → 3 % | 25.7 px | 0.63 | 0.37 | 42 |
| heavy line | 11 % → 4 % | 31.0 px | 0.63 | 0.39 | 65 |
| pressure swell | 8 % → 5 % | 31.7 px | 0.63 | 0.55 | 57 |
| fast wave | 18 % → 5 % | 20.3 px | 0.63 | 0.26 | 115 |
| slow wave | 18 % → 5 % | 21.1 px | 0.63 | 0.25 | 182 |
| spiral | 24 % → 5 % | 15.8 px | 0.63 | 0.20 | 180 |
| loop | 17 % → 5 % | 22.7 px | 0.63 | 0.29 | 102 |
| tilted | 5 % → 6 % | 15.1 px | 0.63 | 1.05 | 47 |
| over the wet one | 16 % → 8 % | 29.8 px | 0.63 | 0.50 | 44 |
| long, no reload | 23 % → 5 % | 10.1 px | 0.63 | 0.22 | 325 | quarters: 0.29 → 0.07 → 0.01 → 0.00

Numbers say: light vs heavy: width 25.7 → 31.0 px, dark 0.63 → 0.63.

## Sponge
Gouache · 30 px · 30.1 s

![Sponge](Sponge.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 4 % → 0 % | 11.4 px | 0.62 | 0.12 | 41 |
| heavy line | 12 % → 2 % | 35.4 px | 0.62 | 0.14 | 86 |
| pressure swell | 7 % → 2 % | 27.9 px | 0.62 | 0.27 | 41 |
| fast wave | 20 % → 4 % | 23.2 px | 0.62 | 0.19 | 150 |
| slow wave | 21 % → 4 % | 23.7 px | 0.62 | 0.18 | 242 |
| spiral | 28 % → 4 % | 18.3 px | 0.62 | 0.14 | 207 |
| loop | 18 % → 5 % | 23.0 px | 0.62 | 0.29 | 96 |
| tilted | 7 % → 7 % | 18.2 px | 0.62 | 1.04 | 90 |
| over the wet one | 16 % → 6 % | 27.8 px | 0.62 | 0.37 | 122 |
| long, no reload | 29 % → 5 % | 12.9 px | 0.62 | 0.17 | 502 | quarters: 0.29 → 0.13 → 0.07 → 0.04

Numbers say: light vs heavy: width 11.4 → 35.4 px, dark 0.62 → 0.62.

## Ink — sumi brush
Watercolor · 22 px · 29.9 s

![Ink — sumi brush](Ink-sumi-brush.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 8 % → 9 % | 23.8 px | 0.77 | 1.13 | 64 |
| heavy line | 13 % → 13 % | 38.0 px | 0.72 | 1.01 | 68 |
| pressure swell | 9 % → 10 % | 34.5 px | 0.75 | 1.05 | 52 |
| fast wave | 27 % → 28 % | 31.7 px | 0.58 | 1.03 | 178 |
| slow wave | 25 % → 26 % | 29.0 px | 0.61 | 1.05 | 282 |
| spiral | 37 % → 38 % | 24.3 px | 0.51 | 1.03 | 321 |
| loop | 22 % → 22 % | 28.2 px | 0.66 | 1.03 | 166 |
| tilted | 9 % → 9 % | 24.7 px | 0.73 | 1.03 | 82 |
| over the wet one | 20 % → 21 % | 31.1 px | 0.73 | 1.03 | 114 |
| long, no reload | 42 % → 43 % | 18.9 px | 0.46 | 1.02 | 772 | quarters: 0.47 → 0.23 → 0.11 → 0.06

Numbers say: light vs heavy: width 23.8 → 38.0 px, dark 0.77 → 0.72.

## Ink — wash
Watercolor · 40 px · 33.2 s

![Ink — wash](Ink-wash.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 13 % → 13 % | 36.5 px | 0.17 | 1.04 | 89 |
| heavy line | 18 % → 19 % | 53.5 px | 0.13 | 1.04 | 95 |
| pressure swell | 12 % → 13 % | 46.6 px | 0.16 | 1.05 | 62 |
| fast wave | 40 % → 42 % | 45.9 px | 0.12 | 1.06 | 248 |
| slow wave | 38 % → 40 % | 43.6 px | 0.17 | 1.06 | 393 |
| spiral | 58 % → 62 % | 38.5 px | 0.12 | 1.06 | 524 |
| loop | 33 % → 34 % | 42.9 px | 0.15 | 1.03 | 237 |
| tilted | 14 % → 14 % | 38.1 px | 0.17 | 1.03 | 122 |
| over the wet one | 29 % → 31 % | 43.2 px | 0.17 | 1.06 | 75 |
| long, no reload | 66 % → 75 % | 29.8 px | 0.12 | 1.12 | 598 | quarters: 0.16 → 0.11 → 0.07 → 0.04

Numbers say: light vs heavy: width 36.5 → 53.5 px, dark 0.17 → 0.13.

## Ink — dry brush
Ink · 30 px · 24.9 s

![Ink — dry brush](Ink-dry-brush.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 9 % → 7 % | 25.2 px | 0.81 | 0.79 | 77 |
| heavy line | 10 % → 8 % | 29.6 px | 0.80 | 0.76 | 199 |
| pressure swell | 7 % → 6 % | 27.9 px | 0.81 | 0.85 | 77 |
| fast wave | 21 % → 8 % | 24.2 px | 0.79 | 0.40 | 270 |
| slow wave | 18 % → 7 % | 20.3 px | 0.79 | 0.39 | 364 |
| spiral | 24 % → 8 % | 15.6 px | 0.78 | 0.34 | 481 |
| loop | 19 % → 8 % | 24.3 px | 0.78 | 0.45 | 201 |
| tilted | 8 % → 8 % | 22.2 px | 0.78 | 1.02 | 127 |
| over the wet one | 17 % → 14 % | 25.9 px | 0.78 | 0.81 | 89 |
| long, no reload | 20 % → 8 % | 9.1 px | 0.79 | 0.41 | 522 | quarters: 0.32 → 0.02 → 0.00 → 0.00

Numbers say: light vs heavy: width 25.2 → 29.6 px, dark 0.81 → 0.80.

## Ink — nib
Watercolor · 5 px · 24.0 s

![Ink — nib](Ink-nib.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 2 % → 5 % | 5.4 px | 0.86 | 2.45 | 81 |
| heavy line | 2 % → 5 % | 6.4 px | 0.86 | 2.33 | 32 |
| pressure swell | 2 % → 4 % | 6.2 px | 0.86 | 2.52 | 19 |
| fast wave | 5 % → 8 % | 5.8 px | 0.82 | 1.65 | 68 |
| slow wave | 5 % → 8 % | 5.6 px | 0.82 | 1.73 | 62 |
| spiral | 7 % → 11 % | 4.8 px | 0.75 | 1.45 | 121 |
| loop | 4 % → 8 % | 5.6 px | 0.84 | 1.75 | 71 |
| tilted | 4 % → 4 % | 10.1 px | 0.85 | 1.04 | 40 |
| over the wet one | 6 % → 9 % | 6.3 px | 0.85 | 1.61 | 22 |
| long, no reload | 9 % → 12 % | 4.0 px | 0.70 | 1.37 | 149 | quarters: 0.23 → 0.08 → 0.04 → 0.02

Numbers say: light vs heavy: width 5.4 → 6.4 px, dark 0.86 → 0.86; wet paint spreads well beyond the stroke.

## 0.45 · Dry brush
Gouache · 34 px · 24.5 s

![0.45 · Dry brush](0-45-Dry-brush.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 10 % → 3 % | 29.4 px | 0.67 | 0.29 | 152 |
| heavy line | 11 % → 3 % | 31.6 px | 0.67 | 0.30 | 124 |
| pressure swell | 8 % → 3 % | 31.5 px | 0.67 | 0.41 | 82 |
| fast wave | 19 % → 3 % | 22.5 px | 0.67 | 0.18 | 407 |
| slow wave | 20 % → 4 % | 23.2 px | 0.67 | 0.18 | 500 |
| spiral | 21 % → 3 % | 14.1 px | 0.67 | 0.16 | 464 |
| loop | 20 % → 4 % | 26.1 px | 0.67 | 0.20 | 247 |
| tilted | 9 % → 8 % | 24.0 px | 0.67 | 0.98 | 142 |
| over the wet one | 19 % → 6 % | 28.2 px | 0.67 | 0.34 | 124 |
| long, no reload | 20 % → 4 % | 9.1 px | 0.67 | 0.19 | 672 | quarters: 0.36 → 0.10 → 0.00 → 0.00

Numbers say: light vs heavy: width 29.4 → 31.6 px, dark 0.67 → 0.67; pressure barely changes the width.

## Dry pastel
Pastel · 26 px · 10.2 s

![Dry pastel](Dry-pastel.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 3 % → 3 % | 8.3 px | 0.38 | 1.00 | 40 |
| heavy line | 5 % → 5 % | 13.2 px | 0.39 | 1.00 | 22 |
| pressure swell | 3 % → 3 % | 11.7 px | 0.38 | 1.00 | 25 |
| fast wave | 10 % → 10 % | 11.9 px | 0.39 | 1.00 | 104 |
| slow wave | 10 % → 10 % | 11.3 px | 0.39 | 1.00 | 127 |
| spiral | 15 % → 15 % | 9.6 px | 0.39 | 1.00 | 136 |
| loop | 7 % → 7 % | 9.4 px | 0.39 | 1.00 | 76 |
| tilted | 3 % → 3 % | 8.3 px | 0.38 | 1.00 | 27 |
| over the wet one | 7 % → 7 % | 11.1 px | 0.38 | 1.00 | 34 |
| long, no reload | 18 % → 18 % | 8.2 px | 0.39 | 1.00 | 232 | quarters: 0.08 → 0.08 → 0.08 → 0.07

Numbers say: light vs heavy: width 8.3 → 13.2 px, dark 0.38 → 0.39; the long stroke does not run out of paint.

## 0.45 · Charcoal
Charcoal · 18 px · 9.9 s

![0.45 · Charcoal](0-45-Charcoal.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 2 % → 2 % | 6.5 px | 0.80 | 1.00 | 16 |
| heavy line | 3 % → 3 % | 9.2 px | 0.80 | 1.00 | 15 |
| pressure swell | 2 % → 2 % | 8.8 px | 0.80 | 1.00 | 8 |
| fast wave | 7 % → 7 % | 8.5 px | 0.80 | 1.00 | 39 |
| slow wave | 7 % → 7 % | 8.0 px | 0.80 | 1.00 | 53 |
| spiral | 12 % → 12 % | 7.9 px | 0.80 | 1.00 | 171 |
| loop | 6 % → 6 % | 8.1 px | 0.80 | 1.00 | 31 |
| tilted | 3 % → 3 % | 7.5 px | 0.80 | 1.00 | 24 |
| over the wet one | 6 % → 6 % | 7.9 px | 0.80 | 1.00 | 18 |
| long, no reload | 17 % → 17 % | 7.8 px | 0.80 | 1.00 | 101 | quarters: 0.15 → 0.16 → 0.15 → 0.16

Numbers say: light vs heavy: width 6.5 → 9.2 px, dark 0.80 → 0.80; the long stroke does not run out of paint.

## Watercolour — wash
Watercolor · 50 px · 32.9 s

![Watercolour — wash](Watercolour-wash.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 15 % → 16 % | 43.3 px | 0.03 | 1.05 | 98 |
| heavy line | 21 % → 22 % | 62.1 px | 0.03 | 1.04 | 124 |
| pressure swell | 14 % → 15 % | 54.3 px | 0.03 | 1.04 | 77 |
| fast wave | 47 % → 49 % | 53.8 px | 0.02 | 1.04 | 241 |
| slow wave | 45 % → 46 % | 52.0 px | 0.04 | 1.03 | 589 |
| spiral | 64 % → 66 % | 42.5 px | 0.03 | 1.03 | 548 |
| loop | 39 % → 40 % | 50.3 px | 0.03 | 1.02 | 251 |
| tilted | 17 % → 17 % | 47.3 px | 0.04 | 1.03 | 163 |
| over the wet one | 35 % → 36 % | 49.0 px | 0.04 | 1.04 | 101 |
| long, no reload | 79 % → 84 % | 35.5 px | 0.03 | 1.06 | 678 | quarters: 0.04 → 0.03 → 0.02 → 0.01

Numbers say: light vs heavy: width 43.3 → 62.1 px, dark 0.03 → 0.03.

## Watercolour — wet-in-wet
Watercolor · 44 px · 31.4 s

![Watercolour — wet-in-wet](Watercolour-wet-in-wet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 13 % → 13 % | 36.6 px | 0.07 | 1.05 | 86 |
| heavy line | 18 % → 19 % | 52.4 px | 0.06 | 1.04 | 98 |
| pressure swell | 12 % → 12 % | 44.9 px | 0.07 | 1.04 | 69 |
| fast wave | 40 % → 41 % | 45.9 px | 0.05 | 1.04 | 214 |
| slow wave | 39 % → 40 % | 45.0 px | 0.08 | 1.03 | 364 |
| spiral | 62 % → 63 % | 40.8 px | 0.06 | 1.02 | 353 |
| loop | 33 % → 34 % | 43.2 px | 0.07 | 1.03 | 194 |
| tilted | 14 % → 15 % | 39.1 px | 0.08 | 1.04 | 141 |
| over the wet one | 29 % → 31 % | 42.0 px | 0.08 | 1.05 | 105 |
| long, no reload | 75 % → 78 % | 33.6 px | 0.06 | 1.04 | 525 | quarters: 0.07 → 0.06 → 0.04 → 0.03

Numbers say: light vs heavy: width 36.6 → 52.4 px, dark 0.07 → 0.06.

## Watercolour — glaze
Watercolor · 38 px · 30.5 s

![Watercolour — glaze](Watercolour-glaze.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 12 % → 13 % | 35.2 px | 0.03 | 1.05 | 71 |
| heavy line | 18 % → 19 % | 52.2 px | 0.02 | 1.06 | 90 |
| pressure swell | 12 % → 13 % | 44.6 px | 0.02 | 1.07 | 63 |
| fast wave | 37 % → 40 % | 42.4 px | 0.02 | 1.08 | 213 |
| slow wave | 35 % → 37 % | 40.2 px | 0.02 | 1.08 | 354 |
| spiral | 54 % → 59 % | 35.9 px | 0.02 | 1.09 | 338 |
| loop | 32 % → 33 % | 40.8 px | 0.02 | 1.05 | 175 |
| tilted | 13 % → 14 % | 37.0 px | 0.03 | 1.03 | 114 |
| over the wet one | 28 % → 30 % | 41.7 px | 0.03 | 1.06 | 82 |
| long, no reload | 60 % → 69 % | 26.8 px | 0.02 | 1.15 | 485 | quarters: 0.02 → 0.01 → 0.01 → 0.00

Numbers say: light vs heavy: width 35.2 → 52.2 px, dark 0.03 → 0.02.

## Watercolour — granulating
Watercolor · 44 px · 31.0 s

![Watercolour — granulating](Watercolour-granulating.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 14 % → 14 % | 40.5 px | 0.05 | 1.03 | 78 |
| heavy line | 20 % → 21 % | 59.2 px | 0.04 | 1.02 | 99 |
| pressure swell | 14 % → 14 % | 51.3 px | 0.05 | 1.02 | 70 |
| fast wave | 44 % → 45 % | 50.3 px | 0.04 | 1.04 | 256 |
| slow wave | 40 % → 42 % | 46.0 px | 0.06 | 1.06 | 368 |
| spiral | 59 % → 63 % | 38.7 px | 0.04 | 1.07 | 370 |
| loop | 36 % → 37 % | 46.9 px | 0.05 | 1.02 | 205 |
| tilted | 15 % → 16 % | 43.1 px | 0.06 | 1.03 | 130 |
| over the wet one | 32 % → 33 % | 46.6 px | 0.06 | 1.04 | 89 |
| long, no reload | 68 % → 76 % | 30.3 px | 0.04 | 1.12 | 531 | quarters: 0.06 → 0.04 → 0.02 → 0.02

Numbers say: light vs heavy: width 40.5 → 59.2 px, dark 0.05 → 0.04.

## Watercolour — dry brush
Watercolor · 36 px · 26.3 s

![Watercolour — dry brush](Watercolour-dry-brush.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 9 % → 9 % | 24.9 px | 0.07 | 1.09 | 91 |
| heavy line | 13 % → 13 % | 36.7 px | 0.06 | 0.99 | 94 |
| pressure swell | 10 % → 10 % | 36.4 px | 0.06 | 1.04 | 82 |
| fast wave | 24 % → 19 % | 27.3 px | 0.05 | 0.82 | 239 |
| slow wave | 22 % → 17 % | 25.2 px | 0.05 | 0.78 | 405 |
| spiral | 29 % → 20 % | 19.3 px | 0.05 | 0.67 | 388 |
| loop | 19 % → 18 % | 24.6 px | 0.05 | 0.94 | 206 |
| tilted | 9 % → 10 % | 24.3 px | 0.06 | 1.10 | 111 |
| over the wet one | 20 % → 20 % | 31.7 px | 0.06 | 0.99 | 95 |
| long, no reload | 28 % → 19 % | 12.4 px | 0.05 | 0.70 | 577 | quarters: 0.03 → 0.01 → 0.00 → 0.00

Numbers say: light vs heavy: width 24.9 → 36.7 px, dark 0.07 → 0.06.

## Gouache
Gouache · 30 px · 24.7 s

![Gouache](Gouache.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 8 % → 5 % | 24.4 px | 0.28 | 0.64 | 117 |
| heavy line | 14 % → 6 % | 39.7 px | 0.28 | 0.47 | 92 |
| pressure swell | 10 % → 6 % | 38.6 px | 0.28 | 0.60 | 79 |
| fast wave | 28 % → 7 % | 32.2 px | 0.28 | 0.25 | 207 |
| slow wave | 27 % → 8 % | 31.4 px | 0.28 | 0.29 | 321 |
| spiral | 38 % → 8 % | 24.8 px | 0.27 | 0.22 | 319 |
| loop | 22 % → 8 % | 28.6 px | 0.28 | 0.35 | 170 |
| tilted | 9 % → 9 % | 23.8 px | 0.27 | 1.01 | 90 |
| over the wet one | 20 % → 13 % | 31.1 px | 0.27 | 0.66 | 77 |
| long, no reload | 40 % → 9 % | 17.9 px | 0.27 | 0.24 | 465 | quarters: 0.01 → 0.01 → 0.02 → 0.02

Numbers say: light vs heavy: width 24.4 → 39.7 px, dark 0.28 → 0.28; the long stroke does not run out of paint.

## Oil — alla prima
Oil · 30 px · 17.5 s

![Oil — alla prima](Oil-alla-prima.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 9 % → 9 % | 27.6 px | 0.51 | 1.00 | 75 |
| heavy line | 10 % → 10 % | 30.3 px | 0.51 | 1.00 | 85 |
| pressure swell | 8 % → 8 % | 29.8 px | 0.53 | 1.00 | 62 |
| fast wave | 24 % → 24 % | 28.1 px | 0.51 | 1.00 | 208 |
| slow wave | 26 % → 26 % | 29.5 px | 0.51 | 1.00 | 339 |
| spiral | 40 % → 40 % | 26.4 px | 0.50 | 1.00 | 351 |
| loop | 21 % → 21 % | 27.6 px | 0.52 | 1.00 | 197 |
| tilted | 11 % → 11 % | 30.4 px | 0.51 | 1.00 | 106 |
| over the wet one | 20 % → 20 % | 26.5 px | 0.51 | 1.00 | 79 |
| long, no reload | 49 % → 49 % | 22.0 px | 0.50 | 1.00 | 528 | quarters: 0.32 → 0.28 → 0.25 → 0.22

Numbers say: light vs heavy: width 27.6 → 30.3 px, dark 0.51 → 0.51; pressure barely changes the width.

## Oil — impasto
Oil · 34 px · 18.6 s

![Oil — impasto](Oil-impasto.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 12 % → 12 % | 33.4 px | 0.25 | 1.00 | 91 |
| heavy line | 12 % → 12 % | 36.3 px | 0.25 | 1.00 | 100 |
| pressure swell | 10 % → 10 % | 35.9 px | 0.26 | 1.00 | 76 |
| fast wave | 30 % → 30 % | 35.1 px | 0.25 | 1.00 | 251 |
| slow wave | 31 % → 31 % | 35.7 px | 0.25 | 1.00 | 451 |
| spiral | 52 % → 52 % | 34.0 px | 0.23 | 1.00 | 453 |
| loop | 26 % → 26 % | 33.7 px | 0.24 | 1.00 | 232 |
| tilted | 12 % → 12 % | 32.8 px | 0.26 | 1.00 | 130 |
| over the wet one | 23 % → 23 % | 31.9 px | 0.26 | 1.00 | 101 |
| long, no reload | 60 % → 60 % | 26.9 px | 0.22 | 1.00 | 661 | quarters: 0.18 → 0.16 → 0.13 → 0.10

Numbers say: light vs heavy: width 33.4 → 36.3 px, dark 0.25 → 0.25; pressure barely changes the width.

## Oil — glaze
Oil · 40 px · 14.6 s

![Oil — glaze](Oil-glaze.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 9 % → 9 % | 25.4 px | 0.50 | 1.00 | 89 |
| heavy line | 13 % → 13 % | 36.3 px | 0.49 | 1.00 | 112 |
| pressure swell | 9 % → 9 % | 35.3 px | 0.50 | 1.00 | 83 |
| fast wave | 26 % → 26 % | 30.1 px | 0.48 | 1.00 | 271 |
| slow wave | 29 % → 29 % | 33.7 px | 0.49 | 1.00 | 437 |
| spiral | 44 % → 44 % | 29.0 px | 0.49 | 1.00 | 431 |
| loop | 23 % → 23 % | 30.2 px | 0.50 | 1.00 | 232 |
| tilted | 10 % → 10 % | 28.9 px | 0.50 | 1.00 | 125 |
| over the wet one | 22 % → 22 % | 31.6 px | 0.50 | 1.00 | 106 |
| long, no reload | 51 % → 51 % | 22.7 px | 0.49 | 1.00 | 637 | quarters: 0.33 → 0.29 → 0.26 → 0.22

Numbers say: light vs heavy: width 25.4 → 36.3 px, dark 0.50 → 0.49.

## Oil — scumble
Oil · 36 px · 19.1 s

![Oil — scumble](Oil-scumble.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 11 % → 11 % | 33.1 px | 0.27 | 1.00 | 118 |
| heavy line | 12 % → 12 % | 36.1 px | 0.27 | 1.00 | 128 |
| pressure swell | 9 % → 9 % | 35.5 px | 0.28 | 1.00 | 87 |
| fast wave | 26 % → 26 % | 29.6 px | 0.19 | 1.00 | 309 |
| slow wave | 27 % → 27 % | 30.9 px | 0.18 | 1.00 | 543 |
| spiral | 41 % → 41 % | 27.1 px | 0.13 | 1.00 | 533 |
| loop | 24 % → 24 % | 30.6 px | 0.20 | 1.00 | 289 |
| tilted | 11 % → 11 % | 30.4 px | 0.25 | 1.00 | 138 |
| over the wet one | 22 % → 22 % | 31.4 px | 0.25 | 1.00 | 131 |
| long, no reload | 45 % → 45 % | 20.3 px | 0.12 | 1.00 | 800 | quarters: 0.00 → 0.00 → 0.00 → 0.00

Numbers say: light vs heavy: width 33.1 → 36.1 px, dark 0.27 → 0.27; pressure barely changes the width.

## Acrylic — heavy body
Heavy acrylic · 30 px · 14.5 s

![Acrylic — heavy body](Acrylic-heavy-body.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 10 % → 9 % | 28.9 px | 0.51 | 0.91 | 92 |
| heavy line | 11 % → 10 % | 31.1 px | 0.51 | 0.93 | 87 |
| pressure swell | 8 % → 8 % | 30.7 px | 0.53 | 0.94 | 74 |
| fast wave | 23 % → 15 % | 26.5 px | 0.52 | 0.64 | 235 |
| slow wave | 24 % → 16 % | 27.7 px | 0.51 | 0.65 | 492 |
| spiral | 35 % → 15 % | 23.3 px | 0.51 | 0.43 | 378 |
| loop | 21 % → 16 % | 26.9 px | 0.51 | 0.76 | 187 |
| tilted | 9 % → 9 % | 24.9 px | 0.52 | 0.99 | 105 |
| over the wet one | 19 % → 17 % | 27.7 px | 0.52 | 0.89 | 94 |
| long, no reload | 39 % → 16 % | 17.3 px | 0.51 | 0.41 | 524 | quarters: 0.29 → 0.20 → 0.12 → 0.04

Numbers say: light vs heavy: width 28.9 → 31.1 px, dark 0.51 → 0.51; pressure barely changes the width.

## Acrylic — fluid
Watercolor · 36 px · 32.4 s

![Acrylic — fluid](Acrylic-fluid.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 12 % → 12 % | 34.3 px | 0.08 | 1.02 | 79 |
| heavy line | 18 % → 18 % | 51.6 px | 0.07 | 1.01 | 93 |
| pressure swell | 12 % → 12 % | 44.8 px | 0.08 | 1.01 | 55 |
| fast wave | 37 % → 38 % | 42.6 px | 0.07 | 1.02 | 196 |
| slow wave | 34 % → 35 % | 39.2 px | 0.07 | 1.03 | 359 |
| spiral | 52 % → 53 % | 34.2 px | 0.07 | 1.03 | 338 |
| loop | 30 % → 31 % | 39.4 px | 0.07 | 1.02 | 181 |
| tilted | 12 % → 12 % | 32.6 px | 0.08 | 1.04 | 107 |
| over the wet one | 27 % → 28 % | 43.2 px | 0.08 | 1.02 | 84 |
| long, no reload | 56 % → 58 % | 25.3 px | 0.06 | 1.04 | 507 | quarters: 0.06 → 0.05 → 0.03 → 0.02

Numbers say: light vs heavy: width 34.3 → 51.6 px, dark 0.08 → 0.07.

## Acrylic — palette knife
Heavy acrylic · 42 px · 18.7 s

![Acrylic — palette knife](Acrylic-palette-knife.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 15 % → 15 % | 44.0 px | 0.36 | 0.98 | 32 |
| heavy line | 15 % → 15 % | 44.2 px | 0.38 | 0.97 | 22 |
| pressure swell | 12 % → 12 % | 43.5 px | 0.40 | 0.99 | 7 |
| fast wave | 36 % → 20 % | 41.9 px | 0.35 | 0.56 | 52 |
| slow wave | 37 % → 21 % | 42.6 px | 0.35 | 0.57 | 84 |
| spiral | 50 % → 18 % | 32.8 px | 0.35 | 0.37 | 85 |
| loop | 32 % → 24 % | 41.2 px | 0.34 | 0.75 | 46 |
| tilted | 12 % → 12 % | 33.6 px | 0.37 | 1.00 | 19 |
| over the wet one | 26 % → 25 % | 39.7 px | 0.37 | 0.97 | 28 |
| long, no reload | 57 % → 21 % | 25.7 px | 0.33 | 0.36 | 125 | quarters: 0.00 → 0.00 → 0.00 → 0.01

Numbers say: light vs heavy: width 44.0 → 44.2 px, dark 0.36 → 0.38; pressure barely changes the width; the long stroke does not run out of paint.

## Finger on oil
Oil · 30 px · 13.4 s

![Finger on oil](Finger-on-oil.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 8 % → 8 % | 23.7 px | 0.40 | 1.00 | 58 |
| heavy line | 13 % → 13 % | 36.5 px | 0.38 | 1.00 | 68 |
| pressure swell | 9 % → 9 % | 33.3 px | 0.41 | 1.00 | 41 |
| fast wave | 22 % → 22 % | 26.0 px | 0.35 | 1.00 | 139 |
| slow wave | 24 % → 24 % | 27.8 px | 0.35 | 1.00 | 240 |
| spiral | 36 % → 36 % | 23.5 px | 0.27 | 1.00 | 227 |
| loop | 21 % → 21 % | 27.3 px | 0.36 | 1.00 | 122 |
| tilted | 9 % → 9 % | 26.4 px | 0.39 | 1.00 | 87 |
| over the wet one | 20 % → 20 % | 29.3 px | 0.39 | 1.00 | 57 |
| long, no reload | 36 % → 36 % | 16.3 px | 0.26 | 1.00 | 350 | quarters: 0.23 → 0.11 → 0.05 → 0.02

Numbers say: light vs heavy: width 23.7 → 36.5 px, dark 0.40 → 0.38.

## Palette knife — oil
Oil · 44 px · 19.3 s

![Palette knife — oil](Palette-knife-oil.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 16 % → 16 % | 45.6 px | 0.33 | 1.00 | 20 |
| heavy line | 16 % → 16 % | 46.3 px | 0.36 | 1.00 | 29 |
| pressure swell | 12 % → 12 % | 45.2 px | 0.35 | 1.00 | 13 |
| fast wave | 39 % → 39 % | 44.9 px | 0.31 | 1.00 | 56 |
| slow wave | 39 % → 39 % | 45.4 px | 0.32 | 1.00 | 103 |
| spiral | 62 % → 62 % | 40.9 px | 0.26 | 1.00 | 112 |
| loop | 34 % → 34 % | 43.8 px | 0.33 | 1.00 | 64 |
| tilted | 13 % → 13 % | 36.6 px | 0.35 | 1.00 | 30 |
| over the wet one | 28 % → 28 % | 40.8 px | 0.35 | 1.00 | 37 |
| long, no reload | 74 % → 74 % | 33.1 px | 0.24 | 1.00 | 181 | quarters: 0.00 → 0.00 → 0.00 → 0.00

Numbers say: light vs heavy: width 45.6 → 46.3 px, dark 0.33 → 0.36; pressure barely changes the width.

## 0.45 · Sponge
Watercolor · 46 px · 32.6 s

![0.45 · Sponge](0-45-Sponge.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 23 % → 15 % | 66.4 px | 0.02 | 0.67 | 51 |
| heavy line | 28 % → 23 % | 81.1 px | 0.02 | 0.81 | 81 |
| pressure swell | 20 % → 16 % | 76.7 px | 0.03 | 0.76 | 54 |
| fast wave | 46 % → 32 % | 53.0 px | 0.03 | 0.70 | 171 |
| slow wave | 53 % → 46 % | 60.7 px | 0.04 | 0.87 | 365 |
| spiral | 65 % → 53 % | 42.6 px | 0.04 | 0.82 | 295 |
| loop | 46 % → 40 % | 60.1 px | 0.04 | 0.86 | 149 |
| tilted | 16 % → 17 % | 43.8 px | 0.05 | 1.07 | 112 |
| over the wet one | 40 % → 35 % | 67.3 px | 0.05 | 0.89 | 71 |
| long, no reload | 74 % → 65 % | 33.2 px | 0.04 | 0.88 | 406 | quarters: 0.05 → 0.04 → 0.03 → 0.02

Numbers say: light vs heavy: width 66.4 → 81.1 px, dark 0.02 → 0.02.

## 0.45 · Eraser
Eraser · 30 px · 20.8 s · over bands of wet oil paint and oil pastel in turn (it works on paint already there: look at what it does to the bands; covered counts the bands too)

![0.45 · Eraser](0-45-Eraser.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 24 % → 24 % | 69.2 px | 0.82 | 1.00 | 26 |
| heavy line | 23 % → 23 % | 67.4 px | 0.81 | 1.00 | 54 |
| pressure swell | 23 % → 23 % | 86.7 px | 0.82 | 1.00 | 50 |
| fast wave | 21 % → 21 % | 24.7 px | 0.81 | 1.00 | 128 |
| slow wave | 20 % → 20 % | 23.5 px | 0.82 | 1.00 | 194 |
| spiral | 20 % → 20 % | 13.5 px | 0.79 | 1.00 | 216 |
| loop | 21 % → 21 % | 27.8 px | 0.80 | 1.00 | 112 |
| tilted | 23 % → 23 % | 64.8 px | 0.81 | 1.00 | 47 |
| over the wet one | 22 % → 22 % | 0.0 px | 0.81 | 1.00 | 46 |
| long, no reload | 17 % → 17 % | 7.5 px | 0.79 | 1.00 | 290 | quarters: 0.13 → 0.16 → 0.13 → 0.17

Numbers say: light vs heavy: width 69.2 → 67.4 px, dark 0.82 → 0.81; pressure barely changes the width; the long stroke does not run out of paint.

## Lift wet paint
Eraser · 30 px · 21.1 s · over bands of wet oil paint and oil pastel in turn (it works on paint already there: look at what it does to the bands; covered counts the bands too)

![Lift wet paint](Lift-wet-paint.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 24 % → 24 % | 70.1 px | 0.82 | 1.00 | 26 |
| heavy line | 24 % → 24 % | 69.8 px | 0.82 | 1.00 | 48 |
| pressure swell | 24 % → 24 % | 89.5 px | 0.82 | 1.00 | 33 |
| fast wave | 24 % → 24 % | 27.7 px | 0.82 | 1.00 | 111 |
| slow wave | 24 % → 24 % | 27.7 px | 0.82 | 1.00 | 148 |
| spiral | 24 % → 24 % | 15.9 px | 0.82 | 1.00 | 165 |
| loop | 24 % → 24 % | 31.1 px | 0.82 | 1.00 | 90 |
| tilted | 24 % → 24 % | 66.8 px | 0.82 | 1.00 | 52 |
| over the wet one | 24 % → 24 % | 0.0 px | 0.82 | 1.00 | 39 |
| long, no reload | 24 % → 24 % | 10.7 px | 0.82 | 1.00 | 232 | quarters: 0.18 → 0.24 → 0.17 → 0.24

Numbers say: light vs heavy: width 70.1 → 69.8 px, dark 0.82 → 0.82; pressure barely changes the width; the long stroke does not run out of paint.

## Sgraffito
Eraser · 10 px · 20.7 s · over bands of wet oil paint and oil pastel in turn (it works on paint already there: look at what it does to the bands; covered counts the bands too)

![Sgraffito](Sgraffito.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 24 % → 24 % | 69.5 px | 0.81 | 1.00 | 8 |
| heavy line | 24 % → 24 % | 69.5 px | 0.82 | 1.00 | 9 |
| pressure swell | 24 % → 24 % | 89.5 px | 0.82 | 1.00 | 8 |
| fast wave | 24 % → 24 % | 27.4 px | 0.82 | 1.00 | 18 |
| slow wave | 24 % → 24 % | 27.4 px | 0.81 | 1.00 | 22 |
| spiral | 24 % → 24 % | 15.7 px | 0.81 | 1.00 | 34 |
| loop | 24 % → 24 % | 30.9 px | 0.82 | 1.00 | 19 |
| tilted | 24 % → 24 % | 66.6 px | 0.82 | 1.00 | 10 |
| over the wet one | 24 % → 24 % | 0.0 px | 0.82 | 1.00 | 4 |
| long, no reload | 24 % → 24 % | 10.6 px | 0.82 | 1.00 | 52 | quarters: 0.17 → 0.24 → 0.17 → 0.24

Numbers say: light vs heavy: width 69.5 → 69.5 px, dark 0.81 → 0.82; pressure barely changes the width; the long stroke does not run out of paint.

## Brush Artist · Refs · #01 Henry Ward peach cloud
Gouache · 44 px · 38.7 s

![Brush Artist · Refs · #01 Henry Ward peach cloud](Brush-Artist-Refs-01-Henry-Ward-peach-cloud.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 15 % → 13 % | 42.3 px | 0.33 | 0.87 | 143 |
| heavy line | 16 % → 14 % | 45.7 px | 0.33 | 0.91 | 147 |
| pressure swell | 12 % → 11 % | 44.3 px | 0.33 | 0.92 | 115 |
| fast wave | 38 % → 25 % | 43.9 px | 0.33 | 0.65 | 346 |
| slow wave | 38 % → 26 % | 43.6 px | 0.33 | 0.68 | 641 |
| spiral | 61 % → 28 % | 40.2 px | 0.33 | 0.46 | 697 |
| loop | 32 % → 26 % | 41.6 px | 0.33 | 0.81 | 307 |
| tilted | 13 % → 13 % | 36.8 px | 0.33 | 1.00 | 173 |
| over the wet one | 27 % → 26 % | 39.2 px | 0.33 | 0.95 | 144 |
| long, no reload | 72 % → 28 % | 32.2 px | 0.33 | 0.40 | 1033 | quarters: 0.01 → 0.01 → 0.01 → 0.01

Numbers say: light vs heavy: width 42.3 → 45.7 px, dark 0.33 → 0.33; pressure barely changes the width; the long stroke does not run out of paint.

## Brush Artist · Refs · #02 Henry Ward cream strokes
Gouache · 46 px · 40.1 s

![Brush Artist · Refs · #02 Henry Ward cream strokes](Brush-Artist-Refs-02-Henry-Ward-cream-strokes.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 14 % → 13 % | 41.4 px | 0.42 | 0.94 | 153 |
| heavy line | 15 % → 15 % | 44.5 px | 0.42 | 0.96 | 144 |
| pressure swell | 12 % → 11 % | 43.9 px | 0.42 | 0.95 | 126 |
| fast wave | 36 % → 25 % | 41.9 px | 0.41 | 0.69 | 388 |
| slow wave | 36 % → 25 % | 41.8 px | 0.41 | 0.70 | 625 |
| spiral | 59 % → 28 % | 39.2 px | 0.41 | 0.46 | 676 |
| loop | 31 % → 27 % | 40.3 px | 0.41 | 0.86 | 370 |
| tilted | 13 % → 13 % | 37.3 px | 0.42 | 1.00 | 231 |
| over the wet one | 27 % → 26 % | 38.4 px | 0.42 | 0.96 | 208 |
| long, no reload | 70 % → 29 % | 31.3 px | 0.41 | 0.41 | 1683 | quarters: 0.01 → 0.01 → 0.01 → 0.01

Numbers say: light vs heavy: width 41.4 → 44.5 px, dark 0.42 → 0.42; pressure barely changes the width; the long stroke does not run out of paint.

## Brush Artist · Refs · #03 Henry Ward navy contours
Heavy acrylic · 22 px · 16.2 s

![Brush Artist · Refs · #03 Henry Ward navy contours](Brush-Artist-Refs-03-Henry-Ward-navy-contours.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 7 % → 7 % | 21.5 px | 0.70 | 0.94 | 67 |
| heavy line | 8 % → 8 % | 23.4 px | 0.70 | 0.95 | 88 |
| pressure swell | 6 % → 6 % | 23.2 px | 0.73 | 0.94 | 48 |
| fast wave | 19 % → 12 % | 21.8 px | 0.72 | 0.66 | 197 |
| slow wave | 19 % → 13 % | 22.4 px | 0.72 | 0.69 | 307 |
| spiral | 30 % → 13 % | 19.5 px | 0.72 | 0.45 | 290 |
| loop | 17 % → 13 % | 21.4 px | 0.72 | 0.81 | 183 |
| tilted | 8 % → 8 % | 22.6 px | 0.71 | 1.00 | 73 |
| over the wet one | 16 % → 14 % | 21.2 px | 0.71 | 0.89 | 176 |
| long, no reload | 34 % → 14 % | 15.1 px | 0.72 | 0.40 | 564 | quarters: 0.35 → 0.29 → 0.20 → 0.08

Numbers say: light vs heavy: width 21.5 → 23.4 px, dark 0.70 → 0.70; pressure barely changes the width.

## Brush Artist · Refs · #04 Henry Ward grey cloud
Gouache · 50 px · 43.6 s

![Brush Artist · Refs · #04 Henry Ward grey cloud](Brush-Artist-Refs-04-Henry-Ward-grey-cloud.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 16 % → 15 % | 47.1 px | 0.32 | 0.90 | 142 |
| heavy line | 17 % → 16 % | 50.6 px | 0.32 | 0.94 | 170 |
| pressure swell | 13 % → 12 % | 49.2 px | 0.32 | 0.94 | 118 |
| fast wave | 41 % → 28 % | 47.4 px | 0.32 | 0.67 | 576 |
| slow wave | 41 % → 28 % | 47.2 px | 0.32 | 0.69 | 1158 |
| spiral | 63 % → 30 % | 41.3 px | 0.32 | 0.48 | 846 |
| loop | 35 % → 29 % | 45.6 px | 0.32 | 0.84 | 390 |
| tilted | 14 % → 14 % | 40.3 px | 0.32 | 1.00 | 238 |
| over the wet one | 30 % → 29 % | 43.2 px | 0.32 | 0.96 | 203 |
| long, no reload | 76 % → 32 % | 33.9 px | 0.32 | 0.43 | 1186 | quarters: 0.01 → 0.01 → 0.01 → 0.01

Numbers say: light vs heavy: width 47.1 → 50.6 px, dark 0.32 → 0.32; pressure barely changes the width; the long stroke does not run out of paint.

## Brush Artist · Refs · #05 Henry Ward green in rust loops
Heavy acrylic · 20 px · 14.9 s

![Brush Artist · Refs · #05 Henry Ward green in rust loops](Brush-Artist-Refs-05-Henry-Ward-green-in-rust-loops.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 7 % → 6 % | 19.5 px | 0.55 | 0.94 | 118 |
| heavy line | 7 % → 7 % | 21.2 px | 0.55 | 0.94 | 97 |
| pressure swell | 6 % → 5 % | 21.5 px | 0.57 | 0.92 | 101 |
| fast wave | 17 % → 11 % | 19.7 px | 0.56 | 0.64 | 233 |
| slow wave | 18 % → 12 % | 20.3 px | 0.56 | 0.66 | 257 |
| spiral | 27 % → 12 % | 17.9 px | 0.55 | 0.42 | 302 |
| loop | 15 % → 12 % | 19.5 px | 0.55 | 0.80 | 172 |
| tilted | 8 % → 8 % | 21.7 px | 0.56 | 1.00 | 91 |
| over the wet one | 15 % → 13 % | 19.1 px | 0.56 | 0.87 | 85 |
| long, no reload | 30 % → 12 % | 13.4 px | 0.56 | 0.39 | 434 | quarters: 0.25 → 0.18 → 0.10 → 0.02

Numbers say: light vs heavy: width 19.5 → 21.2 px, dark 0.55 → 0.55; pressure barely changes the width.

## Brush Artist · Refs · #06 Henry Ward scrubbed grey
Gouache · 50 px · 42.1 s

![Brush Artist · Refs · #06 Henry Ward scrubbed grey](Brush-Artist-Refs-06-Henry-Ward-scrubbed-grey.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 16 % → 15 % | 47.1 px | 0.33 | 0.90 | 154 |
| heavy line | 17 % → 16 % | 50.6 px | 0.33 | 0.94 | 161 |
| pressure swell | 13 % → 12 % | 49.2 px | 0.33 | 0.94 | 126 |
| fast wave | 41 % → 28 % | 47.4 px | 0.33 | 0.67 | 498 |
| slow wave | 41 % → 28 % | 47.2 px | 0.33 | 0.69 | 800 |
| spiral | 63 % → 30 % | 41.3 px | 0.33 | 0.48 | 723 |
| loop | 35 % → 29 % | 45.6 px | 0.33 | 0.84 | 500 |
| tilted | 14 % → 14 % | 40.3 px | 0.33 | 1.00 | 223 |
| over the wet one | 30 % → 29 % | 43.2 px | 0.33 | 0.96 | 188 |
| long, no reload | 76 % → 32 % | 33.9 px | 0.33 | 0.43 | 1075 | quarters: 0.01 → 0.01 → 0.01 → 0.01

Numbers say: light vs heavy: width 47.1 → 50.6 px, dark 0.33 → 0.33; pressure barely changes the width; the long stroke does not run out of paint.

## Brush Artist · Refs · #07 Henry Ward blue L + black zigzag
Heavy acrylic · 34 px · 16.7 s

![Brush Artist · Refs · #07 Henry Ward blue L + black zigzag](Brush-Artist-Refs-07-Henry-Ward-blue-L-black-zigzag.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 11 % → 11 % | 33.1 px | 0.57 | 0.93 | 93 |
| heavy line | 12 % → 11 % | 35.7 px | 0.57 | 0.93 | 108 |
| pressure swell | 9 % → 9 % | 35.2 px | 0.59 | 0.94 | 73 |
| fast wave | 29 % → 20 % | 33.6 px | 0.59 | 0.69 | 233 |
| slow wave | 30 % → 21 % | 34.1 px | 0.58 | 0.73 | 407 |
| spiral | 47 % → 22 % | 31.3 px | 0.58 | 0.46 | 467 |
| loop | 25 % → 21 % | 32.7 px | 0.58 | 0.82 | 240 |
| tilted | 11 % → 11 % | 29.8 px | 0.58 | 1.00 | 122 |
| over the wet one | 22 % → 20 % | 31.7 px | 0.58 | 0.91 | 85 |
| long, no reload | 53 % → 22 % | 23.8 px | 0.59 | 0.42 | 591 | quarters: 0.40 → 0.32 → 0.21 → 0.10

Numbers say: light vs heavy: width 33.1 → 35.7 px, dark 0.57 → 0.57; pressure barely changes the width.

## Brush Artist · Refs · #08 Henry Ward olive bands
Gouache · 34 px · 25.0 s

![Brush Artist · Refs · #08 Henry Ward olive bands](Brush-Artist-Refs-08-Henry-Ward-olive-bands.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 8 % → 2 % | 24.7 px | 0.57 | 0.27 | 72 |
| heavy line | 12 % → 3 % | 33.9 px | 0.57 | 0.22 | 202 |
| pressure swell | 8 % → 3 % | 30.8 px | 0.57 | 0.38 | 88 |
| fast wave | 25 % → 4 % | 29.2 px | 0.57 | 0.15 | 282 |
| slow wave | 25 % → 4 % | 28.9 px | 0.57 | 0.15 | 519 |
| spiral | 39 % → 4 % | 25.7 px | 0.57 | 0.10 | 373 |
| loop | 22 % → 5 % | 28.8 px | 0.57 | 0.21 | 264 |
| tilted | 10 % → 10 % | 28.6 px | 0.57 | 0.98 | 117 |
| over the wet one | 20 % → 8 % | 28.3 px | 0.57 | 0.40 | 103 |
| long, no reload | 45 % → 6 % | 20.0 px | 0.57 | 0.13 | 756 | quarters: 0.35 → 0.27 → 0.17 → 0.08

Numbers say: light vs heavy: width 24.7 → 33.9 px, dark 0.57 → 0.57.

## Brush Artist · Refs · #09 Henry Ward white loops
Gouache · 46 px · 40.8 s

![Brush Artist · Refs · #09 Henry Ward white loops](Brush-Artist-Refs-09-Henry-Ward-white-loops.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 14 % → 13 % | 41.4 px | 0.44 | 0.94 | 153 |
| heavy line | 15 % → 15 % | 44.5 px | 0.45 | 0.96 | 236 |
| pressure swell | 12 % → 11 % | 43.9 px | 0.45 | 0.95 | 98 |
| fast wave | 36 % → 25 % | 41.9 px | 0.44 | 0.69 | 441 |
| slow wave | 36 % → 25 % | 41.8 px | 0.43 | 0.70 | 616 |
| spiral | 59 % → 28 % | 39.2 px | 0.43 | 0.46 | 709 |
| loop | 31 % → 27 % | 40.3 px | 0.43 | 0.86 | 286 |
| tilted | 13 % → 13 % | 37.3 px | 0.44 | 1.00 | 234 |
| over the wet one | 27 % → 26 % | 38.4 px | 0.44 | 0.96 | 253 |
| long, no reload | 70 % → 29 % | 31.3 px | 0.43 | 0.41 | 1060 | quarters: 0.01 → 0.01 → 0.01 → 0.01

Numbers say: light vs heavy: width 41.4 → 44.5 px, dark 0.44 → 0.45; pressure barely changes the width; the long stroke does not run out of paint.

## Brush Artist · Refs · #10 Henry Ward maroon loops
Heavy acrylic · 30 px · 15.7 s

![Brush Artist · Refs · #10 Henry Ward maroon loops](Brush-Artist-Refs-10-Henry-Ward-maroon-loops.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 10 % → 9 % | 28.0 px | 0.70 | 0.94 | 83 |
| heavy line | 10 % → 10 % | 30.2 px | 0.69 | 0.95 | 90 |
| pressure swell | 8 % → 8 % | 30.0 px | 0.73 | 0.94 | 68 |
| fast wave | 24 % → 17 % | 28.3 px | 0.73 | 0.71 | 184 |
| slow wave | 25 % → 18 % | 29.0 px | 0.73 | 0.73 | 355 |
| spiral | 39 % → 18 % | 26.0 px | 0.72 | 0.47 | 345 |
| loop | 21 % → 18 % | 27.6 px | 0.72 | 0.85 | 215 |
| tilted | 10 % → 10 % | 27.9 px | 0.72 | 1.00 | 125 |
| over the wet one | 20 % → 18 % | 26.8 px | 0.72 | 0.91 | 88 |
| long, no reload | 46 % → 18 % | 20.6 px | 0.73 | 0.40 | 547 | quarters: 0.44 → 0.38 → 0.31 → 0.22

Numbers say: light vs heavy: width 28.0 → 30.2 px, dark 0.70 → 0.69; pressure barely changes the width.

## Brush Artist · Refs · #11 Henry Ward purple spun balls
Heavy acrylic · 36 px · 17.9 s

![Brush Artist · Refs · #11 Henry Ward purple spun balls](Brush-Artist-Refs-11-Henry-Ward-purple-spun-balls.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 12 % → 11 % | 34.1 px | 0.70 | 0.96 | 117 |
| heavy line | 13 % → 12 % | 36.6 px | 0.70 | 0.96 | 109 |
| pressure swell | 10 % → 9 % | 36.2 px | 0.74 | 0.95 | 76 |
| fast wave | 30 % → 23 % | 34.6 px | 0.73 | 0.75 | 259 |
| slow wave | 30 % → 24 % | 35.0 px | 0.73 | 0.79 | 470 |
| spiral | 49 % → 25 % | 32.3 px | 0.73 | 0.50 | 531 |
| loop | 26 % → 23 % | 33.4 px | 0.73 | 0.88 | 308 |
| tilted | 11 % → 11 % | 31.2 px | 0.72 | 1.00 | 125 |
| over the wet one | 23 % → 21 % | 32.1 px | 0.72 | 0.93 | 103 |
| long, no reload | 55 % → 24 % | 24.8 px | 0.73 | 0.44 | 718 | quarters: 0.51 → 0.46 → 0.39 → 0.28

Numbers say: light vs heavy: width 34.1 → 36.6 px, dark 0.70 → 0.70; pressure barely changes the width.

## Brush Artist · Refs · #12 Henry Ward black-olive cage
Gouache · 28 px · 26.4 s

![Brush Artist · Refs · #12 Henry Ward black-olive cage](Brush-Artist-Refs-12-Henry-Ward-black-olive-cage.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 7 % → 3 % | 20.9 px | 0.61 | 0.35 | 48 |
| heavy line | 9 % → 4 % | 26.1 px | 0.61 | 0.41 | 125 |
| pressure swell | 6 % → 4 % | 23.9 px | 0.61 | 0.61 | 86 |
| fast wave | 20 % → 4 % | 23.7 px | 0.61 | 0.19 | 288 |
| slow wave | 20 % → 4 % | 23.3 px | 0.61 | 0.21 | 355 |
| spiral | 32 % → 4 % | 21.4 px | 0.61 | 0.14 | 315 |
| loop | 18 % → 5 % | 22.8 px | 0.61 | 0.28 | 228 |
| tilted | 9 % → 9 % | 25.4 px | 0.61 | 0.98 | 89 |
| over the wet one | 17 % → 8 % | 21.8 px | 0.61 | 0.46 | 78 |
| long, no reload | 39 % → 6 % | 17.6 px | 0.61 | 0.15 | 621 | quarters: 0.31 → 0.26 → 0.19 → 0.10

Numbers say: light vs heavy: width 20.9 → 26.1 px, dark 0.61 → 0.61.

## Brush Artist · Refs · #13 Henry Ward blue streaky form
Gouache · 50 px · 42.2 s

![Brush Artist · Refs · #13 Henry Ward blue streaky form](Brush-Artist-Refs-13-Henry-Ward-blue-streaky-form.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 16 % → 15 % | 47.1 px | 0.33 | 0.90 | 177 |
| heavy line | 17 % → 16 % | 50.6 px | 0.33 | 0.94 | 161 |
| pressure swell | 13 % → 12 % | 49.2 px | 0.33 | 0.94 | 143 |
| fast wave | 41 % → 28 % | 47.4 px | 0.33 | 0.67 | 437 |
| slow wave | 41 % → 28 % | 47.2 px | 0.33 | 0.69 | 798 |
| spiral | 63 % → 30 % | 41.3 px | 0.33 | 0.48 | 769 |
| loop | 35 % → 29 % | 45.6 px | 0.33 | 0.84 | 401 |
| tilted | 14 % → 14 % | 40.3 px | 0.33 | 1.00 | 286 |
| over the wet one | 30 % → 29 % | 43.2 px | 0.33 | 0.96 | 226 |
| long, no reload | 76 % → 32 % | 33.9 px | 0.33 | 0.43 | 1224 | quarters: 0.01 → 0.01 → 0.01 → 0.01

Numbers say: light vs heavy: width 47.1 → 50.6 px, dark 0.33 → 0.33; pressure barely changes the width; the long stroke does not run out of paint.

## Brush Artist · Refs · #14 Henry Ward olive totem
Heavy acrylic · 48 px · 23.6 s

![Brush Artist · Refs · #14 Henry Ward olive totem](Brush-Artist-Refs-14-Henry-Ward-olive-totem.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 15 % → 15 % | 44.8 px | 0.31 | 0.94 | 137 |
| heavy line | 16 % → 16 % | 47.7 px | 0.31 | 0.95 | 159 |
| pressure swell | 13 % → 12 % | 47.0 px | 0.32 | 0.95 | 115 |
| fast wave | 38 % → 30 % | 43.9 px | 0.30 | 0.79 | 386 |
| slow wave | 39 % → 31 % | 44.5 px | 0.30 | 0.81 | 747 |
| spiral | 58 % → 32 % | 38.1 px | 0.30 | 0.55 | 644 |
| loop | 33 % → 29 % | 42.6 px | 0.30 | 0.89 | 359 |
| tilted | 13 % → 13 % | 37.5 px | 0.31 | 1.00 | 335 |
| over the wet one | 28 % → 26 % | 41.1 px | 0.31 | 0.93 | 221 |
| long, no reload | 67 % → 33 % | 30.3 px | 0.30 | 0.49 | 1155 | quarters: 0.25 → 0.18 → 0.10 → 0.03

Numbers say: light vs heavy: width 44.8 → 47.7 px, dark 0.31 → 0.31; pressure barely changes the width.

## Brush Artist · Refs · #15 Ultramarine brush script
Ink · 10 px · 27.9 s

![Brush Artist · Refs · #15 Ultramarine brush script](Brush-Artist-Refs-15-Ultramarine-brush-script.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 2 % → 5 % | 5.0 px | 0.53 | 2.62 | 36 |
| heavy line | 10 % → 10 % | 29.6 px | 0.66 | 1.00 | 77 |
| pressure swell | 6 % → 6 % | 20.8 px | 0.68 | 1.12 | 51 |
| fast wave | 18 % → 17 % | 20.2 px | 0.59 | 0.95 | 148 |
| slow wave | 14 % → 14 % | 16.1 px | 0.59 | 1.00 | 135 |
| spiral | 22 % → 18 % | 14.5 px | 0.54 | 0.82 | 271 |
| loop | 13 % → 14 % | 17.4 px | 0.61 | 1.02 | 193 |
| tilted | 6 % → 6 % | 15.5 px | 0.68 | 1.01 | 88 |
| over the wet one | 13 % → 13 % | 20.5 px | 0.68 | 1.04 | 81 |
| long, no reload | 33 % → 20 % | 14.8 px | 0.52 | 0.59 | 434 | quarters: 0.30 → 0.14 → 0.05 → 0.02

Numbers say: light vs heavy: width 5.0 → 29.6 px, dark 0.53 → 0.66; wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #18 Blue oil-stick scribbles
Pastel · 10 px · 11.0 s

![Brush Artist · Refs · #18 Blue oil-stick scribbles](Brush-Artist-Refs-18-Blue-oil-stick-scribbles.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 1 % → 1 % | 2.9 px | 0.52 | 1.00 | 18 |
| heavy line | 2 % → 2 % | 5.5 px | 0.53 | 1.00 | 28 |
| pressure swell | 1 % → 1 % | 5.0 px | 0.53 | 1.00 | 22 |
| fast wave | 4 % → 4 % | 4.8 px | 0.53 | 1.00 | 51 |
| slow wave | 4 % → 4 % | 4.4 px | 0.53 | 1.00 | 53 |
| spiral | 7 % → 7 % | 4.5 px | 0.52 | 1.00 | 157 |
| loop | 3 % → 3 % | 4.5 px | 0.52 | 1.00 | 76 |
| tilted | 2 % → 2 % | 4.7 px | 0.53 | 1.00 | 53 |
| over the wet one | 3 % → 3 % | 4.7 px | 0.53 | 1.00 | 32 |
| long, no reload | 10 % → 10 % | 4.4 px | 0.53 | 1.00 | 164 | quarters: 0.06 → 0.06 → 0.06 → 0.06

Numbers say: light vs heavy: width 2.9 → 5.5 px, dark 0.52 → 0.53; the long stroke does not run out of paint.

## Brush Artist · Refs · #20 Orange-red crayon scribble
Pastel · 14 px · 12.1 s

![Brush Artist · Refs · #20 Orange-red crayon scribble](Brush-Artist-Refs-20-Orange-red-crayon-scribble.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 1 % → 1 % | 4.0 px | 0.53 | 1.00 | 31 |
| heavy line | 3 % → 3 % | 8.0 px | 0.53 | 1.00 | 36 |
| pressure swell | 2 % → 2 % | 7.6 px | 0.53 | 1.00 | 26 |
| fast wave | 6 % → 6 % | 7.2 px | 0.53 | 1.00 | 90 |
| slow wave | 6 % → 6 % | 6.6 px | 0.53 | 1.00 | 96 |
| spiral | 9 % → 9 % | 6.2 px | 0.53 | 1.00 | 150 |
| loop | 5 % → 5 % | 6.2 px | 0.53 | 1.00 | 62 |
| tilted | 2 % → 2 % | 5.6 px | 0.53 | 1.00 | 33 |
| over the wet one | 4 % → 4 % | 6.6 px | 0.53 | 1.00 | 45 |
| long, no reload | 13 % → 13 % | 5.7 px | 0.53 | 1.00 | 214 | quarters: 0.07 → 0.07 → 0.08 → 0.08

Numbers say: light vs heavy: width 4.0 → 8.0 px, dark 0.53 → 0.53; the long stroke does not run out of paint.

## Brush Artist · Refs · #21 Gritty black contours
Gouache · 12 px · 22.7 s

![Brush Artist · Refs · #21 Gritty black contours](Brush-Artist-Refs-21-Gritty-black-contours.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 3 % → 0 % | 8.8 px | 0.79 | 0.12 | 97 |
| heavy line | 4 % → 0 % | 11.9 px | 0.79 | 0.10 | 120 |
| pressure swell | 3 % → 0 % | 11.6 px | 0.79 | 0.15 | 71 |
| fast wave | 7 % → 1 % | 8.5 px | 0.79 | 0.10 | 226 |
| slow wave | 8 % → 1 % | 9.0 px | 0.79 | 0.09 | 217 |
| spiral | 9 % → 1 % | 6.0 px | 0.79 | 0.10 | 362 |
| loop | 8 % → 1 % | 9.9 px | 0.79 | 0.09 | 221 |
| tilted | 4 % → 4 % | 10.8 px | 0.79 | 0.90 | 116 |
| over the wet one | 7 % → 1 % | 9.7 px | 0.79 | 0.17 | 105 |
| long, no reload | 7 % → 1 % | 3.3 px | 0.79 | 0.12 | 869 | quarters: 0.20 → 0.07 → 0.00 → 0.00

Numbers say: light vs heavy: width 8.8 → 11.9 px, dark 0.79 → 0.79.

## Brush Artist · Refs · #22 Bold black brush poster
Ink · 20 px · 28.5 s

![Brush Artist · Refs · #22 Bold black brush poster](Brush-Artist-Refs-22-Bold-black-brush-poster.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 3 % → 5 % | 9.5 px | 0.79 | 1.63 | 47 |
| heavy line | 15 % → 15 % | 44.6 px | 0.88 | 0.99 | 160 |
| pressure swell | 9 % → 9 % | 31.9 px | 0.87 | 1.04 | 114 |
| fast wave | 27 % → 26 % | 31.2 px | 0.87 | 0.98 | 153 |
| slow wave | 22 % → 21 % | 25.2 px | 0.87 | 0.98 | 228 |
| spiral | 34 % → 32 % | 22.2 px | 0.87 | 0.94 | 316 |
| loop | 20 % → 20 % | 26.2 px | 0.88 | 1.00 | 130 |
| tilted | 8 % → 8 % | 22.7 px | 0.88 | 1.01 | 67 |
| over the wet one | 19 % → 19 % | 30.5 px | 0.88 | 1.00 | 72 |
| long, no reload | 45 % → 38 % | 20.2 px | 0.86 | 0.84 | 599 | quarters: 0.54 → 0.45 → 0.35 → 0.27

Numbers say: light vs heavy: width 9.5 → 44.6 px, dark 0.79 → 0.88; wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #23 Dry white on orange + black line
Gouache · 50 px · 26.3 s

![Brush Artist · Refs · #23 Dry white on orange + black line](Brush-Artist-Refs-23-Dry-white-on-orange-black-line.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 12 % → 2 % | 35.1 px | 0.39 | 0.13 | 162 |
| heavy line | 16 % → 2 % | 46.9 px | 0.39 | 0.11 | 261 |
| pressure swell | 11 % → 2 % | 42.6 px | 0.39 | 0.19 | 139 |
| fast wave | 34 % → 3 % | 39.7 px | 0.39 | 0.09 | 459 |
| slow wave | 34 % → 3 % | 39.0 px | 0.39 | 0.10 | 682 |
| spiral | 49 % → 4 % | 32.6 px | 0.38 | 0.07 | 716 |
| loop | 30 % → 4 % | 39.1 px | 0.38 | 0.12 | 430 |
| tilted | 13 % → 12 % | 34.9 px | 0.38 | 0.98 | 169 |
| over the wet one | 26 % → 7 % | 38.0 px | 0.38 | 0.27 | 141 |
| long, no reload | 58 % → 5 % | 26.1 px | 0.38 | 0.09 | 1016 | quarters: 0.02 → 0.02 → 0.03 → 0.04

Numbers say: light vs heavy: width 35.1 → 46.9 px, dark 0.39 → 0.39; the long stroke does not run out of paint.

## Brush Artist · Refs · #24 Picasso flat oil
Oil · 34 px · 21.0 s

![Brush Artist · Refs · #24 Picasso flat oil](Brush-Artist-Refs-24-Picasso-flat-oil.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 11 % → 11 % | 32.2 px | 0.39 | 1.00 | 153 |
| heavy line | 12 % → 12 % | 35.0 px | 0.39 | 1.00 | 147 |
| pressure swell | 9 % → 9 % | 34.4 px | 0.41 | 1.00 | 88 |
| fast wave | 30 % → 30 % | 34.2 px | 0.41 | 1.00 | 367 |
| slow wave | 30 % → 30 % | 34.9 px | 0.41 | 1.00 | 661 |
| spiral | 51 % → 51 % | 33.7 px | 0.40 | 1.00 | 608 |
| loop | 25 % → 25 % | 32.6 px | 0.41 | 1.00 | 305 |
| tilted | 11 % → 11 % | 32.0 px | 0.41 | 1.00 | 221 |
| over the wet one | 22 % → 22 % | 30.7 px | 0.41 | 1.00 | 155 |
| long, no reload | 61 % → 61 % | 27.6 px | 0.39 | 1.00 | 809 | quarters: 0.28 → 0.28 → 0.26 → 0.24

Numbers say: light vs heavy: width 32.2 → 35.0 px, dark 0.39 → 0.39; pressure barely changes the width.

## Brush Artist · Refs · #25 Yellow heavy flat stroke
Heavy acrylic · 110 px · 36.8 s

![Brush Artist · Refs · #25 Yellow heavy flat stroke](Brush-Artist-Refs-25-Yellow-heavy-flat-stroke.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 35 % → 36 % | 101.3 px | 0.30 | 1.02 | 489 |
| heavy line | 36 % → 35 % | 105.0 px | 0.30 | 0.97 | 483 |
| pressure swell | 28 % → 29 % | 105.4 px | 0.30 | 1.04 | 352 |
| fast wave | 72 % → 76 % | 83.8 px | 0.30 | 1.05 | 1234 |
| slow wave | 73 % → 72 % | 84.7 px | 0.29 | 0.98 | 2316 |
| spiral | 86 % → 83 % | 56.7 px | 0.28 | 0.97 | 1769 |
| loop | 65 % → 64 % | 83.6 px | 0.30 | 0.99 | 1084 |
| tilted | 26 % → 26 % | 71.5 px | 0.30 | 1.00 | 474 |
| over the wet one | 55 % → 54 % | 83.1 px | 0.30 | 0.97 | 505 |
| long, no reload | 98 % → 97 % | 44.1 px | 0.29 | 0.99 | 3079 | quarters: 0.00 → 0.00 → 0.00 → 0.00

Numbers say: light vs heavy: width 101.3 → 105.0 px, dark 0.30 → 0.30; pressure barely changes the width; the long stroke does not run out of paint.

## Brush Artist · Refs · #27 Orange impasto swatch
Heavy acrylic · 60 px · 26.0 s

![Brush Artist · Refs · #27 Orange impasto swatch](Brush-Artist-Refs-27-Orange-impasto-swatch.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 20 % → 19 % | 56.7 px | 0.35 | 0.97 | 216 |
| heavy line | 20 % → 20 % | 59.3 px | 0.35 | 0.97 | 198 |
| pressure swell | 16 % → 15 % | 59.6 px | 0.36 | 0.97 | 137 |
| fast wave | 48 % → 46 % | 55.0 px | 0.35 | 0.98 | 548 |
| slow wave | 48 % → 47 % | 55.8 px | 0.36 | 0.98 | 994 |
| spiral | 69 % → 62 % | 45.5 px | 0.35 | 0.91 | 758 |
| loop | 42 % → 40 % | 53.8 px | 0.35 | 0.97 | 404 |
| tilted | 16 % → 16 % | 44.0 px | 0.36 | 1.00 | 249 |
| over the wet one | 34 % → 33 % | 50.6 px | 0.36 | 0.97 | 226 |
| long, no reload | 85 % → 75 % | 38.1 px | 0.35 | 0.88 | 1101 | quarters: 0.33 → 0.31 → 0.29 → 0.26

Numbers say: light vs heavy: width 56.7 → 59.3 px, dark 0.35 → 0.35; pressure barely changes the width.

## Brush Artist · Refs · #28 Miles Davis black lines
Ink · 22 px · 27.3 s

![Brush Artist · Refs · #28 Miles Davis black lines](Brush-Artist-Refs-28-Miles-Davis-black-lines.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 4 % → 6 % | 12.2 px | 0.81 | 1.48 | 61 |
| heavy line | 17 % → 17 % | 49.1 px | 0.88 | 0.99 | 90 |
| pressure swell | 10 % → 10 % | 35.9 px | 0.87 | 1.03 | 41 |
| fast wave | 30 % → 30 % | 35.0 px | 0.87 | 0.98 | 145 |
| slow wave | 25 % → 25 % | 28.5 px | 0.87 | 0.99 | 212 |
| spiral | 38 % → 37 % | 25.3 px | 0.87 | 0.96 | 256 |
| loop | 23 % → 23 % | 29.4 px | 0.88 | 1.00 | 128 |
| tilted | 9 % → 9 % | 25.0 px | 0.88 | 1.01 | 67 |
| over the wet one | 21 % → 21 % | 34.1 px | 0.88 | 1.00 | 59 |
| long, no reload | 51 % → 43 % | 22.7 px | 0.86 | 0.85 | 469 | quarters: 0.59 → 0.51 → 0.40 → 0.31

Numbers say: light vs heavy: width 12.2 → 49.1 px, dark 0.81 → 0.88.

## Brush Artist · Refs · #29 Shrigley magenta asterisk
Watercolor · 70 px · 31.4 s

![Brush Artist · Refs · #29 Shrigley magenta asterisk](Brush-Artist-Refs-29-Shrigley-magenta-asterisk.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 10 % → 13 % | 28.0 px | 0.65 | 1.36 | 49 |
| heavy line | 17 % → 18 % | 50.3 px | 0.64 | 1.03 | 131 |
| pressure swell | 11 % → 12 % | 41.1 px | 0.65 | 1.13 | 85 |
| fast wave | 38 % → 38 % | 43.7 px | 0.64 | 1.00 | 262 |
| slow wave | 35 % → 39 % | 41.0 px | 0.65 | 1.10 | 486 |
| spiral | 61 % → 61 % | 40.0 px | 0.64 | 1.01 | 473 |
| loop | 31 % → 32 % | 40.2 px | 0.65 | 1.03 | 218 |
| tilted | 18 % → 18 % | 49.0 px | 0.65 | 1.00 | 235 |
| over the wet one | 31 % → 34 % | 38.4 px | 0.65 | 1.07 | 132 |
| long, no reload | 75 % → 75 % | 33.5 px | 0.64 | 1.00 | 837 | quarters: 0.55 → 0.53 → 0.52 → 0.49

Numbers say: light vs heavy: width 28.0 → 50.3 px, dark 0.65 → 0.64; the long stroke does not run out of paint.

## Brush Artist · Refs · #30 Red gouache face patch
Gouache · 60 px · 37.0 s

![Brush Artist · Refs · #30 Red gouache face patch](Brush-Artist-Refs-30-Red-gouache-face-patch.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 16 % → 15 % | 46.9 px | 0.49 | 0.91 | 134 |
| heavy line | 25 % → 20 % | 73.8 px | 0.49 | 0.80 | 269 |
| pressure swell | 19 % → 17 % | 72.6 px | 0.49 | 0.86 | 159 |
| fast wave | 48 % → 28 % | 55.1 px | 0.49 | 0.58 | 550 |
| slow wave | 48 % → 28 % | 55.3 px | 0.49 | 0.59 | 823 |
| spiral | 59 % → 28 % | 39.1 px | 0.49 | 0.48 | 834 |
| loop | 40 % → 29 % | 51.3 px | 0.49 | 0.74 | 337 |
| tilted | 16 % → 16 % | 45.7 px | 0.49 | 1.01 | 201 |
| over the wet one | 36 % → 32 % | 55.3 px | 0.49 | 0.88 | 161 |
| long, no reload | 67 % → 30 % | 30.0 px | 0.49 | 0.45 | 925 | quarters: 0.43 → 0.38 → 0.32 → 0.26

Numbers say: light vs heavy: width 46.9 → 73.8 px, dark 0.49 → 0.49.

## Brush Artist · Refs · #31 Warhol blotted line
Ink · 6 px · 21.5 s

![Brush Artist · Refs · #31 Warhol blotted line](Brush-Artist-Refs-31-Warhol-blotted-line.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 1 % → 3 % | 2.6 px | 0.75 | 3.30 | 35 |
| heavy line | 7 % → 7 % | 20.6 px | 0.83 | 0.97 | 64 |
| pressure swell | 4 % → 4 % | 14.8 px | 0.84 | 1.12 | 44 |
| fast wave | 12 % → 9 % | 13.8 px | 0.82 | 0.77 | 169 |
| slow wave | 10 % → 8 % | 11.2 px | 0.80 | 0.85 | 139 |
| spiral | 15 % → 9 % | 9.7 px | 0.80 | 0.58 | 189 |
| loop | 9 % → 9 % | 11.9 px | 0.80 | 0.94 | 98 |
| tilted | 3 % → 3 % | 8.6 px | 0.84 | 1.04 | 56 |
| over the wet one | 8 % → 8 % | 14.5 px | 0.84 | 1.02 | 44 |
| long, no reload | 21 % → 9 % | 9.6 px | 0.78 | 0.43 | 238 | quarters: 0.25 → 0.13 → 0.05 → 0.01

Numbers say: light vs heavy: width 2.6 → 20.6 px, dark 0.75 → 0.83; wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #32 Thick orange swipes
Heavy acrylic · 90 px · 30.8 s

![Brush Artist · Refs · #32 Thick orange swipes](Brush-Artist-Refs-32-Thick-orange-swipes.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 29 % → 29 % | 82.9 px | 0.38 | 1.00 | 272 |
| heavy line | 30 % → 29 % | 86.3 px | 0.38 | 0.97 | 284 |
| pressure swell | 23 % → 23 % | 86.5 px | 0.38 | 1.01 | 197 |
| fast wave | 63 % → 65 % | 73.1 px | 0.38 | 1.03 | 739 |
| slow wave | 64 % → 63 % | 73.5 px | 0.39 | 0.98 | 1253 |
| spiral | 79 % → 77 % | 52.2 px | 0.38 | 0.98 | 1258 |
| loop | 57 % → 56 % | 73.4 px | 0.38 | 0.99 | 621 |
| tilted | 21 % → 21 % | 59.3 px | 0.38 | 1.00 | 355 |
| over the wet one | 47 % → 45 % | 70.7 px | 0.38 | 0.97 | 309 |
| long, no reload | 95 % → 93 % | 42.7 px | 0.38 | 0.98 | 2116 | quarters: 0.38 → 0.38 → 0.37 → 0.35

Numbers say: light vs heavy: width 82.9 → 86.3 px, dark 0.38 → 0.38; pressure barely changes the width; the long stroke does not run out of paint.

## Brush Artist · Refs · #33 Red wet-in-wet band
Watercolor · 80 px · 38.5 s

![Brush Artist · Refs · #33 Red wet-in-wet band](Brush-Artist-Refs-33-Red-wet-in-wet-band.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 21 % → 21 % | 60.7 px | 0.66 | 1.01 | 104 |
| heavy line | 30 % → 30 % | 88.4 px | 0.66 | 0.98 | 213 |
| pressure swell | 20 % → 21 % | 75.9 px | 0.67 | 1.03 | 127 |
| fast wave | 61 % → 64 % | 71.0 px | 0.65 | 1.04 | 400 |
| slow wave | 60 % → 60 % | 68.9 px | 0.68 | 1.00 | 672 |
| spiral | 75 % → 75 % | 49.7 px | 0.67 | 1.00 | 652 |
| loop | 52 % → 52 % | 67.5 px | 0.67 | 1.00 | 336 |
| tilted | 24 % → 24 % | 67.8 px | 0.66 | 1.00 | 264 |
| over the wet one | 48 % → 50 % | 66.6 px | 0.66 | 1.04 | 153 |
| long, no reload | 95 % → 96 % | 42.8 px | 0.67 | 1.00 | 1179 | quarters: 0.68 → 0.68 → 0.67 → 0.61

Numbers say: light vs heavy: width 60.7 → 88.4 px, dark 0.66 → 0.66; the long stroke does not run out of paint.

## Brush Artist · Refs · #34 Magenta oil patches
Oil · 60 px · 24.1 s

![Brush Artist · Refs · #34 Magenta oil patches](Brush-Artist-Refs-34-Magenta-oil-patches.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 19 % → 19 % | 55.6 px | 0.59 | 1.00 | 191 |
| heavy line | 21 % → 21 % | 59.7 px | 0.59 | 1.00 | 202 |
| pressure swell | 16 % → 16 % | 58.8 px | 0.62 | 1.01 | 149 |
| fast wave | 48 % → 49 % | 55.4 px | 0.62 | 1.02 | 518 |
| slow wave | 48 % → 48 % | 55.8 px | 0.62 | 1.00 | 896 |
| spiral | 70 % → 70 % | 46.3 px | 0.62 | 1.00 | 971 |
| loop | 42 % → 42 % | 54.2 px | 0.62 | 1.00 | 590 |
| tilted | 17 % → 17 % | 46.8 px | 0.62 | 1.00 | 300 |
| over the wet one | 35 % → 35 % | 50.0 px | 0.62 | 1.00 | 252 |
| long, no reload | 86 % → 86 % | 38.7 px | 0.62 | 1.00 | 1436 | quarters: 0.59 → 0.58 → 0.57 → 0.52

Numbers say: light vs heavy: width 55.6 → 59.7 px, dark 0.59 → 0.59; pressure barely changes the width; the long stroke does not run out of paint.

## Brush Artist · Refs · #35 Red band with runs
Watercolor · 70 px · 37.0 s

![Brush Artist · Refs · #35 Red band with runs](Brush-Artist-Refs-35-Red-band-with-runs.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 18 % → 19 % | 53.2 px | 0.57 | 1.05 | 102 |
| heavy line | 27 % → 27 % | 78.7 px | 0.57 | 0.99 | 184 |
| pressure swell | 18 % → 18 % | 67.0 px | 0.59 | 1.02 | 113 |
| fast wave | 56 % → 56 % | 64.8 px | 0.57 | 1.00 | 357 |
| slow wave | 54 % → 55 % | 62.6 px | 0.60 | 1.01 | 648 |
| spiral | 72 % → 72 % | 47.6 px | 0.59 | 0.99 | 768 |
| loop | 48 % → 48 % | 61.7 px | 0.58 | 1.01 | 327 |
| tilted | 22 % → 22 % | 60.5 px | 0.58 | 1.00 | 228 |
| over the wet one | 43 % → 45 % | 59.7 px | 0.58 | 1.05 | 193 |
| long, no reload | 93 % → 92 % | 41.6 px | 0.59 | 0.99 | 886 | quarters: 0.58 → 0.59 → 0.57 → 0.53

Numbers say: light vs heavy: width 53.2 → 78.7 px, dark 0.57 → 0.57; the long stroke does not run out of paint.

## Brush Artist · Refs · #36 Magenta letters flat brush
Gouache · 36 px · 33.4 s

![Brush Artist · Refs · #36 Magenta letters flat brush](Brush-Artist-Refs-36-Magenta-letters-flat-brush.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 10 % → 10 % | 29.0 px | 0.45 | 0.98 | 73 |
| heavy line | 17 % → 14 % | 49.1 px | 0.45 | 0.85 | 119 |
| pressure swell | 13 % → 12 % | 49.4 px | 0.45 | 0.89 | 90 |
| fast wave | 35 % → 19 % | 40.3 px | 0.45 | 0.54 | 248 |
| slow wave | 35 % → 19 % | 39.9 px | 0.45 | 0.54 | 369 |
| spiral | 46 % → 19 % | 30.4 px | 0.45 | 0.42 | 389 |
| loop | 27 % → 20 % | 35.3 px | 0.45 | 0.72 | 179 |
| tilted | 11 % → 11 % | 29.8 px | 0.45 | 1.00 | 100 |
| over the wet one | 24 % → 22 % | 38.1 px | 0.45 | 0.92 | 113 |
| long, no reload | 46 % → 19 % | 20.8 px | 0.45 | 0.40 | 717 | quarters: 0.29 → 0.25 → 0.22 → 0.18

Numbers say: light vs heavy: width 29.0 → 49.1 px, dark 0.45 → 0.45.

## Brush Artist · Refs · #37 Oil still life dabs
Oil · 40 px · 21.0 s

![Brush Artist · Refs · #37 Oil still life dabs](Brush-Artist-Refs-37-Oil-still-life-dabs.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 13 % → 13 % | 37.9 px | 0.39 | 1.00 | 119 |
| heavy line | 14 % → 14 % | 41.1 px | 0.38 | 1.00 | 161 |
| pressure swell | 11 % → 11 % | 40.2 px | 0.40 | 1.00 | 113 |
| fast wave | 34 % → 34 % | 39.8 px | 0.40 | 1.00 | 370 |
| slow wave | 35 % → 35 % | 40.2 px | 0.39 | 1.00 | 578 |
| spiral | 59 % → 59 % | 38.7 px | 0.38 | 1.00 | 604 |
| loop | 29 % → 29 % | 37.8 px | 0.39 | 1.00 | 381 |
| tilted | 13 % → 13 % | 35.8 px | 0.39 | 1.00 | 215 |
| over the wet one | 26 % → 26 % | 35.6 px | 0.39 | 1.00 | 211 |
| long, no reload | 69 % → 69 % | 30.9 px | 0.37 | 1.00 | 852 | quarters: 0.31 → 0.30 → 0.28 → 0.24

Numbers say: light vs heavy: width 37.9 → 41.1 px, dark 0.39 → 0.38; pressure barely changes the width.

## Brush Artist · Refs · #38 Sanguine drawing
Pastel · 6 px · 9.3 s

![Brush Artist · Refs · #38 Sanguine drawing](Brush-Artist-Refs-38-Sanguine-drawing.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 1 % → 1 % | 2.0 px | 0.61 | 1.00 | 15 |
| heavy line | 1 % → 1 % | 3.5 px | 0.62 | 1.00 | 23 |
| pressure swell | 1 % → 1 % | 3.3 px | 0.62 | 1.00 | 11 |
| fast wave | 3 % → 3 % | 3.2 px | 0.61 | 1.00 | 33 |
| slow wave | 3 % → 3 % | 3.0 px | 0.61 | 1.00 | 34 |
| spiral | 4 % → 4 % | 2.9 px | 0.61 | 1.00 | 72 |
| loop | 2 % → 2 % | 3.0 px | 0.61 | 1.00 | 35 |
| tilted | 1 % → 1 % | 3.4 px | 0.62 | 1.00 | 21 |
| over the wet one | 2 % → 2 % | 2.9 px | 0.62 | 1.00 | 11 |
| long, no reload | 7 % → 7 % | 3.0 px | 0.61 | 1.00 | 90 | quarters: 0.04 → 0.05 → 0.05 → 0.05

Numbers say: light vs heavy: width 2.0 → 3.5 px, dark 0.61 → 0.62; the long stroke does not run out of paint.

## Brush Artist · Refs · #39 Very thick impasto
Heavy acrylic · 60 px · 22.9 s

![Brush Artist · Refs · #39 Very thick impasto](Brush-Artist-Refs-39-Very-thick-impasto.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 20 % → 19 % | 56.8 px | 0.61 | 0.97 | 161 |
| heavy line | 20 % → 20 % | 59.4 px | 0.61 | 0.97 | 239 |
| pressure swell | 16 % → 15 % | 59.6 px | 0.62 | 0.97 | 161 |
| fast wave | 48 % → 47 % | 55.2 px | 0.62 | 0.98 | 612 |
| slow wave | 48 % → 47 % | 56.0 px | 0.62 | 0.98 | 897 |
| spiral | 69 % → 65 % | 45.6 px | 0.62 | 0.93 | 759 |
| loop | 42 % → 41 % | 54.0 px | 0.62 | 0.97 | 381 |
| tilted | 16 % → 16 % | 44.0 px | 0.62 | 1.00 | 211 |
| over the wet one | 34 % → 33 % | 50.7 px | 0.62 | 0.97 | 181 |
| long, no reload | 85 % → 79 % | 38.3 px | 0.62 | 0.93 | 1528 | quarters: 0.58 → 0.57 → 0.55 → 0.52

Numbers say: light vs heavy: width 56.8 → 59.4 px, dark 0.61 → 0.61; pressure barely changes the width; the long stroke does not run out of paint.

## Brush Artist · Refs · #40 Watercolour blooms
Watercolor · 90 px · 41.1 s

![Brush Artist · Refs · #40 Watercolour blooms](Brush-Artist-Refs-40-Watercolour-blooms.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 23 % → 24 % | 68.2 px | 0.12 | 1.02 | 196 |
| heavy line | 34 % → 33 % | 98.4 px | 0.12 | 0.98 | 382 |
| pressure swell | 23 % → 24 % | 85.3 px | 0.13 | 1.04 | 161 |
| fast wave | 66 % → 69 % | 76.7 px | 0.12 | 1.04 | 595 |
| slow wave | 65 % → 65 % | 74.7 px | 0.16 | 1.00 | 867 |
| spiral | 79 % → 79 % | 52.0 px | 0.15 | 1.00 | 869 |
| loop | 57 % → 57 % | 73.7 px | 0.14 | 1.00 | 742 |
| tilted | 26 % → 26 % | 73.8 px | 0.14 | 1.00 | 389 |
| over the wet one | 53 % → 55 % | 73.9 px | 0.14 | 1.05 | 241 |
| long, no reload | 97 % → 97 % | 43.5 px | 0.15 | 1.00 | 1714 | quarters: 0.18 → 0.17 → 0.14 → 0.11

Numbers say: light vs heavy: width 68.2 → 98.4 px, dark 0.12 → 0.12.

## Brush Artist · Refs · #41 Coloured pencil hatching
Pastel · 4 px · 10.0 s

![Brush Artist · Refs · #41 Coloured pencil hatching](Brush-Artist-Refs-41-Coloured-pencil-hatching.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 1 % → 1 % | 1.6 px | 0.42 | 1.00 | 10 |
| heavy line | 1 % → 1 % | 2.6 px | 0.43 | 1.00 | 7 |
| pressure swell | 1 % → 1 % | 2.1 px | 0.43 | 1.00 | 7 |
| fast wave | 2 % → 2 % | 2.2 px | 0.42 | 1.00 | 32 |
| slow wave | 2 % → 2 % | 2.1 px | 0.43 | 1.00 | 27 |
| spiral | 3 % → 3 % | 2.1 px | 0.43 | 1.00 | 50 |
| loop | 2 % → 2 % | 2.2 px | 0.43 | 1.00 | 39 |
| tilted | 1 % → 1 % | 3.0 px | 0.42 | 1.00 | 20 |
| over the wet one | 2 % → 2 % | 2.2 px | 0.42 | 1.00 | 19 |
| long, no reload | 5 % → 5 % | 2.3 px | 0.43 | 1.00 | 129 | quarters: 0.02 → 0.02 → 0.02 → 0.03

Numbers say: light vs heavy: width 1.6 → 2.6 px, dark 0.42 → 0.43; the long stroke does not run out of paint.

## Brush Artist · Refs · #42 Oil pastel shaggy
Pastel · 18 px · 9.8 s

![Brush Artist · Refs · #42 Oil pastel shaggy](Brush-Artist-Refs-42-Oil-pastel-shaggy.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 2 % → 2 % | 5.1 px | 0.35 | 1.00 | 12 |
| heavy line | 4 % → 4 % | 10.7 px | 0.36 | 1.00 | 24 |
| pressure swell | 3 % → 3 % | 9.5 px | 0.36 | 1.00 | 16 |
| fast wave | 8 % → 8 % | 9.0 px | 0.36 | 1.00 | 67 |
| slow wave | 7 % → 7 % | 8.2 px | 0.36 | 1.00 | 137 |
| spiral | 12 % → 12 % | 7.7 px | 0.36 | 1.00 | 101 |
| loop | 6 % → 6 % | 7.9 px | 0.36 | 1.00 | 93 |
| tilted | 2 % → 2 % | 6.9 px | 0.36 | 1.00 | 29 |
| over the wet one | 6 % → 6 % | 8.5 px | 0.36 | 1.00 | 47 |
| long, no reload | 15 % → 15 % | 6.9 px | 0.36 | 1.00 | 185 | quarters: 0.00 → 0.00 → 0.00 → 0.00

Numbers say: light vs heavy: width 5.1 → 10.7 px, dark 0.35 → 0.36; the long stroke does not run out of paint.

## Brush Artist · Refs · #43 Dragged black ink blocks
Gouache · 70 px · 30.5 s

![Brush Artist · Refs · #43 Dragged black ink blocks](Brush-Artist-Refs-43-Dragged-black-ink-blocks.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 19 % → 5 % | 54.9 px | 0.57 | 0.28 | 117 |
| heavy line | 24 % → 9 % | 69.0 px | 0.57 | 0.38 | 370 |
| pressure swell | 17 % → 9 % | 63.4 px | 0.57 | 0.53 | 274 |
| fast wave | 51 % → 11 % | 58.7 px | 0.57 | 0.21 | 605 |
| slow wave | 50 % → 10 % | 58.1 px | 0.57 | 0.20 | 1071 |
| spiral | 65 % → 14 % | 42.6 px | 0.57 | 0.22 | 981 |
| loop | 45 % → 12 % | 58.1 px | 0.57 | 0.27 | 484 |
| tilted | 17 % → 16 % | 46.4 px | 0.57 | 0.98 | 269 |
| over the wet one | 37 % → 20 % | 55.6 px | 0.57 | 0.56 | 257 |
| long, no reload | 82 % → 17 % | 36.6 px | 0.57 | 0.21 | 1467 | quarters: 0.54 → 0.52 → 0.47 → 0.40

Numbers say: light vs heavy: width 54.9 → 69.0 px, dark 0.57 → 0.57.

## Brush Artist · Refs · #44 Blue looping ribbon
Oil · 80 px · 26.3 s

![Brush Artist · Refs · #44 Blue looping ribbon](Brush-Artist-Refs-44-Blue-looping-ribbon.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 26 % → 27 % | 74.8 px | 0.71 | 1.04 | 323 |
| heavy line | 27 % → 27 % | 79.6 px | 0.71 | 1.00 | 298 |
| pressure swell | 21 % → 21 % | 78.1 px | 0.72 | 1.03 | 228 |
| fast wave | 61 % → 64 % | 70.3 px | 0.73 | 1.05 | 755 |
| slow wave | 61 % → 61 % | 70.0 px | 0.73 | 1.00 | 1402 |
| spiral | 78 % → 78 % | 51.3 px | 0.73 | 1.00 | 1342 |
| loop | 54 % → 54 % | 69.7 px | 0.72 | 1.00 | 698 |
| tilted | 20 % → 20 % | 57.2 px | 0.71 | 1.00 | 373 |
| over the wet one | 44 % → 44 % | 64.9 px | 0.71 | 1.00 | 317 |
| long, no reload | 96 % → 96 % | 42.8 px | 0.73 | 1.00 | 2169 | quarters: 0.72 → 0.72 → 0.72 → 0.69

Numbers say: light vs heavy: width 74.8 → 79.6 px, dark 0.71 → 0.71; pressure barely changes the width; the long stroke does not run out of paint.

## Brush Artist · Refs · #45 Soft pastel pepper
Pastel · 40 px · 10.1 s

![Brush Artist · Refs · #45 Soft pastel pepper](Brush-Artist-Refs-45-Soft-pastel-pepper.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 4 % → 4 % | 11.3 px | 0.53 | 1.00 | 35 |
| heavy line | 8 % → 8 % | 23.0 px | 0.53 | 1.00 | 48 |
| pressure swell | 5 % → 5 % | 19.5 px | 0.53 | 1.00 | 37 |
| fast wave | 17 % → 17 % | 19.4 px | 0.53 | 1.00 | 133 |
| slow wave | 15 % → 15 % | 17.1 px | 0.53 | 1.00 | 210 |
| spiral | 25 % → 25 % | 16.3 px | 0.53 | 1.00 | 215 |
| loop | 12 % → 12 % | 16.1 px | 0.53 | 1.00 | 93 |
| tilted | 5 % → 5 % | 12.8 px | 0.53 | 1.00 | 61 |
| over the wet one | 11 % → 11 % | 17.7 px | 0.53 | 1.00 | 59 |
| long, no reload | 30 % → 30 % | 13.6 px | 0.53 | 1.00 | 280 | quarters: 0.18 → 0.18 → 0.18 → 0.18

Numbers say: light vs heavy: width 11.3 → 23.0 px, dark 0.53 → 0.53; the long stroke does not run out of paint.

## Brush Artist · Refs · #46 Red-brown ink lips
Watercolor · 70 px · 33.6 s

![Brush Artist · Refs · #46 Red-brown ink lips](Brush-Artist-Refs-46-Red-brown-ink-lips.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 18 % → 18 % | 53.2 px | 0.74 | 1.00 | 116 |
| heavy line | 27 % → 27 % | 78.7 px | 0.74 | 0.98 | 188 |
| pressure swell | 18 % → 18 % | 67.0 px | 0.75 | 1.01 | 110 |
| fast wave | 56 % → 58 % | 64.8 px | 0.73 | 1.03 | 346 |
| slow wave | 54 % → 54 % | 62.6 px | 0.74 | 1.00 | 581 |
| spiral | 72 % → 72 % | 47.6 px | 0.74 | 1.00 | 557 |
| loop | 48 % → 48 % | 61.7 px | 0.74 | 1.00 | 297 |
| tilted | 22 % → 22 % | 60.5 px | 0.74 | 1.00 | 230 |
| over the wet one | 43 % → 44 % | 59.9 px | 0.74 | 1.03 | 151 |
| long, no reload | 93 % → 93 % | 41.6 px | 0.74 | 1.00 | 950 | quarters: 0.73 → 0.73 → 0.72 → 0.67

Numbers say: light vs heavy: width 53.2 → 78.7 px, dark 0.74 → 0.74; the long stroke does not run out of paint.

## Brush Artist · Refs · #47 Pink knife slabs
Heavy acrylic · 90 px · 26.7 s

![Brush Artist · Refs · #47 Pink knife slabs](Brush-Artist-Refs-47-Pink-knife-slabs.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 28 % → 27 % | 81.0 px | 0.28 | 0.97 | 211 |
| heavy line | 29 % → 28 % | 83.4 px | 0.28 | 0.97 | 239 |
| pressure swell | 22 % → 22 % | 83.4 px | 0.28 | 1.01 | 146 |
| fast wave | 61 % → 60 % | 70.1 px | 0.27 | 0.98 | 564 |
| slow wave | 61 % → 59 % | 70.9 px | 0.26 | 0.96 | 1018 |
| spiral | 76 % → 58 % | 50.0 px | 0.26 | 0.76 | 1074 |
| loop | 55 % → 54 % | 71.7 px | 0.27 | 0.97 | 517 |
| tilted | 21 % → 21 % | 59.3 px | 0.28 | 1.00 | 248 |
| over the wet one | 46 % → 44 % | 67.9 px | 0.28 | 0.96 | 215 |
| long, no reload | 92 % → 76 % | 41.3 px | 0.26 | 0.83 | 1344 | quarters: 0.00 → 0.00 → 0.00 → 0.00

Numbers say: light vs heavy: width 81.0 → 83.4 px, dark 0.28 → 0.28; pressure barely changes the width; the long stroke does not run out of paint.

## Brush Artist · Refs · #48 Black bands with drips
Gouache · 70 px · 38.5 s

![Brush Artist · Refs · #48 Black bands with drips](Brush-Artist-Refs-48-Black-bands-with-drips.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 19 % → 18 % | 54.6 px | 0.69 | 0.93 | 179 |
| heavy line | 29 % → 24 % | 83.0 px | 0.69 | 0.84 | 294 |
| pressure swell | 23 % → 21 % | 86.1 px | 0.69 | 0.92 | 187 |
| fast wave | 53 % → 36 % | 61.8 px | 0.69 | 0.68 | 597 |
| slow wave | 53 % → 36 % | 61.7 px | 0.69 | 0.67 | 964 |
| spiral | 64 % → 35 % | 41.9 px | 0.69 | 0.55 | 969 |
| loop | 45 % → 36 % | 57.8 px | 0.69 | 0.81 | 445 |
| tilted | 19 % → 19 % | 52.3 px | 0.69 | 1.00 | 258 |
| over the wet one | 41 % → 38 % | 62.4 px | 0.69 | 0.92 | 212 |
| long, no reload | 74 % → 37 % | 33.3 px | 0.69 | 0.50 | 1193 | quarters: 0.64 → 0.61 → 0.54 → 0.45

Numbers say: light vs heavy: width 54.6 → 83.0 px, dark 0.69 → 0.69.

## Brush Artist · Refs · #49 Magenta letters round brush
Ink · 30 px · 27.9 s

![Brush Artist · Refs · #49 Magenta letters round brush](Brush-Artist-Refs-49-Magenta-letters-round-brush.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 6 % → 8 % | 17.5 px | 0.50 | 1.28 | 42 |
| heavy line | 21 % → 21 % | 62.0 px | 0.51 | 0.99 | 110 |
| pressure swell | 12 % → 13 % | 46.3 px | 0.52 | 1.01 | 73 |
| fast wave | 38 % → 38 % | 44.3 px | 0.51 | 0.99 | 242 |
| slow wave | 32 % → 31 % | 36.4 px | 0.51 | 0.99 | 318 |
| spiral | 50 % → 48 % | 32.8 px | 0.51 | 0.97 | 309 |
| loop | 29 % → 29 % | 37.6 px | 0.51 | 1.00 | 160 |
| tilted | 11 % → 11 % | 30.7 px | 0.52 | 1.01 | 94 |
| over the wet one | 26 % → 26 % | 42.1 px | 0.52 | 1.01 | 83 |
| long, no reload | 61 % → 56 % | 27.5 px | 0.51 | 0.92 | 394 | quarters: 0.41 → 0.36 → 0.30 → 0.25

Numbers say: light vs heavy: width 17.5 → 62.0 px, dark 0.50 → 0.51.

## Brush Artist · Refs · #50 Thick swipes on photo
Heavy acrylic · 40 px · 16.6 s

![Brush Artist · Refs · #50 Thick swipes on photo](Brush-Artist-Refs-50-Thick-swipes-on-photo.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 13 % → 13 % | 38.0 px | 0.25 | 0.96 | 142 |
| heavy line | 14 % → 13 % | 40.1 px | 0.25 | 0.96 | 118 |
| pressure swell | 11 % → 10 % | 40.1 px | 0.25 | 0.95 | 106 |
| fast wave | 33 % → 31 % | 38.3 px | 0.25 | 0.93 | 290 |
| slow wave | 34 % → 32 % | 39.1 px | 0.25 | 0.95 | 495 |
| spiral | 58 % → 47 % | 38.5 px | 0.24 | 0.80 | 519 |
| loop | 28 % → 27 % | 36.8 px | 0.26 | 0.95 | 246 |
| tilted | 12 % → 12 % | 34.0 px | 0.25 | 1.00 | 142 |
| over the wet one | 25 % → 24 % | 35.2 px | 0.25 | 0.95 | 100 |
| long, no reload | 66 % → 46 % | 29.5 px | 0.24 | 0.70 | 719 | quarters: 0.00 → 0.00 → 0.00 → 0.00

Numbers say: light vs heavy: width 38.0 → 40.1 px, dark 0.25 → 0.25; pressure barely changes the width; the long stroke does not run out of paint.

## Brush Artist · Refs · Ground #22403f
Gouache · 130 px · 57.7 s

![Brush Artist · Refs · Ground #22403f](Brush-Artist-Refs-Ground-22403f.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 42 % → 40 % | 122.8 px | 0.52 | 0.94 | 601 |
| heavy line | 47 % → 42 % | 136.0 px | 0.52 | 0.90 | 522 |
| pressure swell | 43 % → 42 % | 162.8 px | 0.52 | 0.97 | 448 |
| fast wave | 83 % → 82 % | 95.8 px | 0.52 | 0.98 | 1296 |
| slow wave | 83 % → 76 % | 96.3 px | 0.52 | 0.91 | 2366 |
| spiral | 88 % → 84 % | 57.7 px | 0.52 | 0.96 | 2150 |
| loop | 66 % → 64 % | 85.6 px | 0.52 | 0.96 | 1158 |
| tilted | 37 % → 36 % | 102.0 px | 0.52 | 1.00 | 667 |
| over the wet one | 72 % → 69 % | 99.4 px | 0.52 | 0.96 | 558 |
| long, no reload | 98 % → 93 % | 44.0 px | 0.52 | 0.94 | 3084 | quarters: 0.52 → 0.52 → 0.52 → 0.50

Numbers say: light vs heavy: width 122.8 → 136.0 px, dark 0.52 → 0.52; pressure barely changes the width; the long stroke does not run out of paint.

## Brush Artist · Refs · Ground #2b2f1c
Gouache · 130 px · 57.8 s

![Brush Artist · Refs · Ground #2b2f1c](Brush-Artist-Refs-Ground-2b2f1c.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 42 % → 40 % | 122.8 px | 0.56 | 0.94 | 530 |
| heavy line | 47 % → 42 % | 136.0 px | 0.56 | 0.90 | 575 |
| pressure swell | 43 % → 42 % | 162.8 px | 0.56 | 0.97 | 404 |
| fast wave | 83 % → 82 % | 95.8 px | 0.56 | 0.98 | 1347 |
| slow wave | 83 % → 76 % | 96.3 px | 0.56 | 0.91 | 2418 |
| spiral | 88 % → 84 % | 57.7 px | 0.56 | 0.96 | 2246 |
| loop | 66 % → 64 % | 85.6 px | 0.56 | 0.96 | 1188 |
| tilted | 37 % → 36 % | 102.0 px | 0.56 | 1.00 | 716 |
| over the wet one | 72 % → 69 % | 99.4 px | 0.56 | 0.96 | 532 |
| long, no reload | 98 % → 93 % | 44.0 px | 0.56 | 0.94 | 3167 | quarters: 0.56 → 0.56 → 0.56 → 0.55

Numbers say: light vs heavy: width 122.8 → 136.0 px, dark 0.56 → 0.56; pressure barely changes the width; the long stroke does not run out of paint.

## Brush Artist · Refs · Ground #e8b4a8
Gouache · 130 px · 58.1 s

![Brush Artist · Refs · Ground #e8b4a8](Brush-Artist-Refs-Ground-e8b4a8.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 42 % → 40 % | 122.8 px | 0.32 | 0.94 | 469 |
| heavy line | 47 % → 42 % | 136.0 px | 0.32 | 0.90 | 488 |
| pressure swell | 43 % → 42 % | 162.8 px | 0.32 | 0.97 | 366 |
| fast wave | 83 % → 82 % | 95.8 px | 0.32 | 0.98 | 1379 |
| slow wave | 83 % → 76 % | 96.3 px | 0.32 | 0.91 | 2275 |
| spiral | 88 % → 84 % | 57.7 px | 0.32 | 0.96 | 2191 |
| loop | 66 % → 64 % | 85.6 px | 0.32 | 0.96 | 1110 |
| tilted | 37 % → 36 % | 102.0 px | 0.32 | 1.00 | 681 |
| over the wet one | 72 % → 69 % | 99.4 px | 0.32 | 0.96 | 492 |
| long, no reload | 98 % → 93 % | 44.0 px | 0.32 | 0.94 | 3214 | quarters: 0.00 → 0.00 → 0.00 → 0.00

Numbers say: light vs heavy: width 122.8 → 136.0 px, dark 0.32 → 0.32; pressure barely changes the width.

## Brush Artist · Refs · Ground #d8d4c8
Gouache · 130 px · 57.1 s

![Brush Artist · Refs · Ground #d8d4c8](Brush-Artist-Refs-Ground-d8d4c8.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 42 % → 40 % | 122.8 px | 0.38 | 0.94 | 460 |
| heavy line | 47 % → 42 % | 136.0 px | 0.38 | 0.90 | 514 |
| pressure swell | 43 % → 42 % | 162.8 px | 0.38 | 0.97 | 387 |
| fast wave | 83 % → 82 % | 95.8 px | 0.38 | 0.98 | 1278 |
| slow wave | 83 % → 76 % | 96.3 px | 0.38 | 0.91 | 2293 |
| spiral | 88 % → 84 % | 57.7 px | 0.38 | 0.96 | 2173 |
| loop | 66 % → 64 % | 85.6 px | 0.38 | 0.96 | 1085 |
| tilted | 37 % → 36 % | 102.0 px | 0.38 | 1.00 | 650 |
| over the wet one | 72 % → 69 % | 99.4 px | 0.38 | 0.96 | 479 |
| long, no reload | 98 % → 93 % | 44.0 px | 0.38 | 0.94 | 2952 | quarters: 0.00 → 0.00 → 0.00 → 0.00

Numbers say: light vs heavy: width 122.8 → 136.0 px, dark 0.38 → 0.38; pressure barely changes the width.

## Brush Artist · Refs · Ground #f06040
Gouache · 130 px · 59.2 s

![Brush Artist · Refs · Ground #f06040](Brush-Artist-Refs-Ground-f06040.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 42 % → 40 % | 122.8 px | 0.34 | 0.94 | 468 |
| heavy line | 47 % → 42 % | 136.0 px | 0.34 | 0.90 | 480 |
| pressure swell | 43 % → 42 % | 162.8 px | 0.34 | 0.97 | 394 |
| fast wave | 83 % → 82 % | 95.8 px | 0.34 | 0.98 | 1313 |
| slow wave | 83 % → 76 % | 96.3 px | 0.34 | 0.91 | 2312 |
| spiral | 88 % → 84 % | 57.7 px | 0.34 | 0.96 | 2190 |
| loop | 66 % → 64 % | 85.6 px | 0.34 | 0.96 | 1134 |
| tilted | 37 % → 36 % | 102.0 px | 0.34 | 1.00 | 672 |
| over the wet one | 72 % → 69 % | 99.4 px | 0.34 | 0.96 | 519 |
| long, no reload | 98 % → 93 % | 44.0 px | 0.34 | 0.94 | 2976 | quarters: 0.35 → 0.35 → 0.34 → 0.33

Numbers say: light vs heavy: width 122.8 → 136.0 px, dark 0.34 → 0.34; pressure barely changes the width; the long stroke does not run out of paint.

## Brush Artist · Refs · Ground #e85a10
Gouache · 130 px · 57.5 s

![Brush Artist · Refs · Ground #e85a10](Brush-Artist-Refs-Ground-e85a10.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 42 % → 40 % | 122.8 px | 0.37 | 0.94 | 475 |
| heavy line | 47 % → 42 % | 136.0 px | 0.37 | 0.90 | 538 |
| pressure swell | 43 % → 42 % | 162.8 px | 0.37 | 0.97 | 384 |
| fast wave | 83 % → 82 % | 95.8 px | 0.37 | 0.98 | 1428 |
| slow wave | 83 % → 76 % | 96.3 px | 0.37 | 0.91 | 2232 |
| spiral | 88 % → 84 % | 57.7 px | 0.37 | 0.96 | 2115 |
| loop | 66 % → 64 % | 85.6 px | 0.37 | 0.96 | 1128 |
| tilted | 37 % → 36 % | 102.0 px | 0.37 | 1.00 | 663 |
| over the wet one | 72 % → 69 % | 99.4 px | 0.37 | 0.96 | 536 |
| long, no reload | 98 % → 93 % | 44.0 px | 0.37 | 0.94 | 3175 | quarters: 0.37 → 0.37 → 0.37 → 0.36

Numbers say: light vs heavy: width 122.8 → 136.0 px, dark 0.37 → 0.37; pressure barely changes the width; the long stroke does not run out of paint.

## Brush Artist · Refs · Ground #8c8c88
Gouache · 130 px · 56.6 s

![Brush Artist · Refs · Ground #8c8c88](Brush-Artist-Refs-Ground-8c8c88.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 42 % → 40 % | 122.8 px | 0.24 | 0.94 | 461 |
| heavy line | 47 % → 42 % | 136.0 px | 0.24 | 0.90 | 489 |
| pressure swell | 43 % → 42 % | 162.8 px | 0.24 | 0.97 | 361 |
| fast wave | 83 % → 82 % | 95.8 px | 0.24 | 0.98 | 1269 |
| slow wave | 83 % → 76 % | 96.3 px | 0.24 | 0.91 | 2249 |
| spiral | 88 % → 84 % | 57.7 px | 0.24 | 0.96 | 2064 |
| loop | 66 % → 64 % | 85.6 px | 0.24 | 0.96 | 1133 |
| tilted | 37 % → 36 % | 102.0 px | 0.23 | 1.00 | 659 |
| over the wet one | 72 % → 69 % | 99.4 px | 0.23 | 0.96 | 485 |
| long, no reload | 98 % → 93 % | 44.0 px | 0.24 | 0.94 | 2959 | quarters: 0.24 → 0.24 → 0.24 → 0.22

Numbers say: light vs heavy: width 122.8 → 136.0 px, dark 0.24 → 0.24; pressure barely changes the width; the long stroke does not run out of paint.

## Brush Artist · Refs · Ground #f0c020
Gouache · 130 px · 57.6 s

![Brush Artist · Refs · Ground #f0c020](Brush-Artist-Refs-Ground-f0c020.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 42 % → 40 % | 122.8 px | 0.30 | 0.94 | 507 |
| heavy line | 47 % → 42 % | 136.0 px | 0.30 | 0.90 | 505 |
| pressure swell | 43 % → 42 % | 162.8 px | 0.30 | 0.97 | 373 |
| fast wave | 83 % → 82 % | 95.8 px | 0.30 | 0.98 | 1264 |
| slow wave | 83 % → 76 % | 96.3 px | 0.30 | 0.91 | 2258 |
| spiral | 88 % → 84 % | 57.7 px | 0.30 | 0.96 | 2187 |
| loop | 66 % → 64 % | 85.6 px | 0.30 | 0.96 | 1099 |
| tilted | 37 % → 36 % | 102.0 px | 0.30 | 1.00 | 682 |
| over the wet one | 72 % → 69 % | 99.4 px | 0.30 | 0.96 | 506 |
| long, no reload | 98 % → 93 % | 44.0 px | 0.30 | 0.94 | 3048 | quarters: 0.00 → 0.00 → 0.00 → 0.00

Numbers say: light vs heavy: width 122.8 → 136.0 px, dark 0.30 → 0.30; pressure barely changes the width.

## Brush Artist · Refs · Ground #e8dcc4
Gouache · 130 px · 58.5 s

![Brush Artist · Refs · Ground #e8dcc4](Brush-Artist-Refs-Ground-e8dcc4.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 42 % → 40 % | 122.8 px | 0.40 | 0.94 | 512 |
| heavy line | 47 % → 42 % | 136.0 px | 0.40 | 0.90 | 507 |
| pressure swell | 43 % → 42 % | 162.8 px | 0.39 | 0.97 | 378 |
| fast wave | 83 % → 82 % | 95.8 px | 0.40 | 0.98 | 1311 |
| slow wave | 83 % → 76 % | 96.3 px | 0.40 | 0.91 | 2266 |
| spiral | 88 % → 84 % | 57.7 px | 0.39 | 0.96 | 2220 |
| loop | 66 % → 64 % | 85.6 px | 0.40 | 0.96 | 1198 |
| tilted | 37 % → 36 % | 102.0 px | 0.39 | 1.00 | 671 |
| over the wet one | 72 % → 69 % | 99.4 px | 0.39 | 0.96 | 528 |
| long, no reload | 98 % → 93 % | 44.0 px | 0.39 | 0.94 | 3062 | quarters: 0.00 → 0.00 → 0.00 → 0.00

Numbers say: light vs heavy: width 122.8 → 136.0 px, dark 0.40 → 0.40; pressure barely changes the width.

## Brush Artist · Refs · Ground #f0a020
Gouache · 130 px · 58.5 s

![Brush Artist · Refs · Ground #f0a020](Brush-Artist-Refs-Ground-f0a020.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 42 % → 40 % | 122.8 px | 0.19 | 0.94 | 468 |
| heavy line | 47 % → 42 % | 136.0 px | 0.19 | 0.90 | 541 |
| pressure swell | 43 % → 42 % | 162.8 px | 0.19 | 0.97 | 395 |
| fast wave | 83 % → 82 % | 95.8 px | 0.19 | 0.98 | 1320 |
| slow wave | 83 % → 76 % | 96.3 px | 0.19 | 0.91 | 2298 |
| spiral | 88 % → 84 % | 57.7 px | 0.19 | 0.96 | 2178 |
| loop | 66 % → 64 % | 85.6 px | 0.19 | 0.96 | 1150 |
| tilted | 37 % → 36 % | 102.0 px | 0.19 | 1.00 | 667 |
| over the wet one | 72 % → 69 % | 99.4 px | 0.19 | 0.96 | 556 |
| long, no reload | 98 % → 93 % | 44.0 px | 0.19 | 0.94 | 3189 | quarters: 0.18 → 0.19 → 0.19 → 0.18

Numbers say: light vs heavy: width 122.8 → 136.0 px, dark 0.19 → 0.19; pressure barely changes the width; the long stroke does not run out of paint.

## Brush Artist · Refs · Ground #ff6a10
Gouache · 130 px · 58.4 s

![Brush Artist · Refs · Ground #ff6a10](Brush-Artist-Refs-Ground-ff6a10.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 42 % → 40 % | 122.8 px | 0.36 | 0.94 | 479 |
| heavy line | 47 % → 42 % | 136.0 px | 0.36 | 0.90 | 526 |
| pressure swell | 43 % → 42 % | 162.8 px | 0.36 | 0.97 | 406 |
| fast wave | 83 % → 82 % | 95.8 px | 0.36 | 0.98 | 1361 |
| slow wave | 83 % → 76 % | 96.3 px | 0.36 | 0.91 | 2417 |
| spiral | 88 % → 84 % | 57.7 px | 0.36 | 0.96 | 2280 |
| loop | 66 % → 64 % | 85.6 px | 0.36 | 0.96 | 1169 |
| tilted | 37 % → 36 % | 102.0 px | 0.36 | 1.00 | 685 |
| over the wet one | 72 % → 69 % | 99.4 px | 0.36 | 0.96 | 536 |
| long, no reload | 98 % → 93 % | 44.0 px | 0.36 | 0.94 | 3147 | quarters: 0.36 → 0.36 → 0.36 → 0.35

Numbers say: light vs heavy: width 122.8 → 136.0 px, dark 0.36 → 0.36; pressure barely changes the width; the long stroke does not run out of paint.

## Brush Artist · Ink — wash
Watercolor · 38 px · 28.4 s

![Brush Artist · Ink — wash](Brush-Artist-Ink-wash.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 11 % → 11 % | 31.6 px | 0.38 | 1.03 | 57 |
| heavy line | 19 % → 19 % | 54.3 px | 0.32 | 1.03 | 97 |
| pressure swell | 12 % → 12 % | 45.1 px | 0.36 | 1.04 | 59 |
| fast wave | 39 % → 41 % | 44.7 px | 0.30 | 1.05 | 201 |
| slow wave | 37 % → 38 % | 42.6 px | 0.37 | 1.04 | 324 |
| spiral | 57 % → 60 % | 37.9 px | 0.30 | 1.04 | 324 |
| loop | 32 % → 33 % | 41.8 px | 0.34 | 1.02 | 165 |
| tilted | 13 % → 14 % | 36.8 px | 0.38 | 1.04 | 98 |
| over the wet one | 29 % → 30 % | 42.8 px | 0.38 | 1.04 | 73 |
| long, no reload | 65 % → 70 % | 29.2 px | 0.29 | 1.08 | 473 | quarters: 0.33 → 0.26 → 0.18 → 0.11

Numbers say: light vs heavy: width 31.6 → 54.3 px, dark 0.38 → 0.32.

## Brush Artist · Ink — brush line
Ink · 16 px · 24.5 s

![Brush Artist · Ink — brush line](Brush-Artist-Ink-brush-line.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 3 % → 5 % | 7.7 px | 0.78 | 1.80 | 32 |
| heavy line | 13 % → 13 % | 39.0 px | 0.88 | 0.99 | 77 |
| pressure swell | 8 % → 8 % | 28.4 px | 0.87 | 1.05 | 46 |
| fast wave | 24 % → 23 % | 27.6 px | 0.87 | 0.96 | 153 |
| slow wave | 19 % → 19 % | 22.5 px | 0.87 | 0.97 | 180 |
| spiral | 30 % → 27 % | 19.9 px | 0.86 | 0.90 | 251 |
| loop | 18 % → 18 % | 23.4 px | 0.88 | 1.00 | 120 |
| tilted | 7 % → 7 % | 20.1 px | 0.88 | 1.01 | 63 |
| over the wet one | 17 % → 17 % | 26.8 px | 0.88 | 1.00 | 60 |
| long, no reload | 42 % → 31 % | 18.8 px | 0.85 | 0.73 | 339 | quarters: 0.49 → 0.40 → 0.30 → 0.21

Numbers say: light vs heavy: width 7.7 → 39.0 px, dark 0.78 → 0.88; wet paint spreads well beyond the stroke.

## Brush Artist · Ink — dry brush
Gouache · 30 px · 20.4 s

![Brush Artist · Ink — dry brush](Brush-Artist-Ink-dry-brush.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 7 % → 1 % | 21.8 px | 0.71 | 0.11 | 57 |
| heavy line | 10 % → 1 % | 27.7 px | 0.71 | 0.10 | 117 |
| pressure swell | 7 % → 2 % | 25.5 px | 0.71 | 0.23 | 68 |
| fast wave | 21 % → 2 % | 24.2 px | 0.71 | 0.09 | 219 |
| slow wave | 21 % → 2 % | 23.9 px | 0.71 | 0.08 | 382 |
| spiral | 31 % → 2 % | 20.6 px | 0.71 | 0.06 | 349 |
| loop | 18 % → 2 % | 23.9 px | 0.71 | 0.13 | 193 |
| tilted | 9 % → 8 % | 24.1 px | 0.71 | 0.96 | 107 |
| over the wet one | 17 % → 4 % | 22.8 px | 0.71 | 0.24 | 89 |
| long, no reload | 31 % → 3 % | 14.0 px | 0.71 | 0.09 | 513 | quarters: 0.38 → 0.32 → 0.22 → 0.09

Numbers say: light vs heavy: width 21.8 → 27.7 px, dark 0.71 → 0.71.

## Brush Artist · Watercolour — blue
Watercolor · 40 px · 25.2 s

![Brush Artist · Watercolour — blue](Brush-Artist-Watercolour-blue.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 6 % → 10 % | 16.7 px | 0.25 | 1.70 | 29 |
| heavy line | 11 % → 12 % | 31.5 px | 0.25 | 1.13 | 66 |
| pressure swell | 7 % → 9 % | 25.4 px | 0.26 | 1.32 | 38 |
| fast wave | 24 % → 25 % | 27.8 px | 0.24 | 1.05 | 148 |
| slow wave | 22 % → 27 % | 25.9 px | 0.26 | 1.22 | 223 |
| spiral | 38 % → 41 % | 25.1 px | 0.22 | 1.08 | 214 |
| loop | 20 % → 22 % | 25.3 px | 0.26 | 1.13 | 112 |
| tilted | 12 % → 12 % | 33.3 px | 0.26 | 1.00 | 92 |
| over the wet one | 21 % → 24 % | 24.7 px | 0.26 | 1.15 | 57 |
| long, no reload | 51 % → 54 % | 23.0 px | 0.22 | 1.04 | 358 | quarters: 0.18 → 0.14 → 0.11 → 0.08

Numbers say: light vs heavy: width 16.7 → 31.5 px, dark 0.25 → 0.25; wet paint spreads well beyond the stroke.

## Brush Artist · Watercolour — violet
Watercolor · 40 px · 25.5 s

![Brush Artist · Watercolour — violet](Brush-Artist-Watercolour-violet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 6 % → 10 % | 16.7 px | 0.40 | 1.70 | 31 |
| heavy line | 11 % → 12 % | 31.5 px | 0.40 | 1.13 | 64 |
| pressure swell | 7 % → 9 % | 25.4 px | 0.41 | 1.32 | 38 |
| fast wave | 24 % → 25 % | 27.8 px | 0.38 | 1.05 | 143 |
| slow wave | 22 % → 27 % | 25.9 px | 0.40 | 1.22 | 227 |
| spiral | 38 % → 41 % | 25.1 px | 0.36 | 1.08 | 216 |
| loop | 20 % → 22 % | 25.3 px | 0.40 | 1.13 | 117 |
| tilted | 12 % → 12 % | 33.3 px | 0.40 | 1.00 | 97 |
| over the wet one | 21 % → 24 % | 24.7 px | 0.40 | 1.15 | 51 |
| long, no reload | 51 % → 54 % | 23.0 px | 0.34 | 1.04 | 347 | quarters: 0.28 → 0.22 → 0.17 → 0.14

Numbers say: light vs heavy: width 16.7 → 31.5 px, dark 0.40 → 0.40; wet paint spreads well beyond the stroke.

## Brush Artist · Watercolour — teal
Watercolor · 40 px · 25.4 s

![Brush Artist · Watercolour — teal](Brush-Artist-Watercolour-teal.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 6 % → 10 % | 16.7 px | 0.16 | 1.70 | 28 |
| heavy line | 11 % → 12 % | 31.5 px | 0.16 | 1.13 | 64 |
| pressure swell | 7 % → 9 % | 25.4 px | 0.17 | 1.32 | 45 |
| fast wave | 24 % → 25 % | 27.8 px | 0.15 | 1.05 | 132 |
| slow wave | 22 % → 27 % | 25.9 px | 0.17 | 1.22 | 219 |
| spiral | 38 % → 41 % | 25.1 px | 0.15 | 1.08 | 209 |
| loop | 20 % → 22 % | 25.3 px | 0.16 | 1.13 | 115 |
| tilted | 12 % → 12 % | 33.3 px | 0.16 | 1.00 | 88 |
| over the wet one | 21 % → 24 % | 24.7 px | 0.16 | 1.15 | 57 |
| long, no reload | 51 % → 54 % | 23.0 px | 0.14 | 1.04 | 338 | quarters: 0.11 → 0.09 → 0.07 → 0.06

Numbers say: light vs heavy: width 16.7 → 31.5 px, dark 0.16 → 0.16; wet paint spreads well beyond the stroke.

## Brush Artist · Gouache
Gouache · 30 px · 29.1 s

![Brush Artist · Gouache](Brush-Artist-Gouache.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 8 % → 8 % | 24.4 px | 0.27 | 0.97 | 70 |
| heavy line | 15 % → 11 % | 42.8 px | 0.27 | 0.78 | 86 |
| pressure swell | 11 % → 9 % | 41.0 px | 0.27 | 0.84 | 55 |
| fast wave | 30 % → 13 % | 34.4 px | 0.26 | 0.45 | 186 |
| slow wave | 29 % → 14 % | 33.9 px | 0.26 | 0.46 | 323 |
| spiral | 40 % → 14 % | 26.6 px | 0.26 | 0.35 | 304 |
| loop | 23 % → 15 % | 30.4 px | 0.26 | 0.62 | 161 |
| tilted | 10 % → 10 % | 27.1 px | 0.26 | 1.01 | 88 |
| over the wet one | 21 % → 19 % | 32.8 px | 0.26 | 0.89 | 77 |
| long, no reload | 43 % → 15 % | 19.1 px | 0.26 | 0.35 | 457 | quarters: 0.01 → 0.01 → 0.01 → 0.01

Numbers say: light vs heavy: width 24.4 → 42.8 px, dark 0.27 → 0.27; the long stroke does not run out of paint.

## Brush Artist · Oil — bristle
Oil · 30 px · 18.0 s

![Brush Artist · Oil — bristle](Brush-Artist-Oil-bristle.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 9 % → 9 % | 26.2 px | 0.54 | 1.00 | 92 |
| heavy line | 10 % → 10 % | 28.5 px | 0.54 | 1.00 | 110 |
| pressure swell | 8 % → 8 % | 28.2 px | 0.55 | 1.00 | 70 |
| fast wave | 24 % → 24 % | 27.3 px | 0.55 | 1.00 | 316 |
| slow wave | 24 % → 24 % | 28.2 px | 0.55 | 1.00 | 463 |
| spiral | 39 % → 39 % | 25.6 px | 0.54 | 1.00 | 459 |
| loop | 20 % → 20 % | 26.2 px | 0.54 | 1.00 | 228 |
| tilted | 11 % → 11 % | 29.9 px | 0.54 | 1.00 | 150 |
| over the wet one | 20 % → 20 % | 25.2 px | 0.54 | 1.00 | 104 |
| long, no reload | 50 % → 50 % | 22.4 px | 0.54 | 1.00 | 663 | quarters: 0.32 → 0.30 → 0.29 → 0.28

Numbers say: light vs heavy: width 26.2 → 28.5 px, dark 0.54 → 0.54; pressure barely changes the width; the long stroke does not run out of paint.

## Brush Artist · Charcoal — stick
Charcoal · 28 px · 9.4 s

![Brush Artist · Charcoal — stick](Brush-Artist-Charcoal-stick.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 3 % → 3 % | 8.4 px | 0.85 | 1.00 | 23 |
| heavy line | 6 % → 6 % | 17.8 px | 0.85 | 1.00 | 24 |
| pressure swell | 4 % → 4 % | 13.9 px | 0.85 | 1.00 | 12 |
| fast wave | 12 % → 12 % | 14.0 px | 0.85 | 1.00 | 46 |
| slow wave | 11 % → 11 % | 12.5 px | 0.85 | 1.00 | 77 |
| spiral | 19 % → 19 % | 12.7 px | 0.85 | 1.00 | 79 |
| loop | 10 % → 10 % | 12.8 px | 0.85 | 1.00 | 39 |
| tilted | 4 % → 4 % | 10.9 px | 0.85 | 1.00 | 27 |
| over the wet one | 9 % → 9 % | 13.5 px | 0.85 | 1.00 | 15 |
| long, no reload | 27 % → 27 % | 12.2 px | 0.85 | 1.00 | 101 | quarters: 0.26 → 0.25 → 0.26 → 0.27

Numbers say: light vs heavy: width 8.4 → 17.8 px, dark 0.85 → 0.85; the long stroke does not run out of paint.

## Brush Artist · Charcoal — stick B
Charcoal · 36 px · 9.5 s

![Brush Artist · Charcoal — stick B](Brush-Artist-Charcoal-stick-B.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 4 % → 4 % | 10.5 px | 0.85 | 1.00 | 23 |
| heavy line | 7 % → 7 % | 21.1 px | 0.85 | 1.00 | 29 |
| pressure swell | 4 % → 4 % | 16.5 px | 0.85 | 1.00 | 25 |
| fast wave | 15 % → 15 % | 16.8 px | 0.85 | 1.00 | 65 |
| slow wave | 13 % → 13 % | 14.7 px | 0.85 | 1.00 | 103 |
| spiral | 23 % → 23 % | 15.0 px | 0.85 | 1.00 | 113 |
| loop | 11 % → 11 % | 14.8 px | 0.85 | 1.00 | 58 |
| tilted | 4 % → 4 % | 12.3 px | 0.85 | 1.00 | 35 |
| over the wet one | 10 % → 10 % | 15.9 px | 0.85 | 1.00 | 24 |
| long, no reload | 31 % → 31 % | 13.9 px | 0.85 | 1.00 | 147 | quarters: 0.30 → 0.28 → 0.29 → 0.30

Numbers say: light vs heavy: width 10.5 → 21.1 px, dark 0.85 → 0.85; the long stroke does not run out of paint.

## Brush Artist · Charcoal — stick C
Charcoal · 22 px · 9.1 s

![Brush Artist · Charcoal — stick C](Brush-Artist-Charcoal-stick-C.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 2 % → 2 % | 6.9 px | 0.85 | 1.00 | 14 |
| heavy line | 5 % → 5 % | 15.3 px | 0.85 | 1.00 | 11 |
| pressure swell | 3 % → 3 % | 12.2 px | 0.85 | 1.00 | 8 |
| fast wave | 10 % → 10 % | 12.1 px | 0.85 | 1.00 | 38 |
| slow wave | 9 % → 9 % | 10.8 px | 0.85 | 1.00 | 65 |
| spiral | 17 % → 17 % | 11.0 px | 0.85 | 1.00 | 70 |
| loop | 9 % → 9 % | 11.4 px | 0.85 | 1.00 | 37 |
| tilted | 4 % → 4 % | 9.9 px | 0.85 | 1.00 | 25 |
| over the wet one | 8 % → 8 % | 11.7 px | 0.85 | 1.00 | 12 |
| long, no reload | 24 % → 24 % | 11.0 px | 0.85 | 1.00 | 106 | quarters: 0.24 → 0.22 → 0.23 → 0.24

Numbers say: light vs heavy: width 6.9 → 15.3 px, dark 0.85 → 0.85; the long stroke does not run out of paint.

## Brush Artist · Refs · #01 Henry Ward peach cloud — own sheet
own sheet 600 × 600 · Gouache · 44 px · 69.0 s

![Brush Artist · Refs · #01 Henry Ward peach cloud — own sheet](Brush-Artist-Refs-01-Henry-Ward-peach-cloud-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 99 % → 99 % | 62.0 px | 0.04 | 1.00 | 855 |
| stroke 2 | 100 % → 99 % | 88.9 px | 0.12 | 0.99 | 973 |
| stroke 3 | 99 % → 99 % | 88.0 px | 0.15 | 1.00 | 984 |
| stroke 4 | 100 % → 99 % | 85.6 px | 0.08 | 0.99 | 1030 |
| stroke 5 | 99 % → 98 % | 88.6 px | 0.04 | 0.99 | 973 |
| stroke 6 | 100 % → 99 % | 87.2 px | 0.04 | 0.99 | 943 |
| stroke 7 | 99 % → 99 % | 90.9 px | 0.03 | 1.00 | 973 |
| stroke 8 | 100 % → 98 % | 88.7 px | 0.02 | 0.99 | 959 |
| stroke 9 | 100 % → 98 % | 60.0 px | 0.00 | 0.98 | 776 |
| stroke 10 | 100 % → 100 % | 129.9 px | 0.06 | 1.00 | 159 |
| stroke 11 | 100 % → 100 % | 160.5 px | 0.09 | 1.00 | 159 |
| stroke 12 | 100 % → 100 % | 131.4 px | 0.10 | 1.00 | 155 |
| stroke 13 | 100 % → 100 % | 162.0 px | 0.09 | 1.00 | 151 |
| stroke 14 | 100 % → 100 % | 135.7 px | 0.11 | 1.00 | 146 |
| stroke 15 | 100 % → 100 % | 148.2 px | 0.08 | 1.00 | 152 |
| stroke 16 | 100 % → 100 % | 138.8 px | 0.12 | 1.00 | 148 |
| stroke 17 | 100 % → 100 % | 129.3 px | 0.13 | 1.00 | 195 |
| stroke 18 | 100 % → 100 % | 124.6 px | 0.14 | 1.00 | 164 |
| stroke 19 | 100 % → 100 % | 125.6 px | 0.15 | 1.00 | 188 |
| stroke 20 | 100 % → 100 % | 137.3 px | 0.16 | 1.00 | 190 |
| stroke 21 | 100 % → 100 % | 136.3 px | 0.19 | 1.00 | 165 |
| stroke 22 | 100 % → 100 % | 132.5 px | 0.20 | 1.00 | 172 |
| stroke 23 | 100 % → 100 % | 129.7 px | 0.20 | 1.00 | 195 |
| stroke 24 | 100 % → 100 % | 135.8 px | 0.19 | 1.00 | 170 |
| stroke 25 | 100 % → 100 % | 140.2 px | 0.20 | 1.00 | 173 |
| stroke 26 | 100 % → 100 % | 124.0 px | 0.19 | 1.00 | 190 |
| stroke 27 | 100 % → 100 % | 131.8 px | 0.19 | 1.00 | 186 |
| stroke 28 | 100 % → 100 % | 124.2 px | 0.19 | 1.00 | 164 |
| stroke 29 | 100 % → 100 % | 131.9 px | 0.18 | 1.00 | 184 |
| stroke 30 | 100 % → 100 % | 134.2 px | 0.17 | 1.00 | 182 |
| stroke 31 | 100 % → 100 % | 134.5 px | 0.17 | 1.00 | 192 |
| stroke 32 | 100 % → 100 % | 127.6 px | 0.15 | 1.00 | 190 |
| stroke 33 | 100 % → 100 % | 134.4 px | 0.16 | 1.00 | 177 |

## Brush Artist · Refs · #02 Henry Ward cream strokes — own sheet
own sheet 600 × 600 · Gouache · 46 px · 61.2 s

![Brush Artist · Refs · #02 Henry Ward cream strokes — own sheet](Brush-Artist-Refs-02-Henry-Ward-cream-strokes-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 95 % → 99 % | 58.8 px | 0.03 | 1.04 | 818 |
| stroke 2 | 99 % → 99 % | 91.6 px | 0.05 | 1.00 | 1034 |
| stroke 3 | 98 % → 99 % | 89.0 px | 0.04 | 1.01 | 1063 |
| stroke 4 | 95 % → 99 % | 89.9 px | 0.04 | 1.04 | 1031 |
| stroke 5 | 98 % → 99 % | 90.2 px | 0.06 | 1.00 | 989 |
| stroke 6 | 100 % → 99 % | 89.6 px | 0.03 | 1.00 | 992 |
| stroke 7 | 99 % → 99 % | 93.0 px | 0.04 | 1.00 | 981 |
| stroke 8 | 98 % → 99 % | 92.0 px | 0.00 | 1.00 | 993 |
| stroke 9 | 100 % → 99 % | 61.8 px | 0.00 | 0.99 | 756 |
| stroke 10 | 100 % → 99 % | 129.9 px | 0.03 | 0.99 | 260 |
| stroke 11 | 100 % → 99 % | 142.3 px | 0.03 | 0.99 | 248 |
| stroke 12 | 100 % → 100 % | 138.5 px | 0.04 | 1.00 | 237 |
| stroke 13 | 100 % → 99 % | 137.9 px | 0.06 | 0.99 | 221 |
| stroke 14 | 100 % → 98 % | 129.1 px | 0.05 | 0.99 | 237 |
| stroke 15 | 100 % → 100 % | 121.4 px | 0.04 | 1.00 | 240 |
| stroke 16 | 100 % → 100 % | 128.5 px | 0.04 | 1.00 | 215 |

## Brush Artist · Refs · #03 Henry Ward navy contours — own sheet
own sheet 600 × 600 · Heavy acrylic · 22 px · 2.5 s

![Brush Artist · Refs · #03 Henry Ward navy contours — own sheet](Brush-Artist-Refs-03-Henry-Ward-navy-contours-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 15 % → 20 % | 23.1 px | 0.69 | 1.28 | 122 |
| stroke 2 | 28 % → 30 % | 26.3 px | 0.69 | 1.09 | 99 |
| stroke 3 | 28 % → 28 % | 29.4 px | 0.70 | 0.99 | 113 |
| stroke 4 | 26 % → 24 % | 45.9 px | 0.69 | 0.92 | 126 |

## Brush Artist · Refs · #04 Henry Ward grey cloud — own sheet
own sheet 600 × 600 · Gouache · 50 px · 13.3 s

![Brush Artist · Refs · #04 Henry Ward grey cloud — own sheet](Brush-Artist-Refs-04-Henry-Ward-grey-cloud-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 33 % → 59 % | 49.5 px | 0.40 | 1.81 | 227 |
| stroke 2 | 38 % → 64 % | 58.2 px | 0.40 | 1.68 | 218 |
| stroke 3 | 59 % → 82 % | 81.0 px | 0.40 | 1.39 | 215 |
| stroke 4 | 58 % → 83 % | 87.5 px | 0.40 | 1.41 | 227 |
| stroke 5 | 61 % → 86 % | 90.7 px | 0.40 | 1.41 | 215 |
| stroke 6 | 61 % → 89 % | 98.2 px | 0.40 | 1.45 | 224 |
| stroke 7 | 60 % → 84 % | 88.7 px | 0.40 | 1.39 | 216 |
| stroke 8 | 57 % → 84 % | 85.9 px | 0.40 | 1.48 | 216 |
| stroke 9 | 60 % → 86 % | 88.9 px | 0.40 | 1.44 | 198 |
| stroke 10 | 61 % → 88 % | 98.3 px | 0.40 | 1.44 | 213 |
| stroke 11 | 61 % → 86 % | 83.2 px | 0.40 | 1.40 | 221 |
| stroke 12 | 62 % → 86 % | 94.7 px | 0.40 | 1.38 | 216 |
| stroke 13 | 62 % → 86 % | 84.6 px | 0.40 | 1.39 | 204 |
| stroke 14 | 60 % → 84 % | 93.4 px | 0.40 | 1.39 | 202 |
| stroke 15 | 60 % → 83 % | 88.4 px | 0.40 | 1.38 | 224 |
| stroke 16 | 61 % → 84 % | 96.2 px | 0.40 | 1.38 | 203 |
| stroke 17 | 60 % → 84 % | 84.0 px | 0.40 | 1.41 | 212 |
| stroke 18 | 61 % → 84 % | 96.8 px | 0.40 | 1.39 | 204 |
| stroke 19 | 60 % → 62 % | 89.9 px | 0.40 | 1.03 | 212 |
| stroke 20 | 61 % → 61 % | 99.6 px | 0.40 | 0.99 | 203 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #05 Henry Ward green in rust loops — own sheet
own sheet 600 × 600 · Heavy acrylic · 20 px · 2.2 s

![Brush Artist · Refs · #05 Henry Ward green in rust loops — own sheet](Brush-Artist-Refs-05-Henry-Ward-green-in-rust-loops-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 16 % → 24 % | 20.9 px | 0.02 | 1.48 | 120 |
| stroke 2 | 15 % → 13 % | 22.7 px | 0.03 | 0.90 | 150 |
| stroke 3 | 25 % → 24 % | 37.1 px | 0.02 | 0.94 | 135 |

## Brush Artist · Refs · #06 Henry Ward scrubbed grey — own sheet
own sheet 600 × 600 · Gouache · 50 px · 14.7 s

![Brush Artist · Refs · #06 Henry Ward scrubbed grey — own sheet](Brush-Artist-Refs-06-Henry-Ward-scrubbed-grey-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 35 % → 59 % | 49.2 px | 0.40 | 1.71 | 213 |
| stroke 2 | 41 % → 66 % | 64.6 px | 0.40 | 1.58 | 221 |
| stroke 3 | 59 % → 89 % | 86.2 px | 0.40 | 1.51 | 197 |
| stroke 4 | 58 % → 88 % | 92.9 px | 0.40 | 1.51 | 219 |
| stroke 5 | 56 % → 86 % | 84.4 px | 0.40 | 1.53 | 211 |
| stroke 6 | 60 % → 86 % | 93.2 px | 0.40 | 1.44 | 207 |
| stroke 7 | 61 % → 85 % | 88.7 px | 0.40 | 1.38 | 213 |
| stroke 8 | 62 % → 88 % | 98.2 px | 0.40 | 1.43 | 222 |
| stroke 9 | 61 % → 89 % | 88.8 px | 0.40 | 1.46 | 206 |
| stroke 10 | 59 % → 89 % | 95.5 px | 0.40 | 1.50 | 205 |
| stroke 11 | 60 % → 84 % | 85.9 px | 0.40 | 1.42 | 213 |
| stroke 12 | 58 % → 83 % | 93.4 px | 0.40 | 1.43 | 316 |
| stroke 13 | 58 % → 83 % | 83.2 px | 0.40 | 1.44 | 216 |
| stroke 14 | 56 % → 84 % | 84.9 px | 0.40 | 1.49 | 205 |
| stroke 15 | 58 % → 85 % | 83.3 px | 0.40 | 1.46 | 214 |
| stroke 16 | 63 % → 90 % | 96.7 px | 0.40 | 1.44 | 199 |
| stroke 17 | 61 % → 86 % | 88.7 px | 0.40 | 1.42 | 205 |
| stroke 18 | 61 % → 85 % | 95.6 px | 0.40 | 1.39 | 199 |
| stroke 19 | 57 % → 85 % | 87.0 px | 0.40 | 1.49 | 222 |
| stroke 20 | 58 % → 84 % | 93.6 px | 0.40 | 1.45 | 226 |
| stroke 21 | 58 % → 68 % | 84.6 px | 0.40 | 1.17 | 211 |
| stroke 22 | 62 % → 61 % | 98.3 px | 0.40 | 0.99 | 191 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #07 Henry Ward blue L + black zigzag — own sheet
own sheet 600 × 600 · Heavy acrylic · 34 px · 1.9 s

![Brush Artist · Refs · #07 Henry Ward blue L + black zigzag — own sheet](Brush-Artist-Refs-07-Henry-Ward-blue-L-black-zigzag-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 30 % → 31 % | 35.6 px | 0.59 | 1.05 | 107 |
| stroke 2 | 31 % → 29 % | 38.6 px | 0.59 | 0.94 | 85 |

## Brush Artist · Refs · #08 Henry Ward olive bands — own sheet
own sheet 600 × 600 · Gouache · 34 px · 5.1 s

![Brush Artist · Refs · #08 Henry Ward olive bands — own sheet](Brush-Artist-Refs-08-Henry-Ward-olive-bands-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 33 % → 19 % | 32.3 px | 0.57 | 0.58 | 147 |
| stroke 2 | 37 % → 20 % | 44.3 px | 0.57 | 0.53 | 155 |
| stroke 3 | 30 % → 23 % | 32.4 px | 0.57 | 0.75 | 155 |
| stroke 4 | 38 % → 37 % | 44.3 px | 0.57 | 0.98 | 173 |
| stroke 5 | 50 % → 35 % | 52.4 px | 0.57 | 0.71 | 165 |
| stroke 6 | 36 % → 22 % | 32.2 px | 0.57 | 0.61 | 149 |

## Brush Artist · Refs · #09 Henry Ward white loops — own sheet
own sheet 600 × 600 · Gouache · 46 px · 59.9 s

![Brush Artist · Refs · #09 Henry Ward white loops — own sheet](Brush-Artist-Refs-09-Henry-Ward-white-loops-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 96 % → 99 % | 59.1 px | 0.01 | 1.03 | 750 |
| stroke 2 | 99 % → 100 % | 91.6 px | 0.01 | 1.01 | 946 |
| stroke 3 | 97 % → 99 % | 89.3 px | 0.01 | 1.02 | 943 |
| stroke 4 | 99 % → 99 % | 90.3 px | 0.02 | 1.00 | 942 |
| stroke 5 | 97 % → 99 % | 89.4 px | 0.02 | 1.02 | 949 |
| stroke 6 | 95 % → 99 % | 90.2 px | 0.03 | 1.05 | 922 |
| stroke 7 | 99 % → 99 % | 92.7 px | 0.02 | 1.00 | 937 |
| stroke 8 | 98 % → 99 % | 92.0 px | 0.01 | 1.01 | 956 |
| stroke 9 | 100 % → 99 % | 64.4 px | 0.01 | 0.99 | 789 |
| stroke 10 | 100 % → 100 % | 31.6 px | 0.02 | 1.00 | 1091 |
| stroke 11 | 100 % → 100 % | 70.2 px | 0.02 | 1.00 | 1147 |
| stroke 12 | 100 % → 100 % | 58.2 px | 0.03 | 1.00 | 993 |

## Brush Artist · Refs · #10 Henry Ward maroon loops — own sheet
own sheet 600 × 600 · Heavy acrylic · 30 px · 2.9 s

![Brush Artist · Refs · #10 Henry Ward maroon loops — own sheet](Brush-Artist-Refs-10-Henry-Ward-maroon-loops-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 16 % → 33 % | 28.6 px | 0.72 | 2.07 | 197 |
| stroke 2 | 29 % → 47 % | 46.0 px | 0.72 | 1.60 | 121 |
| stroke 3 | 40 % → 50 % | 54.7 px | 0.72 | 1.24 | 158 |
| stroke 4 | 45 % → 43 % | 64.1 px | 0.72 | 0.96 | 104 |
| stroke 5 | 41 % → 38 % | 70.6 px | 0.72 | 0.93 | 130 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #11 Henry Ward purple spun balls — own sheet
own sheet 600 × 600 · Heavy acrylic · 36 px · 58.8 s

![Brush Artist · Refs · #11 Henry Ward purple spun balls — own sheet](Brush-Artist-Refs-11-Henry-Ward-purple-spun-balls-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 100 % → 99 % | 54.7 px | 0.01 | 0.99 | 813 |
| stroke 2 | 100 % → 99 % | 73.2 px | 0.01 | 0.99 | 1000 |
| stroke 3 | 100 % → 99 % | 77.6 px | 0.01 | 0.99 | 1000 |
| stroke 4 | 100 % → 100 % | 75.0 px | 0.01 | 1.00 | 1000 |
| stroke 5 | 100 % → 99 % | 75.9 px | 0.01 | 0.99 | 1013 |
| stroke 6 | 100 % → 99 % | 76.8 px | 0.08 | 0.99 | 988 |
| stroke 7 | 100 % → 99 % | 75.0 px | 0.26 | 0.99 | 997 |
| stroke 8 | 100 % → 99 % | 75.9 px | 0.30 | 0.99 | 976 |
| stroke 9 | 100 % → 99 % | 55.6 px | 0.04 | 0.99 | 839 |
| stroke 10 | 100 % → 100 % | 49.5 px | 0.28 | 1.00 | 374 |
| stroke 11 | 100 % → 100 % | 48.8 px | 0.34 | 1.00 | 367 |
| stroke 12 | 100 % → 100 % | 48.7 px | 0.30 | 1.00 | 373 |

## Brush Artist · Refs · #12 Henry Ward black-olive cage — own sheet
own sheet 600 × 600 · Gouache · 28 px · 5.2 s

![Brush Artist · Refs · #12 Henry Ward black-olive cage — own sheet](Brush-Artist-Refs-12-Henry-Ward-black-olive-cage-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 18 % → 22 % | 24.3 px | 0.59 | 1.24 | 188 |
| stroke 2 | 16 % → 26 % | 27.7 px | 0.59 | 1.61 | 166 |
| stroke 3 | 34 % → 34 % | 40.4 px | 0.59 | 1.01 | 214 |
| stroke 4 | 34 % → 34 % | 42.8 px | 0.59 | 1.03 | 122 |
| stroke 5 | 34 % → 21 % | 43.1 px | 0.59 | 0.60 | 122 |
| stroke 6 | 52 % → 37 % | 67.3 px | 0.59 | 0.72 | 153 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #13 Henry Ward blue streaky form — own sheet
own sheet 600 × 600 · Gouache · 50 px · 14.1 s

![Brush Artist · Refs · #13 Henry Ward blue streaky form — own sheet](Brush-Artist-Refs-13-Henry-Ward-blue-streaky-form-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 34 % → 64 % | 49.1 px | 0.05 | 1.86 | 211 |
| stroke 2 | 42 % → 66 % | 67.5 px | 0.05 | 1.58 | 215 |
| stroke 3 | 60 % → 86 % | 85.2 px | 0.05 | 1.43 | 215 |
| stroke 4 | 60 % → 89 % | 97.8 px | 0.06 | 1.49 | 204 |
| stroke 5 | 61 % → 86 % | 86.7 px | 0.06 | 1.42 | 210 |
| stroke 6 | 56 % → 82 % | 86.1 px | 0.06 | 1.47 | 233 |
| stroke 7 | 62 % → 85 % | 92.3 px | 0.05 | 1.38 | 218 |
| stroke 8 | 62 % → 85 % | 96.3 px | 0.06 | 1.37 | 212 |
| stroke 9 | 62 % → 87 % | 94.7 px | 0.05 | 1.41 | 206 |
| stroke 10 | 63 % → 89 % | 102.4 px | 0.05 | 1.40 | 195 |
| stroke 11 | 58 % → 86 % | 87.3 px | 0.06 | 1.48 | 201 |
| stroke 12 | 58 % → 82 % | 91.0 px | 0.05 | 1.42 | 227 |
| stroke 13 | 61 % → 88 % | 89.4 px | 0.06 | 1.44 | 194 |
| stroke 14 | 54 % → 82 % | 83.9 px | 0.06 | 1.53 | 211 |
| stroke 15 | 57 % → 83 % | 82.3 px | 0.06 | 1.45 | 217 |
| stroke 16 | 56 % → 84 % | 90.5 px | 0.06 | 1.51 | 200 |
| stroke 17 | 61 % → 84 % | 93.7 px | 0.06 | 1.39 | 210 |
| stroke 18 | 61 % → 82 % | 95.3 px | 0.06 | 1.35 | 216 |
| stroke 19 | 68 % → 80 % | 84.6 px | 0.06 | 1.18 | 221 |
| stroke 20 | 78 % → 77 % | 93.1 px | 0.06 | 0.99 | 218 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #14 Henry Ward olive totem — own sheet
own sheet 600 × 600 · Heavy acrylic · 48 px · 6.4 s

![Brush Artist · Refs · #14 Henry Ward olive totem — own sheet](Brush-Artist-Refs-14-Henry-Ward-olive-totem-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 31 % → 50 % | 46.9 px | 0.38 | 1.58 | 131 |
| stroke 2 | 36 % → 62 % | 64.3 px | 0.38 | 1.71 | 122 |
| stroke 3 | 54 % → 76 % | 79.7 px | 0.38 | 1.42 | 112 |
| stroke 4 | 50 % → 73 % | 88.4 px | 0.38 | 1.46 | 127 |
| stroke 5 | 56 % → 78 % | 83.2 px | 0.38 | 1.39 | 115 |
| stroke 6 | 54 % → 81 % | 96.5 px | 0.38 | 1.50 | 132 |
| stroke 7 | 52 % → 75 % | 74.2 px | 0.38 | 1.45 | 115 |
| stroke 8 | 51 % → 77 % | 90.4 px | 0.38 | 1.53 | 117 |
| stroke 9 | 56 % → 81 % | 82.9 px | 0.38 | 1.44 | 116 |
| stroke 10 | 56 % → 78 % | 94.7 px | 0.38 | 1.40 | 122 |
| stroke 11 | 57 % → 79 % | 90.0 px | 0.38 | 1.38 | 113 |
| stroke 12 | 53 % → 80 % | 90.4 px | 0.38 | 1.53 | 119 |
| stroke 13 | 55 % → 83 % | 82.0 px | 0.38 | 1.51 | 106 |
| stroke 14 | 52 % → 76 % | 86.9 px | 0.38 | 1.48 | 133 |
| stroke 15 | 58 % → 82 % | 85.5 px | 0.38 | 1.41 | 121 |
| stroke 16 | 54 % → 80 % | 89.8 px | 0.38 | 1.47 | 131 |
| stroke 17 | 53 % → 78 % | 77.7 px | 0.38 | 1.45 | 131 |
| stroke 18 | 57 % → 84 % | 100.3 px | 0.38 | 1.47 | 131 |
| stroke 19 | 57 % → 80 % | 86.5 px | 0.38 | 1.41 | 118 |
| stroke 20 | 55 % → 76 % | 95.2 px | 0.38 | 1.40 | 142 |
| stroke 21 | 52 % → 67 % | 83.7 px | 0.37 | 1.30 | 121 |
| stroke 22 | 60 % → 59 % | 94.0 px | 0.37 | 0.98 | 120 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #15 Ultramarine brush script — own sheet
own sheet 600 × 600 · Ink · 10 px · 9.1 s

![Brush Artist · Refs · #15 Ultramarine brush script — own sheet](Brush-Artist-Refs-15-Ultramarine-brush-script-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 69 % → 72 % | 17.0 px | 0.75 | 1.05 | 63 |
| stroke 2 | 70 % → 72 % | 16.6 px | 0.73 | 1.04 | 71 |
| stroke 3 | 70 % → 74 % | 17.4 px | 0.74 | 1.05 | 62 |
| stroke 4 | 71 % → 72 % | 16.3 px | 0.71 | 1.01 | 91 |
| stroke 5 | 66 % → 69 % | 15.7 px | 0.71 | 1.04 | 99 |
| stroke 6 | 67 % → 71 % | 18.5 px | 0.75 | 1.05 | 56 |
| stroke 7 | 69 % → 71 % | 15.9 px | 0.72 | 1.04 | 86 |
| stroke 8 | 69 % → 71 % | 17.6 px | 0.74 | 1.02 | 70 |
| stroke 9 | 67 % → 70 % | 16.5 px | 0.73 | 1.05 | 76 |
| stroke 10 | 65 % → 69 % | 17.1 px | 0.74 | 1.05 | 67 |
| stroke 11 | 72 % → 75 % | 17.5 px | 0.74 | 1.04 | 72 |
| stroke 12 | 68 % → 69 % | 15.8 px | 0.72 | 1.01 | 99 |
| stroke 13 | 66 % → 69 % | 15.7 px | 0.72 | 1.04 | 97 |
| stroke 14 | 67 % → 71 % | 18.2 px | 0.75 | 1.05 | 45 |
| stroke 15 | 69 % → 73 % | 18.8 px | 0.76 | 1.05 | 43 |
| stroke 16 | 68 % → 72 % | 17.4 px | 0.75 | 1.04 | 61 |
| stroke 17 | 68 % → 69 % | 18.1 px | 0.75 | 1.02 | 48 |
| stroke 18 | 68 % → 71 % | 17.2 px | 0.75 | 1.05 | 88 |
| stroke 19 | 66 % → 71 % | 18.9 px | 0.76 | 1.07 | 56 |
| stroke 20 | 68 % → 72 % | 18.8 px | 0.76 | 1.06 | 47 |
| stroke 21 | 70 % → 73 % | 16.0 px | 0.71 | 1.03 | 107 |
| stroke 22 | 77 % → 79 % | 12.6 px | 0.75 | 1.02 | 163 |
| stroke 23 | 67 % → 71 % | 16.9 px | 0.74 | 1.05 | 66 |
| stroke 24 | 66 % → 69 % | 17.9 px | 0.76 | 1.05 | 50 |
| stroke 25 | 69 % → 72 % | 16.5 px | 0.73 | 1.04 | 87 |
| stroke 26 | 70 % → 71 % | 15.8 px | 0.70 | 1.01 | 100 |

## Brush Artist · Refs · #18 Blue oil-stick scribbles — own sheet
own sheet 600 × 600 · Pastel · 10 px · 2.8 s

![Brush Artist · Refs · #18 Blue oil-stick scribbles — own sheet](Brush-Artist-Refs-18-Blue-oil-stick-scribbles-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 18 % → 37 % | 3.8 px | 0.49 | 2.02 | 130 |
| stroke 2 | 16 % → 40 % | 3.6 px | 0.49 | 2.52 | 121 |
| stroke 3 | 18 % → 29 % | 5.8 px | 0.49 | 1.59 | 164 |
| stroke 4 | 17 % → 32 % | 7.8 px | 0.49 | 1.90 | 161 |
| stroke 5 | 32 % → 37 % | 7.8 px | 0.49 | 1.15 | 138 |
| stroke 6 | 30 % → 30 % | 9.2 px | 0.49 | 1.02 | 116 |
| stroke 7 | 28 % → 35 % | 7.5 px | 0.49 | 1.26 | 127 |
| stroke 8 | 33 % → 33 % | 16.3 px | 0.49 | 1.00 | 143 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #20 Orange-red crayon scribble — own sheet
own sheet 600 × 600 · Pastel · 14 px · 2.5 s

![Brush Artist · Refs · #20 Orange-red crayon scribble — own sheet](Brush-Artist-Refs-20-Orange-red-crayon-scribble-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 9 % → 20 % | 5.5 px | 0.59 | 2.30 | 157 |
| stroke 2 | 10 % → 25 % | 6.5 px | 0.59 | 2.49 | 145 |
| stroke 3 | 15 % → 25 % | 8.3 px | 0.59 | 1.61 | 137 |
| stroke 4 | 28 % → 35 % | 8.3 px | 0.59 | 1.25 | 146 |
| stroke 5 | 32 % → 32 % | 7.0 px | 0.59 | 1.00 | 141 |
| stroke 6 | 24 % → 24 % | 16.1 px | 0.59 | 1.00 | 161 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #21 Gritty black contours — own sheet
own sheet 600 × 600 · Gouache · 12 px · 58.3 s

![Brush Artist · Refs · #21 Gritty black contours — own sheet](Brush-Artist-Refs-21-Gritty-black-contours-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 100 % → 98 % | 31.8 px | 0.00 | 0.98 | 740 |
| stroke 2 | 100 % → 98 % | 33.5 px | 0.00 | 0.98 | 942 |
| stroke 3 | 100 % → 99 % | 32.6 px | 0.00 | 0.99 | 988 |
| stroke 4 | 100 % → 99 % | 31.8 px | 0.01 | 0.99 | 964 |
| stroke 5 | 100 % → 98 % | 30.9 px | 0.04 | 0.98 | 925 |
| stroke 6 | 100 % → 99 % | 34.4 px | 0.06 | 0.99 | 944 |
| stroke 7 | 100 % → 99 % | 35.3 px | 0.03 | 0.99 | 949 |
| stroke 8 | 100 % → 98 % | 34.4 px | 0.02 | 0.98 | 950 |
| stroke 9 | 100 % → 98 % | 30.0 px | 0.00 | 0.98 | 783 |
| stroke 10 | 100 % → 100 % | 89.0 px | 0.07 | 1.00 | 160 |
| stroke 11 | 100 % → 100 % | 139.6 px | 0.04 | 1.00 | 179 |
| stroke 12 | 100 % → 100 % | 68.3 px | 0.07 | 1.00 | 130 |
| stroke 13 | 100 % → 100 % | 97.7 px | 0.07 | 1.00 | 145 |
| stroke 14 | 100 % → 100 % | 93.8 px | 0.06 | 1.00 | 90 |

## Brush Artist · Refs · #22 Bold black brush poster — own sheet
own sheet 600 × 600 · Ink · 20 px · 4.6 s

![Brush Artist · Refs · #22 Bold black brush poster — own sheet](Brush-Artist-Refs-22-Bold-black-brush-poster-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 34 % → 37 % | 36.3 px | 0.94 | 1.10 | 97 |
| stroke 2 | 55 % → 66 % | 36.9 px | 0.95 | 1.21 | 23 |
| stroke 3 | 49 % → 49 % | 40.5 px | 0.94 | 1.00 | 42 |
| stroke 4 | 36 % → 43 % | 45.3 px | 0.94 | 1.20 | 51 |
| stroke 5 | 35 % → 35 % | 40.5 px | 0.94 | 1.00 | 85 |

## Brush Artist · Refs · #23 Dry white on orange + black line — own sheet
own sheet 600 × 600 · Gouache · 50 px · 61.8 s

![Brush Artist · Refs · #23 Dry white on orange + black line — own sheet](Brush-Artist-Refs-23-Dry-white-on-orange-black-line-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 89 % → 99 % | 61.2 px | 0.00 | 1.12 | 899 |
| stroke 2 | 96 % → 99 % | 94.7 px | 0.01 | 1.04 | 980 |
| stroke 3 | 92 % → 99 % | 93.5 px | 0.02 | 1.08 | 937 |
| stroke 4 | 95 % → 99 % | 97.2 px | 0.01 | 1.04 | 929 |
| stroke 5 | 95 % → 99 % | 93.7 px | 0.02 | 1.04 | 900 |
| stroke 6 | 95 % → 99 % | 95.7 px | 0.02 | 1.04 | 913 |
| stroke 7 | 96 % → 99 % | 93.4 px | 0.02 | 1.03 | 948 |
| stroke 8 | 95 % → 99 % | 92.6 px | 0.01 | 1.05 | 939 |
| stroke 9 | 100 % → 99 % | 67.9 px | 0.00 | 0.99 | 805 |
| stroke 10 | 100 % → 100 % | 167.5 px | 0.02 | 1.00 | 190 |
| stroke 11 | 100 % → 100 % | 173.3 px | 0.02 | 1.00 | 176 |
| stroke 12 | 100 % → 100 % | 162.3 px | 0.03 | 1.00 | 164 |
| stroke 13 | 100 % → 100 % | 183.6 px | 0.03 | 1.00 | 173 |
| stroke 14 | 100 % → 100 % | 154.9 px | 0.02 | 1.00 | 161 |
| stroke 15 | 100 % → 100 % | 190.8 px | 0.02 | 1.00 | 167 |
| stroke 16 | 100 % → 100 % | 169.8 px | 0.02 | 1.00 | 161 |
| stroke 17 | 100 % → 100 % | 180.0 px | 0.02 | 1.00 | 185 |
| stroke 18 | 100 % → 100 % | 163.5 px | 0.02 | 1.00 | 179 |
| stroke 19 | 100 % → 100 % | 178.5 px | 0.03 | 1.00 | 172 |
| stroke 20 | 100 % → 100 % | 164.4 px | 0.03 | 1.00 | 169 |
| stroke 21 | 100 % → 100 % | 180.5 px | 0.02 | 1.00 | 176 |
| stroke 22 | 100 % → 100 % | 161.8 px | 0.02 | 1.00 | 182 |
| stroke 23 | 100 % → 100 % | 185.9 px | 0.02 | 1.00 | 193 |
| stroke 24 | 100 % → 100 % | 161.8 px | 0.02 | 1.00 | 158 |
| stroke 25 | 100 % → 100 % | 185.5 px | 0.02 | 1.00 | 170 |
| stroke 26 | 100 % → 100 % | 165.8 px | 0.02 | 1.00 | 180 |
| stroke 27 | 100 % → 100 % | 185.6 px | 0.02 | 1.00 | 191 |

## Brush Artist · Refs · #24 Picasso flat oil — own sheet
own sheet 600 × 600 · Oil · 34 px · 5.1 s

![Brush Artist · Refs · #24 Picasso flat oil — own sheet](Brush-Artist-Refs-24-Picasso-flat-oil-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 35 % → 60 % | 34.6 px | 0.24 | 1.73 | 121 |
| stroke 2 | 40 % → 66 % | 47.1 px | 0.23 | 1.65 | 122 |
| stroke 3 | 56 % → 84 % | 59.7 px | 0.23 | 1.50 | 127 |
| stroke 4 | 56 % → 82 % | 63.9 px | 0.23 | 1.47 | 133 |
| stroke 5 | 55 % → 86 % | 59.9 px | 0.23 | 1.56 | 132 |
| stroke 6 | 56 % → 85 % | 66.3 px | 0.23 | 1.52 | 92 |
| stroke 7 | 60 % → 75 % | 59.1 px | 0.23 | 1.23 | 119 |
| stroke 8 | 56 % → 72 % | 71.1 px | 0.23 | 1.28 | 91 |
| stroke 9 | 42 % → 67 % | 43.8 px | 0.23 | 1.61 | 118 |
| stroke 10 | 46 % → 69 % | 56.7 px | 0.23 | 1.49 | 128 |
| stroke 11 | 59 % → 73 % | 60.6 px | 0.23 | 1.24 | 129 |
| stroke 12 | 59 % → 78 % | 72.3 px | 0.23 | 1.31 | 122 |
| stroke 13 | 47 % → 72 % | 50.2 px | 0.23 | 1.55 | 136 |
| stroke 14 | 48 % → 75 % | 55.1 px | 0.23 | 1.54 | 129 |
| stroke 15 | 53 % → 82 % | 53.5 px | 0.23 | 1.56 | 123 |
| stroke 16 | 49 % → 78 % | 58.9 px | 0.23 | 1.59 | 141 |
| stroke 17 | 60 % → 71 % | 59.6 px | 0.23 | 1.18 | 236 |
| stroke 18 | 56 % → 56 % | 71.0 px | 0.23 | 1.00 | 124 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #25 Yellow heavy flat stroke — own sheet
own sheet 600 × 600 · Heavy acrylic · 110 px · 2.7 s

![Brush Artist · Refs · #25 Yellow heavy flat stroke — own sheet](Brush-Artist-Refs-25-Yellow-heavy-flat-stroke-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 35 % → 35 % | 104.2 px | 0.17 | 0.98 | 619 |

## Brush Artist · Refs · #27 Orange impasto swatch — own sheet
own sheet 600 × 600 · Heavy acrylic · 60 px · 2.8 s

![Brush Artist · Refs · #27 Orange impasto swatch — own sheet](Brush-Artist-Refs-27-Orange-impasto-swatch-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 23 % → 29 % | 61.8 px | 0.34 | 1.29 | 65 |
| stroke 2 | 19 % → 40 % | 62.5 px | 0.33 | 2.07 | 42 |
| stroke 3 | 26 % → 38 % | 94.9 px | 0.34 | 1.48 | 33 |
| stroke 4 | 22 % → 22 % | 62.5 px | 0.33 | 0.96 | 66 |
| stroke 5 | 32 % → 41 % | 62.2 px | 0.33 | 1.28 | 61 |
| stroke 6 | 39 % → 40 % | 112.2 px | 0.33 | 1.02 | 58 |
| stroke 7 | 19 % → 21 % | 63.8 px | 0.33 | 1.11 | 43 |
| stroke 8 | 42 % → 40 % | 143.3 px | 0.33 | 0.97 | 40 |
| stroke 9 | 49 % → 48 % | 97.7 px | 0.33 | 0.97 | 65 |
| stroke 10 | 28 % → 27 % | 87.2 px | 0.33 | 0.96 | 47 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #28 Miles Davis black lines — own sheet
own sheet 600 × 600 · Ink · 22 px · 5.5 s

![Brush Artist · Refs · #28 Miles Davis black lines — own sheet](Brush-Artist-Refs-28-Miles-Davis-black-lines-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 29 % → 36 % | 36.4 px | 0.88 | 1.26 | 159 |
| stroke 2 | 37 % → 57 % | 36.0 px | 0.88 | 1.52 | 121 |
| stroke 3 | 47 % → 48 % | 66.3 px | 0.88 | 1.02 | 99 |
| stroke 4 | 49 % → 58 % | 76.4 px | 0.88 | 1.16 | 156 |
| stroke 5 | 63 % → 64 % | 95.0 px | 0.88 | 1.00 | 112 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #29 Shrigley magenta asterisk — own sheet
own sheet 600 × 600 · Watercolor · 70 px · 5.5 s

![Brush Artist · Refs · #29 Shrigley magenta asterisk — own sheet](Brush-Artist-Refs-29-Shrigley-magenta-asterisk-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 25 % → 44 % | 46.6 px | 0.72 | 1.76 | 168 |
| stroke 2 | 17 % → 17 % | 86.5 px | 0.71 | 1.00 | 186 |
| stroke 3 | 37 % → 43 % | 69.5 px | 0.71 | 1.17 | 178 |
| stroke 4 | 32 % → 33 % | 162.9 px | 0.71 | 1.02 | 182 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #30 Red gouache face patch — own sheet
own sheet 600 × 600 · Gouache · 60 px · 10.3 s

![Brush Artist · Refs · #30 Red gouache face patch — own sheet](Brush-Artist-Refs-30-Red-gouache-face-patch-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 27 % → 51 % | 51.5 px | 0.53 | 1.89 | 154 |
| stroke 2 | 33 % → 57 % | 74.5 px | 0.53 | 1.74 | 160 |
| stroke 3 | 50 % → 77 % | 99.1 px | 0.53 | 1.54 | 153 |
| stroke 4 | 50 % → 77 % | 110.7 px | 0.53 | 1.54 | 167 |
| stroke 5 | 49 % → 78 % | 97.1 px | 0.53 | 1.61 | 172 |
| stroke 6 | 50 % → 80 % | 112.2 px | 0.53 | 1.59 | 171 |
| stroke 7 | 51 % → 78 % | 101.2 px | 0.53 | 1.53 | 165 |
| stroke 8 | 49 % → 76 % | 103.7 px | 0.53 | 1.55 | 175 |
| stroke 9 | 52 % → 80 % | 104.6 px | 0.53 | 1.53 | 152 |
| stroke 10 | 54 % → 76 % | 123.0 px | 0.53 | 1.39 | 148 |
| stroke 11 | 52 % → 74 % | 107.4 px | 0.53 | 1.43 | 147 |
| stroke 12 | 50 % → 74 % | 109.1 px | 0.53 | 1.48 | 160 |
| stroke 13 | 45 % → 72 % | 87.5 px | 0.53 | 1.61 | 159 |
| stroke 14 | 45 % → 63 % | 95.7 px | 0.53 | 1.42 | 189 |
| stroke 15 | 48 % → 58 % | 92.1 px | 0.53 | 1.21 | 175 |
| stroke 16 | 55 % → 54 % | 122.4 px | 0.53 | 0.99 | 151 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #31 Warhol blotted line — own sheet
own sheet 600 × 600 · Ink · 6 px · 4.4 s

![Brush Artist · Refs · #31 Warhol blotted line — own sheet](Brush-Artist-Refs-31-Warhol-blotted-line-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 24 % → 47 % | 15.7 px | 0.82 | 1.93 | 65 |
| stroke 2 | 19 % → 24 % | 15.8 px | 0.82 | 1.27 | 72 |
| stroke 3 | 27 % → 27 % | 24.7 px | 0.82 | 1.02 | 90 |
| stroke 4 | 31 % → 41 % | 27.9 px | 0.82 | 1.32 | 46 |
| stroke 5 | 38 % → 46 % | 34.7 px | 0.82 | 1.22 | 67 |
| stroke 6 | 35 % → 36 % | 25.2 px | 0.81 | 1.03 | 65 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #32 Thick orange swipes — own sheet
own sheet 600 × 600 · Heavy acrylic · 90 px · 56.7 s

![Brush Artist · Refs · #32 Thick orange swipes — own sheet](Brush-Artist-Refs-32-Thick-orange-swipes-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 60 % → 99 % | 60.8 px | 0.00 | 1.65 | 794 |
| stroke 2 | 75 % → 99 % | 121.8 px | 0.02 | 1.32 | 957 |
| stroke 3 | 76 % → 99 % | 129.3 px | 0.03 | 1.30 | 971 |
| stroke 4 | 74 % → 99 % | 128.7 px | 0.04 | 1.33 | 977 |
| stroke 5 | 75 % → 99 % | 128.6 px | 0.04 | 1.32 | 920 |
| stroke 6 | 76 % → 99 % | 128.9 px | 0.05 | 1.30 | 973 |
| stroke 7 | 77 % → 99 % | 129.4 px | 0.03 | 1.29 | 997 |
| stroke 8 | 79 % → 99 % | 131.4 px | 0.03 | 1.25 | 967 |
| stroke 9 | 100 % → 99 % | 102.4 px | 0.01 | 0.99 | 792 |
| stroke 10 | 100 % → 100 % | 308.3 px | 0.03 | 1.00 | 345 |
| stroke 11 | 100 % → 100 % | 313.1 px | 0.04 | 1.00 | 283 |
| stroke 12 | 100 % → 100 % | 318.4 px | 0.04 | 1.00 | 267 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #33 Red wet-in-wet band — own sheet
own sheet 600 × 600 · Watercolor · 80 px · 6.9 s

![Brush Artist · Refs · #33 Red wet-in-wet band — own sheet](Brush-Artist-Refs-33-Red-wet-in-wet-band-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 45 % → 63 % | 92.3 px | 0.66 | 1.38 | 398 |
| stroke 2 | 50 % → 63 % | 180.2 px | 0.67 | 1.28 | 100 |
| stroke 3 | 61 % → 74 % | 234.0 px | 0.67 | 1.22 | 106 |
| stroke 4 | 62 % → 71 % | 228.8 px | 0.67 | 1.15 | 98 |
| stroke 5 | 57 % → 70 % | 201.2 px | 0.67 | 1.22 | 111 |
| stroke 6 | 61 % → 61 % | 212.9 px | 0.67 | 1.00 | 114 |

## Brush Artist · Refs · #34 Magenta oil patches — own sheet
own sheet 600 × 600 · Oil · 60 px · 4.1 s

![Brush Artist · Refs · #34 Magenta oil patches — own sheet](Brush-Artist-Refs-34-Magenta-oil-patches-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 24 % → 44 % | 61.9 px | 0.13 | 1.86 | 87 |
| stroke 2 | 22 % → 37 % | 62.8 px | 0.13 | 1.68 | 76 |
| stroke 3 | 21 % → 52 % | 62.3 px | 0.13 | 2.42 | 67 |
| stroke 4 | 31 % → 31 % | 97.0 px | 0.13 | 1.00 | 60 |
| stroke 5 | 28 % → 40 % | 61.7 px | 0.13 | 1.46 | 87 |
| stroke 6 | 27 % → 45 % | 80.2 px | 0.13 | 1.65 | 54 |
| stroke 7 | 29 % → 41 % | 82.2 px | 0.13 | 1.42 | 72 |
| stroke 8 | 52 % → 56 % | 134.7 px | 0.13 | 1.07 | 83 |
| stroke 9 | 34 % → 39 % | 87.4 px | 0.13 | 1.13 | 88 |
| stroke 10 | 48 % → 48 % | 152.6 px | 0.13 | 1.00 | 58 |
| stroke 11 | 61 % → 61 % | 185.1 px | 0.13 | 1.00 | 55 |
| stroke 12 | 35 % → 35 % | 104.1 px | 0.13 | 1.00 | 60 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #35 Red band with runs — own sheet
own sheet 600 × 600 · Watercolor · 70 px · 4.0 s

![Brush Artist · Refs · #35 Red band with runs — own sheet](Brush-Artist-Refs-35-Red-band-with-runs-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 41 % → 39 % | 82.9 px | 0.59 | 0.95 | 283 |

## Brush Artist · Refs · #36 Magenta letters flat brush — own sheet
own sheet 600 × 600 · Gouache · 36 px · 9.7 s

![Brush Artist · Refs · #36 Magenta letters flat brush — own sheet](Brush-Artist-Refs-36-Magenta-letters-flat-brush-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 46 % → 46 % | 59.1 px | 0.50 | 1.00 | 28 |
| stroke 2 | 38 % → 48 % | 39.7 px | 0.50 | 1.25 | 34 |
| stroke 3 | 56 % → 63 % | 72.2 px | 0.50 | 1.12 | 32 |
| stroke 4 | 45 % → 53 % | 44.9 px | 0.50 | 1.19 | 109 |
| stroke 5 | 41 % → 52 % | 61.1 px | 0.50 | 1.29 | 72 |
| stroke 6 | 78 % → 76 % | 153.6 px | 0.50 | 0.97 | 14 |
| stroke 7 | 43 % → 50 % | 42.1 px | 0.50 | 1.15 | 118 |
| stroke 8 | 39 % → 59 % | 63.5 px | 0.50 | 1.52 | 61 |
| stroke 9 | 54 % → 53 % | 82.8 px | 0.50 | 0.98 | 26 |
| stroke 10 | 42 % → 61 % | 63.1 px | 0.50 | 1.44 | 68 |
| stroke 11 | 78 % → 77 % | 153.6 px | 0.50 | 0.98 | 18 |
| stroke 12 | 58 % → 68 % | 57.2 px | 0.50 | 1.17 | 122 |
| stroke 13 | 43 % → 50 % | 58.9 px | 0.50 | 1.18 | 33 |
| stroke 14 | 52 % → 73 % | 74.9 px | 0.50 | 1.40 | 30 |
| stroke 15 | 44 % → 52 % | 66.5 px | 0.50 | 1.18 | 68 |
| stroke 16 | 78 % → 76 % | 153.3 px | 0.50 | 0.98 | 13 |
| stroke 17 | 53 % → 61 % | 51.3 px | 0.50 | 1.15 | 108 |
| stroke 18 | 40 % → 47 % | 54.9 px | 0.50 | 1.17 | 37 |
| stroke 19 | 65 % → 63 % | 81.6 px | 0.50 | 0.97 | 38 |
| stroke 20 | 56 % → 54 % | 70.5 px | 0.50 | 0.97 | 29 |
| stroke 21 | 47 % → 46 % | 53.9 px | 0.50 | 0.96 | 75 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #37 Oil still life dabs — own sheet
own sheet 600 × 600 · Oil · 40 px · 3.4 s

![Brush Artist · Refs · #37 Oil still life dabs — own sheet](Brush-Artist-Refs-37-Oil-still-life-dabs-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 20 % → 20 % | 44.0 px | 0.39 | 1.00 | 29 |
| stroke 2 | 18 % → 48 % | 44.4 px | 0.39 | 2.65 | 21 |
| stroke 3 | 23 % → 48 % | 59.8 px | 0.38 | 2.12 | 22 |
| stroke 4 | 22 % → 22 % | 42.7 px | 0.39 | 1.00 | 33 |
| stroke 5 | 17 % → 18 % | 43.2 px | 0.39 | 1.04 | 23 |
| stroke 6 | 37 % → 45 % | 83.3 px | 0.39 | 1.24 | 25 |
| stroke 7 | 16 % → 27 % | 54.8 px | 0.39 | 1.71 | 13 |
| stroke 8 | 14 % → 29 % | 47.9 px | 0.39 | 2.08 | 12 |
| stroke 9 | 23 % → 23 % | 43.9 px | 0.39 | 1.00 | 32 |
| stroke 10 | 31 % → 37 % | 58.3 px | 0.39 | 1.18 | 34 |
| stroke 11 | 39 % → 39 % | 109.7 px | 0.39 | 1.00 | 19 |
| stroke 12 | 31 % → 31 % | 109.5 px | 0.40 | 1.00 | 12 |
| stroke 13 | 17 % → 17 % | 59.0 px | 0.39 | 1.00 | 16 |
| stroke 14 | 35 % → 35 % | 91.9 px | 0.39 | 1.00 | 18 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #38 Sanguine drawing — own sheet
own sheet 600 × 600 · Pastel · 6 px · 2.1 s

![Brush Artist · Refs · #38 Sanguine drawing — own sheet](Brush-Artist-Refs-38-Sanguine-drawing-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 3 % → 14 % | 2.9 px | 0.57 | 4.35 | 9 |
| stroke 2 | 3 % → 7 % | 2.9 px | 0.57 | 2.23 | 4 |
| stroke 3 | 3 % → 9 % | 2.9 px | 0.57 | 2.76 | 4 |
| stroke 4 | 3 % → 19 % | 2.7 px | 0.57 | 6.27 | 7 |
| stroke 5 | 3 % → 8 % | 2.7 px | 0.57 | 2.71 | 3 |
| stroke 6 | 3 % → 20 % | 3.0 px | 0.57 | 6.20 | 7 |
| stroke 7 | 5 % → 15 % | 4.7 px | 0.57 | 2.84 | 4 |
| stroke 8 | 4 % → 15 % | 3.9 px | 0.57 | 3.43 | 7 |
| stroke 9 | 3 % → 7 % | 2.9 px | 0.57 | 2.30 | 4 |
| stroke 10 | 4 % → 17 % | 4.0 px | 0.57 | 3.83 | 6 |
| stroke 11 | 3 % → 5 % | 2.9 px | 0.57 | 1.49 | 4 |
| stroke 12 | 5 % → 16 % | 4.5 px | 0.57 | 3.20 | 4 |
| stroke 13 | 8 % → 18 % | 7.8 px | 0.57 | 2.10 | 3 |
| stroke 14 | 5 % → 15 % | 4.5 px | 0.57 | 2.96 | 6 |
| stroke 15 | 10 % → 18 % | 9.5 px | 0.57 | 1.71 | 7 |
| stroke 16 | 6 % → 16 % | 5.4 px | 0.57 | 2.74 | 4 |
| stroke 17 | 4 % → 9 % | 4.0 px | 0.57 | 2.07 | 7 |
| stroke 18 | 3 % → 5 % | 2.9 px | 0.57 | 1.68 | 6 |
| stroke 19 | 7 % → 17 % | 6.0 px | 0.57 | 2.63 | 4 |
| stroke 20 | 8 % → 15 % | 7.8 px | 0.57 | 1.72 | 3 |
| stroke 21 | 4 % → 4 % | 4.0 px | 0.57 | 1.00 | 4 |
| stroke 22 | 9 % → 14 % | 7.8 px | 0.58 | 1.66 | 8 |
| stroke 23 | 8 % → 12 % | 7.0 px | 0.57 | 1.52 | 4 |
| stroke 24 | 4 % → 7 % | 3.9 px | 0.57 | 1.55 | 6 |
| stroke 25 | 8 % → 15 % | 7.3 px | 0.57 | 1.86 | 6 |
| stroke 26 | 6 % → 8 % | 5.7 px | 0.57 | 1.26 | 6 |
| stroke 27 | 4 % → 4 % | 3.8 px | 0.57 | 1.05 | 6 |
| stroke 28 | 8 % → 12 % | 7.0 px | 0.57 | 1.56 | 3 |
| stroke 29 | 8 % → 17 % | 6.9 px | 0.57 | 2.22 | 8 |
| stroke 30 | 14 % → 18 % | 13.1 px | 0.57 | 1.25 | 3 |
| stroke 31 | 6 % → 7 % | 5.2 px | 0.57 | 1.23 | 7 |
| stroke 32 | 12 % → 13 % | 10.5 px | 0.57 | 1.15 | 6 |
| stroke 33 | 7 % → 8 % | 6.6 px | 0.57 | 1.06 | 8 |
| stroke 34 | 11 % → 14 % | 10.2 px | 0.57 | 1.28 | 4 |
| stroke 35 | 9 % → 15 % | 8.6 px | 0.57 | 1.56 | 7 |
| stroke 36 | 11 % → 13 % | 9.8 px | 0.57 | 1.27 | 5 |
| stroke 37 | 11 % → 17 % | 9.8 px | 0.57 | 1.64 | 6 |
| stroke 38 | 14 % → 21 % | 12.4 px | 0.57 | 1.51 | 3 |
| stroke 39 | 15 % → 18 % | 13.6 px | 0.57 | 1.22 | 7 |
| stroke 40 | 6 % → 7 % | 5.3 px | 0.57 | 1.16 | 3 |
| stroke 41 | 17 % → 17 % | 15.3 px | 0.57 | 1.00 | 5 |
| stroke 42 | 14 % → 16 % | 12.6 px | 0.57 | 1.16 | 7 |
| stroke 43 | 11 % → 13 % | 10.0 px | 0.57 | 1.18 | 4 |
| stroke 44 | 13 % → 16 % | 11.6 px | 0.57 | 1.23 | 7 |
| stroke 45 | 3 % → 3 % | 2.6 px | 0.57 | 1.00 | 7 |
| stroke 46 | 17 % → 17 % | 15.6 px | 0.57 | 1.00 | 3 |
| stroke 47 | 14 % → 14 % | 13.1 px | 0.57 | 1.00 | 7 |
| stroke 48 | 13 % → 14 % | 12.4 px | 0.58 | 1.04 | 3 |
| stroke 49 | 20 % → 20 % | 18.3 px | 0.57 | 1.00 | 8 |
| stroke 50 | 10 % → 10 % | 9.5 px | 0.57 | 1.00 | 4 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #39 Very thick impasto — own sheet
own sheet 600 × 600 · Heavy acrylic · 60 px · 53.8 s

![Brush Artist · Refs · #39 Very thick impasto — own sheet](Brush-Artist-Refs-39-Very-thick-impasto-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 84 % → 99 % | 62.8 px | 0.22 | 1.18 | 827 |
| stroke 2 | 87 % → 99 % | 101.6 px | 0.18 | 1.15 | 978 |
| stroke 3 | 88 % → 99 % | 101.6 px | 0.19 | 1.13 | 1002 |
| stroke 4 | 89 % → 99 % | 103.9 px | 0.29 | 1.12 | 1020 |
| stroke 5 | 88 % → 99 % | 104.4 px | 0.17 | 1.12 | 1005 |
| stroke 6 | 89 % → 99 % | 104.7 px | 0.21 | 1.12 | 1002 |
| stroke 7 | 89 % → 99 % | 104.7 px | 0.23 | 1.12 | 1132 |
| stroke 8 | 89 % → 99 % | 104.8 px | 0.17 | 1.12 | 967 |
| stroke 9 | 100 % → 99 % | 75.0 px | 0.16 | 0.99 | 783 |
| stroke 10 | 100 % → 99 % | 156.8 px | 0.18 | 0.99 | 247 |
| stroke 11 | 100 % → 99 % | 162.7 px | 0.19 | 0.99 | 248 |
| stroke 12 | 100 % → 99 % | 180.0 px | 0.19 | 0.99 | 221 |
| stroke 13 | 100 % → 99 % | 153.1 px | 0.18 | 0.99 | 247 |
| stroke 14 | 100 % → 99 % | 168.3 px | 0.17 | 0.99 | 207 |

## Brush Artist · Refs · #40 Watercolour blooms — own sheet
own sheet 600 × 600 · Watercolor · 90 px · 5.3 s

![Brush Artist · Refs · #40 Watercolour blooms — own sheet](Brush-Artist-Refs-40-Watercolour-blooms-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 39 % → 39 % | 94.2 px | 0.13 | 1.00 | 796 |

## Brush Artist · Refs · #41 Coloured pencil hatching — own sheet
own sheet 600 × 600 · Pastel · 4 px · 51.2 s

![Brush Artist · Refs · #41 Coloured pencil hatching — own sheet](Brush-Artist-Refs-41-Coloured-pencil-hatching-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 100 % → 97 % | 16.8 px | 0.01 | 0.97 | 798 |
| stroke 2 | 100 % → 97 % | 15.0 px | 0.03 | 0.97 | 918 |
| stroke 3 | 100 % → 98 % | 17.6 px | 0.03 | 0.98 | 920 |
| stroke 4 | 100 % → 98 % | 16.8 px | 0.02 | 0.98 | 917 |
| stroke 5 | 100 % → 97 % | 16.8 px | 0.03 | 0.97 | 921 |
| stroke 6 | 100 % → 98 % | 19.4 px | 0.04 | 0.98 | 918 |
| stroke 7 | 100 % → 98 % | 18.5 px | 0.04 | 0.98 | 913 |
| stroke 8 | 100 % → 97 % | 19.4 px | 0.03 | 0.97 | 907 |
| stroke 9 | 100 % → 97 % | 17.6 px | 0.01 | 0.97 | 727 |
| stroke 10 | 100 % → 100 % | 63.9 px | 0.05 | 1.00 | 3 |
| stroke 11 | 100 % → 100 % | 62.9 px | 0.03 | 1.00 | 3 |
| stroke 12 | 100 % → 100 % | 63.9 px | 0.04 | 1.00 | 3 |
| stroke 13 | 100 % → 100 % | 64.0 px | 0.07 | 1.00 | 3 |
| stroke 14 | 100 % → 100 % | 63.9 px | 0.03 | 1.00 | 3 |
| stroke 15 | 100 % → 100 % | 62.9 px | 0.05 | 1.00 | 3 |
| stroke 16 | 100 % → 100 % | 62.8 px | 0.05 | 1.00 | 3 |
| stroke 17 | 100 % → 100 % | 62.9 px | 0.05 | 1.00 | 3 |
| stroke 18 | 100 % → 100 % | 62.4 px | 0.05 | 1.00 | 3 |
| stroke 19 | 100 % → 100 % | 63.5 px | 0.06 | 1.00 | 3 |
| stroke 20 | 100 % → 100 % | 64.0 px | 0.05 | 1.00 | 3 |
| stroke 21 | 100 % → 100 % | 62.9 px | 0.02 | 1.00 | 3 |
| stroke 22 | 100 % → 100 % | 62.9 px | 0.06 | 1.00 | 3 |
| stroke 23 | 100 % → 100 % | 63.9 px | 0.05 | 1.00 | 3 |
| stroke 24 | 100 % → 100 % | 62.9 px | 0.05 | 1.00 | 3 |
| stroke 25 | 100 % → 100 % | 62.9 px | 0.04 | 1.00 | 3 |
| stroke 26 | 100 % → 100 % | 64.0 px | 0.02 | 1.00 | 3 |
| stroke 27 | 100 % → 100 % | 64.0 px | 0.04 | 1.00 | 3 |
| stroke 28 | 100 % → 100 % | 64.0 px | 0.05 | 1.00 | 3 |
| stroke 29 | 100 % → 100 % | 63.9 px | 0.06 | 1.00 | 3 |
| stroke 30 | 100 % → 100 % | 63.9 px | 0.05 | 1.00 | 3 |
| stroke 31 | 100 % → 100 % | 64.0 px | 0.06 | 1.00 | 3 |
| stroke 32 | 100 % → 100 % | 62.9 px | 0.05 | 1.00 | 3 |
| stroke 33 | 100 % → 100 % | 62.5 px | 0.05 | 1.00 | 3 |
| stroke 34 | 100 % → 100 % | 63.9 px | 0.04 | 1.00 | 3 |
| stroke 35 | 100 % → 100 % | 64.0 px | 0.03 | 1.00 | 3 |
| stroke 36 | 100 % → 100 % | 63.4 px | 0.03 | 1.00 | 3 |
| stroke 37 | 100 % → 100 % | 64.0 px | 0.04 | 1.00 | 3 |
| stroke 38 | 100 % → 100 % | 62.4 px | 0.05 | 1.00 | 3 |
| stroke 39 | 100 % → 100 % | 62.9 px | 0.04 | 1.00 | 3 |
| stroke 40 | 100 % → 100 % | 64.0 px | 0.06 | 1.00 | 3 |
| stroke 41 | 100 % → 100 % | 63.9 px | 0.03 | 1.00 | 3 |
| stroke 42 | 100 % → 100 % | 64.0 px | 0.05 | 1.00 | 3 |
| stroke 43 | 100 % → 100 % | 64.0 px | 0.03 | 1.00 | 3 |
| stroke 44 | 100 % → 100 % | 63.9 px | 0.05 | 1.00 | 3 |
| stroke 45 | 100 % → 100 % | 62.9 px | 0.03 | 1.00 | 3 |
| stroke 46 | 100 % → 100 % | 62.8 px | 0.06 | 1.00 | 3 |
| stroke 47 | 100 % → 100 % | 63.8 px | 0.05 | 1.00 | 3 |
| stroke 48 | 100 % → 100 % | 64.0 px | 0.05 | 1.00 | 3 |
| stroke 49 | 100 % → 100 % | 62.8 px | 0.07 | 1.00 | 3 |
| stroke 50 | 100 % → 100 % | 62.8 px | 0.05 | 1.00 | 3 |
| stroke 51 | 100 % → 100 % | 63.5 px | 0.07 | 1.00 | 3 |
| stroke 52 | 100 % → 100 % | 62.8 px | 0.04 | 1.00 | 3 |
| stroke 53 | 100 % → 100 % | 63.9 px | 0.06 | 1.00 | 3 |
| stroke 54 | 100 % → 100 % | 63.4 px | 0.06 | 1.00 | 3 |
| stroke 55 | 100 % → 100 % | 62.9 px | 0.03 | 1.00 | 3 |
| stroke 56 | 100 % → 100 % | 62.9 px | 0.05 | 1.00 | 3 |
| stroke 57 | 100 % → 100 % | 62.9 px | 0.06 | 1.00 | 3 |
| stroke 58 | 100 % → 100 % | 63.9 px | 0.04 | 1.00 | 3 |
| stroke 59 | 100 % → 100 % | 62.9 px | 0.03 | 1.00 | 3 |
| stroke 60 | 100 % → 100 % | 62.9 px | 0.06 | 1.00 | 3 |
| stroke 61 | 100 % → 100 % | 64.0 px | 0.06 | 1.00 | 3 |
| stroke 62 | 100 % → 100 % | 62.9 px | 0.06 | 1.00 | 3 |
| stroke 63 | 100 % → 100 % | 63.9 px | 0.06 | 1.00 | 3 |
| stroke 64 | 100 % → 100 % | 64.0 px | 0.05 | 1.00 | 3 |
| stroke 65 | 100 % → 100 % | 64.0 px | 0.05 | 1.00 | 3 |
| stroke 66 | 100 % → 100 % | 62.9 px | 0.05 | 1.00 | 3 |
| stroke 67 | 100 % → 100 % | 64.0 px | 0.05 | 1.00 | 3 |
| stroke 68 | 100 % → 100 % | 62.4 px | 0.05 | 1.00 | 3 |
| stroke 69 | 100 % → 100 % | 63.0 px | 0.07 | 1.00 | 3 |
| stroke 70 | 100 % → 100 % | 62.8 px | 0.07 | 1.00 | 3 |
| stroke 71 | 100 % → 100 % | 63.9 px | 0.04 | 1.00 | 3 |
| stroke 72 | 100 % → 100 % | 64.0 px | 0.05 | 1.00 | 3 |
| stroke 73 | 100 % → 100 % | 62.9 px | 0.06 | 1.00 | 3 |
| stroke 74 | 100 % → 100 % | 63.8 px | 0.06 | 1.00 | 3 |
| stroke 75 | 100 % → 100 % | 64.0 px | 0.05 | 1.00 | 3 |
| stroke 76 | 100 % → 100 % | 62.9 px | 0.05 | 1.00 | 3 |
| stroke 77 | 100 % → 100 % | 63.9 px | 0.04 | 1.00 | 3 |
| stroke 78 | 100 % → 100 % | 62.8 px | 0.03 | 1.00 | 3 |
| stroke 79 | 100 % → 100 % | 62.9 px | 0.05 | 1.00 | 3 |
| stroke 80 | 100 % → 100 % | 62.9 px | 0.05 | 1.00 | 3 |
| stroke 81 | 100 % → 100 % | 64.0 px | 0.03 | 1.00 | 3 |
| stroke 82 | 100 % → 100 % | 63.9 px | 0.05 | 1.00 | 3 |
| stroke 83 | 100 % → 100 % | 62.4 px | 0.06 | 1.00 | 3 |
| stroke 84 | 100 % → 100 % | 62.4 px | 0.06 | 1.00 | 3 |
| stroke 85 | 100 % → 100 % | 62.8 px | 0.06 | 1.00 | 3 |
| stroke 86 | 100 % → 100 % | 62.9 px | 0.04 | 1.00 | 3 |
| stroke 87 | 100 % → 100 % | 63.9 px | 0.04 | 1.00 | 3 |
| stroke 88 | 100 % → 100 % | 62.9 px | 0.03 | 1.00 | 3 |
| stroke 89 | 100 % → 100 % | 63.5 px | 0.05 | 1.00 | 3 |

## Brush Artist · Refs · #42 Oil pastel shaggy — own sheet
own sheet 600 × 600 · Pastel · 18 px · 2.5 s

![Brush Artist · Refs · #42 Oil pastel shaggy — own sheet](Brush-Artist-Refs-42-Oil-pastel-shaggy-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 9 % → 20 % | 8.0 px | 0.28 | 2.21 | 6 |
| stroke 2 | 10 % → 26 % | 8.6 px | 0.28 | 2.58 | 7 |
| stroke 3 | 10 % → 33 % | 8.9 px | 0.29 | 3.29 | 11 |
| stroke 4 | 10 % → 21 % | 8.8 px | 0.28 | 2.08 | 8 |
| stroke 5 | 11 % → 21 % | 9.9 px | 0.28 | 1.84 | 6 |
| stroke 6 | 10 % → 31 % | 9.1 px | 0.29 | 3.00 | 10 |
| stroke 7 | 14 % → 40 % | 12.6 px | 0.28 | 2.79 | 6 |
| stroke 8 | 11 % → 44 % | 9.5 px | 0.28 | 3.98 | 7 |
| stroke 9 | 13 % → 22 % | 11.5 px | 0.28 | 1.69 | 12 |
| stroke 10 | 11 % → 19 % | 9.5 px | 0.28 | 1.77 | 9 |
| stroke 11 | 10 % → 28 % | 9.0 px | 0.28 | 2.72 | 10 |
| stroke 12 | 14 % → 19 % | 12.3 px | 0.28 | 1.36 | 7 |
| stroke 13 | 19 % → 30 % | 16.7 px | 0.28 | 1.60 | 11 |
| stroke 14 | 9 % → 20 % | 7.9 px | 0.28 | 2.25 | 6 |
| stroke 15 | 10 % → 36 % | 9.0 px | 0.29 | 3.51 | 12 |
| stroke 16 | 16 % → 34 % | 14.4 px | 0.29 | 2.06 | 6 |
| stroke 17 | 21 % → 39 % | 18.6 px | 0.28 | 1.82 | 11 |
| stroke 18 | 25 % → 35 % | 21.6 px | 0.29 | 1.42 | 9 |
| stroke 19 | 22 % → 40 % | 19.1 px | 0.28 | 1.79 | 6 |
| stroke 20 | 23 % → 42 % | 19.9 px | 0.28 | 1.81 | 9 |
| stroke 21 | 14 % → 20 % | 12.7 px | 0.28 | 1.41 | 9 |
| stroke 22 | 14 % → 16 % | 12.0 px | 0.28 | 1.14 | 11 |
| stroke 23 | 20 % → 27 % | 17.3 px | 0.29 | 1.34 | 6 |
| stroke 24 | 30 % → 35 % | 26.0 px | 0.30 | 1.20 | 10 |
| stroke 25 | 20 % → 33 % | 17.4 px | 0.28 | 1.67 | 10 |
| stroke 26 | 11 % → 22 % | 9.2 px | 0.28 | 2.04 | 7 |
| stroke 27 | 31 % → 36 % | 27.6 px | 0.29 | 1.15 | 6 |
| stroke 28 | 19 % → 30 % | 16.5 px | 0.28 | 1.60 | 8 |
| stroke 29 | 11 % → 29 % | 9.4 px | 0.29 | 2.75 | 9 |
| stroke 30 | 14 % → 38 % | 11.9 px | 0.29 | 2.79 | 7 |
| stroke 31 | 16 % → 16 % | 13.9 px | 0.28 | 1.00 | 6 |
| stroke 32 | 20 % → 33 % | 17.2 px | 0.29 | 1.70 | 8 |
| stroke 33 | 20 % → 21 % | 17.6 px | 0.29 | 1.03 | 10 |
| stroke 34 | 30 % → 36 % | 26.0 px | 0.28 | 1.20 | 7 |
| stroke 35 | 29 % → 37 % | 25.2 px | 0.28 | 1.27 | 6 |
| stroke 36 | 25 % → 27 % | 22.0 px | 0.28 | 1.05 | 9 |
| stroke 37 | 21 % → 21 % | 17.9 px | 0.28 | 1.00 | 12 |
| stroke 38 | 29 % → 34 % | 24.6 px | 0.28 | 1.20 | 6 |
| stroke 39 | 15 % → 25 % | 13.2 px | 0.28 | 1.64 | 13 |
| stroke 40 | 34 % → 41 % | 29.5 px | 0.28 | 1.21 | 12 |
| stroke 41 | 32 % → 34 % | 28.3 px | 0.28 | 1.04 | 13 |
| stroke 42 | 21 % → 30 % | 18.8 px | 0.28 | 1.39 | 8 |
| stroke 43 | 14 % → 14 % | 12.4 px | 0.28 | 1.00 | 6 |
| stroke 44 | 29 % → 39 % | 25.3 px | 0.28 | 1.35 | 7 |
| stroke 45 | 25 % → 25 % | 21.7 px | 0.28 | 1.00 | 9 |
| stroke 46 | 40 % → 45 % | 34.6 px | 0.29 | 1.12 | 10 |
| stroke 47 | 38 % → 45 % | 33.1 px | 0.28 | 1.17 | 6 |
| stroke 48 | 27 % → 30 % | 23.5 px | 0.29 | 1.12 | 12 |
| stroke 49 | 32 % → 34 % | 27.9 px | 0.29 | 1.06 | 10 |
| stroke 50 | 39 % → 42 % | 34.1 px | 0.28 | 1.08 | 6 |
| stroke 51 | 20 % → 20 % | 17.4 px | 0.29 | 1.00 | 11 |
| stroke 52 | 37 % → 37 % | 32.1 px | 0.29 | 1.00 | 10 |
| stroke 53 | 23 % → 23 % | 19.8 px | 0.28 | 1.02 | 6 |
| stroke 54 | 28 % → 31 % | 24.4 px | 0.29 | 1.10 | 11 |
| stroke 55 | 17 % → 17 % | 14.6 px | 0.28 | 1.00 | 9 |
| stroke 56 | 21 % → 21 % | 18.2 px | 0.28 | 1.00 | 6 |
| stroke 57 | 36 % → 36 % | 31.3 px | 0.29 | 1.00 | 7 |
| stroke 58 | 29 % → 29 % | 25.3 px | 0.28 | 1.00 | 10 |
| stroke 59 | 50 % → 50 % | 43.8 px | 0.28 | 1.00 | 8 |
| stroke 60 | 19 % → 19 % | 16.5 px | 0.28 | 1.00 | 9 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #43 Dragged black ink blocks — own sheet
own sheet 600 × 600 · Gouache · 70 px · 50.6 s

![Brush Artist · Refs · #43 Dragged black ink blocks — own sheet](Brush-Artist-Refs-43-Dragged-black-ink-blocks-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 74 % → 99 % | 63.1 px | 0.26 | 1.33 | 861 |
| stroke 2 | 81 % → 99 % | 111.0 px | 0.20 | 1.23 | 996 |
| stroke 3 | 84 % → 99 % | 111.0 px | 0.18 | 1.18 | 956 |
| stroke 4 | 83 % → 99 % | 111.9 px | 0.28 | 1.19 | 993 |
| stroke 5 | 82 % → 99 % | 110.3 px | 0.19 | 1.21 | 965 |
| stroke 6 | 81 % → 99 % | 110.6 px | 0.27 | 1.22 | 980 |
| stroke 7 | 84 % → 99 % | 110.0 px | 0.20 | 1.18 | 1000 |
| stroke 8 | 81 % → 99 % | 110.7 px | 0.18 | 1.22 | 984 |
| stroke 9 | 100 % → 99 % | 86.5 px | 0.28 | 0.99 | 932 |
| stroke 10 | 100 % → 99 % | 145.3 px | 0.22 | 0.99 | 309 |
| stroke 11 | 100 % → 99 % | 189.3 px | 0.17 | 0.99 | 322 |
| stroke 12 | 100 % → 99 % | 188.7 px | 0.19 | 0.99 | 309 |
| stroke 13 | 100 % → 99 % | 182.4 px | 0.19 | 0.99 | 319 |
| stroke 14 | 100 % → 99 % | 152.9 px | 0.21 | 0.99 | 329 |

## Brush Artist · Refs · #44 Blue looping ribbon — own sheet
own sheet 600 × 600 · Oil · 80 px · 5.2 s

![Brush Artist · Refs · #44 Blue looping ribbon — own sheet](Brush-Artist-Refs-44-Blue-looping-ribbon-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 48 % → 48 % | 42.2 px | 0.78 | 1.00 | 2339 |

## Brush Artist · Refs · #45 Soft pastel pepper — own sheet
own sheet 600 × 600 · Pastel · 40 px · 3.0 s

![Brush Artist · Refs · #45 Soft pastel pepper — own sheet](Brush-Artist-Refs-45-Soft-pastel-pepper-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 15 % → 33 % | 11.3 px | 0.49 | 2.20 | 311 |
| stroke 2 | 25 % → 37 % | 20.6 px | 0.49 | 1.47 | 278 |
| stroke 3 | 34 % → 42 % | 13.8 px | 0.49 | 1.25 | 267 |
| stroke 4 | 32 % → 36 % | 27.8 px | 0.49 | 1.13 | 282 |
| stroke 5 | 37 % → 37 % | 13.9 px | 0.49 | 1.00 | 219 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #46 Red-brown ink lips — own sheet
own sheet 600 × 600 · Watercolor · 70 px · 4.6 s

![Brush Artist · Refs · #46 Red-brown ink lips — own sheet](Brush-Artist-Refs-46-Red-brown-ink-lips-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 30 % → 43 % | 78.1 px | 0.72 | 1.42 | 198 |
| stroke 2 | 45 % → 45 % | 119.4 px | 0.72 | 1.00 | 166 |

## Brush Artist · Refs · #47 Pink knife slabs — own sheet
own sheet 600 × 600 · Heavy acrylic · 90 px · 4.1 s

![Brush Artist · Refs · #47 Pink knife slabs — own sheet](Brush-Artist-Refs-47-Pink-knife-slabs-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 28 % → 34 % | 83.2 px | 0.11 | 1.18 | 256 |
| stroke 2 | 36 % → 41 % | 106.4 px | 0.11 | 1.13 | 260 |
| stroke 3 | 36 % → 41 % | 106.3 px | 0.11 | 1.14 | 263 |
| stroke 4 | 37 % → 36 % | 106.4 px | 0.11 | 0.97 | 254 |

## Brush Artist · Refs · #48 Black bands with drips — own sheet
own sheet 600 × 600 · Gouache · 70 px · 43.2 s

![Brush Artist · Refs · #48 Black bands with drips — own sheet](Brush-Artist-Refs-48-Black-bands-with-drips-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 75 % → 99 % | 62.0 px | 0.11 | 1.32 | 819 |
| stroke 2 | 81 % → 99 % | 110.7 px | 0.12 | 1.22 | 1000 |
| stroke 3 | 82 % → 99 % | 111.0 px | 0.18 | 1.21 | 1021 |
| stroke 4 | 84 % → 99 % | 113.5 px | 0.12 | 1.18 | 954 |
| stroke 5 | 81 % → 99 % | 111.0 px | 0.17 | 1.22 | 974 |
| stroke 6 | 80 % → 99 % | 110.7 px | 0.12 | 1.23 | 949 |
| stroke 7 | 81 % → 99 % | 110.4 px | 0.13 | 1.21 | 932 |
| stroke 8 | 83 % → 99 % | 112.5 px | 0.12 | 1.18 | 906 |
| stroke 9 | 100 % → 99 % | 82.9 px | 0.02 | 0.99 | 701 |
| stroke 10 | 100 % → 99 % | 177.4 px | 0.12 | 0.99 | 310 |
| stroke 11 | 100 % → 99 % | 166.7 px | 0.12 | 0.99 | 311 |
| stroke 12 | 100 % → 99 % | 175.1 px | 0.11 | 0.99 | 356 |
| stroke 13 | 100 % → 99 % | 174.8 px | 0.12 | 0.99 | 314 |

## Brush Artist · Refs · #49 Magenta letters round brush — own sheet
own sheet 600 × 600 · Ink · 30 px · 8.6 s

![Brush Artist · Refs · #49 Magenta letters round brush — own sheet](Brush-Artist-Refs-49-Magenta-letters-round-brush-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 61 % → 65 % | 64.3 px | 0.52 | 1.06 | 30 |
| stroke 2 | 59 % → 63 % | 52.0 px | 0.53 | 1.07 | 28 |
| stroke 3 | 71 % → 80 % | 74.2 px | 0.53 | 1.13 | 28 |
| stroke 4 | 54 % → 64 % | 48.0 px | 0.52 | 1.18 | 113 |
| stroke 5 | 48 % → 65 % | 63.0 px | 0.52 | 1.35 | 76 |
| stroke 6 | 93 % → 94 % | 141.0 px | 0.53 | 1.01 | 18 |
| stroke 7 | 61 % → 70 % | 51.9 px | 0.52 | 1.14 | 108 |
| stroke 8 | 44 % → 72 % | 63.4 px | 0.53 | 1.61 | 64 |
| stroke 9 | 71 % → 71 % | 86.0 px | 0.53 | 1.00 | 24 |
| stroke 10 | 51 % → 72 % | 66.5 px | 0.52 | 1.42 | 75 |
| stroke 11 | 93 % → 94 % | 140.9 px | 0.53 | 1.01 | 14 |
| stroke 12 | 71 % → 83 % | 60.6 px | 0.52 | 1.18 | 124 |
| stroke 13 | 61 % → 65 % | 67.4 px | 0.53 | 1.05 | 35 |
| stroke 14 | 69 % → 92 % | 78.6 px | 0.53 | 1.33 | 27 |
| stroke 15 | 52 % → 63 % | 68.8 px | 0.52 | 1.20 | 71 |
| stroke 16 | 93 % → 93 % | 140.9 px | 0.53 | 1.00 | 14 |
| stroke 17 | 68 % → 76 % | 58.1 px | 0.52 | 1.12 | 111 |
| stroke 18 | 59 % → 62 % | 64.6 px | 0.52 | 1.05 | 31 |
| stroke 19 | 81 % → 80 % | 82.3 px | 0.53 | 0.99 | 37 |
| stroke 20 | 71 % → 70 % | 72.0 px | 0.52 | 1.00 | 35 |
| stroke 21 | 59 % → 59 % | 61.0 px | 0.52 | 1.00 | 85 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #50 Thick swipes on photo — own sheet
own sheet 600 × 600 · Heavy acrylic · 40 px · 2.5 s

![Brush Artist · Refs · #50 Thick swipes on photo — own sheet](Brush-Artist-Refs-50-Thick-swipes-on-photo-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 24 % → 27 % | 42.6 px | 0.32 | 1.12 | 27 |
| stroke 2 | 21 % → 28 % | 42.4 px | 0.33 | 1.33 | 25 |
| stroke 3 | 26 % → 24 % | 41.8 px | 0.33 | 0.95 | 38 |
| stroke 4 | 26 % → 24 % | 42.6 px | 0.33 | 0.94 | 35 |
| stroke 5 | 24 % → 22 % | 41.8 px | 0.33 | 0.95 | 29 |
| stroke 6 | 21 % → 19 % | 42.9 px | 0.33 | 0.94 | 22 |
| stroke 7 | 36 % → 37 % | 59.4 px | 0.33 | 1.02 | 44 |
| stroke 8 | 34 % → 33 % | 66.7 px | 0.32 | 0.97 | 30 |
| stroke 9 | 25 % → 23 % | 42.0 px | 0.33 | 0.95 | 36 |
| stroke 10 | 28 % → 27 % | 42.2 px | 0.33 | 0.95 | 35 |
| stroke 11 | 23 % → 21 % | 42.6 px | 0.33 | 0.95 | 31 |
| stroke 12 | 24 % → 23 % | 53.2 px | 0.33 | 0.95 | 19 |

## Brush Artist · Ink — dry brush — own sheet
own sheet 600 × 600 · Gouache · 30 px · 2.9 s

![Brush Artist · Ink — dry brush — own sheet](Brush-Artist-Ink-dry-brush-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| ear | 17 % → 4 % | 16.7 px | 0.82 | 0.24 | 503 |
| drag0 | 20 % → 24 % | 25.0 px | 0.82 | 1.22 | 135 |
| drag1 | 25 % → 25 % | 34.2 px | 0.82 | 1.02 | 109 |
| drag2 | 28 % → 25 % | 42.1 px | 0.82 | 0.92 | 90 |
| drag3 | 30 % → 26 % | 50.2 px | 0.82 | 0.87 | 78 |

## Brush Artist · Watercolour — blue — own sheet
own sheet 600 × 600 · Watercolor · 40 px · 8.5 s

![Brush Artist · Watercolour — blue — own sheet](Brush-Artist-Watercolour-blue-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| s0 | 14 % → 28 % | 28.4 px | 0.28 | 2.04 | 40 |
| s1 | 8 % → 36 % | 9.9 px | 0.40 | 4.46 | 32 |
| s2 | 12 % → 21 % | 28.5 px | 0.16 | 1.74 | 37 |
| s3 | 11 % → 18 % | 20.3 px | 0.26 | 1.68 | 46 |
| s4 | 17 % → 34 % | 36.6 px | 0.38 | 1.96 | 56 |
| s5 | 25 % → 33 % | 34.0 px | 0.35 | 1.32 | 47 |
| s6 | 25 % → 30 % | 39.5 px | 0.28 | 1.23 | 54 |
| s7 | 27 % → 34 % | 18.5 px | 0.42 | 1.28 | 40 |
| s8 | 21 % → 25 % | 44.1 px | 0.22 | 1.19 | 42 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Charcoal — stick — own sheet
own sheet 600 × 600 · Charcoal · 28 px · 1.1 s

![Brush Artist · Charcoal — stick — own sheet](Brush-Artist-Charcoal-stick-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| finger0 | 16 % → 21 % | 15.5 px | 0.83 | 1.33 | 25 |
| tip0 | 15 % → 22 % | 18.4 px | 0.83 | 1.47 | 5 |
| finger1 | 16 % → 26 % | 15.7 px | 0.83 | 1.64 | 26 |
| tip1 | 20 % → 27 % | 24.8 px | 0.83 | 1.34 | 7 |
| finger2 | 16 % → 24 % | 16.0 px | 0.83 | 1.45 | 21 |
| tip2 | 20 % → 27 % | 24.1 px | 0.83 | 1.34 | 5 |
| finger3 | 16 % → 18 % | 16.1 px | 0.83 | 1.12 | 22 |
| tip3 | 20 % → 20 % | 24.3 px | 0.83 | 1.00 | 5 |
| cig0 | 38 % → 50 % | 35.5 px | 0.83 | 1.32 | 7 |
| cig1 | 42 % → 55 % | 39.5 px | 0.83 | 1.30 | 6 |
| cig2 | 47 % → 60 % | 44.1 px | 0.83 | 1.27 | 9 |
| cig3 | 51 % → 60 % | 47.1 px | 0.83 | 1.20 | 10 |
| cig4 | 50 % → 55 % | 46.8 px | 0.83 | 1.10 | 7 |
| cig5 | 51 % → 51 % | 47.1 px | 0.83 | 1.00 | 14 |

Numbers say: wet paint spreads well beyond the stroke.

