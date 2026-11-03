![All brushes](contact.png)

# Brush Lab — 169 brushes · 3 Nov 2026 at 18:35

Every sheet: 1500 × 600, ten strokes in a 5 × 2 grid — 1. light line · 2. heavy line · 3. pressure swell · 4. fast wave · 5. slow wave · 6. spiral · 7. loop · 8. tilted · 9. over the wet one · 10. long, no reload (cell 8 holds «tilted» and «over the wet one» crossed). The CPU reference of Mamay's paint engine; the wet layer settles 20 s at the end.

Columns: **covered** = share of the cell with paint right after the stroke → after settling; **width** = painted area of the stroke ÷ its length (px); **dark** = mean darkness of the painted pixels above the paper's own grain (0 = paper, 1 = black); **spread** = how far wet paint went beyond the stroke (1.0 = stayed); **ms** = the stroke on the CPU; long stroke: paint in each quarter of its length (it should run out: wet → streaks → dry tail).

## Ink Line
Ink · 12 px · 23.2 s

![Ink Line](Ink-Line.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 1 % → 4 % | 4.3 px | 0.55 | 2.44 | 37 |
| heavy line | 5 % → 6 % | 15.7 px | 0.68 | 1.13 | 39 |
| pressure swell | 3 % → 4 % | 11.3 px | 0.64 | 1.40 | 23 |
| fast wave | 10 % → 11 % | 11.2 px | 0.59 | 1.11 | 112 |
| slow wave | 8 % → 10 % | 9.6 px | 0.57 | 1.16 | 96 |
| spiral | 14 % → 15 % | 8.9 px | 0.50 | 1.07 | 141 |
| loop | 8 % → 9 % | 10.6 px | 0.61 | 1.16 | 134 |
| tilted | 5 % → 5 % | 14.4 px | 0.65 | 1.05 | 53 |
| over the wet one | 10 % → 11 % | 12.5 px | 0.65 | 1.15 | 43 |
| long, no reload | 18 % → 17 % | 8.1 px | 0.47 | 0.96 | 291 | quarters: 0.22 → 0.09 → 0.04 → 0.02

Numbers say: light vs heavy: width 4.3 → 15.7 px, dark 0.55 → 0.68; wet paint spreads well beyond the stroke.

## Dense Ink
Ink · 14 px · 23.2 s

![Dense Ink](Dense-Ink.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 5 % → 7 % | 15.2 px | 0.72 | 1.26 | 37 |
| heavy line | 7 % → 7 % | 19.1 px | 0.73 | 1.09 | 63 |
| pressure swell | 5 % → 6 % | 17.9 px | 0.72 | 1.17 | 43 |
| fast wave | 13 % → 13 % | 15.3 px | 0.69 | 1.01 | 146 |
| slow wave | 12 % → 12 % | 13.6 px | 0.67 | 1.04 | 152 |
| spiral | 18 % → 15 % | 12.2 px | 0.65 | 0.80 | 198 |
| loop | 11 % → 12 % | 14.8 px | 0.69 | 1.08 | 105 |
| tilted | 5 % → 6 % | 14.6 px | 0.72 | 1.07 | 52 |
| over the wet one | 12 % → 13 % | 17.7 px | 0.72 | 1.11 | 51 |
| long, no reload | 23 % → 15 % | 10.1 px | 0.64 | 0.66 | 268 | quarters: 0.30 → 0.12 → 0.04 → 0.02

Numbers say: light vs heavy: width 15.2 → 19.1 px, dark 0.72 → 0.73.

## Transparent Wash
Watercolor · 22 px · 24.0 s

![Transparent Wash](Transparent-Wash.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 2 % → 5 % | 6.9 px | 0.27 | 2.25 | 37 |
| heavy line | 7 % → 9 % | 20.4 px | 0.27 | 1.22 | 68 |
| pressure swell | 4 % → 6 % | 15.2 px | 0.28 | 1.54 | 33 |
| fast wave | 14 % → 16 % | 16.1 px | 0.20 | 1.17 | 119 |
| slow wave | 12 % → 15 % | 13.7 px | 0.21 | 1.28 | 154 |
| spiral | 18 % → 22 % | 11.9 px | 0.16 | 1.23 | 162 |
| loop | 11 % → 13 % | 14.5 px | 0.22 | 1.20 | 97 |
| tilted | 8 % → 8 % | 21.1 px | 0.24 | 1.06 | 61 |
| over the wet one | 13 % → 16 % | 16.4 px | 0.24 | 1.18 | 49 |
| long, no reload | 26 % → 32 % | 11.6 px | 0.13 | 1.22 | 262 | quarters: 0.11 → 0.04 → 0.02 → 0.01

Numbers say: light vs heavy: width 6.9 → 20.4 px, dark 0.27 → 0.27; wet paint spreads well beyond the stroke.

## Dry Brush
Gouache · 24 px · 19.1 s

![Dry Brush](Dry-Brush.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 5 % → 0 % | 14.0 px | 0.65 | 0.09 | 51 |
| heavy line | 6 % → 0 % | 18.6 px | 0.65 | 0.02 | 69 |
| pressure swell | 5 % → 0 % | 18.2 px | 0.65 | 0.08 | 46 |
| fast wave | 6 % → 1 % | 7.3 px | 0.65 | 0.08 | 139 |
| slow wave | 7 % → 0 % | 8.1 px | 0.65 | 0.06 | 227 |
| spiral | 7 % → 0 % | 4.6 px | 0.65 | 0.07 | 215 |
| loop | 10 % → 0 % | 12.4 px | 0.65 | 0.04 | 136 |
| tilted | 4 % → 3 % | 10.6 px | 0.65 | 0.88 | 60 |
| over the wet one | 9 % → 1 % | 14.5 px | 0.65 | 0.12 | 55 |
| long, no reload | 6 % → 1 % | 2.9 px | 0.65 | 0.14 | 321 | quarters: 0.12 → 0.00 → 0.00 → 0.00

Numbers say: light vs heavy: width 14.0 → 18.6 px, dark 0.65 → 0.65.

## Wax Crayon
Wax · 8 px · 9.6 s

![Wax Crayon](Wax-Crayon.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 1 % → 1 % | 2.5 px | 0.71 | 1.00 | 16 |
| heavy line | 1 % → 1 % | 3.9 px | 0.69 | 1.00 | 9 |
| pressure swell | 1 % → 1 % | 3.3 px | 0.70 | 1.00 | 6 |
| fast wave | 3 % → 3 % | 3.5 px | 0.69 | 1.00 | 29 |
| slow wave | 3 % → 3 % | 3.4 px | 0.70 | 1.00 | 37 |
| spiral | 5 % → 5 % | 3.3 px | 0.70 | 1.00 | 58 |
| loop | 3 % → 3 % | 3.3 px | 0.70 | 1.00 | 21 |
| tilted | 2 % → 2 % | 5.6 px | 0.68 | 1.00 | 19 |
| over the wet one | 3 % → 3 % | 3.6 px | 0.68 | 1.00 | 10 |
| long, no reload | 7 % → 7 % | 3.3 px | 0.70 | 1.00 | 108 | quarters: 0.06 → 0.06 → 0.06 → 0.06

Numbers say: light vs heavy: width 2.5 → 3.9 px, dark 0.71 → 0.69; the long stroke does not run out of paint.

## Oil Pastel
Wax · 12 px · 9.1 s

![Oil Pastel](Oil-Pastel.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 1 % → 1 % | 4.0 px | 0.68 | 1.00 | 22 |
| heavy line | 2 % → 2 % | 6.5 px | 0.68 | 1.00 | 21 |
| pressure swell | 2 % → 2 % | 5.7 px | 0.69 | 1.00 | 21 |
| fast wave | 5 % → 5 % | 5.7 px | 0.68 | 1.00 | 60 |
| slow wave | 5 % → 5 % | 5.5 px | 0.68 | 1.00 | 54 |
| spiral | 8 % → 8 % | 5.5 px | 0.68 | 1.00 | 90 |
| loop | 4 % → 4 % | 5.6 px | 0.68 | 1.00 | 60 |
| tilted | 2 % → 2 % | 6.8 px | 0.68 | 1.00 | 36 |
| over the wet one | 5 % → 5 % | 5.8 px | 0.68 | 1.00 | 24 |
| long, no reload | 13 % → 13 % | 5.6 px | 0.68 | 1.00 | 126 | quarters: 0.10 → 0.09 → 0.10 → 0.10

Numbers say: light vs heavy: width 4.0 → 6.5 px, dark 0.68 → 0.68; the long stroke does not run out of paint.

## Charcoal
Charcoal · 5 px · 8.9 s

![Charcoal](Charcoal.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 1 % → 1 % | 2.0 px | 0.74 | 1.00 | 14 |
| heavy line | 1 % → 1 % | 3.0 px | 0.74 | 1.00 | 6 |
| pressure swell | 1 % → 1 % | 2.7 px | 0.74 | 1.00 | 10 |
| fast wave | 2 % → 2 % | 2.7 px | 0.73 | 1.00 | 39 |
| slow wave | 2 % → 2 % | 2.6 px | 0.74 | 1.00 | 21 |
| spiral | 4 % → 4 % | 2.5 px | 0.74 | 1.00 | 54 |
| loop | 2 % → 2 % | 2.6 px | 0.74 | 1.00 | 23 |
| tilted | 2 % → 2 % | 4.3 px | 0.72 | 1.00 | 9 |
| over the wet one | 2 % → 2 % | 2.4 px | 0.72 | 1.00 | 6 |
| long, no reload | 6 % → 6 % | 2.7 px | 0.73 | 1.00 | 92 | quarters: 0.05 → 0.05 → 0.05 → 0.05

Numbers say: light vs heavy: width 2.0 → 3.0 px, dark 0.74 → 0.74; the long stroke does not run out of paint.

## Impasto
Heavy acrylic · 22 px · 13.2 s

![Impasto](Impasto.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 8 % → 8 % | 24.1 px | 0.71 | 0.93 | 35 |
| heavy line | 10 % → 9 % | 28.8 px | 0.70 | 0.94 | 75 |
| pressure swell | 7 % → 7 % | 28.1 px | 0.72 | 0.94 | 49 |
| fast wave | 20 % → 13 % | 23.5 px | 0.71 | 0.64 | 153 |
| slow wave | 21 % → 14 % | 24.5 px | 0.71 | 0.66 | 208 |
| spiral | 30 % → 14 % | 20.0 px | 0.71 | 0.46 | 220 |
| loop | 18 % → 14 % | 23.9 px | 0.71 | 0.77 | 136 |
| tilted | 8 % → 8 % | 21.8 px | 0.70 | 1.00 | 60 |
| over the wet one | 17 % → 15 % | 25.4 px | 0.70 | 0.91 | 73 |
| long, no reload | 34 % → 14 % | 15.2 px | 0.71 | 0.41 | 320 | quarters: 0.38 → 0.21 → 0.10 → 0.03

Numbers say: light vs heavy: width 24.1 → 28.8 px, dark 0.71 → 0.70.

## Oil Round
Oil · 18 px · 15.8 s

![Oil Round](Oil-Round.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 2 % → 2 % | 7.2 px | 0.75 | 1.00 | 38 |
| heavy line | 7 % → 7 % | 19.3 px | 0.73 | 1.00 | 59 |
| pressure swell | 4 % → 4 % | 13.7 px | 0.72 | 1.00 | 33 |
| fast wave | 11 % → 11 % | 12.7 px | 0.65 | 1.00 | 115 |
| slow wave | 8 % → 8 % | 9.0 px | 0.57 | 1.00 | 147 |
| spiral | 10 % → 10 % | 6.6 px | 0.50 | 1.00 | 192 |
| loop | 5 % → 5 % | 7.1 px | 0.45 | 1.00 | 89 |
| tilted | 4 % → 4 % | 10.1 px | 0.52 | 1.00 | 46 |
| over the wet one | 6 % → 6 % | 7.4 px | 0.52 | 1.00 | 49 |
| long, no reload | 15 % → 15 % | 6.8 px | 0.42 | 1.00 | 289 | quarters: 0.08 → 0.08 → 0.07 → 0.06

Numbers say: light vs heavy: width 7.2 → 19.3 px, dark 0.75 → 0.73.

## Palette Knife
Oil · 20 px · 15.7 s

![Palette Knife](Palette-Knife.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 8 % → 8 % | 21.9 px | 0.67 | 1.00 | 19 |
| heavy line | 8 % → 8 % | 22.5 px | 0.73 | 1.00 | 8 |
| pressure swell | 6 % → 6 % | 22.4 px | 0.74 | 1.00 | 7 |
| fast wave | 17 % → 17 % | 19.3 px | 0.49 | 1.00 | 22 |
| slow wave | 17 % → 17 % | 19.9 px | 0.43 | 1.00 | 33 |
| spiral | 18 % → 18 % | 11.7 px | 0.45 | 1.00 | 45 |
| loop | 16 % → 16 % | 21.0 px | 0.58 | 1.00 | 21 |
| tilted | 5 % → 5 % | 15.0 px | 0.72 | 1.00 | 16 |
| over the wet one | 13 % → 13 % | 21.0 px | 0.72 | 1.00 | 13 |
| long, no reload | 17 % → 17 % | 7.5 px | 0.47 | 1.00 | 56 | quarters: 0.29 → 0.05 → 0.00 → 0.00

Numbers say: light vs heavy: width 21.9 → 22.5 px, dark 0.67 → 0.73; pressure barely changes the width.

## Water
Watercolor · 20 px · 33.1 s · over bands of wet oil paint and oil pastel in turn (it works on paint already there: look at what it does to the bands; covered counts the bands too)

![Water](Water.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 25 % → 27 % | 73.8 px | 0.80 | 1.06 | 16 |
| heavy line | 24 % → 25 % | 69.8 px | 0.81 | 1.04 | 41 |
| pressure swell | 24 % → 25 % | 89.6 px | 0.81 | 1.03 | 26 |
| fast wave | 24 % → 26 % | 27.7 px | 0.81 | 1.07 | 136 |
| slow wave | 24 % → 25 % | 27.7 px | 0.81 | 1.06 | 143 |
| spiral | 24 % → 26 % | 15.9 px | 0.81 | 1.07 | 160 |
| loop | 24 % → 25 % | 31.1 px | 0.81 | 1.03 | 87 |
| tilted | 24 % → 24 % | 67.0 px | 0.81 | 1.00 | 48 |
| over the wet one | 24 % → 25 % | 0.0 px | 0.81 | 1.06 | 40 |
| long, no reload | 24 % → 26 % | 10.7 px | 0.81 | 1.08 | 227 | quarters: 0.21 → 0.27 → 0.18 → 0.27

Numbers say: light vs heavy: width 73.8 → 69.8 px, dark 0.80 → 0.81; pressure barely changes the width; the long stroke does not run out of paint.

## Blender
Pastel · 16 px · 18.7 s · over bands of wet oil paint and oil pastel in turn (it works on paint already there: look at what it does to the bands; covered counts the bands too)

![Blender](Blender.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 24 % → 24 % | 70.7 px | 0.81 | 1.00 | 16 |
| heavy line | 25 % → 25 % | 72.1 px | 0.80 | 1.00 | 27 |
| pressure swell | 24 % → 24 % | 91.3 px | 0.81 | 1.00 | 23 |
| fast wave | 26 % → 26 % | 30.0 px | 0.79 | 1.00 | 66 |
| slow wave | 26 % → 26 % | 29.9 px | 0.80 | 1.00 | 77 |
| spiral | 28 % → 28 % | 18.7 px | 0.77 | 1.00 | 103 |
| loop | 25 % → 25 % | 32.9 px | 0.80 | 1.00 | 57 |
| tilted | 25 % → 25 % | 70.1 px | 0.79 | 1.00 | 30 |
| over the wet one | 26 % → 26 % | 1.8 px | 0.79 | 1.00 | 35 |
| long, no reload | 30 % → 30 % | 13.7 px | 0.76 | 1.00 | 164 | quarters: 0.20 → 0.28 → 0.23 → 0.30

Numbers say: light vs heavy: width 70.7 → 72.1 px, dark 0.81 → 0.80; pressure barely changes the width; the long stroke does not run out of paint.

## Eraser
Eraser · 16 px · 18.3 s · over bands of wet oil paint and oil pastel in turn (it works on paint already there: look at what it does to the bands; covered counts the bands too)

![Eraser](Eraser.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 24 % → 24 % | 69.5 px | 0.82 | 1.00 | 19 |
| heavy line | 23 % → 23 % | 67.9 px | 0.82 | 1.00 | 22 |
| pressure swell | 23 % → 23 % | 87.3 px | 0.82 | 1.00 | 19 |
| fast wave | 22 % → 22 % | 25.7 px | 0.82 | 1.00 | 63 |
| slow wave | 22 % → 22 % | 25.7 px | 0.82 | 1.00 | 84 |
| spiral | 22 % → 22 % | 14.4 px | 0.82 | 1.00 | 107 |
| loop | 22 % → 22 % | 28.6 px | 0.82 | 1.00 | 67 |
| tilted | 23 % → 23 % | 65.1 px | 0.82 | 1.00 | 48 |
| over the wet one | 23 % → 23 % | 0.0 px | 0.82 | 1.00 | 24 |
| long, no reload | 20 % → 20 % | 8.9 px | 0.82 | 1.00 | 205 | quarters: 0.15 → 0.20 → 0.15 → 0.20

Numbers say: light vs heavy: width 69.5 → 67.9 px, dark 0.82 → 0.82; pressure barely changes the width; the long stroke does not run out of paint.

## Fan
Gouache · 30 px · 27.3 s

![Fan](Fan.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 9 % → 3 % | 25.7 px | 0.63 | 0.37 | 26 |
| heavy line | 11 % → 4 % | 31.0 px | 0.63 | 0.39 | 46 |
| pressure swell | 8 % → 5 % | 31.7 px | 0.63 | 0.55 | 30 |
| fast wave | 18 % → 5 % | 20.3 px | 0.63 | 0.26 | 86 |
| slow wave | 18 % → 5 % | 21.1 px | 0.63 | 0.25 | 153 |
| spiral | 24 % → 5 % | 15.8 px | 0.63 | 0.20 | 172 |
| loop | 17 % → 5 % | 22.7 px | 0.63 | 0.29 | 86 |
| tilted | 5 % → 6 % | 15.1 px | 0.63 | 1.05 | 31 |
| over the wet one | 16 % → 8 % | 29.8 px | 0.63 | 0.50 | 38 |
| long, no reload | 23 % → 5 % | 10.1 px | 0.63 | 0.22 | 227 | quarters: 0.29 → 0.07 → 0.01 → 0.00

Numbers say: light vs heavy: width 25.7 → 31.0 px, dark 0.63 → 0.63.

## Sponge
Gouache · 30 px · 26.9 s

![Sponge](Sponge.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 4 % → 0 % | 11.4 px | 0.62 | 0.12 | 26 |
| heavy line | 12 % → 2 % | 35.4 px | 0.62 | 0.14 | 50 |
| pressure swell | 7 % → 2 % | 27.9 px | 0.62 | 0.27 | 36 |
| fast wave | 20 % → 4 % | 23.2 px | 0.62 | 0.19 | 101 |
| slow wave | 21 % → 4 % | 23.7 px | 0.62 | 0.18 | 221 |
| spiral | 28 % → 4 % | 18.3 px | 0.62 | 0.14 | 178 |
| loop | 18 % → 5 % | 23.0 px | 0.62 | 0.29 | 95 |
| tilted | 7 % → 7 % | 18.2 px | 0.62 | 1.04 | 78 |
| over the wet one | 16 % → 6 % | 27.8 px | 0.62 | 0.37 | 44 |
| long, no reload | 29 % → 5 % | 12.9 px | 0.62 | 0.17 | 260 | quarters: 0.29 → 0.13 → 0.07 → 0.04

Numbers say: light vs heavy: width 11.4 → 35.4 px, dark 0.62 → 0.62.

## Ink — sumi brush
Watercolor · 22 px · 25.1 s

![Ink — sumi brush](Ink-sumi-brush.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 6 % → 6 % | 18.4 px | 0.43 | 0.99 | 51 |
| heavy line | 10 % → 10 % | 30.2 px | 0.37 | 0.99 | 56 |
| pressure swell | 7 % → 7 % | 27.7 px | 0.42 | 0.99 | 48 |
| fast wave | 20 % → 16 % | 23.6 px | 0.31 | 0.79 | 141 |
| slow wave | 19 % → 17 % | 22.4 px | 0.36 | 0.89 | 204 |
| spiral | 29 % → 20 % | 18.9 px | 0.31 | 0.71 | 253 |
| loop | 17 % → 17 % | 22.4 px | 0.35 | 0.97 | 135 |
| tilted | 6 % → 7 % | 16.4 px | 0.39 | 1.16 | 57 |
| over the wet one | 16 % → 15 % | 28.0 px | 0.39 | 0.95 | 57 |
| long, no reload | 34 % → 23 % | 15.1 px | 0.31 | 0.68 | 353 | quarters: 0.22 → 0.10 → 0.06 → 0.04

Numbers say: light vs heavy: width 18.4 → 30.2 px, dark 0.43 → 0.37.

## Ink — wash
Watercolor · 40 px · 28.4 s

![Ink — wash](Ink-wash.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 7 % → 9 % | 20.6 px | 0.05 | 1.21 | 60 |
| heavy line | 10 % → 12 % | 30.2 px | 0.04 | 1.11 | 75 |
| pressure swell | 7 % → 8 % | 25.9 px | 0.05 | 1.20 | 53 |
| fast wave | 21 % → 23 % | 24.7 px | 0.04 | 1.07 | 173 |
| slow wave | 20 % → 23 % | 23.5 px | 0.06 | 1.15 | 314 |
| spiral | 33 % → 35 % | 21.8 px | 0.05 | 1.05 | 282 |
| loop | 19 % → 22 % | 24.0 px | 0.05 | 1.17 | 170 |
| tilted | 7 % → 8 % | 19.6 px | 0.06 | 1.20 | 106 |
| over the wet one | 17 % → 19 % | 28.3 px | 0.06 | 1.11 | 77 |
| long, no reload | 38 % → 40 % | 17.1 px | 0.05 | 1.04 | 423 | quarters: 0.04 → 0.03 → 0.02 → 0.01

Numbers say: light vs heavy: width 20.6 → 30.2 px, dark 0.05 → 0.04.

## Ink — dry brush
Ink · 30 px · 23.0 s

![Ink — dry brush](Ink-dry-brush.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 9 % → 7 % | 25.2 px | 0.81 | 0.79 | 72 |
| heavy line | 10 % → 8 % | 29.6 px | 0.80 | 0.76 | 99 |
| pressure swell | 7 % → 6 % | 27.9 px | 0.81 | 0.85 | 74 |
| fast wave | 21 % → 8 % | 24.2 px | 0.79 | 0.40 | 217 |
| slow wave | 18 % → 7 % | 20.3 px | 0.79 | 0.39 | 380 |
| spiral | 24 % → 8 % | 15.6 px | 0.78 | 0.34 | 344 |
| loop | 19 % → 8 % | 24.3 px | 0.78 | 0.45 | 197 |
| tilted | 8 % → 8 % | 22.2 px | 0.78 | 1.02 | 105 |
| over the wet one | 17 % → 14 % | 25.9 px | 0.78 | 0.81 | 96 |
| long, no reload | 20 % → 8 % | 9.1 px | 0.79 | 0.41 | 490 | quarters: 0.32 → 0.02 → 0.00 → 0.00

Numbers say: light vs heavy: width 25.2 → 29.6 px, dark 0.81 → 0.80.

## Ink — nib
Watercolor · 5 px · 20.5 s

![Ink — nib](Ink-nib.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 1 % → 2 % | 4.3 px | 0.71 | 1.15 | 23 |
| heavy line | 2 % → 2 % | 5.0 px | 0.73 | 1.15 | 21 |
| pressure swell | 1 % → 2 % | 4.8 px | 0.74 | 1.19 | 24 |
| fast wave | 4 % → 3 % | 4.1 px | 0.65 | 0.96 | 56 |
| slow wave | 4 % → 4 % | 4.1 px | 0.65 | 1.06 | 61 |
| spiral | 5 % → 4 % | 3.4 px | 0.60 | 0.84 | 93 |
| loop | 3 % → 3 % | 4.1 px | 0.66 | 1.07 | 46 |
| tilted | 2 % → 2 % | 5.3 px | 0.63 | 1.22 | 19 |
| over the wet one | 4 % → 4 % | 5.8 px | 0.63 | 0.95 | 27 |
| long, no reload | 7 % → 5 % | 3.1 px | 0.60 | 0.70 | 158 | quarters: 0.09 → 0.04 → 0.02 → 0.02

Numbers say: light vs heavy: width 4.3 → 5.0 px, dark 0.71 → 0.73.

## 0.45 · Dry brush
Gouache · 34 px · 24.4 s

![0.45 · Dry brush](0-45-Dry-brush.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 10 % → 3 % | 29.4 px | 0.67 | 0.29 | 98 |
| heavy line | 11 % → 3 % | 31.6 px | 0.67 | 0.30 | 121 |
| pressure swell | 8 % → 3 % | 31.5 px | 0.67 | 0.41 | 69 |
| fast wave | 19 % → 3 % | 22.5 px | 0.67 | 0.18 | 280 |
| slow wave | 20 % → 4 % | 23.2 px | 0.67 | 0.18 | 459 |
| spiral | 21 % → 3 % | 14.1 px | 0.67 | 0.16 | 496 |
| loop | 20 % → 4 % | 26.1 px | 0.67 | 0.20 | 245 |
| tilted | 9 % → 8 % | 24.0 px | 0.67 | 0.98 | 148 |
| over the wet one | 19 % → 6 % | 28.2 px | 0.67 | 0.34 | 107 |
| long, no reload | 20 % → 4 % | 9.1 px | 0.67 | 0.19 | 726 | quarters: 0.36 → 0.10 → 0.00 → 0.00

Numbers say: light vs heavy: width 29.4 → 31.6 px, dark 0.67 → 0.67; pressure barely changes the width.

## Dry pastel
Pastel · 26 px · 10.0 s

![Dry pastel](Dry-pastel.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 3 % → 3 % | 8.3 px | 0.38 | 1.00 | 28 |
| heavy line | 5 % → 5 % | 13.2 px | 0.39 | 1.00 | 32 |
| pressure swell | 3 % → 3 % | 11.7 px | 0.38 | 1.00 | 33 |
| fast wave | 10 % → 10 % | 11.9 px | 0.39 | 1.00 | 81 |
| slow wave | 10 % → 10 % | 11.3 px | 0.39 | 1.00 | 144 |
| spiral | 15 % → 15 % | 9.6 px | 0.39 | 1.00 | 149 |
| loop | 7 % → 7 % | 9.4 px | 0.39 | 1.00 | 68 |
| tilted | 3 % → 3 % | 8.3 px | 0.38 | 1.00 | 48 |
| over the wet one | 7 % → 7 % | 11.1 px | 0.38 | 1.00 | 29 |
| long, no reload | 18 % → 18 % | 8.2 px | 0.39 | 1.00 | 184 | quarters: 0.08 → 0.08 → 0.08 → 0.07

Numbers say: light vs heavy: width 8.3 → 13.2 px, dark 0.38 → 0.39; the long stroke does not run out of paint.

## 0.45 · Charcoal
Charcoal · 18 px · 9.7 s

![0.45 · Charcoal](0-45-Charcoal.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 2 % → 2 % | 6.5 px | 0.80 | 1.00 | 20 |
| heavy line | 3 % → 3 % | 9.2 px | 0.80 | 1.00 | 11 |
| pressure swell | 2 % → 2 % | 8.8 px | 0.80 | 1.00 | 8 |
| fast wave | 7 % → 7 % | 8.5 px | 0.80 | 1.00 | 54 |
| slow wave | 7 % → 7 % | 8.0 px | 0.80 | 1.00 | 42 |
| spiral | 12 % → 12 % | 7.9 px | 0.80 | 1.00 | 75 |
| loop | 6 % → 6 % | 8.1 px | 0.80 | 1.00 | 22 |
| tilted | 3 % → 3 % | 7.5 px | 0.80 | 1.00 | 25 |
| over the wet one | 6 % → 6 % | 7.9 px | 0.80 | 1.00 | 18 |
| long, no reload | 17 % → 17 % | 7.8 px | 0.80 | 1.00 | 119 | quarters: 0.15 → 0.16 → 0.15 → 0.16

Numbers say: light vs heavy: width 6.5 → 9.2 px, dark 0.80 → 0.80; the long stroke does not run out of paint.

## Watercolour — wash
Watercolor · 50 px · 30.5 s

![Watercolour — wash](Watercolour-wash.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 8 % → 9 % | 23.5 px | 0.01 | 1.13 | 95 |
| heavy line | 13 % → 14 % | 37.2 px | 0.01 | 1.07 | 106 |
| pressure swell | 8 % → 9 % | 28.6 px | 0.01 | 1.12 | 72 |
| fast wave | 25 % → 27 % | 28.9 px | 0.01 | 1.10 | 241 |
| slow wave | 25 % → 28 % | 28.5 px | 0.01 | 1.13 | 428 |
| spiral | 38 % → 43 % | 25.1 px | 0.01 | 1.12 | 427 |
| loop | 22 % → 25 % | 28.3 px | 0.01 | 1.14 | 225 |
| tilted | 10 % → 11 % | 26.7 px | 0.01 | 1.13 | 157 |
| over the wet one | 20 % → 22 % | 29.3 px | 0.01 | 1.09 | 122 |
| long, no reload | 44 % → 49 % | 19.7 px | 0.01 | 1.12 | 685 | quarters: 0.01 → 0.01 → 0.00 → 0.00

Numbers say: light vs heavy: width 23.5 → 37.2 px, dark 0.01 → 0.01.

## Watercolour — wet-in-wet
Watercolor · 44 px · 28.8 s

![Watercolour — wet-in-wet](Watercolour-wet-in-wet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 7 % → 8 % | 19.2 px | 0.01 | 1.23 | 65 |
| heavy line | 11 % → 12 % | 30.8 px | 0.01 | 1.16 | 88 |
| pressure swell | 7 % → 8 % | 24.7 px | 0.01 | 1.19 | 66 |
| fast wave | 22 % → 26 % | 25.8 px | 0.01 | 1.15 | 190 |
| slow wave | 22 % → 25 % | 25.1 px | 0.01 | 1.17 | 344 |
| spiral | 35 % → 41 % | 23.1 px | 0.01 | 1.17 | 363 |
| loop | 19 % → 23 % | 25.2 px | 0.01 | 1.17 | 184 |
| tilted | 8 % → 9 % | 21.2 px | 0.01 | 1.15 | 85 |
| over the wet one | 16 % → 18 % | 24.7 px | 0.01 | 1.12 | 68 |
| long, no reload | 41 % → 48 % | 18.3 px | 0.01 | 1.18 | 565 | quarters: 0.01 → 0.00 → 0.00 → 0.00

Numbers say: light vs heavy: width 19.2 → 30.8 px, dark 0.01 → 0.01.

## Watercolour — glaze
Watercolor · 38 px · 27.5 s

![Watercolour — glaze](Watercolour-glaze.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 7 % → 8 % | 19.2 px | 0.01 | 1.17 | 66 |
| heavy line | 11 % → 13 % | 32.3 px | 0.01 | 1.15 | 81 |
| pressure swell | 6 % → 8 % | 23.9 px | 0.01 | 1.21 | 55 |
| fast wave | 19 % → 22 % | 22.3 px | 0.01 | 1.14 | 183 |
| slow wave | 19 % → 22 % | 21.9 px | 0.01 | 1.16 | 296 |
| spiral | 30 % → 32 % | 19.9 px | 0.01 | 1.06 | 313 |
| loop | 18 % → 22 % | 23.8 px | 0.01 | 1.20 | 182 |
| tilted | 7 % → 8 % | 19.2 px | 0.01 | 1.18 | 123 |
| over the wet one | 16 % → 18 % | 25.9 px | 0.01 | 1.14 | 75 |
| long, no reload | 34 % → 36 % | 15.4 px | 0.01 | 1.04 | 437 | quarters: 0.01 → 0.00 → 0.00 → 0.00

Numbers say: light vs heavy: width 19.2 → 32.3 px, dark 0.01 → 0.01.

## Watercolour — granulating
Watercolor · 44 px · 27.7 s

![Watercolour — granulating](Watercolour-granulating.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 7 % → 7 % | 19.3 px | 0.01 | 1.05 | 67 |
| heavy line | 11 % → 11 % | 31.0 px | 0.01 | 1.02 | 77 |
| pressure swell | 7 % → 7 % | 25.9 px | 0.01 | 1.05 | 53 |
| fast wave | 21 % → 20 % | 24.0 px | 0.01 | 0.99 | 192 |
| slow wave | 21 % → 21 % | 24.3 px | 0.02 | 1.02 | 366 |
| spiral | 34 % → 35 % | 22.5 px | 0.01 | 1.03 | 364 |
| loop | 17 % → 18 % | 22.5 px | 0.02 | 1.04 | 189 |
| tilted | 8 % → 8 % | 22.0 px | 0.02 | 1.08 | 145 |
| over the wet one | 17 % → 18 % | 26.4 px | 0.02 | 1.04 | 96 |
| long, no reload | 39 % → 39 % | 17.4 px | 0.02 | 1.01 | 599 | quarters: 0.01 → 0.01 → 0.01 → 0.00

Numbers say: light vs heavy: width 19.3 → 31.0 px, dark 0.01 → 0.01.

## Watercolour — dry brush
Watercolor · 36 px · 24.0 s

![Watercolour — dry brush](Watercolour-dry-brush.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 5 % → 5 % | 15.5 px | 0.06 | 0.88 | 80 |
| heavy line | 9 % → 7 % | 24.9 px | 0.05 | 0.80 | 86 |
| pressure swell | 6 % → 5 % | 22.3 px | 0.06 | 0.89 | 82 |
| fast wave | 19 % → 11 % | 21.9 px | 0.04 | 0.58 | 199 |
| slow wave | 18 % → 10 % | 20.6 px | 0.05 | 0.55 | 378 |
| spiral | 23 % → 11 % | 15.2 px | 0.04 | 0.46 | 418 |
| loop | 15 % → 11 % | 19.5 px | 0.05 | 0.73 | 235 |
| tilted | 7 % → 7 % | 18.2 px | 0.05 | 1.08 | 106 |
| over the wet one | 14 % → 13 % | 21.8 px | 0.05 | 0.88 | 110 |
| long, no reload | 21 % → 12 % | 9.6 px | 0.05 | 0.57 | 594 | quarters: 0.02 → 0.01 → 0.00 → 0.00

Numbers say: light vs heavy: width 15.5 → 24.9 px, dark 0.06 → 0.05.

## Gouache
Gouache · 30 px · 25.1 s

![Gouache](Gouache.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 8 % → 5 % | 24.4 px | 0.14 | 0.64 | 66 |
| heavy line | 14 % → 6 % | 39.7 px | 0.14 | 0.47 | 81 |
| pressure swell | 10 % → 6 % | 38.6 px | 0.14 | 0.60 | 73 |
| fast wave | 28 % → 7 % | 32.2 px | 0.14 | 0.25 | 184 |
| slow wave | 27 % → 8 % | 31.4 px | 0.14 | 0.29 | 332 |
| spiral | 38 % → 8 % | 24.8 px | 0.14 | 0.22 | 338 |
| loop | 22 % → 8 % | 28.6 px | 0.14 | 0.35 | 184 |
| tilted | 9 % → 9 % | 23.8 px | 0.14 | 1.01 | 93 |
| over the wet one | 20 % → 13 % | 31.1 px | 0.14 | 0.66 | 88 |
| long, no reload | 40 % → 9 % | 17.9 px | 0.14 | 0.24 | 474 | quarters: 0.07 → 0.04 → 0.01 → 0.01

Numbers say: light vs heavy: width 24.4 → 39.7 px, dark 0.14 → 0.14.

## Oil — alla prima
Oil · 30 px · 18.2 s

![Oil — alla prima](Oil-alla-prima.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 9 % → 9 % | 27.6 px | 0.51 | 1.00 | 84 |
| heavy line | 10 % → 10 % | 30.3 px | 0.51 | 1.00 | 78 |
| pressure swell | 8 % → 8 % | 29.8 px | 0.53 | 1.00 | 60 |
| fast wave | 24 % → 24 % | 28.1 px | 0.51 | 1.00 | 227 |
| slow wave | 26 % → 26 % | 29.5 px | 0.51 | 1.00 | 383 |
| spiral | 40 % → 40 % | 26.4 px | 0.50 | 1.00 | 387 |
| loop | 21 % → 21 % | 27.6 px | 0.52 | 1.00 | 181 |
| tilted | 11 % → 11 % | 30.4 px | 0.51 | 1.00 | 111 |
| over the wet one | 20 % → 20 % | 26.5 px | 0.51 | 1.00 | 96 |
| long, no reload | 49 % → 49 % | 22.0 px | 0.50 | 1.00 | 537 | quarters: 0.32 → 0.28 → 0.25 → 0.22

Numbers say: light vs heavy: width 27.6 → 30.3 px, dark 0.51 → 0.51; pressure barely changes the width.

## Oil — impasto
Oil · 34 px · 19.3 s

![Oil — impasto](Oil-impasto.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 12 % → 12 % | 33.4 px | 0.25 | 1.00 | 90 |
| heavy line | 12 % → 12 % | 36.3 px | 0.25 | 1.00 | 98 |
| pressure swell | 10 % → 10 % | 35.9 px | 0.26 | 1.00 | 88 |
| fast wave | 30 % → 30 % | 35.1 px | 0.25 | 1.00 | 272 |
| slow wave | 31 % → 31 % | 35.7 px | 0.25 | 1.00 | 470 |
| spiral | 52 % → 52 % | 34.0 px | 0.23 | 1.00 | 454 |
| loop | 26 % → 26 % | 33.7 px | 0.24 | 1.00 | 249 |
| tilted | 12 % → 12 % | 32.8 px | 0.26 | 1.00 | 140 |
| over the wet one | 23 % → 23 % | 31.9 px | 0.26 | 1.00 | 114 |
| long, no reload | 60 % → 60 % | 26.9 px | 0.22 | 1.00 | 694 | quarters: 0.18 → 0.16 → 0.13 → 0.10

Numbers say: light vs heavy: width 33.4 → 36.3 px, dark 0.25 → 0.25; pressure barely changes the width.

## Oil — glaze
Oil · 40 px · 15.2 s

![Oil — glaze](Oil-glaze.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 9 % → 9 % | 25.4 px | 0.50 | 1.00 | 95 |
| heavy line | 13 % → 13 % | 36.3 px | 0.49 | 1.00 | 134 |
| pressure swell | 9 % → 9 % | 35.3 px | 0.50 | 1.00 | 81 |
| fast wave | 26 % → 26 % | 30.1 px | 0.48 | 1.00 | 273 |
| slow wave | 29 % → 29 % | 33.7 px | 0.49 | 1.00 | 446 |
| spiral | 44 % → 44 % | 29.0 px | 0.49 | 1.00 | 491 |
| loop | 23 % → 23 % | 30.2 px | 0.50 | 1.00 | 240 |
| tilted | 10 % → 10 % | 28.9 px | 0.50 | 1.00 | 133 |
| over the wet one | 22 % → 22 % | 31.6 px | 0.50 | 1.00 | 116 |
| long, no reload | 51 % → 51 % | 22.7 px | 0.49 | 1.00 | 668 | quarters: 0.33 → 0.29 → 0.26 → 0.22

Numbers say: light vs heavy: width 25.4 → 36.3 px, dark 0.50 → 0.49.

## Oil — scumble
Oil · 36 px · 19.9 s

![Oil — scumble](Oil-scumble.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 11 % → 11 % | 33.1 px | 0.08 | 1.00 | 180 |
| heavy line | 12 % → 12 % | 36.1 px | 0.07 | 1.00 | 134 |
| pressure swell | 9 % → 9 % | 35.5 px | 0.07 | 1.00 | 98 |
| fast wave | 26 % → 26 % | 29.6 px | 0.06 | 1.00 | 337 |
| slow wave | 27 % → 27 % | 30.9 px | 0.05 | 1.00 | 525 |
| spiral | 41 % → 41 % | 27.1 px | 0.04 | 1.00 | 581 |
| loop | 24 % → 24 % | 30.6 px | 0.06 | 1.00 | 275 |
| tilted | 11 % → 11 % | 30.4 px | 0.07 | 1.00 | 153 |
| over the wet one | 22 % → 22 % | 31.4 px | 0.07 | 1.00 | 128 |
| long, no reload | 45 % → 45 % | 20.3 px | 0.04 | 1.00 | 880 | quarters: 0.04 → 0.02 → 0.01 → 0.00

Numbers say: light vs heavy: width 33.1 → 36.1 px, dark 0.08 → 0.07; pressure barely changes the width.

## Acrylic — heavy body
Heavy acrylic · 30 px · 15.0 s

![Acrylic — heavy body](Acrylic-heavy-body.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 10 % → 9 % | 28.9 px | 0.51 | 0.91 | 90 |
| heavy line | 11 % → 10 % | 31.1 px | 0.51 | 0.93 | 87 |
| pressure swell | 8 % → 8 % | 30.7 px | 0.53 | 0.94 | 67 |
| fast wave | 23 % → 15 % | 26.5 px | 0.52 | 0.64 | 232 |
| slow wave | 24 % → 16 % | 27.7 px | 0.51 | 0.65 | 468 |
| spiral | 35 % → 15 % | 23.3 px | 0.51 | 0.43 | 404 |
| loop | 21 % → 16 % | 26.9 px | 0.51 | 0.76 | 224 |
| tilted | 9 % → 9 % | 24.9 px | 0.52 | 0.99 | 115 |
| over the wet one | 19 % → 17 % | 27.7 px | 0.52 | 0.89 | 89 |
| long, no reload | 39 % → 16 % | 17.3 px | 0.51 | 0.41 | 523 | quarters: 0.29 → 0.20 → 0.12 → 0.04

Numbers say: light vs heavy: width 28.9 → 31.1 px, dark 0.51 → 0.51; pressure barely changes the width.

## Acrylic — fluid
Watercolor · 36 px · 30.5 s

![Acrylic — fluid](Acrylic-fluid.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 8 % → 8 % | 22.6 px | 0.06 | 1.03 | 68 |
| heavy line | 12 % → 12 % | 35.0 px | 0.05 | 0.99 | 81 |
| pressure swell | 7 % → 7 % | 27.4 px | 0.06 | 0.99 | 44 |
| fast wave | 25 % → 24 % | 28.7 px | 0.05 | 0.95 | 209 |
| slow wave | 23 % → 23 % | 26.9 px | 0.06 | 1.01 | 334 |
| spiral | 36 % → 35 % | 23.6 px | 0.05 | 0.97 | 330 |
| loop | 21 % → 22 % | 27.2 px | 0.06 | 1.03 | 181 |
| tilted | 8 % → 9 % | 22.5 px | 0.06 | 1.12 | 104 |
| over the wet one | 19 % → 19 % | 30.7 px | 0.06 | 1.01 | 81 |
| long, no reload | 41 % → 40 % | 18.3 px | 0.05 | 0.98 | 545 | quarters: 0.04 → 0.03 → 0.02 → 0.01

Numbers say: light vs heavy: width 22.6 → 35.0 px, dark 0.06 → 0.05.

## Acrylic — palette knife
Heavy acrylic · 42 px · 20.9 s

![Acrylic — palette knife](Acrylic-palette-knife.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 15 % → 15 % | 44.0 px | 0.06 | 0.98 | 23 |
| heavy line | 15 % → 15 % | 44.2 px | 0.05 | 0.97 | 21 |
| pressure swell | 12 % → 12 % | 43.5 px | 0.07 | 0.99 | 10 |
| fast wave | 36 % → 20 % | 41.9 px | 0.06 | 0.56 | 48 |
| slow wave | 37 % → 21 % | 42.6 px | 0.06 | 0.57 | 89 |
| spiral | 50 % → 18 % | 32.8 px | 0.07 | 0.37 | 89 |
| loop | 32 % → 24 % | 41.2 px | 0.06 | 0.75 | 47 |
| tilted | 12 % → 12 % | 33.6 px | 0.06 | 1.00 | 22 |
| over the wet one | 26 % → 25 % | 39.7 px | 0.06 | 0.97 | 26 |
| long, no reload | 57 % → 21 % | 25.7 px | 0.06 | 0.36 | 191 | quarters: 0.04 → 0.02 → 0.00 → 0.00

Numbers say: light vs heavy: width 44.0 → 44.2 px, dark 0.06 → 0.05; pressure barely changes the width.

## Finger on oil
Oil · 30 px · 14.9 s

![Finger on oil](Finger-on-oil.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 8 % → 8 % | 23.7 px | 0.40 | 1.00 | 54 |
| heavy line | 13 % → 13 % | 36.5 px | 0.38 | 1.00 | 61 |
| pressure swell | 9 % → 9 % | 33.3 px | 0.41 | 1.00 | 42 |
| fast wave | 22 % → 22 % | 26.0 px | 0.35 | 1.00 | 126 |
| slow wave | 24 % → 24 % | 27.8 px | 0.35 | 1.00 | 274 |
| spiral | 36 % → 36 % | 23.5 px | 0.27 | 1.00 | 219 |
| loop | 21 % → 21 % | 27.3 px | 0.36 | 1.00 | 118 |
| tilted | 9 % → 9 % | 26.4 px | 0.39 | 1.00 | 87 |
| over the wet one | 20 % → 20 % | 29.3 px | 0.39 | 1.00 | 42 |
| long, no reload | 36 % → 36 % | 16.3 px | 0.26 | 1.00 | 283 | quarters: 0.23 → 0.11 → 0.05 → 0.02

Numbers say: light vs heavy: width 23.7 → 36.5 px, dark 0.40 → 0.38.

## Palette knife — oil
Oil · 44 px · 21.4 s

![Palette knife — oil](Palette-knife-oil.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 16 % → 16 % | 45.6 px | 0.12 | 1.00 | 23 |
| heavy line | 16 % → 16 % | 46.3 px | 0.11 | 1.00 | 25 |
| pressure swell | 12 % → 12 % | 45.2 px | 0.12 | 1.00 | 13 |
| fast wave | 39 % → 39 % | 44.9 px | 0.11 | 1.00 | 50 |
| slow wave | 39 % → 39 % | 45.4 px | 0.11 | 1.00 | 117 |
| spiral | 62 % → 62 % | 40.9 px | 0.08 | 1.00 | 126 |
| loop | 34 % → 34 % | 43.8 px | 0.11 | 1.00 | 47 |
| tilted | 13 % → 13 % | 36.6 px | 0.11 | 1.00 | 43 |
| over the wet one | 28 % → 28 % | 40.8 px | 0.11 | 1.00 | 42 |
| long, no reload | 74 % → 74 % | 33.1 px | 0.08 | 1.00 | 187 | quarters: 0.10 → 0.07 → 0.05 → 0.04

Numbers say: light vs heavy: width 45.6 → 46.3 px, dark 0.12 → 0.11; pressure barely changes the width.

## 0.45 · Sponge
Watercolor · 46 px · 25.3 s

![0.45 · Sponge](0-45-Sponge.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 9 % → 0 % | 26.5 px | 0.00 | 0.00 | 42 |
| heavy line | 12 % → 0 % | 35.5 px | 0.00 | 0.00 | 63 |
| pressure swell | 8 % → 0 % | 30.7 px | 0.01 | 0.05 | 55 |
| fast wave | 18 % → 0 % | 20.4 px | 0.01 | 0.02 | 163 |
| slow wave | 25 % → 3 % | 29.0 px | 0.02 | 0.14 | 417 |
| spiral | 31 % → 5 % | 20.2 px | 0.02 | 0.17 | 316 |
| loop | 21 % → 2 % | 27.1 px | 0.02 | 0.12 | 275 |
| tilted | 8 % → 10 % | 23.1 px | 0.05 | 1.17 | 125 |
| over the wet one | 19 % → 6 % | 29.5 px | 0.05 | 0.31 | 86 |
| long, no reload | 36 % → 8 % | 16.1 px | 0.02 | 0.22 | 393 | quarters: 0.01 → 0.01 → 0.01 → 0.01

Numbers say: light vs heavy: width 26.5 → 35.5 px, dark 0.00 → 0.00.

## 0.45 · Eraser
Eraser · 30 px · 22.3 s · over bands of wet oil paint and oil pastel in turn (it works on paint already there: look at what it does to the bands; covered counts the bands too)

![0.45 · Eraser](0-45-Eraser.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 24 % → 24 % | 69.2 px | 0.82 | 1.00 | 61 |
| heavy line | 23 % → 23 % | 67.4 px | 0.81 | 1.00 | 60 |
| pressure swell | 23 % → 23 % | 86.7 px | 0.82 | 1.00 | 42 |
| fast wave | 21 % → 21 % | 24.7 px | 0.81 | 1.00 | 116 |
| slow wave | 20 % → 20 % | 23.5 px | 0.82 | 1.00 | 188 |
| spiral | 20 % → 20 % | 13.5 px | 0.79 | 1.00 | 213 |
| loop | 21 % → 21 % | 27.8 px | 0.80 | 1.00 | 107 |
| tilted | 23 % → 23 % | 64.8 px | 0.81 | 1.00 | 66 |
| over the wet one | 22 % → 22 % | 0.0 px | 0.81 | 1.00 | 46 |
| long, no reload | 17 % → 17 % | 7.5 px | 0.79 | 1.00 | 320 | quarters: 0.13 → 0.16 → 0.13 → 0.17

Numbers say: light vs heavy: width 69.2 → 67.4 px, dark 0.82 → 0.81; pressure barely changes the width; the long stroke does not run out of paint.

## Lift wet paint
Eraser · 30 px · 21.8 s · over bands of wet oil paint and oil pastel in turn (it works on paint already there: look at what it does to the bands; covered counts the bands too)

![Lift wet paint](Lift-wet-paint.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 24 % → 24 % | 70.1 px | 0.82 | 1.00 | 41 |
| heavy line | 24 % → 24 % | 69.8 px | 0.82 | 1.00 | 57 |
| pressure swell | 24 % → 24 % | 89.5 px | 0.82 | 1.00 | 34 |
| fast wave | 24 % → 24 % | 27.7 px | 0.82 | 1.00 | 106 |
| slow wave | 24 % → 24 % | 27.7 px | 0.82 | 1.00 | 216 |
| spiral | 24 % → 24 % | 15.9 px | 0.82 | 1.00 | 181 |
| loop | 24 % → 24 % | 31.1 px | 0.82 | 1.00 | 92 |
| tilted | 24 % → 24 % | 66.8 px | 0.82 | 1.00 | 41 |
| over the wet one | 24 % → 24 % | 0.0 px | 0.82 | 1.00 | 30 |
| long, no reload | 24 % → 24 % | 10.7 px | 0.82 | 1.00 | 214 | quarters: 0.18 → 0.24 → 0.17 → 0.24

Numbers say: light vs heavy: width 70.1 → 69.8 px, dark 0.82 → 0.82; pressure barely changes the width; the long stroke does not run out of paint.

## Sgraffito
Eraser · 10 px · 21.3 s · over bands of wet oil paint and oil pastel in turn (it works on paint already there: look at what it does to the bands; covered counts the bands too)

![Sgraffito](Sgraffito.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 24 % → 24 % | 69.5 px | 0.81 | 1.00 | 10 |
| heavy line | 24 % → 24 % | 69.5 px | 0.82 | 1.00 | 10 |
| pressure swell | 24 % → 24 % | 89.5 px | 0.82 | 1.00 | 11 |
| fast wave | 24 % → 24 % | 27.4 px | 0.82 | 1.00 | 27 |
| slow wave | 24 % → 24 % | 27.4 px | 0.81 | 1.00 | 48 |
| spiral | 24 % → 24 % | 15.7 px | 0.81 | 1.00 | 81 |
| loop | 24 % → 24 % | 30.9 px | 0.82 | 1.00 | 27 |
| tilted | 24 % → 24 % | 66.6 px | 0.82 | 1.00 | 12 |
| over the wet one | 24 % → 24 % | 0.0 px | 0.82 | 1.00 | 10 |
| long, no reload | 24 % → 24 % | 10.6 px | 0.82 | 1.00 | 69 | quarters: 0.17 → 0.24 → 0.17 → 0.24

Numbers say: light vs heavy: width 69.5 → 69.5 px, dark 0.81 → 0.82; pressure barely changes the width; the long stroke does not run out of paint.

## Brush Artist · Refs · #01 Henry Ward peach cloud
Gouache · 44 px · 40.5 s

![Brush Artist · Refs · #01 Henry Ward peach cloud](Brush-Artist-Refs-01-Henry-Ward-peach-cloud.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 15 % → 13 % | 42.3 px | 0.10 | 0.87 | 119 |
| heavy line | 16 % → 14 % | 45.7 px | 0.10 | 0.91 | 135 |
| pressure swell | 12 % → 11 % | 44.3 px | 0.10 | 0.92 | 159 |
| fast wave | 38 % → 25 % | 43.9 px | 0.10 | 0.65 | 493 |
| slow wave | 38 % → 26 % | 43.6 px | 0.10 | 0.68 | 864 |
| spiral | 61 % → 28 % | 40.2 px | 0.10 | 0.46 | 638 |
| loop | 32 % → 26 % | 41.6 px | 0.10 | 0.81 | 336 |
| tilted | 13 % → 13 % | 36.8 px | 0.10 | 1.00 | 215 |
| over the wet one | 27 % → 26 % | 39.2 px | 0.10 | 0.95 | 190 |
| long, no reload | 72 % → 28 % | 32.2 px | 0.10 | 0.40 | 1116 | quarters: 0.08 → 0.07 → 0.06 → 0.03

Numbers say: light vs heavy: width 42.3 → 45.7 px, dark 0.10 → 0.10; pressure barely changes the width.

## Brush Artist · Refs · #02 Henry Ward cream strokes
Gouache · 46 px · 40.3 s

![Brush Artist · Refs · #02 Henry Ward cream strokes](Brush-Artist-Refs-02-Henry-Ward-cream-strokes.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 14 % → 13 % | 41.4 px | 0.02 | 0.94 | 152 |
| heavy line | 15 % → 15 % | 44.5 px | 0.02 | 0.96 | 240 |
| pressure swell | 12 % → 11 % | 43.9 px | 0.01 | 0.95 | 131 |
| fast wave | 36 % → 25 % | 41.9 px | 0.02 | 0.69 | 566 |
| slow wave | 36 % → 25 % | 41.8 px | 0.02 | 0.70 | 776 |
| spiral | 59 % → 28 % | 39.2 px | 0.02 | 0.46 | 656 |
| loop | 31 % → 27 % | 40.3 px | 0.02 | 0.86 | 427 |
| tilted | 13 % → 13 % | 37.3 px | 0.02 | 1.00 | 213 |
| over the wet one | 27 % → 26 % | 38.4 px | 0.02 | 0.96 | 191 |
| long, no reload | 70 % → 29 % | 31.3 px | 0.02 | 0.41 | 1081 | quarters: 0.01 → 0.02 → 0.02 → 0.01

Numbers say: light vs heavy: width 41.4 → 44.5 px, dark 0.02 → 0.02; pressure barely changes the width; the long stroke does not run out of paint.

## Brush Artist · Refs · #03 Henry Ward navy contours
Heavy acrylic · 22 px · 16.0 s

![Brush Artist · Refs · #03 Henry Ward navy contours](Brush-Artist-Refs-03-Henry-Ward-navy-contours.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 7 % → 7 % | 21.5 px | 0.70 | 0.94 | 86 |
| heavy line | 8 % → 8 % | 23.4 px | 0.70 | 0.95 | 94 |
| pressure swell | 6 % → 6 % | 23.2 px | 0.73 | 0.94 | 57 |
| fast wave | 19 % → 12 % | 21.8 px | 0.72 | 0.66 | 225 |
| slow wave | 19 % → 13 % | 22.4 px | 0.72 | 0.69 | 304 |
| spiral | 30 % → 13 % | 19.5 px | 0.72 | 0.45 | 355 |
| loop | 17 % → 13 % | 21.4 px | 0.72 | 0.81 | 179 |
| tilted | 8 % → 8 % | 22.6 px | 0.71 | 1.00 | 97 |
| over the wet one | 16 % → 14 % | 21.2 px | 0.71 | 0.89 | 90 |
| long, no reload | 34 % → 14 % | 15.1 px | 0.72 | 0.40 | 649 | quarters: 0.35 → 0.29 → 0.20 → 0.08

Numbers say: light vs heavy: width 21.5 → 23.4 px, dark 0.70 → 0.70; pressure barely changes the width.

## Brush Artist · Refs · #04 Henry Ward grey cloud
Gouache · 50 px · 40.9 s

![Brush Artist · Refs · #04 Henry Ward grey cloud](Brush-Artist-Refs-04-Henry-Ward-grey-cloud.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 16 % → 15 % | 47.1 px | 0.11 | 0.90 | 266 |
| heavy line | 17 % → 16 % | 50.6 px | 0.11 | 0.94 | 224 |
| pressure swell | 13 % → 12 % | 49.2 px | 0.11 | 0.94 | 127 |
| fast wave | 41 % → 28 % | 47.4 px | 0.11 | 0.67 | 406 |
| slow wave | 41 % → 28 % | 47.2 px | 0.11 | 0.69 | 792 |
| spiral | 63 % → 30 % | 41.3 px | 0.11 | 0.48 | 973 |
| loop | 35 % → 29 % | 45.6 px | 0.11 | 0.84 | 391 |
| tilted | 14 % → 14 % | 40.3 px | 0.11 | 1.00 | 240 |
| over the wet one | 30 % → 29 % | 43.2 px | 0.11 | 0.96 | 191 |
| long, no reload | 76 % → 32 % | 33.9 px | 0.11 | 0.43 | 1118 | quarters: 0.09 → 0.08 → 0.06 → 0.03

Numbers say: light vs heavy: width 47.1 → 50.6 px, dark 0.11 → 0.11; pressure barely changes the width.

## Brush Artist · Refs · #05 Henry Ward green in rust loops
Heavy acrylic · 20 px · 15.4 s

![Brush Artist · Refs · #05 Henry Ward green in rust loops](Brush-Artist-Refs-05-Henry-Ward-green-in-rust-loops.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 7 % → 6 % | 19.5 px | 0.55 | 0.94 | 72 |
| heavy line | 7 % → 7 % | 21.2 px | 0.55 | 0.94 | 93 |
| pressure swell | 6 % → 5 % | 21.5 px | 0.57 | 0.92 | 54 |
| fast wave | 17 % → 11 % | 19.7 px | 0.56 | 0.64 | 201 |
| slow wave | 18 % → 12 % | 20.3 px | 0.56 | 0.66 | 300 |
| spiral | 27 % → 12 % | 17.9 px | 0.55 | 0.42 | 310 |
| loop | 15 % → 12 % | 19.5 px | 0.55 | 0.80 | 166 |
| tilted | 8 % → 8 % | 21.7 px | 0.56 | 1.00 | 108 |
| over the wet one | 15 % → 13 % | 19.1 px | 0.56 | 0.87 | 75 |
| long, no reload | 30 % → 12 % | 13.4 px | 0.56 | 0.39 | 549 | quarters: 0.25 → 0.18 → 0.10 → 0.02

Numbers say: light vs heavy: width 19.5 → 21.2 px, dark 0.55 → 0.55; pressure barely changes the width.

## Brush Artist · Refs · #06 Henry Ward scrubbed grey
Gouache · 50 px · 39.9 s

![Brush Artist · Refs · #06 Henry Ward scrubbed grey](Brush-Artist-Refs-06-Henry-Ward-scrubbed-grey.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 16 % → 15 % | 47.1 px | 0.09 | 0.90 | 184 |
| heavy line | 17 % → 16 % | 50.6 px | 0.09 | 0.94 | 221 |
| pressure swell | 13 % → 12 % | 49.2 px | 0.09 | 0.94 | 128 |
| fast wave | 41 % → 28 % | 47.4 px | 0.09 | 0.67 | 533 |
| slow wave | 41 % → 28 % | 47.2 px | 0.09 | 0.69 | 847 |
| spiral | 63 % → 30 % | 41.3 px | 0.09 | 0.48 | 790 |
| loop | 35 % → 29 % | 45.6 px | 0.09 | 0.84 | 465 |
| tilted | 14 % → 14 % | 40.3 px | 0.09 | 1.00 | 210 |
| over the wet one | 30 % → 29 % | 43.2 px | 0.09 | 0.96 | 196 |
| long, no reload | 76 % → 32 % | 33.9 px | 0.09 | 0.43 | 1099 | quarters: 0.08 → 0.07 → 0.05 → 0.03

Numbers say: light vs heavy: width 47.1 → 50.6 px, dark 0.09 → 0.09; pressure barely changes the width.

## Brush Artist · Refs · #07 Henry Ward blue L + black zigzag
Heavy acrylic · 34 px · 18.0 s

![Brush Artist · Refs · #07 Henry Ward blue L + black zigzag](Brush-Artist-Refs-07-Henry-Ward-blue-L-black-zigzag.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 11 % → 11 % | 33.1 px | 0.57 | 0.93 | 113 |
| heavy line | 12 % → 11 % | 35.7 px | 0.57 | 0.93 | 141 |
| pressure swell | 9 % → 9 % | 35.2 px | 0.59 | 0.94 | 78 |
| fast wave | 29 % → 20 % | 33.6 px | 0.59 | 0.69 | 268 |
| slow wave | 30 % → 21 % | 34.1 px | 0.58 | 0.73 | 508 |
| spiral | 47 % → 22 % | 31.3 px | 0.58 | 0.46 | 536 |
| loop | 25 % → 21 % | 32.7 px | 0.58 | 0.82 | 295 |
| tilted | 11 % → 11 % | 29.8 px | 0.58 | 1.00 | 124 |
| over the wet one | 22 % → 20 % | 31.7 px | 0.58 | 0.91 | 111 |
| long, no reload | 53 % → 22 % | 23.8 px | 0.59 | 0.42 | 674 | quarters: 0.40 → 0.32 → 0.21 → 0.10

Numbers say: light vs heavy: width 33.1 → 35.7 px, dark 0.57 → 0.57; pressure barely changes the width.

## Brush Artist · Refs · #08 Henry Ward olive bands
Gouache · 34 px · 24.9 s

![Brush Artist · Refs · #08 Henry Ward olive bands](Brush-Artist-Refs-08-Henry-Ward-olive-bands.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 8 % → 2 % | 24.7 px | 0.57 | 0.27 | 61 |
| heavy line | 12 % → 3 % | 33.9 px | 0.57 | 0.22 | 153 |
| pressure swell | 8 % → 3 % | 30.8 px | 0.57 | 0.38 | 88 |
| fast wave | 25 % → 4 % | 29.2 px | 0.57 | 0.15 | 323 |
| slow wave | 25 % → 4 % | 28.9 px | 0.57 | 0.15 | 620 |
| spiral | 39 % → 4 % | 25.7 px | 0.57 | 0.10 | 434 |
| loop | 22 % → 5 % | 28.8 px | 0.57 | 0.21 | 252 |
| tilted | 10 % → 10 % | 28.6 px | 0.57 | 0.98 | 126 |
| over the wet one | 20 % → 8 % | 28.3 px | 0.57 | 0.40 | 133 |
| long, no reload | 45 % → 6 % | 20.0 px | 0.57 | 0.13 | 699 | quarters: 0.35 → 0.27 → 0.17 → 0.08

Numbers say: light vs heavy: width 24.7 → 33.9 px, dark 0.57 → 0.57.

## Brush Artist · Refs · #09 Henry Ward white loops
Gouache · 46 px · 38.4 s

![Brush Artist · Refs · #09 Henry Ward white loops](Brush-Artist-Refs-09-Henry-Ward-white-loops.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 14 % → 13 % | 41.4 px | 0.01 | 0.94 | 166 |
| heavy line | 15 % → 15 % | 44.5 px | 0.02 | 0.96 | 236 |
| pressure swell | 12 % → 11 % | 43.9 px | 0.02 | 0.95 | 124 |
| fast wave | 36 % → 25 % | 41.9 px | 0.01 | 0.69 | 416 |
| slow wave | 36 % → 25 % | 41.8 px | 0.01 | 0.70 | 753 |
| spiral | 59 % → 28 % | 39.2 px | 0.01 | 0.46 | 699 |
| loop | 31 % → 27 % | 40.3 px | 0.01 | 0.86 | 369 |
| tilted | 13 % → 13 % | 37.3 px | 0.01 | 1.00 | 209 |
| over the wet one | 27 % → 26 % | 38.4 px | 0.01 | 0.96 | 170 |
| long, no reload | 70 % → 29 % | 31.3 px | 0.01 | 0.41 | 1038 | quarters: 0.00 → 0.01 → 0.02 → 0.01

Numbers say: light vs heavy: width 41.4 → 44.5 px, dark 0.01 → 0.02; pressure barely changes the width; the long stroke does not run out of paint.

## Brush Artist · Refs · #10 Henry Ward maroon loops
Heavy acrylic · 30 px · 15.4 s

![Brush Artist · Refs · #10 Henry Ward maroon loops](Brush-Artist-Refs-10-Henry-Ward-maroon-loops.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 10 % → 9 % | 28.0 px | 0.70 | 0.94 | 111 |
| heavy line | 10 % → 10 % | 30.2 px | 0.69 | 0.95 | 134 |
| pressure swell | 8 % → 8 % | 30.0 px | 0.73 | 0.94 | 88 |
| fast wave | 24 % → 17 % | 28.3 px | 0.73 | 0.71 | 252 |
| slow wave | 25 % → 18 % | 29.0 px | 0.73 | 0.73 | 451 |
| spiral | 39 % → 18 % | 26.0 px | 0.72 | 0.47 | 413 |
| loop | 21 % → 18 % | 27.6 px | 0.72 | 0.85 | 223 |
| tilted | 10 % → 10 % | 27.9 px | 0.72 | 1.00 | 133 |
| over the wet one | 20 % → 18 % | 26.8 px | 0.72 | 0.91 | 115 |
| long, no reload | 46 % → 18 % | 20.6 px | 0.73 | 0.40 | 599 | quarters: 0.44 → 0.38 → 0.31 → 0.22

Numbers say: light vs heavy: width 28.0 → 30.2 px, dark 0.70 → 0.69; pressure barely changes the width.

## Brush Artist · Refs · #11 Henry Ward purple spun balls
Heavy acrylic · 36 px · 17.4 s

![Brush Artist · Refs · #11 Henry Ward purple spun balls](Brush-Artist-Refs-11-Henry-Ward-purple-spun-balls.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 12 % → 11 % | 34.1 px | 0.70 | 0.96 | 112 |
| heavy line | 13 % → 12 % | 36.6 px | 0.70 | 0.96 | 146 |
| pressure swell | 10 % → 9 % | 36.2 px | 0.74 | 0.95 | 85 |
| fast wave | 30 % → 23 % | 34.6 px | 0.73 | 0.75 | 313 |
| slow wave | 30 % → 24 % | 35.0 px | 0.73 | 0.79 | 493 |
| spiral | 49 % → 25 % | 32.3 px | 0.73 | 0.50 | 526 |
| loop | 26 % → 23 % | 33.4 px | 0.73 | 0.88 | 275 |
| tilted | 11 % → 11 % | 31.2 px | 0.72 | 1.00 | 127 |
| over the wet one | 23 % → 21 % | 32.1 px | 0.72 | 0.93 | 138 |
| long, no reload | 55 % → 24 % | 24.8 px | 0.73 | 0.44 | 754 | quarters: 0.51 → 0.46 → 0.39 → 0.28

Numbers say: light vs heavy: width 34.1 → 36.6 px, dark 0.70 → 0.70; pressure barely changes the width.

## Brush Artist · Refs · #12 Henry Ward black-olive cage
Gouache · 28 px · 23.6 s

![Brush Artist · Refs · #12 Henry Ward black-olive cage](Brush-Artist-Refs-12-Henry-Ward-black-olive-cage.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 7 % → 3 % | 20.9 px | 0.61 | 0.35 | 56 |
| heavy line | 9 % → 4 % | 26.1 px | 0.61 | 0.41 | 106 |
| pressure swell | 6 % → 4 % | 23.9 px | 0.61 | 0.61 | 69 |
| fast wave | 20 % → 4 % | 23.7 px | 0.61 | 0.19 | 221 |
| slow wave | 20 % → 4 % | 23.3 px | 0.61 | 0.21 | 388 |
| spiral | 32 % → 4 % | 21.4 px | 0.61 | 0.14 | 358 |
| loop | 18 % → 5 % | 22.8 px | 0.61 | 0.28 | 227 |
| tilted | 9 % → 9 % | 25.4 px | 0.61 | 0.98 | 89 |
| over the wet one | 17 % → 8 % | 21.8 px | 0.61 | 0.46 | 91 |
| long, no reload | 39 % → 6 % | 17.6 px | 0.61 | 0.15 | 552 | quarters: 0.31 → 0.26 → 0.19 → 0.10

Numbers say: light vs heavy: width 20.9 → 26.1 px, dark 0.61 → 0.61.

## Brush Artist · Refs · #13 Henry Ward blue streaky form
Gouache · 50 px · 39.1 s

![Brush Artist · Refs · #13 Henry Ward blue streaky form](Brush-Artist-Refs-13-Henry-Ward-blue-streaky-form.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 16 % → 15 % | 47.1 px | 0.09 | 0.90 | 170 |
| heavy line | 17 % → 16 % | 50.6 px | 0.09 | 0.94 | 136 |
| pressure swell | 13 % → 12 % | 49.2 px | 0.09 | 0.94 | 122 |
| fast wave | 41 % → 28 % | 47.4 px | 0.09 | 0.67 | 433 |
| slow wave | 41 % → 28 % | 47.2 px | 0.09 | 0.69 | 761 |
| spiral | 63 % → 30 % | 41.3 px | 0.09 | 0.48 | 701 |
| loop | 35 % → 29 % | 45.6 px | 0.09 | 0.84 | 359 |
| tilted | 14 % → 14 % | 40.3 px | 0.09 | 1.00 | 201 |
| over the wet one | 30 % → 29 % | 43.2 px | 0.09 | 0.96 | 199 |
| long, no reload | 76 % → 32 % | 33.9 px | 0.09 | 0.43 | 1023 | quarters: 0.08 → 0.07 → 0.05 → 0.03

Numbers say: light vs heavy: width 47.1 → 50.6 px, dark 0.09 → 0.09; pressure barely changes the width.

## Brush Artist · Refs · #14 Henry Ward olive totem
Heavy acrylic · 48 px · 19.6 s

![Brush Artist · Refs · #14 Henry Ward olive totem](Brush-Artist-Refs-14-Henry-Ward-olive-totem.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 15 % → 15 % | 44.8 px | 0.31 | 0.94 | 138 |
| heavy line | 16 % → 16 % | 47.7 px | 0.31 | 0.95 | 148 |
| pressure swell | 13 % → 12 % | 47.0 px | 0.32 | 0.95 | 130 |
| fast wave | 38 % → 30 % | 43.9 px | 0.30 | 0.79 | 397 |
| slow wave | 39 % → 31 % | 44.5 px | 0.30 | 0.81 | 643 |
| spiral | 58 % → 32 % | 38.1 px | 0.30 | 0.55 | 648 |
| loop | 33 % → 29 % | 42.6 px | 0.30 | 0.89 | 429 |
| tilted | 13 % → 13 % | 37.5 px | 0.31 | 1.00 | 190 |
| over the wet one | 28 % → 26 % | 41.1 px | 0.31 | 0.93 | 157 |
| long, no reload | 67 % → 33 % | 30.3 px | 0.30 | 0.49 | 947 | quarters: 0.25 → 0.18 → 0.10 → 0.03

Numbers say: light vs heavy: width 44.8 → 47.7 px, dark 0.31 → 0.31; pressure barely changes the width.

## Brush Artist · Refs · #15 Ultramarine brush script
Ink · 10 px · 25.3 s

![Brush Artist · Refs · #15 Ultramarine brush script](Brush-Artist-Refs-15-Ultramarine-brush-script.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 2 % → 5 % | 5.0 px | 0.53 | 2.62 | 42 |
| heavy line | 10 % → 10 % | 29.6 px | 0.66 | 1.00 | 88 |
| pressure swell | 6 % → 6 % | 20.8 px | 0.68 | 1.12 | 45 |
| fast wave | 18 % → 17 % | 20.2 px | 0.59 | 0.95 | 155 |
| slow wave | 14 % → 14 % | 16.1 px | 0.59 | 1.00 | 163 |
| spiral | 22 % → 18 % | 14.5 px | 0.54 | 0.82 | 281 |
| loop | 13 % → 14 % | 17.4 px | 0.61 | 1.02 | 114 |
| tilted | 6 % → 6 % | 15.5 px | 0.68 | 1.01 | 82 |
| over the wet one | 13 % → 13 % | 20.5 px | 0.68 | 1.04 | 69 |
| long, no reload | 33 % → 20 % | 14.8 px | 0.52 | 0.59 | 372 | quarters: 0.30 → 0.14 → 0.05 → 0.02

Numbers say: light vs heavy: width 5.0 → 29.6 px, dark 0.53 → 0.66; wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #18 Blue oil-stick scribbles
Pastel · 10 px · 10.0 s

![Brush Artist · Refs · #18 Blue oil-stick scribbles](Brush-Artist-Refs-18-Blue-oil-stick-scribbles.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 1 % → 1 % | 2.9 px | 0.52 | 1.00 | 23 |
| heavy line | 2 % → 2 % | 5.5 px | 0.53 | 1.00 | 35 |
| pressure swell | 1 % → 1 % | 5.0 px | 0.53 | 1.00 | 22 |
| fast wave | 4 % → 4 % | 4.8 px | 0.53 | 1.00 | 62 |
| slow wave | 4 % → 4 % | 4.4 px | 0.53 | 1.00 | 46 |
| spiral | 7 % → 7 % | 4.5 px | 0.52 | 1.00 | 135 |
| loop | 3 % → 3 % | 4.5 px | 0.52 | 1.00 | 79 |
| tilted | 2 % → 2 % | 4.7 px | 0.53 | 1.00 | 42 |
| over the wet one | 3 % → 3 % | 4.7 px | 0.53 | 1.00 | 31 |
| long, no reload | 10 % → 10 % | 4.4 px | 0.53 | 1.00 | 158 | quarters: 0.06 → 0.06 → 0.06 → 0.06

Numbers say: light vs heavy: width 2.9 → 5.5 px, dark 0.52 → 0.53; the long stroke does not run out of paint.

## Brush Artist · Refs · #20 Orange-red crayon scribble
Pastel · 14 px · 9.8 s

![Brush Artist · Refs · #20 Orange-red crayon scribble](Brush-Artist-Refs-20-Orange-red-crayon-scribble.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 1 % → 1 % | 4.0 px | 0.53 | 1.00 | 14 |
| heavy line | 3 % → 3 % | 8.0 px | 0.53 | 1.00 | 27 |
| pressure swell | 2 % → 2 % | 7.6 px | 0.53 | 1.00 | 14 |
| fast wave | 6 % → 6 % | 7.2 px | 0.53 | 1.00 | 89 |
| slow wave | 6 % → 6 % | 6.6 px | 0.53 | 1.00 | 94 |
| spiral | 9 % → 9 % | 6.2 px | 0.53 | 1.00 | 116 |
| loop | 5 % → 5 % | 6.2 px | 0.53 | 1.00 | 50 |
| tilted | 2 % → 2 % | 5.6 px | 0.53 | 1.00 | 37 |
| over the wet one | 4 % → 4 % | 6.6 px | 0.53 | 1.00 | 35 |
| long, no reload | 13 % → 13 % | 5.7 px | 0.53 | 1.00 | 168 | quarters: 0.07 → 0.07 → 0.08 → 0.08

Numbers say: light vs heavy: width 4.0 → 8.0 px, dark 0.53 → 0.53; the long stroke does not run out of paint.

## Brush Artist · Refs · #21 Gritty black contours
Gouache · 12 px · 20.7 s

![Brush Artist · Refs · #21 Gritty black contours](Brush-Artist-Refs-21-Gritty-black-contours.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 3 % → 0 % | 8.8 px | 0.79 | 0.12 | 59 |
| heavy line | 4 % → 0 % | 11.9 px | 0.79 | 0.10 | 86 |
| pressure swell | 3 % → 0 % | 11.6 px | 0.79 | 0.15 | 58 |
| fast wave | 7 % → 1 % | 8.5 px | 0.79 | 0.10 | 215 |
| slow wave | 8 % → 1 % | 9.0 px | 0.79 | 0.09 | 180 |
| spiral | 9 % → 1 % | 6.0 px | 0.79 | 0.10 | 369 |
| loop | 8 % → 1 % | 9.9 px | 0.79 | 0.09 | 169 |
| tilted | 4 % → 4 % | 10.8 px | 0.79 | 0.90 | 70 |
| over the wet one | 7 % → 1 % | 9.7 px | 0.79 | 0.17 | 84 |
| long, no reload | 7 % → 1 % | 3.3 px | 0.79 | 0.12 | 497 | quarters: 0.20 → 0.07 → 0.00 → 0.00

Numbers say: light vs heavy: width 8.8 → 11.9 px, dark 0.79 → 0.79.

## Brush Artist · Refs · #22 Bold black brush poster
Ink · 20 px · 27.2 s

![Brush Artist · Refs · #22 Bold black brush poster](Brush-Artist-Refs-22-Bold-black-brush-poster.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 3 % → 5 % | 9.5 px | 0.79 | 1.63 | 45 |
| heavy line | 15 % → 15 % | 44.6 px | 0.88 | 0.99 | 85 |
| pressure swell | 9 % → 9 % | 31.9 px | 0.87 | 1.04 | 42 |
| fast wave | 27 % → 26 % | 31.2 px | 0.87 | 0.98 | 121 |
| slow wave | 22 % → 21 % | 25.2 px | 0.87 | 0.98 | 253 |
| spiral | 34 % → 32 % | 22.2 px | 0.87 | 0.94 | 255 |
| loop | 20 % → 20 % | 26.2 px | 0.88 | 1.00 | 132 |
| tilted | 8 % → 8 % | 22.7 px | 0.88 | 1.01 | 71 |
| over the wet one | 19 % → 19 % | 30.5 px | 0.88 | 1.00 | 56 |
| long, no reload | 45 % → 38 % | 20.2 px | 0.86 | 0.84 | 377 | quarters: 0.54 → 0.45 → 0.35 → 0.27

Numbers say: light vs heavy: width 9.5 → 44.6 px, dark 0.79 → 0.88; wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #23 Dry white on orange + black line
Gouache · 50 px · 25.6 s

![Brush Artist · Refs · #23 Dry white on orange + black line](Brush-Artist-Refs-23-Dry-white-on-orange-black-line.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 12 % → 2 % | 35.1 px | 0.01 | 0.13 | 87 |
| heavy line | 16 % → 2 % | 46.9 px | 0.00 | 0.11 | 243 |
| pressure swell | 11 % → 2 % | 42.6 px | 0.01 | 0.19 | 111 |
| fast wave | 34 % → 3 % | 39.7 px | 0.00 | 0.09 | 404 |
| slow wave | 34 % → 3 % | 39.0 px | 0.00 | 0.10 | 642 |
| spiral | 49 % → 4 % | 32.6 px | 0.00 | 0.07 | 672 |
| loop | 30 % → 4 % | 39.1 px | 0.00 | 0.12 | 354 |
| tilted | 13 % → 12 % | 34.9 px | 0.01 | 0.98 | 179 |
| over the wet one | 26 % → 7 % | 38.0 px | 0.01 | 0.27 | 156 |
| long, no reload | 58 % → 5 % | 26.1 px | 0.01 | 0.09 | 948 | quarters: 0.01 → 0.01 → 0.00 → 0.00

Numbers say: light vs heavy: width 35.1 → 46.9 px, dark 0.01 → 0.00.

## Brush Artist · Refs · #24 Picasso flat oil
Oil · 34 px · 19.7 s

![Brush Artist · Refs · #24 Picasso flat oil](Brush-Artist-Refs-24-Picasso-flat-oil.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 11 % → 11 % | 32.2 px | 0.39 | 1.00 | 76 |
| heavy line | 12 % → 12 % | 35.0 px | 0.39 | 1.00 | 118 |
| pressure swell | 9 % → 9 % | 34.4 px | 0.41 | 1.00 | 83 |
| fast wave | 30 % → 30 % | 34.2 px | 0.41 | 1.00 | 343 |
| slow wave | 30 % → 30 % | 34.9 px | 0.41 | 1.00 | 558 |
| spiral | 51 % → 51 % | 33.7 px | 0.40 | 1.00 | 554 |
| loop | 25 % → 25 % | 32.6 px | 0.41 | 1.00 | 262 |
| tilted | 11 % → 11 % | 32.0 px | 0.41 | 1.00 | 170 |
| over the wet one | 22 % → 22 % | 30.7 px | 0.41 | 1.00 | 123 |
| long, no reload | 61 % → 61 % | 27.6 px | 0.39 | 1.00 | 775 | quarters: 0.28 → 0.28 → 0.26 → 0.24

Numbers say: light vs heavy: width 32.2 → 35.0 px, dark 0.39 → 0.39; pressure barely changes the width.

## Brush Artist · Refs · #25 Yellow heavy flat stroke
Heavy acrylic · 110 px · 35.7 s

![Brush Artist · Refs · #25 Yellow heavy flat stroke](Brush-Artist-Refs-25-Yellow-heavy-flat-stroke.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 35 % → 36 % | 101.3 px | 0.17 | 1.02 | 419 |
| heavy line | 36 % → 35 % | 105.0 px | 0.17 | 0.97 | 428 |
| pressure swell | 28 % → 29 % | 105.4 px | 0.17 | 1.04 | 312 |
| fast wave | 72 % → 76 % | 83.8 px | 0.17 | 1.05 | 1050 |
| slow wave | 73 % → 72 % | 84.7 px | 0.18 | 0.98 | 1805 |
| spiral | 86 % → 83 % | 56.7 px | 0.17 | 0.97 | 1824 |
| loop | 65 % → 64 % | 83.6 px | 0.17 | 0.99 | 1073 |
| tilted | 26 % → 26 % | 71.5 px | 0.17 | 1.00 | 505 |
| over the wet one | 55 % → 54 % | 83.1 px | 0.17 | 0.97 | 474 |
| long, no reload | 98 % → 97 % | 44.1 px | 0.17 | 0.99 | 2627 | quarters: 0.18 → 0.17 → 0.17 → 0.16

Numbers say: light vs heavy: width 101.3 → 105.0 px, dark 0.17 → 0.17; pressure barely changes the width; the long stroke does not run out of paint.

## Brush Artist · Refs · #27 Orange impasto swatch
Heavy acrylic · 60 px · 25.9 s

![Brush Artist · Refs · #27 Orange impasto swatch](Brush-Artist-Refs-27-Orange-impasto-swatch.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 20 % → 19 % | 56.7 px | 0.35 | 0.97 | 195 |
| heavy line | 20 % → 20 % | 59.3 px | 0.35 | 0.97 | 169 |
| pressure swell | 16 % → 15 % | 59.6 px | 0.36 | 0.97 | 122 |
| fast wave | 48 % → 46 % | 55.0 px | 0.35 | 0.98 | 506 |
| slow wave | 48 % → 47 % | 55.8 px | 0.36 | 0.98 | 840 |
| spiral | 69 % → 62 % | 45.5 px | 0.35 | 0.91 | 783 |
| loop | 42 % → 40 % | 53.8 px | 0.35 | 0.97 | 428 |
| tilted | 16 % → 16 % | 44.0 px | 0.36 | 1.00 | 198 |
| over the wet one | 34 % → 33 % | 50.6 px | 0.36 | 0.97 | 192 |
| long, no reload | 85 % → 75 % | 38.1 px | 0.35 | 0.88 | 1408 | quarters: 0.33 → 0.31 → 0.29 → 0.26

Numbers say: light vs heavy: width 56.7 → 59.3 px, dark 0.35 → 0.35; pressure barely changes the width.

## Brush Artist · Refs · #28 Miles Davis black lines
Ink · 22 px · 27.7 s

![Brush Artist · Refs · #28 Miles Davis black lines](Brush-Artist-Refs-28-Miles-Davis-black-lines.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 4 % → 6 % | 12.2 px | 0.81 | 1.48 | 45 |
| heavy line | 17 % → 17 % | 49.1 px | 0.88 | 0.99 | 86 |
| pressure swell | 10 % → 10 % | 35.9 px | 0.87 | 1.03 | 42 |
| fast wave | 30 % → 30 % | 35.0 px | 0.87 | 0.98 | 135 |
| slow wave | 25 % → 25 % | 28.5 px | 0.87 | 0.99 | 239 |
| spiral | 38 % → 37 % | 25.3 px | 0.87 | 0.96 | 268 |
| loop | 23 % → 23 % | 29.4 px | 0.88 | 1.00 | 142 |
| tilted | 9 % → 9 % | 25.0 px | 0.88 | 1.01 | 84 |
| over the wet one | 21 % → 21 % | 34.1 px | 0.88 | 1.00 | 72 |
| long, no reload | 51 % → 43 % | 22.7 px | 0.86 | 0.85 | 404 | quarters: 0.59 → 0.51 → 0.40 → 0.31

Numbers say: light vs heavy: width 12.2 → 49.1 px, dark 0.81 → 0.88.

## Brush Artist · Refs · #29 Shrigley magenta asterisk
Watercolor · 70 px · 31.7 s

![Brush Artist · Refs · #29 Shrigley magenta asterisk](Brush-Artist-Refs-29-Shrigley-magenta-asterisk.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 10 % → 13 % | 28.0 px | 0.41 | 1.36 | 57 |
| heavy line | 17 % → 18 % | 50.2 px | 0.41 | 1.03 | 135 |
| pressure swell | 11 % → 12 % | 41.0 px | 0.43 | 1.13 | 80 |
| fast wave | 38 % → 38 % | 43.7 px | 0.38 | 1.00 | 265 |
| slow wave | 35 % → 39 % | 41.0 px | 0.43 | 1.10 | 482 |
| spiral | 61 % → 61 % | 40.0 px | 0.37 | 1.01 | 513 |
| loop | 31 % → 32 % | 40.2 px | 0.42 | 1.03 | 279 |
| tilted | 18 % → 18 % | 48.9 px | 0.43 | 1.00 | 235 |
| over the wet one | 31 % → 34 % | 38.4 px | 0.43 | 1.07 | 116 |
| long, no reload | 75 % → 75 % | 33.5 px | 0.36 | 1.00 | 733 | quarters: 0.39 → 0.33 → 0.27 → 0.21

Numbers say: light vs heavy: width 28.0 → 50.2 px, dark 0.41 → 0.41.

## Brush Artist · Refs · #30 Red gouache face patch
Gouache · 60 px · 38.2 s

![Brush Artist · Refs · #30 Red gouache face patch](Brush-Artist-Refs-30-Red-gouache-face-patch.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 16 % → 15 % | 46.9 px | 0.49 | 0.91 | 146 |
| heavy line | 25 % → 20 % | 73.8 px | 0.49 | 0.80 | 254 |
| pressure swell | 19 % → 17 % | 72.6 px | 0.49 | 0.86 | 183 |
| fast wave | 48 % → 28 % | 55.1 px | 0.49 | 0.58 | 391 |
| slow wave | 48 % → 28 % | 55.3 px | 0.49 | 0.59 | 752 |
| spiral | 59 % → 28 % | 39.1 px | 0.49 | 0.48 | 747 |
| loop | 40 % → 29 % | 51.3 px | 0.49 | 0.74 | 380 |
| tilted | 16 % → 16 % | 45.7 px | 0.49 | 1.01 | 231 |
| over the wet one | 36 % → 32 % | 55.3 px | 0.49 | 0.88 | 146 |
| long, no reload | 67 % → 30 % | 30.0 px | 0.49 | 0.45 | 1119 | quarters: 0.43 → 0.38 → 0.32 → 0.26

Numbers say: light vs heavy: width 46.9 → 73.8 px, dark 0.49 → 0.49.

## Brush Artist · Refs · #31 Warhol blotted line
Ink · 6 px · 21.4 s

![Brush Artist · Refs · #31 Warhol blotted line](Brush-Artist-Refs-31-Warhol-blotted-line.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 1 % → 3 % | 2.6 px | 0.75 | 3.30 | 31 |
| heavy line | 7 % → 7 % | 20.6 px | 0.83 | 0.97 | 75 |
| pressure swell | 4 % → 4 % | 14.8 px | 0.84 | 1.12 | 47 |
| fast wave | 12 % → 9 % | 13.8 px | 0.82 | 0.77 | 93 |
| slow wave | 10 % → 8 % | 11.2 px | 0.80 | 0.85 | 95 |
| spiral | 15 % → 9 % | 9.7 px | 0.80 | 0.58 | 196 |
| loop | 9 % → 9 % | 11.9 px | 0.80 | 0.94 | 90 |
| tilted | 3 % → 3 % | 8.6 px | 0.84 | 1.04 | 39 |
| over the wet one | 8 % → 8 % | 14.5 px | 0.84 | 1.02 | 42 |
| long, no reload | 21 % → 9 % | 9.6 px | 0.78 | 0.43 | 256 | quarters: 0.25 → 0.13 → 0.05 → 0.01

Numbers say: light vs heavy: width 2.6 → 20.6 px, dark 0.75 → 0.83; wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #32 Thick orange swipes
Heavy acrylic · 90 px · 31.8 s

![Brush Artist · Refs · #32 Thick orange swipes](Brush-Artist-Refs-32-Thick-orange-swipes.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 29 % → 29 % | 82.9 px | 0.38 | 1.00 | 331 |
| heavy line | 30 % → 29 % | 86.3 px | 0.38 | 0.97 | 331 |
| pressure swell | 23 % → 23 % | 86.5 px | 0.38 | 1.01 | 222 |
| fast wave | 63 % → 65 % | 73.1 px | 0.38 | 1.03 | 855 |
| slow wave | 64 % → 63 % | 73.5 px | 0.39 | 0.98 | 1370 |
| spiral | 79 % → 77 % | 52.2 px | 0.38 | 0.98 | 1324 |
| loop | 57 % → 56 % | 73.4 px | 0.38 | 0.99 | 715 |
| tilted | 21 % → 21 % | 59.3 px | 0.38 | 1.00 | 406 |
| over the wet one | 47 % → 45 % | 70.7 px | 0.38 | 0.97 | 344 |
| long, no reload | 95 % → 93 % | 42.7 px | 0.38 | 0.98 | 2059 | quarters: 0.38 → 0.38 → 0.37 → 0.35

Numbers say: light vs heavy: width 82.9 → 86.3 px, dark 0.38 → 0.38; pressure barely changes the width; the long stroke does not run out of paint.

## Brush Artist · Refs · #33 Red wet-in-wet band
Watercolor · 80 px · 39.2 s

![Brush Artist · Refs · #33 Red wet-in-wet band](Brush-Artist-Refs-33-Red-wet-in-wet-band.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 21 % → 21 % | 60.7 px | 0.34 | 1.01 | 178 |
| heavy line | 30 % → 30 % | 88.4 px | 0.33 | 0.98 | 264 |
| pressure swell | 20 % → 21 % | 75.9 px | 0.36 | 1.03 | 142 |
| fast wave | 61 % → 64 % | 71.0 px | 0.30 | 1.04 | 455 |
| slow wave | 60 % → 60 % | 68.9 px | 0.41 | 1.00 | 819 |
| spiral | 75 % → 75 % | 49.7 px | 0.38 | 1.00 | 759 |
| loop | 52 % → 52 % | 67.5 px | 0.36 | 1.00 | 371 |
| tilted | 24 % → 24 % | 67.8 px | 0.37 | 1.00 | 312 |
| over the wet one | 48 % → 50 % | 66.6 px | 0.37 | 1.04 | 161 |
| long, no reload | 95 % → 96 % | 42.8 px | 0.37 | 1.00 | 1193 | quarters: 0.45 → 0.42 → 0.37 → 0.28

Numbers say: light vs heavy: width 60.7 → 88.4 px, dark 0.34 → 0.33.

## Brush Artist · Refs · #34 Magenta oil patches
Oil · 60 px · 24.7 s

![Brush Artist · Refs · #34 Magenta oil patches](Brush-Artist-Refs-34-Magenta-oil-patches.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 19 % → 19 % | 55.6 px | 0.59 | 1.00 | 217 |
| heavy line | 21 % → 21 % | 59.7 px | 0.59 | 1.00 | 241 |
| pressure swell | 16 % → 16 % | 58.8 px | 0.62 | 1.01 | 159 |
| fast wave | 48 % → 49 % | 55.4 px | 0.62 | 1.02 | 616 |
| slow wave | 48 % → 48 % | 55.8 px | 0.62 | 1.00 | 974 |
| spiral | 70 % → 70 % | 46.3 px | 0.62 | 1.00 | 980 |
| loop | 42 % → 42 % | 54.2 px | 0.62 | 1.00 | 483 |
| tilted | 17 % → 17 % | 46.8 px | 0.62 | 1.00 | 269 |
| over the wet one | 35 % → 35 % | 50.0 px | 0.62 | 1.00 | 221 |
| long, no reload | 86 % → 86 % | 38.7 px | 0.62 | 1.00 | 1384 | quarters: 0.59 → 0.58 → 0.57 → 0.52

Numbers say: light vs heavy: width 55.6 → 59.7 px, dark 0.59 → 0.59; pressure barely changes the width; the long stroke does not run out of paint.

## Brush Artist · Refs · #35 Red band with runs
Watercolor · 70 px · 38.4 s

![Brush Artist · Refs · #35 Red band with runs](Brush-Artist-Refs-35-Red-band-with-runs.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 18 % → 19 % | 53.2 px | 0.26 | 1.05 | 130 |
| heavy line | 27 % → 27 % | 78.7 px | 0.25 | 0.99 | 188 |
| pressure swell | 18 % → 18 % | 67.0 px | 0.28 | 1.02 | 120 |
| fast wave | 56 % → 56 % | 64.8 px | 0.24 | 1.00 | 372 |
| slow wave | 54 % → 55 % | 62.6 px | 0.33 | 1.01 | 677 |
| spiral | 72 % → 72 % | 47.6 px | 0.30 | 0.99 | 626 |
| loop | 48 % → 48 % | 61.7 px | 0.28 | 1.01 | 386 |
| tilted | 22 % → 22 % | 60.5 px | 0.30 | 1.00 | 257 |
| over the wet one | 43 % → 45 % | 59.7 px | 0.30 | 1.05 | 137 |
| long, no reload | 93 % → 92 % | 41.6 px | 0.29 | 0.99 | 966 | quarters: 0.34 → 0.32 → 0.27 → 0.21

Numbers say: light vs heavy: width 53.2 → 78.7 px, dark 0.26 → 0.25.

## Brush Artist · Refs · #36 Magenta letters flat brush
Gouache · 36 px · 35.0 s

![Brush Artist · Refs · #36 Magenta letters flat brush](Brush-Artist-Refs-36-Magenta-letters-flat-brush.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 10 % → 10 % | 29.0 px | 0.45 | 0.98 | 80 |
| heavy line | 17 % → 14 % | 49.1 px | 0.45 | 0.85 | 109 |
| pressure swell | 13 % → 12 % | 49.4 px | 0.45 | 0.89 | 67 |
| fast wave | 35 % → 19 % | 40.3 px | 0.45 | 0.54 | 248 |
| slow wave | 35 % → 19 % | 39.9 px | 0.45 | 0.54 | 439 |
| spiral | 46 % → 19 % | 30.4 px | 0.45 | 0.42 | 403 |
| loop | 27 % → 20 % | 35.3 px | 0.45 | 0.72 | 219 |
| tilted | 11 % → 11 % | 29.8 px | 0.45 | 1.00 | 115 |
| over the wet one | 24 % → 22 % | 38.1 px | 0.45 | 0.92 | 107 |
| long, no reload | 46 % → 19 % | 20.8 px | 0.45 | 0.40 | 586 | quarters: 0.29 → 0.25 → 0.22 → 0.18

Numbers say: light vs heavy: width 29.0 → 49.1 px, dark 0.45 → 0.45.

## Brush Artist · Refs · #37 Oil still life dabs
Oil · 40 px · 21.3 s

![Brush Artist · Refs · #37 Oil still life dabs](Brush-Artist-Refs-37-Oil-still-life-dabs.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 13 % → 13 % | 37.9 px | 0.39 | 1.00 | 139 |
| heavy line | 14 % → 14 % | 41.1 px | 0.38 | 1.00 | 124 |
| pressure swell | 11 % → 11 % | 40.2 px | 0.40 | 1.00 | 106 |
| fast wave | 34 % → 34 % | 39.8 px | 0.40 | 1.00 | 394 |
| slow wave | 35 % → 35 % | 40.2 px | 0.39 | 1.00 | 597 |
| spiral | 59 % → 59 % | 38.7 px | 0.38 | 1.00 | 619 |
| loop | 29 % → 29 % | 37.8 px | 0.39 | 1.00 | 321 |
| tilted | 13 % → 13 % | 35.8 px | 0.39 | 1.00 | 201 |
| over the wet one | 26 % → 26 % | 35.6 px | 0.39 | 1.00 | 139 |
| long, no reload | 69 % → 69 % | 30.9 px | 0.37 | 1.00 | 892 | quarters: 0.31 → 0.30 → 0.28 → 0.24

Numbers say: light vs heavy: width 37.9 → 41.1 px, dark 0.39 → 0.38; pressure barely changes the width.

## Brush Artist · Refs · #38 Sanguine drawing
Pastel · 6 px · 10.2 s

![Brush Artist · Refs · #38 Sanguine drawing](Brush-Artist-Refs-38-Sanguine-drawing.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 1 % → 1 % | 2.0 px | 0.61 | 1.00 | 18 |
| heavy line | 1 % → 1 % | 3.5 px | 0.62 | 1.00 | 10 |
| pressure swell | 1 % → 1 % | 3.3 px | 0.62 | 1.00 | 15 |
| fast wave | 3 % → 3 % | 3.2 px | 0.61 | 1.00 | 38 |
| slow wave | 3 % → 3 % | 3.0 px | 0.61 | 1.00 | 44 |
| spiral | 4 % → 4 % | 2.9 px | 0.61 | 1.00 | 67 |
| loop | 2 % → 2 % | 3.0 px | 0.61 | 1.00 | 39 |
| tilted | 1 % → 1 % | 3.4 px | 0.62 | 1.00 | 14 |
| over the wet one | 2 % → 2 % | 2.9 px | 0.62 | 1.00 | 16 |
| long, no reload | 7 % → 7 % | 3.0 px | 0.61 | 1.00 | 107 | quarters: 0.04 → 0.05 → 0.05 → 0.05

Numbers say: light vs heavy: width 2.0 → 3.5 px, dark 0.61 → 0.62; the long stroke does not run out of paint.

## Brush Artist · Refs · #39 Very thick impasto
Heavy acrylic · 60 px · 23.4 s

![Brush Artist · Refs · #39 Very thick impasto](Brush-Artist-Refs-39-Very-thick-impasto.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 20 % → 19 % | 56.8 px | 0.61 | 0.97 | 223 |
| heavy line | 20 % → 20 % | 59.4 px | 0.61 | 0.97 | 200 |
| pressure swell | 16 % → 15 % | 59.6 px | 0.62 | 0.97 | 156 |
| fast wave | 48 % → 47 % | 55.2 px | 0.62 | 0.98 | 476 |
| slow wave | 48 % → 47 % | 56.0 px | 0.62 | 0.98 | 1077 |
| spiral | 69 % → 65 % | 45.6 px | 0.62 | 0.93 | 916 |
| loop | 42 % → 41 % | 54.0 px | 0.62 | 0.97 | 592 |
| tilted | 16 % → 16 % | 44.0 px | 0.62 | 1.00 | 231 |
| over the wet one | 34 % → 33 % | 50.7 px | 0.62 | 0.97 | 231 |
| long, no reload | 85 % → 79 % | 38.3 px | 0.62 | 0.93 | 1293 | quarters: 0.58 → 0.57 → 0.55 → 0.52

Numbers say: light vs heavy: width 56.8 → 59.4 px, dark 0.61 → 0.61; pressure barely changes the width; the long stroke does not run out of paint.

## Brush Artist · Refs · #40 Watercolour blooms
Watercolor · 90 px · 42.5 s

![Brush Artist · Refs · #40 Watercolour blooms](Brush-Artist-Refs-40-Watercolour-blooms.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 23 % → 24 % | 68.2 px | 0.24 | 1.02 | 161 |
| heavy line | 34 % → 33 % | 98.4 px | 0.24 | 0.98 | 289 |
| pressure swell | 23 % → 24 % | 85.3 px | 0.26 | 1.04 | 198 |
| fast wave | 66 % → 69 % | 76.7 px | 0.23 | 1.04 | 887 |
| slow wave | 65 % → 65 % | 74.7 px | 0.31 | 1.00 | 933 |
| spiral | 79 % → 79 % | 52.0 px | 0.29 | 1.00 | 1184 |
| loop | 57 % → 57 % | 73.7 px | 0.27 | 1.00 | 502 |
| tilted | 26 % → 26 % | 73.8 px | 0.27 | 1.00 | 374 |
| over the wet one | 53 % → 55 % | 73.9 px | 0.27 | 1.05 | 248 |
| long, no reload | 97 % → 97 % | 43.5 px | 0.29 | 1.00 | 1483 | quarters: 0.35 → 0.33 → 0.29 → 0.22

Numbers say: light vs heavy: width 68.2 → 98.4 px, dark 0.24 → 0.24.

## Brush Artist · Refs · #41 Coloured pencil hatching
Pastel · 4 px · 9.9 s

![Brush Artist · Refs · #41 Coloured pencil hatching](Brush-Artist-Refs-41-Coloured-pencil-hatching.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 1 % → 1 % | 1.6 px | 0.42 | 1.00 | 16 |
| heavy line | 1 % → 1 % | 2.6 px | 0.43 | 1.00 | 19 |
| pressure swell | 1 % → 1 % | 2.1 px | 0.43 | 1.00 | 14 |
| fast wave | 2 % → 2 % | 2.2 px | 0.42 | 1.00 | 42 |
| slow wave | 2 % → 2 % | 2.1 px | 0.43 | 1.00 | 50 |
| spiral | 3 % → 3 % | 2.1 px | 0.43 | 1.00 | 71 |
| loop | 2 % → 2 % | 2.2 px | 0.43 | 1.00 | 22 |
| tilted | 1 % → 1 % | 3.0 px | 0.42 | 1.00 | 9 |
| over the wet one | 2 % → 2 % | 2.2 px | 0.42 | 1.00 | 15 |
| long, no reload | 5 % → 5 % | 2.3 px | 0.43 | 1.00 | 99 | quarters: 0.02 → 0.02 → 0.02 → 0.03

Numbers say: light vs heavy: width 1.6 → 2.6 px, dark 0.42 → 0.43; the long stroke does not run out of paint.

## Brush Artist · Refs · #42 Oil pastel shaggy
Pastel · 18 px · 10.2 s

![Brush Artist · Refs · #42 Oil pastel shaggy](Brush-Artist-Refs-42-Oil-pastel-shaggy.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 2 % → 2 % | 5.1 px | 0.07 | 1.00 | 32 |
| heavy line | 4 % → 4 % | 10.7 px | 0.08 | 1.00 | 32 |
| pressure swell | 3 % → 3 % | 9.5 px | 0.08 | 1.00 | 17 |
| fast wave | 8 % → 8 % | 9.0 px | 0.08 | 1.00 | 60 |
| slow wave | 7 % → 7 % | 8.2 px | 0.08 | 1.00 | 120 |
| spiral | 12 % → 12 % | 7.7 px | 0.08 | 1.00 | 130 |
| loop | 6 % → 6 % | 7.9 px | 0.08 | 1.00 | 52 |
| tilted | 2 % → 2 % | 6.9 px | 0.08 | 1.00 | 35 |
| over the wet one | 6 % → 6 % | 8.5 px | 0.08 | 1.00 | 30 |
| long, no reload | 15 % → 15 % | 6.9 px | 0.08 | 1.00 | 206 | quarters: 0.01 → 0.01 → 0.01 → 0.01

Numbers say: light vs heavy: width 5.1 → 10.7 px, dark 0.07 → 0.08; the long stroke does not run out of paint.

## Brush Artist · Refs · #43 Dragged black ink blocks
Gouache · 70 px · 31.6 s

![Brush Artist · Refs · #43 Dragged black ink blocks](Brush-Artist-Refs-43-Dragged-black-ink-blocks.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 19 % → 5 % | 54.9 px | 0.57 | 0.28 | 125 |
| heavy line | 24 % → 9 % | 69.0 px | 0.57 | 0.38 | 378 |
| pressure swell | 17 % → 9 % | 63.4 px | 0.57 | 0.53 | 183 |
| fast wave | 51 % → 11 % | 58.7 px | 0.57 | 0.21 | 686 |
| slow wave | 50 % → 10 % | 58.1 px | 0.57 | 0.20 | 1060 |
| spiral | 65 % → 14 % | 42.6 px | 0.57 | 0.22 | 1075 |
| loop | 45 % → 12 % | 58.1 px | 0.57 | 0.27 | 474 |
| tilted | 17 % → 16 % | 46.4 px | 0.57 | 0.98 | 265 |
| over the wet one | 37 % → 20 % | 55.6 px | 0.57 | 0.56 | 229 |
| long, no reload | 82 % → 17 % | 36.6 px | 0.57 | 0.21 | 1574 | quarters: 0.54 → 0.52 → 0.47 → 0.40

Numbers say: light vs heavy: width 54.9 → 69.0 px, dark 0.57 → 0.57.

## Brush Artist · Refs · #44 Blue looping ribbon
Oil · 80 px · 27.4 s

![Brush Artist · Refs · #44 Blue looping ribbon](Brush-Artist-Refs-44-Blue-looping-ribbon.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 26 % → 27 % | 74.8 px | 0.71 | 1.04 | 334 |
| heavy line | 27 % → 27 % | 79.6 px | 0.71 | 1.00 | 359 |
| pressure swell | 21 % → 21 % | 78.1 px | 0.72 | 1.03 | 289 |
| fast wave | 61 % → 64 % | 70.3 px | 0.73 | 1.05 | 772 |
| slow wave | 61 % → 61 % | 70.0 px | 0.73 | 1.00 | 1394 |
| spiral | 78 % → 78 % | 51.3 px | 0.73 | 1.00 | 1444 |
| loop | 54 % → 54 % | 69.7 px | 0.72 | 1.00 | 676 |
| tilted | 20 % → 20 % | 57.2 px | 0.71 | 1.00 | 393 |
| over the wet one | 44 % → 44 % | 64.9 px | 0.71 | 1.00 | 343 |
| long, no reload | 96 % → 96 % | 42.8 px | 0.73 | 1.00 | 1957 | quarters: 0.72 → 0.72 → 0.72 → 0.69

Numbers say: light vs heavy: width 74.8 → 79.6 px, dark 0.71 → 0.71; pressure barely changes the width; the long stroke does not run out of paint.

## Brush Artist · Refs · #45 Soft pastel pepper
Pastel · 40 px · 10.7 s

![Brush Artist · Refs · #45 Soft pastel pepper](Brush-Artist-Refs-45-Soft-pastel-pepper.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 4 % → 4 % | 11.3 px | 0.53 | 1.00 | 33 |
| heavy line | 8 % → 8 % | 23.0 px | 0.53 | 1.00 | 47 |
| pressure swell | 5 % → 5 % | 19.5 px | 0.53 | 1.00 | 29 |
| fast wave | 17 % → 17 % | 19.4 px | 0.53 | 1.00 | 157 |
| slow wave | 15 % → 15 % | 17.1 px | 0.53 | 1.00 | 247 |
| spiral | 25 % → 25 % | 16.3 px | 0.53 | 1.00 | 223 |
| loop | 12 % → 12 % | 16.1 px | 0.53 | 1.00 | 146 |
| tilted | 5 % → 5 % | 12.8 px | 0.53 | 1.00 | 65 |
| over the wet one | 11 % → 11 % | 17.7 px | 0.53 | 1.00 | 56 |
| long, no reload | 30 % → 30 % | 13.6 px | 0.53 | 1.00 | 370 | quarters: 0.18 → 0.18 → 0.18 → 0.18

Numbers say: light vs heavy: width 11.3 → 23.0 px, dark 0.53 → 0.53; the long stroke does not run out of paint.

## Brush Artist · Refs · #46 Red-brown ink lips
Watercolor · 70 px · 37.5 s

![Brush Artist · Refs · #46 Red-brown ink lips](Brush-Artist-Refs-46-Red-brown-ink-lips.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 18 % → 18 % | 53.2 px | 0.51 | 1.00 | 122 |
| heavy line | 27 % → 27 % | 78.7 px | 0.49 | 0.98 | 199 |
| pressure swell | 18 % → 18 % | 67.0 px | 0.53 | 1.01 | 116 |
| fast wave | 56 % → 58 % | 64.8 px | 0.46 | 1.03 | 404 |
| slow wave | 54 % → 54 % | 62.6 px | 0.58 | 1.00 | 613 |
| spiral | 72 % → 72 % | 47.6 px | 0.54 | 1.00 | 617 |
| loop | 48 % → 48 % | 61.7 px | 0.53 | 1.00 | 297 |
| tilted | 22 % → 22 % | 60.5 px | 0.54 | 1.00 | 247 |
| over the wet one | 43 % → 44 % | 59.9 px | 0.54 | 1.03 | 146 |
| long, no reload | 93 % → 93 % | 41.6 px | 0.52 | 1.00 | 927 | quarters: 0.59 → 0.57 → 0.51 → 0.40

Numbers say: light vs heavy: width 53.2 → 78.7 px, dark 0.51 → 0.49.

## Brush Artist · Refs · #47 Pink knife slabs
Heavy acrylic · 90 px · 29.7 s

![Brush Artist · Refs · #47 Pink knife slabs](Brush-Artist-Refs-47-Pink-knife-slabs.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 28 % → 27 % | 81.0 px | 0.17 | 0.97 | 220 |
| heavy line | 29 % → 28 % | 83.4 px | 0.17 | 0.97 | 235 |
| pressure swell | 22 % → 22 % | 83.4 px | 0.18 | 1.01 | 155 |
| fast wave | 61 % → 60 % | 70.1 px | 0.17 | 0.98 | 581 |
| slow wave | 61 % → 59 % | 70.9 px | 0.17 | 0.96 | 1132 |
| spiral | 76 % → 58 % | 50.0 px | 0.16 | 0.76 | 990 |
| loop | 55 % → 54 % | 71.7 px | 0.17 | 0.97 | 530 |
| tilted | 21 % → 21 % | 59.3 px | 0.17 | 1.00 | 311 |
| over the wet one | 46 % → 44 % | 67.9 px | 0.17 | 0.96 | 254 |
| long, no reload | 92 % → 76 % | 41.3 px | 0.16 | 0.83 | 1446 | quarters: 0.18 → 0.16 → 0.14 → 0.09

Numbers say: light vs heavy: width 81.0 → 83.4 px, dark 0.17 → 0.17; pressure barely changes the width.

## Brush Artist · Refs · #48 Black bands with drips
Gouache · 70 px · 41.6 s

![Brush Artist · Refs · #48 Black bands with drips](Brush-Artist-Refs-48-Black-bands-with-drips.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 19 % → 18 % | 54.6 px | 0.69 | 0.93 | 175 |
| heavy line | 29 % → 24 % | 83.0 px | 0.69 | 0.84 | 294 |
| pressure swell | 23 % → 21 % | 86.1 px | 0.69 | 0.92 | 223 |
| fast wave | 53 % → 36 % | 61.8 px | 0.69 | 0.68 | 493 |
| slow wave | 53 % → 36 % | 61.7 px | 0.69 | 0.67 | 910 |
| spiral | 64 % → 35 % | 41.9 px | 0.69 | 0.55 | 873 |
| loop | 45 % → 36 % | 57.8 px | 0.69 | 0.81 | 444 |
| tilted | 19 % → 19 % | 52.3 px | 0.69 | 1.00 | 266 |
| over the wet one | 41 % → 38 % | 62.4 px | 0.69 | 0.92 | 234 |
| long, no reload | 74 % → 37 % | 33.3 px | 0.69 | 0.50 | 1246 | quarters: 0.64 → 0.61 → 0.54 → 0.45

Numbers say: light vs heavy: width 54.6 → 83.0 px, dark 0.69 → 0.69.

## Brush Artist · Refs · #49 Magenta letters round brush
Ink · 30 px · 30.9 s

![Brush Artist · Refs · #49 Magenta letters round brush](Brush-Artist-Refs-49-Magenta-letters-round-brush.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 6 % → 8 % | 17.5 px | 0.50 | 1.28 | 34 |
| heavy line | 21 % → 21 % | 62.0 px | 0.51 | 0.99 | 123 |
| pressure swell | 12 % → 13 % | 46.3 px | 0.52 | 1.01 | 67 |
| fast wave | 38 % → 38 % | 44.3 px | 0.51 | 0.99 | 254 |
| slow wave | 32 % → 31 % | 36.4 px | 0.51 | 0.99 | 340 |
| spiral | 50 % → 48 % | 32.8 px | 0.51 | 0.97 | 317 |
| loop | 29 % → 29 % | 37.6 px | 0.51 | 1.00 | 156 |
| tilted | 11 % → 11 % | 30.7 px | 0.52 | 1.01 | 84 |
| over the wet one | 26 % → 26 % | 42.1 px | 0.52 | 1.01 | 90 |
| long, no reload | 61 % → 56 % | 27.5 px | 0.51 | 0.92 | 449 | quarters: 0.41 → 0.36 → 0.30 → 0.25

Numbers say: light vs heavy: width 17.5 → 62.0 px, dark 0.50 → 0.51.

## Brush Artist · Refs · #50 Thick swipes on photo
Heavy acrylic · 40 px · 18.3 s

![Brush Artist · Refs · #50 Thick swipes on photo](Brush-Artist-Refs-50-Thick-swipes-on-photo.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 13 % → 13 % | 38.0 px | 0.21 | 0.96 | 121 |
| heavy line | 14 % → 13 % | 40.1 px | 0.21 | 0.96 | 104 |
| pressure swell | 11 % → 10 % | 40.1 px | 0.22 | 0.95 | 95 |
| fast wave | 33 % → 31 % | 38.3 px | 0.21 | 0.93 | 276 |
| slow wave | 34 % → 32 % | 39.1 px | 0.20 | 0.95 | 491 |
| spiral | 58 % → 47 % | 38.5 px | 0.20 | 0.80 | 507 |
| loop | 28 % → 27 % | 36.8 px | 0.20 | 0.95 | 281 |
| tilted | 12 % → 12 % | 34.0 px | 0.22 | 1.00 | 140 |
| over the wet one | 25 % → 24 % | 35.2 px | 0.22 | 0.95 | 134 |
| long, no reload | 66 % → 46 % | 29.5 px | 0.20 | 0.70 | 730 | quarters: 0.16 → 0.13 → 0.11 → 0.07

Numbers say: light vs heavy: width 38.0 → 40.1 px, dark 0.21 → 0.21; pressure barely changes the width.

## Brush Artist · Refs · Ground #22403f
Gouache · 130 px · 63.9 s

![Brush Artist · Refs · Ground #22403f](Brush-Artist-Refs-Ground-22403f.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 42 % → 40 % | 122.8 px | 0.52 | 0.94 | 506 |
| heavy line | 47 % → 42 % | 136.0 px | 0.52 | 0.90 | 569 |
| pressure swell | 43 % → 42 % | 162.8 px | 0.52 | 0.97 | 459 |
| fast wave | 83 % → 82 % | 95.8 px | 0.52 | 0.98 | 1440 |
| slow wave | 83 % → 76 % | 96.3 px | 0.52 | 0.91 | 2591 |
| spiral | 88 % → 84 % | 57.7 px | 0.52 | 0.96 | 2511 |
| loop | 66 % → 64 % | 85.6 px | 0.52 | 0.96 | 1705 |
| tilted | 37 % → 36 % | 102.0 px | 0.52 | 1.00 | 926 |
| over the wet one | 72 % → 69 % | 99.4 px | 0.52 | 0.96 | 660 |
| long, no reload | 98 % → 93 % | 44.0 px | 0.52 | 0.94 | 4106 | quarters: 0.52 → 0.52 → 0.52 → 0.50

Numbers say: light vs heavy: width 122.8 → 136.0 px, dark 0.52 → 0.52; pressure barely changes the width; the long stroke does not run out of paint.

## Brush Artist · Refs · Ground #2b2f1c
Gouache · 130 px · 63.2 s

![Brush Artist · Refs · Ground #2b2f1c](Brush-Artist-Refs-Ground-2b2f1c.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 42 % → 40 % | 122.8 px | 0.56 | 0.94 | 509 |
| heavy line | 47 % → 42 % | 136.0 px | 0.56 | 0.90 | 559 |
| pressure swell | 43 % → 42 % | 162.8 px | 0.56 | 0.97 | 411 |
| fast wave | 83 % → 82 % | 95.8 px | 0.56 | 0.98 | 1383 |
| slow wave | 83 % → 76 % | 96.3 px | 0.56 | 0.91 | 2507 |
| spiral | 88 % → 84 % | 57.7 px | 0.56 | 0.96 | 2304 |
| loop | 66 % → 64 % | 85.6 px | 0.56 | 0.96 | 1595 |
| tilted | 37 % → 36 % | 102.0 px | 0.56 | 1.00 | 997 |
| over the wet one | 72 % → 69 % | 99.4 px | 0.56 | 0.96 | 599 |
| long, no reload | 98 % → 93 % | 44.0 px | 0.56 | 0.94 | 4022 | quarters: 0.56 → 0.56 → 0.56 → 0.55

Numbers say: light vs heavy: width 122.8 → 136.0 px, dark 0.56 → 0.56; pressure barely changes the width; the long stroke does not run out of paint.

## Brush Artist · Refs · Ground #8a6a20
Gouache · 130 px · 63.2 s

![Brush Artist · Refs · Ground #8a6a20](Brush-Artist-Refs-Ground-8a6a20.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 42 % → 40 % | 122.8 px | 0.34 | 0.94 | 531 |
| heavy line | 47 % → 42 % | 136.0 px | 0.34 | 0.90 | 689 |
| pressure swell | 43 % → 42 % | 162.8 px | 0.34 | 0.97 | 502 |
| fast wave | 83 % → 82 % | 95.8 px | 0.34 | 0.98 | 1766 |
| slow wave | 83 % → 76 % | 96.3 px | 0.34 | 0.91 | 3200 |
| spiral | 88 % → 84 % | 57.7 px | 0.34 | 0.96 | 2635 |
| loop | 66 % → 64 % | 85.6 px | 0.34 | 0.96 | 1359 |
| tilted | 37 % → 36 % | 102.0 px | 0.34 | 1.00 | 711 |
| over the wet one | 72 % → 69 % | 99.4 px | 0.34 | 0.96 | 598 |
| long, no reload | 98 % → 93 % | 44.0 px | 0.34 | 0.94 | 3233 | quarters: 0.34 → 0.34 → 0.34 → 0.33

Numbers say: light vs heavy: width 122.8 → 136.0 px, dark 0.34 → 0.34; pressure barely changes the width; the long stroke does not run out of paint.

## Brush Artist · Refs · Ground #3b6a50
Gouache · 130 px · 61.6 s

![Brush Artist · Refs · Ground #3b6a50](Brush-Artist-Refs-Ground-3b6a50.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 42 % → 40 % | 122.8 px | 0.39 | 0.94 | 544 |
| heavy line | 47 % → 42 % | 136.0 px | 0.39 | 0.90 | 604 |
| pressure swell | 43 % → 42 % | 162.8 px | 0.39 | 0.97 | 479 |
| fast wave | 83 % → 82 % | 95.8 px | 0.39 | 0.98 | 1684 |
| slow wave | 83 % → 76 % | 96.3 px | 0.39 | 0.91 | 3138 |
| spiral | 88 % → 84 % | 57.7 px | 0.39 | 0.96 | 2512 |
| loop | 66 % → 64 % | 85.6 px | 0.39 | 0.96 | 1359 |
| tilted | 37 % → 36 % | 102.0 px | 0.39 | 1.00 | 650 |
| over the wet one | 72 % → 69 % | 99.4 px | 0.39 | 0.96 | 536 |
| long, no reload | 98 % → 93 % | 44.0 px | 0.39 | 0.94 | 3231 | quarters: 0.39 → 0.39 → 0.39 → 0.37

Numbers say: light vs heavy: width 122.8 → 136.0 px, dark 0.39 → 0.39; pressure barely changes the width; the long stroke does not run out of paint.

## Brush Artist · Refs · Ground #8c6e28
Gouache · 130 px · 62.0 s

![Brush Artist · Refs · Ground #8c6e28](Brush-Artist-Refs-Ground-8c6e28.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 42 % → 40 % | 122.8 px | 0.33 | 0.94 | 630 |
| heavy line | 47 % → 42 % | 136.0 px | 0.33 | 0.90 | 691 |
| pressure swell | 43 % → 42 % | 162.8 px | 0.33 | 0.97 | 419 |
| fast wave | 83 % → 82 % | 95.8 px | 0.33 | 0.98 | 1602 |
| slow wave | 83 % → 76 % | 96.3 px | 0.33 | 0.91 | 2888 |
| spiral | 88 % → 84 % | 57.7 px | 0.33 | 0.96 | 2681 |
| loop | 66 % → 64 % | 85.6 px | 0.33 | 0.96 | 1413 |
| tilted | 37 % → 36 % | 102.0 px | 0.33 | 1.00 | 717 |
| over the wet one | 72 % → 69 % | 99.4 px | 0.33 | 0.96 | 748 |
| long, no reload | 98 % → 93 % | 44.0 px | 0.33 | 0.94 | 3322 | quarters: 0.33 → 0.33 → 0.33 → 0.31

Numbers say: light vs heavy: width 122.8 → 136.0 px, dark 0.33 → 0.33; pressure barely changes the width; the long stroke does not run out of paint.

## Brush Artist · Refs · Ground #e8b4a8
Gouache · 130 px · 62.4 s

![Brush Artist · Refs · Ground #e8b4a8](Brush-Artist-Refs-Ground-e8b4a8.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 42 % → 40 % | 122.8 px | 0.10 | 0.94 | 682 |
| heavy line | 47 % → 42 % | 136.0 px | 0.10 | 0.90 | 552 |
| pressure swell | 43 % → 42 % | 162.8 px | 0.10 | 0.97 | 518 |
| fast wave | 83 % → 82 % | 95.8 px | 0.10 | 0.98 | 1617 |
| slow wave | 83 % → 76 % | 96.3 px | 0.10 | 0.91 | 2861 |
| spiral | 88 % → 84 % | 57.7 px | 0.10 | 0.96 | 2609 |
| loop | 66 % → 64 % | 85.6 px | 0.10 | 0.96 | 1303 |
| tilted | 37 % → 36 % | 102.0 px | 0.10 | 1.00 | 754 |
| over the wet one | 72 % → 69 % | 99.4 px | 0.10 | 0.96 | 522 |
| long, no reload | 98 % → 93 % | 44.0 px | 0.10 | 0.94 | 3247 | quarters: 0.10 → 0.11 → 0.11 → 0.10

Numbers say: light vs heavy: width 122.8 → 136.0 px, dark 0.10 → 0.10; pressure barely changes the width; the long stroke does not run out of paint.

## Brush Artist · Refs · Ground #d8d4c8
Gouache · 130 px · 62.4 s

![Brush Artist · Refs · Ground #d8d4c8](Brush-Artist-Refs-Ground-d8d4c8.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 42 % → 40 % | 122.8 px | 0.05 | 0.94 | 568 |
| heavy line | 47 % → 42 % | 136.0 px | 0.05 | 0.90 | 879 |
| pressure swell | 43 % → 42 % | 162.8 px | 0.05 | 0.97 | 482 |
| fast wave | 83 % → 82 % | 95.8 px | 0.05 | 0.98 | 1581 |
| slow wave | 83 % → 76 % | 96.3 px | 0.05 | 0.91 | 2720 |
| spiral | 88 % → 84 % | 57.7 px | 0.05 | 0.96 | 2317 |
| loop | 66 % → 64 % | 85.6 px | 0.05 | 0.96 | 1246 |
| tilted | 37 % → 36 % | 102.0 px | 0.05 | 1.00 | 783 |
| over the wet one | 72 % → 69 % | 99.4 px | 0.05 | 0.96 | 564 |
| long, no reload | 98 % → 93 % | 44.0 px | 0.05 | 0.94 | 3222 | quarters: 0.05 → 0.05 → 0.05 → 0.05

Numbers say: light vs heavy: width 122.8 → 136.0 px, dark 0.05 → 0.05; pressure barely changes the width; the long stroke does not run out of paint.

## Brush Artist · Refs · Ground #e8e2b8
Gouache · 130 px · 59.7 s

![Brush Artist · Refs · Ground #e8e2b8](Brush-Artist-Refs-Ground-e8e2b8.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 42 % → 40 % | 122.8 px | 0.02 | 0.94 | 584 |
| heavy line | 47 % → 42 % | 136.0 px | 0.02 | 0.90 | 546 |
| pressure swell | 43 % → 42 % | 162.8 px | 0.02 | 0.97 | 503 |
| fast wave | 83 % → 82 % | 95.8 px | 0.02 | 0.98 | 1532 |
| slow wave | 83 % → 76 % | 96.3 px | 0.02 | 0.91 | 2332 |
| spiral | 88 % → 84 % | 57.7 px | 0.02 | 0.96 | 2261 |
| loop | 66 % → 64 % | 85.6 px | 0.02 | 0.96 | 1189 |
| tilted | 37 % → 36 % | 102.0 px | 0.02 | 1.00 | 740 |
| over the wet one | 72 % → 69 % | 99.4 px | 0.02 | 0.96 | 538 |
| long, no reload | 98 % → 93 % | 44.0 px | 0.02 | 0.94 | 3302 | quarters: 0.02 → 0.02 → 0.03 → 0.03

Numbers say: light vs heavy: width 122.8 → 136.0 px, dark 0.02 → 0.02; pressure barely changes the width; the long stroke does not run out of paint.

## Brush Artist · Refs · Ground #3a3a34
Gouache · 130 px · 60.4 s

![Brush Artist · Refs · Ground #3a3a34](Brush-Artist-Refs-Ground-3a3a34.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 42 % → 40 % | 122.8 px | 0.51 | 0.94 | 611 |
| heavy line | 47 % → 42 % | 136.0 px | 0.51 | 0.90 | 536 |
| pressure swell | 43 % → 42 % | 162.8 px | 0.51 | 0.97 | 457 |
| fast wave | 83 % → 82 % | 95.8 px | 0.51 | 0.98 | 1548 |
| slow wave | 83 % → 76 % | 96.3 px | 0.51 | 0.91 | 2366 |
| spiral | 88 % → 84 % | 57.7 px | 0.51 | 0.96 | 2270 |
| loop | 66 % → 64 % | 85.6 px | 0.51 | 0.96 | 1244 |
| tilted | 37 % → 36 % | 102.0 px | 0.51 | 1.00 | 735 |
| over the wet one | 72 % → 69 % | 99.4 px | 0.51 | 0.96 | 552 |
| long, no reload | 98 % → 93 % | 44.0 px | 0.51 | 0.94 | 3246 | quarters: 0.51 → 0.51 → 0.51 → 0.49

Numbers say: light vs heavy: width 122.8 → 136.0 px, dark 0.51 → 0.51; pressure barely changes the width; the long stroke does not run out of paint.

## Brush Artist · Refs · Ground #f06040
Gouache · 130 px · 58.8 s

![Brush Artist · Refs · Ground #f06040](Brush-Artist-Refs-Ground-f06040.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 42 % → 40 % | 122.8 px | 0.34 | 0.94 | 498 |
| heavy line | 47 % → 42 % | 136.0 px | 0.34 | 0.90 | 544 |
| pressure swell | 43 % → 42 % | 162.8 px | 0.34 | 0.97 | 411 |
| fast wave | 83 % → 82 % | 95.8 px | 0.34 | 0.98 | 1465 |
| slow wave | 83 % → 76 % | 96.3 px | 0.34 | 0.91 | 2517 |
| spiral | 88 % → 84 % | 57.7 px | 0.34 | 0.96 | 2322 |
| loop | 66 % → 64 % | 85.6 px | 0.34 | 0.96 | 1270 |
| tilted | 37 % → 36 % | 102.0 px | 0.34 | 1.00 | 706 |
| over the wet one | 72 % → 69 % | 99.4 px | 0.34 | 0.96 | 592 |
| long, no reload | 98 % → 93 % | 44.0 px | 0.34 | 0.94 | 3741 | quarters: 0.35 → 0.35 → 0.34 → 0.33

Numbers say: light vs heavy: width 122.8 → 136.0 px, dark 0.34 → 0.34; pressure barely changes the width; the long stroke does not run out of paint.

## Brush Artist · Refs · Ground #e85a10
Gouache · 130 px · 60.3 s

![Brush Artist · Refs · Ground #e85a10](Brush-Artist-Refs-Ground-e85a10.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 42 % → 40 % | 122.8 px | 0.37 | 0.94 | 482 |
| heavy line | 47 % → 42 % | 136.0 px | 0.37 | 0.90 | 509 |
| pressure swell | 43 % → 42 % | 162.8 px | 0.37 | 0.97 | 383 |
| fast wave | 83 % → 82 % | 95.8 px | 0.37 | 0.98 | 1342 |
| slow wave | 83 % → 76 % | 96.3 px | 0.37 | 0.91 | 2466 |
| spiral | 88 % → 84 % | 57.7 px | 0.37 | 0.96 | 2176 |
| loop | 66 % → 64 % | 85.6 px | 0.37 | 0.96 | 1209 |
| tilted | 37 % → 36 % | 102.0 px | 0.37 | 1.00 | 688 |
| over the wet one | 72 % → 69 % | 99.4 px | 0.37 | 0.96 | 568 |
| long, no reload | 98 % → 93 % | 44.0 px | 0.37 | 0.94 | 3200 | quarters: 0.37 → 0.37 → 0.37 → 0.36

Numbers say: light vs heavy: width 122.8 → 136.0 px, dark 0.37 → 0.37; pressure barely changes the width; the long stroke does not run out of paint.

## Brush Artist · Refs · Ground #3a4a6a
Gouache · 130 px · 60.0 s

![Brush Artist · Refs · Ground #3a4a6a](Brush-Artist-Refs-Ground-3a4a6a.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 42 % → 40 % | 122.8 px | 0.45 | 0.94 | 533 |
| heavy line | 47 % → 42 % | 136.0 px | 0.45 | 0.90 | 547 |
| pressure swell | 43 % → 42 % | 162.8 px | 0.45 | 0.97 | 410 |
| fast wave | 83 % → 82 % | 95.8 px | 0.45 | 0.98 | 1361 |
| slow wave | 83 % → 76 % | 96.3 px | 0.45 | 0.91 | 2439 |
| spiral | 88 % → 84 % | 57.7 px | 0.45 | 0.96 | 2266 |
| loop | 66 % → 64 % | 85.6 px | 0.45 | 0.96 | 1211 |
| tilted | 37 % → 36 % | 102.0 px | 0.45 | 1.00 | 698 |
| over the wet one | 72 % → 69 % | 99.4 px | 0.45 | 0.96 | 532 |
| long, no reload | 98 % → 93 % | 44.0 px | 0.45 | 0.94 | 3207 | quarters: 0.45 → 0.45 → 0.45 → 0.44

Numbers say: light vs heavy: width 122.8 → 136.0 px, dark 0.45 → 0.45; pressure barely changes the width; the long stroke does not run out of paint.

## Brush Artist · Refs · Ground #8c8c88
Gouache · 130 px · 60.2 s

![Brush Artist · Refs · Ground #8c8c88](Brush-Artist-Refs-Ground-8c8c88.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 42 % → 40 % | 122.8 px | 0.24 | 0.94 | 445 |
| heavy line | 47 % → 42 % | 136.0 px | 0.24 | 0.90 | 514 |
| pressure swell | 43 % → 42 % | 162.8 px | 0.24 | 0.97 | 394 |
| fast wave | 83 % → 82 % | 95.8 px | 0.24 | 0.98 | 1352 |
| slow wave | 83 % → 76 % | 96.3 px | 0.24 | 0.91 | 2190 |
| spiral | 88 % → 84 % | 57.7 px | 0.24 | 0.96 | 2385 |
| loop | 66 % → 64 % | 85.6 px | 0.24 | 0.96 | 1224 |
| tilted | 37 % → 36 % | 102.0 px | 0.23 | 1.00 | 670 |
| over the wet one | 72 % → 69 % | 99.4 px | 0.23 | 0.96 | 571 |
| long, no reload | 98 % → 93 % | 44.0 px | 0.24 | 0.94 | 3383 | quarters: 0.24 → 0.24 → 0.24 → 0.22

Numbers say: light vs heavy: width 122.8 → 136.0 px, dark 0.24 → 0.24; pressure barely changes the width; the long stroke does not run out of paint.

## Brush Artist · Refs · Ground #6a1a3a
Gouache · 130 px · 61.5 s

![Brush Artist · Refs · Ground #6a1a3a](Brush-Artist-Refs-Ground-6a1a3a.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 42 % → 40 % | 122.8 px | 0.59 | 0.94 | 508 |
| heavy line | 47 % → 42 % | 136.0 px | 0.59 | 0.90 | 509 |
| pressure swell | 43 % → 42 % | 162.8 px | 0.59 | 0.97 | 401 |
| fast wave | 83 % → 82 % | 95.8 px | 0.59 | 0.98 | 1388 |
| slow wave | 83 % → 76 % | 96.3 px | 0.59 | 0.91 | 2289 |
| spiral | 88 % → 84 % | 57.7 px | 0.59 | 0.96 | 2237 |
| loop | 66 % → 64 % | 85.6 px | 0.59 | 0.96 | 1295 |
| tilted | 37 % → 36 % | 102.0 px | 0.59 | 1.00 | 762 |
| over the wet one | 72 % → 69 % | 99.4 px | 0.59 | 0.96 | 546 |
| long, no reload | 98 % → 93 % | 44.0 px | 0.59 | 0.94 | 3314 | quarters: 0.59 → 0.59 → 0.59 → 0.58

Numbers say: light vs heavy: width 122.8 → 136.0 px, dark 0.59 → 0.59; pressure barely changes the width; the long stroke does not run out of paint.

## Brush Artist · Refs · Ground #3a1a12
Gouache · 130 px · 60.8 s

![Brush Artist · Refs · Ground #3a1a12](Brush-Artist-Refs-Ground-3a1a12.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 42 % → 40 % | 122.8 px | 0.62 | 0.94 | 495 |
| heavy line | 47 % → 42 % | 136.0 px | 0.62 | 0.90 | 538 |
| pressure swell | 43 % → 42 % | 162.8 px | 0.62 | 0.97 | 392 |
| fast wave | 83 % → 82 % | 95.8 px | 0.62 | 0.98 | 1336 |
| slow wave | 83 % → 76 % | 96.3 px | 0.62 | 0.91 | 2376 |
| spiral | 88 % → 84 % | 57.7 px | 0.62 | 0.96 | 2319 |
| loop | 66 % → 64 % | 85.6 px | 0.62 | 0.96 | 1326 |
| tilted | 37 % → 36 % | 102.0 px | 0.62 | 1.00 | 721 |
| over the wet one | 72 % → 69 % | 99.4 px | 0.62 | 0.96 | 550 |
| long, no reload | 98 % → 93 % | 44.0 px | 0.62 | 0.94 | 3260 | quarters: 0.62 → 0.62 → 0.62 → 0.61

Numbers say: light vs heavy: width 122.8 → 136.0 px, dark 0.62 → 0.62; pressure barely changes the width; the long stroke does not run out of paint.

## Brush Artist · Refs · Ground #f0c020
Gouache · 130 px · 61.7 s

![Brush Artist · Refs · Ground #f0c020](Brush-Artist-Refs-Ground-f0c020.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 42 % → 40 % | 122.8 px | 0.12 | 0.94 | 512 |
| heavy line | 47 % → 42 % | 136.0 px | 0.12 | 0.90 | 554 |
| pressure swell | 43 % → 42 % | 162.8 px | 0.12 | 0.97 | 422 |
| fast wave | 83 % → 82 % | 95.8 px | 0.12 | 0.98 | 1381 |
| slow wave | 83 % → 76 % | 96.3 px | 0.12 | 0.91 | 2416 |
| spiral | 88 % → 84 % | 57.7 px | 0.12 | 0.96 | 2366 |
| loop | 66 % → 64 % | 85.6 px | 0.12 | 0.96 | 1205 |
| tilted | 37 % → 36 % | 102.0 px | 0.12 | 1.00 | 706 |
| over the wet one | 72 % → 69 % | 99.4 px | 0.12 | 0.96 | 555 |
| long, no reload | 98 % → 93 % | 44.0 px | 0.12 | 0.94 | 3399 | quarters: 0.12 → 0.12 → 0.13 → 0.12

Numbers say: light vs heavy: width 122.8 → 136.0 px, dark 0.12 → 0.12; pressure barely changes the width; the long stroke does not run out of paint.

## Brush Artist · Refs · Ground #e8dcc4
Gouache · 130 px · 60.5 s

![Brush Artist · Refs · Ground #e8dcc4](Brush-Artist-Refs-Ground-e8dcc4.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 42 % → 40 % | 122.8 px | 0.03 | 0.94 | 472 |
| heavy line | 47 % → 42 % | 136.0 px | 0.03 | 0.90 | 482 |
| pressure swell | 43 % → 42 % | 162.8 px | 0.03 | 0.97 | 373 |
| fast wave | 83 % → 82 % | 95.8 px | 0.03 | 0.98 | 1300 |
| slow wave | 83 % → 76 % | 96.3 px | 0.03 | 0.91 | 2376 |
| spiral | 88 % → 84 % | 57.7 px | 0.03 | 0.96 | 2124 |
| loop | 66 % → 64 % | 85.6 px | 0.03 | 0.96 | 1122 |
| tilted | 37 % → 36 % | 102.0 px | 0.03 | 1.00 | 657 |
| over the wet one | 72 % → 69 % | 99.4 px | 0.03 | 0.96 | 536 |
| long, no reload | 98 % → 93 % | 44.0 px | 0.03 | 0.94 | 3092 | quarters: 0.03 → 0.03 → 0.03 → 0.03

Numbers say: light vs heavy: width 122.8 → 136.0 px, dark 0.03 → 0.03; pressure barely changes the width; the long stroke does not run out of paint.

## Brush Artist · Refs · Ground #e070a0
Gouache · 130 px · 60.8 s

![Brush Artist · Refs · Ground #e070a0](Brush-Artist-Refs-Ground-e070a0.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 42 % → 40 % | 122.8 px | 0.25 | 0.94 | 444 |
| heavy line | 47 % → 42 % | 136.0 px | 0.25 | 0.90 | 525 |
| pressure swell | 43 % → 42 % | 162.8 px | 0.25 | 0.97 | 366 |
| fast wave | 83 % → 82 % | 95.8 px | 0.25 | 0.98 | 1248 |
| slow wave | 83 % → 76 % | 96.3 px | 0.25 | 0.91 | 2347 |
| spiral | 88 % → 84 % | 57.7 px | 0.25 | 0.96 | 2241 |
| loop | 66 % → 64 % | 85.6 px | 0.25 | 0.96 | 1099 |
| tilted | 37 % → 36 % | 102.0 px | 0.25 | 1.00 | 709 |
| over the wet one | 72 % → 69 % | 99.4 px | 0.25 | 0.96 | 522 |
| long, no reload | 98 % → 93 % | 44.0 px | 0.25 | 0.94 | 3355 | quarters: 0.25 → 0.25 → 0.25 → 0.24

Numbers say: light vs heavy: width 122.8 → 136.0 px, dark 0.25 → 0.25; pressure barely changes the width; the long stroke does not run out of paint.

## Brush Artist · Refs · Ground #f0a020
Gouache · 130 px · 61.0 s

![Brush Artist · Refs · Ground #f0a020](Brush-Artist-Refs-Ground-f0a020.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 42 % → 40 % | 122.8 px | 0.19 | 0.94 | 477 |
| heavy line | 47 % → 42 % | 136.0 px | 0.19 | 0.90 | 518 |
| pressure swell | 43 % → 42 % | 162.8 px | 0.19 | 0.97 | 390 |
| fast wave | 83 % → 82 % | 95.8 px | 0.19 | 0.98 | 1421 |
| slow wave | 83 % → 76 % | 96.3 px | 0.19 | 0.91 | 2502 |
| spiral | 88 % → 84 % | 57.7 px | 0.19 | 0.96 | 2365 |
| loop | 66 % → 64 % | 85.6 px | 0.19 | 0.96 | 1224 |
| tilted | 37 % → 36 % | 102.0 px | 0.19 | 1.00 | 729 |
| over the wet one | 72 % → 69 % | 99.4 px | 0.19 | 0.96 | 562 |
| long, no reload | 98 % → 93 % | 44.0 px | 0.19 | 0.94 | 3437 | quarters: 0.18 → 0.19 → 0.19 → 0.18

Numbers say: light vs heavy: width 122.8 → 136.0 px, dark 0.19 → 0.19; pressure barely changes the width; the long stroke does not run out of paint.

## Brush Artist · Refs · Ground #e8f020
Gouache · 130 px · 62.6 s

![Brush Artist · Refs · Ground #e8f020](Brush-Artist-Refs-Ground-e8f020.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 42 % → 40 % | 122.8 px | 0.05 | 0.94 | 497 |
| heavy line | 47 % → 42 % | 136.0 px | 0.05 | 0.90 | 491 |
| pressure swell | 43 % → 42 % | 162.8 px | 0.06 | 0.97 | 375 |
| fast wave | 83 % → 82 % | 95.8 px | 0.05 | 0.98 | 1314 |
| slow wave | 83 % → 76 % | 96.3 px | 0.05 | 0.91 | 2387 |
| spiral | 88 % → 84 % | 57.7 px | 0.05 | 0.96 | 2386 |
| loop | 66 % → 64 % | 85.6 px | 0.05 | 0.96 | 1171 |
| tilted | 37 % → 36 % | 102.0 px | 0.05 | 1.00 | 767 |
| over the wet one | 72 % → 69 % | 99.4 px | 0.05 | 0.96 | 561 |
| long, no reload | 98 % → 93 % | 44.0 px | 0.06 | 0.94 | 3385 | quarters: 0.05 → 0.05 → 0.06 → 0.07

Numbers say: light vs heavy: width 122.8 → 136.0 px, dark 0.05 → 0.05; pressure barely changes the width; the long stroke does not run out of paint.

## Brush Artist · Refs · Ground #ff6a10
Gouache · 130 px · 63.8 s

![Brush Artist · Refs · Ground #ff6a10](Brush-Artist-Refs-Ground-ff6a10.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 42 % → 40 % | 122.8 px | 0.36 | 0.94 | 499 |
| heavy line | 47 % → 42 % | 136.0 px | 0.36 | 0.90 | 556 |
| pressure swell | 43 % → 42 % | 162.8 px | 0.36 | 0.97 | 403 |
| fast wave | 83 % → 82 % | 95.8 px | 0.36 | 0.98 | 1414 |
| slow wave | 83 % → 76 % | 96.3 px | 0.36 | 0.91 | 2527 |
| spiral | 88 % → 84 % | 57.7 px | 0.36 | 0.96 | 2460 |
| loop | 66 % → 64 % | 85.6 px | 0.36 | 0.96 | 1650 |
| tilted | 37 % → 36 % | 102.0 px | 0.36 | 1.00 | 792 |
| over the wet one | 72 % → 69 % | 99.4 px | 0.36 | 0.96 | 568 |
| long, no reload | 98 % → 93 % | 44.0 px | 0.36 | 0.94 | 3469 | quarters: 0.36 → 0.36 → 0.36 → 0.35

Numbers say: light vs heavy: width 122.8 → 136.0 px, dark 0.36 → 0.36; pressure barely changes the width; the long stroke does not run out of paint.

## Brush Artist · Refs · Ground #3a6a8a
Gouache · 130 px · 63.8 s

![Brush Artist · Refs · Ground #3a6a8a](Brush-Artist-Refs-Ground-3a6a8a.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 42 % → 40 % | 122.8 px | 0.37 | 0.94 | 517 |
| heavy line | 47 % → 42 % | 136.0 px | 0.37 | 0.90 | 521 |
| pressure swell | 43 % → 42 % | 162.8 px | 0.37 | 0.97 | 432 |
| fast wave | 83 % → 82 % | 95.8 px | 0.37 | 0.98 | 1403 |
| slow wave | 83 % → 76 % | 96.3 px | 0.37 | 0.91 | 2437 |
| spiral | 88 % → 84 % | 57.7 px | 0.37 | 0.96 | 2377 |
| loop | 66 % → 64 % | 85.6 px | 0.37 | 0.96 | 1742 |
| tilted | 37 % → 36 % | 102.0 px | 0.37 | 1.00 | 800 |
| over the wet one | 72 % → 69 % | 99.4 px | 0.37 | 0.96 | 566 |
| long, no reload | 98 % → 93 % | 44.0 px | 0.37 | 0.94 | 3489 | quarters: 0.37 → 0.37 → 0.37 → 0.36

Numbers say: light vs heavy: width 122.8 → 136.0 px, dark 0.37 → 0.37; pressure barely changes the width; the long stroke does not run out of paint.

## Brush Artist · Ink — wash
Watercolor · 38 px · 32.2 s

![Brush Artist · Ink — wash](Brush-Artist-Ink-wash.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 11 % → 11 % | 31.6 px | 0.39 | 1.03 | 64 |
| heavy line | 19 % → 19 % | 54.3 px | 0.32 | 1.03 | 214 |
| pressure swell | 12 % → 12 % | 45.1 px | 0.37 | 1.04 | 80 |
| fast wave | 39 % → 41 % | 44.7 px | 0.30 | 1.05 | 194 |
| slow wave | 37 % → 38 % | 42.6 px | 0.37 | 1.04 | 348 |
| spiral | 57 % → 60 % | 37.9 px | 0.30 | 1.04 | 326 |
| loop | 32 % → 33 % | 41.8 px | 0.35 | 1.02 | 161 |
| tilted | 13 % → 14 % | 36.8 px | 0.38 | 1.04 | 120 |
| over the wet one | 29 % → 30 % | 42.8 px | 0.38 | 1.04 | 72 |
| long, no reload | 65 % → 70 % | 29.2 px | 0.29 | 1.08 | 462 | quarters: 0.34 → 0.26 → 0.18 → 0.12

Numbers say: light vs heavy: width 31.6 → 54.3 px, dark 0.39 → 0.32.

## Brush Artist · Ink — brush line
Ink · 16 px · 26.3 s

![Brush Artist · Ink — brush line](Brush-Artist-Ink-brush-line.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 3 % → 5 % | 7.7 px | 0.78 | 1.80 | 34 |
| heavy line | 13 % → 13 % | 39.0 px | 0.88 | 0.99 | 80 |
| pressure swell | 8 % → 8 % | 28.4 px | 0.87 | 1.05 | 61 |
| fast wave | 24 % → 23 % | 27.6 px | 0.87 | 0.96 | 145 |
| slow wave | 19 % → 19 % | 22.5 px | 0.87 | 0.97 | 176 |
| spiral | 30 % → 27 % | 19.9 px | 0.86 | 0.90 | 265 |
| loop | 18 % → 18 % | 23.4 px | 0.88 | 1.00 | 132 |
| tilted | 7 % → 7 % | 20.1 px | 0.88 | 1.01 | 64 |
| over the wet one | 17 % → 17 % | 26.8 px | 0.88 | 1.00 | 55 |
| long, no reload | 42 % → 31 % | 18.8 px | 0.85 | 0.73 | 336 | quarters: 0.49 → 0.40 → 0.30 → 0.21

Numbers say: light vs heavy: width 7.7 → 39.0 px, dark 0.78 → 0.88; wet paint spreads well beyond the stroke.

## Brush Artist · Ink — dry brush
Gouache · 30 px · 22.4 s

![Brush Artist · Ink — dry brush](Brush-Artist-Ink-dry-brush.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 7 % → 1 % | 21.8 px | 0.71 | 0.11 | 55 |
| heavy line | 10 % → 1 % | 27.7 px | 0.71 | 0.10 | 148 |
| pressure swell | 7 % → 2 % | 25.5 px | 0.71 | 0.23 | 77 |
| fast wave | 21 % → 2 % | 24.2 px | 0.71 | 0.09 | 220 |
| slow wave | 21 % → 2 % | 23.9 px | 0.71 | 0.08 | 378 |
| spiral | 31 % → 2 % | 20.6 px | 0.71 | 0.06 | 403 |
| loop | 18 % → 2 % | 23.9 px | 0.71 | 0.13 | 199 |
| tilted | 9 % → 8 % | 24.1 px | 0.71 | 0.96 | 125 |
| over the wet one | 17 % → 4 % | 22.8 px | 0.71 | 0.24 | 108 |
| long, no reload | 31 % → 3 % | 14.0 px | 0.71 | 0.09 | 590 | quarters: 0.38 → 0.32 → 0.22 → 0.09

Numbers say: light vs heavy: width 21.8 → 27.7 px, dark 0.71 → 0.71.

## Brush Artist · Watercolour — blue
Watercolor · 40 px · 27.8 s

![Brush Artist · Watercolour — blue](Brush-Artist-Watercolour-blue.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 6 % → 10 % | 16.7 px | 0.19 | 1.70 | 34 |
| heavy line | 11 % → 12 % | 31.5 px | 0.19 | 1.13 | 82 |
| pressure swell | 7 % → 9 % | 25.4 px | 0.20 | 1.32 | 45 |
| fast wave | 24 % → 25 % | 27.8 px | 0.18 | 1.05 | 136 |
| slow wave | 22 % → 27 % | 25.9 px | 0.19 | 1.22 | 256 |
| spiral | 38 % → 41 % | 25.1 px | 0.17 | 1.08 | 218 |
| loop | 20 % → 22 % | 25.3 px | 0.19 | 1.13 | 124 |
| tilted | 12 % → 12 % | 33.3 px | 0.19 | 1.00 | 89 |
| over the wet one | 21 % → 24 % | 24.7 px | 0.19 | 1.15 | 58 |
| long, no reload | 51 % → 54 % | 23.0 px | 0.16 | 1.04 | 342 | quarters: 0.14 → 0.10 → 0.08 → 0.06

Numbers say: light vs heavy: width 16.7 → 31.5 px, dark 0.19 → 0.19; wet paint spreads well beyond the stroke.

## Brush Artist · Watercolour — violet
Watercolor · 40 px · 27.8 s

![Brush Artist · Watercolour — violet](Brush-Artist-Watercolour-violet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 6 % → 10 % | 16.7 px | 0.14 | 1.70 | 31 |
| heavy line | 11 % → 12 % | 31.5 px | 0.14 | 1.13 | 70 |
| pressure swell | 7 % → 9 % | 25.4 px | 0.15 | 1.32 | 46 |
| fast wave | 24 % → 25 % | 27.8 px | 0.14 | 1.05 | 136 |
| slow wave | 22 % → 27 % | 25.9 px | 0.15 | 1.22 | 251 |
| spiral | 38 % → 41 % | 25.1 px | 0.13 | 1.08 | 224 |
| loop | 20 % → 22 % | 25.3 px | 0.15 | 1.13 | 147 |
| tilted | 12 % → 12 % | 33.3 px | 0.15 | 1.00 | 93 |
| over the wet one | 21 % → 24 % | 24.7 px | 0.15 | 1.15 | 62 |
| long, no reload | 51 % → 54 % | 23.0 px | 0.13 | 1.04 | 502 | quarters: 0.10 → 0.08 → 0.06 → 0.05

Numbers say: light vs heavy: width 16.7 → 31.5 px, dark 0.14 → 0.14; wet paint spreads well beyond the stroke.

## Brush Artist · Watercolour — teal
Watercolor · 40 px · 28.7 s

![Brush Artist · Watercolour — teal](Brush-Artist-Watercolour-teal.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 6 % → 10 % | 16.7 px | 0.26 | 1.70 | 32 |
| heavy line | 11 % → 12 % | 31.5 px | 0.27 | 1.13 | 71 |
| pressure swell | 7 % → 9 % | 25.4 px | 0.28 | 1.32 | 41 |
| fast wave | 24 % → 25 % | 27.8 px | 0.25 | 1.05 | 170 |
| slow wave | 22 % → 27 % | 25.9 px | 0.27 | 1.22 | 264 |
| spiral | 38 % → 41 % | 25.1 px | 0.23 | 1.08 | 229 |
| loop | 20 % → 22 % | 25.3 px | 0.27 | 1.13 | 150 |
| tilted | 12 % → 12 % | 33.3 px | 0.27 | 1.00 | 108 |
| over the wet one | 21 % → 24 % | 24.7 px | 0.27 | 1.15 | 59 |
| long, no reload | 51 % → 54 % | 23.0 px | 0.23 | 1.04 | 372 | quarters: 0.19 → 0.14 → 0.11 → 0.09

Numbers say: light vs heavy: width 16.7 → 31.5 px, dark 0.26 → 0.27; wet paint spreads well beyond the stroke.

## Brush Artist · Gouache
Gouache · 30 px · 32.2 s

![Brush Artist · Gouache](Brush-Artist-Gouache.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 8 % → 8 % | 24.4 px | 0.16 | 0.97 | 63 |
| heavy line | 15 % → 11 % | 42.8 px | 0.16 | 0.78 | 81 |
| pressure swell | 11 % → 9 % | 41.0 px | 0.16 | 0.84 | 64 |
| fast wave | 30 % → 13 % | 34.4 px | 0.16 | 0.45 | 180 |
| slow wave | 29 % → 14 % | 33.9 px | 0.16 | 0.46 | 464 |
| spiral | 40 % → 14 % | 26.6 px | 0.16 | 0.35 | 357 |
| loop | 23 % → 15 % | 30.4 px | 0.16 | 0.62 | 182 |
| tilted | 10 % → 10 % | 27.1 px | 0.16 | 1.01 | 101 |
| over the wet one | 21 % → 19 % | 32.8 px | 0.16 | 0.89 | 58 |
| long, no reload | 43 % → 15 % | 19.1 px | 0.16 | 0.35 | 507 | quarters: 0.10 → 0.07 → 0.04 → 0.02

Numbers say: light vs heavy: width 24.4 → 42.8 px, dark 0.16 → 0.16.

## Brush Artist · Oil — bristle
Oil · 30 px · 18.8 s

![Brush Artist · Oil — bristle](Brush-Artist-Oil-bristle.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 9 % → 9 % | 26.2 px | 0.54 | 1.00 | 103 |
| heavy line | 10 % → 10 % | 28.5 px | 0.54 | 1.00 | 129 |
| pressure swell | 8 % → 8 % | 28.2 px | 0.55 | 1.00 | 94 |
| fast wave | 24 % → 24 % | 27.3 px | 0.55 | 1.00 | 335 |
| slow wave | 24 % → 24 % | 28.2 px | 0.55 | 1.00 | 468 |
| spiral | 39 % → 39 % | 25.6 px | 0.54 | 1.00 | 498 |
| loop | 20 % → 20 % | 26.2 px | 0.54 | 1.00 | 249 |
| tilted | 11 % → 11 % | 29.9 px | 0.54 | 1.00 | 134 |
| over the wet one | 20 % → 20 % | 25.2 px | 0.54 | 1.00 | 119 |
| long, no reload | 50 % → 50 % | 22.4 px | 0.54 | 1.00 | 720 | quarters: 0.32 → 0.30 → 0.29 → 0.28

Numbers say: light vs heavy: width 26.2 → 28.5 px, dark 0.54 → 0.54; pressure barely changes the width; the long stroke does not run out of paint.

## Brush Artist · Charcoal — stick
Charcoal · 28 px · 9.8 s

![Brush Artist · Charcoal — stick](Brush-Artist-Charcoal-stick.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 3 % → 3 % | 8.4 px | 0.85 | 1.00 | 18 |
| heavy line | 6 % → 6 % | 17.8 px | 0.85 | 1.00 | 19 |
| pressure swell | 4 % → 4 % | 13.9 px | 0.85 | 1.00 | 20 |
| fast wave | 12 % → 12 % | 14.0 px | 0.85 | 1.00 | 47 |
| slow wave | 11 % → 11 % | 12.5 px | 0.85 | 1.00 | 77 |
| spiral | 19 % → 19 % | 12.7 px | 0.85 | 1.00 | 73 |
| loop | 10 % → 10 % | 12.8 px | 0.85 | 1.00 | 41 |
| tilted | 4 % → 4 % | 10.9 px | 0.85 | 1.00 | 29 |
| over the wet one | 9 % → 9 % | 13.5 px | 0.85 | 1.00 | 27 |
| long, no reload | 27 % → 27 % | 12.2 px | 0.85 | 1.00 | 120 | quarters: 0.26 → 0.25 → 0.26 → 0.27

Numbers say: light vs heavy: width 8.4 → 17.8 px, dark 0.85 → 0.85; the long stroke does not run out of paint.

## Brush Artist · Charcoal — stick B
Charcoal · 36 px · 10.0 s

![Brush Artist · Charcoal — stick B](Brush-Artist-Charcoal-stick-B.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 4 % → 4 % | 10.5 px | 0.85 | 1.00 | 22 |
| heavy line | 7 % → 7 % | 21.1 px | 0.85 | 1.00 | 34 |
| pressure swell | 4 % → 4 % | 16.5 px | 0.85 | 1.00 | 19 |
| fast wave | 15 % → 15 % | 16.8 px | 0.85 | 1.00 | 63 |
| slow wave | 13 % → 13 % | 14.7 px | 0.85 | 1.00 | 111 |
| spiral | 23 % → 23 % | 15.0 px | 0.85 | 1.00 | 113 |
| loop | 11 % → 11 % | 14.8 px | 0.85 | 1.00 | 57 |
| tilted | 4 % → 4 % | 12.3 px | 0.85 | 1.00 | 38 |
| over the wet one | 10 % → 10 % | 15.9 px | 0.85 | 1.00 | 25 |
| long, no reload | 31 % → 31 % | 13.9 px | 0.85 | 1.00 | 172 | quarters: 0.30 → 0.28 → 0.29 → 0.30

Numbers say: light vs heavy: width 10.5 → 21.1 px, dark 0.85 → 0.85; the long stroke does not run out of paint.

## Brush Artist · Charcoal — stick C
Charcoal · 22 px · 9.4 s

![Brush Artist · Charcoal — stick C](Brush-Artist-Charcoal-stick-C.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 2 % → 2 % | 6.9 px | 0.85 | 1.00 | 24 |
| heavy line | 5 % → 5 % | 15.3 px | 0.85 | 1.00 | 10 |
| pressure swell | 3 % → 3 % | 12.2 px | 0.85 | 1.00 | 7 |
| fast wave | 10 % → 10 % | 12.1 px | 0.85 | 1.00 | 30 |
| slow wave | 9 % → 9 % | 10.8 px | 0.85 | 1.00 | 46 |
| spiral | 17 % → 17 % | 11.0 px | 0.85 | 1.00 | 64 |
| loop | 9 % → 9 % | 11.4 px | 0.85 | 1.00 | 38 |
| tilted | 4 % → 4 % | 9.9 px | 0.85 | 1.00 | 28 |
| over the wet one | 8 % → 8 % | 11.7 px | 0.85 | 1.00 | 11 |
| long, no reload | 24 % → 24 % | 11.0 px | 0.85 | 1.00 | 104 | quarters: 0.24 → 0.22 → 0.23 → 0.24

Numbers say: light vs heavy: width 6.9 → 15.3 px, dark 0.85 → 0.85; the long stroke does not run out of paint.

## Brush Artist · Refs · #01 Henry Ward peach cloud — own sheet
own sheet 600 × 600 · Gouache · 44 px · 76.4 s

![Brush Artist · Refs · #01 Henry Ward peach cloud — own sheet](Brush-Artist-Refs-01-Henry-Ward-peach-cloud-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 99 % → 99 % | 62.0 px | 0.00 | 1.00 | 945 |
| stroke 2 | 100 % → 99 % | 88.9 px | 0.00 | 0.99 | 1270 |
| stroke 3 | 99 % → 99 % | 88.0 px | 0.00 | 1.00 | 1039 |
| stroke 4 | 100 % → 99 % | 85.6 px | 0.00 | 0.99 | 1157 |
| stroke 5 | 99 % → 98 % | 88.6 px | 0.00 | 0.99 | 1163 |
| stroke 6 | 100 % → 99 % | 87.2 px | 0.00 | 0.99 | 1169 |
| stroke 7 | 99 % → 99 % | 90.9 px | 0.00 | 1.00 | 1220 |
| stroke 8 | 100 % → 98 % | 88.7 px | 0.00 | 0.99 | 1016 |
| stroke 9 | 100 % → 98 % | 60.0 px | 0.00 | 0.98 | 807 |
| stroke 10 | 100 % → 100 % | 129.9 px | 0.00 | 1.00 | 198 |
| stroke 11 | 100 % → 100 % | 160.5 px | 0.00 | 1.00 | 241 |
| stroke 12 | 100 % → 100 % | 131.4 px | 0.00 | 1.00 | 157 |
| stroke 13 | 100 % → 100 % | 162.0 px | 0.00 | 1.00 | 180 |
| stroke 14 | 100 % → 100 % | 135.7 px | 0.00 | 1.00 | 191 |
| stroke 15 | 100 % → 100 % | 148.2 px | 0.00 | 1.00 | 165 |
| stroke 16 | 100 % → 100 % | 138.8 px | 0.00 | 1.00 | 169 |
| stroke 17 | 100 % → 100 % | 129.3 px | 0.00 | 1.00 | 197 |
| stroke 18 | 100 % → 100 % | 124.6 px | 0.00 | 1.00 | 244 |
| stroke 19 | 100 % → 100 % | 125.6 px | 0.00 | 1.00 | 196 |
| stroke 20 | 100 % → 100 % | 137.3 px | 0.00 | 1.00 | 216 |
| stroke 21 | 100 % → 100 % | 136.3 px | 0.00 | 1.00 | 195 |
| stroke 22 | 100 % → 100 % | 132.5 px | 0.00 | 1.00 | 177 |
| stroke 23 | 100 % → 100 % | 129.7 px | 0.00 | 1.00 | 204 |
| stroke 24 | 100 % → 100 % | 135.8 px | 0.00 | 1.00 | 160 |
| stroke 25 | 100 % → 100 % | 140.2 px | 0.00 | 1.00 | 193 |
| stroke 26 | 100 % → 100 % | 124.0 px | 0.00 | 1.00 | 218 |
| stroke 27 | 100 % → 100 % | 131.8 px | 0.00 | 1.00 | 203 |
| stroke 28 | 100 % → 100 % | 124.2 px | 0.00 | 1.00 | 189 |
| stroke 29 | 100 % → 100 % | 131.9 px | 0.00 | 1.00 | 214 |
| stroke 30 | 100 % → 100 % | 134.2 px | 0.00 | 1.00 | 197 |
| stroke 31 | 100 % → 100 % | 134.5 px | 0.00 | 1.00 | 240 |
| stroke 32 | 100 % → 100 % | 127.6 px | 0.00 | 1.00 | 178 |
| stroke 33 | 100 % → 100 % | 134.4 px | 0.00 | 1.00 | 180 |

## Brush Artist · Refs · #02 Henry Ward cream strokes — own sheet
own sheet 600 × 600 · Gouache · 46 px · 68.3 s

![Brush Artist · Refs · #02 Henry Ward cream strokes — own sheet](Brush-Artist-Refs-02-Henry-Ward-cream-strokes-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 95 % → 99 % | 58.8 px | 0.00 | 1.04 | 794 |
| stroke 2 | 99 % → 99 % | 91.6 px | 0.00 | 1.00 | 1214 |
| stroke 3 | 98 % → 99 % | 89.0 px | 0.00 | 1.01 | 1131 |
| stroke 4 | 95 % → 99 % | 89.9 px | 0.00 | 1.04 | 1109 |
| stroke 5 | 98 % → 99 % | 90.2 px | 0.00 | 1.00 | 1172 |
| stroke 6 | 100 % → 99 % | 89.6 px | 0.00 | 1.00 | 975 |
| stroke 7 | 99 % → 99 % | 93.0 px | 0.00 | 1.00 | 1008 |
| stroke 8 | 98 % → 99 % | 92.0 px | 0.00 | 1.00 | 1067 |
| stroke 9 | 100 % → 99 % | 61.8 px | 0.00 | 0.99 | 895 |
| stroke 10 | 100 % → 99 % | 129.9 px | 0.00 | 0.99 | 329 |
| stroke 11 | 100 % → 99 % | 142.3 px | 0.00 | 0.99 | 262 |
| stroke 12 | 100 % → 100 % | 138.5 px | 0.00 | 1.00 | 270 |
| stroke 13 | 100 % → 99 % | 137.9 px | 0.00 | 0.99 | 273 |
| stroke 14 | 100 % → 98 % | 129.1 px | 0.00 | 0.99 | 259 |
| stroke 15 | 100 % → 100 % | 121.4 px | 0.00 | 1.00 | 247 |
| stroke 16 | 100 % → 100 % | 128.5 px | 0.00 | 1.00 | 250 |

## Brush Artist · Refs · #03 Henry Ward navy contours — own sheet
own sheet 600 × 600 · Heavy acrylic · 22 px · 2.7 s

![Brush Artist · Refs · #03 Henry Ward navy contours — own sheet](Brush-Artist-Refs-03-Henry-Ward-navy-contours-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 15 % → 20 % | 23.1 px | 0.75 | 1.28 | 110 |
| stroke 2 | 28 % → 30 % | 26.3 px | 0.75 | 1.09 | 101 |
| stroke 3 | 28 % → 28 % | 29.4 px | 0.75 | 0.99 | 132 |
| stroke 4 | 26 % → 24 % | 45.9 px | 0.75 | 0.92 | 172 |

## Brush Artist · Refs · #04 Henry Ward grey cloud — own sheet
own sheet 600 × 600 · Gouache · 50 px · 73.3 s

![Brush Artist · Refs · #04 Henry Ward grey cloud — own sheet](Brush-Artist-Refs-04-Henry-Ward-grey-cloud-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 91 % → 99 % | 59.2 px | 0.00 | 1.09 | 850 |
| stroke 2 | 96 % → 99 % | 95.5 px | 0.00 | 1.04 | 1162 |
| stroke 3 | 94 % → 99 % | 92.8 px | 0.00 | 1.06 | 1022 |
| stroke 4 | 96 % → 99 % | 93.8 px | 0.00 | 1.04 | 1038 |
| stroke 5 | 94 % → 99 % | 92.9 px | 0.00 | 1.05 | 984 |
| stroke 6 | 92 % → 99 % | 93.7 px | 0.00 | 1.08 | 1142 |
| stroke 7 | 96 % → 99 % | 96.2 px | 0.00 | 1.04 | 1087 |
| stroke 8 | 95 % → 99 % | 95.6 px | 0.00 | 1.04 | 975 |
| stroke 9 | 100 % → 99 % | 67.9 px | 0.00 | 0.99 | 825 |
| stroke 10 | 100 % → 100 % | 151.1 px | 0.00 | 1.00 | 199 |
| stroke 11 | 100 % → 100 % | 153.3 px | 0.00 | 1.00 | 282 |
| stroke 12 | 100 % → 100 % | 137.6 px | 0.00 | 1.00 | 242 |
| stroke 13 | 100 % → 99 % | 149.6 px | 0.00 | 0.99 | 281 |
| stroke 14 | 100 % → 100 % | 148.6 px | 0.00 | 1.00 | 236 |
| stroke 15 | 100 % → 100 % | 159.9 px | 0.00 | 1.00 | 200 |
| stroke 16 | 100 % → 100 % | 146.6 px | 0.00 | 1.00 | 271 |
| stroke 17 | 100 % → 100 % | 151.2 px | 0.00 | 1.00 | 254 |
| stroke 18 | 100 % → 100 % | 148.5 px | 0.00 | 1.00 | 326 |
| stroke 19 | 100 % → 100 % | 160.0 px | 0.00 | 1.00 | 248 |
| stroke 20 | 100 % → 100 % | 135.7 px | 0.00 | 1.00 | 250 |
| stroke 21 | 100 % → 100 % | 152.0 px | 0.00 | 1.00 | 276 |
| stroke 22 | 100 % → 100 % | 137.1 px | 0.00 | 1.00 | 234 |
| stroke 23 | 100 % → 100 % | 154.5 px | 0.00 | 1.00 | 247 |
| stroke 24 | 100 % → 100 % | 147.1 px | 0.00 | 1.00 | 248 |
| stroke 25 | 100 % → 99 % | 158.1 px | 0.00 | 0.99 | 273 |
| stroke 26 | 100 % → 100 % | 140.5 px | 0.00 | 1.00 | 229 |
| stroke 27 | 100 % → 100 % | 159.2 px | 0.00 | 1.00 | 242 |
| stroke 28 | 100 % → 100 % | 149.2 px | 0.00 | 1.00 | 258 |
| stroke 29 | 100 % → 100 % | 162.8 px | 0.00 | 1.00 | 234 |

## Brush Artist · Refs · #05 Henry Ward green in rust loops — own sheet
own sheet 600 × 600 · Heavy acrylic · 20 px · 63.6 s

![Brush Artist · Refs · #05 Henry Ward green in rust loops — own sheet](Brush-Artist-Refs-05-Henry-Ward-green-in-rust-loops-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 100 % → 99 % | 40.6 px | 0.00 | 0.99 | 921 |
| stroke 2 | 100 % → 99 % | 45.0 px | 0.00 | 0.99 | 1136 |
| stroke 3 | 100 % → 99 % | 49.4 px | 0.00 | 0.99 | 943 |
| stroke 4 | 100 % → 99 % | 46.8 px | 0.01 | 0.99 | 1031 |
| stroke 5 | 100 % → 99 % | 47.6 px | 0.02 | 0.99 | 998 |
| stroke 6 | 100 % → 99 % | 48.5 px | 0.02 | 0.99 | 1155 |
| stroke 7 | 100 % → 99 % | 46.8 px | 0.01 | 0.99 | 1060 |
| stroke 8 | 100 % → 99 % | 47.6 px | 0.01 | 0.99 | 977 |
| stroke 9 | 100 % → 99 % | 41.5 px | 0.01 | 0.99 | 842 |
| stroke 10 | 100 % → 100 % | 131.6 px | 0.02 | 1.00 | 147 |
| stroke 11 | 100 % → 100 % | 155.1 px | 0.02 | 1.00 | 176 |
| stroke 12 | 100 % → 100 % | 145.9 px | 0.03 | 1.00 | 150 |

## Brush Artist · Refs · #06 Henry Ward scrubbed grey — own sheet
own sheet 600 × 600 · Gouache · 50 px · 74.6 s

![Brush Artist · Refs · #06 Henry Ward scrubbed grey — own sheet](Brush-Artist-Refs-06-Henry-Ward-scrubbed-grey-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 89 % → 98 % | 57.9 px | 0.00 | 1.11 | 851 |
| stroke 2 | 95 % → 99 % | 95.9 px | 0.00 | 1.03 | 1150 |
| stroke 3 | 96 % → 99 % | 95.3 px | 0.00 | 1.04 | 970 |
| stroke 4 | 94 % → 99 % | 92.8 px | 0.00 | 1.06 | 954 |
| stroke 5 | 96 % → 99 % | 93.9 px | 0.00 | 1.03 | 981 |
| stroke 6 | 92 % → 99 % | 93.4 px | 0.00 | 1.08 | 1146 |
| stroke 7 | 91 % → 99 % | 93.6 px | 0.00 | 1.08 | 1173 |
| stroke 8 | 92 % → 99 % | 93.0 px | 0.00 | 1.08 | 1017 |
| stroke 9 | 100 % → 99 % | 67.1 px | 0.00 | 0.99 | 865 |
| stroke 10 | 100 % → 100 % | 141.6 px | 0.00 | 1.00 | 234 |
| stroke 11 | 100 % → 100 % | 155.7 px | 0.00 | 1.00 | 261 |
| stroke 12 | 100 % → 100 % | 146.6 px | 0.00 | 1.00 | 248 |
| stroke 13 | 100 % → 100 % | 159.5 px | 0.00 | 1.00 | 243 |
| stroke 14 | 100 % → 100 % | 149.4 px | 0.00 | 1.00 | 223 |
| stroke 15 | 100 % → 100 % | 155.4 px | 0.00 | 1.00 | 237 |
| stroke 16 | 100 % → 100 % | 144.9 px | 0.00 | 1.00 | 276 |
| stroke 17 | 100 % → 100 % | 158.8 px | 0.00 | 1.00 | 263 |
| stroke 18 | 100 % → 100 % | 146.6 px | 0.00 | 1.00 | 265 |
| stroke 19 | 100 % → 100 % | 161.7 px | 0.00 | 1.00 | 239 |
| stroke 20 | 100 % → 100 % | 144.3 px | 0.00 | 1.00 | 252 |
| stroke 21 | 100 % → 100 % | 161.0 px | 0.00 | 1.00 | 258 |
| stroke 22 | 100 % → 100 % | 143.2 px | 0.00 | 1.00 | 231 |
| stroke 23 | 100 % → 100 % | 151.2 px | 0.00 | 1.00 | 276 |
| stroke 24 | 100 % → 100 % | 143.5 px | 0.00 | 1.00 | 235 |
| stroke 25 | 100 % → 100 % | 154.5 px | 0.00 | 1.00 | 244 |
| stroke 26 | 100 % → 100 % | 145.7 px | 0.00 | 1.00 | 217 |
| stroke 27 | 100 % → 100 % | 156.3 px | 0.00 | 1.00 | 287 |
| stroke 28 | 100 % → 100 % | 152.6 px | 0.00 | 1.00 | 305 |
| stroke 29 | 100 % → 100 % | 161.4 px | 0.00 | 1.00 | 272 |
| stroke 30 | 100 % → 100 % | 146.2 px | 0.00 | 1.00 | 255 |
| stroke 31 | 100 % → 100 % | 159.1 px | 0.00 | 1.00 | 256 |

## Brush Artist · Refs · #07 Henry Ward blue L + black zigzag — own sheet
own sheet 600 × 600 · Heavy acrylic · 34 px · 1.9 s

![Brush Artist · Refs · #07 Henry Ward blue L + black zigzag — own sheet](Brush-Artist-Refs-07-Henry-Ward-blue-L-black-zigzag-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 30 % → 31 % | 35.6 px | 0.63 | 1.05 | 170 |
| stroke 2 | 31 % → 29 % | 38.6 px | 0.63 | 0.94 | 100 |

## Brush Artist · Refs · #08 Henry Ward olive bands — own sheet
own sheet 600 × 600 · Gouache · 34 px · 5.5 s

![Brush Artist · Refs · #08 Henry Ward olive bands — own sheet](Brush-Artist-Refs-08-Henry-Ward-olive-bands-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 33 % → 19 % | 32.3 px | 0.61 | 0.58 | 157 |
| stroke 2 | 37 % → 20 % | 44.3 px | 0.61 | 0.53 | 151 |
| stroke 3 | 30 % → 23 % | 32.4 px | 0.61 | 0.75 | 154 |
| stroke 4 | 38 % → 37 % | 44.3 px | 0.61 | 0.98 | 169 |
| stroke 5 | 50 % → 35 % | 52.4 px | 0.61 | 0.71 | 180 |
| stroke 6 | 36 % → 22 % | 32.2 px | 0.61 | 0.61 | 163 |

## Brush Artist · Refs · #09 Henry Ward white loops — own sheet
own sheet 600 × 600 · Gouache · 46 px · 67.1 s

![Brush Artist · Refs · #09 Henry Ward white loops — own sheet](Brush-Artist-Refs-09-Henry-Ward-white-loops-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 94 % → 99 % | 61.2 px | 0.00 | 1.06 | 814 |
| stroke 2 | 99 % → 100 % | 90.9 px | 0.00 | 1.00 | 1063 |
| stroke 3 | 95 % → 100 % | 89.9 px | 0.00 | 1.04 | 1142 |
| stroke 4 | 98 % → 99 % | 93.6 px | 0.00 | 1.01 | 1045 |
| stroke 5 | 98 % → 99 % | 90.1 px | 0.00 | 1.01 | 986 |
| stroke 6 | 99 % → 99 % | 92.2 px | 0.00 | 1.01 | 1028 |
| stroke 7 | 100 % → 99 % | 89.8 px | 0.00 | 1.00 | 1109 |
| stroke 8 | 98 % → 99 % | 89.1 px | 0.00 | 1.01 | 1008 |
| stroke 9 | 100 % → 99 % | 64.4 px | 0.00 | 0.99 | 975 |
| stroke 10 | 100 % → 100 % | 31.6 px | 0.00 | 1.00 | 1209 |
| stroke 11 | 100 % → 100 % | 70.2 px | 0.00 | 1.00 | 1233 |
| stroke 12 | 100 % → 100 % | 58.2 px | 0.00 | 1.00 | 1148 |

## Brush Artist · Refs · #10 Henry Ward maroon loops — own sheet
own sheet 600 × 600 · Heavy acrylic · 30 px · 3.2 s

![Brush Artist · Refs · #10 Henry Ward maroon loops — own sheet](Brush-Artist-Refs-10-Henry-Ward-maroon-loops-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 16 % → 33 % | 28.6 px | 0.77 | 2.07 | 216 |
| stroke 2 | 29 % → 47 % | 46.0 px | 0.77 | 1.60 | 137 |
| stroke 3 | 40 % → 50 % | 54.7 px | 0.77 | 1.24 | 154 |
| stroke 4 | 45 % → 43 % | 64.1 px | 0.77 | 0.96 | 97 |
| stroke 5 | 41 % → 38 % | 70.6 px | 0.77 | 0.93 | 171 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #11 Henry Ward purple spun balls — own sheet
own sheet 600 × 600 · Heavy acrylic · 36 px · 65.1 s

![Brush Artist · Refs · #11 Henry Ward purple spun balls — own sheet](Brush-Artist-Refs-11-Henry-Ward-purple-spun-balls-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 100 % → 99 % | 53.8 px | 0.00 | 0.99 | 817 |
| stroke 2 | 100 % → 100 % | 73.2 px | 0.00 | 1.00 | 1000 |
| stroke 3 | 100 % → 99 % | 74.1 px | 0.00 | 0.99 | 1059 |
| stroke 4 | 100 % → 99 % | 77.6 px | 0.00 | 0.99 | 1108 |
| stroke 5 | 100 % → 99 % | 76.8 px | 0.00 | 0.99 | 1032 |
| stroke 6 | 100 % → 99 % | 74.1 px | 0.08 | 0.99 | 1275 |
| stroke 7 | 100 % → 99 % | 73.2 px | 0.26 | 0.99 | 1070 |
| stroke 8 | 100 % → 99 % | 75.9 px | 0.30 | 0.99 | 1217 |
| stroke 9 | 100 % → 99 % | 54.7 px | 0.03 | 0.99 | 1001 |
| stroke 10 | 100 % → 100 % | 49.5 px | 0.28 | 1.00 | 412 |
| stroke 11 | 100 % → 100 % | 48.8 px | 0.35 | 1.00 | 380 |
| stroke 12 | 100 % → 100 % | 48.7 px | 0.30 | 1.00 | 416 |

## Brush Artist · Refs · #12 Henry Ward black-olive cage — own sheet
own sheet 600 × 600 · Gouache · 28 px · 65.7 s

![Brush Artist · Refs · #12 Henry Ward black-olive cage — own sheet](Brush-Artist-Refs-12-Henry-Ward-black-olive-cage-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 100 % → 99 % | 46.8 px | 0.00 | 0.99 | 899 |
| stroke 2 | 100 % → 99 % | 60.9 px | 0.00 | 0.99 | 1087 |
| stroke 3 | 100 % → 99 % | 59.1 px | 0.01 | 0.99 | 1047 |
| stroke 4 | 100 % → 99 % | 60.9 px | 0.04 | 0.99 | 1038 |
| stroke 5 | 100 % → 99 % | 61.8 px | 0.21 | 0.99 | 1036 |
| stroke 6 | 100 % → 99 % | 61.8 px | 0.16 | 0.99 | 1233 |
| stroke 7 | 100 % → 99 % | 61.8 px | 0.27 | 0.99 | 1224 |
| stroke 8 | 100 % → 99 % | 61.8 px | 0.07 | 0.99 | 1196 |
| stroke 9 | 100 % → 99 % | 46.8 px | 0.00 | 0.99 | 893 |
| stroke 10 | 100 % → 100 % | 137.9 px | 0.16 | 1.00 | 219 |
| stroke 11 | 100 % → 100 % | 171.4 px | 0.18 | 1.00 | 207 |
| stroke 12 | 100 % → 99 % | 118.8 px | 0.23 | 0.99 | 273 |
| stroke 13 | 100 % → 100 % | 127.7 px | 0.21 | 1.00 | 173 |
| stroke 14 | 99 % → 98 % | 124.4 px | 0.17 | 0.99 | 154 |
| stroke 15 | 100 % → 100 % | 130.5 px | 0.24 | 1.00 | 182 |

## Brush Artist · Refs · #13 Henry Ward blue streaky form — own sheet
own sheet 600 × 600 · Gouache · 50 px · 16.5 s

![Brush Artist · Refs · #13 Henry Ward blue streaky form — own sheet](Brush-Artist-Refs-13-Henry-Ward-blue-streaky-form-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 34 % → 64 % | 49.1 px | 0.10 | 1.86 | 218 |
| stroke 2 | 42 % → 66 % | 67.5 px | 0.10 | 1.58 | 223 |
| stroke 3 | 60 % → 86 % | 85.2 px | 0.10 | 1.43 | 248 |
| stroke 4 | 60 % → 89 % | 97.8 px | 0.10 | 1.49 | 191 |
| stroke 5 | 61 % → 86 % | 86.7 px | 0.10 | 1.42 | 228 |
| stroke 6 | 56 % → 82 % | 86.1 px | 0.10 | 1.47 | 219 |
| stroke 7 | 62 % → 85 % | 92.3 px | 0.10 | 1.38 | 217 |
| stroke 8 | 62 % → 85 % | 96.3 px | 0.10 | 1.37 | 206 |
| stroke 9 | 62 % → 87 % | 94.7 px | 0.10 | 1.41 | 293 |
| stroke 10 | 63 % → 89 % | 102.4 px | 0.10 | 1.40 | 291 |
| stroke 11 | 58 % → 86 % | 87.3 px | 0.10 | 1.48 | 214 |
| stroke 12 | 58 % → 82 % | 91.0 px | 0.10 | 1.42 | 255 |
| stroke 13 | 61 % → 88 % | 89.4 px | 0.10 | 1.44 | 212 |
| stroke 14 | 54 % → 82 % | 83.9 px | 0.10 | 1.53 | 289 |
| stroke 15 | 57 % → 83 % | 82.3 px | 0.10 | 1.45 | 228 |
| stroke 16 | 56 % → 84 % | 90.5 px | 0.10 | 1.51 | 272 |
| stroke 17 | 61 % → 84 % | 93.7 px | 0.10 | 1.39 | 228 |
| stroke 18 | 61 % → 82 % | 95.3 px | 0.10 | 1.35 | 248 |
| stroke 19 | 68 % → 80 % | 84.6 px | 0.10 | 1.18 | 237 |
| stroke 20 | 78 % → 77 % | 93.1 px | 0.10 | 0.99 | 255 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #14 Henry Ward olive totem — own sheet
own sheet 600 × 600 · Heavy acrylic · 48 px · 73.4 s

![Brush Artist · Refs · #14 Henry Ward olive totem — own sheet](Brush-Artist-Refs-14-Henry-Ward-olive-totem-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 95 % → 99 % | 63.2 px | 0.00 | 1.04 | 912 |
| stroke 2 | 97 % → 99 % | 89.9 px | 0.00 | 1.02 | 1006 |
| stroke 3 | 95 % → 99 % | 91.0 px | 0.00 | 1.04 | 1245 |
| stroke 4 | 97 % → 99 % | 91.7 px | 0.00 | 1.02 | 1114 |
| stroke 5 | 96 % → 99 % | 90.5 px | 0.00 | 1.03 | 1209 |
| stroke 6 | 97 % → 99 % | 94.0 px | 0.00 | 1.03 | 1191 |
| stroke 7 | 95 % → 99 % | 91.5 px | 0.00 | 1.04 | 1206 |
| stroke 8 | 94 % → 99 % | 91.1 px | 0.00 | 1.05 | 1165 |
| stroke 9 | 100 % → 99 % | 63.5 px | 0.00 | 0.99 | 1103 |
| stroke 10 | 100 % → 100 % | 149.5 px | 0.00 | 1.00 | 150 |
| stroke 11 | 100 % → 100 % | 177.2 px | 0.00 | 1.00 | 139 |
| stroke 12 | 100 % → 100 % | 148.8 px | 0.00 | 1.00 | 126 |
| stroke 13 | 100 % → 100 % | 175.3 px | 0.00 | 1.00 | 171 |
| stroke 14 | 100 % → 100 % | 148.6 px | 0.00 | 1.00 | 136 |
| stroke 15 | 100 % → 100 % | 179.4 px | 0.00 | 1.00 | 134 |
| stroke 16 | 100 % → 100 % | 143.9 px | 0.00 | 1.00 | 154 |
| stroke 17 | 100 % → 100 % | 178.3 px | 0.00 | 1.00 | 157 |
| stroke 18 | 100 % → 100 % | 148.3 px | 0.00 | 1.00 | 156 |
| stroke 19 | 100 % → 100 % | 170.4 px | 0.00 | 1.00 | 166 |
| stroke 20 | 100 % → 100 % | 157.2 px | 0.00 | 1.00 | 152 |
| stroke 21 | 100 % → 100 % | 172.2 px | 0.00 | 1.00 | 160 |
| stroke 22 | 100 % → 100 % | 149.6 px | 0.00 | 1.00 | 146 |
| stroke 23 | 100 % → 100 % | 168.6 px | 0.00 | 1.00 | 181 |
| stroke 24 | 100 % → 100 % | 146.5 px | 0.00 | 1.00 | 136 |
| stroke 25 | 100 % → 100 % | 165.6 px | 0.00 | 1.00 | 182 |
| stroke 26 | 100 % → 100 % | 145.4 px | 0.00 | 1.00 | 149 |
| stroke 27 | 100 % → 100 % | 176.6 px | 0.00 | 1.00 | 148 |
| stroke 28 | 100 % → 100 % | 153.0 px | 0.00 | 1.00 | 163 |
| stroke 29 | 100 % → 100 % | 174.5 px | 0.00 | 1.00 | 170 |
| stroke 30 | 100 % → 100 % | 161.6 px | 0.00 | 1.00 | 142 |
| stroke 31 | 100 % → 100 % | 155.5 px | 0.00 | 1.00 | 129 |

## Brush Artist · Refs · #15 Ultramarine brush script — own sheet
own sheet 600 × 600 · Ink · 10 px · 10.4 s

![Brush Artist · Refs · #15 Ultramarine brush script — own sheet](Brush-Artist-Refs-15-Ultramarine-brush-script-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 69 % → 72 % | 17.0 px | 0.70 | 1.05 | 84 |
| stroke 2 | 70 % → 72 % | 16.6 px | 0.69 | 1.04 | 96 |
| stroke 3 | 70 % → 74 % | 17.4 px | 0.69 | 1.05 | 71 |
| stroke 4 | 71 % → 72 % | 16.3 px | 0.66 | 1.01 | 166 |
| stroke 5 | 66 % → 69 % | 15.7 px | 0.67 | 1.04 | 94 |
| stroke 6 | 67 % → 71 % | 18.5 px | 0.70 | 1.05 | 45 |
| stroke 7 | 69 % → 71 % | 15.9 px | 0.67 | 1.04 | 108 |
| stroke 8 | 69 % → 71 % | 17.6 px | 0.70 | 1.02 | 62 |
| stroke 9 | 67 % → 70 % | 16.5 px | 0.68 | 1.05 | 87 |
| stroke 10 | 65 % → 69 % | 17.1 px | 0.69 | 1.05 | 78 |
| stroke 11 | 72 % → 75 % | 17.5 px | 0.69 | 1.04 | 70 |
| stroke 12 | 68 % → 69 % | 15.8 px | 0.67 | 1.01 | 133 |
| stroke 13 | 66 % → 69 % | 15.7 px | 0.67 | 1.04 | 113 |
| stroke 14 | 67 % → 71 % | 18.2 px | 0.70 | 1.05 | 49 |
| stroke 15 | 69 % → 73 % | 18.8 px | 0.71 | 1.05 | 63 |
| stroke 16 | 68 % → 72 % | 17.4 px | 0.70 | 1.04 | 80 |
| stroke 17 | 68 % → 69 % | 18.1 px | 0.70 | 1.02 | 58 |
| stroke 18 | 68 % → 71 % | 17.2 px | 0.70 | 1.05 | 77 |
| stroke 19 | 66 % → 71 % | 18.9 px | 0.71 | 1.07 | 62 |
| stroke 20 | 68 % → 72 % | 18.8 px | 0.71 | 1.06 | 64 |
| stroke 21 | 70 % → 73 % | 16.0 px | 0.67 | 1.03 | 105 |
| stroke 22 | 77 % → 79 % | 12.6 px | 0.70 | 1.02 | 123 |
| stroke 23 | 67 % → 71 % | 16.9 px | 0.70 | 1.05 | 83 |
| stroke 24 | 66 % → 69 % | 17.9 px | 0.71 | 1.05 | 71 |
| stroke 25 | 69 % → 72 % | 16.5 px | 0.68 | 1.04 | 92 |
| stroke 26 | 70 % → 71 % | 15.8 px | 0.66 | 1.01 | 121 |

## Brush Artist · Refs · #18 Blue oil-stick scribbles — own sheet
own sheet 600 × 600 · Pastel · 10 px · 3.2 s

![Brush Artist · Refs · #18 Blue oil-stick scribbles — own sheet](Brush-Artist-Refs-18-Blue-oil-stick-scribbles-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 18 % → 37 % | 3.8 px | 0.53 | 2.02 | 140 |
| stroke 2 | 16 % → 40 % | 3.6 px | 0.53 | 2.52 | 176 |
| stroke 3 | 18 % → 29 % | 5.8 px | 0.53 | 1.59 | 162 |
| stroke 4 | 17 % → 32 % | 7.8 px | 0.53 | 1.90 | 199 |
| stroke 5 | 32 % → 37 % | 7.8 px | 0.53 | 1.15 | 161 |
| stroke 6 | 30 % → 30 % | 9.2 px | 0.53 | 1.02 | 122 |
| stroke 7 | 28 % → 35 % | 7.5 px | 0.53 | 1.26 | 142 |
| stroke 8 | 33 % → 33 % | 16.3 px | 0.53 | 1.00 | 181 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #20 Orange-red crayon scribble — own sheet
own sheet 600 × 600 · Pastel · 14 px · 2.8 s

![Brush Artist · Refs · #20 Orange-red crayon scribble — own sheet](Brush-Artist-Refs-20-Orange-red-crayon-scribble-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 9 % → 20 % | 5.5 px | 0.53 | 2.30 | 197 |
| stroke 2 | 10 % → 25 % | 6.5 px | 0.53 | 2.49 | 162 |
| stroke 3 | 15 % → 25 % | 8.3 px | 0.53 | 1.61 | 146 |
| stroke 4 | 28 % → 35 % | 8.3 px | 0.53 | 1.25 | 187 |
| stroke 5 | 32 % → 32 % | 7.0 px | 0.53 | 1.00 | 147 |
| stroke 6 | 24 % → 24 % | 16.1 px | 0.53 | 1.00 | 172 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #21 Gritty black contours — own sheet
own sheet 600 × 600 · Gouache · 12 px · 64.1 s

![Brush Artist · Refs · #21 Gritty black contours — own sheet](Brush-Artist-Refs-21-Gritty-black-contours-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 100 % → 98 % | 30.0 px | 0.00 | 0.98 | 918 |
| stroke 2 | 100 % → 99 % | 35.3 px | 0.00 | 0.99 | 1210 |
| stroke 3 | 100 % → 99 % | 30.0 px | 0.00 | 0.99 | 1087 |
| stroke 4 | 100 % → 99 % | 31.8 px | 0.01 | 0.99 | 1196 |
| stroke 5 | 100 % → 98 % | 32.6 px | 0.03 | 0.98 | 1174 |
| stroke 6 | 100 % → 99 % | 34.4 px | 0.06 | 0.99 | 1054 |
| stroke 7 | 100 % → 99 % | 29.1 px | 0.03 | 0.99 | 1092 |
| stroke 8 | 100 % → 98 % | 34.4 px | 0.01 | 0.98 | 1032 |
| stroke 9 | 100 % → 99 % | 33.5 px | 0.00 | 0.99 | 945 |
| stroke 10 | 100 % → 100 % | 89.0 px | 0.07 | 1.00 | 181 |
| stroke 11 | 100 % → 100 % | 139.6 px | 0.04 | 1.00 | 215 |
| stroke 12 | 100 % → 100 % | 68.3 px | 0.07 | 1.00 | 143 |
| stroke 13 | 100 % → 100 % | 97.7 px | 0.07 | 1.00 | 156 |
| stroke 14 | 100 % → 100 % | 93.8 px | 0.06 | 1.00 | 98 |

## Brush Artist · Refs · #22 Bold black brush poster — own sheet
own sheet 600 × 600 · Ink · 20 px · 5.4 s

![Brush Artist · Refs · #22 Bold black brush poster — own sheet](Brush-Artist-Refs-22-Bold-black-brush-poster-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 34 % → 37 % | 36.3 px | 0.89 | 1.10 | 103 |
| stroke 2 | 55 % → 66 % | 36.9 px | 0.89 | 1.21 | 24 |
| stroke 3 | 49 % → 49 % | 40.5 px | 0.89 | 1.00 | 43 |
| stroke 4 | 36 % → 43 % | 45.3 px | 0.89 | 1.20 | 60 |
| stroke 5 | 35 % → 35 % | 40.5 px | 0.89 | 1.00 | 72 |

## Brush Artist · Refs · #23 Dry white on orange + black line — own sheet
own sheet 600 × 600 · Gouache · 50 px · 67.3 s

![Brush Artist · Refs · #23 Dry white on orange + black line — own sheet](Brush-Artist-Refs-23-Dry-white-on-orange-black-line-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 95 % → 99 % | 62.0 px | 0.00 | 1.04 | 942 |
| stroke 2 | 92 % → 99 % | 93.1 px | 0.00 | 1.08 | 1203 |
| stroke 3 | 93 % → 99 % | 93.3 px | 0.00 | 1.07 | 1181 |
| stroke 4 | 95 % → 99 % | 95.8 px | 0.00 | 1.04 | 1115 |
| stroke 5 | 92 % → 99 % | 93.3 px | 0.00 | 1.08 | 1090 |
| stroke 6 | 91 % → 99 % | 93.1 px | 0.00 | 1.09 | 1009 |
| stroke 7 | 92 % → 99 % | 92.8 px | 0.00 | 1.07 | 1129 |
| stroke 8 | 95 % → 99 % | 94.9 px | 0.00 | 1.04 | 1084 |
| stroke 9 | 100 % → 99 % | 65.3 px | 0.00 | 0.99 | 798 |
| stroke 10 | 100 % → 100 % | 167.5 px | 0.00 | 1.00 | 179 |
| stroke 11 | 100 % → 100 % | 173.3 px | 0.00 | 1.00 | 175 |
| stroke 12 | 100 % → 100 % | 162.3 px | 0.00 | 1.00 | 175 |
| stroke 13 | 100 % → 100 % | 183.6 px | 0.00 | 1.00 | 171 |
| stroke 14 | 100 % → 100 % | 154.9 px | 0.00 | 1.00 | 179 |
| stroke 15 | 100 % → 100 % | 190.8 px | 0.00 | 1.00 | 154 |
| stroke 16 | 100 % → 100 % | 169.8 px | 0.00 | 1.00 | 168 |
| stroke 17 | 100 % → 100 % | 180.0 px | 0.00 | 1.00 | 171 |
| stroke 18 | 100 % → 100 % | 163.5 px | 0.00 | 1.00 | 164 |
| stroke 19 | 100 % → 100 % | 178.5 px | 0.00 | 1.00 | 165 |
| stroke 20 | 100 % → 100 % | 164.4 px | 0.00 | 1.00 | 176 |
| stroke 21 | 100 % → 100 % | 180.5 px | 0.00 | 1.00 | 179 |
| stroke 22 | 100 % → 100 % | 161.8 px | 0.00 | 1.00 | 185 |
| stroke 23 | 100 % → 100 % | 185.9 px | 0.00 | 1.00 | 165 |
| stroke 24 | 100 % → 100 % | 161.8 px | 0.00 | 1.00 | 162 |
| stroke 25 | 100 % → 100 % | 185.5 px | 0.00 | 1.00 | 157 |
| stroke 26 | 100 % → 100 % | 165.8 px | 0.00 | 1.00 | 186 |
| stroke 27 | 100 % → 100 % | 185.6 px | 0.00 | 1.00 | 150 |

## Brush Artist · Refs · #24 Picasso flat oil — own sheet
own sheet 600 × 600 · Oil · 34 px · 67.2 s

![Brush Artist · Refs · #24 Picasso flat oil — own sheet](Brush-Artist-Refs-24-Picasso-flat-oil-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 100 % → 99 % | 54.7 px | 0.00 | 0.99 | 985 |
| stroke 2 | 100 % → 99 % | 67.9 px | 0.00 | 0.99 | 1071 |
| stroke 3 | 100 % → 99 % | 72.4 px | 0.01 | 0.99 | 1116 |
| stroke 4 | 100 % → 99 % | 71.5 px | 0.01 | 0.99 | 1097 |
| stroke 5 | 100 % → 99 % | 70.6 px | 0.01 | 0.99 | 1138 |
| stroke 6 | 100 % → 99 % | 67.9 px | 0.01 | 0.99 | 1124 |
| stroke 7 | 100 % → 99 % | 70.6 px | 0.01 | 0.99 | 1108 |
| stroke 8 | 100 % → 99 % | 70.6 px | 0.00 | 0.99 | 1300 |
| stroke 9 | 100 % → 99 % | 51.2 px | 0.00 | 0.99 | 979 |
| stroke 10 | 100 % → 100 % | 99.9 px | 0.00 | 1.00 | 137 |
| stroke 11 | 100 % → 100 % | 119.0 px | 0.01 | 1.00 | 186 |
| stroke 12 | 100 % → 100 % | 106.7 px | 0.01 | 1.00 | 148 |
| stroke 13 | 100 % → 100 % | 113.9 px | 0.01 | 1.00 | 148 |
| stroke 14 | 100 % → 100 % | 108.9 px | 0.01 | 1.00 | 159 |
| stroke 15 | 100 % → 100 % | 118.5 px | 0.01 | 1.00 | 138 |
| stroke 16 | 100 % → 100 % | 97.7 px | 0.01 | 1.00 | 150 |
| stroke 17 | 100 % → 100 % | 126.3 px | 0.01 | 1.00 | 145 |
| stroke 18 | 100 % → 100 % | 105.1 px | 0.01 | 1.00 | 135 |
| stroke 19 | 100 % → 100 % | 123.4 px | 0.01 | 1.00 | 145 |
| stroke 20 | 100 % → 100 % | 102.6 px | 0.01 | 1.00 | 135 |
| stroke 21 | 100 % → 100 % | 122.7 px | 0.01 | 1.00 | 133 |
| stroke 22 | 100 % → 100 % | 107.6 px | 0.01 | 1.00 | 149 |
| stroke 23 | 100 % → 100 % | 113.8 px | 0.01 | 1.00 | 145 |
| stroke 24 | 100 % → 100 % | 101.5 px | 0.01 | 1.00 | 139 |
| stroke 25 | 100 % → 100 % | 119.8 px | 0.01 | 1.00 | 139 |
| stroke 26 | 100 % → 100 % | 99.0 px | 0.01 | 1.00 | 147 |
| stroke 27 | 100 % → 100 % | 126.1 px | 0.01 | 1.00 | 144 |

## Brush Artist · Refs · #25 Yellow heavy flat stroke — own sheet
own sheet 600 × 600 · Heavy acrylic · 110 px · 2.9 s

![Brush Artist · Refs · #25 Yellow heavy flat stroke — own sheet](Brush-Artist-Refs-25-Yellow-heavy-flat-stroke-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 35 % → 35 % | 104.2 px | 0.17 | 0.98 | 683 |

## Brush Artist · Refs · #27 Orange impasto swatch — own sheet
own sheet 600 × 600 · Heavy acrylic · 60 px · 3.1 s

![Brush Artist · Refs · #27 Orange impasto swatch — own sheet](Brush-Artist-Refs-27-Orange-impasto-swatch-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 23 % → 29 % | 61.8 px | 0.37 | 1.29 | 89 |
| stroke 2 | 19 % → 40 % | 62.5 px | 0.37 | 2.07 | 44 |
| stroke 3 | 26 % → 38 % | 94.9 px | 0.37 | 1.48 | 35 |
| stroke 4 | 22 % → 22 % | 62.5 px | 0.36 | 0.96 | 63 |
| stroke 5 | 32 % → 41 % | 62.2 px | 0.36 | 1.28 | 61 |
| stroke 6 | 39 % → 40 % | 112.2 px | 0.36 | 1.02 | 64 |
| stroke 7 | 19 % → 21 % | 63.8 px | 0.36 | 1.11 | 51 |
| stroke 8 | 42 % → 40 % | 143.3 px | 0.36 | 0.97 | 39 |
| stroke 9 | 49 % → 48 % | 97.7 px | 0.37 | 0.97 | 68 |
| stroke 10 | 28 % → 27 % | 87.2 px | 0.36 | 0.96 | 53 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #28 Miles Davis black lines — own sheet
own sheet 600 × 600 · Ink · 22 px · 6.1 s

![Brush Artist · Refs · #28 Miles Davis black lines — own sheet](Brush-Artist-Refs-28-Miles-Davis-black-lines-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 29 % → 36 % | 36.4 px | 0.89 | 1.26 | 183 |
| stroke 2 | 37 % → 57 % | 36.0 px | 0.89 | 1.52 | 172 |
| stroke 3 | 47 % → 48 % | 66.3 px | 0.89 | 1.02 | 88 |
| stroke 4 | 49 % → 58 % | 76.4 px | 0.89 | 1.16 | 251 |
| stroke 5 | 63 % → 64 % | 95.0 px | 0.89 | 1.00 | 115 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #29 Shrigley magenta asterisk — own sheet
own sheet 600 × 600 · Watercolor · 70 px · 6.3 s

![Brush Artist · Refs · #29 Shrigley magenta asterisk — own sheet](Brush-Artist-Refs-29-Shrigley-magenta-asterisk-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 25 % → 44 % | 46.6 px | 0.45 | 1.76 | 196 |
| stroke 2 | 17 % → 17 % | 86.5 px | 0.43 | 1.00 | 198 |
| stroke 3 | 37 % → 43 % | 69.4 px | 0.45 | 1.17 | 200 |
| stroke 4 | 32 % → 33 % | 162.9 px | 0.43 | 1.02 | 270 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #30 Red gouache face patch — own sheet
own sheet 600 × 600 · Gouache · 60 px · 11.7 s

![Brush Artist · Refs · #30 Red gouache face patch — own sheet](Brush-Artist-Refs-30-Red-gouache-face-patch-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 27 % → 51 % | 51.5 px | 0.59 | 1.89 | 188 |
| stroke 2 | 33 % → 57 % | 74.5 px | 0.59 | 1.74 | 158 |
| stroke 3 | 50 % → 77 % | 99.1 px | 0.59 | 1.54 | 146 |
| stroke 4 | 50 % → 77 % | 110.7 px | 0.59 | 1.54 | 155 |
| stroke 5 | 49 % → 78 % | 97.1 px | 0.59 | 1.61 | 206 |
| stroke 6 | 50 % → 80 % | 112.2 px | 0.59 | 1.59 | 202 |
| stroke 7 | 51 % → 78 % | 101.2 px | 0.59 | 1.53 | 173 |
| stroke 8 | 49 % → 76 % | 103.7 px | 0.59 | 1.55 | 215 |
| stroke 9 | 52 % → 80 % | 104.6 px | 0.59 | 1.53 | 151 |
| stroke 10 | 54 % → 76 % | 123.0 px | 0.59 | 1.39 | 161 |
| stroke 11 | 52 % → 74 % | 107.4 px | 0.59 | 1.43 | 193 |
| stroke 12 | 50 % → 74 % | 109.1 px | 0.59 | 1.48 | 167 |
| stroke 13 | 45 % → 72 % | 87.5 px | 0.59 | 1.61 | 170 |
| stroke 14 | 45 % → 63 % | 95.7 px | 0.59 | 1.42 | 180 |
| stroke 15 | 48 % → 58 % | 92.1 px | 0.59 | 1.21 | 195 |
| stroke 16 | 55 % → 54 % | 122.4 px | 0.59 | 0.99 | 171 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #31 Warhol blotted line — own sheet
own sheet 600 × 600 · Ink · 6 px · 4.9 s

![Brush Artist · Refs · #31 Warhol blotted line — own sheet](Brush-Artist-Refs-31-Warhol-blotted-line-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 24 % → 47 % | 15.7 px | 0.83 | 1.93 | 84 |
| stroke 2 | 19 % → 24 % | 15.8 px | 0.83 | 1.27 | 67 |
| stroke 3 | 27 % → 27 % | 24.7 px | 0.82 | 1.02 | 69 |
| stroke 4 | 31 % → 41 % | 27.9 px | 0.83 | 1.32 | 47 |
| stroke 5 | 38 % → 46 % | 34.7 px | 0.83 | 1.22 | 91 |
| stroke 6 | 35 % → 36 % | 25.2 px | 0.82 | 1.03 | 70 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #32 Thick orange swipes — own sheet
own sheet 600 × 600 · Heavy acrylic · 90 px · 64.2 s

![Brush Artist · Refs · #32 Thick orange swipes — own sheet](Brush-Artist-Refs-32-Thick-orange-swipes-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 61 % → 99 % | 61.9 px | 0.00 | 1.62 | 914 |
| stroke 2 | 75 % → 99 % | 121.7 px | 0.02 | 1.32 | 1181 |
| stroke 3 | 75 % → 99 % | 127.8 px | 0.03 | 1.31 | 1127 |
| stroke 4 | 77 % → 99 % | 130.5 px | 0.05 | 1.29 | 1218 |
| stroke 5 | 77 % → 99 % | 129.5 px | 0.03 | 1.29 | 1255 |
| stroke 6 | 77 % → 99 % | 128.7 px | 0.04 | 1.29 | 1243 |
| stroke 7 | 76 % → 99 % | 128.8 px | 0.03 | 1.30 | 1170 |
| stroke 8 | 78 % → 99 % | 128.3 px | 0.03 | 1.26 | 1223 |
| stroke 9 | 100 % → 99 % | 104.1 px | 0.01 | 0.99 | 945 |
| stroke 10 | 100 % → 100 % | 308.3 px | 0.03 | 1.00 | 352 |
| stroke 11 | 100 % → 100 % | 313.1 px | 0.04 | 1.00 | 333 |
| stroke 12 | 100 % → 100 % | 318.4 px | 0.03 | 1.00 | 301 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #33 Red wet-in-wet band — own sheet
own sheet 600 × 600 · Watercolor · 80 px · 8.0 s

![Brush Artist · Refs · #33 Red wet-in-wet band — own sheet](Brush-Artist-Refs-33-Red-wet-in-wet-band-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 45 % → 63 % | 92.3 px | 0.34 | 1.38 | 470 |
| stroke 2 | 50 % → 63 % | 180.2 px | 0.37 | 1.28 | 106 |
| stroke 3 | 61 % → 74 % | 234.0 px | 0.37 | 1.22 | 119 |
| stroke 4 | 62 % → 71 % | 228.8 px | 0.35 | 1.15 | 109 |
| stroke 5 | 57 % → 70 % | 201.2 px | 0.37 | 1.22 | 122 |
| stroke 6 | 61 % → 61 % | 212.9 px | 0.36 | 1.00 | 113 |

## Brush Artist · Refs · #34 Magenta oil patches — own sheet
own sheet 600 × 600 · Oil · 60 px · 65.6 s

![Brush Artist · Refs · #34 Magenta oil patches — own sheet](Brush-Artist-Refs-34-Magenta-oil-patches-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 82 % → 99 % | 60.8 px | 0.00 | 1.20 | 979 |
| stroke 2 | 88 % → 99 % | 102.4 px | 0.00 | 1.13 | 1208 |
| stroke 3 | 88 % → 99 % | 101.5 px | 0.00 | 1.13 | 1171 |
| stroke 4 | 88 % → 99 % | 105.3 px | 0.00 | 1.12 | 1263 |
| stroke 5 | 89 % → 99 % | 102.3 px | 0.00 | 1.11 | 1212 |
| stroke 6 | 87 % → 99 % | 101.6 px | 0.00 | 1.15 | 1092 |
| stroke 7 | 86 % → 99 % | 101.9 px | 0.00 | 1.15 | 1252 |
| stroke 8 | 89 % → 99 % | 100.9 px | 0.00 | 1.11 | 1210 |
| stroke 9 | 100 % → 99 % | 74.1 px | 0.00 | 0.99 | 929 |
| stroke 10 | 100 % → 100 % | 260.1 px | 0.00 | 1.00 | 115 |
| stroke 11 | 100 % → 100 % | 282.9 px | 0.00 | 1.00 | 81 |
| stroke 12 | 100 % → 100 % | 290.5 px | 0.00 | 1.00 | 71 |
| stroke 13 | 100 % → 100 % | 313.2 px | 0.00 | 1.00 | 65 |
| stroke 14 | 99 % → 97 % | 222.6 px | 0.00 | 0.98 | 101 |
| stroke 15 | 100 % → 100 % | 293.1 px | 0.00 | 1.00 | 70 |
| stroke 16 | 100 % → 100 % | 282.1 px | 0.00 | 1.00 | 92 |
| stroke 17 | 100 % → 100 % | 258.1 px | 0.00 | 1.00 | 95 |
| stroke 18 | 100 % → 100 % | 255.0 px | 0.00 | 1.00 | 111 |
| stroke 19 | 100 % → 100 % | 316.2 px | 0.00 | 1.00 | 73 |
| stroke 20 | 100 % → 100 % | 305.9 px | 0.00 | 1.00 | 73 |
| stroke 21 | 100 % → 100 % | 294.2 px | 0.00 | 1.00 | 66 |

## Brush Artist · Refs · #35 Red band with runs — own sheet
own sheet 600 × 600 · Watercolor · 70 px · 4.8 s

![Brush Artist · Refs · #35 Red band with runs — own sheet](Brush-Artist-Refs-35-Red-band-with-runs-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 41 % → 39 % | 82.9 px | 0.27 | 0.95 | 357 |

## Brush Artist · Refs · #36 Magenta letters flat brush — own sheet
own sheet 600 × 600 · Gouache · 36 px · 11.4 s

![Brush Artist · Refs · #36 Magenta letters flat brush — own sheet](Brush-Artist-Refs-36-Magenta-letters-flat-brush-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 46 % → 46 % | 59.1 px | 0.50 | 1.00 | 41 |
| stroke 2 | 38 % → 48 % | 39.7 px | 0.50 | 1.25 | 31 |
| stroke 3 | 56 % → 63 % | 72.2 px | 0.50 | 1.12 | 46 |
| stroke 4 | 45 % → 53 % | 44.9 px | 0.50 | 1.19 | 158 |
| stroke 5 | 41 % → 52 % | 61.1 px | 0.50 | 1.29 | 76 |
| stroke 6 | 78 % → 76 % | 153.6 px | 0.50 | 0.97 | 17 |
| stroke 7 | 43 % → 50 % | 42.1 px | 0.50 | 1.15 | 120 |
| stroke 8 | 39 % → 59 % | 63.5 px | 0.50 | 1.52 | 56 |
| stroke 9 | 54 % → 53 % | 82.8 px | 0.50 | 0.98 | 43 |
| stroke 10 | 42 % → 61 % | 63.1 px | 0.50 | 1.44 | 84 |
| stroke 11 | 78 % → 77 % | 153.6 px | 0.50 | 0.98 | 19 |
| stroke 12 | 58 % → 68 % | 57.2 px | 0.50 | 1.17 | 147 |
| stroke 13 | 43 % → 50 % | 58.9 px | 0.50 | 1.18 | 36 |
| stroke 14 | 52 % → 73 % | 74.9 px | 0.50 | 1.40 | 37 |
| stroke 15 | 44 % → 52 % | 66.5 px | 0.50 | 1.18 | 95 |
| stroke 16 | 78 % → 76 % | 153.3 px | 0.50 | 0.98 | 20 |
| stroke 17 | 53 % → 61 % | 51.3 px | 0.50 | 1.15 | 137 |
| stroke 18 | 40 % → 47 % | 54.9 px | 0.50 | 1.17 | 48 |
| stroke 19 | 65 % → 63 % | 81.6 px | 0.50 | 0.97 | 26 |
| stroke 20 | 56 % → 54 % | 70.5 px | 0.50 | 0.97 | 30 |
| stroke 21 | 47 % → 46 % | 53.9 px | 0.50 | 0.96 | 76 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #37 Oil still life dabs — own sheet
own sheet 600 × 600 · Oil · 40 px · 65.4 s

![Brush Artist · Refs · #37 Oil still life dabs — own sheet](Brush-Artist-Refs-37-Oil-still-life-dabs-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 100 % → 99 % | 60.9 px | 0.00 | 0.99 | 1004 |
| stroke 2 | 100 % → 99 % | 81.2 px | 0.00 | 0.99 | 1186 |
| stroke 3 | 100 % → 99 % | 78.5 px | 0.00 | 0.99 | 1132 |
| stroke 4 | 100 % → 99 % | 82.9 px | 0.00 | 0.99 | 1317 |
| stroke 5 | 100 % → 99 % | 82.1 px | 0.00 | 0.99 | 1177 |
| stroke 6 | 100 % → 99 % | 80.3 px | 0.00 | 0.99 | 1222 |
| stroke 7 | 100 % → 99 % | 82.9 px | 0.00 | 0.99 | 1164 |
| stroke 8 | 100 % → 98 % | 82.1 px | 0.00 | 0.98 | 1205 |
| stroke 9 | 100 % → 99 % | 56.5 px | 0.00 | 0.99 | 928 |
| stroke 10 | 100 % → 100 % | 216.5 px | 0.00 | 1.00 | 28 |
| stroke 11 | 100 % → 100 % | 244.7 px | 0.00 | 1.00 | 28 |
| stroke 12 | 100 % → 100 % | 264.5 px | 0.00 | 1.00 | 19 |
| stroke 13 | 100 % → 100 % | 191.4 px | 0.00 | 1.00 | 42 |
| stroke 14 | 100 % → 100 % | 250.8 px | 0.00 | 1.00 | 29 |
| stroke 15 | 100 % → 100 % | 226.6 px | 0.00 | 1.00 | 27 |
| stroke 16 | 100 % → 100 % | 345.1 px | 0.00 | 1.00 | 13 |
| stroke 17 | 100 % → 100 % | 344.8 px | 0.00 | 1.00 | 21 |
| stroke 18 | 100 % → 100 % | 192.0 px | 0.00 | 1.00 | 41 |
| stroke 19 | 100 % → 100 % | 186.8 px | 0.00 | 1.00 | 43 |
| stroke 20 | 100 % → 100 % | 280.3 px | 0.00 | 1.00 | 21 |
| stroke 21 | 100 % → 100 % | 349.4 px | 0.00 | 1.00 | 17 |
| stroke 22 | 100 % → 100 % | 338.2 px | 0.00 | 1.00 | 11 |
| stroke 23 | 100 % → 100 % | 264.7 px | 0.00 | 1.00 | 19 |

## Brush Artist · Refs · #38 Sanguine drawing — own sheet
own sheet 600 × 600 · Pastel · 6 px · 2.2 s

![Brush Artist · Refs · #38 Sanguine drawing — own sheet](Brush-Artist-Refs-38-Sanguine-drawing-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 3 % → 14 % | 2.9 px | 0.61 | 4.35 | 6 |
| stroke 2 | 3 % → 7 % | 2.9 px | 0.61 | 2.23 | 3 |
| stroke 3 | 3 % → 9 % | 2.9 px | 0.61 | 2.76 | 3 |
| stroke 4 | 3 % → 19 % | 2.7 px | 0.61 | 6.27 | 4 |
| stroke 5 | 3 % → 8 % | 2.7 px | 0.61 | 2.71 | 3 |
| stroke 6 | 3 % → 20 % | 3.0 px | 0.61 | 6.20 | 8 |
| stroke 7 | 5 % → 15 % | 4.7 px | 0.61 | 2.84 | 3 |
| stroke 8 | 4 % → 15 % | 3.9 px | 0.61 | 3.43 | 4 |
| stroke 9 | 3 % → 7 % | 2.9 px | 0.61 | 2.30 | 6 |
| stroke 10 | 4 % → 17 % | 4.0 px | 0.61 | 3.83 | 3 |
| stroke 11 | 3 % → 5 % | 2.9 px | 0.61 | 1.49 | 6 |
| stroke 12 | 5 % → 16 % | 4.5 px | 0.61 | 3.20 | 9 |
| stroke 13 | 8 % → 18 % | 7.8 px | 0.61 | 2.10 | 7 |
| stroke 14 | 5 % → 15 % | 4.5 px | 0.62 | 2.96 | 10 |
| stroke 15 | 10 % → 18 % | 9.5 px | 0.61 | 1.71 | 5 |
| stroke 16 | 6 % → 16 % | 5.4 px | 0.61 | 2.74 | 7 |
| stroke 17 | 4 % → 9 % | 4.0 px | 0.61 | 2.07 | 4 |
| stroke 18 | 3 % → 5 % | 2.9 px | 0.61 | 1.68 | 6 |
| stroke 19 | 7 % → 17 % | 6.0 px | 0.61 | 2.63 | 5 |
| stroke 20 | 8 % → 15 % | 7.8 px | 0.61 | 1.72 | 4 |
| stroke 21 | 4 % → 4 % | 4.0 px | 0.61 | 1.00 | 8 |
| stroke 22 | 9 % → 14 % | 7.8 px | 0.62 | 1.66 | 7 |
| stroke 23 | 8 % → 12 % | 7.0 px | 0.61 | 1.52 | 4 |
| stroke 24 | 4 % → 7 % | 3.9 px | 0.61 | 1.55 | 7 |
| stroke 25 | 8 % → 15 % | 7.3 px | 0.61 | 1.86 | 4 |
| stroke 26 | 6 % → 8 % | 5.7 px | 0.61 | 1.26 | 7 |
| stroke 27 | 4 % → 4 % | 3.8 px | 0.61 | 1.05 | 4 |
| stroke 28 | 8 % → 12 % | 7.0 px | 0.61 | 1.56 | 6 |
| stroke 29 | 8 % → 17 % | 6.9 px | 0.61 | 2.22 | 4 |
| stroke 30 | 14 % → 18 % | 13.1 px | 0.61 | 1.25 | 3 |
| stroke 31 | 6 % → 7 % | 5.2 px | 0.61 | 1.23 | 5 |
| stroke 32 | 12 % → 13 % | 10.5 px | 0.61 | 1.15 | 10 |
| stroke 33 | 7 % → 8 % | 6.6 px | 0.61 | 1.06 | 3 |
| stroke 34 | 11 % → 14 % | 10.2 px | 0.61 | 1.28 | 3 |
| stroke 35 | 9 % → 15 % | 8.6 px | 0.61 | 1.56 | 4 |
| stroke 36 | 11 % → 13 % | 9.8 px | 0.61 | 1.27 | 4 |
| stroke 37 | 11 % → 17 % | 9.8 px | 0.61 | 1.64 | 4 |
| stroke 38 | 14 % → 21 % | 12.4 px | 0.61 | 1.51 | 3 |
| stroke 39 | 15 % → 18 % | 13.6 px | 0.61 | 1.22 | 7 |
| stroke 40 | 6 % → 7 % | 5.3 px | 0.61 | 1.16 | 9 |
| stroke 41 | 17 % → 17 % | 15.3 px | 0.61 | 1.00 | 7 |
| stroke 42 | 14 % → 16 % | 12.6 px | 0.61 | 1.16 | 9 |
| stroke 43 | 11 % → 13 % | 10.0 px | 0.61 | 1.18 | 5 |
| stroke 44 | 13 % → 16 % | 11.6 px | 0.61 | 1.23 | 3 |
| stroke 45 | 3 % → 3 % | 2.6 px | 0.61 | 1.00 | 7 |
| stroke 46 | 17 % → 17 % | 15.6 px | 0.61 | 1.00 | 5 |
| stroke 47 | 14 % → 14 % | 13.1 px | 0.61 | 1.00 | 3 |
| stroke 48 | 13 % → 14 % | 12.4 px | 0.62 | 1.04 | 9 |
| stroke 49 | 20 % → 20 % | 18.3 px | 0.61 | 1.00 | 9 |
| stroke 50 | 10 % → 10 % | 9.5 px | 0.61 | 1.00 | 4 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #39 Very thick impasto — own sheet
own sheet 600 × 600 · Heavy acrylic · 60 px · 64.4 s

![Brush Artist · Refs · #39 Very thick impasto — own sheet](Brush-Artist-Refs-39-Very-thick-impasto-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 76 % → 99 % | 56.5 px | 0.22 | 1.30 | 824 |
| stroke 2 | 89 % → 99 % | 104.1 px | 0.18 | 1.12 | 1169 |
| stroke 3 | 89 % → 99 % | 101.8 px | 0.19 | 1.12 | 1326 |
| stroke 4 | 87 % → 99 % | 101.2 px | 0.29 | 1.14 | 1043 |
| stroke 5 | 87 % → 99 % | 102.6 px | 0.17 | 1.13 | 1296 |
| stroke 6 | 86 % → 99 % | 102.2 px | 0.21 | 1.14 | 1130 |
| stroke 7 | 88 % → 99 % | 101.6 px | 0.22 | 1.13 | 1281 |
| stroke 8 | 86 % → 99 % | 101.5 px | 0.17 | 1.14 | 1144 |
| stroke 9 | 100 % → 99 % | 75.0 px | 0.16 | 0.99 | 833 |
| stroke 10 | 100 % → 99 % | 156.7 px | 0.18 | 0.99 | 315 |
| stroke 11 | 100 % → 99 % | 162.6 px | 0.20 | 0.99 | 392 |
| stroke 12 | 100 % → 99 % | 180.2 px | 0.19 | 0.99 | 286 |
| stroke 13 | 100 % → 99 % | 153.1 px | 0.18 | 0.99 | 308 |
| stroke 14 | 100 % → 99 % | 168.5 px | 0.16 | 0.99 | 307 |

## Brush Artist · Refs · #40 Watercolour blooms — own sheet
own sheet 600 × 600 · Watercolor · 90 px · 6.1 s

![Brush Artist · Refs · #40 Watercolour blooms — own sheet](Brush-Artist-Refs-40-Watercolour-blooms-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 39 % → 39 % | 94.2 px | 0.26 | 1.00 | 858 |

## Brush Artist · Refs · #41 Coloured pencil hatching — own sheet
own sheet 600 × 600 · Pastel · 4 px · 64.6 s

![Brush Artist · Refs · #41 Coloured pencil hatching — own sheet](Brush-Artist-Refs-41-Coloured-pencil-hatching-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 100 % → 97 % | 18.5 px | 0.00 | 0.97 | 952 |
| stroke 2 | 100 % → 98 % | 19.4 px | 0.01 | 0.98 | 1327 |
| stroke 3 | 100 % → 98 % | 15.0 px | 0.02 | 0.98 | 1190 |
| stroke 4 | 100 % → 98 % | 17.6 px | 0.01 | 0.98 | 1278 |
| stroke 5 | 100 % → 97 % | 18.5 px | 0.02 | 0.97 | 1146 |
| stroke 6 | 100 % → 98 % | 18.5 px | 0.03 | 0.98 | 1231 |
| stroke 7 | 100 % → 98 % | 15.9 px | 0.03 | 0.98 | 1125 |
| stroke 8 | 100 % → 98 % | 21.2 px | 0.02 | 0.98 | 1107 |
| stroke 9 | 100 % → 97 % | 15.9 px | 0.00 | 0.97 | 840 |
| stroke 10 | 100 % → 100 % | 63.9 px | 0.04 | 1.00 | 6 |
| stroke 11 | 100 % → 100 % | 62.9 px | 0.02 | 1.00 | 6 |
| stroke 12 | 100 % → 100 % | 63.9 px | 0.03 | 1.00 | 4 |
| stroke 13 | 100 % → 100 % | 64.0 px | 0.06 | 1.00 | 7 |
| stroke 14 | 100 % → 100 % | 63.9 px | 0.02 | 1.00 | 3 |
| stroke 15 | 100 % → 100 % | 62.9 px | 0.04 | 1.00 | 7 |
| stroke 16 | 100 % → 100 % | 62.8 px | 0.05 | 1.00 | 6 |
| stroke 17 | 100 % → 100 % | 62.9 px | 0.04 | 1.00 | 4 |
| stroke 18 | 100 % → 100 % | 62.4 px | 0.04 | 1.00 | 3 |
| stroke 19 | 100 % → 100 % | 63.5 px | 0.05 | 1.00 | 5 |
| stroke 20 | 100 % → 100 % | 64.0 px | 0.04 | 1.00 | 8 |
| stroke 21 | 100 % → 100 % | 62.9 px | 0.01 | 1.00 | 6 |
| stroke 22 | 100 % → 100 % | 62.9 px | 0.05 | 1.00 | 3 |
| stroke 23 | 100 % → 100 % | 63.9 px | 0.05 | 1.00 | 3 |
| stroke 24 | 100 % → 100 % | 62.9 px | 0.04 | 1.00 | 6 |
| stroke 25 | 100 % → 100 % | 62.9 px | 0.03 | 1.00 | 4 |
| stroke 26 | 100 % → 100 % | 64.0 px | 0.01 | 1.00 | 5 |
| stroke 27 | 100 % → 100 % | 64.0 px | 0.03 | 1.00 | 6 |
| stroke 28 | 100 % → 100 % | 64.0 px | 0.04 | 1.00 | 6 |
| stroke 29 | 100 % → 100 % | 63.9 px | 0.05 | 1.00 | 7 |
| stroke 30 | 100 % → 100 % | 63.9 px | 0.05 | 1.00 | 5 |
| stroke 31 | 100 % → 100 % | 64.0 px | 0.05 | 1.00 | 4 |
| stroke 32 | 100 % → 100 % | 62.9 px | 0.04 | 1.00 | 6 |
| stroke 33 | 100 % → 100 % | 62.5 px | 0.05 | 1.00 | 3 |
| stroke 34 | 100 % → 100 % | 63.9 px | 0.03 | 1.00 | 7 |
| stroke 35 | 100 % → 100 % | 64.0 px | 0.02 | 1.00 | 4 |
| stroke 36 | 100 % → 100 % | 63.4 px | 0.02 | 1.00 | 3 |
| stroke 37 | 100 % → 100 % | 64.0 px | 0.03 | 1.00 | 3 |
| stroke 38 | 100 % → 100 % | 62.4 px | 0.04 | 1.00 | 4 |
| stroke 39 | 100 % → 100 % | 62.9 px | 0.03 | 1.00 | 3 |
| stroke 40 | 100 % → 100 % | 64.0 px | 0.05 | 1.00 | 6 |
| stroke 41 | 100 % → 100 % | 63.9 px | 0.02 | 1.00 | 5 |
| stroke 42 | 100 % → 100 % | 64.0 px | 0.04 | 1.00 | 6 |
| stroke 43 | 100 % → 100 % | 64.0 px | 0.02 | 1.00 | 3 |
| stroke 44 | 100 % → 100 % | 63.9 px | 0.04 | 1.00 | 6 |
| stroke 45 | 100 % → 100 % | 62.9 px | 0.02 | 1.00 | 4 |
| stroke 46 | 100 % → 100 % | 62.8 px | 0.05 | 1.00 | 3 |
| stroke 47 | 100 % → 100 % | 63.8 px | 0.04 | 1.00 | 4 |
| stroke 48 | 100 % → 100 % | 64.0 px | 0.04 | 1.00 | 7 |
| stroke 49 | 100 % → 100 % | 62.8 px | 0.06 | 1.00 | 6 |
| stroke 50 | 100 % → 100 % | 62.8 px | 0.04 | 1.00 | 8 |
| stroke 51 | 100 % → 100 % | 63.5 px | 0.06 | 1.00 | 3 |
| stroke 52 | 100 % → 100 % | 62.8 px | 0.03 | 1.00 | 6 |
| stroke 53 | 100 % → 100 % | 63.9 px | 0.05 | 1.00 | 5 |
| stroke 54 | 100 % → 100 % | 63.4 px | 0.06 | 1.00 | 3 |
| stroke 55 | 100 % → 100 % | 62.9 px | 0.02 | 1.00 | 6 |
| stroke 56 | 100 % → 100 % | 62.9 px | 0.04 | 1.00 | 6 |
| stroke 57 | 100 % → 100 % | 62.9 px | 0.06 | 1.00 | 5 |
| stroke 58 | 100 % → 100 % | 63.9 px | 0.03 | 1.00 | 7 |
| stroke 59 | 100 % → 100 % | 62.9 px | 0.02 | 1.00 | 5 |
| stroke 60 | 100 % → 100 % | 62.9 px | 0.05 | 1.00 | 7 |
| stroke 61 | 100 % → 100 % | 64.0 px | 0.05 | 1.00 | 4 |
| stroke 62 | 100 % → 100 % | 62.9 px | 0.05 | 1.00 | 7 |
| stroke 63 | 100 % → 100 % | 63.9 px | 0.05 | 1.00 | 3 |
| stroke 64 | 100 % → 100 % | 64.0 px | 0.04 | 1.00 | 7 |
| stroke 65 | 100 % → 100 % | 64.0 px | 0.04 | 1.00 | 3 |
| stroke 66 | 100 % → 100 % | 62.9 px | 0.04 | 1.00 | 4 |
| stroke 67 | 100 % → 100 % | 64.0 px | 0.04 | 1.00 | 4 |
| stroke 68 | 100 % → 100 % | 62.4 px | 0.04 | 1.00 | 3 |
| stroke 69 | 100 % → 100 % | 63.0 px | 0.06 | 1.00 | 7 |
| stroke 70 | 100 % → 100 % | 62.8 px | 0.07 | 1.00 | 3 |
| stroke 71 | 100 % → 100 % | 63.9 px | 0.03 | 1.00 | 3 |
| stroke 72 | 100 % → 100 % | 64.0 px | 0.04 | 1.00 | 7 |
| stroke 73 | 100 % → 100 % | 62.9 px | 0.05 | 1.00 | 4 |
| stroke 74 | 100 % → 100 % | 63.8 px | 0.05 | 1.00 | 3 |
| stroke 75 | 100 % → 100 % | 64.0 px | 0.04 | 1.00 | 3 |
| stroke 76 | 100 % → 100 % | 62.9 px | 0.04 | 1.00 | 5 |
| stroke 77 | 100 % → 100 % | 63.9 px | 0.03 | 1.00 | 7 |
| stroke 78 | 100 % → 100 % | 62.8 px | 0.02 | 1.00 | 7 |
| stroke 79 | 100 % → 100 % | 62.9 px | 0.04 | 1.00 | 3 |
| stroke 80 | 100 % → 100 % | 62.9 px | 0.04 | 1.00 | 5 |
| stroke 81 | 100 % → 100 % | 64.0 px | 0.02 | 1.00 | 3 |
| stroke 82 | 100 % → 100 % | 63.9 px | 0.04 | 1.00 | 7 |
| stroke 83 | 100 % → 100 % | 62.4 px | 0.05 | 1.00 | 4 |
| stroke 84 | 100 % → 100 % | 62.4 px | 0.05 | 1.00 | 40 |
| stroke 85 | 100 % → 100 % | 62.8 px | 0.05 | 1.00 | 10 |
| stroke 86 | 100 % → 100 % | 62.9 px | 0.03 | 1.00 | 8 |
| stroke 87 | 100 % → 100 % | 63.9 px | 0.03 | 1.00 | 15 |
| stroke 88 | 100 % → 100 % | 62.9 px | 0.02 | 1.00 | 4 |
| stroke 89 | 100 % → 100 % | 63.5 px | 0.04 | 1.00 | 5 |

## Brush Artist · Refs · #42 Oil pastel shaggy — own sheet
own sheet 600 × 600 · Pastel · 18 px · 61.6 s

![Brush Artist · Refs · #42 Oil pastel shaggy — own sheet](Brush-Artist-Refs-42-Oil-pastel-shaggy-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 100 % → 98 % | 37.1 px | 0.00 | 0.98 | 902 |
| stroke 2 | 100 % → 99 % | 42.4 px | 0.00 | 0.99 | 1153 |
| stroke 3 | 100 % → 99 % | 39.7 px | 0.00 | 0.99 | 1224 |
| stroke 4 | 100 % → 99 % | 45.0 px | 0.00 | 0.99 | 1045 |
| stroke 5 | 100 % → 98 % | 40.6 px | 0.00 | 0.98 | 1000 |
| stroke 6 | 100 % → 99 % | 43.2 px | 0.00 | 0.99 | 1034 |
| stroke 7 | 100 % → 99 % | 43.2 px | 0.00 | 0.99 | 965 |
| stroke 8 | 100 % → 98 % | 44.1 px | 0.00 | 0.98 | 1011 |
| stroke 9 | 100 % → 99 % | 42.4 px | 0.00 | 0.99 | 884 |
| stroke 10 | 100 % → 100 % | 88.3 px | 0.00 | 1.00 | 8 |
| stroke 11 | 100 % → 100 % | 86.4 px | 0.00 | 1.00 | 14 |
| stroke 12 | 100 % → 100 % | 87.7 px | 0.00 | 1.00 | 11 |
| stroke 13 | 100 % → 100 % | 87.7 px | 0.00 | 1.00 | 10 |
| stroke 14 | 100 % → 100 % | 86.3 px | 0.00 | 1.00 | 16 |
| stroke 15 | 100 % → 100 % | 87.7 px | 0.00 | 1.00 | 7 |
| stroke 16 | 100 % → 100 % | 87.7 px | 0.00 | 1.00 | 6 |
| stroke 17 | 100 % → 100 % | 86.3 px | 0.00 | 1.00 | 12 |
| stroke 18 | 100 % → 100 % | 87.6 px | 0.00 | 1.00 | 8 |
| stroke 19 | 100 % → 100 % | 87.0 px | 0.00 | 1.00 | 7 |
| stroke 20 | 100 % → 100 % | 88.3 px | 0.00 | 1.00 | 9 |
| stroke 21 | 100 % → 100 % | 86.4 px | 0.00 | 1.00 | 10 |
| stroke 22 | 100 % → 100 % | 87.7 px | 0.00 | 1.00 | 9 |
| stroke 23 | 100 % → 100 % | 88.1 px | 0.00 | 1.00 | 6 |
| stroke 24 | 100 % → 100 % | 86.2 px | 0.00 | 1.00 | 7 |
| stroke 25 | 100 % → 100 % | 87.7 px | 0.00 | 1.00 | 16 |
| stroke 26 | 100 % → 100 % | 86.9 px | 0.00 | 1.00 | 8 |
| stroke 27 | 100 % → 100 % | 87.6 px | 0.00 | 1.00 | 11 |
| stroke 28 | 100 % → 100 % | 86.3 px | 0.00 | 1.00 | 13 |
| stroke 29 | 100 % → 100 % | 86.4 px | 0.00 | 1.00 | 6 |
| stroke 30 | 100 % → 100 % | 88.3 px | 0.00 | 1.00 | 6 |
| stroke 31 | 100 % → 100 % | 87.7 px | 0.00 | 1.00 | 19 |
| stroke 32 | 100 % → 100 % | 86.9 px | 0.00 | 1.00 | 11 |
| stroke 33 | 100 % → 100 % | 87.6 px | 0.00 | 1.00 | 14 |
| stroke 34 | 100 % → 100 % | 86.9 px | 0.00 | 1.00 | 8 |
| stroke 35 | 100 % → 100 % | 86.4 px | 0.00 | 1.00 | 12 |
| stroke 36 | 100 % → 100 % | 87.7 px | 0.00 | 1.00 | 11 |
| stroke 37 | 100 % → 100 % | 88.1 px | 0.00 | 1.00 | 7 |
| stroke 38 | 100 % → 100 % | 87.5 px | 0.00 | 1.00 | 14 |
| stroke 39 | 100 % → 100 % | 87.5 px | 0.00 | 1.00 | 7 |
| stroke 40 | 100 % → 100 % | 88.3 px | 0.00 | 1.00 | 11 |
| stroke 41 | 100 % → 100 % | 87.8 px | 0.00 | 1.00 | 6 |
| stroke 42 | 100 % → 100 % | 86.2 px | 0.00 | 1.00 | 17 |
| stroke 43 | 100 % → 100 % | 86.4 px | 0.00 | 1.00 | 7 |
| stroke 44 | 100 % → 100 % | 86.4 px | 0.00 | 1.00 | 9 |
| stroke 45 | 100 % → 100 % | 86.4 px | 0.00 | 1.00 | 18 |
| stroke 46 | 100 % → 100 % | 86.2 px | 0.00 | 1.00 | 10 |
| stroke 47 | 100 % → 100 % | 86.3 px | 0.00 | 1.00 | 15 |
| stroke 48 | 100 % → 100 % | 87.8 px | 0.00 | 1.00 | 12 |
| stroke 49 | 100 % → 100 % | 86.3 px | 0.00 | 1.00 | 21 |
| stroke 50 | 100 % → 100 % | 87.6 px | 0.00 | 1.00 | 11 |
| stroke 51 | 100 % → 100 % | 87.7 px | 0.00 | 1.00 | 9 |
| stroke 52 | 100 % → 100 % | 87.6 px | 0.00 | 1.00 | 12 |
| stroke 53 | 100 % → 100 % | 86.8 px | 0.00 | 1.00 | 13 |
| stroke 54 | 100 % → 100 % | 86.3 px | 0.00 | 1.00 | 16 |
| stroke 55 | 100 % → 100 % | 86.4 px | 0.00 | 1.00 | 18 |
| stroke 56 | 100 % → 100 % | 86.4 px | 0.00 | 1.00 | 14 |
| stroke 57 | 100 % → 100 % | 88.2 px | 0.00 | 1.00 | 14 |
| stroke 58 | 100 % → 100 % | 86.4 px | 0.00 | 1.00 | 19 |
| stroke 59 | 100 % → 100 % | 87.7 px | 0.00 | 1.00 | 11 |
| stroke 60 | 100 % → 100 % | 88.3 px | 0.00 | 1.00 | 17 |
| stroke 61 | 100 % → 100 % | 87.7 px | 0.00 | 1.00 | 16 |
| stroke 62 | 100 % → 100 % | 86.3 px | 0.00 | 1.00 | 17 |
| stroke 63 | 100 % → 100 % | 87.8 px | 0.00 | 1.00 | 17 |
| stroke 64 | 100 % → 100 % | 86.3 px | 0.00 | 1.00 | 19 |
| stroke 65 | 100 % → 100 % | 86.4 px | 0.00 | 1.00 | 7 |
| stroke 66 | 100 % → 100 % | 86.7 px | 0.00 | 1.00 | 9 |
| stroke 67 | 100 % → 100 % | 86.8 px | 0.00 | 1.00 | 15 |
| stroke 68 | 100 % → 100 % | 87.6 px | 0.00 | 1.00 | 10 |
| stroke 69 | 100 % → 100 % | 86.4 px | 0.00 | 1.00 | 16 |

## Brush Artist · Refs · #43 Dragged black ink blocks — own sheet
own sheet 600 × 600 · Gouache · 70 px · 62.8 s

![Brush Artist · Refs · #43 Dragged black ink blocks — own sheet](Brush-Artist-Refs-43-Dragged-black-ink-blocks-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 69 % → 99 % | 57.4 px | 0.28 | 1.42 | 829 |
| stroke 2 | 84 % → 99 % | 111.1 px | 0.20 | 1.18 | 1251 |
| stroke 3 | 83 % → 99 % | 110.2 px | 0.18 | 1.20 | 1248 |
| stroke 4 | 84 % → 99 % | 109.9 px | 0.28 | 1.18 | 1087 |
| stroke 5 | 83 % → 99 % | 109.7 px | 0.19 | 1.19 | 1075 |
| stroke 6 | 83 % → 99 % | 110.0 px | 0.28 | 1.19 | 1001 |
| stroke 7 | 83 % → 99 % | 111.6 px | 0.19 | 1.20 | 960 |
| stroke 8 | 84 % → 99 % | 112.6 px | 0.19 | 1.18 | 1042 |
| stroke 9 | 100 % → 99 % | 82.9 px | 0.30 | 0.99 | 773 |
| stroke 10 | 100 % → 99 % | 145.1 px | 0.22 | 0.99 | 452 |
| stroke 11 | 100 % → 99 % | 189.4 px | 0.17 | 1.00 | 703 |
| stroke 12 | 100 % → 99 % | 188.6 px | 0.19 | 0.99 | 634 |
| stroke 13 | 100 % → 99 % | 182.4 px | 0.18 | 0.99 | 547 |
| stroke 14 | 100 % → 99 % | 153.0 px | 0.21 | 0.99 | 662 |

## Brush Artist · Refs · #44 Blue looping ribbon — own sheet
own sheet 600 × 600 · Oil · 80 px · 5.3 s

![Brush Artist · Refs · #44 Blue looping ribbon — own sheet](Brush-Artist-Refs-44-Blue-looping-ribbon-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 48 % → 48 % | 42.2 px | 0.73 | 1.00 | 2359 |

## Brush Artist · Refs · #45 Soft pastel pepper — own sheet
own sheet 600 × 600 · Pastel · 40 px · 3.0 s

![Brush Artist · Refs · #45 Soft pastel pepper — own sheet](Brush-Artist-Refs-45-Soft-pastel-pepper-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 15 % → 33 % | 11.3 px | 0.54 | 2.20 | 315 |
| stroke 2 | 25 % → 37 % | 20.6 px | 0.54 | 1.47 | 298 |
| stroke 3 | 34 % → 42 % | 13.8 px | 0.54 | 1.25 | 260 |
| stroke 4 | 32 % → 36 % | 27.8 px | 0.54 | 1.13 | 282 |
| stroke 5 | 37 % → 37 % | 13.9 px | 0.54 | 1.00 | 194 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #46 Red-brown ink lips — own sheet
own sheet 600 × 600 · Watercolor · 70 px · 4.5 s

![Brush Artist · Refs · #46 Red-brown ink lips — own sheet](Brush-Artist-Refs-46-Red-brown-ink-lips-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 30 % → 43 % | 78.1 px | 0.54 | 1.42 | 210 |
| stroke 2 | 45 % → 45 % | 119.4 px | 0.53 | 1.00 | 181 |

## Brush Artist · Refs · #47 Pink knife slabs — own sheet
own sheet 600 × 600 · Heavy acrylic · 90 px · 51.3 s

![Brush Artist · Refs · #47 Pink knife slabs — own sheet](Brush-Artist-Refs-47-Pink-knife-slabs-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 60 % → 99 % | 60.5 px | 0.00 | 1.64 | 784 |
| stroke 2 | 75 % → 99 % | 122.8 px | 0.02 | 1.32 | 962 |
| stroke 3 | 75 % → 99 % | 128.2 px | 0.03 | 1.32 | 988 |
| stroke 4 | 76 % → 99 % | 129.6 px | 0.03 | 1.30 | 995 |
| stroke 5 | 76 % → 99 % | 128.8 px | 0.03 | 1.29 | 932 |
| stroke 6 | 76 % → 99 % | 128.2 px | 0.03 | 1.31 | 948 |
| stroke 7 | 75 % → 99 % | 128.1 px | 0.04 | 1.32 | 959 |
| stroke 8 | 81 % → 99 % | 131.1 px | 0.02 | 1.22 | 978 |
| stroke 9 | 100 % → 98 % | 104.1 px | 0.03 | 0.98 | 821 |
| stroke 10 | 100 % → 100 % | 292.2 px | 0.02 | 1.00 | 232 |
| stroke 11 | 100 % → 100 % | 292.0 px | 0.03 | 1.00 | 238 |
| stroke 12 | 100 % → 99 % | 292.0 px | 0.03 | 0.99 | 246 |
| stroke 13 | 100 % → 99 % | 284.5 px | 0.02 | 0.99 | 225 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #48 Black bands with drips — own sheet
own sheet 600 × 600 · Gouache · 70 px · 47.6 s

![Brush Artist · Refs · #48 Black bands with drips — own sheet](Brush-Artist-Refs-48-Black-bands-with-drips-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 72 % → 99 % | 61.7 px | 0.11 | 1.37 | 885 |
| stroke 2 | 84 % → 99 % | 113.0 px | 0.12 | 1.18 | 932 |
| stroke 3 | 82 % → 99 % | 110.6 px | 0.18 | 1.21 | 986 |
| stroke 4 | 83 % → 99 % | 109.7 px | 0.13 | 1.18 | 987 |
| stroke 5 | 83 % → 99 % | 111.5 px | 0.17 | 1.20 | 978 |
| stroke 6 | 82 % → 99 % | 110.3 px | 0.12 | 1.20 | 1169 |
| stroke 7 | 81 % → 99 % | 110.6 px | 0.13 | 1.21 | 1114 |
| stroke 8 | 82 % → 98 % | 111.1 px | 0.12 | 1.20 | 1333 |
| stroke 9 | 100 % → 99 % | 83.8 px | 0.01 | 0.99 | 1002 |
| stroke 10 | 100 % → 99 % | 177.4 px | 0.11 | 0.99 | 325 |
| stroke 11 | 100 % → 99 % | 166.7 px | 0.12 | 0.99 | 322 |
| stroke 12 | 100 % → 99 % | 175.1 px | 0.11 | 0.99 | 334 |
| stroke 13 | 100 % → 99 % | 174.8 px | 0.11 | 0.99 | 320 |

## Brush Artist · Refs · #49 Magenta letters round brush — own sheet
own sheet 600 × 600 · Ink · 30 px · 9.9 s

![Brush Artist · Refs · #49 Magenta letters round brush — own sheet](Brush-Artist-Refs-49-Magenta-letters-round-brush-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 61 % → 65 % | 64.3 px | 0.52 | 1.06 | 28 |
| stroke 2 | 59 % → 63 % | 52.0 px | 0.53 | 1.07 | 34 |
| stroke 3 | 71 % → 80 % | 74.2 px | 0.53 | 1.13 | 29 |
| stroke 4 | 54 % → 64 % | 48.0 px | 0.52 | 1.18 | 106 |
| stroke 5 | 48 % → 65 % | 63.0 px | 0.52 | 1.35 | 66 |
| stroke 6 | 93 % → 94 % | 141.0 px | 0.53 | 1.01 | 16 |
| stroke 7 | 61 % → 70 % | 51.9 px | 0.52 | 1.14 | 114 |
| stroke 8 | 44 % → 72 % | 63.4 px | 0.53 | 1.61 | 71 |
| stroke 9 | 71 % → 71 % | 86.0 px | 0.53 | 1.00 | 29 |
| stroke 10 | 51 % → 72 % | 66.5 px | 0.52 | 1.42 | 80 |
| stroke 11 | 93 % → 94 % | 140.9 px | 0.53 | 1.01 | 17 |
| stroke 12 | 71 % → 83 % | 60.6 px | 0.52 | 1.18 | 112 |
| stroke 13 | 61 % → 65 % | 67.4 px | 0.53 | 1.05 | 35 |
| stroke 14 | 69 % → 92 % | 78.6 px | 0.53 | 1.33 | 73 |
| stroke 15 | 52 % → 63 % | 68.8 px | 0.52 | 1.20 | 112 |
| stroke 16 | 93 % → 93 % | 140.9 px | 0.53 | 1.00 | 13 |
| stroke 17 | 68 % → 76 % | 58.1 px | 0.52 | 1.12 | 106 |
| stroke 18 | 59 % → 62 % | 64.6 px | 0.52 | 1.05 | 32 |
| stroke 19 | 81 % → 80 % | 82.3 px | 0.53 | 0.99 | 42 |
| stroke 20 | 71 % → 70 % | 72.0 px | 0.52 | 1.00 | 30 |
| stroke 21 | 59 % → 59 % | 61.0 px | 0.52 | 1.00 | 104 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #50 Thick swipes on photo — own sheet
own sheet 600 × 600 · Heavy acrylic · 40 px · 43.4 s

![Brush Artist · Refs · #50 Thick swipes on photo — own sheet](Brush-Artist-Refs-50-Thick-swipes-on-photo-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 100 % → 99 % | 56.5 px | 0.00 | 0.99 | 850 |
| stroke 2 | 100 % → 99 % | 82.9 px | 0.00 | 0.99 | 1435 |
| stroke 3 | 100 % → 99 % | 83.8 px | 0.00 | 0.99 | 1196 |
| stroke 4 | 100 % → 99 % | 82.1 px | 0.00 | 0.99 | 1132 |
| stroke 5 | 100 % → 99 % | 82.1 px | 0.00 | 0.99 | 1108 |
| stroke 6 | 100 % → 99 % | 82.9 px | 0.00 | 0.99 | 1105 |
| stroke 7 | 100 % → 99 % | 82.9 px | 0.00 | 0.99 | 1092 |
| stroke 8 | 100 % → 99 % | 82.1 px | 0.00 | 0.99 | 1374 |
| stroke 9 | 100 % → 99 % | 58.2 px | 0.00 | 0.99 | 747 |
| stroke 10 | 100 % → 100 % | 175.9 px | 0.00 | 1.00 | 24 |
| stroke 11 | 100 % → 99 % | 198.5 px | 0.01 | 0.99 | 18 |
| stroke 12 | 100 % → 100 % | 163.3 px | 0.00 | 1.00 | 30 |
| stroke 13 | 99 % → 98 % | 165.2 px | 0.01 | 0.98 | 21 |
| stroke 14 | 100 % → 98 % | 176.7 px | 0.01 | 0.98 | 23 |
| stroke 15 | 100 % → 100 % | 207.2 px | 0.00 | 1.00 | 18 |
| stroke 16 | 100 % → 100 % | 163.5 px | 0.01 | 1.00 | 27 |
| stroke 17 | 100 % → 100 % | 198.2 px | 0.00 | 1.00 | 20 |
| stroke 18 | 100 % → 100 % | 171.1 px | 0.00 | 1.00 | 25 |
| stroke 19 | 99 % → 95 % | 148.2 px | 0.01 | 0.96 | 25 |
| stroke 20 | 100 % → 100 % | 188.0 px | 0.00 | 1.00 | 23 |
| stroke 21 | 100 % → 100 % | 222.0 px | 0.00 | 1.00 | 13 |

## Brush Artist · Ink — dry brush — own sheet
own sheet 600 × 600 · Gouache · 30 px · 3.2 s

![Brush Artist · Ink — dry brush — own sheet](Brush-Artist-Ink-dry-brush-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| ear | 17 % → 4 % | 16.7 px | 0.77 | 0.24 | 519 |
| drag0 | 20 % → 24 % | 25.0 px | 0.77 | 1.22 | 130 |
| drag1 | 25 % → 25 % | 34.2 px | 0.77 | 1.02 | 109 |
| drag2 | 28 % → 25 % | 42.1 px | 0.77 | 0.92 | 121 |
| drag3 | 30 % → 26 % | 50.2 px | 0.77 | 0.87 | 89 |

## Brush Artist · Watercolour — blue — own sheet
own sheet 600 × 600 · Watercolor · 40 px · 8.5 s

![Brush Artist · Watercolour — blue — own sheet](Brush-Artist-Watercolour-blue-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| s0 | 14 % → 28 % | 28.4 px | 0.21 | 2.04 | 57 |
| s1 | 8 % → 36 % | 9.9 px | 0.19 | 4.47 | 34 |
| s2 | 12 % → 21 % | 28.4 px | 0.28 | 1.74 | 37 |
| s3 | 11 % → 18 % | 20.3 px | 0.21 | 1.68 | 51 |
| s4 | 17 % → 34 % | 36.6 px | 0.20 | 1.96 | 99 |
| s5 | 25 % → 33 % | 34.0 px | 0.25 | 1.32 | 49 |
| s6 | 25 % → 30 % | 39.5 px | 0.21 | 1.23 | 50 |
| s7 | 27 % → 34 % | 18.5 px | 0.16 | 1.28 | 31 |
| s8 | 21 % → 25 % | 44.1 px | 0.24 | 1.19 | 38 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Charcoal — stick — own sheet
own sheet 600 × 600 · Charcoal · 28 px · 1.3 s

![Brush Artist · Charcoal — stick — own sheet](Brush-Artist-Charcoal-stick-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| finger0 | 16 % → 21 % | 15.5 px | 0.85 | 1.33 | 36 |
| tip0 | 15 % → 22 % | 18.4 px | 0.85 | 1.47 | 12 |
| finger1 | 16 % → 26 % | 15.7 px | 0.85 | 1.64 | 21 |
| tip1 | 20 % → 27 % | 24.8 px | 0.85 | 1.34 | 13 |
| finger2 | 16 % → 24 % | 16.0 px | 0.85 | 1.45 | 28 |
| tip2 | 20 % → 27 % | 24.1 px | 0.85 | 1.34 | 9 |
| finger3 | 16 % → 18 % | 16.1 px | 0.85 | 1.12 | 31 |
| tip3 | 20 % → 20 % | 24.3 px | 0.85 | 1.00 | 8 |
| cig0 | 38 % → 50 % | 35.5 px | 0.85 | 1.32 | 8 |
| cig1 | 42 % → 55 % | 39.5 px | 0.85 | 1.30 | 36 |
| cig2 | 47 % → 60 % | 44.1 px | 0.85 | 1.27 | 15 |
| cig3 | 51 % → 60 % | 47.1 px | 0.85 | 1.20 | 13 |
| cig4 | 50 % → 55 % | 46.8 px | 0.85 | 1.10 | 10 |
| cig5 | 51 % → 51 % | 47.1 px | 0.85 | 1.00 | 21 |

Numbers say: wet paint spreads well beyond the stroke.

