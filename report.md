![All brushes](contact.png)

# Brush Lab — 241 brushes · 8 Nov 2026 at 15:09

Every sheet: 1500 × 600, ten strokes in a 5 × 2 grid — 1. light line · 2. heavy line · 3. pressure swell · 4. fast wave · 5. slow wave · 6. spiral · 7. loop · 8. tilted · 9. over the wet one · 10. long, no reload (cell 8 holds «tilted» and «over the wet one» crossed). The CPU reference of Mamay's paint engine; the wet layer settles 20 s at the end.

Columns: **covered** = share of the cell with paint right after the stroke → after settling; **width** = painted area of the stroke ÷ its length (px); **dark** = mean darkness of the painted pixels above the paper's own grain (0 = paper, 1 = black); **spread** = how far wet paint went beyond the stroke (1.0 = stayed); **ms** = the stroke on the CPU; long stroke: paint in each quarter of its length (it should run out: wet → streaks → dry tail).

## Ink Line
Ink · 12 px · 25.3 s

![Ink Line](Ink-Line.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 1 % → 4 % | 4.3 px | 0.55 | 2.45 | 121 |
| heavy line | 5 % → 6 % | 15.7 px | 0.68 | 1.14 | 66 |
| pressure swell | 3 % → 4 % | 11.3 px | 0.64 | 1.40 | 45 |
| fast wave | 10 % → 11 % | 11.2 px | 0.59 | 1.11 | 163 |
| slow wave | 8 % → 10 % | 9.6 px | 0.57 | 1.16 | 121 |
| spiral | 14 % → 15 % | 8.9 px | 0.49 | 1.07 | 186 |
| loop | 8 % → 9 % | 10.6 px | 0.61 | 1.15 | 93 |
| tilted | 5 % → 5 % | 14.3 px | 0.64 | 1.05 | 43 |
| over the wet one | 10 % → 11 % | 12.5 px | 0.64 | 1.15 | 46 |
| long, no reload | 18 % → 17 % | 8.1 px | 0.47 | 0.96 | 263 | quarters: 0.22 → 0.09 → 0.04 → 0.02

Numbers say: light vs heavy: width 4.3 → 15.7 px, dark 0.55 → 0.68; wet paint spreads well beyond the stroke.

## Dense Ink
Ink · 14 px · 25.8 s

![Dense Ink](Dense-Ink.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 5 % → 7 % | 15.2 px | 0.72 | 1.27 | 119 |
| heavy line | 7 % → 7 % | 19.1 px | 0.73 | 1.09 | 86 |
| pressure swell | 5 % → 6 % | 17.9 px | 0.72 | 1.18 | 55 |
| fast wave | 13 % → 13 % | 15.2 px | 0.69 | 1.01 | 140 |
| slow wave | 12 % → 12 % | 13.5 px | 0.67 | 1.04 | 133 |
| spiral | 18 % → 15 % | 12.2 px | 0.65 | 0.80 | 166 |
| loop | 11 % → 12 % | 14.8 px | 0.69 | 1.08 | 229 |
| tilted | 5 % → 6 % | 14.5 px | 0.72 | 1.07 | 60 |
| over the wet one | 12 % → 13 % | 17.7 px | 0.72 | 1.12 | 62 |
| long, no reload | 23 % → 15 % | 10.1 px | 0.64 | 0.66 | 289 | quarters: 0.30 → 0.12 → 0.04 → 0.02

Numbers say: light vs heavy: width 15.2 → 19.1 px, dark 0.72 → 0.73.

## Transparent Wash
Watercolor · 22 px · 26.9 s

![Transparent Wash](Transparent-Wash.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 2 % → 5 % | 6.9 px | 0.27 | 2.26 | 96 |
| heavy line | 7 % → 9 % | 20.4 px | 0.27 | 1.23 | 73 |
| pressure swell | 4 % → 6 % | 15.2 px | 0.28 | 1.54 | 24 |
| fast wave | 14 % → 16 % | 16.1 px | 0.20 | 1.17 | 143 |
| slow wave | 12 % → 15 % | 13.7 px | 0.21 | 1.28 | 174 |
| spiral | 18 % → 22 % | 11.9 px | 0.16 | 1.22 | 167 |
| loop | 11 % → 13 % | 14.5 px | 0.22 | 1.20 | 94 |
| tilted | 8 % → 8 % | 21.1 px | 0.24 | 1.06 | 56 |
| over the wet one | 13 % → 16 % | 16.4 px | 0.24 | 1.19 | 42 |
| long, no reload | 26 % → 32 % | 11.6 px | 0.13 | 1.22 | 265 | quarters: 0.11 → 0.04 → 0.02 → 0.01

Numbers say: light vs heavy: width 6.9 → 20.4 px, dark 0.27 → 0.27; wet paint spreads well beyond the stroke.

## Dry Brush
Gouache · 24 px · 25.2 s

![Dry Brush](Dry-Brush.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 5 % → 1 % | 13.8 px | 0.65 | 0.11 | 163 |
| heavy line | 6 % → 0 % | 18.4 px | 0.65 | 0.02 | 101 |
| pressure swell | 5 % → 0 % | 18.1 px | 0.65 | 0.09 | 59 |
| fast wave | 6 % → 1 % | 6.9 px | 0.65 | 0.08 | 129 |
| slow wave | 7 % → 0 % | 7.8 px | 0.65 | 0.07 | 212 |
| spiral | 7 % → 1 % | 4.4 px | 0.65 | 0.08 | 230 |
| loop | 9 % → 0 % | 12.2 px | 0.65 | 0.05 | 126 |
| tilted | 4 % → 3 % | 10.3 px | 0.65 | 0.89 | 60 |
| over the wet one | 9 % → 1 % | 14.3 px | 0.65 | 0.12 | 56 |
| long, no reload | 6 % → 1 % | 2.7 px | 0.65 | 0.15 | 305 | quarters: 0.12 → 0.00 → 0.00 → 0.00

Numbers say: light vs heavy: width 13.8 → 18.4 px, dark 0.65 → 0.65.

## Wax Crayon
Wax · 8 px · 10.0 s

![Wax Crayon](Wax-Crayon.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 1 % → 1 % | 2.5 px | 0.71 | 1.00 | 41 |
| heavy line | 1 % → 1 % | 3.9 px | 0.69 | 1.00 | 45 |
| pressure swell | 1 % → 1 % | 3.3 px | 0.70 | 1.00 | 20 |
| fast wave | 3 % → 3 % | 3.5 px | 0.69 | 1.00 | 29 |
| slow wave | 3 % → 3 % | 3.4 px | 0.70 | 1.00 | 41 |
| spiral | 5 % → 5 % | 3.3 px | 0.70 | 1.00 | 99 |
| loop | 3 % → 3 % | 3.3 px | 0.70 | 1.00 | 61 |
| tilted | 2 % → 2 % | 5.6 px | 0.68 | 1.00 | 28 |
| over the wet one | 3 % → 3 % | 3.6 px | 0.68 | 1.00 | 9 |
| long, no reload | 7 % → 7 % | 3.3 px | 0.70 | 1.00 | 127 | quarters: 0.06 → 0.06 → 0.06 → 0.06

Numbers say: light vs heavy: width 2.5 → 3.9 px, dark 0.71 → 0.69; the long stroke does not run out of paint.

## Oil Pastel
Wax · 12 px · 10.2 s

![Oil Pastel](Oil-Pastel.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 1 % → 1 % | 4.0 px | 0.68 | 1.00 | 87 |
| heavy line | 2 % → 2 % | 6.5 px | 0.68 | 1.00 | 42 |
| pressure swell | 2 % → 2 % | 5.7 px | 0.69 | 1.00 | 20 |
| fast wave | 5 % → 5 % | 5.7 px | 0.68 | 1.00 | 63 |
| slow wave | 5 % → 5 % | 5.5 px | 0.68 | 1.00 | 78 |
| spiral | 8 % → 8 % | 5.5 px | 0.68 | 1.00 | 91 |
| loop | 4 % → 4 % | 5.6 px | 0.68 | 1.00 | 62 |
| tilted | 2 % → 2 % | 6.8 px | 0.68 | 1.00 | 43 |
| over the wet one | 5 % → 5 % | 5.8 px | 0.68 | 1.00 | 24 |
| long, no reload | 13 % → 13 % | 5.6 px | 0.68 | 1.00 | 144 | quarters: 0.10 → 0.09 → 0.10 → 0.10

Numbers say: light vs heavy: width 4.0 → 6.5 px, dark 0.68 → 0.68; the long stroke does not run out of paint.

## Charcoal
Charcoal · 5 px · 9.8 s

![Charcoal](Charcoal.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 1 % → 1 % | 2.0 px | 0.74 | 1.00 | 52 |
| heavy line | 1 % → 1 % | 3.0 px | 0.74 | 1.00 | 16 |
| pressure swell | 1 % → 1 % | 2.7 px | 0.74 | 1.00 | 11 |
| fast wave | 2 % → 2 % | 2.7 px | 0.73 | 1.00 | 23 |
| slow wave | 2 % → 2 % | 2.6 px | 0.74 | 1.00 | 24 |
| spiral | 4 % → 4 % | 2.5 px | 0.74 | 1.00 | 51 |
| loop | 2 % → 2 % | 2.6 px | 0.74 | 1.00 | 41 |
| tilted | 2 % → 2 % | 4.3 px | 0.72 | 1.00 | 28 |
| over the wet one | 2 % → 2 % | 2.4 px | 0.72 | 1.00 | 6 |
| long, no reload | 6 % → 6 % | 2.7 px | 0.73 | 1.00 | 86 | quarters: 0.05 → 0.05 → 0.05 → 0.05

Numbers say: light vs heavy: width 2.0 → 3.0 px, dark 0.74 → 0.74; the long stroke does not run out of paint.

## Impasto
Heavy acrylic · 22 px · 15.8 s

![Impasto](Impasto.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 8 % → 8 % | 24.1 px | 0.72 | 0.93 | 195 |
| heavy line | 10 % → 9 % | 28.8 px | 0.70 | 0.94 | 113 |
| pressure swell | 7 % → 7 % | 28.1 px | 0.72 | 0.94 | 47 |
| fast wave | 20 % → 13 % | 23.4 px | 0.71 | 0.64 | 158 |
| slow wave | 21 % → 14 % | 24.5 px | 0.71 | 0.66 | 250 |
| spiral | 30 % → 14 % | 19.9 px | 0.71 | 0.46 | 258 |
| loop | 18 % → 14 % | 23.9 px | 0.71 | 0.77 | 130 |
| tilted | 8 % → 8 % | 21.7 px | 0.70 | 1.00 | 77 |
| over the wet one | 17 % → 15 % | 25.4 px | 0.70 | 0.91 | 63 |
| long, no reload | 33 % → 14 % | 14.9 px | 0.71 | 0.42 | 337 | quarters: 0.38 → 0.21 → 0.10 → 0.03

Numbers say: light vs heavy: width 24.1 → 28.8 px, dark 0.72 → 0.70.

## Oil Round
Oil · 18 px · 18.2 s

![Oil Round](Oil-Round.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 2 % → 2 % | 7.2 px | 0.75 | 1.00 | 193 |
| heavy line | 7 % → 7 % | 19.3 px | 0.73 | 1.00 | 114 |
| pressure swell | 4 % → 4 % | 13.7 px | 0.72 | 1.00 | 33 |
| fast wave | 11 % → 11 % | 12.8 px | 0.65 | 1.00 | 166 |
| slow wave | 8 % → 8 % | 9.0 px | 0.57 | 1.00 | 143 |
| spiral | 10 % → 10 % | 6.6 px | 0.50 | 1.00 | 201 |
| loop | 6 % → 6 % | 7.2 px | 0.45 | 1.00 | 121 |
| tilted | 4 % → 4 % | 10.1 px | 0.52 | 1.00 | 63 |
| over the wet one | 6 % → 6 % | 7.6 px | 0.52 | 1.00 | 48 |
| long, no reload | 15 % → 15 % | 6.9 px | 0.42 | 1.00 | 283 | quarters: 0.09 → 0.08 → 0.07 → 0.06

Numbers say: light vs heavy: width 7.2 → 19.3 px, dark 0.75 → 0.73.

## Palette Knife
Oil · 20 px · 17.7 s

![Palette Knife](Palette-Knife.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 8 % → 8 % | 21.9 px | 0.67 | 1.00 | 148 |
| heavy line | 8 % → 8 % | 22.5 px | 0.74 | 1.00 | 57 |
| pressure swell | 6 % → 6 % | 22.3 px | 0.74 | 1.00 | 17 |
| fast wave | 16 % → 16 % | 18.9 px | 0.50 | 1.00 | 23 |
| slow wave | 17 % → 17 % | 19.9 px | 0.43 | 1.00 | 63 |
| spiral | 17 % → 17 % | 11.3 px | 0.46 | 1.00 | 56 |
| loop | 16 % → 16 % | 21.0 px | 0.59 | 1.00 | 19 |
| tilted | 5 % → 5 % | 15.0 px | 0.72 | 1.00 | 13 |
| over the wet one | 13 % → 13 % | 21.0 px | 0.72 | 1.00 | 14 |
| long, no reload | 16 % → 16 % | 7.2 px | 0.49 | 1.00 | 55 | quarters: 0.29 → 0.05 → 0.00 → 0.00

Numbers say: light vs heavy: width 21.9 → 22.5 px, dark 0.67 → 0.74; pressure barely changes the width.

## Water
Watercolor · 20 px · 35.7 s · over bands of wet oil paint and oil pastel in turn (it works on paint already there: look at what it does to the bands; covered counts the bands too)

![Water](Water.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 25 % → 27 % | 73.8 px | 0.80 | 1.06 | 31 |
| heavy line | 24 % → 25 % | 69.8 px | 0.81 | 1.04 | 84 |
| pressure swell | 24 % → 25 % | 89.6 px | 0.81 | 1.03 | 27 |
| fast wave | 24 % → 26 % | 27.7 px | 0.81 | 1.07 | 118 |
| slow wave | 24 % → 25 % | 27.8 px | 0.81 | 1.06 | 171 |
| spiral | 24 % → 26 % | 15.9 px | 0.81 | 1.07 | 234 |
| loop | 24 % → 25 % | 31.1 px | 0.81 | 1.03 | 130 |
| tilted | 24 % → 24 % | 67.0 px | 0.81 | 1.00 | 54 |
| over the wet one | 24 % → 25 % | 0.0 px | 0.81 | 1.06 | 42 |
| long, no reload | 24 % → 26 % | 10.7 px | 0.81 | 1.08 | 259 | quarters: 0.21 → 0.27 → 0.18 → 0.27

Numbers say: light vs heavy: width 73.8 → 69.8 px, dark 0.80 → 0.81; pressure barely changes the width; the long stroke does not run out of paint.

## Blender
Pastel · 16 px · 21.3 s · over bands of wet oil paint and oil pastel in turn (it works on paint already there: look at what it does to the bands; covered counts the bands too)

![Blender](Blender.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 24 % → 24 % | 70.7 px | 0.81 | 1.00 | 25 |
| heavy line | 25 % → 25 % | 72.1 px | 0.80 | 1.00 | 28 |
| pressure swell | 24 % → 24 % | 91.3 px | 0.81 | 1.00 | 17 |
| fast wave | 26 % → 26 % | 30.0 px | 0.79 | 1.00 | 69 |
| slow wave | 26 % → 26 % | 29.9 px | 0.80 | 1.00 | 99 |
| spiral | 28 % → 28 % | 18.7 px | 0.77 | 1.00 | 114 |
| loop | 25 % → 25 % | 33.0 px | 0.80 | 1.00 | 88 |
| tilted | 25 % → 25 % | 70.1 px | 0.79 | 1.00 | 43 |
| over the wet one | 26 % → 26 % | 1.8 px | 0.79 | 1.00 | 20 |
| long, no reload | 30 % → 30 % | 13.7 px | 0.76 | 1.00 | 255 | quarters: 0.20 → 0.28 → 0.23 → 0.30

Numbers say: light vs heavy: width 70.7 → 72.1 px, dark 0.81 → 0.80; pressure barely changes the width; the long stroke does not run out of paint.

## Eraser
Eraser · 16 px · 20.8 s · over bands of wet oil paint and oil pastel in turn (it works on paint already there: look at what it does to the bands; covered counts the bands too)

![Eraser](Eraser.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 24 % → 24 % | 69.6 px | 0.82 | 1.00 | 27 |
| heavy line | 23 % → 23 % | 67.9 px | 0.82 | 1.00 | 54 |
| pressure swell | 23 % → 23 % | 87.3 px | 0.82 | 1.00 | 35 |
| fast wave | 22 % → 22 % | 25.7 px | 0.82 | 1.00 | 62 |
| slow wave | 22 % → 22 % | 25.7 px | 0.82 | 1.00 | 77 |
| spiral | 22 % → 22 % | 14.4 px | 0.82 | 1.00 | 105 |
| loop | 22 % → 22 % | 28.6 px | 0.82 | 1.00 | 72 |
| tilted | 23 % → 23 % | 65.1 px | 0.82 | 1.00 | 34 |
| over the wet one | 23 % → 23 % | 0.0 px | 0.82 | 1.00 | 32 |
| long, no reload | 20 % → 20 % | 8.9 px | 0.82 | 1.00 | 290 | quarters: 0.15 → 0.20 → 0.15 → 0.20

Numbers say: light vs heavy: width 69.6 → 67.9 px, dark 0.82 → 0.82; pressure barely changes the width; the long stroke does not run out of paint.

## Fan
Gouache · 30 px · 28.5 s

![Fan](Fan.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 9 % → 3 % | 25.6 px | 0.63 | 0.37 | 35 |
| heavy line | 11 % → 4 % | 30.9 px | 0.63 | 0.39 | 50 |
| pressure swell | 8 % → 5 % | 31.7 px | 0.63 | 0.55 | 31 |
| fast wave | 17 % → 5 % | 20.2 px | 0.63 | 0.26 | 123 |
| slow wave | 18 % → 5 % | 21.0 px | 0.63 | 0.25 | 176 |
| spiral | 24 % → 5 % | 15.5 px | 0.63 | 0.19 | 144 |
| loop | 17 % → 5 % | 22.7 px | 0.63 | 0.28 | 126 |
| tilted | 5 % → 6 % | 15.0 px | 0.63 | 1.05 | 44 |
| over the wet one | 16 % → 8 % | 29.7 px | 0.63 | 0.49 | 57 |
| long, no reload | 22 % → 5 % | 9.9 px | 0.63 | 0.22 | 223 | quarters: 0.29 → 0.07 → 0.01 → 0.00

Numbers say: light vs heavy: width 25.6 → 30.9 px, dark 0.63 → 0.63.

## Sponge
Gouache · 30 px · 28.1 s

![Sponge](Sponge.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 4 % → 0 % | 11.3 px | 0.62 | 0.12 | 33 |
| heavy line | 12 % → 2 % | 35.4 px | 0.62 | 0.14 | 81 |
| pressure swell | 7 % → 2 % | 27.9 px | 0.62 | 0.28 | 58 |
| fast wave | 20 % → 4 % | 23.2 px | 0.62 | 0.19 | 106 |
| slow wave | 21 % → 4 % | 23.8 px | 0.62 | 0.18 | 245 |
| spiral | 28 % → 4 % | 18.3 px | 0.62 | 0.14 | 172 |
| loop | 18 % → 5 % | 23.0 px | 0.62 | 0.29 | 104 |
| tilted | 7 % → 7 % | 18.2 px | 0.62 | 1.04 | 85 |
| over the wet one | 16 % → 6 % | 27.8 px | 0.62 | 0.37 | 45 |
| long, no reload | 29 % → 5 % | 12.9 px | 0.62 | 0.17 | 257 | quarters: 0.29 → 0.13 → 0.07 → 0.04

Numbers say: light vs heavy: width 11.3 → 35.4 px, dark 0.62 → 0.62.

## Ink — sumi brush
Watercolour 1.00 · 22 px · 28.2 s

![Ink — sumi brush](Ink-sumi-brush.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 8 % → 9 % | 23.9 px | 0.87 | 1.13 | 90 |
| heavy line | 12 % → 13 % | 36.2 px | 0.86 | 1.01 | 78 |
| pressure swell | 10 % → 10 % | 36.1 px | 0.87 | 1.04 | 57 |
| fast wave | 27 % → 27 % | 31.0 px | 0.82 | 1.00 | 157 |
| slow wave | 27 % → 28 % | 31.2 px | 0.82 | 1.02 | 278 |
| spiral | 38 % → 36 % | 25.2 px | 0.75 | 0.95 | 264 |
| loop | 22 % → 23 % | 29.0 px | 0.84 | 1.01 | 157 |
| tilted | 9 % → 9 % | 25.7 px | 0.86 | 1.00 | 81 |
| over the wet one | 20 % → 20 % | 30.0 px | 0.86 | 1.02 | 58 |
| long, no reload | 46 % → 41 % | 20.7 px | 0.70 | 0.90 | 396 | quarters: 0.57 → 0.42 → 0.24 → 0.15

Numbers say: light vs heavy: width 23.9 → 36.2 px, dark 0.87 → 0.86.

## Ink — wash
Watercolour 1.00 · 40 px · 31.4 s

![Ink — wash](Ink-wash.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 13 % → 13 % | 37.3 px | 0.42 | 1.02 | 75 |
| heavy line | 19 % → 19 % | 55.2 px | 0.35 | 1.01 | 74 |
| pressure swell | 13 % → 13 % | 48.2 px | 0.41 | 1.02 | 67 |
| fast wave | 41 % → 42 % | 47.8 px | 0.32 | 1.02 | 192 |
| slow wave | 39 % → 40 % | 45.3 px | 0.42 | 1.02 | 337 |
| spiral | 60 % → 62 % | 39.7 px | 0.33 | 1.02 | 356 |
| loop | 34 % → 34 % | 43.8 px | 0.39 | 1.01 | 181 |
| tilted | 15 % → 15 % | 40.7 px | 0.43 | 1.01 | 104 |
| over the wet one | 30 % → 31 % | 43.4 px | 0.43 | 1.02 | 82 |
| long, no reload | 71 % → 75 % | 32.0 px | 0.31 | 1.05 | 487 | quarters: 0.40 → 0.29 → 0.19 → 0.12

Numbers say: light vs heavy: width 37.3 → 55.2 px, dark 0.42 → 0.35.

## Ink — dry brush
Ink 1.00 · 30 px · 23.7 s

![Ink — dry brush](Ink-dry-brush.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 5 % → 5 % | 14.9 px | 0.82 | 0.88 | 93 |
| heavy line | 7 % → 6 % | 19.4 px | 0.82 | 0.87 | 123 |
| pressure swell | 5 % → 5 % | 18.9 px | 0.81 | 0.96 | 77 |
| fast wave | 12 % → 7 % | 13.4 px | 0.80 | 0.65 | 237 |
| slow wave | 12 % → 8 % | 14.1 px | 0.81 | 0.62 | 375 |
| spiral | 16 % → 8 % | 10.8 px | 0.80 | 0.47 | 402 |
| loop | 11 % → 9 % | 14.5 px | 0.79 | 0.77 | 209 |
| tilted | 5 % → 6 % | 15.0 px | 0.81 | 1.08 | 114 |
| over the wet one | 12 % → 11 % | 18.4 px | 0.81 | 0.94 | 84 |
| long, no reload | 21 % → 10 % | 9.2 px | 0.77 | 0.47 | 520 | quarters: 0.28 → 0.10 → 0.03 → 0.01

Numbers say: light vs heavy: width 14.9 → 19.4 px, dark 0.82 → 0.82.

## Ink — nib
Watercolour 1.00 · 5 px · 23.0 s

![Ink — nib](Ink-nib.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 2 % → 5 % | 5.5 px | 0.89 | 2.46 | 28 |
| heavy line | 2 % → 5 % | 6.4 px | 0.89 | 2.34 | 27 |
| pressure swell | 2 % → 4 % | 6.2 px | 0.89 | 2.53 | 18 |
| fast wave | 5 % → 8 % | 5.9 px | 0.89 | 1.63 | 53 |
| slow wave | 5 % → 8 % | 5.7 px | 0.89 | 1.70 | 65 |
| spiral | 8 % → 11 % | 5.0 px | 0.87 | 1.41 | 143 |
| loop | 4 % → 8 % | 5.7 px | 0.89 | 1.74 | 60 |
| tilted | 4 % → 4 % | 10.3 px | 0.89 | 1.02 | 20 |
| over the wet one | 6 % → 9 % | 6.1 px | 0.89 | 1.61 | 25 |
| long, no reload | 9 % → 12 % | 4.2 px | 0.85 | 1.30 | 135 | quarters: 0.24 → 0.11 → 0.07 → 0.05

Numbers say: light vs heavy: width 5.5 → 6.4 px, dark 0.89 → 0.89; wet paint spreads well beyond the stroke.

## 0.45 · Dry brush
Gouache 0.91 · Ink 0.07 · 34 px · 30.2 s

![0.45 · Dry brush](0-45-Dry-brush.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 8 % → 2 % | 22.9 px | 0.68 | 0.26 | 103 |
| heavy line | 10 % → 6 % | 27.8 px | 0.68 | 0.58 | 130 |
| pressure swell | 7 % → 4 % | 26.5 px | 0.68 | 0.61 | 89 |
| fast wave | 19 % → 6 % | 21.4 px | 0.68 | 0.33 | 326 |
| slow wave | 20 % → 7 % | 23.0 px | 0.68 | 0.38 | 613 |
| spiral | 27 % → 8 % | 17.6 px | 0.68 | 0.29 | 505 |
| loop | 18 % → 9 % | 23.0 px | 0.68 | 0.51 | 261 |
| tilted | 8 % → 8 % | 21.8 px | 0.68 | 1.02 | 127 |
| over the wet one | 17 % → 12 % | 25.0 px | 0.68 | 0.73 | 139 |
| long, no reload | 34 % → 9 % | 15.3 px | 0.68 | 0.28 | 810 | quarters: 0.37 → 0.26 → 0.19 → 0.17

Numbers say: light vs heavy: width 22.9 → 27.8 px, dark 0.68 → 0.68.

## Dry pastel
Pastel 1.00 · 26 px · 10.6 s

![Dry pastel](Dry-pastel.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 3 % → 3 % | 8.2 px | 0.37 | 1.00 | 33 |
| heavy line | 5 % → 5 % | 13.1 px | 0.39 | 1.00 | 29 |
| pressure swell | 3 % → 3 % | 11.5 px | 0.39 | 1.00 | 24 |
| fast wave | 10 % → 10 % | 11.8 px | 0.39 | 1.00 | 88 |
| slow wave | 10 % → 10 % | 11.1 px | 0.39 | 1.00 | 151 |
| spiral | 14 % → 14 % | 9.1 px | 0.38 | 1.00 | 145 |
| loop | 7 % → 7 % | 9.5 px | 0.38 | 1.00 | 91 |
| tilted | 3 % → 3 % | 7.5 px | 0.39 | 1.00 | 29 |
| over the wet one | 6 % → 6 % | 10.6 px | 0.39 | 1.00 | 28 |
| long, no reload | 17 % → 17 % | 7.6 px | 0.38 | 1.00 | 220 | quarters: 0.08 → 0.07 → 0.07 → 0.07

Numbers say: light vs heavy: width 8.2 → 13.1 px, dark 0.37 → 0.39; the long stroke does not run out of paint.

## 0.45 · Charcoal
Charcoal 1.00 · 18 px · 9.7 s

![0.45 · Charcoal](0-45-Charcoal.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 2 % → 2 % | 5.4 px | 0.79 | 1.00 | 21 |
| heavy line | 3 % → 3 % | 8.0 px | 0.79 | 1.00 | 13 |
| pressure swell | 2 % → 2 % | 7.8 px | 0.80 | 1.00 | 19 |
| fast wave | 8 % → 8 % | 8.8 px | 0.80 | 1.00 | 43 |
| slow wave | 6 % → 6 % | 7.3 px | 0.80 | 1.00 | 63 |
| spiral | 10 % → 10 % | 6.7 px | 0.80 | 1.00 | 60 |
| loop | 6 % → 6 % | 8.2 px | 0.80 | 1.00 | 35 |
| tilted | 3 % → 3 % | 7.2 px | 0.79 | 1.00 | 24 |
| over the wet one | 5 % → 5 % | 7.4 px | 0.79 | 1.00 | 24 |
| long, no reload | 17 % → 17 % | 7.8 px | 0.80 | 1.00 | 107 | quarters: 0.15 → 0.16 → 0.16 → 0.16

Numbers say: light vs heavy: width 5.4 → 8.0 px, dark 0.79 → 0.79; the long stroke does not run out of paint.

## Watercolour — wash
Watercolour 1.00 · 50 px · 33.6 s

![Watercolour — wash](Watercolour-wash.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 16 % → 16 % | 45.5 px | 0.22 | 1.01 | 100 |
| heavy line | 22 % → 22 % | 64.9 px | 0.19 | 1.00 | 123 |
| pressure swell | 15 % → 15 % | 56.1 px | 0.22 | 1.01 | 77 |
| fast wave | 48 % → 49 % | 55.5 px | 0.19 | 1.01 | 305 |
| slow wave | 46 % → 46 % | 53.3 px | 0.24 | 1.00 | 467 |
| spiral | 66 % → 66 % | 43.7 px | 0.21 | 1.00 | 501 |
| loop | 40 % → 40 % | 51.4 px | 0.22 | 1.00 | 245 |
| tilted | 18 % → 18 % | 49.7 px | 0.23 | 1.00 | 168 |
| over the wet one | 36 % → 36 % | 49.6 px | 0.23 | 1.01 | 102 |
| long, no reload | 84 % → 84 % | 37.7 px | 0.20 | 1.00 | 793 | quarters: 0.24 → 0.20 → 0.16 → 0.12

Numbers say: light vs heavy: width 45.5 → 64.9 px, dark 0.22 → 0.19.

## Watercolour — wet-in-wet
Watercolour 1.00 · 44 px · 34.6 s

![Watercolour — wet-in-wet](Watercolour-wet-in-wet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 13 % → 21 % | 37.4 px | 0.32 | 1.63 | 85 |
| heavy line | 19 % → 22 % | 54.7 px | 0.34 | 1.17 | 95 |
| pressure swell | 12 % → 17 % | 45.7 px | 0.36 | 1.36 | 68 |
| fast wave | 42 % → 49 % | 48.5 px | 0.33 | 1.16 | 227 |
| slow wave | 40 % → 48 % | 45.7 px | 0.41 | 1.22 | 431 |
| spiral | 63 % → 69 % | 41.3 px | 0.37 | 1.11 | 412 |
| loop | 34 % → 41 % | 44.0 px | 0.37 | 1.21 | 200 |
| tilted | 16 % → 17 % | 44.6 px | 0.36 | 1.05 | 140 |
| over the wet one | 32 % → 40 % | 44.4 px | 0.36 | 1.26 | 86 |
| long, no reload | 79 % → 87 % | 35.3 px | 0.36 | 1.11 | 535 | quarters: 0.40 → 0.37 → 0.33 → 0.26

Numbers say: light vs heavy: width 37.4 → 54.7 px, dark 0.32 → 0.34; wet paint spreads well beyond the stroke.

## Watercolour — glaze
Watercolour 1.00 · 38 px · 30.4 s

![Watercolour — glaze](Watercolour-glaze.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 13 % → 13 % | 36.6 px | 0.07 | 1.02 | 71 |
| heavy line | 19 % → 19 % | 55.4 px | 0.07 | 1.00 | 88 |
| pressure swell | 13 % → 13 % | 47.0 px | 0.07 | 1.02 | 64 |
| fast wave | 39 % → 40 % | 45.6 px | 0.07 | 1.01 | 186 |
| slow wave | 37 % → 37 % | 42.8 px | 0.07 | 1.01 | 325 |
| spiral | 59 % → 60 % | 38.8 px | 0.06 | 1.01 | 325 |
| loop | 33 % → 33 % | 42.6 px | 0.07 | 1.00 | 195 |
| tilted | 14 % → 14 % | 40.1 px | 0.07 | 1.00 | 118 |
| over the wet one | 30 % → 30 % | 42.3 px | 0.07 | 1.01 | 80 |
| long, no reload | 69 % → 70 % | 30.9 px | 0.06 | 1.01 | 494 | quarters: 0.06 → 0.05 → 0.03 → 0.02

Numbers say: light vs heavy: width 36.6 → 55.4 px, dark 0.07 → 0.07.

## Watercolour — granulating
Watercolour 1.00 · 44 px · 31.2 s

![Watercolour — granulating](Watercolour-granulating.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 14 % → 14 % | 41.4 px | 0.35 | 1.01 | 85 |
| heavy line | 21 % → 21 % | 60.4 px | 0.31 | 1.00 | 105 |
| pressure swell | 14 % → 14 % | 52.2 px | 0.34 | 1.01 | 69 |
| fast wave | 45 % → 45 % | 51.7 px | 0.29 | 1.01 | 237 |
| slow wave | 42 % → 42 % | 48.2 px | 0.35 | 1.01 | 360 |
| spiral | 62 % → 63 % | 41.0 px | 0.30 | 1.01 | 469 |
| loop | 37 % → 37 % | 47.6 px | 0.33 | 1.00 | 206 |
| tilted | 16 % → 16 % | 45.5 px | 0.36 | 1.00 | 147 |
| over the wet one | 33 % → 33 % | 46.2 px | 0.36 | 1.01 | 95 |
| long, no reload | 75 % → 76 % | 33.6 px | 0.29 | 1.01 | 584 | quarters: 0.34 → 0.26 → 0.20 → 0.14

Numbers say: light vs heavy: width 41.4 → 60.4 px, dark 0.35 → 0.31.

## Watercolour — dry brush
Watercolour 1.00 · 36 px · 25.7 s

![Watercolour — dry brush](Watercolour-dry-brush.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 10 % → 9 % | 27.8 px | 0.17 | 0.99 | 98 |
| heavy line | 14 % → 12 % | 39.3 px | 0.16 | 0.92 | 94 |
| pressure swell | 11 % → 10 % | 39.6 px | 0.16 | 0.95 | 54 |
| fast wave | 27 % → 20 % | 31.3 px | 0.13 | 0.74 | 250 |
| slow wave | 25 % → 17 % | 28.9 px | 0.14 | 0.70 | 425 |
| spiral | 34 % → 19 % | 22.6 px | 0.13 | 0.56 | 457 |
| loop | 21 % → 18 % | 27.7 px | 0.14 | 0.85 | 237 |
| tilted | 10 % → 10 % | 28.5 px | 0.16 | 1.01 | 131 |
| over the wet one | 21 % → 20 % | 31.0 px | 0.16 | 0.95 | 102 |
| long, no reload | 35 % → 19 % | 15.9 px | 0.14 | 0.54 | 631 | quarters: 0.09 → 0.03 → 0.01 → 0.00

Numbers say: light vs heavy: width 27.8 → 39.3 px, dark 0.17 → 0.16.

## Gouache
Gouache 1.00 · 30 px · 28.2 s

![Gouache](Gouache.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 8 % → 5 % | 23.3 px | 0.29 | 0.61 | 70 |
| heavy line | 12 % → 5 % | 35.6 px | 0.28 | 0.41 | 89 |
| pressure swell | 10 % → 5 % | 36.2 px | 0.28 | 0.49 | 72 |
| fast wave | 22 % → 6 % | 25.0 px | 0.28 | 0.27 | 217 |
| slow wave | 22 % → 7 % | 25.9 px | 0.28 | 0.30 | 415 |
| spiral | 28 % → 7 % | 18.5 px | 0.28 | 0.23 | 367 |
| loop | 18 % → 7 % | 23.7 px | 0.28 | 0.37 | 187 |
| tilted | 9 % → 9 % | 24.0 px | 0.28 | 1.01 | 112 |
| over the wet one | 19 % → 12 % | 28.7 px | 0.28 | 0.62 | 84 |
| long, no reload | 27 % → 8 % | 12.2 px | 0.28 | 0.31 | 500 | quarters: 0.01 → 0.02 → 0.02 → 0.02

Numbers say: light vs heavy: width 23.3 → 35.6 px, dark 0.29 → 0.28; the long stroke does not run out of paint.

## Oil — alla prima
Oil 0.89 · Oil glaze 0.11 · 30 px · 13.5 s

![Oil — alla prima](Oil-alla-prima.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 9 % → 9 % | 27.5 px | 0.49 | 1.00 | 94 |
| heavy line | 10 % → 10 % | 28.7 px | 0.50 | 1.00 | 92 |
| pressure swell | 7 % → 7 % | 27.5 px | 0.50 | 1.00 | 66 |
| fast wave | 22 % → 22 % | 25.5 px | 0.50 | 1.00 | 265 |
| slow wave | 25 % → 25 % | 29.0 px | 0.50 | 1.00 | 382 |
| spiral | 37 % → 37 % | 24.5 px | 0.49 | 1.00 | 389 |
| loop | 21 % → 21 % | 27.5 px | 0.50 | 1.00 | 210 |
| tilted | 10 % → 10 % | 26.8 px | 0.50 | 1.00 | 102 |
| over the wet one | 19 % → 19 % | 27.7 px | 0.50 | 1.00 | 99 |
| long, no reload | 46 % → 46 % | 20.5 px | 0.47 | 1.00 | 616 | quarters: 0.31 → 0.25 → 0.22 → 0.18

Numbers say: light vs heavy: width 27.5 → 28.7 px, dark 0.49 → 0.50; pressure barely changes the width.

## Oil — impasto
Oil heavy 1.00 · 34 px · 14.5 s

![Oil — impasto](Oil-impasto.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 8 % → 8 % | 24.0 px | 0.22 | 1.00 | 95 |
| heavy line | 12 % → 12 % | 35.3 px | 0.22 | 1.00 | 105 |
| pressure swell | 9 % → 9 % | 33.1 px | 0.23 | 1.00 | 87 |
| fast wave | 29 % → 29 % | 33.7 px | 0.22 | 1.00 | 302 |
| slow wave | 30 % → 30 % | 34.6 px | 0.22 | 1.00 | 585 |
| spiral | 47 % → 47 % | 31.3 px | 0.21 | 1.00 | 522 |
| loop | 25 % → 25 % | 32.5 px | 0.22 | 1.00 | 308 |
| tilted | 11 % → 11 % | 31.8 px | 0.24 | 1.00 | 157 |
| over the wet one | 21 % → 21 % | 26.8 px | 0.24 | 1.00 | 90 |
| long, no reload | 54 % → 54 % | 24.4 px | 0.20 | 1.00 | 718 | quarters: 0.16 → 0.14 → 0.11 → 0.09

Numbers say: light vs heavy: width 24.0 → 35.3 px, dark 0.22 → 0.22.

## Oil — glaze
Oil glaze 1.00 · 40 px · 14.9 s

![Oil — glaze](Oil-glaze.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 9 % → 9 % | 27.0 px | 0.50 | 1.00 | 88 |
| heavy line | 13 % → 13 % | 38.3 px | 0.49 | 1.00 | 113 |
| pressure swell | 10 % → 10 % | 36.6 px | 0.50 | 1.00 | 75 |
| fast wave | 29 % → 29 % | 33.5 px | 0.49 | 1.00 | 268 |
| slow wave | 30 % → 30 % | 34.6 px | 0.50 | 1.00 | 409 |
| spiral | 46 % → 46 % | 30.1 px | 0.49 | 1.00 | 450 |
| loop | 24 % → 24 % | 31.4 px | 0.50 | 1.00 | 232 |
| tilted | 11 % → 11 % | 30.4 px | 0.50 | 1.00 | 135 |
| over the wet one | 23 % → 23 % | 32.5 px | 0.50 | 1.00 | 106 |
| long, no reload | 52 % → 52 % | 23.5 px | 0.49 | 1.00 | 648 | quarters: 0.34 → 0.30 → 0.27 → 0.22

Numbers say: light vs heavy: width 27.0 → 38.3 px, dark 0.50 → 0.49.

## Oil — scumble
Oil 1.00 · 36 px · 14.2 s

![Oil — scumble](Oil-scumble.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 5 % → 5 % | 13.1 px | 0.08 | 1.00 | 217 |
| heavy line | 6 % → 6 % | 17.3 px | 0.26 | 1.00 | 130 |
| pressure swell | 7 % → 7 % | 26.1 px | 0.19 | 1.00 | 84 |
| fast wave | 18 % → 18 % | 21.3 px | 0.18 | 1.00 | 328 |
| slow wave | 23 % → 23 % | 26.7 px | 0.17 | 1.00 | 692 |
| spiral | 30 % → 30 % | 20.0 px | 0.15 | 1.00 | 674 |
| loop | 18 % → 18 % | 23.0 px | 0.16 | 1.00 | 293 |
| tilted | 10 % → 10 % | 26.6 px | 0.22 | 1.00 | 173 |
| over the wet one | 16 % → 16 % | 18.6 px | 0.22 | 1.00 | 131 |
| long, no reload | 32 % → 32 % | 14.6 px | 0.13 | 1.00 | 785 | quarters: 0.01 → 0.00 → 0.00 → 0.00

Numbers say: light vs heavy: width 13.1 → 17.3 px, dark 0.08 → 0.26.

## Acrylic — heavy body
Impasto 0.98 · 30 px · 14.0 s

![Acrylic — heavy body](Acrylic-heavy-body.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 9 % → 7 % | 25.4 px | 0.52 | 0.83 | 90 |
| heavy line | 8 % → 7 % | 24.6 px | 0.52 | 0.88 | 85 |
| pressure swell | 8 % → 7 % | 28.6 px | 0.53 | 0.89 | 68 |
| fast wave | 17 % → 13 % | 19.4 px | 0.52 | 0.78 | 226 |
| slow wave | 19 % → 15 % | 21.6 px | 0.52 | 0.79 | 407 |
| spiral | 24 % → 15 % | 15.8 px | 0.52 | 0.61 | 378 |
| loop | 17 % → 13 % | 22.2 px | 0.52 | 0.78 | 202 |
| tilted | 8 % → 8 % | 23.3 px | 0.53 | 0.99 | 103 |
| over the wet one | 18 % → 15 % | 25.6 px | 0.53 | 0.85 | 103 |
| long, no reload | 31 % → 18 % | 14.0 px | 0.52 | 0.58 | 567 | quarters: 0.26 → 0.16 → 0.11 → 0.09

Numbers say: light vs heavy: width 25.4 → 24.6 px, dark 0.52 → 0.52; pressure barely changes the width.

## Acrylic — fluid
Watercolour 1.00 · 36 px · 29.7 s

![Acrylic — fluid](Acrylic-fluid.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 12 % → 12 % | 33.6 px | 0.24 | 1.01 | 73 |
| heavy line | 18 % → 17 % | 50.9 px | 0.21 | 0.99 | 79 |
| pressure swell | 12 % → 12 % | 45.5 px | 0.23 | 1.01 | 61 |
| fast wave | 39 % → 39 % | 45.1 px | 0.19 | 0.99 | 211 |
| slow wave | 35 % → 35 % | 40.9 px | 0.22 | 1.00 | 328 |
| spiral | 55 % → 54 % | 36.4 px | 0.19 | 0.98 | 332 |
| loop | 31 % → 31 % | 40.0 px | 0.21 | 1.00 | 170 |
| tilted | 13 % → 13 % | 36.0 px | 0.24 | 1.00 | 111 |
| over the wet one | 28 % → 28 % | 42.4 px | 0.24 | 1.01 | 78 |
| long, no reload | 61 % → 58 % | 27.4 px | 0.19 | 0.95 | 494 | quarters: 0.20 → 0.14 → 0.09 → 0.06

Numbers say: light vs heavy: width 33.6 → 50.9 px, dark 0.24 → 0.21.

## Acrylic — palette knife
Impasto 1.00 · 42 px · 18.6 s

![Acrylic — palette knife](Acrylic-palette-knife.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 15 % → 15 % | 44.0 px | 0.39 | 0.98 | 32 |
| heavy line | 15 % → 15 % | 44.3 px | 0.40 | 0.98 | 36 |
| pressure swell | 12 % → 12 % | 43.6 px | 0.42 | 0.99 | 13 |
| fast wave | 36 % → 20 % | 42.0 px | 0.37 | 0.55 | 68 |
| slow wave | 37 % → 21 % | 42.7 px | 0.37 | 0.57 | 127 |
| spiral | 47 % → 18 % | 30.7 px | 0.37 | 0.39 | 104 |
| loop | 32 % → 24 % | 41.3 px | 0.36 | 0.77 | 74 |
| tilted | 12 % → 12 % | 33.7 px | 0.39 | 1.00 | 21 |
| over the wet one | 26 % → 25 % | 39.8 px | 0.39 | 0.97 | 50 |
| long, no reload | 53 % → 20 % | 23.7 px | 0.35 | 0.39 | 167 | quarters: 0.00 → 0.00 → 0.00 → 0.01

Numbers say: light vs heavy: width 44.0 → 44.3 px, dark 0.39 → 0.40; pressure barely changes the width; the long stroke does not run out of paint.

## Finger on oil
Oil 1.00 · 30 px · 12.5 s

![Finger on oil](Finger-on-oil.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 6 % → 6 % | 16.8 px | 0.23 | 1.00 | 60 |
| heavy line | 9 % → 9 % | 27.6 px | 0.28 | 1.00 | 63 |
| pressure swell | 7 % → 7 % | 25.3 px | 0.35 | 1.00 | 60 |
| fast wave | 15 % → 15 % | 17.0 px | 0.12 | 1.00 | 121 |
| slow wave | 16 % → 16 % | 18.6 px | 0.24 | 1.00 | 234 |
| spiral | 28 % → 28 % | 18.2 px | 0.24 | 1.00 | 248 |
| loop | 19 % → 19 % | 24.9 px | 0.28 | 1.00 | 128 |
| tilted | 9 % → 9 % | 26.4 px | 0.28 | 1.00 | 80 |
| over the wet one | 16 % → 16 % | 19.6 px | 0.28 | 1.00 | 32 |
| long, no reload | 36 % → 36 % | 15.9 px | 0.22 | 1.00 | 295 | quarters: 0.12 → 0.11 → 0.07 → 0.04

Numbers say: light vs heavy: width 16.8 → 27.6 px, dark 0.23 → 0.28.

## Palette knife — oil
Oil heavy 0.93 · Impasto 0.07 · 44 px · 18.3 s

![Palette knife — oil](Palette-knife-oil.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 16 % → 14 % | 45.7 px | 0.37 | 0.91 | 38 |
| heavy line | 16 % → 16 % | 46.3 px | 0.38 | 0.98 | 38 |
| pressure swell | 12 % → 12 % | 45.2 px | 0.38 | 0.99 | 16 |
| fast wave | 39 % → 35 % | 44.9 px | 0.35 | 0.89 | 98 |
| slow wave | 39 % → 36 % | 45.4 px | 0.35 | 0.92 | 129 |
| spiral | 62 % → 37 % | 40.7 px | 0.35 | 0.60 | 139 |
| loop | 34 % → 31 % | 43.8 px | 0.36 | 0.92 | 68 |
| tilted | 13 % → 13 % | 36.6 px | 0.37 | 1.00 | 23 |
| over the wet one | 28 % → 27 % | 40.8 px | 0.37 | 0.97 | 27 |
| long, no reload | 74 % → 40 % | 33.0 px | 0.34 | 0.54 | 184 | quarters: 0.00 → 0.00 → 0.01 → 0.01

Numbers say: light vs heavy: width 45.7 → 46.3 px, dark 0.37 → 0.38; pressure barely changes the width; the long stroke does not run out of paint.

## 0.45 · Sponge
Watercolour 0.93 · Ink 0.07 · 46 px · 32.1 s

![0.45 · Sponge](0-45-Sponge.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 27 % → 24 % | 77.5 px | 0.13 | 0.91 | 63 |
| heavy line | 32 % → 28 % | 92.0 px | 0.13 | 0.89 | 88 |
| pressure swell | 24 % → 22 % | 90.9 px | 0.13 | 0.91 | 59 |
| fast wave | 60 % → 54 % | 69.8 px | 0.12 | 0.90 | 203 |
| slow wave | 63 % → 59 % | 72.4 px | 0.17 | 0.94 | 365 |
| spiral | 77 % → 74 % | 51.0 px | 0.16 | 0.96 | 331 |
| loop | 54 % → 51 % | 70.4 px | 0.15 | 0.94 | 165 |
| tilted | 17 % → 17 % | 47.9 px | 0.17 | 1.01 | 113 |
| over the wet one | 45 % → 42 % | 76.8 px | 0.17 | 0.93 | 87 |
| long, no reload | 94 % → 90 % | 42.3 px | 0.17 | 0.96 | 472 | quarters: 0.18 → 0.18 → 0.17 → 0.14

Numbers say: light vs heavy: width 77.5 → 92.0 px, dark 0.13 → 0.13.

## 0.45 · Eraser
Watercolour 1.00 · 30 px · 19.5 s · over bands of wet oil paint and oil pastel in turn (it works on paint already there: look at what it does to the bands; covered counts the bands too)

![0.45 · Eraser](0-45-Eraser.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 24 % → 24 % | 69.2 px | 0.82 | 1.00 | 27 |
| heavy line | 23 % → 23 % | 67.4 px | 0.82 | 1.00 | 38 |
| pressure swell | 23 % → 23 % | 86.8 px | 0.82 | 1.00 | 38 |
| fast wave | 21 % → 21 % | 24.7 px | 0.81 | 1.00 | 117 |
| slow wave | 20 % → 20 % | 23.5 px | 0.82 | 1.00 | 201 |
| spiral | 20 % → 20 % | 13.5 px | 0.79 | 1.00 | 210 |
| loop | 21 % → 21 % | 27.8 px | 0.80 | 1.00 | 155 |
| tilted | 23 % → 23 % | 64.8 px | 0.81 | 1.00 | 56 |
| over the wet one | 22 % → 22 % | 0.0 px | 0.81 | 1.00 | 52 |
| long, no reload | 17 % → 17 % | 7.5 px | 0.79 | 1.00 | 293 | quarters: 0.13 → 0.16 → 0.13 → 0.17

Numbers say: light vs heavy: width 69.2 → 67.4 px, dark 0.82 → 0.82; pressure barely changes the width; the long stroke does not run out of paint.

## Lift wet paint
Watercolour 1.00 · 30 px · 19.4 s · over bands of wet oil paint and oil pastel in turn (it works on paint already there: look at what it does to the bands; covered counts the bands too)

![Lift wet paint](Lift-wet-paint.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 24 % → 24 % | 70.1 px | 0.82 | 1.00 | 32 |
| heavy line | 24 % → 24 % | 69.8 px | 0.82 | 1.00 | 38 |
| pressure swell | 24 % → 24 % | 89.6 px | 0.82 | 1.00 | 25 |
| fast wave | 24 % → 24 % | 27.7 px | 0.82 | 1.00 | 106 |
| slow wave | 24 % → 24 % | 27.7 px | 0.82 | 1.00 | 162 |
| spiral | 24 % → 24 % | 15.9 px | 0.82 | 1.00 | 178 |
| loop | 24 % → 24 % | 31.1 px | 0.82 | 1.00 | 111 |
| tilted | 24 % → 24 % | 66.8 px | 0.82 | 1.00 | 50 |
| over the wet one | 24 % → 24 % | 0.0 px | 0.82 | 1.00 | 45 |
| long, no reload | 24 % → 24 % | 10.7 px | 0.82 | 1.00 | 239 | quarters: 0.18 → 0.24 → 0.17 → 0.24

Numbers say: light vs heavy: width 70.1 → 69.8 px, dark 0.82 → 0.82; pressure barely changes the width; the long stroke does not run out of paint.

## Sgraffito
Watercolour 1.00 · 10 px · 19.7 s · over bands of wet oil paint and oil pastel in turn (it works on paint already there: look at what it does to the bands; covered counts the bands too)

![Sgraffito](Sgraffito.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 24 % → 24 % | 69.9 px | 0.81 | 1.00 | 13 |
| heavy line | 24 % → 24 % | 69.8 px | 0.82 | 1.00 | 6 |
| pressure swell | 24 % → 24 % | 89.6 px | 0.82 | 1.00 | 3 |
| fast wave | 24 % → 24 % | 27.7 px | 0.82 | 1.00 | 21 |
| slow wave | 24 % → 24 % | 27.7 px | 0.82 | 1.00 | 37 |
| spiral | 24 % → 24 % | 15.9 px | 0.82 | 1.00 | 41 |
| loop | 24 % → 24 % | 31.1 px | 0.82 | 1.00 | 21 |
| tilted | 24 % → 24 % | 66.9 px | 0.82 | 1.00 | 7 |
| over the wet one | 24 % → 24 % | 0.0 px | 0.82 | 1.00 | 12 |
| long, no reload | 24 % → 24 % | 10.6 px | 0.82 | 1.00 | 70 | quarters: 0.17 → 0.24 → 0.17 → 0.24

Numbers say: light vs heavy: width 69.9 → 69.8 px, dark 0.81 → 0.82; pressure barely changes the width; the long stroke does not run out of paint.

## Brush Artist · Refs · #01 Henry Ward peach cloud
Gouache 1.00 · 44 px · 26.1 s

![Brush Artist · Refs · #01 Henry Ward peach cloud](Brush-Artist-Refs-01-Henry-Ward-peach-cloud.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 5 % → 0 % | 13.4 px | 0.00 | 0.00 | 95 |
| heavy line | 8 % → 0 % | 22.4 px | 0.32 | 0.01 | 130 |
| pressure swell | 7 % → 3 % | 24.8 px | 0.33 | 0.40 | 103 |
| fast wave | 31 % → 3 % | 36.2 px | 0.27 | 0.09 | 381 |
| slow wave | 20 % → 2 % | 23.3 px | 0.32 | 0.10 | 562 |
| spiral | 33 % → 2 % | 21.6 px | 0.35 | 0.07 | 715 |
| loop | 17 % → 0 % | 22.4 px | 0.32 | 0.01 | 310 |
| tilted | 12 % → 11 % | 32.7 px | 0.25 | 0.97 | 183 |
| over the wet one | 16 % → 2 % | 12.9 px | 0.25 | 0.10 | 126 |
| long, no reload | 30 % → 2 % | 13.6 px | 0.32 | 0.08 | 774 | quarters: 0.03 → 0.03 → 0.03 → 0.03

Numbers say: light vs heavy: width 13.4 → 22.4 px, dark 0.00 → 0.32; the long stroke does not run out of paint.

## Brush Artist · Refs · #02 Henry Ward cream strokes
Gouache 1.00 · 46 px · 29.5 s

![Brush Artist · Refs · #02 Henry Ward cream strokes](Brush-Artist-Refs-02-Henry-Ward-cream-strokes.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 5 % → 0 % | 14.3 px | 0.00 | 0.00 | 105 |
| heavy line | 8 % → 2 % | 24.6 px | 0.41 | 0.22 | 155 |
| pressure swell | 7 % → 3 % | 27.7 px | 0.41 | 0.38 | 106 |
| fast wave | 30 % → 4 % | 34.5 px | 0.36 | 0.15 | 381 |
| slow wave | 21 % → 5 % | 24.3 px | 0.39 | 0.21 | 680 |
| spiral | 43 % → 4 % | 28.4 px | 0.40 | 0.10 | 654 |
| loop | 19 % → 1 % | 24.8 px | 0.39 | 0.04 | 421 |
| tilted | 12 % → 12 % | 33.1 px | 0.34 | 0.98 | 206 |
| over the wet one | 17 % → 1 % | 13.0 px | 0.34 | 0.05 | 159 |
| long, no reload | 25 % → 4 % | 11.1 px | 0.41 | 0.17 | 741 | quarters: 0.03 → 0.04 → 0.03 → 0.04

Numbers say: light vs heavy: width 14.3 → 24.6 px, dark 0.00 → 0.41; the long stroke does not run out of paint.

## Brush Artist · Refs · #03 Henry Ward navy contours
Impasto 1.00 · 22 px · 13.3 s

![Brush Artist · Refs · #03 Henry Ward navy contours](Brush-Artist-Refs-03-Henry-Ward-navy-contours.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 7 % → 6 % | 19.4 px | 0.72 | 0.90 | 69 |
| heavy line | 6 % → 6 % | 18.3 px | 0.71 | 0.92 | 72 |
| pressure swell | 5 % → 5 % | 20.1 px | 0.75 | 0.89 | 60 |
| fast wave | 16 % → 11 % | 18.3 px | 0.76 | 0.71 | 210 |
| slow wave | 18 % → 14 % | 20.5 px | 0.72 | 0.78 | 328 |
| spiral | 28 % → 13 % | 18.3 px | 0.68 | 0.47 | 366 |
| loop | 13 % → 11 % | 17.0 px | 0.71 | 0.83 | 184 |
| tilted | 7 % → 7 % | 20.7 px | 0.73 | 0.99 | 102 |
| over the wet one | 15 % → 13 % | 20.4 px | 0.73 | 0.88 | 97 |
| long, no reload | 32 % → 13 % | 14.4 px | 0.71 | 0.41 | 447 | quarters: 0.33 → 0.27 → 0.19 → 0.08

Numbers say: light vs heavy: width 19.4 → 18.3 px, dark 0.72 → 0.71; pressure barely changes the width.

## Brush Artist · Refs · #04 Henry Ward grey cloud
Gouache 1.00 · 50 px · 30.0 s

![Brush Artist · Refs · #04 Henry Ward grey cloud](Brush-Artist-Refs-04-Henry-Ward-grey-cloud.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 5 % → 0 % | 14.6 px | 0.00 | 0.00 | 111 |
| heavy line | 10 % → 2 % | 28.3 px | 0.31 | 0.25 | 154 |
| pressure swell | 7 % → 2 % | 24.5 px | 0.31 | 0.36 | 140 |
| fast wave | 32 % → 4 % | 37.5 px | 0.24 | 0.14 | 433 |
| slow wave | 23 % → 2 % | 26.3 px | 0.33 | 0.10 | 666 |
| spiral | 47 % → 3 % | 30.8 px | 0.37 | 0.06 | 729 |
| loop | 19 % → 0 % | 25.2 px | 0.00 | 0.00 | 345 |
| tilted | 12 % → 12 % | 33.3 px | 0.24 | 0.98 | 237 |
| over the wet one | 17 % → 3 % | 14.1 px | 0.24 | 0.17 | 138 |
| long, no reload | 22 % → 4 % | 9.9 px | 0.34 | 0.17 | 815 | quarters: 0.03 → 0.04 → 0.04 → 0.04

Numbers say: light vs heavy: width 14.6 → 28.3 px, dark 0.00 → 0.31; the long stroke does not run out of paint.

## Brush Artist · Refs · #05 Henry Ward green in rust loops
Impasto 1.00 · 20 px · 13.3 s

![Brush Artist · Refs · #05 Henry Ward green in rust loops](Brush-Artist-Refs-05-Henry-Ward-green-in-rust-loops.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 6 % → 6 % | 18.5 px | 0.56 | 0.88 | 76 |
| heavy line | 8 % → 7 % | 22.1 px | 0.56 | 0.87 | 73 |
| pressure swell | 4 % → 4 % | 16.1 px | 0.58 | 0.93 | 59 |
| fast wave | 16 % → 10 % | 17.9 px | 0.56 | 0.67 | 222 |
| slow wave | 16 % → 12 % | 19.1 px | 0.56 | 0.74 | 274 |
| spiral | 24 % → 11 % | 16.1 px | 0.53 | 0.46 | 346 |
| loop | 15 % → 12 % | 19.7 px | 0.56 | 0.79 | 185 |
| tilted | 7 % → 7 % | 19.8 px | 0.58 | 0.99 | 97 |
| over the wet one | 14 % → 12 % | 18.1 px | 0.58 | 0.85 | 101 |
| long, no reload | 28 % → 12 % | 12.6 px | 0.55 | 0.41 | 472 | quarters: 0.23 → 0.17 → 0.11 → 0.04

Numbers say: light vs heavy: width 18.5 → 22.1 px, dark 0.56 → 0.56.

## Brush Artist · Refs · #06 Henry Ward scrubbed grey
Gouache 1.00 · 50 px · 29.5 s

![Brush Artist · Refs · #06 Henry Ward scrubbed grey](Brush-Artist-Refs-06-Henry-Ward-scrubbed-grey.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 5 % → 0 % | 14.6 px | 0.00 | 0.00 | 127 |
| heavy line | 10 % → 2 % | 28.3 px | 0.33 | 0.25 | 152 |
| pressure swell | 7 % → 2 % | 24.5 px | 0.33 | 0.36 | 115 |
| fast wave | 32 % → 4 % | 37.5 px | 0.25 | 0.14 | 448 |
| slow wave | 23 % → 2 % | 26.3 px | 0.34 | 0.10 | 683 |
| spiral | 47 % → 3 % | 30.8 px | 0.38 | 0.06 | 667 |
| loop | 19 % → 0 % | 25.2 px | 0.00 | 0.00 | 318 |
| tilted | 12 % → 12 % | 33.3 px | 0.25 | 0.98 | 259 |
| over the wet one | 17 % → 3 % | 14.1 px | 0.25 | 0.17 | 156 |
| long, no reload | 22 % → 4 % | 9.9 px | 0.36 | 0.17 | 873 | quarters: 0.03 → 0.04 → 0.04 → 0.04

Numbers say: light vs heavy: width 14.6 → 28.3 px, dark 0.00 → 0.33; the long stroke does not run out of paint.

## Brush Artist · Refs · #07 Henry Ward blue L + black zigzag
Impasto 1.00 · 34 px · 15.9 s

![Brush Artist · Refs · #07 Henry Ward blue L + black zigzag](Brush-Artist-Refs-07-Henry-Ward-blue-L-black-zigzag.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 10 % → 9 % | 30.2 px | 0.59 | 0.86 | 108 |
| heavy line | 11 % → 10 % | 30.8 px | 0.59 | 0.93 | 100 |
| pressure swell | 8 % → 8 % | 31.6 px | 0.59 | 0.92 | 90 |
| fast wave | 25 % → 19 % | 28.8 px | 0.60 | 0.77 | 276 |
| slow wave | 26 % → 20 % | 29.7 px | 0.57 | 0.76 | 454 |
| spiral | 44 % → 23 % | 29.1 px | 0.54 | 0.52 | 484 |
| loop | 24 % → 19 % | 30.4 px | 0.57 | 0.80 | 201 |
| tilted | 11 % → 11 % | 29.8 px | 0.61 | 1.00 | 118 |
| over the wet one | 22 % → 20 % | 32.0 px | 0.61 | 0.90 | 118 |
| long, no reload | 50 % → 23 % | 22.5 px | 0.57 | 0.46 | 680 | quarters: 0.36 → 0.31 → 0.21 → 0.10

Numbers say: light vs heavy: width 30.2 → 30.8 px, dark 0.59 → 0.59; pressure barely changes the width.

## Brush Artist · Refs · #08 Henry Ward olive bands
Gouache 1.00 · 34 px · 22.2 s

![Brush Artist · Refs · #08 Henry Ward olive bands](Brush-Artist-Refs-08-Henry-Ward-olive-bands.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 2 % → 0 % | 5.8 px | 0.00 | 0.00 | 44 |
| heavy line | 7 % → 1 % | 19.2 px | 0.61 | 0.15 | 141 |
| pressure swell | 5 % → 1 % | 19.1 px | 0.61 | 0.20 | 79 |
| fast wave | 18 % → 1 % | 21.1 px | 0.59 | 0.04 | 266 |
| slow wave | 16 % → 0 % | 18.3 px | 0.63 | 0.02 | 470 |
| spiral | 27 % → 0 % | 17.5 px | 0.52 | 0.01 | 428 |
| loop | 10 % → 1 % | 13.5 px | 0.61 | 0.12 | 224 |
| tilted | 7 % → 7 % | 20.5 px | 0.65 | 0.92 | 127 |
| over the wet one | 11 % → 1 % | 9.8 px | 0.65 | 0.12 | 96 |
| long, no reload | 23 % → 2 % | 10.4 px | 0.53 | 0.10 | 630 | quarters: 0.21 → 0.11 → 0.12 → 0.08

Numbers say: light vs heavy: width 5.8 → 19.2 px, dark 0.00 → 0.61.

## Brush Artist · Refs · #09 Henry Ward white loops
Gouache 1.00 · 46 px · 31.1 s

![Brush Artist · Refs · #09 Henry Ward white loops](Brush-Artist-Refs-09-Henry-Ward-white-loops.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 5 % → 0 % | 14.3 px | 0.00 | 0.00 | 127 |
| heavy line | 8 % → 2 % | 24.6 px | 0.43 | 0.22 | 133 |
| pressure swell | 7 % → 3 % | 27.7 px | 0.43 | 0.38 | 98 |
| fast wave | 30 % → 4 % | 34.5 px | 0.38 | 0.15 | 385 |
| slow wave | 21 % → 5 % | 24.3 px | 0.40 | 0.21 | 628 |
| spiral | 43 % → 4 % | 28.4 px | 0.41 | 0.10 | 713 |
| loop | 19 % → 1 % | 24.8 px | 0.41 | 0.04 | 315 |
| tilted | 12 % → 12 % | 33.1 px | 0.37 | 0.98 | 244 |
| over the wet one | 17 % → 1 % | 13.0 px | 0.37 | 0.05 | 180 |
| long, no reload | 25 % → 4 % | 11.1 px | 0.41 | 0.17 | 838 | quarters: 0.03 → 0.04 → 0.04 → 0.04

Numbers say: light vs heavy: width 14.3 → 24.6 px, dark 0.00 → 0.43; the long stroke does not run out of paint.

## Brush Artist · Refs · #10 Henry Ward maroon loops
Impasto 1.00 · 30 px · 16.1 s

![Brush Artist · Refs · #10 Henry Ward maroon loops](Brush-Artist-Refs-10-Henry-Ward-maroon-loops.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 10 % → 8 % | 27.9 px | 0.73 | 0.88 | 83 |
| heavy line | 11 % → 10 % | 32.1 px | 0.73 | 0.90 | 93 |
| pressure swell | 8 % → 7 % | 29.7 px | 0.74 | 0.91 | 73 |
| fast wave | 23 % → 17 % | 26.5 px | 0.76 | 0.76 | 217 |
| slow wave | 22 % → 19 % | 25.9 px | 0.72 | 0.85 | 380 |
| spiral | 37 % → 18 % | 24.2 px | 0.72 | 0.50 | 407 |
| loop | 17 % → 15 % | 22.1 px | 0.73 | 0.86 | 205 |
| tilted | 10 % → 10 % | 27.6 px | 0.73 | 1.00 | 107 |
| over the wet one | 19 % → 17 % | 26.8 px | 0.73 | 0.86 | 115 |
| long, no reload | 40 % → 17 % | 18.0 px | 0.71 | 0.43 | 633 | quarters: 0.38 → 0.33 → 0.27 → 0.18

Numbers say: light vs heavy: width 27.9 → 32.1 px, dark 0.73 → 0.73.

## Brush Artist · Refs · #11 Henry Ward purple spun balls
Impasto 1.00 · 36 px · 17.3 s

![Brush Artist · Refs · #11 Henry Ward purple spun balls](Brush-Artist-Refs-11-Henry-Ward-purple-spun-balls.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 11 % → 10 % | 31.5 px | 0.74 | 0.93 | 112 |
| heavy line | 11 % → 10 % | 30.5 px | 0.74 | 0.95 | 114 |
| pressure swell | 10 % → 9 % | 36.4 px | 0.75 | 0.92 | 82 |
| fast wave | 27 % → 21 % | 31.1 px | 0.74 | 0.78 | 298 |
| slow wave | 30 % → 24 % | 34.6 px | 0.73 | 0.82 | 604 |
| spiral | 40 % → 24 % | 26.5 px | 0.70 | 0.59 | 520 |
| loop | 24 % → 21 % | 30.7 px | 0.75 | 0.90 | 243 |
| tilted | 10 % → 10 % | 28.5 px | 0.73 | 1.00 | 138 |
| over the wet one | 22 % → 20 % | 33.9 px | 0.73 | 0.91 | 143 |
| long, no reload | 53 % → 25 % | 23.9 px | 0.74 | 0.46 | 897 | quarters: 0.50 → 0.45 → 0.38 → 0.27

Numbers say: light vs heavy: width 31.5 → 30.5 px, dark 0.74 → 0.74; pressure barely changes the width.

## Brush Artist · Refs · #12 Henry Ward black-olive cage
Gouache 1.00 · 28 px · 22.6 s

![Brush Artist · Refs · #12 Henry Ward black-olive cage](Brush-Artist-Refs-12-Henry-Ward-black-olive-cage.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 2 % → 0 % | 6.3 px | 0.00 | 0.00 | 58 |
| heavy line | 6 % → 1 % | 16.9 px | 0.64 | 0.21 | 134 |
| pressure swell | 5 % → 1 % | 17.2 px | 0.64 | 0.22 | 124 |
| fast wave | 14 % → 0 % | 16.6 px | 0.00 | 0.00 | 210 |
| slow wave | 14 % → 1 % | 15.6 px | 0.64 | 0.07 | 409 |
| spiral | 18 % → 0 % | 11.7 px | 0.63 | 0.02 | 505 |
| loop | 11 % → 1 % | 14.3 px | 0.63 | 0.10 | 231 |
| tilted | 6 % → 6 % | 17.8 px | 0.68 | 0.92 | 145 |
| over the wet one | 10 % → 0 % | 9.7 px | 0.68 | 0.04 | 117 |
| long, no reload | 18 % → 2 % | 8.0 px | 0.59 | 0.12 | 579 | quarters: 0.15 → 0.12 → 0.06 → 0.02

Numbers say: light vs heavy: width 6.3 → 16.9 px, dark 0.00 → 0.64.

## Brush Artist · Refs · #13 Henry Ward blue streaky form
Gouache 1.00 · 50 px · 30.0 s

![Brush Artist · Refs · #13 Henry Ward blue streaky form](Brush-Artist-Refs-13-Henry-Ward-blue-streaky-form.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 5 % → 0 % | 14.6 px | 0.00 | 0.00 | 137 |
| heavy line | 10 % → 2 % | 28.3 px | 0.33 | 0.25 | 143 |
| pressure swell | 7 % → 2 % | 24.5 px | 0.33 | 0.36 | 106 |
| fast wave | 32 % → 4 % | 37.5 px | 0.25 | 0.14 | 612 |
| slow wave | 23 % → 2 % | 26.3 px | 0.34 | 0.10 | 793 |
| spiral | 47 % → 3 % | 30.8 px | 0.38 | 0.06 | 762 |
| loop | 19 % → 0 % | 25.2 px | 0.00 | 0.00 | 331 |
| tilted | 12 % → 12 % | 33.3 px | 0.25 | 0.98 | 240 |
| over the wet one | 17 % → 3 % | 14.1 px | 0.25 | 0.17 | 147 |
| long, no reload | 22 % → 4 % | 9.9 px | 0.35 | 0.17 | 869 | quarters: 0.03 → 0.04 → 0.04 → 0.04

Numbers say: light vs heavy: width 14.6 → 28.3 px, dark 0.00 → 0.33; the long stroke does not run out of paint.

## Brush Artist · Refs · #14 Henry Ward olive totem
Impasto 1.00 · 48 px · 19.3 s

![Brush Artist · Refs · #14 Henry Ward olive totem](Brush-Artist-Refs-14-Henry-Ward-olive-totem.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 15 % → 14 % | 44.4 px | 0.31 | 0.91 | 147 |
| heavy line | 16 % → 15 % | 46.3 px | 0.31 | 0.95 | 149 |
| pressure swell | 12 % → 11 % | 44.0 px | 0.31 | 0.93 | 123 |
| fast wave | 36 % → 28 % | 41.7 px | 0.36 | 0.78 | 444 |
| slow wave | 37 % → 32 % | 42.3 px | 0.30 | 0.87 | 1073 |
| spiral | 59 % → 35 % | 38.7 px | 0.28 | 0.59 | 745 |
| loop | 30 % → 27 % | 39.1 px | 0.29 | 0.89 | 364 |
| tilted | 13 % → 13 % | 36.4 px | 0.33 | 1.00 | 146 |
| over the wet one | 28 % → 25 % | 40.5 px | 0.33 | 0.92 | 171 |
| long, no reload | 61 % → 31 % | 27.3 px | 0.27 | 0.52 | 933 | quarters: 0.20 → 0.15 → 0.09 → 0.04

Numbers say: light vs heavy: width 44.4 → 46.3 px, dark 0.31 → 0.31; pressure barely changes the width.

## Brush Artist · Refs · #15 Ultramarine brush script
Ink 1.00 · 4 px · 21.8 s

![Brush Artist · Refs · #15 Ultramarine brush script](Brush-Artist-Refs-15-Ultramarine-brush-script.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 1 % → 3 % | 2.1 px | 0.55 | 3.99 | 44 |
| heavy line | 5 % → 5 % | 15.6 px | 0.62 | 1.00 | 58 |
| pressure swell | 3 % → 4 % | 11.0 px | 0.62 | 1.21 | 40 |
| fast wave | 9 % → 7 % | 10.2 px | 0.54 | 0.81 | 89 |
| slow wave | 8 % → 7 % | 8.8 px | 0.53 | 0.89 | 87 |
| spiral | 11 % → 8 % | 7.3 px | 0.53 | 0.68 | 116 |
| loop | 7 % → 7 % | 9.4 px | 0.54 | 0.96 | 94 |
| tilted | 3 % → 3 % | 7.4 px | 0.64 | 1.04 | 35 |
| over the wet one | 7 % → 7 % | 10.7 px | 0.64 | 1.08 | 36 |
| long, no reload | 16 % → 7 % | 7.1 px | 0.51 | 0.47 | 255 | quarters: 0.14 → 0.04 → 0.01 → 0.00

Numbers say: light vs heavy: width 2.1 → 15.6 px, dark 0.55 → 0.62; wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #18 Blue oil-stick scribbles
Pastel 1.00 · 10 px · 9.9 s

![Brush Artist · Refs · #18 Blue oil-stick scribbles](Brush-Artist-Refs-18-Blue-oil-stick-scribbles.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 1 % → 1 % | 2.9 px | 0.53 | 1.00 | 21 |
| heavy line | 2 % → 2 % | 6.0 px | 0.53 | 1.00 | 28 |
| pressure swell | 1 % → 1 % | 5.5 px | 0.52 | 1.00 | 20 |
| fast wave | 5 % → 5 % | 5.3 px | 0.53 | 1.00 | 73 |
| slow wave | 4 % → 4 % | 5.2 px | 0.53 | 1.00 | 65 |
| spiral | 7 % → 7 % | 4.4 px | 0.52 | 1.00 | 111 |
| loop | 4 % → 4 % | 4.6 px | 0.52 | 1.00 | 40 |
| tilted | 2 % → 2 % | 4.4 px | 0.53 | 1.00 | 40 |
| over the wet one | 3 % → 3 % | 4.8 px | 0.53 | 1.00 | 22 |
| long, no reload | 9 % → 9 % | 4.2 px | 0.52 | 1.00 | 199 | quarters: 0.05 → 0.05 → 0.06 → 0.06

Numbers say: light vs heavy: width 2.9 → 6.0 px, dark 0.53 → 0.53; the long stroke does not run out of paint.

## Brush Artist · Refs · #20 Orange-red crayon scribble
Pastel 1.00 · 14 px · 10.1 s

![Brush Artist · Refs · #20 Orange-red crayon scribble](Brush-Artist-Refs-20-Orange-red-crayon-scribble.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 1 % → 1 % | 3.8 px | 0.53 | 1.00 | 23 |
| heavy line | 3 % → 3 % | 8.0 px | 0.53 | 1.00 | 24 |
| pressure swell | 2 % → 2 % | 7.6 px | 0.55 | 1.00 | 18 |
| fast wave | 6 % → 6 % | 7.3 px | 0.56 | 1.00 | 76 |
| slow wave | 6 % → 6 % | 6.9 px | 0.53 | 1.00 | 81 |
| spiral | 9 % → 9 % | 6.0 px | 0.54 | 1.00 | 107 |
| loop | 5 % → 5 % | 6.1 px | 0.54 | 1.00 | 55 |
| tilted | 2 % → 2 % | 5.6 px | 0.55 | 1.00 | 34 |
| over the wet one | 4 % → 4 % | 6.2 px | 0.55 | 1.00 | 22 |
| long, no reload | 12 % → 12 % | 5.4 px | 0.53 | 1.00 | 161 | quarters: 0.07 → 0.07 → 0.07 → 0.07

Numbers say: light vs heavy: width 3.8 → 8.0 px, dark 0.53 → 0.53; the long stroke does not run out of paint.

## Brush Artist · Refs · #21 Gritty black contours
Gouache 1.00 · 12 px · 18.5 s

![Brush Artist · Refs · #21 Gritty black contours](Brush-Artist-Refs-21-Gritty-black-contours.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 1 % → 0 % | 3.2 px | 0.00 | 0.00 | 57 |
| heavy line | 2 % → 0 % | 6.0 px | 0.00 | 0.00 | 97 |
| pressure swell | 1 % → 0 % | 5.6 px | 0.00 | 0.00 | 68 |
| fast wave | 4 % → 0 % | 4.9 px | 0.00 | 0.00 | 230 |
| slow wave | 4 % → 0 % | 5.1 px | 0.81 | 0.01 | 202 |
| spiral | 7 % → 0 % | 4.6 px | 0.75 | 0.03 | 334 |
| loop | 4 % → 0 % | 5.5 px | 0.80 | 0.09 | 244 |
| tilted | 3 % → 2 % | 7.7 px | 0.66 | 0.84 | 111 |
| over the wet one | 3 % → 0 % | 2.1 px | 0.66 | 0.01 | 100 |
| long, no reload | 5 % → 0 % | 2.2 px | 0.76 | 0.00 | 467 | quarters: 0.07 → 0.03 → 0.03 → 0.02

Numbers say: light vs heavy: width 3.2 → 6.0 px, dark 0.00 → 0.00.

## Brush Artist · Refs · #22 Bold black brush poster
Ink 1.00 · 20 px · 26.7 s

![Brush Artist · Refs · #22 Bold black brush poster](Brush-Artist-Refs-22-Bold-black-brush-poster.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 4 % → 5 % | 10.3 px | 0.79 | 1.52 | 33 |
| heavy line | 15 % → 14 % | 42.6 px | 0.88 | 0.99 | 90 |
| pressure swell | 9 % → 9 % | 33.6 px | 0.87 | 1.03 | 63 |
| fast wave | 28 % → 27 % | 32.3 px | 0.88 | 0.98 | 155 |
| slow wave | 23 % → 23 % | 27.0 px | 0.87 | 0.98 | 212 |
| spiral | 35 % → 32 % | 23.0 px | 0.87 | 0.92 | 247 |
| loop | 22 % → 22 % | 28.2 px | 0.88 | 1.00 | 176 |
| tilted | 9 % → 9 % | 24.2 px | 0.88 | 1.00 | 92 |
| over the wet one | 20 % → 20 % | 30.8 px | 0.88 | 1.00 | 58 |
| long, no reload | 48 % → 38 % | 21.3 px | 0.85 | 0.79 | 357 | quarters: 0.56 → 0.45 → 0.35 → 0.26

Numbers say: light vs heavy: width 10.3 → 42.6 px, dark 0.79 → 0.88; wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #23 Dry white on orange + black line
Gouache 1.00 · 50 px · 22.6 s

![Brush Artist · Refs · #23 Dry white on orange + black line](Brush-Artist-Refs-23-Dry-white-on-orange-black-line.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 3 % → 0 % | 9.9 px | 0.00 | 0.00 | 82 |
| heavy line | 9 % → 2 % | 26.8 px | 0.42 | 0.20 | 206 |
| pressure swell | 7 % → 0 % | 24.9 px | 0.41 | 0.03 | 130 |
| fast wave | 25 % → 0 % | 28.6 px | 0.00 | 0.00 | 496 |
| slow wave | 24 % → 1 % | 27.6 px | 0.40 | 0.02 | 591 |
| spiral | 33 % → 1 % | 21.5 px | 0.40 | 0.02 | 557 |
| loop | 20 % → 0 % | 26.0 px | 0.39 | 0.00 | 306 |
| tilted | 10 % → 9 % | 28.2 px | 0.38 | 0.93 | 172 |
| over the wet one | 15 % → 1 % | 13.1 px | 0.38 | 0.05 | 139 |
| long, no reload | 30 % → 4 % | 13.5 px | 0.40 | 0.12 | 890 | quarters: 0.02 → 0.03 → 0.03 → 0.03

Numbers say: light vs heavy: width 9.9 → 26.8 px, dark 0.00 → 0.42; the long stroke does not run out of paint.

## Brush Artist · Refs · #24 Picasso flat oil
Oil 0.89 · Oil glaze 0.11 · 34 px · 14.7 s

![Brush Artist · Refs · #24 Picasso flat oil](Brush-Artist-Refs-24-Picasso-flat-oil.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 10 % → 10 % | 28.8 px | 0.39 | 1.00 | 108 |
| heavy line | 11 % → 11 % | 32.5 px | 0.39 | 1.00 | 131 |
| pressure swell | 8 % → 8 % | 31.7 px | 0.38 | 1.00 | 89 |
| fast wave | 30 % → 30 % | 35.2 px | 0.39 | 1.00 | 439 |
| slow wave | 28 % → 28 % | 32.8 px | 0.38 | 1.00 | 667 |
| spiral | 42 % → 42 % | 27.8 px | 0.38 | 1.00 | 503 |
| loop | 22 % → 22 % | 28.8 px | 0.40 | 1.00 | 269 |
| tilted | 11 % → 11 % | 31.3 px | 0.41 | 1.00 | 182 |
| over the wet one | 20 % → 20 % | 25.3 px | 0.41 | 1.00 | 128 |
| long, no reload | 58 % → 58 % | 26.0 px | 0.32 | 1.00 | 763 | quarters: 0.23 → 0.22 → 0.19 → 0.17

Numbers say: light vs heavy: width 28.8 → 32.5 px, dark 0.39 → 0.39.

## Brush Artist · Refs · #25 Yellow heavy flat stroke
Impasto 1.00 · 110 px · 36.7 s

![Brush Artist · Refs · #25 Yellow heavy flat stroke](Brush-Artist-Refs-25-Yellow-heavy-flat-stroke.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 35 % → 35 % | 101.0 px | 0.31 | 1.00 | 552 |
| heavy line | 36 % → 35 % | 104.1 px | 0.31 | 0.97 | 415 |
| pressure swell | 28 % → 29 % | 104.0 px | 0.28 | 1.05 | 297 |
| fast wave | 72 % → 75 % | 82.8 px | 0.25 | 1.04 | 1150 |
| slow wave | 72 % → 71 % | 83.7 px | 0.30 | 0.98 | 1973 |
| spiral | 86 % → 81 % | 56.5 px | 0.30 | 0.94 | 2155 |
| loop | 64 % → 63 % | 82.7 px | 0.31 | 0.99 | 977 |
| tilted | 25 % → 25 % | 70.3 px | 0.28 | 1.00 | 583 |
| over the wet one | 55 % → 53 % | 83.3 px | 0.28 | 0.97 | 498 |
| long, no reload | 98 % → 96 % | 43.9 px | 0.31 | 0.98 | 2820 | quarters: 0.00 → 0.00 → 0.00 → 0.00

Numbers say: light vs heavy: width 101.0 → 104.1 px, dark 0.31 → 0.31; pressure barely changes the width; the long stroke does not run out of paint.

## Brush Artist · Refs · #27 Orange impasto swatch
Impasto 1.00 · 60 px · 22.2 s

![Brush Artist · Refs · #27 Orange impasto swatch](Brush-Artist-Refs-27-Orange-impasto-swatch.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 18 % → 18 % | 52.9 px | 0.34 | 0.97 | 233 |
| heavy line | 21 % → 20 % | 60.0 px | 0.34 | 0.95 | 187 |
| pressure swell | 15 % → 15 % | 57.8 px | 0.36 | 0.97 | 138 |
| fast wave | 48 % → 46 % | 55.2 px | 0.37 | 0.97 | 544 |
| slow wave | 46 % → 45 % | 53.6 px | 0.33 | 0.97 | 896 |
| spiral | 68 % → 61 % | 45.1 px | 0.34 | 0.89 | 918 |
| loop | 40 % → 39 % | 51.8 px | 0.33 | 0.97 | 446 |
| tilted | 16 % → 16 % | 43.7 px | 0.35 | 1.00 | 402 |
| over the wet one | 34 % → 32 % | 50.0 px | 0.35 | 0.97 | 230 |
| long, no reload | 84 % → 76 % | 37.8 px | 0.32 | 0.90 | 1371 | quarters: 0.30 → 0.29 → 0.28 → 0.25

Numbers say: light vs heavy: width 52.9 → 60.0 px, dark 0.34 → 0.34.

## Brush Artist · Refs · #28 Miles Davis black lines
Ink 1.00 · 22 px · 27.0 s

![Brush Artist · Refs · #28 Miles Davis black lines](Brush-Artist-Refs-28-Miles-Davis-black-lines.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 4 % → 6 % | 12.3 px | 0.80 | 1.40 | 29 |
| heavy line | 16 % → 16 % | 45.9 px | 0.88 | 0.99 | 86 |
| pressure swell | 10 % → 10 % | 36.7 px | 0.87 | 1.03 | 47 |
| fast wave | 29 % → 29 % | 33.8 px | 0.88 | 0.99 | 129 |
| slow wave | 27 % → 26 % | 30.7 px | 0.88 | 0.99 | 224 |
| spiral | 39 % → 36 % | 25.4 px | 0.87 | 0.93 | 241 |
| loop | 24 % → 24 % | 31.0 px | 0.88 | 1.00 | 134 |
| tilted | 9 % → 9 % | 26.0 px | 0.88 | 1.01 | 78 |
| over the wet one | 21 % → 21 % | 32.9 px | 0.88 | 1.00 | 144 |
| long, no reload | 53 % → 45 % | 23.9 px | 0.85 | 0.83 | 366 | quarters: 0.61 → 0.53 → 0.41 → 0.31

Numbers say: light vs heavy: width 12.3 → 45.9 px, dark 0.80 → 0.88.

## Brush Artist · Refs · #29 Shrigley magenta asterisk
Watercolour 1.00 · 70 px · 31.6 s

![Brush Artist · Refs · #29 Shrigley magenta asterisk](Brush-Artist-Refs-29-Shrigley-magenta-asterisk.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 10 % → 13 % | 28.0 px | 0.61 | 1.39 | 54 |
| heavy line | 17 % → 18 % | 50.3 px | 0.61 | 1.04 | 123 |
| pressure swell | 11 % → 13 % | 41.1 px | 0.62 | 1.14 | 80 |
| fast wave | 38 % → 38 % | 43.8 px | 0.60 | 1.01 | 252 |
| slow wave | 35 % → 39 % | 41.0 px | 0.62 | 1.11 | 416 |
| spiral | 61 % → 61 % | 40.0 px | 0.60 | 1.01 | 434 |
| loop | 31 % → 32 % | 40.2 px | 0.61 | 1.03 | 261 |
| tilted | 18 % → 18 % | 49.0 px | 0.61 | 1.00 | 195 |
| over the wet one | 31 % → 34 % | 38.5 px | 0.61 | 1.08 | 101 |
| long, no reload | 75 % → 76 % | 33.6 px | 0.60 | 1.01 | 671 | quarters: 0.53 → 0.50 → 0.48 → 0.45

Numbers say: light vs heavy: width 28.0 → 50.3 px, dark 0.61 → 0.61; the long stroke does not run out of paint.

## Brush Artist · Refs · #30 Red gouache face patch
Gouache 1.00 · 60 px · 42.5 s

![Brush Artist · Refs · #30 Red gouache face patch](Brush-Artist-Refs-30-Red-gouache-face-patch.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 16 % → 14 % | 45.5 px | 0.49 | 0.87 | 147 |
| heavy line | 25 % → 19 % | 71.4 px | 0.49 | 0.78 | 217 |
| pressure swell | 20 % → 17 % | 74.8 px | 0.50 | 0.84 | 160 |
| fast wave | 48 % → 28 % | 55.1 px | 0.51 | 0.58 | 507 |
| slow wave | 50 % → 31 % | 57.3 px | 0.48 | 0.62 | 814 |
| spiral | 59 % → 30 % | 39.0 px | 0.48 | 0.50 | 815 |
| loop | 40 % → 28 % | 51.4 px | 0.48 | 0.71 | 404 |
| tilted | 17 % → 17 % | 46.7 px | 0.50 | 1.00 | 307 |
| over the wet one | 37 % → 32 % | 55.9 px | 0.50 | 0.87 | 190 |
| long, no reload | 66 % → 28 % | 29.6 px | 0.46 | 0.42 | 1275 | quarters: 0.40 → 0.36 → 0.31 → 0.26

Numbers say: light vs heavy: width 45.5 → 71.4 px, dark 0.49 → 0.49.

## Brush Artist · Refs · #31 Warhol blotted line
Ink 1.00 · 6 px · 22.4 s

![Brush Artist · Refs · #31 Warhol blotted line](Brush-Artist-Refs-31-Warhol-blotted-line.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 1 % → 4 % | 3.0 px | 0.72 | 3.49 | 26 |
| heavy line | 7 % → 7 % | 19.5 px | 0.84 | 0.98 | 71 |
| pressure swell | 4 % → 4 % | 14.2 px | 0.82 | 1.18 | 36 |
| fast wave | 12 % → 9 % | 13.6 px | 0.81 | 0.73 | 102 |
| slow wave | 11 % → 9 % | 12.3 px | 0.80 | 0.80 | 103 |
| spiral | 15 % → 9 % | 10.0 px | 0.79 | 0.58 | 181 |
| loop | 10 % → 9 % | 12.6 px | 0.80 | 0.94 | 87 |
| tilted | 4 % → 4 % | 11.0 px | 0.83 | 1.03 | 49 |
| over the wet one | 9 % → 9 % | 14.0 px | 0.83 | 1.05 | 42 |
| long, no reload | 21 % → 10 % | 9.5 px | 0.78 | 0.45 | 256 | quarters: 0.25 → 0.13 → 0.05 → 0.01

Numbers say: light vs heavy: width 3.0 → 19.5 px, dark 0.72 → 0.84; wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #32 Thick orange swipes
Impasto 1.00 · 90 px · 33.2 s

![Brush Artist · Refs · #32 Thick orange swipes](Brush-Artist-Refs-32-Thick-orange-swipes.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 29 % → 28 % | 83.5 px | 0.37 | 0.99 | 301 |
| heavy line | 30 % → 29 % | 86.8 px | 0.37 | 0.97 | 281 |
| pressure swell | 23 % → 23 % | 84.8 px | 0.38 | 1.01 | 229 |
| fast wave | 64 % → 65 % | 74.2 px | 0.39 | 1.02 | 861 |
| slow wave | 64 % → 62 % | 73.9 px | 0.37 | 0.97 | 1429 |
| spiral | 80 % → 75 % | 52.6 px | 0.35 | 0.94 | 1964 |
| loop | 56 % → 55 % | 73.0 px | 0.36 | 0.97 | 842 |
| tilted | 21 % → 21 % | 58.8 px | 0.38 | 1.00 | 456 |
| over the wet one | 46 % → 45 % | 70.6 px | 0.38 | 0.96 | 352 |
| long, no reload | 95 % → 92 % | 42.8 px | 0.36 | 0.97 | 2188 | quarters: 0.35 → 0.35 → 0.35 → 0.34

Numbers say: light vs heavy: width 83.5 → 86.8 px, dark 0.37 → 0.37; pressure barely changes the width; the long stroke does not run out of paint.

## Brush Artist · Refs · #33 Red wet-in-wet band
Watercolour 1.00 · 80 px · 50.8 s

![Brush Artist · Refs · #33 Red wet-in-wet band](Brush-Artist-Refs-33-Red-wet-in-wet-band.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 24 % → 42 % | 69.3 px | 0.54 | 1.75 | 132 |
| heavy line | 33 % → 48 % | 96.9 px | 0.55 | 1.45 | 249 |
| pressure swell | 19 % → 30 % | 72.1 px | 0.57 | 1.56 | 146 |
| fast wave | 65 % → 79 % | 75.5 px | 0.60 | 1.21 | 439 |
| slow wave | 61 % → 78 % | 70.5 px | 0.63 | 1.28 | 837 |
| spiral | 77 % → 89 % | 50.8 px | 0.64 | 1.15 | 929 |
| loop | 54 % → 67 % | 70.5 px | 0.62 | 1.23 | 457 |
| tilted | 28 % → 30 % | 78.0 px | 0.58 | 1.09 | 262 |
| over the wet one | 55 % → 79 % | 76.7 px | 0.58 | 1.43 | 204 |
| long, no reload | 96 % → 99 % | 42.9 px | 0.66 | 1.04 | 1215 | quarters: 0.68 → 0.68 → 0.68 → 0.64

Numbers say: light vs heavy: width 69.3 → 96.9 px, dark 0.54 → 0.55; the long stroke does not run out of paint; wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #34 Magenta oil patches
Oil 0.89 · Oil glaze 0.11 · 60 px · 19.7 s

![Brush Artist · Refs · #34 Magenta oil patches](Brush-Artist-Refs-34-Magenta-oil-patches.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 18 % → 18 % | 51.4 px | 0.61 | 1.00 | 222 |
| heavy line | 19 % → 19 % | 55.1 px | 0.61 | 1.00 | 221 |
| pressure swell | 15 % → 15 % | 54.6 px | 0.61 | 1.01 | 163 |
| fast wave | 44 % → 45 % | 51.1 px | 0.61 | 1.02 | 630 |
| slow wave | 45 % → 45 % | 52.4 px | 0.61 | 1.00 | 948 |
| spiral | 68 % → 68 % | 44.9 px | 0.58 | 1.00 | 1019 |
| loop | 42 % → 42 % | 54.2 px | 0.61 | 1.00 | 496 |
| tilted | 17 % → 17 % | 46.3 px | 0.61 | 1.00 | 320 |
| over the wet one | 34 % → 34 % | 48.4 px | 0.61 | 1.00 | 227 |
| long, no reload | 83 % → 83 % | 37.1 px | 0.59 | 1.00 | 1950 | quarters: 0.54 → 0.54 → 0.53 → 0.47

Numbers say: light vs heavy: width 51.4 → 55.1 px, dark 0.61 → 0.61; pressure barely changes the width; the long stroke does not run out of paint.

## Brush Artist · Refs · #35 Red band with runs
Watercolour 1.00 · 70 px · 52.3 s

![Brush Artist · Refs · #35 Red band with runs](Brush-Artist-Refs-35-Red-band-with-runs.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 40 % → 45 % | 115.3 px | 0.42 | 1.14 | 156 |
| heavy line | 45 % → 50 % | 132.0 px | 0.42 | 1.09 | 222 |
| pressure swell | 20 % → 28 % | 76.7 px | 0.48 | 1.37 | 148 |
| fast wave | 66 % → 76 % | 76.8 px | 0.49 | 1.14 | 482 |
| slow wave | 65 % → 76 % | 75.6 px | 0.52 | 1.16 | 836 |
| spiral | 86 % → 94 % | 56.9 px | 0.53 | 1.09 | 1066 |
| loop | 79 % → 88 % | 102.7 px | 0.49 | 1.11 | 558 |
| tilted | 50 % → 51 % | 139.1 px | 0.47 | 1.02 | 281 |
| over the wet one | 78 % → 84 % | 77.5 px | 0.47 | 1.09 | 181 |
| long, no reload | 96 % → 100 % | 43.2 px | 0.58 | 1.04 | 1282 | quarters: 0.59 → 0.60 → 0.59 → 0.56

Numbers say: light vs heavy: width 115.3 → 132.0 px, dark 0.42 → 0.42; the long stroke does not run out of paint.

## Brush Artist · Refs · #36 Magenta letters flat brush
Gouache 1.00 · 36 px · 36.6 s

![Brush Artist · Refs · #36 Magenta letters flat brush](Brush-Artist-Refs-36-Magenta-letters-flat-brush.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 10 % → 10 % | 29.6 px | 0.45 | 0.94 | 89 |
| heavy line | 16 % → 13 % | 47.5 px | 0.45 | 0.78 | 102 |
| pressure swell | 13 % → 11 % | 48.4 px | 0.47 | 0.85 | 76 |
| fast wave | 34 % → 16 % | 39.3 px | 0.47 | 0.48 | 248 |
| slow wave | 35 % → 20 % | 40.5 px | 0.45 | 0.57 | 422 |
| spiral | 46 % → 19 % | 30.6 px | 0.44 | 0.41 | 641 |
| loop | 27 % → 18 % | 35.0 px | 0.45 | 0.67 | 241 |
| tilted | 12 % → 12 % | 32.8 px | 0.47 | 1.00 | 175 |
| over the wet one | 26 % → 22 % | 38.5 px | 0.47 | 0.88 | 105 |
| long, no reload | 49 % → 19 % | 22.0 px | 0.44 | 0.39 | 712 | quarters: 0.30 → 0.27 → 0.22 → 0.18

Numbers say: light vs heavy: width 29.6 → 47.5 px, dark 0.45 → 0.45.

## Brush Artist · Refs · #37 Oil still life dabs
Oil 0.89 · Oil glaze 0.11 · 40 px · 17.9 s

![Brush Artist · Refs · #37 Oil still life dabs](Brush-Artist-Refs-37-Oil-still-life-dabs.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 11 % → 11 % | 32.1 px | 0.36 | 1.00 | 198 |
| heavy line | 12 % → 12 % | 36.1 px | 0.39 | 1.00 | 172 |
| pressure swell | 10 % → 10 % | 39.3 px | 0.40 | 1.00 | 109 |
| fast wave | 30 % → 30 % | 35.0 px | 0.39 | 1.00 | 545 |
| slow wave | 35 % → 35 % | 40.6 px | 0.37 | 1.00 | 792 |
| spiral | 52 % → 52 % | 34.4 px | 0.38 | 1.00 | 819 |
| loop | 29 % → 29 % | 36.9 px | 0.39 | 1.00 | 388 |
| tilted | 12 % → 12 % | 34.7 px | 0.41 | 1.00 | 226 |
| over the wet one | 23 % → 23 % | 30.6 px | 0.41 | 1.00 | 152 |
| long, no reload | 59 % → 59 % | 26.6 px | 0.31 | 1.00 | 1169 | quarters: 0.23 → 0.22 → 0.20 → 0.17

Numbers say: light vs heavy: width 32.1 → 36.1 px, dark 0.36 → 0.39.

## Brush Artist · Refs · #38 Sanguine drawing
Pastel 1.00 · 6 px · 10.4 s

![Brush Artist · Refs · #38 Sanguine drawing](Brush-Artist-Refs-38-Sanguine-drawing.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 1 % → 1 % | 2.1 px | 0.61 | 1.00 | 13 |
| heavy line | 1 % → 1 % | 3.9 px | 0.61 | 1.00 | 21 |
| pressure swell | 1 % → 1 % | 3.8 px | 0.61 | 1.00 | 14 |
| fast wave | 3 % → 3 % | 3.4 px | 0.61 | 1.00 | 51 |
| slow wave | 3 % → 3 % | 3.4 px | 0.61 | 1.00 | 34 |
| spiral | 4 % → 4 % | 2.8 px | 0.61 | 1.00 | 88 |
| loop | 2 % → 2 % | 3.1 px | 0.61 | 1.00 | 35 |
| tilted | 1 % → 1 % | 3.4 px | 0.61 | 1.00 | 21 |
| over the wet one | 2 % → 2 % | 2.9 px | 0.61 | 1.00 | 14 |
| long, no reload | 6 % → 6 % | 2.7 px | 0.61 | 1.00 | 124 | quarters: 0.04 → 0.04 → 0.04 → 0.04

Numbers say: light vs heavy: width 2.1 → 3.9 px, dark 0.61 → 0.61; the long stroke does not run out of paint.

## Brush Artist · Refs · #39 Very thick impasto
Impasto 1.00 · 60 px · 24.5 s

![Brush Artist · Refs · #39 Very thick impasto](Brush-Artist-Refs-39-Very-thick-impasto.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 18 % → 18 % | 53.1 px | 0.61 | 0.97 | 210 |
| heavy line | 21 % → 20 % | 60.0 px | 0.62 | 0.96 | 218 |
| pressure swell | 15 % → 15 % | 58.1 px | 0.62 | 0.97 | 160 |
| fast wave | 48 % → 47 % | 55.3 px | 0.63 | 0.98 | 650 |
| slow wave | 47 % → 45 % | 53.9 px | 0.61 | 0.97 | 999 |
| spiral | 69 % → 63 % | 45.3 px | 0.61 | 0.92 | 1041 |
| loop | 40 % → 39 % | 52.1 px | 0.61 | 0.97 | 539 |
| tilted | 16 % → 16 % | 43.8 px | 0.62 | 1.00 | 333 |
| over the wet one | 34 % → 33 % | 50.1 px | 0.62 | 0.97 | 228 |
| long, no reload | 85 % → 79 % | 38.0 px | 0.60 | 0.93 | 1842 | quarters: 0.56 → 0.55 → 0.54 → 0.51

Numbers say: light vs heavy: width 53.1 → 60.0 px, dark 0.61 → 0.62; the long stroke does not run out of paint.

## Brush Artist · Refs · #40 Watercolour blooms
Watercolour 1.00 · 90 px · 52.9 s

![Brush Artist · Refs · #40 Watercolour blooms](Brush-Artist-Refs-40-Watercolour-blooms.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 27 % → 47 % | 78.4 px | 0.08 | 1.72 | 221 |
| heavy line | 38 % → 51 % | 110.0 px | 0.09 | 1.36 | 282 |
| pressure swell | 24 % → 39 % | 91.8 px | 0.09 | 1.61 | 193 |
| fast wave | 68 % → 82 % | 78.3 px | 0.11 | 1.21 | 690 |
| slow wave | 68 % → 81 % | 79.1 px | 0.15 | 1.18 | 1392 |
| spiral | 81 % → 92 % | 53.5 px | 0.14 | 1.14 | 1208 |
| loop | 58 % → 72 % | 75.3 px | 0.13 | 1.24 | 572 |
| tilted | 34 % → 36 % | 94.8 px | 0.11 | 1.07 | 385 |
| over the wet one | 62 % → 81 % | 78.2 px | 0.11 | 1.31 | 255 |
| long, no reload | 97 % → 100 % | 43.6 px | 0.17 | 1.03 | 1519 | quarters: 0.21 → 0.20 → 0.17 → 0.13

Numbers say: light vs heavy: width 78.4 → 110.0 px, dark 0.08 → 0.09; wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #41 Coloured pencil hatching
Pastel 1.00 · 4 px · 10.8 s

![Brush Artist · Refs · #41 Coloured pencil hatching](Brush-Artist-Refs-41-Coloured-pencil-hatching.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 1 % → 1 % | 1.6 px | 0.43 | 1.00 | 11 |
| heavy line | 1 % → 1 % | 2.9 px | 0.43 | 1.00 | 14 |
| pressure swell | 1 % → 1 % | 2.8 px | 0.43 | 1.00 | 8 |
| fast wave | 2 % → 2 % | 2.5 px | 0.43 | 1.00 | 25 |
| slow wave | 2 % → 2 % | 2.5 px | 0.43 | 1.00 | 36 |
| spiral | 3 % → 3 % | 2.1 px | 0.43 | 1.00 | 61 |
| loop | 2 % → 2 % | 2.3 px | 0.43 | 1.00 | 29 |
| tilted | 1 % → 1 % | 3.0 px | 0.43 | 1.00 | 18 |
| over the wet one | 2 % → 2 % | 2.3 px | 0.43 | 1.00 | 14 |
| long, no reload | 5 % → 5 % | 2.0 px | 0.42 | 1.00 | 92 | quarters: 0.02 → 0.02 → 0.02 → 0.02

Numbers say: light vs heavy: width 1.6 → 2.9 px, dark 0.43 → 0.43; the long stroke does not run out of paint.

## Brush Artist · Refs · #42 Oil pastel shaggy
Pastel 1.00 · 18 px · 11.0 s

![Brush Artist · Refs · #42 Oil pastel shaggy](Brush-Artist-Refs-42-Oil-pastel-shaggy.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 2 % → 2 % | 4.7 px | 0.36 | 1.00 | 24 |
| heavy line | 3 % → 3 % | 10.0 px | 0.36 | 1.00 | 32 |
| pressure swell | 2 % → 2 % | 9.3 px | 0.34 | 1.00 | 16 |
| fast wave | 8 % → 8 % | 9.2 px | 0.32 | 1.00 | 118 |
| slow wave | 7 % → 7 % | 8.6 px | 0.37 | 1.00 | 99 |
| spiral | 11 % → 11 % | 7.5 px | 0.36 | 1.00 | 159 |
| loop | 6 % → 6 % | 7.8 px | 0.35 | 1.00 | 65 |
| tilted | 2 % → 2 % | 6.5 px | 0.33 | 1.00 | 37 |
| over the wet one | 5 % → 5 % | 7.6 px | 0.33 | 1.00 | 39 |
| long, no reload | 15 % → 15 % | 6.5 px | 0.37 | 1.00 | 272 | quarters: 0.00 → 0.00 → 0.00 → 0.00

Numbers say: light vs heavy: width 4.7 → 10.0 px, dark 0.36 → 0.36; the long stroke does not run out of paint.

## Brush Artist · Refs · #43 Dragged black ink blocks
Gouache 1.00 · 70 px · 28.3 s

![Brush Artist · Refs · #43 Dragged black ink blocks](Brush-Artist-Refs-43-Dragged-black-ink-blocks.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 5 % → 0 % | 14.8 px | 0.00 | 0.00 | 151 |
| heavy line | 14 % → 4 % | 40.5 px | 0.66 | 0.27 | 424 |
| pressure swell | 11 % → 4 % | 42.1 px | 0.65 | 0.33 | 197 |
| fast wave | 38 % → 1 % | 43.8 px | 0.66 | 0.03 | 743 |
| slow wave | 32 % → 2 % | 36.6 px | 0.57 | 0.05 | 1080 |
| spiral | 51 % → 4 % | 33.4 px | 0.54 | 0.07 | 1044 |
| loop | 30 % → 2 % | 38.3 px | 0.62 | 0.06 | 498 |
| tilted | 13 % → 13 % | 37.0 px | 0.66 | 0.95 | 350 |
| over the wet one | 21 % → 2 % | 22.9 px | 0.66 | 0.10 | 195 |
| long, no reload | 44 % → 7 % | 19.8 px | 0.66 | 0.16 | 1420 | quarters: 0.47 → 0.37 → 0.18 → 0.13

Numbers say: light vs heavy: width 14.8 → 40.5 px, dark 0.00 → 0.66.

## Brush Artist · Refs · #44 Blue looping ribbon
Oil 1.00 · 80 px · 28.6 s

![Brush Artist · Refs · #44 Blue looping ribbon](Brush-Artist-Refs-44-Blue-looping-ribbon.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 25 % → 26 % | 73.1 px | 0.72 | 1.04 | 345 |
| heavy line | 27 % → 27 % | 77.7 px | 0.71 | 1.00 | 447 |
| pressure swell | 20 % → 21 % | 76.5 px | 0.71 | 1.03 | 243 |
| fast wave | 62 % → 64 % | 71.4 px | 0.71 | 1.04 | 1436 |
| slow wave | 58 % → 58 % | 67.4 px | 0.70 | 1.00 | 1657 |
| spiral | 76 % → 77 % | 50.3 px | 0.69 | 1.00 | 1740 |
| loop | 53 % → 53 % | 69.2 px | 0.69 | 1.00 | 830 |
| tilted | 20 % → 20 % | 56.1 px | 0.74 | 1.00 | 397 |
| over the wet one | 41 % → 41 % | 58.7 px | 0.74 | 1.00 | 368 |
| long, no reload | 90 % → 90 % | 40.1 px | 0.69 | 1.00 | 2420 | quarters: 0.67 → 0.68 → 0.66 → 0.59

Numbers say: light vs heavy: width 73.1 → 77.7 px, dark 0.72 → 0.71; pressure barely changes the width; the long stroke does not run out of paint.

## Brush Artist · Refs · #45 Soft pastel pepper
Pastel 1.00 · 40 px · 11.6 s

![Brush Artist · Refs · #45 Soft pastel pepper](Brush-Artist-Refs-45-Soft-pastel-pepper.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 4 % → 4 % | 11.0 px | 0.53 | 1.00 | 114 |
| heavy line | 7 % → 7 % | 21.2 px | 0.53 | 1.00 | 54 |
| pressure swell | 5 % → 5 % | 19.0 px | 0.55 | 1.00 | 41 |
| fast wave | 17 % → 17 % | 19.3 px | 0.56 | 1.00 | 140 |
| slow wave | 16 % → 16 % | 18.0 px | 0.54 | 1.00 | 248 |
| spiral | 23 % → 23 % | 15.4 px | 0.54 | 1.00 | 294 |
| loop | 12 % → 12 % | 15.4 px | 0.54 | 1.00 | 143 |
| tilted | 4 % → 4 % | 11.4 px | 0.55 | 1.00 | 71 |
| over the wet one | 10 % → 10 % | 16.7 px | 0.55 | 1.00 | 62 |
| long, no reload | 28 % → 28 % | 12.6 px | 0.53 | 1.00 | 359 | quarters: 0.17 → 0.16 → 0.17 → 0.17

Numbers say: light vs heavy: width 11.0 → 21.2 px, dark 0.53 → 0.53; the long stroke does not run out of paint.

## Brush Artist · Refs · #46 Red-brown ink lips
Watercolour 1.00 · 50 px · 42.2 s

![Brush Artist · Refs · #46 Red-brown ink lips](Brush-Artist-Refs-46-Red-brown-ink-lips.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 15 % → 31 % | 43.9 px | 0.59 | 2.04 | 168 |
| heavy line | 22 % → 35 % | 63.4 px | 0.60 | 1.58 | 107 |
| pressure swell | 13 % → 22 % | 50.3 px | 0.63 | 1.64 | 90 |
| fast wave | 43 % → 64 % | 49.7 px | 0.64 | 1.50 | 246 |
| slow wave | 42 % → 63 % | 49.1 px | 0.67 | 1.49 | 461 |
| spiral | 65 % → 79 % | 42.6 px | 0.69 | 1.22 | 455 |
| loop | 38 % → 55 % | 48.8 px | 0.67 | 1.47 | 239 |
| tilted | 21 % → 23 % | 58.2 px | 0.60 | 1.11 | 147 |
| over the wet one | 42 % → 63 % | 58.5 px | 0.60 | 1.51 | 114 |
| long, no reload | 78 % → 95 % | 35.1 px | 0.70 | 1.21 | 620 | quarters: 0.71 → 0.71 → 0.69 → 0.65

Numbers say: light vs heavy: width 43.9 → 63.4 px, dark 0.59 → 0.60; the long stroke does not run out of paint; wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #47 Pink knife slabs
Impasto 1.00 · 90 px · 31.3 s

![Brush Artist · Refs · #47 Pink knife slabs](Brush-Artist-Refs-47-Pink-knife-slabs.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 27 % → 26 % | 78.7 px | 0.29 | 0.97 | 215 |
| heavy line | 29 % → 28 % | 84.6 px | 0.29 | 0.96 | 273 |
| pressure swell | 22 % → 22 % | 81.2 px | 0.26 | 1.01 | 265 |
| fast wave | 62 % → 61 % | 71.8 px | 0.24 | 0.98 | 730 |
| slow wave | 62 % → 58 % | 71.5 px | 0.28 | 0.94 | 1154 |
| spiral | 75 % → 60 % | 49.3 px | 0.28 | 0.80 | 1384 |
| loop | 56 % → 54 % | 72.1 px | 0.29 | 0.97 | 640 |
| tilted | 22 % → 22 % | 60.2 px | 0.25 | 1.00 | 477 |
| over the wet one | 46 % → 44 % | 69.3 px | 0.25 | 0.96 | 308 |
| long, no reload | 93 % → 77 % | 41.9 px | 0.26 | 0.83 | 1871 | quarters: 0.00 → 0.00 → 0.00 → 0.00

Numbers say: light vs heavy: width 78.7 → 84.6 px, dark 0.29 → 0.29; pressure barely changes the width; the long stroke does not run out of paint.

## Brush Artist · Refs · #48 Black bands with drips
Gouache 1.00 · 70 px · 47.9 s

![Brush Artist · Refs · #48 Black bands with drips](Brush-Artist-Refs-48-Black-bands-with-drips.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 28 % → 23 % | 80.2 px | 0.63 | 0.82 | 211 |
| heavy line | 35 % → 26 % | 100.7 px | 0.64 | 0.75 | 287 |
| pressure swell | 25 % → 21 % | 93.8 px | 0.63 | 0.85 | 224 |
| fast wave | 63 % → 41 % | 72.9 px | 0.63 | 0.64 | 709 |
| slow wave | 62 % → 41 % | 71.5 px | 0.63 | 0.66 | 1166 |
| spiral | 69 % → 40 % | 45.7 px | 0.61 | 0.57 | 1140 |
| loop | 54 % → 40 % | 69.9 px | 0.63 | 0.74 | 658 |
| tilted | 29 % → 29 % | 80.5 px | 0.62 | 1.01 | 384 |
| over the wet one | 59 % → 48 % | 82.9 px | 0.62 | 0.82 | 275 |
| long, no reload | 78 % → 37 % | 34.9 px | 0.61 | 0.47 | 1663 | quarters: 0.58 → 0.54 → 0.47 → 0.39

Numbers say: light vs heavy: width 80.2 → 100.7 px, dark 0.63 → 0.64.

## Brush Artist · Refs · #49 Magenta letters round brush
Ink 1.00 · 30 px · 31.6 s

![Brush Artist · Refs · #49 Magenta letters round brush](Brush-Artist-Refs-49-Magenta-letters-round-brush.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 6 % → 8 % | 18.1 px | 0.49 | 1.21 | 62 |
| heavy line | 21 % → 20 % | 60.3 px | 0.51 | 0.98 | 120 |
| pressure swell | 13 % → 13 % | 47.1 px | 0.51 | 1.01 | 100 |
| fast wave | 38 % → 38 % | 44.0 px | 0.51 | 1.00 | 231 |
| slow wave | 34 % → 34 % | 39.4 px | 0.51 | 0.99 | 430 |
| spiral | 49 % → 48 % | 32.6 px | 0.51 | 0.96 | 298 |
| loop | 30 % → 30 % | 38.3 px | 0.51 | 1.00 | 168 |
| tilted | 11 % → 12 % | 32.0 px | 0.52 | 1.00 | 108 |
| over the wet one | 27 % → 27 % | 42.2 px | 0.52 | 1.01 | 73 |
| long, no reload | 63 % → 56 % | 28.2 px | 0.50 | 0.90 | 553 | quarters: 0.42 → 0.37 → 0.30 → 0.25

Numbers say: light vs heavy: width 18.1 → 60.3 px, dark 0.49 → 0.51.

## Brush Artist · Refs · #50 Thick swipes on photo
Impasto 1.00 · 40 px · 18.8 s

![Brush Artist · Refs · #50 Thick swipes on photo](Brush-Artist-Refs-50-Thick-swipes-on-photo.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 13 % → 13 % | 38.6 px | 0.27 | 0.95 | 135 |
| heavy line | 14 % → 13 % | 40.0 px | 0.27 | 0.96 | 142 |
| pressure swell | 11 % → 10 % | 40.1 px | 0.24 | 0.95 | 122 |
| fast wave | 35 % → 31 % | 40.1 px | 0.24 | 0.89 | 399 |
| slow wave | 34 % → 32 % | 39.5 px | 0.26 | 0.93 | 725 |
| spiral | 58 % → 46 % | 38.5 px | 0.29 | 0.79 | 608 |
| loop | 29 % → 28 % | 37.4 px | 0.26 | 0.96 | 293 |
| tilted | 12 % → 12 % | 33.6 px | 0.22 | 1.00 | 192 |
| over the wet one | 25 % → 24 % | 36.7 px | 0.22 | 0.96 | 134 |
| long, no reload | 68 % → 46 % | 30.4 px | 0.26 | 0.68 | 910 | quarters: 0.00 → 0.00 → 0.00 → 0.00

Numbers say: light vs heavy: width 38.6 → 40.0 px, dark 0.27 → 0.27; pressure barely changes the width.

## Brush Artist · Refs · Drag #e8b4a8
Gouache 1.00 · 40 px · 17.8 s

![Brush Artist · Refs · Drag #e8b4a8](Brush-Artist-Refs-Drag-e8b4a8.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 3 % → 0 % | 9.3 px | 0.00 | 0.00 | 116 |
| heavy line | 6 % → 0 % | 16.2 px | 0.34 | 0.01 | 103 |
| pressure swell | 3 % → 0 % | 12.9 px | 0.00 | 0.00 | 98 |
| fast wave | 16 % → 0 % | 18.1 px | 0.00 | 0.00 | 322 |
| slow wave | 13 % → 0 % | 15.0 px | 0.00 | 0.00 | 549 |
| spiral | 20 % → 0 % | 13.4 px | 0.00 | 0.00 | 612 |
| loop | 13 % → 0 % | 17.1 px | 0.00 | 0.00 | 305 |
| tilted | 6 % → 5 % | 16.8 px | 0.00 | 0.77 | 150 |
| over the wet one | 7 % → 0 % | 1.8 px | 0.00 | 0.00 | 123 |
| long, no reload | 10 % → 0 % | 4.6 px | 0.00 | 0.00 | 795 | quarters: 0.02 → 0.02 → 0.02 → 0.02

Numbers say: light vs heavy: width 9.3 → 16.2 px, dark 0.00 → 0.34; the long stroke does not run out of paint.

## Brush Artist · Refs · Drag #e8e4e0
Gouache 1.00 · 40 px · 18.1 s

![Brush Artist · Refs · Drag #e8e4e0](Brush-Artist-Refs-Drag-e8e4e0.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 3 % → 0 % | 9.3 px | 0.00 | 0.00 | 136 |
| heavy line | 6 % → 0 % | 16.2 px | 0.43 | 0.01 | 145 |
| pressure swell | 3 % → 0 % | 12.9 px | 0.00 | 0.00 | 81 |
| fast wave | 16 % → 0 % | 18.1 px | 0.00 | 0.00 | 356 |
| slow wave | 13 % → 0 % | 15.0 px | 0.00 | 0.00 | 513 |
| spiral | 20 % → 0 % | 13.4 px | 0.00 | 0.00 | 513 |
| loop | 13 % → 0 % | 17.1 px | 0.00 | 0.00 | 270 |
| tilted | 6 % → 5 % | 16.8 px | 0.00 | 0.77 | 142 |
| over the wet one | 7 % → 0 % | 1.8 px | 0.00 | 0.00 | 105 |
| long, no reload | 10 % → 0 % | 4.6 px | 0.00 | 0.00 | 700 | quarters: 0.02 → 0.02 → 0.02 → 0.02

Numbers say: light vs heavy: width 9.3 → 16.2 px, dark 0.00 → 0.43; the long stroke does not run out of paint.

## Brush Artist · Refs · Finger
Pastel 1.00 · 36 px · 21.2 s · over bands of wet oil paint and oil pastel in turn (it works on paint already there: look at what it does to the bands; covered counts the bands too)

![Brush Artist · Refs · Finger](Brush-Artist-Refs-Finger.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 26 % → 26 % | 74.4 px | 0.80 | 1.00 | 40 |
| heavy line | 27 % → 27 % | 79.3 px | 0.80 | 1.00 | 43 |
| pressure swell | 26 % → 26 % | 98.0 px | 0.80 | 1.00 | 37 |
| fast wave | 33 % → 33 % | 38.0 px | 0.78 | 1.00 | 120 |
| slow wave | 31 % → 31 % | 36.3 px | 0.78 | 1.00 | 201 |
| spiral | 38 % → 38 % | 25.3 px | 0.76 | 1.00 | 182 |
| loop | 31 % → 31 % | 39.5 px | 0.79 | 1.00 | 132 |
| tilted | 26 % → 26 % | 73.5 px | 0.78 | 1.00 | 71 |
| over the wet one | 29 % → 29 % | 7.5 px | 0.78 | 1.00 | 56 |
| long, no reload | 39 % → 39 % | 17.4 px | 0.76 | 1.00 | 337 | quarters: 0.24 → 0.36 → 0.32 → 0.37

Numbers say: light vs heavy: width 74.4 → 79.3 px, dark 0.80 → 0.80; pressure barely changes the width; the long stroke does not run out of paint.

## Brush Artist · Ink — wash
Watercolour 1.00 · 38 px · 32.7 s

![Brush Artist · Ink — wash](Brush-Artist-Ink-wash.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 11 % → 11 % | 31.6 px | 0.39 | 1.04 | 65 |
| heavy line | 19 % → 19 % | 54.3 px | 0.32 | 1.03 | 106 |
| pressure swell | 12 % → 13 % | 45.2 px | 0.37 | 1.04 | 64 |
| fast wave | 39 % → 41 % | 45.5 px | 0.31 | 1.04 | 194 |
| slow wave | 37 % → 38 % | 42.9 px | 0.37 | 1.03 | 321 |
| spiral | 58 % → 61 % | 38.6 px | 0.31 | 1.04 | 301 |
| loop | 32 % → 33 % | 41.9 px | 0.35 | 1.02 | 150 |
| tilted | 13 % → 14 % | 37.0 px | 0.38 | 1.04 | 111 |
| over the wet one | 29 % → 30 % | 42.8 px | 0.38 | 1.04 | 71 |
| long, no reload | 67 % → 72 % | 30.0 px | 0.29 | 1.07 | 445 | quarters: 0.34 → 0.27 → 0.19 → 0.12

Numbers say: light vs heavy: width 31.6 → 54.3 px, dark 0.39 → 0.32.

## Brush Artist · Ink — brush line
Ink 1.00 · 16 px · 26.9 s

![Brush Artist · Ink — brush line](Brush-Artist-Ink-brush-line.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 3 % → 5 % | 8.2 px | 0.77 | 1.72 | 32 |
| heavy line | 12 % → 12 % | 35.2 px | 0.88 | 0.99 | 83 |
| pressure swell | 8 % → 8 % | 28.5 px | 0.86 | 1.06 | 48 |
| fast wave | 24 % → 24 % | 28.2 px | 0.87 | 0.98 | 146 |
| slow wave | 20 % → 20 % | 23.7 px | 0.87 | 0.97 | 182 |
| spiral | 31 % → 27 % | 20.3 px | 0.86 | 0.87 | 241 |
| loop | 19 % → 19 % | 24.3 px | 0.87 | 0.99 | 105 |
| tilted | 8 % → 8 % | 21.2 px | 0.88 | 1.01 | 78 |
| over the wet one | 17 % → 17 % | 26.2 px | 0.88 | 1.01 | 62 |
| long, no reload | 44 % → 31 % | 19.7 px | 0.84 | 0.70 | 376 | quarters: 0.51 → 0.41 → 0.30 → 0.20

Numbers say: light vs heavy: width 8.2 → 35.2 px, dark 0.77 → 0.88; wet paint spreads well beyond the stroke.

## Brush Artist · Ink — dry brush
Gouache 1.00 · 30 px · 20.6 s

![Brush Artist · Ink — dry brush](Brush-Artist-Ink-dry-brush.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 2 % → 0 % | 5.7 px | 0.00 | 0.00 | 58 |
| heavy line | 4 % → 0 % | 10.2 px | 0.77 | 0.01 | 138 |
| pressure swell | 4 % → 0 % | 14.1 px | 0.77 | 0.06 | 59 |
| fast wave | 12 % → 0 % | 14.0 px | 0.77 | 0.00 | 293 |
| slow wave | 10 % → 0 % | 11.9 px | 0.77 | 0.00 | 412 |
| spiral | 17 % → 0 % | 11.1 px | 0.77 | 0.00 | 406 |
| loop | 9 % → 0 % | 11.2 px | 0.77 | 0.01 | 188 |
| tilted | 5 % → 4 % | 13.5 px | 0.77 | 0.89 | 110 |
| over the wet one | 7 % → 0 % | 5.9 px | 0.77 | 0.00 | 80 |
| long, no reload | 14 % → 1 % | 6.5 px | 0.77 | 0.08 | 517 | quarters: 0.21 → 0.14 → 0.10 → 0.07

Numbers say: light vs heavy: width 5.7 → 10.2 px, dark 0.00 → 0.77.

## Brush Artist · Watercolour — blue
Watercolour 0.93 · Ink 0.07 · 40 px · 29.2 s

![Brush Artist · Watercolour — blue](Brush-Artist-Watercolour-blue.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 6 % → 11 % | 16.2 px | 0.29 | 1.88 | 37 |
| heavy line | 11 % → 13 % | 31.9 px | 0.29 | 1.17 | 70 |
| pressure swell | 7 % → 9 % | 25.7 px | 0.30 | 1.38 | 33 |
| fast wave | 24 % → 27 % | 28.2 px | 0.29 | 1.12 | 127 |
| slow wave | 23 % → 32 % | 26.4 px | 0.31 | 1.41 | 269 |
| spiral | 39 % → 47 % | 25.6 px | 0.29 | 1.21 | 198 |
| loop | 20 % → 25 % | 25.7 px | 0.30 | 1.25 | 150 |
| tilted | 12 % → 12 % | 34.0 px | 0.30 | 1.00 | 98 |
| over the wet one | 21 % → 25 % | 25.2 px | 0.30 | 1.19 | 57 |
| long, no reload | 53 % → 59 % | 23.6 px | 0.30 | 1.12 | 418 | quarters: 0.23 → 0.21 → 0.19 → 0.16

Numbers say: light vs heavy: width 16.2 → 31.9 px, dark 0.29 → 0.29; wet paint spreads well beyond the stroke.

## Brush Artist · Watercolour — violet
Watercolour 0.93 · Ink 0.07 · 40 px · 29.6 s

![Brush Artist · Watercolour — violet](Brush-Artist-Watercolour-violet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 6 % → 11 % | 16.2 px | 0.36 | 1.88 | 46 |
| heavy line | 11 % → 13 % | 31.9 px | 0.37 | 1.17 | 89 |
| pressure swell | 7 % → 9 % | 25.7 px | 0.38 | 1.38 | 51 |
| fast wave | 24 % → 27 % | 28.2 px | 0.38 | 1.12 | 223 |
| slow wave | 23 % → 32 % | 26.4 px | 0.39 | 1.41 | 279 |
| spiral | 39 % → 47 % | 25.6 px | 0.37 | 1.21 | 247 |
| loop | 20 % → 25 % | 25.7 px | 0.38 | 1.25 | 129 |
| tilted | 12 % → 12 % | 34.0 px | 0.38 | 1.00 | 90 |
| over the wet one | 21 % → 25 % | 25.2 px | 0.38 | 1.19 | 71 |
| long, no reload | 53 % → 59 % | 23.6 px | 0.38 | 1.12 | 364 | quarters: 0.28 → 0.27 → 0.24 → 0.21

Numbers say: light vs heavy: width 16.2 → 31.9 px, dark 0.36 → 0.37; wet paint spreads well beyond the stroke.

## Brush Artist · Watercolour — teal
Watercolour 0.93 · Ink 0.07 · 40 px · 29.4 s

![Brush Artist · Watercolour — teal](Brush-Artist-Watercolour-teal.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 6 % → 11 % | 16.2 px | 0.23 | 1.88 | 33 |
| heavy line | 11 % → 13 % | 31.9 px | 0.23 | 1.17 | 84 |
| pressure swell | 7 % → 9 % | 25.7 px | 0.24 | 1.38 | 41 |
| fast wave | 24 % → 27 % | 28.2 px | 0.23 | 1.12 | 178 |
| slow wave | 23 % → 32 % | 26.4 px | 0.25 | 1.41 | 243 |
| spiral | 39 % → 47 % | 25.6 px | 0.23 | 1.21 | 221 |
| loop | 20 % → 25 % | 25.7 px | 0.24 | 1.25 | 137 |
| tilted | 12 % → 12 % | 34.0 px | 0.24 | 1.00 | 102 |
| over the wet one | 21 % → 25 % | 25.2 px | 0.24 | 1.19 | 54 |
| long, no reload | 53 % → 59 % | 23.6 px | 0.24 | 1.12 | 385 | quarters: 0.18 → 0.16 → 0.15 → 0.13

Numbers say: light vs heavy: width 16.2 → 31.9 px, dark 0.23 → 0.23; wet paint spreads well beyond the stroke.

## Brush Artist · Gouache
Gouache 1.00 · 30 px · 31.7 s

![Brush Artist · Gouache](Brush-Artist-Gouache.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 8 % → 8 % | 24.4 px | 0.27 | 0.97 | 94 |
| heavy line | 15 % → 12 % | 42.8 px | 0.27 | 0.78 | 165 |
| pressure swell | 11 % → 9 % | 41.0 px | 0.27 | 0.85 | 62 |
| fast wave | 30 % → 14 % | 34.9 px | 0.26 | 0.45 | 173 |
| slow wave | 29 % → 14 % | 34.0 px | 0.26 | 0.47 | 346 |
| spiral | 40 % → 14 % | 26.6 px | 0.26 | 0.35 | 368 |
| loop | 24 % → 15 % | 30.6 px | 0.26 | 0.62 | 165 |
| tilted | 10 % → 10 % | 27.4 px | 0.27 | 1.01 | 103 |
| over the wet one | 22 % → 19 % | 32.9 px | 0.27 | 0.89 | 78 |
| long, no reload | 43 % → 15 % | 19.1 px | 0.26 | 0.35 | 421 | quarters: 0.01 → 0.01 → 0.01 → 0.01

Numbers say: light vs heavy: width 24.4 → 42.8 px, dark 0.27 → 0.27; the long stroke does not run out of paint.

## Brush Artist · Oil — bristle
Oil 0.89 · Oil glaze 0.11 · 30 px · 14.4 s

![Brush Artist · Oil — bristle](Brush-Artist-Oil-bristle.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 10 % → 10 % | 28.5 px | 0.53 | 1.00 | 132 |
| heavy line | 11 % → 11 % | 32.4 px | 0.54 | 1.00 | 128 |
| pressure swell | 8 % → 8 % | 31.8 px | 0.54 | 1.00 | 75 |
| fast wave | 28 % → 28 % | 32.0 px | 0.54 | 1.00 | 289 |
| slow wave | 27 % → 27 % | 31.6 px | 0.54 | 1.00 | 486 |
| spiral | 48 % → 48 % | 31.3 px | 0.53 | 1.00 | 583 |
| loop | 22 % → 22 % | 28.9 px | 0.54 | 1.00 | 279 |
| tilted | 11 % → 11 % | 29.9 px | 0.54 | 1.00 | 122 |
| over the wet one | 21 % → 21 % | 29.6 px | 0.54 | 1.00 | 114 |
| long, no reload | 55 % → 55 % | 24.7 px | 0.52 | 1.00 | 847 | quarters: 0.35 → 0.33 → 0.31 → 0.29

Numbers say: light vs heavy: width 28.5 → 32.4 px, dark 0.53 → 0.54.

## Brush Artist · Charcoal — stick
Charcoal 0.78 · Pastel 0.22 · 28 px · 10.1 s

![Brush Artist · Charcoal — stick](Brush-Artist-Charcoal-stick.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 5 % → 5 % | 15.2 px | 0.85 | 1.00 | 16 |
| heavy line | 8 % → 8 % | 24.2 px | 0.85 | 1.00 | 31 |
| pressure swell | 5 % → 5 % | 19.3 px | 0.85 | 1.00 | 21 |
| fast wave | 19 % → 19 % | 21.5 px | 0.85 | 1.00 | 82 |
| slow wave | 18 % → 18 % | 21.1 px | 0.85 | 1.00 | 118 |
| spiral | 25 % → 25 % | 16.3 px | 0.85 | 1.00 | 125 |
| loop | 16 % → 16 % | 20.2 px | 0.85 | 1.00 | 54 |
| tilted | 6 % → 6 % | 17.3 px | 0.85 | 1.00 | 33 |
| over the wet one | 14 % → 14 % | 20.5 px | 0.85 | 1.00 | 18 |
| long, no reload | 41 % → 41 % | 18.5 px | 0.85 | 1.00 | 216 | quarters: 0.39 → 0.39 → 0.39 → 0.39

Numbers say: light vs heavy: width 15.2 → 24.2 px, dark 0.85 → 0.85; the long stroke does not run out of paint.

## Brush Artist · Charcoal — stick B
Charcoal 0.78 · Pastel 0.22 · 36 px · 10.2 s

![Brush Artist · Charcoal — stick B](Brush-Artist-Charcoal-stick-B.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 7 % → 7 % | 19.2 px | 0.85 | 1.00 | 22 |
| heavy line | 10 % → 10 % | 30.5 px | 0.85 | 1.00 | 34 |
| pressure swell | 7 % → 7 % | 24.5 px | 0.85 | 1.00 | 23 |
| fast wave | 24 % → 24 % | 27.6 px | 0.85 | 1.00 | 101 |
| slow wave | 23 % → 23 % | 26.6 px | 0.85 | 1.00 | 161 |
| spiral | 35 % → 35 % | 23.2 px | 0.85 | 1.00 | 149 |
| loop | 19 % → 19 % | 25.2 px | 0.85 | 1.00 | 82 |
| tilted | 7 % → 7 % | 20.3 px | 0.85 | 1.00 | 36 |
| over the wet one | 17 % → 17 % | 25.9 px | 0.85 | 1.00 | 45 |
| long, no reload | 50 % → 50 % | 22.6 px | 0.85 | 1.00 | 244 | quarters: 0.47 → 0.47 → 0.47 → 0.47

Numbers say: light vs heavy: width 19.2 → 30.5 px, dark 0.85 → 0.85; the long stroke does not run out of paint.

## Brush Artist · Charcoal — stick C
Charcoal 0.78 · Pastel 0.22 · 22 px · 9.8 s

![Brush Artist · Charcoal — stick C](Brush-Artist-Charcoal-stick-C.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 4 % → 4 % | 12.2 px | 0.85 | 1.00 | 25 |
| heavy line | 7 % → 7 % | 19.4 px | 0.85 | 1.00 | 21 |
| pressure swell | 4 % → 4 % | 14.3 px | 0.85 | 1.00 | 22 |
| fast wave | 15 % → 15 % | 17.1 px | 0.85 | 1.00 | 46 |
| slow wave | 15 % → 15 % | 17.0 px | 0.85 | 1.00 | 67 |
| spiral | 20 % → 20 % | 13.3 px | 0.85 | 1.00 | 100 |
| loop | 12 % → 12 % | 16.1 px | 0.85 | 1.00 | 52 |
| tilted | 5 % → 5 % | 15.1 px | 0.85 | 1.00 | 20 |
| over the wet one | 11 % → 11 % | 16.8 px | 0.85 | 1.00 | 19 |
| long, no reload | 34 % → 34 % | 15.3 px | 0.85 | 1.00 | 119 | quarters: 0.33 → 0.32 → 0.32 → 0.32

Numbers say: light vs heavy: width 12.2 → 19.4 px, dark 0.85 → 0.85; the long stroke does not run out of paint.

## Oil · Henry Ward · Loaded flat
Gouache 1.00 · 84 px · 46.3 s

![Oil · Henry Ward · Loaded flat](Oil-Henry-Ward-Loaded-flat.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 13 % → 4 % | 39.1 px | 0.38 | 0.29 | 260 |
| heavy line | 19 % → 18 % | 54.3 px | 0.40 | 0.99 | 314 |
| pressure swell | 16 % → 14 % | 61.7 px | 0.38 | 0.86 | 233 |
| fast wave | 52 % → 43 % | 60.1 px | 0.34 | 0.83 | 860 |
| slow wave | 51 % → 40 % | 59.2 px | 0.39 | 0.79 | 1462 |
| spiral | 69 % → 41 % | 45.6 px | 0.38 | 0.59 | 1401 |
| loop | 48 % → 38 % | 62.4 px | 0.38 | 0.79 | 667 |
| tilted | 20 % → 20 % | 54.9 px | 0.34 | 1.00 | 416 |
| over the wet one | 38 % → 34 % | 52.0 px | 0.34 | 0.88 | 366 |
| long, no reload | 73 % → 48 % | 32.5 px | 0.40 | 0.66 | 1811 | quarters: 0.00 → 0.00 → 0.01 → 0.02

Numbers say: light vs heavy: width 39.1 → 54.3 px, dark 0.38 → 0.40; the long stroke does not run out of paint.

## Oil · Henry Ward · Dry scrub
Gouache 1.00 · 90 px · 33.9 s

![Oil · Henry Ward · Dry scrub](Oil-Henry-Ward-Dry-scrub.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 8 % → 0 % | 23.3 px | 0.00 | 0.00 | 231 |
| heavy line | 14 % → 4 % | 39.5 px | 0.36 | 0.26 | 298 |
| pressure swell | 12 % → 4 % | 44.1 px | 0.38 | 0.37 | 208 |
| fast wave | 48 % → 21 % | 55.4 px | 0.29 | 0.44 | 896 |
| slow wave | 42 % → 16 % | 48.6 px | 0.34 | 0.38 | 1464 |
| spiral | 61 % → 5 % | 40.5 px | 0.33 | 0.08 | 1334 |
| loop | 33 % → 4 % | 42.9 px | 0.30 | 0.11 | 663 |
| tilted | 19 % → 19 % | 54.1 px | 0.31 | 1.00 | 501 |
| over the wet one | 28 % → 14 % | 22.7 px | 0.31 | 0.51 | 273 |
| long, no reload | 44 % → 4 % | 19.8 px | 0.35 | 0.10 | 1517 | quarters: 0.03 → 0.03 → 0.03 → 0.05

Numbers say: light vs heavy: width 23.3 → 39.5 px, dark 0.00 → 0.36; the long stroke does not run out of paint.

## Oil · Henry Ward · Dirty contour
Gouache 1.00 · 34 px · 35.2 s

![Oil · Henry Ward · Dirty contour](Oil-Henry-Ward-Dirty-contour.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 10 % → 8 % | 29.7 px | 0.67 | 0.78 | 126 |
| heavy line | 12 % → 11 % | 33.9 px | 0.67 | 0.92 | 122 |
| pressure swell | 9 % → 8 % | 32.4 px | 0.68 | 0.96 | 99 |
| fast wave | 23 % → 20 % | 26.4 px | 0.69 | 0.88 | 318 |
| slow wave | 28 % → 25 % | 32.6 px | 0.65 | 0.87 | 576 |
| spiral | 39 % → 24 % | 25.4 px | 0.62 | 0.63 | 584 |
| loop | 21 % → 20 % | 27.5 px | 0.65 | 0.93 | 268 |
| tilted | 10 % → 10 % | 28.6 px | 0.69 | 1.02 | 154 |
| over the wet one | 22 % → 21 % | 32.3 px | 0.69 | 0.96 | 145 |
| long, no reload | 47 % → 28 % | 20.9 px | 0.64 | 0.61 | 864 | quarters: 0.43 → 0.37 → 0.28 → 0.25

Numbers say: light vs heavy: width 29.7 → 33.9 px, dark 0.67 → 0.67.

## Oil · Henry Ward · Wet drag
Gouache 1.00 · 80 px · 39.1 s

![Oil · Henry Ward · Wet drag](Oil-Henry-Ward-Wet-drag.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 12 % → 2 % | 36.2 px | 0.35 | 0.17 | 242 |
| heavy line | 17 % → 13 % | 50.1 px | 0.36 | 0.75 | 271 |
| pressure swell | 16 % → 9 % | 60.0 px | 0.35 | 0.54 | 236 |
| fast wave | 45 % → 17 % | 52.3 px | 0.31 | 0.37 | 892 |
| slow wave | 51 % → 26 % | 58.6 px | 0.34 | 0.51 | 1366 |
| spiral | 67 % → 33 % | 44.5 px | 0.34 | 0.49 | 1436 |
| loop | 44 % → 21 % | 57.5 px | 0.33 | 0.46 | 690 |
| tilted | 19 % → 19 % | 53.3 px | 0.31 | 1.00 | 410 |
| over the wet one | 38 % → 29 % | 53.1 px | 0.31 | 0.76 | 351 |
| long, no reload | 74 % → 34 % | 33.3 px | 0.34 | 0.45 | 1867 | quarters: 0.00 → 0.00 → 0.01 → 0.03

Numbers say: light vs heavy: width 36.2 → 50.1 px, dark 0.35 → 0.36; the long stroke does not run out of paint.

## Oil · Henry Ward · Thin veil
Oil 0.81 · Ink 0.19 · 96 px · 46.4 s

![Oil · Henry Ward · Thin veil](Oil-Henry-Ward-Thin-veil.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 9 % → 4 % | 24.9 px | 0.06 | 0.51 | 256 |
| heavy line | 22 % → 20 % | 65.2 px | 0.26 | 0.89 | 442 |
| pressure swell | 20 % → 18 % | 73.8 px | 0.19 | 0.91 | 272 |
| fast wave | 59 % → 58 % | 68.4 px | 0.15 | 0.98 | 1042 |
| slow wave | 58 % → 51 % | 67.1 px | 0.18 | 0.89 | 1669 |
| spiral | 83 % → 67 % | 55.0 px | 0.17 | 0.80 | 1665 |
| loop | 57 % → 49 % | 74.0 px | 0.12 | 0.85 | 810 |
| tilted | 23 % → 23 % | 63.1 px | 0.18 | 1.01 | 516 |
| over the wet one | 36 % → 34 % | 38.7 px | 0.18 | 0.93 | 487 |
| long, no reload | 82 % → 70 % | 36.7 px | 0.15 | 0.85 | 2423 | quarters: 0.00 → 0.01 → 0.01 → 0.01

Numbers say: light vs heavy: width 24.9 → 65.2 px, dark 0.06 → 0.26; the long stroke does not run out of paint.

## Oil · Henry Ward · Ground
Gouache 1.00 · 160 px · 75.2 s

![Oil · Henry Ward · Ground](Oil-Henry-Ward-Ground.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 51 % → 46 % | 148.3 px | 0.37 | 0.89 | 742 |
| heavy line | 52 % → 47 % | 151.5 px | 0.37 | 0.91 | 898 |
| pressure swell | 41 % → 45 % | 154.8 px | 0.36 | 1.10 | 693 |
| fast wave | 85 % → 86 % | 97.8 px | 0.36 | 1.01 | 2291 |
| slow wave | 86 % → 73 % | 99.2 px | 0.37 | 0.86 | 4599 |
| spiral | 88 % → 69 % | 58.3 px | 0.36 | 0.77 | 4202 |
| loop | 75 % → 69 % | 97.0 px | 0.37 | 0.92 | 1977 |
| tilted | 39 % → 39 % | 107.5 px | 0.37 | 1.00 | 1140 |
| over the wet one | 76 % → 71 % | 104.6 px | 0.37 | 0.93 | 921 |
| long, no reload | 98 % → 87 % | 44.0 px | 0.37 | 0.88 | 6104 | quarters: 0.00 → 0.00 → 0.00 → 0.00

Numbers say: light vs heavy: width 148.3 → 151.5 px, dark 0.37 → 0.37; pressure barely changes the width.

## Oil · Henry Ward · HW #02 cream over wet olive
Oil 0.81 · Ink 0.19 · 96 px · 47.8 s

![Oil · Henry Ward · HW #02 cream over wet olive](Oil-Henry-Ward-HW-02-cream-over-wet-olive.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 9 % → 4 % | 24.9 px | 0.56 | 0.51 | 306 |
| heavy line | 22 % → 20 % | 65.2 px | 0.63 | 0.89 | 375 |
| pressure swell | 20 % → 18 % | 73.8 px | 0.59 | 0.91 | 266 |
| fast wave | 59 % → 58 % | 68.4 px | 0.65 | 0.98 | 1114 |
| slow wave | 58 % → 51 % | 67.1 px | 0.65 | 0.89 | 1751 |
| spiral | 83 % → 67 % | 55.0 px | 0.70 | 0.80 | 1991 |
| loop | 57 % → 49 % | 74.0 px | 0.62 | 0.85 | 942 |
| tilted | 23 % → 23 % | 63.1 px | 0.64 | 1.01 | 610 |
| over the wet one | 36 % → 34 % | 38.7 px | 0.64 | 0.93 | 524 |
| long, no reload | 82 % → 70 % | 36.7 px | 0.67 | 0.85 | 2620 | quarters: 0.65 → 0.61 → 0.54 → 0.28

Numbers say: light vs heavy: width 24.9 → 65.2 px, dark 0.56 → 0.63.

## Oil · Henry Ward · HW #04 grey arcs over ochre
Gouache 1.00 · 84 px · 48.6 s

![Oil · Henry Ward · HW #04 grey arcs over ochre](Oil-Henry-Ward-HW-04-grey-arcs-over-ochre.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 12 % → 7 % | 35.0 px | 0.29 | 0.56 | 244 |
| heavy line | 21 % → 20 % | 60.6 px | 0.36 | 0.94 | 304 |
| pressure swell | 16 % → 14 % | 60.6 px | 0.34 | 0.89 | 281 |
| fast wave | 51 % → 44 % | 59.2 px | 0.26 | 0.85 | 908 |
| slow wave | 53 % → 41 % | 61.3 px | 0.30 | 0.77 | 1732 |
| spiral | 66 % → 50 % | 43.3 px | 0.24 | 0.77 | 1471 |
| loop | 52 % → 36 % | 67.4 px | 0.29 | 0.68 | 934 |
| tilted | 19 % → 19 % | 52.9 px | 0.26 | 1.00 | 535 |
| over the wet one | 38 % → 34 % | 53.6 px | 0.26 | 0.89 | 386 |
| long, no reload | 77 % → 52 % | 34.7 px | 0.25 | 0.67 | 2015 | quarters: 0.00 → 0.00 → 0.01 → 0.01

Numbers say: light vs heavy: width 35.0 → 60.6 px, dark 0.29 → 0.36; the long stroke does not run out of paint.

## Oil · Henry Ward · HW #09 white arches over wet blue-grey
Gouache 1.00 · 84 px · 46.9 s

![Oil · Henry Ward · HW #09 white arches over wet blue-grey](Oil-Henry-Ward-HW-09-white-arches-over-wet-blue-grey.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 13 % → 4 % | 39.1 px | 0.22 | 0.29 | 239 |
| heavy line | 19 % → 18 % | 54.3 px | 0.28 | 0.99 | 293 |
| pressure swell | 16 % → 14 % | 61.7 px | 0.30 | 0.86 | 221 |
| fast wave | 52 % → 43 % | 60.1 px | 0.36 | 0.83 | 973 |
| slow wave | 51 % → 40 % | 59.2 px | 0.29 | 0.79 | 1617 |
| spiral | 69 % → 41 % | 45.6 px | 0.31 | 0.59 | 1655 |
| loop | 48 % → 38 % | 62.4 px | 0.26 | 0.79 | 761 |
| tilted | 20 % → 20 % | 54.9 px | 0.32 | 1.00 | 558 |
| over the wet one | 38 % → 34 % | 52.0 px | 0.32 | 0.88 | 381 |
| long, no reload | 73 % → 48 % | 32.5 px | 0.34 | 0.66 | 1860 | quarters: 0.30 → 0.28 → 0.21 → 0.13

Numbers say: light vs heavy: width 39.1 → 54.3 px, dark 0.22 → 0.28.

## Oil · Henry Ward · HW #03 navy contours over wet band
Gouache 1.00 · 84 px · 47.4 s

![Oil · Henry Ward · HW #03 navy contours over wet band](Oil-Henry-Ward-HW-03-navy-contours-over-wet-band.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 13 % → 4 % | 39.1 px | 0.24 | 0.29 | 324 |
| heavy line | 19 % → 18 % | 54.3 px | 0.30 | 0.99 | 305 |
| pressure swell | 16 % → 14 % | 61.7 px | 0.31 | 0.86 | 221 |
| fast wave | 52 % → 43 % | 60.1 px | 0.38 | 0.83 | 899 |
| slow wave | 51 % → 40 % | 59.2 px | 0.31 | 0.79 | 1601 |
| spiral | 69 % → 41 % | 45.6 px | 0.32 | 0.59 | 1711 |
| loop | 48 % → 38 % | 62.4 px | 0.28 | 0.79 | 722 |
| tilted | 20 % → 20 % | 54.9 px | 0.34 | 1.00 | 464 |
| over the wet one | 38 % → 34 % | 52.0 px | 0.34 | 0.88 | 351 |
| long, no reload | 73 % → 48 % | 32.5 px | 0.36 | 0.66 | 1844 | quarters: 0.31 → 0.30 → 0.22 → 0.14

Numbers say: light vs heavy: width 39.1 → 54.3 px, dark 0.24 → 0.30.

## Oil · Henry Ward · HW #01 peach cloud and legs over teal
Gouache 1.00 · 84 px · 47.6 s

![Oil · Henry Ward · HW #01 peach cloud and legs over teal](Oil-Henry-Ward-HW-01-peach-cloud-and-legs-over-teal.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 12 % → 7 % | 35.0 px | 0.30 | 0.56 | 244 |
| heavy line | 21 % → 20 % | 60.6 px | 0.36 | 0.94 | 307 |
| pressure swell | 16 % → 14 % | 60.6 px | 0.34 | 0.89 | 238 |
| fast wave | 51 % → 44 % | 59.2 px | 0.27 | 0.85 | 1132 |
| slow wave | 53 % → 41 % | 61.3 px | 0.30 | 0.77 | 1506 |
| spiral | 66 % → 50 % | 43.3 px | 0.24 | 0.77 | 1437 |
| loop | 52 % → 36 % | 67.4 px | 0.29 | 0.68 | 761 |
| tilted | 19 % → 19 % | 52.9 px | 0.27 | 1.00 | 533 |
| over the wet one | 38 % → 34 % | 53.6 px | 0.27 | 0.89 | 342 |
| long, no reload | 77 % → 52 % | 34.7 px | 0.26 | 0.67 | 2018 | quarters: 0.00 → 0.00 → 0.01 → 0.01

Numbers say: light vs heavy: width 35.0 → 60.6 px, dark 0.30 → 0.36; the long stroke does not run out of paint.

## Oil · Henry Ward · HW #05 rust, pink, green-black
Gouache 1.00 · 84 px · 47.0 s

![Oil · Henry Ward · HW #05 rust, pink, green-black](Oil-Henry-Ward-HW-05-rust-pink-green-black.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 13 % → 4 % | 39.1 px | 0.40 | 0.29 | 322 |
| heavy line | 19 % → 18 % | 54.3 px | 0.47 | 0.99 | 458 |
| pressure swell | 16 % → 14 % | 61.7 px | 0.48 | 0.86 | 235 |
| fast wave | 52 % → 43 % | 60.1 px | 0.53 | 0.83 | 875 |
| slow wave | 51 % → 40 % | 59.2 px | 0.48 | 0.79 | 1358 |
| spiral | 69 % → 41 % | 45.6 px | 0.49 | 0.59 | 1681 |
| loop | 48 % → 38 % | 62.4 px | 0.45 | 0.79 | 749 |
| tilted | 20 % → 20 % | 54.9 px | 0.50 | 1.00 | 454 |
| over the wet one | 38 % → 34 % | 52.0 px | 0.50 | 0.88 | 340 |
| long, no reload | 73 % → 48 % | 32.5 px | 0.52 | 0.66 | 1834 | quarters: 0.47 → 0.45 → 0.36 → 0.23

Numbers say: light vs heavy: width 39.1 → 54.3 px, dark 0.40 → 0.47.

## Oil · Henry Ward · HW #07 blue L and zigzag on lilac
Gouache 1.00 · 90 px · 35.7 s

![Oil · Henry Ward · HW #07 blue L and zigzag on lilac](Oil-Henry-Ward-HW-07-blue-L-and-zigzag-on-lilac.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 8 % → 0 % | 23.8 px | 0.00 | 0.00 | 250 |
| heavy line | 17 % → 6 % | 50.1 px | 0.38 | 0.34 | 337 |
| pressure swell | 15 % → 6 % | 56.0 px | 0.36 | 0.42 | 208 |
| fast wave | 52 % → 16 % | 59.8 px | 0.33 | 0.31 | 1023 |
| slow wave | 40 % → 14 % | 46.4 px | 0.34 | 0.35 | 1606 |
| spiral | 68 % → 14 % | 44.7 px | 0.29 | 0.21 | 1439 |
| loop | 34 % → 4 % | 43.7 px | 0.29 | 0.12 | 656 |
| tilted | 19 % → 19 % | 51.8 px | 0.30 | 1.00 | 401 |
| over the wet one | 27 % → 12 % | 24.7 px | 0.30 | 0.45 | 288 |
| long, no reload | 53 % → 9 % | 23.7 px | 0.30 | 0.18 | 1688 | quarters: 0.04 → 0.02 → 0.03 → 0.05

Numbers say: light vs heavy: width 23.8 → 50.1 px, dark 0.00 → 0.38; the long stroke does not run out of paint.

## Oil · Henry Ward · HW #08 crown and dark oval
Gouache 1.00 · 84 px · 49.7 s

![Oil · Henry Ward · HW #08 crown and dark oval](Oil-Henry-Ward-HW-08-crown-and-dark-oval.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 13 % → 5 % | 36.9 px | 0.17 | 0.42 | 303 |
| heavy line | 21 % → 19 % | 60.8 px | 0.15 | 0.90 | 366 |
| pressure swell | 18 % → 16 % | 67.8 px | 0.17 | 0.89 | 244 |
| fast wave | 54 % → 44 % | 61.8 px | 0.26 | 0.82 | 858 |
| slow wave | 56 % → 47 % | 65.1 px | 0.17 | 0.83 | 1482 |
| spiral | 66 % → 48 % | 43.8 px | 0.22 | 0.73 | 1614 |
| loop | 53 % → 36 % | 68.2 px | 0.20 | 0.68 | 868 |
| tilted | 20 % → 20 % | 54.5 px | 0.21 | 1.00 | 464 |
| over the wet one | 37 % → 31 % | 49.1 px | 0.21 | 0.83 | 338 |
| long, no reload | 77 % → 50 % | 34.7 px | 0.24 | 0.65 | 1964 | quarters: 0.22 → 0.20 → 0.15 → 0.09

Numbers say: light vs heavy: width 36.9 → 60.8 px, dark 0.17 → 0.15.

## Oil · Henry Ward · HW #10 green block over maroon
Gouache 1.00 · 84 px · 47.6 s

![Oil · Henry Ward · HW #10 green block over maroon](Oil-Henry-Ward-HW-10-green-block-over-maroon.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 13 % → 5 % | 36.9 px | 0.15 | 0.42 | 247 |
| heavy line | 21 % → 19 % | 60.8 px | 0.13 | 0.90 | 328 |
| pressure swell | 18 % → 16 % | 67.8 px | 0.15 | 0.89 | 219 |
| fast wave | 54 % → 44 % | 61.8 px | 0.24 | 0.82 | 863 |
| slow wave | 56 % → 47 % | 65.1 px | 0.15 | 0.83 | 1512 |
| spiral | 66 % → 48 % | 43.8 px | 0.20 | 0.73 | 1605 |
| loop | 53 % → 36 % | 68.2 px | 0.17 | 0.68 | 718 |
| tilted | 20 % → 20 % | 54.5 px | 0.19 | 1.00 | 477 |
| over the wet one | 37 % → 31 % | 49.1 px | 0.19 | 0.83 | 310 |
| long, no reload | 77 % → 50 % | 34.7 px | 0.22 | 0.65 | 1913 | quarters: 0.20 → 0.19 → 0.14 → 0.08

Numbers say: light vs heavy: width 36.9 → 60.8 px, dark 0.15 → 0.13.

## Oil · Henry Ward · HW #11 cream mass and purple balls
Gouache 1.00 · 84 px · 47.5 s

![Oil · Henry Ward · HW #11 cream mass and purple balls](Oil-Henry-Ward-HW-11-cream-mass-and-purple-balls.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 13 % → 4 % | 39.1 px | 0.40 | 0.29 | 282 |
| heavy line | 19 % → 18 % | 54.3 px | 0.40 | 0.99 | 291 |
| pressure swell | 16 % → 14 % | 61.7 px | 0.35 | 0.86 | 213 |
| fast wave | 52 % → 43 % | 60.1 px | 0.30 | 0.83 | 828 |
| slow wave | 51 % → 40 % | 59.2 px | 0.37 | 0.79 | 1519 |
| spiral | 69 % → 41 % | 45.6 px | 0.33 | 0.59 | 1557 |
| loop | 48 % → 38 % | 62.4 px | 0.37 | 0.79 | 694 |
| tilted | 20 % → 20 % | 54.9 px | 0.33 | 1.00 | 481 |
| over the wet one | 38 % → 34 % | 52.0 px | 0.33 | 0.88 | 370 |
| long, no reload | 73 % → 48 % | 32.5 px | 0.31 | 0.66 | 2049 | quarters: 0.00 → 0.00 → 0.01 → 0.02

Numbers say: light vs heavy: width 39.1 → 54.3 px, dark 0.40 → 0.40; the long stroke does not run out of paint.

## Oil · Henry Ward · HW #13 blue scrub under red
Gouache 1.00 · 84 px · 48.6 s

![Oil · Henry Ward · HW #13 blue scrub under red](Oil-Henry-Ward-HW-13-blue-scrub-under-red.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 12 % → 7 % | 35.0 px | 0.55 | 0.56 | 241 |
| heavy line | 21 % → 20 % | 60.6 px | 0.53 | 0.94 | 309 |
| pressure swell | 16 % → 14 % | 60.6 px | 0.52 | 0.89 | 222 |
| fast wave | 51 % → 44 % | 59.2 px | 0.58 | 0.85 | 1045 |
| slow wave | 53 % → 41 % | 61.3 px | 0.56 | 0.77 | 1486 |
| spiral | 66 % → 50 % | 43.3 px | 0.60 | 0.77 | 1441 |
| loop | 52 % → 36 % | 67.4 px | 0.55 | 0.68 | 777 |
| tilted | 19 % → 19 % | 52.9 px | 0.58 | 1.00 | 537 |
| over the wet one | 38 % → 34 % | 53.6 px | 0.58 | 0.89 | 383 |
| long, no reload | 77 % → 52 % | 34.7 px | 0.58 | 0.67 | 2091 | quarters: 0.56 → 0.53 → 0.45 → 0.29

Numbers say: light vs heavy: width 35.0 → 60.6 px, dark 0.55 → 0.53.

## Oil · Henry Ward · HW #14 olive totem on dark
Gouache 1.00 · 84 px · 48.5 s

![Oil · Henry Ward · HW #14 olive totem on dark](Oil-Henry-Ward-HW-14-olive-totem-on-dark.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 13 % → 5 % | 36.9 px | 0.23 | 0.42 | 232 |
| heavy line | 21 % → 19 % | 60.8 px | 0.21 | 0.90 | 307 |
| pressure swell | 18 % → 16 % | 67.8 px | 0.23 | 0.89 | 258 |
| fast wave | 54 % → 44 % | 61.8 px | 0.31 | 0.82 | 821 |
| slow wave | 56 % → 47 % | 65.1 px | 0.23 | 0.83 | 1574 |
| spiral | 66 % → 48 % | 43.8 px | 0.28 | 0.73 | 1513 |
| loop | 53 % → 36 % | 68.2 px | 0.25 | 0.68 | 835 |
| tilted | 20 % → 20 % | 54.5 px | 0.27 | 1.00 | 491 |
| over the wet one | 37 % → 31 % | 49.1 px | 0.27 | 0.83 | 307 |
| long, no reload | 77 % → 50 % | 34.7 px | 0.29 | 0.65 | 2134 | quarters: 0.27 → 0.25 → 0.19 → 0.11

Numbers say: light vs heavy: width 36.9 → 60.8 px, dark 0.23 → 0.21.

## Oil · Henry Ward · Ground #2b2f1c flat
Gouache 1.00 · 160 px · 79.2 s

![Oil · Henry Ward · Ground #2b2f1c flat](Oil-Henry-Ward-Ground-2b2f1c-flat.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 51 % → 46 % | 148.3 px | 0.52 | 0.89 | 813 |
| heavy line | 52 % → 47 % | 151.5 px | 0.52 | 0.91 | 877 |
| pressure swell | 41 % → 45 % | 154.8 px | 0.52 | 1.10 | 615 |
| fast wave | 85 % → 86 % | 97.8 px | 0.52 | 1.01 | 2356 |
| slow wave | 86 % → 73 % | 99.2 px | 0.52 | 0.86 | 4507 |
| spiral | 88 % → 69 % | 58.3 px | 0.52 | 0.77 | 4226 |
| loop | 75 % → 69 % | 97.0 px | 0.52 | 0.92 | 1928 |
| tilted | 39 % → 39 % | 107.5 px | 0.52 | 1.00 | 1147 |
| over the wet one | 76 % → 71 % | 104.6 px | 0.52 | 0.93 | 962 |
| long, no reload | 98 % → 87 % | 44.0 px | 0.52 | 0.88 | 5903 | quarters: 0.52 → 0.52 → 0.52 → 0.50

Numbers say: light vs heavy: width 148.3 → 151.5 px, dark 0.52 → 0.52; pressure barely changes the width; the long stroke does not run out of paint.

## Oil · Henry Ward · Thin veil #2b3a44 flat
Oil 0.81 · Ink 0.19 · 96 px · 51.4 s

![Oil · Henry Ward · Thin veil #2b3a44 flat](Oil-Henry-Ward-Thin-veil-2b3a44-flat.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 9 % → 4 % | 24.9 px | 0.56 | 0.51 | 290 |
| heavy line | 22 % → 20 % | 65.2 px | 0.63 | 0.89 | 409 |
| pressure swell | 20 % → 18 % | 73.8 px | 0.59 | 0.91 | 286 |
| fast wave | 59 % → 58 % | 68.4 px | 0.65 | 0.98 | 1183 |
| slow wave | 58 % → 51 % | 67.1 px | 0.65 | 0.89 | 2008 |
| spiral | 83 % → 67 % | 55.0 px | 0.70 | 0.80 | 1997 |
| loop | 57 % → 49 % | 74.0 px | 0.62 | 0.85 | 878 |
| tilted | 23 % → 23 % | 63.1 px | 0.64 | 1.01 | 595 |
| over the wet one | 36 % → 34 % | 38.7 px | 0.64 | 0.93 | 396 |
| long, no reload | 82 % → 70 % | 36.7 px | 0.67 | 0.85 | 2305 | quarters: 0.65 → 0.61 → 0.54 → 0.28

Numbers say: light vs heavy: width 24.9 → 65.2 px, dark 0.56 → 0.63.

## Oil · Henry Ward · Loaded flat #ece6c0 flat
Gouache 1.00 · 84 px · 48.9 s

![Oil · Henry Ward · Loaded flat #ece6c0 flat](Oil-Henry-Ward-Loaded-flat-ece6c0-flat.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 13 % → 4 % | 39.1 px | 0.40 | 0.29 | 345 |
| heavy line | 19 % → 18 % | 54.3 px | 0.42 | 0.99 | 316 |
| pressure swell | 16 % → 14 % | 61.7 px | 0.37 | 0.86 | 232 |
| fast wave | 52 % → 43 % | 60.1 px | 0.32 | 0.83 | 899 |
| slow wave | 51 % → 40 % | 59.2 px | 0.39 | 0.79 | 1462 |
| spiral | 69 % → 41 % | 45.6 px | 0.35 | 0.59 | 1645 |
| loop | 48 % → 38 % | 62.4 px | 0.39 | 0.79 | 778 |
| tilted | 20 % → 20 % | 54.9 px | 0.35 | 1.00 | 476 |
| over the wet one | 38 % → 34 % | 52.0 px | 0.35 | 0.88 | 365 |
| long, no reload | 73 % → 48 % | 32.5 px | 0.33 | 0.66 | 1758 | quarters: 0.00 → 0.00 → 0.01 → 0.02

Numbers say: light vs heavy: width 39.1 → 54.3 px, dark 0.40 → 0.42; the long stroke does not run out of paint.

## Oil · Henry Ward · Dry scrub #ece6c0 filbert
Gouache 1.00 · 90 px · 37.5 s

![Oil · Henry Ward · Dry scrub #ece6c0 filbert](Oil-Henry-Ward-Dry-scrub-ece6c0-filbert.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 8 % → 0 % | 23.8 px | 0.00 | 0.00 | 283 |
| heavy line | 17 % → 6 % | 50.1 px | 0.38 | 0.34 | 324 |
| pressure swell | 15 % → 6 % | 56.0 px | 0.35 | 0.42 | 236 |
| fast wave | 52 % → 16 % | 59.8 px | 0.31 | 0.31 | 856 |
| slow wave | 40 % → 14 % | 46.4 px | 0.33 | 0.35 | 1486 |
| spiral | 68 % → 14 % | 44.7 px | 0.27 | 0.21 | 1408 |
| loop | 34 % → 4 % | 43.7 px | 0.27 | 0.12 | 622 |
| tilted | 19 % → 19 % | 51.8 px | 0.28 | 1.00 | 450 |
| over the wet one | 27 % → 12 % | 24.7 px | 0.28 | 0.45 | 295 |
| long, no reload | 53 % → 9 % | 23.7 px | 0.28 | 0.18 | 1672 | quarters: 0.03 → 0.02 → 0.03 → 0.05

Numbers say: light vs heavy: width 23.8 → 50.1 px, dark 0.00 → 0.38; the long stroke does not run out of paint.

## Oil · Henry Ward · Ground #8a6a20 flat
Gouache 1.00 · 160 px · 79.7 s

![Oil · Henry Ward · Ground #8a6a20 flat](Oil-Henry-Ward-Ground-8a6a20-flat.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 51 % → 46 % | 148.3 px | 0.32 | 0.89 | 811 |
| heavy line | 52 % → 47 % | 151.5 px | 0.32 | 0.91 | 886 |
| pressure swell | 41 % → 45 % | 154.8 px | 0.32 | 1.10 | 640 |
| fast wave | 85 % → 86 % | 97.8 px | 0.33 | 1.01 | 2343 |
| slow wave | 86 % → 73 % | 99.2 px | 0.32 | 0.86 | 3945 |
| spiral | 88 % → 69 % | 58.3 px | 0.32 | 0.77 | 4269 |
| loop | 75 % → 69 % | 97.0 px | 0.32 | 0.92 | 2207 |
| tilted | 39 % → 39 % | 107.5 px | 0.32 | 1.00 | 1286 |
| over the wet one | 76 % → 71 % | 104.6 px | 0.32 | 0.93 | 1054 |
| long, no reload | 98 % → 87 % | 44.0 px | 0.32 | 0.88 | 6861 | quarters: 0.32 → 0.32 → 0.32 → 0.29

Numbers say: light vs heavy: width 148.3 → 151.5 px, dark 0.32 → 0.32; pressure barely changes the width; the long stroke does not run out of paint.

## Oil · Henry Ward · Loaded flat #b8bcc0 filbert
Gouache 1.00 · 84 px · 51.1 s

![Oil · Henry Ward · Loaded flat #b8bcc0 filbert](Oil-Henry-Ward-Loaded-flat-b8bcc0-filbert.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 12 % → 7 % | 35.0 px | 0.29 | 0.56 | 228 |
| heavy line | 21 % → 20 % | 60.6 px | 0.36 | 0.94 | 309 |
| pressure swell | 16 % → 14 % | 60.6 px | 0.34 | 0.89 | 212 |
| fast wave | 51 % → 44 % | 59.2 px | 0.26 | 0.85 | 868 |
| slow wave | 53 % → 41 % | 61.3 px | 0.30 | 0.77 | 1910 |
| spiral | 66 % → 50 % | 43.3 px | 0.24 | 0.77 | 1783 |
| loop | 52 % → 36 % | 67.4 px | 0.29 | 0.68 | 1088 |
| tilted | 19 % → 19 % | 52.9 px | 0.26 | 1.00 | 575 |
| over the wet one | 38 % → 34 % | 53.6 px | 0.26 | 0.89 | 324 |
| long, no reload | 77 % → 52 % | 34.7 px | 0.25 | 0.67 | 2587 | quarters: 0.00 → 0.00 → 0.01 → 0.01

Numbers say: light vs heavy: width 35.0 → 60.6 px, dark 0.29 → 0.36; the long stroke does not run out of paint.

## Oil · Henry Ward · Dry scrub #c8ccd0 round
Gouache 1.00 · 90 px · 37.6 s

![Oil · Henry Ward · Dry scrub #c8ccd0 round](Oil-Henry-Ward-Dry-scrub-c8ccd0-round.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 8 % → 0 % | 24.6 px | 0.00 | 0.00 | 215 |
| heavy line | 15 % → 2 % | 42.5 px | 0.33 | 0.15 | 432 |
| pressure swell | 13 % → 7 % | 48.5 px | 0.34 | 0.52 | 214 |
| fast wave | 54 % → 11 % | 62.6 px | 0.26 | 0.21 | 960 |
| slow wave | 42 % → 20 % | 48.8 px | 0.30 | 0.48 | 1797 |
| spiral | 78 % → 18 % | 51.6 px | 0.24 | 0.23 | 1831 |
| loop | 34 % → 4 % | 44.5 px | 0.24 | 0.12 | 936 |
| tilted | 19 % → 19 % | 51.9 px | 0.25 | 1.00 | 467 |
| over the wet one | 27 % → 11 % | 23.4 px | 0.25 | 0.40 | 387 |
| long, no reload | 45 % → 2 % | 20.3 px | 0.22 | 0.04 | 1884 | quarters: 0.03 → 0.02 → 0.03 → 0.04

Numbers say: light vs heavy: width 24.6 → 42.5 px, dark 0.00 → 0.33; the long stroke does not run out of paint.

## Oil · Henry Ward · Wet drag #9ea4aa flat
Gouache 1.00 · 80 px · 43.4 s

![Oil · Henry Ward · Wet drag #9ea4aa flat](Oil-Henry-Ward-Wet-drag-9ea4aa-flat.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 12 % → 2 % | 36.2 px | 0.19 | 0.17 | 251 |
| heavy line | 17 % → 13 % | 50.1 px | 0.15 | 0.75 | 430 |
| pressure swell | 16 % → 9 % | 60.0 px | 0.19 | 0.54 | 209 |
| fast wave | 45 % → 17 % | 52.3 px | 0.24 | 0.37 | 925 |
| slow wave | 51 % → 26 % | 58.6 px | 0.14 | 0.51 | 1635 |
| spiral | 67 % → 33 % | 44.5 px | 0.22 | 0.49 | 1928 |
| loop | 44 % → 21 % | 57.5 px | 0.11 | 0.46 | 860 |
| tilted | 19 % → 19 % | 53.3 px | 0.23 | 1.00 | 501 |
| over the wet one | 38 % → 29 % | 53.1 px | 0.23 | 0.76 | 328 |
| long, no reload | 74 % → 34 % | 33.3 px | 0.22 | 0.45 | 1872 | quarters: 0.19 → 0.17 → 0.10 → 0.07

Numbers say: light vs heavy: width 36.2 → 50.1 px, dark 0.19 → 0.15.

## Oil · Henry Ward · Ground #e8b4a8 flat
Gouache 1.00 · 160 px · 80.3 s

![Oil · Henry Ward · Ground #e8b4a8 flat](Oil-Henry-Ward-Ground-e8b4a8-flat.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 51 % → 46 % | 148.3 px | 0.30 | 0.89 | 878 |
| heavy line | 52 % → 47 % | 151.5 px | 0.30 | 0.91 | 1072 |
| pressure swell | 41 % → 45 % | 154.8 px | 0.30 | 1.10 | 794 |
| fast wave | 85 % → 86 % | 97.8 px | 0.29 | 1.01 | 2654 |
| slow wave | 86 % → 73 % | 99.2 px | 0.30 | 0.86 | 4467 |
| spiral | 88 % → 69 % | 58.3 px | 0.30 | 0.77 | 4292 |
| loop | 75 % → 69 % | 97.0 px | 0.30 | 0.92 | 2282 |
| tilted | 39 % → 39 % | 107.5 px | 0.30 | 1.00 | 1306 |
| over the wet one | 76 % → 71 % | 104.6 px | 0.30 | 0.93 | 1141 |
| long, no reload | 98 % → 87 % | 44.0 px | 0.30 | 0.88 | 6366 | quarters: 0.00 → 0.00 → 0.00 → 0.00

Numbers say: light vs heavy: width 148.3 → 151.5 px, dark 0.30 → 0.30; pressure barely changes the width.

## Oil · Henry Ward · Loaded flat #6e7f90 flat
Gouache 1.00 · 84 px · 52.2 s

![Oil · Henry Ward · Loaded flat #6e7f90 flat](Oil-Henry-Ward-Loaded-flat-6e7f90-flat.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 13 % → 4 % | 39.1 px | 0.22 | 0.29 | 268 |
| heavy line | 19 % → 18 % | 54.3 px | 0.28 | 0.99 | 330 |
| pressure swell | 16 % → 14 % | 61.7 px | 0.30 | 0.86 | 310 |
| fast wave | 52 % → 43 % | 60.1 px | 0.36 | 0.83 | 937 |
| slow wave | 51 % → 40 % | 59.2 px | 0.29 | 0.79 | 1537 |
| spiral | 69 % → 41 % | 45.6 px | 0.31 | 0.59 | 1615 |
| loop | 48 % → 38 % | 62.4 px | 0.26 | 0.79 | 846 |
| tilted | 20 % → 20 % | 54.9 px | 0.32 | 1.00 | 615 |
| over the wet one | 38 % → 34 % | 52.0 px | 0.32 | 0.88 | 515 |
| long, no reload | 73 % → 48 % | 32.5 px | 0.34 | 0.66 | 2244 | quarters: 0.30 → 0.28 → 0.21 → 0.13

Numbers say: light vs heavy: width 39.1 → 54.3 px, dark 0.22 → 0.28.

## Oil · Henry Ward · Loaded flat #f6f6f2 filbert
Gouache 1.00 · 84 px · 50.6 s

![Oil · Henry Ward · Loaded flat #f6f6f2 filbert](Oil-Henry-Ward-Loaded-flat-f6f6f2-filbert.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 12 % → 7 % | 35.0 px | 0.38 | 0.56 | 277 |
| heavy line | 21 % → 20 % | 60.6 px | 0.45 | 0.94 | 346 |
| pressure swell | 16 % → 14 % | 60.6 px | 0.41 | 0.89 | 234 |
| fast wave | 51 % → 44 % | 59.2 px | 0.37 | 0.85 | 1038 |
| slow wave | 53 % → 41 % | 61.3 px | 0.40 | 0.77 | 1643 |
| spiral | 66 % → 50 % | 43.3 px | 0.35 | 0.77 | 1761 |
| loop | 52 % → 36 % | 67.4 px | 0.38 | 0.68 | 886 |
| tilted | 19 % → 19 % | 52.9 px | 0.37 | 1.00 | 590 |
| over the wet one | 38 % → 34 % | 53.6 px | 0.37 | 0.89 | 427 |
| long, no reload | 77 % → 52 % | 34.7 px | 0.36 | 0.67 | 2246 | quarters: 0.00 → 0.00 → 0.01 → 0.02

Numbers say: light vs heavy: width 35.0 → 60.6 px, dark 0.38 → 0.45; the long stroke does not run out of paint.

## Oil · Henry Ward · Dry scrub #f6f6f2 filbert
Gouache 1.00 · 90 px · 38.7 s

![Oil · Henry Ward · Dry scrub #f6f6f2 filbert](Oil-Henry-Ward-Dry-scrub-f6f6f2-filbert.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 8 % → 0 % | 23.8 px | 0.00 | 0.00 | 251 |
| heavy line | 17 % → 6 % | 50.1 px | 0.39 | 0.34 | 381 |
| pressure swell | 15 % → 6 % | 56.0 px | 0.36 | 0.42 | 259 |
| fast wave | 52 % → 16 % | 59.8 px | 0.33 | 0.31 | 1035 |
| slow wave | 40 % → 14 % | 46.4 px | 0.35 | 0.35 | 1846 |
| spiral | 68 % → 14 % | 44.7 px | 0.30 | 0.21 | 1631 |
| loop | 34 % → 4 % | 43.7 px | 0.30 | 0.12 | 741 |
| tilted | 19 % → 19 % | 51.8 px | 0.31 | 1.00 | 501 |
| over the wet one | 27 % → 12 % | 24.7 px | 0.31 | 0.45 | 290 |
| long, no reload | 53 % → 9 % | 23.7 px | 0.31 | 0.18 | 1777 | quarters: 0.04 → 0.02 → 0.03 → 0.05

Numbers say: light vs heavy: width 23.8 → 50.1 px, dark 0.00 → 0.39; the long stroke does not run out of paint.

## Oil · Henry Ward · Ground #e8e2da flat
Gouache 1.00 · 160 px · 78.1 s

![Oil · Henry Ward · Ground #e8e2da flat](Oil-Henry-Ward-Ground-e8e2da-flat.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 51 % → 46 % | 148.3 px | 0.38 | 0.89 | 799 |
| heavy line | 52 % → 47 % | 151.5 px | 0.38 | 0.91 | 1003 |
| pressure swell | 41 % → 45 % | 154.8 px | 0.38 | 1.10 | 834 |
| fast wave | 85 % → 86 % | 97.8 px | 0.37 | 1.01 | 2695 |
| slow wave | 86 % → 73 % | 99.2 px | 0.38 | 0.86 | 4374 |
| spiral | 88 % → 69 % | 58.3 px | 0.38 | 0.77 | 4006 |
| loop | 75 % → 69 % | 97.0 px | 0.38 | 0.92 | 2330 |
| tilted | 39 % → 39 % | 107.5 px | 0.38 | 1.00 | 1197 |
| over the wet one | 76 % → 71 % | 104.6 px | 0.38 | 0.93 | 1034 |
| long, no reload | 98 % → 87 % | 44.0 px | 0.38 | 0.88 | 6288 | quarters: 0.00 → 0.00 → 0.00 → 0.00

Numbers say: light vs heavy: width 148.3 → 151.5 px, dark 0.38 → 0.38; pressure barely changes the width.

## Oil · Henry Ward · Loaded flat #6a7a80 flat
Gouache 1.00 · 84 px · 48.6 s

![Oil · Henry Ward · Loaded flat #6a7a80 flat](Oil-Henry-Ward-Loaded-flat-6a7a80-flat.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 13 % → 4 % | 39.1 px | 0.24 | 0.29 | 263 |
| heavy line | 19 % → 18 % | 54.3 px | 0.30 | 0.99 | 340 |
| pressure swell | 16 % → 14 % | 61.7 px | 0.31 | 0.86 | 268 |
| fast wave | 52 % → 43 % | 60.1 px | 0.38 | 0.83 | 876 |
| slow wave | 51 % → 40 % | 59.2 px | 0.31 | 0.79 | 1361 |
| spiral | 69 % → 41 % | 45.6 px | 0.32 | 0.59 | 1721 |
| loop | 48 % → 38 % | 62.4 px | 0.28 | 0.79 | 757 |
| tilted | 20 % → 20 % | 54.9 px | 0.34 | 1.00 | 562 |
| over the wet one | 38 % → 34 % | 52.0 px | 0.34 | 0.88 | 366 |
| long, no reload | 73 % → 48 % | 32.5 px | 0.36 | 0.66 | 2008 | quarters: 0.31 → 0.30 → 0.22 → 0.14

Numbers say: light vs heavy: width 39.1 → 54.3 px, dark 0.24 → 0.30.

## Oil · Henry Ward · Loaded flat #5a1810 flat
Gouache 1.00 · 84 px · 48.8 s

![Oil · Henry Ward · Loaded flat #5a1810 flat](Oil-Henry-Ward-Loaded-flat-5a1810-flat.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 13 % → 4 % | 39.1 px | 0.57 | 0.29 | 264 |
| heavy line | 19 % → 18 % | 54.3 px | 0.62 | 0.99 | 329 |
| pressure swell | 16 % → 14 % | 61.7 px | 0.61 | 0.86 | 219 |
| fast wave | 52 % → 43 % | 60.1 px | 0.64 | 0.83 | 905 |
| slow wave | 51 % → 40 % | 59.2 px | 0.62 | 0.79 | 1610 |
| spiral | 69 % → 41 % | 45.6 px | 0.61 | 0.59 | 1850 |
| loop | 48 % → 38 % | 62.4 px | 0.60 | 0.79 | 836 |
| tilted | 20 % → 20 % | 54.9 px | 0.62 | 1.00 | 543 |
| over the wet one | 38 % → 34 % | 52.0 px | 0.62 | 0.88 | 374 |
| long, no reload | 73 % → 48 % | 32.5 px | 0.63 | 0.66 | 2136 | quarters: 0.59 → 0.55 → 0.46 → 0.29

Numbers say: light vs heavy: width 39.1 → 54.3 px, dark 0.57 → 0.62.

## Oil · Henry Ward · Dirty contour #1c2240 flat
Gouache 1.00 · 34 px · 37.5 s

![Oil · Henry Ward · Dirty contour #1c2240 flat](Oil-Henry-Ward-Dirty-contour-1c2240-flat.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 10 % → 8 % | 29.7 px | 0.64 | 0.78 | 169 |
| heavy line | 12 % → 11 % | 33.9 px | 0.63 | 0.92 | 113 |
| pressure swell | 9 % → 8 % | 32.4 px | 0.68 | 0.96 | 97 |
| fast wave | 23 % → 20 % | 26.4 px | 0.74 | 0.88 | 339 |
| slow wave | 28 % → 25 % | 32.6 px | 0.68 | 0.87 | 641 |
| spiral | 39 % → 24 % | 25.4 px | 0.72 | 0.63 | 714 |
| loop | 21 % → 20 % | 27.5 px | 0.68 | 0.93 | 306 |
| tilted | 10 % → 10 % | 28.6 px | 0.69 | 1.02 | 171 |
| over the wet one | 22 % → 21 % | 32.3 px | 0.69 | 0.96 | 154 |
| long, no reload | 47 % → 28 % | 20.9 px | 0.70 | 0.61 | 837 | quarters: 0.46 → 0.41 → 0.31 → 0.28

Numbers say: light vs heavy: width 29.7 → 33.9 px, dark 0.64 → 0.63.

## Oil · Henry Ward · Ground #22403f flat
Gouache 1.00 · 160 px · 78.7 s

![Oil · Henry Ward · Ground #22403f flat](Oil-Henry-Ward-Ground-22403f-flat.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 51 % → 46 % | 148.3 px | 0.48 | 0.89 | 798 |
| heavy line | 52 % → 47 % | 151.5 px | 0.48 | 0.91 | 997 |
| pressure swell | 41 % → 45 % | 154.8 px | 0.48 | 1.10 | 716 |
| fast wave | 85 % → 86 % | 97.8 px | 0.48 | 1.01 | 2654 |
| slow wave | 86 % → 73 % | 99.2 px | 0.48 | 0.86 | 4655 |
| spiral | 88 % → 69 % | 58.3 px | 0.48 | 0.77 | 4043 |
| loop | 75 % → 69 % | 97.0 px | 0.48 | 0.92 | 2111 |
| tilted | 39 % → 39 % | 107.5 px | 0.48 | 1.00 | 1184 |
| over the wet one | 76 % → 71 % | 104.6 px | 0.48 | 0.93 | 1021 |
| long, no reload | 98 % → 87 % | 44.0 px | 0.48 | 0.88 | 6656 | quarters: 0.48 → 0.48 → 0.48 → 0.46

Numbers say: light vs heavy: width 148.3 → 151.5 px, dark 0.48 → 0.48; pressure barely changes the width; the long stroke does not run out of paint.

## Oil · Henry Ward · Loaded flat #f0b89a filbert
Gouache 1.00 · 84 px · 50.1 s

![Oil · Henry Ward · Loaded flat #f0b89a filbert](Oil-Henry-Ward-Loaded-flat-f0b89a-filbert.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 12 % → 7 % | 35.0 px | 0.30 | 0.56 | 254 |
| heavy line | 21 % → 20 % | 60.6 px | 0.36 | 0.94 | 351 |
| pressure swell | 16 % → 14 % | 60.6 px | 0.34 | 0.89 | 248 |
| fast wave | 51 % → 44 % | 59.2 px | 0.27 | 0.85 | 987 |
| slow wave | 53 % → 41 % | 61.3 px | 0.30 | 0.77 | 1475 |
| spiral | 66 % → 50 % | 43.3 px | 0.24 | 0.77 | 1697 |
| loop | 52 % → 36 % | 67.4 px | 0.29 | 0.68 | 787 |
| tilted | 19 % → 19 % | 52.9 px | 0.27 | 1.00 | 489 |
| over the wet one | 38 % → 34 % | 53.6 px | 0.27 | 0.89 | 346 |
| long, no reload | 77 % → 52 % | 34.7 px | 0.26 | 0.67 | 2130 | quarters: 0.00 → 0.00 → 0.01 → 0.01

Numbers say: light vs heavy: width 35.0 → 60.6 px, dark 0.30 → 0.36; the long stroke does not run out of paint.

## Oil · Henry Ward · Dry scrub #f0b89a filbert
Gouache 1.00 · 90 px · 38.9 s

![Oil · Henry Ward · Dry scrub #f0b89a filbert](Oil-Henry-Ward-Dry-scrub-f0b89a-filbert.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 8 % → 0 % | 23.8 px | 0.00 | 0.00 | 256 |
| heavy line | 17 % → 6 % | 50.1 px | 0.34 | 0.34 | 364 |
| pressure swell | 15 % → 6 % | 56.0 px | 0.30 | 0.42 | 218 |
| fast wave | 52 % → 16 % | 59.8 px | 0.26 | 0.31 | 1003 |
| slow wave | 40 % → 14 % | 46.4 px | 0.29 | 0.35 | 1593 |
| spiral | 68 % → 14 % | 44.7 px | 0.20 | 0.21 | 1604 |
| loop | 34 % → 4 % | 43.7 px | 0.22 | 0.12 | 776 |
| tilted | 19 % → 19 % | 51.8 px | 0.21 | 1.00 | 418 |
| over the wet one | 27 % → 12 % | 24.7 px | 0.21 | 0.45 | 301 |
| long, no reload | 53 % → 9 % | 23.7 px | 0.21 | 0.18 | 1753 | quarters: 0.03 → 0.01 → 0.02 → 0.04

Numbers say: light vs heavy: width 23.8 → 50.1 px, dark 0.00 → 0.34; the long stroke does not run out of paint.

## Oil · Henry Ward · Dirty contour #1c2238 flat
Gouache 1.00 · 34 px · 38.0 s

![Oil · Henry Ward · Dirty contour #1c2238 flat](Oil-Henry-Ward-Dirty-contour-1c2238-flat.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 10 % → 8 % | 29.7 px | 0.64 | 0.78 | 139 |
| heavy line | 12 % → 11 % | 33.9 px | 0.64 | 0.92 | 155 |
| pressure swell | 9 % → 8 % | 32.4 px | 0.69 | 0.96 | 107 |
| fast wave | 23 % → 20 % | 26.4 px | 0.74 | 0.88 | 319 |
| slow wave | 28 % → 25 % | 32.6 px | 0.68 | 0.87 | 681 |
| spiral | 39 % → 24 % | 25.4 px | 0.72 | 0.63 | 608 |
| loop | 21 % → 20 % | 27.5 px | 0.68 | 0.93 | 366 |
| tilted | 10 % → 10 % | 28.6 px | 0.69 | 1.02 | 185 |
| over the wet one | 22 % → 21 % | 32.3 px | 0.69 | 0.96 | 173 |
| long, no reload | 47 % → 28 % | 20.9 px | 0.70 | 0.61 | 913 | quarters: 0.46 → 0.41 → 0.31 → 0.29

Numbers say: light vs heavy: width 29.7 → 33.9 px, dark 0.64 → 0.64.

## Oil · Henry Ward · Ground #ece8e2 flat
Gouache 1.00 · 160 px · 79.0 s

![Oil · Henry Ward · Ground #ece8e2 flat](Oil-Henry-Ward-Ground-ece8e2-flat.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 51 % → 46 % | 148.3 px | 0.39 | 0.89 | 799 |
| heavy line | 52 % → 47 % | 151.5 px | 0.39 | 0.91 | 906 |
| pressure swell | 41 % → 45 % | 154.8 px | 0.39 | 1.10 | 661 |
| fast wave | 85 % → 86 % | 97.8 px | 0.38 | 1.01 | 2539 |
| slow wave | 86 % → 73 % | 99.2 px | 0.39 | 0.86 | 4636 |
| spiral | 88 % → 69 % | 58.3 px | 0.39 | 0.77 | 4050 |
| loop | 75 % → 69 % | 97.0 px | 0.39 | 0.92 | 2078 |
| tilted | 39 % → 39 % | 107.5 px | 0.39 | 1.00 | 1083 |
| over the wet one | 76 % → 71 % | 104.6 px | 0.39 | 0.93 | 1014 |
| long, no reload | 98 % → 87 % | 44.0 px | 0.39 | 0.88 | 6125 | quarters: 0.00 → 0.00 → 0.00 → 0.00

Numbers say: light vs heavy: width 148.3 → 151.5 px, dark 0.39 → 0.39; pressure barely changes the width.

## Oil · Henry Ward · Loaded flat #a03c1c flat
Gouache 1.00 · 84 px · 49.3 s

![Oil · Henry Ward · Loaded flat #a03c1c flat](Oil-Henry-Ward-Loaded-flat-a03c1c-flat.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 13 % → 4 % | 39.1 px | 0.40 | 0.29 | 284 |
| heavy line | 19 % → 18 % | 54.3 px | 0.47 | 0.99 | 295 |
| pressure swell | 16 % → 14 % | 61.7 px | 0.48 | 0.86 | 237 |
| fast wave | 52 % → 43 % | 60.1 px | 0.53 | 0.83 | 1001 |
| slow wave | 51 % → 40 % | 59.2 px | 0.48 | 0.79 | 1470 |
| spiral | 69 % → 41 % | 45.6 px | 0.49 | 0.59 | 1664 |
| loop | 48 % → 38 % | 62.4 px | 0.45 | 0.79 | 729 |
| tilted | 20 % → 20 % | 54.9 px | 0.50 | 1.00 | 498 |
| over the wet one | 38 % → 34 % | 52.0 px | 0.50 | 0.88 | 442 |
| long, no reload | 73 % → 48 % | 32.5 px | 0.52 | 0.66 | 1826 | quarters: 0.47 → 0.45 → 0.36 → 0.23

Numbers say: light vs heavy: width 39.1 → 54.3 px, dark 0.40 → 0.47.

## Oil · Henry Ward · Dirty contour #1f3a2c flat
Gouache 1.00 · 34 px · 37.0 s

![Oil · Henry Ward · Dirty contour #1f3a2c flat](Oil-Henry-Ward-Dirty-contour-1f3a2c-flat.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 10 % → 8 % | 29.7 px | 0.56 | 0.78 | 141 |
| heavy line | 12 % → 11 % | 33.9 px | 0.56 | 0.92 | 151 |
| pressure swell | 9 % → 8 % | 32.4 px | 0.62 | 0.96 | 97 |
| fast wave | 23 % → 20 % | 26.4 px | 0.67 | 0.88 | 352 |
| slow wave | 28 % → 25 % | 32.6 px | 0.61 | 0.87 | 600 |
| spiral | 39 % → 24 % | 25.4 px | 0.65 | 0.63 | 591 |
| loop | 21 % → 20 % | 27.5 px | 0.60 | 0.93 | 365 |
| tilted | 10 % → 10 % | 28.6 px | 0.62 | 1.02 | 190 |
| over the wet one | 22 % → 21 % | 32.3 px | 0.62 | 0.96 | 142 |
| long, no reload | 47 % → 28 % | 20.9 px | 0.62 | 0.61 | 885 | quarters: 0.41 → 0.37 → 0.27 → 0.25

Numbers say: light vs heavy: width 29.7 → 33.9 px, dark 0.56 → 0.56.

## Oil · Henry Ward · Loaded flat #ecc8c8 round
Gouache 1.00 · 84 px · 50.9 s

![Oil · Henry Ward · Loaded flat #ecc8c8 round](Oil-Henry-Ward-Loaded-flat-ecc8c8-round.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 13 % → 5 % | 36.9 px | 0.36 | 0.42 | 276 |
| heavy line | 21 % → 19 % | 60.8 px | 0.39 | 0.90 | 378 |
| pressure swell | 18 % → 16 % | 67.8 px | 0.36 | 0.89 | 206 |
| fast wave | 54 % → 44 % | 61.8 px | 0.28 | 0.82 | 936 |
| slow wave | 56 % → 47 % | 65.1 px | 0.36 | 0.83 | 1666 |
| spiral | 66 % → 48 % | 43.8 px | 0.31 | 0.73 | 1760 |
| loop | 53 % → 36 % | 68.2 px | 0.32 | 0.68 | 929 |
| tilted | 20 % → 20 % | 54.5 px | 0.32 | 1.00 | 516 |
| over the wet one | 37 % → 31 % | 49.1 px | 0.32 | 0.83 | 333 |
| long, no reload | 77 % → 50 % | 34.7 px | 0.29 | 0.65 | 2020 | quarters: 0.00 → 0.00 → 0.01 → 0.02

Numbers say: light vs heavy: width 36.9 → 60.8 px, dark 0.36 → 0.39; the long stroke does not run out of paint.

## Oil · Henry Ward · Loaded flat #62c8e8 flat
Gouache 1.00 · 84 px · 49.2 s

![Oil · Henry Ward · Loaded flat #62c8e8 flat](Oil-Henry-Ward-Loaded-flat-62c8e8-flat.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 13 % → 4 % | 39.1 px | 0.31 | 0.29 | 305 |
| heavy line | 19 % → 18 % | 54.3 px | 0.28 | 0.99 | 313 |
| pressure swell | 16 % → 14 % | 61.7 px | 0.25 | 0.86 | 233 |
| fast wave | 52 % → 43 % | 60.1 px | 0.19 | 0.83 | 906 |
| slow wave | 51 % → 40 % | 59.2 px | 0.26 | 0.79 | 1542 |
| spiral | 69 % → 41 % | 45.6 px | 0.24 | 0.59 | 1556 |
| loop | 48 % → 38 % | 62.4 px | 0.27 | 0.79 | 762 |
| tilted | 20 % → 20 % | 54.9 px | 0.23 | 1.00 | 525 |
| over the wet one | 38 % → 34 % | 52.0 px | 0.23 | 0.88 | 362 |
| long, no reload | 73 % → 48 % | 32.5 px | 0.21 | 0.66 | 2237 | quarters: 0.00 → 0.00 → 0.01 → 0.01

Numbers say: light vs heavy: width 39.1 → 54.3 px, dark 0.31 → 0.28; the long stroke does not run out of paint.

## Oil · Henry Ward · Loaded flat #0f2018 flat
Gouache 1.00 · 84 px · 50.6 s

![Oil · Henry Ward · Loaded flat #0f2018 flat](Oil-Henry-Ward-Loaded-flat-0f2018-flat.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 13 % → 4 % | 39.1 px | 0.59 | 0.29 | 285 |
| heavy line | 19 % → 18 % | 54.3 px | 0.64 | 0.99 | 295 |
| pressure swell | 16 % → 14 % | 61.7 px | 0.65 | 0.86 | 218 |
| fast wave | 52 % → 43 % | 60.1 px | 0.69 | 0.83 | 861 |
| slow wave | 51 % → 40 % | 59.2 px | 0.65 | 0.79 | 1625 |
| spiral | 69 % → 41 % | 45.6 px | 0.66 | 0.59 | 1560 |
| loop | 48 % → 38 % | 62.4 px | 0.62 | 0.79 | 783 |
| tilted | 20 % → 20 % | 54.9 px | 0.67 | 1.00 | 510 |
| over the wet one | 38 % → 34 % | 52.0 px | 0.67 | 0.88 | 412 |
| long, no reload | 73 % → 48 % | 32.5 px | 0.69 | 0.66 | 1969 | quarters: 0.63 → 0.60 → 0.51 → 0.32

Numbers say: light vs heavy: width 39.1 → 54.3 px, dark 0.59 → 0.64.

## Oil · Henry Ward · Ground #e6e2ee flat
Gouache 1.00 · 160 px · 77.9 s

![Oil · Henry Ward · Ground #e6e2ee flat](Oil-Henry-Ward-Ground-e6e2ee-flat.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 51 % → 46 % | 148.3 px | 0.39 | 0.89 | 764 |
| heavy line | 52 % → 47 % | 151.5 px | 0.39 | 0.91 | 912 |
| pressure swell | 41 % → 45 % | 154.8 px | 0.38 | 1.10 | 700 |
| fast wave | 85 % → 86 % | 97.8 px | 0.37 | 1.01 | 2771 |
| slow wave | 86 % → 73 % | 99.2 px | 0.38 | 0.86 | 4312 |
| spiral | 88 % → 69 % | 58.3 px | 0.38 | 0.77 | 3933 |
| loop | 75 % → 69 % | 97.0 px | 0.38 | 0.92 | 2084 |
| tilted | 39 % → 39 % | 107.5 px | 0.38 | 1.00 | 1250 |
| over the wet one | 76 % → 71 % | 104.6 px | 0.38 | 0.93 | 1042 |
| long, no reload | 98 % → 87 % | 44.0 px | 0.38 | 0.88 | 6396 | quarters: 0.00 → 0.00 → 0.00 → 0.00

Numbers say: light vs heavy: width 148.3 → 151.5 px, dark 0.39 → 0.39; pressure barely changes the width.

## Oil · Henry Ward · Dry scrub #f2f0f6 filbert
Gouache 1.00 · 90 px · 38.9 s

![Oil · Henry Ward · Dry scrub #f2f0f6 filbert](Oil-Henry-Ward-Dry-scrub-f2f0f6-filbert.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 8 % → 0 % | 23.8 px | 0.00 | 0.00 | 321 |
| heavy line | 17 % → 6 % | 50.1 px | 0.38 | 0.34 | 436 |
| pressure swell | 15 % → 6 % | 56.0 px | 0.36 | 0.42 | 236 |
| fast wave | 52 % → 16 % | 59.8 px | 0.33 | 0.31 | 965 |
| slow wave | 40 % → 14 % | 46.4 px | 0.34 | 0.35 | 1482 |
| spiral | 68 % → 14 % | 44.7 px | 0.29 | 0.21 | 1517 |
| loop | 34 % → 4 % | 43.7 px | 0.29 | 0.12 | 742 |
| tilted | 19 % → 19 % | 51.8 px | 0.30 | 1.00 | 465 |
| over the wet one | 27 % → 12 % | 24.7 px | 0.30 | 0.45 | 273 |
| long, no reload | 53 % → 9 % | 23.7 px | 0.30 | 0.18 | 2006 | quarters: 0.04 → 0.02 → 0.03 → 0.05

Numbers say: light vs heavy: width 23.8 → 50.1 px, dark 0.00 → 0.38; the long stroke does not run out of paint.

## Oil · Henry Ward · Dirty contour #1e4a78 flat
Gouache 1.00 · 34 px · 37.8 s

![Oil · Henry Ward · Dirty contour #1e4a78 flat](Oil-Henry-Ward-Dirty-contour-1e4a78-flat.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 10 % → 8 % | 29.7 px | 0.50 | 0.78 | 137 |
| heavy line | 12 % → 11 % | 33.9 px | 0.49 | 0.92 | 129 |
| pressure swell | 9 % → 8 % | 32.4 px | 0.55 | 0.96 | 92 |
| fast wave | 23 % → 20 % | 26.4 px | 0.61 | 0.88 | 340 |
| slow wave | 28 % → 25 % | 32.6 px | 0.54 | 0.87 | 614 |
| spiral | 39 % → 24 % | 25.4 px | 0.59 | 0.63 | 658 |
| loop | 21 % → 20 % | 27.5 px | 0.54 | 0.93 | 309 |
| tilted | 10 % → 10 % | 28.6 px | 0.56 | 1.02 | 182 |
| over the wet one | 22 % → 21 % | 32.3 px | 0.56 | 0.96 | 163 |
| long, no reload | 47 % → 28 % | 20.9 px | 0.56 | 0.61 | 988 | quarters: 0.37 → 0.33 → 0.24 → 0.22

Numbers say: light vs heavy: width 29.7 → 33.9 px, dark 0.50 → 0.49.

## Oil · Henry Ward · Dirty contour #141414 flat
Gouache 1.00 · 34 px · 37.7 s

![Oil · Henry Ward · Dirty contour #141414 flat](Oil-Henry-Ward-Dirty-contour-141414-flat.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 10 % → 8 % | 29.7 px | 0.72 | 0.78 | 139 |
| heavy line | 12 % → 11 % | 33.9 px | 0.71 | 0.92 | 159 |
| pressure swell | 9 % → 8 % | 32.4 px | 0.75 | 0.96 | 105 |
| fast wave | 23 % → 20 % | 26.4 px | 0.79 | 0.88 | 293 |
| slow wave | 28 % → 25 % | 32.6 px | 0.75 | 0.87 | 623 |
| spiral | 39 % → 24 % | 25.4 px | 0.78 | 0.63 | 714 |
| loop | 21 % → 20 % | 27.5 px | 0.75 | 0.93 | 342 |
| tilted | 10 % → 10 % | 28.6 px | 0.75 | 1.02 | 187 |
| over the wet one | 22 % → 21 % | 32.3 px | 0.75 | 0.96 | 154 |
| long, no reload | 47 % → 28 % | 20.9 px | 0.76 | 0.61 | 960 | quarters: 0.51 → 0.45 → 0.35 → 0.32

Numbers say: light vs heavy: width 29.7 → 33.9 px, dark 0.72 → 0.71.

## Oil · Henry Ward · Dry scrub #c89038 filbert
Gouache 1.00 · 90 px · 39.5 s

![Oil · Henry Ward · Dry scrub #c89038 filbert](Oil-Henry-Ward-Dry-scrub-c89038-filbert.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 8 % → 0 % | 23.8 px | 0.00 | 0.00 | 259 |
| heavy line | 17 % → 6 % | 50.1 px | 0.13 | 0.34 | 356 |
| pressure swell | 15 % → 6 % | 56.0 px | 0.19 | 0.42 | 233 |
| fast wave | 52 % → 16 % | 59.8 px | 0.21 | 0.31 | 982 |
| slow wave | 40 % → 14 % | 46.4 px | 0.17 | 0.35 | 1529 |
| spiral | 68 % → 14 % | 44.7 px | 0.29 | 0.21 | 1644 |
| loop | 34 % → 4 % | 43.7 px | 0.24 | 0.12 | 715 |
| tilted | 19 % → 19 % | 51.8 px | 0.26 | 1.00 | 492 |
| over the wet one | 27 % → 12 % | 24.7 px | 0.26 | 0.45 | 288 |
| long, no reload | 53 % → 9 % | 23.7 px | 0.27 | 0.18 | 1945 | quarters: 0.09 → 0.15 → 0.11 → 0.05

Numbers say: light vs heavy: width 23.8 → 50.1 px, dark 0.00 → 0.13.

## Oil · Henry Ward · Ground #efe8b8 flat
Gouache 1.00 · 160 px · 74.4 s

![Oil · Henry Ward · Ground #efe8b8 flat](Oil-Henry-Ward-Ground-efe8b8-flat.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 51 % → 46 % | 148.3 px | 0.39 | 0.89 | 852 |
| heavy line | 52 % → 47 % | 151.5 px | 0.39 | 0.91 | 981 |
| pressure swell | 41 % → 45 % | 154.8 px | 0.38 | 1.10 | 669 |
| fast wave | 85 % → 86 % | 97.8 px | 0.38 | 1.01 | 2643 |
| slow wave | 86 % → 73 % | 99.2 px | 0.39 | 0.86 | 4728 |
| spiral | 88 % → 69 % | 58.3 px | 0.38 | 0.77 | 4001 |
| loop | 75 % → 69 % | 97.0 px | 0.39 | 0.92 | 2144 |
| tilted | 39 % → 39 % | 107.5 px | 0.38 | 1.00 | 1084 |
| over the wet one | 76 % → 71 % | 104.6 px | 0.38 | 0.93 | 1031 |
| long, no reload | 98 % → 87 % | 44.0 px | 0.38 | 0.88 | 6181 | quarters: 0.00 → 0.00 → 0.00 → 0.00

Numbers say: light vs heavy: width 148.3 → 151.5 px, dark 0.39 → 0.39; pressure barely changes the width.

## Oil · Henry Ward · Loaded flat #a89ac8 round
Gouache 1.00 · 84 px · 48.4 s

![Oil · Henry Ward · Loaded flat #a89ac8 round](Oil-Henry-Ward-Loaded-flat-a89ac8-round.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 13 % → 5 % | 36.9 px | 0.17 | 0.42 | 289 |
| heavy line | 21 % → 19 % | 60.8 px | 0.15 | 0.90 | 360 |
| pressure swell | 18 % → 16 % | 67.8 px | 0.17 | 0.89 | 251 |
| fast wave | 54 % → 44 % | 61.8 px | 0.26 | 0.82 | 971 |
| slow wave | 56 % → 47 % | 65.1 px | 0.17 | 0.83 | 1573 |
| spiral | 66 % → 48 % | 43.8 px | 0.22 | 0.73 | 1873 |
| loop | 53 % → 36 % | 68.2 px | 0.20 | 0.68 | 822 |
| tilted | 20 % → 20 % | 54.5 px | 0.21 | 1.00 | 557 |
| over the wet one | 37 % → 31 % | 49.1 px | 0.21 | 0.83 | 402 |
| long, no reload | 77 % → 50 % | 34.7 px | 0.24 | 0.65 | 2029 | quarters: 0.22 → 0.20 → 0.15 → 0.09

Numbers say: light vs heavy: width 36.9 → 60.8 px, dark 0.17 → 0.15.

## Oil · Henry Ward · Dirty contour #2a2418 flat
Gouache 1.00 · 34 px · 36.6 s

![Oil · Henry Ward · Dirty contour #2a2418 flat](Oil-Henry-Ward-Dirty-contour-2a2418-flat.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 10 % → 8 % | 29.7 px | 0.63 | 0.78 | 123 |
| heavy line | 12 % → 11 % | 33.9 px | 0.62 | 0.92 | 173 |
| pressure swell | 9 % → 8 % | 32.4 px | 0.67 | 0.96 | 127 |
| fast wave | 23 % → 20 % | 26.4 px | 0.72 | 0.88 | 451 |
| slow wave | 28 % → 25 % | 32.6 px | 0.67 | 0.87 | 569 |
| spiral | 39 % → 24 % | 25.4 px | 0.71 | 0.63 | 586 |
| loop | 21 % → 20 % | 27.5 px | 0.67 | 0.93 | 329 |
| tilted | 10 % → 10 % | 28.6 px | 0.68 | 1.02 | 199 |
| over the wet one | 22 % → 21 % | 32.3 px | 0.68 | 0.96 | 145 |
| long, no reload | 47 % → 28 % | 20.9 px | 0.69 | 0.61 | 817 | quarters: 0.46 → 0.40 → 0.31 → 0.28

Numbers say: light vs heavy: width 29.7 → 33.9 px, dark 0.63 → 0.62.

## Oil · Henry Ward · Loaded flat #2a2418 filbert
Gouache 1.00 · 84 px · 47.4 s

![Oil · Henry Ward · Loaded flat #2a2418 filbert](Oil-Henry-Ward-Loaded-flat-2a2418-filbert.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 12 % → 7 % | 35.0 px | 0.61 | 0.56 | 287 |
| heavy line | 21 % → 20 % | 60.6 px | 0.58 | 0.94 | 350 |
| pressure swell | 16 % → 14 % | 60.6 px | 0.58 | 0.89 | 274 |
| fast wave | 51 % → 44 % | 59.2 px | 0.64 | 0.85 | 898 |
| slow wave | 53 % → 41 % | 61.3 px | 0.62 | 0.77 | 1628 |
| spiral | 66 % → 50 % | 43.3 px | 0.67 | 0.77 | 1655 |
| loop | 52 % → 36 % | 67.4 px | 0.62 | 0.68 | 882 |
| tilted | 19 % → 19 % | 52.9 px | 0.64 | 1.00 | 530 |
| over the wet one | 38 % → 34 % | 53.6 px | 0.64 | 0.89 | 396 |
| long, no reload | 77 % → 52 % | 34.7 px | 0.65 | 0.67 | 2645 | quarters: 0.62 → 0.59 → 0.51 → 0.32

Numbers say: light vs heavy: width 35.0 → 60.6 px, dark 0.61 → 0.58.

## Oil · Henry Ward · Dry scrub #efeee6 round
Gouache 1.00 · 90 px · 33.5 s

![Oil · Henry Ward · Dry scrub #efeee6 round](Oil-Henry-Ward-Dry-scrub-efeee6-round.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 8 % → 0 % | 24.6 px | 0.00 | 0.00 | 230 |
| heavy line | 15 % → 2 % | 42.5 px | 0.37 | 0.15 | 336 |
| pressure swell | 13 % → 7 % | 48.5 px | 0.37 | 0.52 | 219 |
| fast wave | 54 % → 11 % | 62.6 px | 0.31 | 0.21 | 936 |
| slow wave | 42 % → 20 % | 48.8 px | 0.34 | 0.48 | 1760 |
| spiral | 78 % → 18 % | 51.6 px | 0.29 | 0.23 | 1548 |
| loop | 34 % → 4 % | 44.5 px | 0.29 | 0.12 | 627 |
| tilted | 19 % → 19 % | 51.9 px | 0.31 | 1.00 | 440 |
| over the wet one | 27 % → 11 % | 23.4 px | 0.31 | 0.40 | 316 |
| long, no reload | 45 % → 2 % | 20.3 px | 0.28 | 0.04 | 2180 | quarters: 0.04 → 0.03 → 0.04 → 0.05

Numbers say: light vs heavy: width 24.6 → 42.5 px, dark 0.00 → 0.37; the long stroke does not run out of paint.

## Oil · Henry Ward · Ground #e6e2f0 flat
Gouache 1.00 · 160 px · 72.3 s

![Oil · Henry Ward · Ground #e6e2f0 flat](Oil-Henry-Ward-Ground-e6e2f0-flat.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 51 % → 46 % | 148.3 px | 0.39 | 0.89 | 800 |
| heavy line | 52 % → 47 % | 151.5 px | 0.39 | 0.91 | 957 |
| pressure swell | 41 % → 45 % | 154.8 px | 0.38 | 1.10 | 801 |
| fast wave | 85 % → 86 % | 97.8 px | 0.37 | 1.01 | 2508 |
| slow wave | 86 % → 73 % | 99.2 px | 0.38 | 0.86 | 4605 |
| spiral | 88 % → 69 % | 58.3 px | 0.38 | 0.77 | 3838 |
| loop | 75 % → 69 % | 97.0 px | 0.38 | 0.92 | 1847 |
| tilted | 39 % → 39 % | 107.5 px | 0.38 | 1.00 | 1136 |
| over the wet one | 76 % → 71 % | 104.6 px | 0.38 | 0.93 | 987 |
| long, no reload | 98 % → 87 % | 44.0 px | 0.38 | 0.88 | 5404 | quarters: 0.00 → 0.00 → 0.00 → 0.00

Numbers say: light vs heavy: width 148.3 → 151.5 px, dark 0.39 → 0.39; pressure barely changes the width.

## Oil · Henry Ward · Loaded flat #a8b84a round
Gouache 1.00 · 84 px · 46.8 s

![Oil · Henry Ward · Loaded flat #a8b84a round](Oil-Henry-Ward-Loaded-flat-a8b84a-round.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 13 % → 5 % | 36.9 px | 0.15 | 0.42 | 241 |
| heavy line | 21 % → 19 % | 60.8 px | 0.13 | 0.90 | 392 |
| pressure swell | 18 % → 16 % | 67.8 px | 0.15 | 0.89 | 306 |
| fast wave | 54 % → 44 % | 61.8 px | 0.24 | 0.82 | 890 |
| slow wave | 56 % → 47 % | 65.1 px | 0.15 | 0.83 | 1693 |
| spiral | 66 % → 48 % | 43.8 px | 0.20 | 0.73 | 1735 |
| loop | 53 % → 36 % | 68.2 px | 0.17 | 0.68 | 899 |
| tilted | 20 % → 20 % | 54.5 px | 0.19 | 1.00 | 444 |
| over the wet one | 37 % → 31 % | 49.1 px | 0.19 | 0.83 | 348 |
| long, no reload | 77 % → 50 % | 34.7 px | 0.22 | 0.65 | 2150 | quarters: 0.20 → 0.19 → 0.14 → 0.08

Numbers say: light vs heavy: width 36.9 → 60.8 px, dark 0.15 → 0.13.

## Oil · Henry Ward · Thin veil #5a8a6a flat
Oil 0.81 · Ink 0.19 · 96 px · 46.0 s

![Oil · Henry Ward · Thin veil #5a8a6a flat](Oil-Henry-Ward-Thin-veil-5a8a6a-flat.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 9 % → 4 % | 24.9 px | 0.20 | 0.51 | 306 |
| heavy line | 22 % → 20 % | 65.2 px | 0.34 | 0.89 | 460 |
| pressure swell | 20 % → 18 % | 73.8 px | 0.30 | 0.91 | 281 |
| fast wave | 59 % → 58 % | 68.4 px | 0.36 | 0.98 | 1178 |
| slow wave | 58 % → 51 % | 67.1 px | 0.35 | 0.89 | 1933 |
| spiral | 83 % → 67 % | 55.0 px | 0.41 | 0.80 | 1899 |
| loop | 57 % → 49 % | 74.0 px | 0.29 | 0.85 | 831 |
| tilted | 23 % → 23 % | 63.1 px | 0.36 | 1.01 | 596 |
| over the wet one | 36 % → 34 % | 38.7 px | 0.36 | 0.93 | 392 |
| long, no reload | 82 % → 70 % | 36.7 px | 0.36 | 0.85 | 2227 | quarters: 0.40 → 0.32 → 0.27 → 0.12

Numbers say: light vs heavy: width 24.9 → 65.2 px, dark 0.20 → 0.34.

## Oil · Henry Ward · Loaded flat #4a1420 round
Gouache 1.00 · 84 px · 45.2 s

![Oil · Henry Ward · Loaded flat #4a1420 round](Oil-Henry-Ward-Loaded-flat-4a1420-round.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 13 % → 5 % | 36.9 px | 0.63 | 0.42 | 324 |
| heavy line | 21 % → 19 % | 60.8 px | 0.61 | 0.90 | 301 |
| pressure swell | 18 % → 16 % | 67.8 px | 0.61 | 0.89 | 229 |
| fast wave | 54 % → 44 % | 61.8 px | 0.66 | 0.82 | 838 |
| slow wave | 56 % → 47 % | 65.1 px | 0.63 | 0.83 | 1501 |
| spiral | 66 % → 48 % | 43.8 px | 0.64 | 0.73 | 1573 |
| loop | 53 % → 36 % | 68.2 px | 0.63 | 0.68 | 807 |
| tilted | 20 % → 20 % | 54.5 px | 0.63 | 1.00 | 455 |
| over the wet one | 37 % → 31 % | 49.1 px | 0.63 | 0.83 | 306 |
| long, no reload | 77 % → 50 % | 34.7 px | 0.65 | 0.65 | 1925 | quarters: 0.63 → 0.59 → 0.51 → 0.33

Numbers say: light vs heavy: width 36.9 → 60.8 px, dark 0.63 → 0.61.

## Oil · Henry Ward · Dirty contour #2a0a10 flat
Gouache 1.00 · 34 px · 33.0 s

![Oil · Henry Ward · Dirty contour #2a0a10 flat](Oil-Henry-Ward-Dirty-contour-2a0a10-flat.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 10 % → 8 % | 29.7 px | 0.73 | 0.78 | 113 |
| heavy line | 12 % → 11 % | 33.9 px | 0.73 | 0.92 | 124 |
| pressure swell | 9 % → 8 % | 32.4 px | 0.75 | 0.96 | 85 |
| fast wave | 23 % → 20 % | 26.4 px | 0.78 | 0.88 | 320 |
| slow wave | 28 % → 25 % | 32.6 px | 0.76 | 0.87 | 573 |
| spiral | 39 % → 24 % | 25.4 px | 0.77 | 0.63 | 561 |
| loop | 21 % → 20 % | 27.5 px | 0.75 | 0.93 | 305 |
| tilted | 10 % → 10 % | 28.6 px | 0.75 | 1.02 | 160 |
| over the wet one | 22 % → 21 % | 32.3 px | 0.75 | 0.96 | 152 |
| long, no reload | 47 % → 28 % | 20.9 px | 0.76 | 0.61 | 774 | quarters: 0.50 → 0.45 → 0.34 → 0.32

Numbers say: light vs heavy: width 29.7 → 33.9 px, dark 0.73 → 0.73.

## Oil · Henry Ward · Dry scrub #c0506a round
Gouache 1.00 · 90 px · 31.7 s

![Oil · Henry Ward · Dry scrub #c0506a round](Oil-Henry-Ward-Dry-scrub-c0506a-round.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 8 % → 0 % | 24.6 px | 0.00 | 0.00 | 218 |
| heavy line | 15 % → 2 % | 42.5 px | 0.32 | 0.15 | 333 |
| pressure swell | 13 % → 7 % | 48.5 px | 0.29 | 0.52 | 220 |
| fast wave | 54 % → 11 % | 62.6 px | 0.36 | 0.21 | 947 |
| slow wave | 42 % → 20 % | 48.8 px | 0.34 | 0.48 | 1467 |
| spiral | 78 % → 18 % | 51.6 px | 0.40 | 0.23 | 1475 |
| loop | 34 % → 4 % | 44.5 px | 0.37 | 0.12 | 688 |
| tilted | 19 % → 19 % | 51.9 px | 0.38 | 1.00 | 391 |
| over the wet one | 27 % → 11 % | 23.4 px | 0.38 | 0.40 | 283 |
| long, no reload | 45 % → 2 % | 20.3 px | 0.42 | 0.04 | 1695 | quarters: 0.12 → 0.16 → 0.13 → 0.10

Numbers say: light vs heavy: width 24.6 → 42.5 px, dark 0.00 → 0.32.

## Oil · Henry Ward · Ground #d8d4c8 flat
Gouache 1.00 · 160 px · 69.5 s

![Oil · Henry Ward · Ground #d8d4c8 flat](Oil-Henry-Ward-Ground-d8d4c8-flat.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 51 % → 46 % | 148.3 px | 0.35 | 0.89 | 685 |
| heavy line | 52 % → 47 % | 151.5 px | 0.35 | 0.91 | 880 |
| pressure swell | 41 % → 45 % | 154.8 px | 0.35 | 1.10 | 637 |
| fast wave | 85 % → 86 % | 97.8 px | 0.34 | 1.01 | 2195 |
| slow wave | 86 % → 73 % | 99.2 px | 0.35 | 0.86 | 3743 |
| spiral | 88 % → 69 % | 58.3 px | 0.35 | 0.77 | 3329 |
| loop | 75 % → 69 % | 97.0 px | 0.35 | 0.92 | 1766 |
| tilted | 39 % → 39 % | 107.5 px | 0.35 | 1.00 | 1036 |
| over the wet one | 76 % → 71 % | 104.6 px | 0.35 | 0.93 | 976 |
| long, no reload | 98 % → 87 % | 44.0 px | 0.35 | 0.88 | 5540 | quarters: 0.00 → 0.00 → 0.00 → 0.00

Numbers say: light vs heavy: width 148.3 → 151.5 px, dark 0.35 → 0.35; pressure barely changes the width.

## Oil · Henry Ward · Loaded flat #e8d8b0 flat
Gouache 1.00 · 84 px · 44.0 s

![Oil · Henry Ward · Loaded flat #e8d8b0 flat](Oil-Henry-Ward-Loaded-flat-e8d8b0-flat.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 13 % → 4 % | 39.1 px | 0.40 | 0.29 | 222 |
| heavy line | 19 % → 18 % | 54.3 px | 0.40 | 0.99 | 295 |
| pressure swell | 16 % → 14 % | 61.7 px | 0.35 | 0.86 | 224 |
| fast wave | 52 % → 43 % | 60.1 px | 0.30 | 0.83 | 814 |
| slow wave | 51 % → 40 % | 59.2 px | 0.37 | 0.79 | 1354 |
| spiral | 69 % → 41 % | 45.6 px | 0.33 | 0.59 | 1543 |
| loop | 48 % → 38 % | 62.4 px | 0.37 | 0.79 | 703 |
| tilted | 20 % → 20 % | 54.9 px | 0.33 | 1.00 | 537 |
| over the wet one | 38 % → 34 % | 52.0 px | 0.33 | 0.88 | 324 |
| long, no reload | 73 % → 48 % | 32.5 px | 0.31 | 0.66 | 1769 | quarters: 0.00 → 0.00 → 0.01 → 0.02

Numbers say: light vs heavy: width 39.1 → 54.3 px, dark 0.40 → 0.40; the long stroke does not run out of paint.

## Oil · Henry Ward · Dry scrub #f2ead0 filbert
Gouache 1.00 · 90 px · 33.9 s

![Oil · Henry Ward · Dry scrub #f2ead0 filbert](Oil-Henry-Ward-Dry-scrub-f2ead0-filbert.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 8 % → 0 % | 23.8 px | 0.00 | 0.00 | 226 |
| heavy line | 17 % → 6 % | 50.1 px | 0.38 | 0.34 | 299 |
| pressure swell | 15 % → 6 % | 56.0 px | 0.35 | 0.42 | 203 |
| fast wave | 52 % → 16 % | 59.8 px | 0.32 | 0.31 | 783 |
| slow wave | 40 % → 14 % | 46.4 px | 0.34 | 0.35 | 1339 |
| spiral | 68 % → 14 % | 44.7 px | 0.28 | 0.21 | 1320 |
| loop | 34 % → 4 % | 43.7 px | 0.28 | 0.12 | 635 |
| tilted | 19 % → 19 % | 51.8 px | 0.29 | 1.00 | 384 |
| over the wet one | 27 % → 12 % | 24.7 px | 0.29 | 0.45 | 277 |
| long, no reload | 53 % → 9 % | 23.7 px | 0.29 | 0.18 | 1648 | quarters: 0.04 → 0.02 → 0.03 → 0.05

Numbers say: light vs heavy: width 23.8 → 50.1 px, dark 0.00 → 0.38; the long stroke does not run out of paint.

## Oil · Henry Ward · Loaded flat #2a1428 flat
Gouache 1.00 · 84 px · 44.8 s

![Oil · Henry Ward · Loaded flat #2a1428 flat](Oil-Henry-Ward-Loaded-flat-2a1428-flat.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 13 % → 4 % | 39.1 px | 0.59 | 0.29 | 239 |
| heavy line | 19 % → 18 % | 54.3 px | 0.65 | 0.99 | 294 |
| pressure swell | 16 % → 14 % | 61.7 px | 0.65 | 0.86 | 228 |
| fast wave | 52 % → 43 % | 60.1 px | 0.69 | 0.83 | 819 |
| slow wave | 51 % → 40 % | 59.2 px | 0.65 | 0.79 | 1347 |
| spiral | 69 % → 41 % | 45.6 px | 0.66 | 0.59 | 1486 |
| loop | 48 % → 38 % | 62.4 px | 0.63 | 0.79 | 745 |
| tilted | 20 % → 20 % | 54.9 px | 0.66 | 1.00 | 500 |
| over the wet one | 38 % → 34 % | 52.0 px | 0.66 | 0.88 | 372 |
| long, no reload | 73 % → 48 % | 32.5 px | 0.68 | 0.66 | 1858 | quarters: 0.63 → 0.60 → 0.50 → 0.32

Numbers say: light vs heavy: width 39.1 → 54.3 px, dark 0.59 → 0.65.

## Oil · Henry Ward · Ground #e8e4e0 flat
Gouache 1.00 · 160 px · 71.5 s

![Oil · Henry Ward · Ground #e8e4e0 flat](Oil-Henry-Ward-Ground-e8e4e0-flat.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 51 % → 46 % | 148.3 px | 0.39 | 0.89 | 746 |
| heavy line | 52 % → 47 % | 151.5 px | 0.39 | 0.91 | 803 |
| pressure swell | 41 % → 45 % | 154.8 px | 0.38 | 1.10 | 605 |
| fast wave | 85 % → 86 % | 97.8 px | 0.37 | 1.01 | 2383 |
| slow wave | 86 % → 73 % | 99.2 px | 0.38 | 0.86 | 3972 |
| spiral | 88 % → 69 % | 58.3 px | 0.38 | 0.77 | 3402 |
| loop | 75 % → 69 % | 97.0 px | 0.39 | 0.92 | 1871 |
| tilted | 39 % → 39 % | 107.5 px | 0.38 | 1.00 | 1010 |
| over the wet one | 76 % → 71 % | 104.6 px | 0.38 | 0.93 | 892 |
| long, no reload | 98 % → 87 % | 44.0 px | 0.38 | 0.88 | 5148 | quarters: 0.00 → 0.00 → 0.00 → 0.00

Numbers say: light vs heavy: width 148.3 → 151.5 px, dark 0.39 → 0.39; pressure barely changes the width.

## Oil · Henry Ward · Loaded flat #8a2a18 filbert
Gouache 1.00 · 84 px · 44.7 s

![Oil · Henry Ward · Loaded flat #8a2a18 filbert](Oil-Henry-Ward-Loaded-flat-8a2a18-filbert.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 12 % → 7 % | 35.0 px | 0.55 | 0.56 | 208 |
| heavy line | 21 % → 20 % | 60.6 px | 0.53 | 0.94 | 290 |
| pressure swell | 16 % → 14 % | 60.6 px | 0.52 | 0.89 | 219 |
| fast wave | 51 % → 44 % | 59.2 px | 0.58 | 0.85 | 901 |
| slow wave | 53 % → 41 % | 61.3 px | 0.56 | 0.77 | 1444 |
| spiral | 66 % → 50 % | 43.3 px | 0.60 | 0.77 | 1476 |
| loop | 52 % → 36 % | 67.4 px | 0.55 | 0.68 | 837 |
| tilted | 19 % → 19 % | 52.9 px | 0.58 | 1.00 | 444 |
| over the wet one | 38 % → 34 % | 53.6 px | 0.58 | 0.89 | 333 |
| long, no reload | 77 % → 52 % | 34.7 px | 0.58 | 0.67 | 1926 | quarters: 0.56 → 0.53 → 0.45 → 0.29

Numbers say: light vs heavy: width 35.0 → 60.6 px, dark 0.55 → 0.53.

## Oil · Henry Ward · Loaded flat #a8c8dc filbert
Gouache 1.00 · 84 px · 44.4 s

![Oil · Henry Ward · Loaded flat #a8c8dc filbert](Oil-Henry-Ward-Loaded-flat-a8c8dc-filbert.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 12 % → 7 % | 35.0 px | 0.30 | 0.56 | 266 |
| heavy line | 21 % → 20 % | 60.6 px | 0.37 | 0.94 | 315 |
| pressure swell | 16 % → 14 % | 60.6 px | 0.35 | 0.89 | 211 |
| fast wave | 51 % → 44 % | 59.2 px | 0.27 | 0.85 | 767 |
| slow wave | 53 % → 41 % | 61.3 px | 0.31 | 0.77 | 1387 |
| spiral | 66 % → 50 % | 43.3 px | 0.25 | 0.77 | 1431 |
| loop | 52 % → 36 % | 67.4 px | 0.30 | 0.68 | 795 |
| tilted | 19 % → 19 % | 52.9 px | 0.27 | 1.00 | 436 |
| over the wet one | 38 % → 34 % | 53.6 px | 0.27 | 0.89 | 328 |
| long, no reload | 77 % → 52 % | 34.7 px | 0.27 | 0.67 | 2124 | quarters: 0.00 → 0.00 → 0.01 → 0.01

Numbers say: light vs heavy: width 35.0 → 60.6 px, dark 0.30 → 0.37; the long stroke does not run out of paint.

## Oil · Henry Ward · Dry scrub #d8e8f0 filbert
Gouache 1.00 · 90 px · 34.7 s

![Oil · Henry Ward · Dry scrub #d8e8f0 filbert](Oil-Henry-Ward-Dry-scrub-d8e8f0-filbert.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 8 % → 0 % | 23.8 px | 0.00 | 0.00 | 234 |
| heavy line | 17 % → 6 % | 50.1 px | 0.38 | 0.34 | 315 |
| pressure swell | 15 % → 6 % | 56.0 px | 0.35 | 0.42 | 234 |
| fast wave | 52 % → 16 % | 59.8 px | 0.31 | 0.31 | 915 |
| slow wave | 40 % → 14 % | 46.4 px | 0.33 | 0.35 | 1428 |
| spiral | 68 % → 14 % | 44.7 px | 0.27 | 0.21 | 1399 |
| loop | 34 % → 4 % | 43.7 px | 0.28 | 0.12 | 729 |
| tilted | 19 % → 19 % | 51.8 px | 0.28 | 1.00 | 414 |
| over the wet one | 27 % → 12 % | 24.7 px | 0.28 | 0.45 | 271 |
| long, no reload | 53 % → 9 % | 23.7 px | 0.28 | 0.18 | 1666 | quarters: 0.03 → 0.02 → 0.03 → 0.05

Numbers say: light vs heavy: width 23.8 → 50.1 px, dark 0.00 → 0.38; the long stroke does not run out of paint.

## Oil · Henry Ward · Ground #3a3a34 flat
Gouache 1.00 · 160 px · 69.4 s

![Oil · Henry Ward · Ground #3a3a34 flat](Oil-Henry-Ward-Ground-3a3a34-flat.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 51 % → 46 % | 148.3 px | 0.47 | 0.89 | 698 |
| heavy line | 52 % → 47 % | 151.5 px | 0.47 | 0.91 | 783 |
| pressure swell | 41 % → 45 % | 154.8 px | 0.48 | 1.10 | 587 |
| fast wave | 85 % → 86 % | 97.8 px | 0.48 | 1.01 | 2276 |
| slow wave | 86 % → 73 % | 99.2 px | 0.47 | 0.86 | 3731 |
| spiral | 88 % → 69 % | 58.3 px | 0.48 | 0.77 | 3689 |
| loop | 75 % → 69 % | 97.0 px | 0.47 | 0.92 | 1766 |
| tilted | 39 % → 39 % | 107.5 px | 0.47 | 1.00 | 1032 |
| over the wet one | 76 % → 71 % | 104.6 px | 0.47 | 0.93 | 854 |
| long, no reload | 98 % → 87 % | 44.0 px | 0.47 | 0.88 | 5299 | quarters: 0.47 → 0.47 → 0.47 → 0.45

Numbers say: light vs heavy: width 148.3 → 151.5 px, dark 0.47 → 0.47; pressure barely changes the width; the long stroke does not run out of paint.

## Oil · Henry Ward · Loaded flat #8a906a round
Gouache 1.00 · 84 px · 44.9 s

![Oil · Henry Ward · Loaded flat #8a906a round](Oil-Henry-Ward-Loaded-flat-8a906a-round.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 13 % → 5 % | 36.9 px | 0.23 | 0.42 | 247 |
| heavy line | 21 % → 19 % | 60.8 px | 0.21 | 0.90 | 311 |
| pressure swell | 18 % → 16 % | 67.8 px | 0.23 | 0.89 | 220 |
| fast wave | 54 % → 44 % | 61.8 px | 0.31 | 0.82 | 807 |
| slow wave | 56 % → 47 % | 65.1 px | 0.23 | 0.83 | 1552 |
| spiral | 66 % → 48 % | 43.8 px | 0.28 | 0.73 | 1603 |
| loop | 53 % → 36 % | 68.2 px | 0.25 | 0.68 | 708 |
| tilted | 20 % → 20 % | 54.5 px | 0.27 | 1.00 | 436 |
| over the wet one | 37 % → 31 % | 49.1 px | 0.27 | 0.83 | 305 |
| long, no reload | 77 % → 50 % | 34.7 px | 0.29 | 0.65 | 1962 | quarters: 0.27 → 0.25 → 0.19 → 0.11

Numbers say: light vs heavy: width 36.9 → 60.8 px, dark 0.23 → 0.21.

## Oil · Henry Ward · Loaded flat #7a8458 flat
Gouache 1.00 · 84 px · 44.0 s

![Oil · Henry Ward · Loaded flat #7a8458 flat](Oil-Henry-Ward-Loaded-flat-7a8458-flat.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 13 % → 4 % | 39.1 px | 0.22 | 0.29 | 225 |
| heavy line | 19 % → 18 % | 54.3 px | 0.28 | 0.99 | 286 |
| pressure swell | 16 % → 14 % | 61.7 px | 0.29 | 0.86 | 206 |
| fast wave | 52 % → 43 % | 60.1 px | 0.36 | 0.83 | 793 |
| slow wave | 51 % → 40 % | 59.2 px | 0.28 | 0.79 | 1309 |
| spiral | 69 % → 41 % | 45.6 px | 0.30 | 0.59 | 1389 |
| loop | 48 % → 38 % | 62.4 px | 0.26 | 0.79 | 797 |
| tilted | 20 % → 20 % | 54.9 px | 0.32 | 1.00 | 447 |
| over the wet one | 38 % → 34 % | 52.0 px | 0.32 | 0.88 | 324 |
| long, no reload | 73 % → 48 % | 32.5 px | 0.34 | 0.66 | 1763 | quarters: 0.29 → 0.28 → 0.20 → 0.13

Numbers say: light vs heavy: width 39.1 → 54.3 px, dark 0.22 → 0.28.

## Oil · Henry Ward · Dry scrub #a8ae88 filbert
Gouache 1.00 · 90 px · 34.2 s

![Oil · Henry Ward · Dry scrub #a8ae88 filbert](Oil-Henry-Ward-Dry-scrub-a8ae88-filbert.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 8 % → 0 % | 23.8 px | 0.00 | 0.00 | 224 |
| heavy line | 17 % → 6 % | 50.1 px | 0.07 | 0.34 | 294 |
| pressure swell | 15 % → 6 % | 56.0 px | 0.13 | 0.42 | 212 |
| fast wave | 52 % → 16 % | 59.8 px | 0.16 | 0.31 | 815 |
| slow wave | 40 % → 14 % | 46.4 px | 0.11 | 0.35 | 1378 |
| spiral | 68 % → 14 % | 44.7 px | 0.24 | 0.21 | 1285 |
| loop | 34 % → 4 % | 43.7 px | 0.19 | 0.12 | 663 |
| tilted | 19 % → 19 % | 51.8 px | 0.21 | 1.00 | 407 |
| over the wet one | 27 % → 12 % | 24.7 px | 0.21 | 0.45 | 264 |
| long, no reload | 53 % → 9 % | 23.7 px | 0.22 | 0.18 | 1628 | quarters: 0.07 → 0.12 → 0.08 → 0.03

Numbers say: light vs heavy: width 23.8 → 50.1 px, dark 0.00 → 0.07.

## v3 · Any shape · K stamp
Gouache 1.00 · 48 px · 38.8 s

![v3 · Any shape · K stamp](v3-Any-shape-K-stamp.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 20 % → 19 % | 59.0 px | 0.40 | 0.93 | 194 |
| heavy line | 20 % → 19 % | 59.1 px | 0.40 | 0.94 | 205 |
| pressure swell | 12 % → 11 % | 43.7 px | 0.40 | 0.98 | 148 |
| fast wave | 42 % → 34 % | 48.2 px | 0.40 | 0.83 | 508 |
| slow wave | 42 % → 34 % | 48.3 px | 0.40 | 0.82 | 971 |
| spiral | 66 % → 44 % | 43.5 px | 0.40 | 0.67 | 892 |
| loop | 37 % → 34 % | 48.2 px | 0.40 | 0.91 | 444 |
| tilted | 15 % → 15 % | 42.0 px | 0.40 | 1.01 | 245 |
| over the wet one | 33 % → 32 % | 51.3 px | 0.40 | 0.95 | 216 |
| long, no reload | 81 % → 47 % | 36.3 px | 0.40 | 0.58 | 1298 | quarters: 0.35 → 0.34 → 0.32 → 0.28

Numbers say: light vs heavy: width 59.0 → 59.1 px, dark 0.40 → 0.40; pressure barely changes the width.

## v3 · Any shape · K of hairs
Oil 1.00 · 48 px · 15.5 s

![v3 · Any shape · K of hairs](v3-Any-shape-K-of-hairs.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 18 % → 18 % | 51.8 px | 0.40 | 1.00 | 136 |
| heavy line | 27 % → 27 % | 78.4 px | 0.46 | 1.00 | 173 |
| pressure swell | 16 % → 16 % | 58.4 px | 0.47 | 1.01 | 118 |
| fast wave | 49 % → 51 % | 56.8 px | 0.44 | 1.04 | 385 |
| slow wave | 50 % → 50 % | 57.8 px | 0.48 | 1.00 | 680 |
| spiral | 67 % → 67 % | 44.1 px | 0.45 | 1.00 | 791 |
| loop | 45 % → 45 % | 58.8 px | 0.48 | 1.00 | 335 |
| tilted | 16 % → 16 % | 45.8 px | 0.46 | 1.00 | 179 |
| over the wet one | 39 % → 39 % | 62.3 px | 0.46 | 1.01 | 161 |
| long, no reload | 84 % → 84 % | 37.8 px | 0.43 | 1.00 | 1019 | quarters: 0.48 → 0.46 → 0.33 → 0.26

Numbers say: light vs heavy: width 51.8 → 78.4 px, dark 0.40 → 0.46.

## v3 · Any shape · Star stamp
Gouache 1.00 · 44 px · 33.2 s

![v3 · Any shape · Star stamp](v3-Any-shape-Star-stamp.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 13 % → 11 % | 37.9 px | 0.36 | 0.84 | 100 |
| heavy line | 13 % → 12 % | 38.4 px | 0.36 | 0.87 | 98 |
| pressure swell | 10 % → 10 % | 39.2 px | 0.36 | 0.93 | 88 |
| fast wave | 33 % → 28 % | 38.0 px | 0.36 | 0.84 | 270 |
| slow wave | 33 % → 27 % | 38.4 px | 0.35 | 0.80 | 461 |
| spiral | 56 % → 41 % | 37.2 px | 0.35 | 0.73 | 436 |
| loop | 28 % → 25 % | 36.0 px | 0.36 | 0.88 | 227 |
| tilted | 13 % → 13 % | 37.0 px | 0.36 | 1.01 | 161 |
| over the wet one | 26 % → 24 % | 36.5 px | 0.36 | 0.91 | 106 |
| long, no reload | 68 % → 45 % | 30.4 px | 0.35 | 0.67 | 697 | quarters: 0.01 → 0.01 → 0.01 → 0.01

Numbers say: light vs heavy: width 37.9 → 38.4 px, dark 0.36 → 0.36; pressure barely changes the width; the long stroke does not run out of paint.

## v3 · Any shape · Star of hairs
Oil 1.00 · 44 px · 14.5 s

![v3 · Any shape · Star of hairs](v3-Any-shape-Star-of-hairs.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 15 % → 15 % | 43.7 px | 0.34 | 1.00 | 118 |
| heavy line | 23 % → 23 % | 67.9 px | 0.33 | 1.00 | 150 |
| pressure swell | 14 % → 14 % | 53.1 px | 0.35 | 1.00 | 105 |
| fast wave | 45 % → 46 % | 52.0 px | 0.32 | 1.01 | 346 |
| slow wave | 44 % → 44 % | 50.7 px | 0.33 | 1.00 | 579 |
| spiral | 63 % → 63 % | 41.7 px | 0.32 | 1.00 | 583 |
| loop | 39 % → 39 % | 50.4 px | 0.33 | 1.00 | 293 |
| tilted | 14 % → 14 % | 39.1 px | 0.34 | 1.00 | 153 |
| over the wet one | 34 % → 34 % | 55.5 px | 0.34 | 1.00 | 141 |
| long, no reload | 78 % → 78 % | 35.1 px | 0.30 | 1.00 | 811 | quarters: 0.32 → 0.28 → 0.23 → 0.17

Numbers say: light vs heavy: width 43.7 → 67.9 px, dark 0.34 → 0.33.

## v3 · Any shape · Rag
Oil 1.00 · 60 px · 19.3 s

![v3 · Any shape · Rag](v3-Any-shape-Rag.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 22 % → 25 % | 64.2 px | 0.16 | 1.12 | 167 |
| heavy line | 38 % → 38 % | 111.5 px | 0.29 | 1.00 | 256 |
| pressure swell | 25 % → 26 % | 94.4 px | 0.24 | 1.02 | 178 |
| fast wave | 68 % → 73 % | 78.9 px | 0.26 | 1.07 | 584 |
| slow wave | 71 % → 71 % | 82.3 px | 0.27 | 1.00 | 1045 |
| spiral | 81 % → 81 % | 53.5 px | 0.28 | 1.00 | 1172 |
| loop | 61 % → 62 % | 79.6 px | 0.29 | 1.00 | 549 |
| tilted | 22 % → 22 % | 61.1 px | 0.26 | 1.00 | 308 |
| over the wet one | 51 % → 52 % | 80.5 px | 0.26 | 1.03 | 227 |
| long, no reload | 94 % → 94 % | 42.3 px | 0.29 | 1.00 | 1583 | quarters: 0.35 → 0.32 → 0.27 → 0.21

Numbers say: light vs heavy: width 64.2 → 111.5 px, dark 0.16 → 0.29.

## v3 · Any shape · Dry oil on canvas
Oil 1.00 · 40 px · 13.1 s

![v3 · Any shape · Dry oil on canvas](v3-Any-shape-Dry-oil-on-canvas.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 5 % → 5 % | 13.3 px | 0.14 | 1.00 | 82 |
| heavy line | 8 % → 8 % | 23.7 px | 0.35 | 1.00 | 88 |
| pressure swell | 9 % → 9 % | 32.2 px | 0.27 | 1.00 | 66 |
| fast wave | 27 % → 27 % | 31.7 px | 0.25 | 1.00 | 250 |
| slow wave | 26 % → 26 % | 30.5 px | 0.24 | 1.00 | 457 |
| spiral | 45 % → 45 % | 29.7 px | 0.25 | 1.00 | 445 |
| loop | 21 % → 21 % | 27.3 px | 0.24 | 1.00 | 206 |
| tilted | 9 % → 9 % | 26.3 px | 0.24 | 1.00 | 97 |
| over the wet one | 18 % → 18 % | 23.1 px | 0.24 | 1.00 | 96 |
| long, no reload | 41 % → 41 % | 18.2 px | 0.21 | 1.00 | 566 | quarters: 0.00 → 0.00 → 0.00 → 0.00

Numbers say: light vs heavy: width 13.3 → 23.7 px, dark 0.14 → 0.35; the long stroke does not run out of paint.

## v3 · Any shape · Two colours streaks
Oil 1.00 · 44 px · 14.2 s

![v3 · Any shape · Two colours streaks](v3-Any-shape-Two-colours-streaks.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 14 % → 14 % | 39.6 px | 0.35 | 1.00 | 112 |
| heavy line | 16 % → 16 % | 46.1 px | 0.31 | 1.00 | 124 |
| pressure swell | 11 % → 11 % | 42.9 px | 0.39 | 1.00 | 91 |
| fast wave | 37 % → 37 % | 43.1 px | 0.34 | 1.00 | 308 |
| slow wave | 35 % → 35 % | 40.7 px | 0.31 | 1.00 | 516 |
| spiral | 61 % → 61 % | 40.4 px | 0.35 | 1.00 | 650 |
| loop | 32 % → 32 % | 41.1 px | 0.32 | 1.00 | 286 |
| tilted | 13 % → 13 % | 37.2 px | 0.36 | 1.00 | 174 |
| over the wet one | 27 % → 27 % | 39.3 px | 0.36 | 1.00 | 121 |
| long, no reload | 73 % → 73 % | 32.6 px | 0.31 | 1.00 | 755 | quarters: 0.29 → 0.28 → 0.24 → 0.18

Numbers say: light vs heavy: width 39.6 → 46.1 px, dark 0.35 → 0.31.

## Brush Artist · Refs · #01 Henry Ward peach cloud — own sheet
own sheet 600 × 600 · Gouache 1.00 · 44 px · 10.5 s

![Brush Artist · Refs · #01 Henry Ward peach cloud — own sheet](Brush-Artist-Refs-01-Henry-Ward-peach-cloud-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 5 % → 16 % | 15.6 px | 0.53 | 2.97 | 126 |
| stroke 2 | 11 % → 29 % | 35.1 px | 0.54 | 2.71 | 138 |
| stroke 3 | 16 % → 31 % | 45.4 px | 0.54 | 2.00 | 131 |
| stroke 4 | 21 % → 34 % | 68.0 px | 0.54 | 1.63 | 148 |
| stroke 5 | 21 % → 31 % | 60.5 px | 0.54 | 1.48 | 131 |
| stroke 6 | 20 % → 24 % | 61.5 px | 0.54 | 1.21 | 142 |
| stroke 7 | 9 % → 33 % | 22.9 px | 0.53 | 3.58 | 128 |
| stroke 8 | 14 % → 32 % | 34.7 px | 0.53 | 2.28 | 144 |
| stroke 9 | 13 % → 33 % | 33.9 px | 0.53 | 2.47 | 160 |
| stroke 10 | 13 % → 34 % | 35.3 px | 0.53 | 2.57 | 191 |
| stroke 11 | 14 % → 36 % | 40.5 px | 0.54 | 2.53 | 151 |
| stroke 12 | 14 % → 39 % | 42.4 px | 0.54 | 2.76 | 101 |
| stroke 13 | 19 % → 42 % | 54.8 px | 0.54 | 2.23 | 130 |
| stroke 14 | 27 % → 44 % | 77.4 px | 0.54 | 1.63 | 177 |
| stroke 15 | 30 % → 48 % | 88.5 px | 0.53 | 1.60 | 118 |
| stroke 16 | 35 % → 48 % | 104.8 px | 0.53 | 1.39 | 152 |
| stroke 17 | 35 % → 50 % | 98.5 px | 0.53 | 1.41 | 151 |
| stroke 18 | 41 % → 49 % | 117.6 px | 0.53 | 1.21 | 189 |
| stroke 19 | 41 % → 49 % | 116.0 px | 0.54 | 1.18 | 139 |
| stroke 20 | 43 % → 46 % | 123.0 px | 0.54 | 1.07 | 154 |
| stroke 21 | 43 % → 42 % | 125.4 px | 0.54 | 0.96 | 168 |
| stroke 22 | 45 % → 42 % | 131.2 px | 0.54 | 0.94 | 162 |
| stroke 23 | 49 % → 43 % | 139.0 px | 0.54 | 0.88 | 146 |
| stroke 24 | 52 % → 45 % | 156.2 px | 0.54 | 0.86 | 119 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #02 Henry Ward cream strokes — own sheet
own sheet 600 × 600 · Gouache 1.00 · 46 px · 7.1 s

![Brush Artist · Refs · #02 Henry Ward cream strokes — own sheet](Brush-Artist-Refs-02-Henry-Ward-cream-strokes-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 9 % → 2 % | 17.7 px | 0.65 | 0.26 | 175 |
| stroke 2 | 15 % → 6 % | 39.4 px | 0.66 | 0.41 | 195 |
| stroke 3 | 19 % → 22 % | 48.9 px | 0.64 | 1.15 | 210 |
| stroke 4 | 23 % → 22 % | 56.7 px | 0.64 | 0.97 | 241 |
| stroke 5 | 24 % → 27 % | 59.0 px | 0.64 | 1.11 | 223 |
| stroke 6 | 18 % → 16 % | 43.4 px | 0.64 | 0.88 | 203 |
| stroke 7 | 21 % → 10 % | 53.1 px | 0.64 | 0.48 | 244 |

## Brush Artist · Refs · #03 Henry Ward navy contours — own sheet
own sheet 600 × 600 · Impasto 1.00 · 22 px · 2.5 s

![Brush Artist · Refs · #03 Henry Ward navy contours — own sheet](Brush-Artist-Refs-03-Henry-Ward-navy-contours-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 10 % → 15 % | 20.0 px | 0.70 | 1.51 | 109 |
| stroke 2 | 16 % → 19 % | 22.1 px | 0.70 | 1.19 | 89 |
| stroke 3 | 20 % → 20 % | 29.5 px | 0.71 | 0.99 | 132 |
| stroke 4 | 19 % → 17 % | 43.6 px | 0.71 | 0.89 | 165 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #04 Henry Ward grey cloud — own sheet
own sheet 600 × 600 · Gouache 1.00 · 50 px · 9.8 s

![Brush Artist · Refs · #04 Henry Ward grey cloud — own sheet](Brush-Artist-Refs-04-Henry-Ward-grey-cloud-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 5 % → 21 % | 15.7 px | 0.32 | 3.88 | 163 |
| stroke 2 | 14 % → 21 % | 40.2 px | 0.31 | 1.53 | 190 |
| stroke 3 | 21 % → 22 % | 59.7 px | 0.31 | 1.05 | 200 |
| stroke 4 | 27 % → 23 % | 79.5 px | 0.31 | 0.84 | 225 |
| stroke 5 | 27 % → 26 % | 83.3 px | 0.31 | 0.94 | 191 |
| stroke 6 | 33 % → 30 % | 109.0 px | 0.31 | 0.89 | 190 |
| stroke 7 | 34 % → 36 % | 100.8 px | 0.30 | 1.03 | 208 |
| stroke 8 | 38 % → 38 % | 112.6 px | 0.30 | 0.99 | 191 |
| stroke 9 | 32 % → 39 % | 94.9 px | 0.31 | 1.23 | 176 |
| stroke 10 | 33 % → 39 % | 106.9 px | 0.31 | 1.19 | 178 |
| stroke 11 | 34 % → 36 % | 96.9 px | 0.31 | 1.05 | 204 |
| stroke 12 | 32 % → 34 % | 96.3 px | 0.30 | 1.06 | 145 |
| stroke 13 | 27 % → 38 % | 78.1 px | 0.31 | 1.38 | 173 |
| stroke 14 | 34 % → 38 % | 100.7 px | 0.31 | 1.11 | 225 |
| stroke 15 | 35 % → 37 % | 100.1 px | 0.31 | 1.07 | 177 |
| stroke 16 | 38 % → 36 % | 116.5 px | 0.31 | 0.93 | 220 |
| stroke 17 | 39 % → 31 % | 112.7 px | 0.31 | 0.79 | 200 |
| stroke 18 | 40 % → 28 % | 133.2 px | 0.31 | 0.70 | 188 |
| stroke 19 | 38 % → 24 % | 113.0 px | 0.32 | 0.63 | 188 |
| stroke 20 | 40 % → 23 % | 125.2 px | 0.32 | 0.57 | 223 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #05 Henry Ward green in rust loops — own sheet
own sheet 600 × 600 · Impasto 1.00 · 20 px · 2.2 s

![Brush Artist · Refs · #05 Henry Ward green in rust loops — own sheet](Brush-Artist-Refs-05-Henry-Ward-green-in-rust-loops-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 11 % → 16 % | 19.1 px | 0.02 | 1.49 | 107 |
| stroke 2 | 12 % → 10 % | 24.0 px | 0.02 | 0.86 | 147 |
| stroke 3 | 20 % → 17 % | 35.4 px | 0.02 | 0.89 | 117 |

## Brush Artist · Refs · #06 Henry Ward scrubbed grey — own sheet
own sheet 600 × 600 · Gouache 1.00 · 50 px · 10.8 s

![Brush Artist · Refs · #06 Henry Ward scrubbed grey — own sheet](Brush-Artist-Refs-06-Henry-Ward-scrubbed-grey-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 6 % → 24 % | 15.9 px | 0.32 | 3.69 | 165 |
| stroke 2 | 16 % → 25 % | 41.5 px | 0.31 | 1.58 | 196 |
| stroke 3 | 21 % → 23 % | 64.7 px | 0.31 | 1.10 | 188 |
| stroke 4 | 25 % → 24 % | 78.0 px | 0.31 | 0.96 | 219 |
| stroke 5 | 31 % → 30 % | 92.8 px | 0.31 | 0.97 | 195 |
| stroke 6 | 38 % → 31 % | 115.7 px | 0.31 | 0.81 | 209 |
| stroke 7 | 36 % → 35 % | 103.6 px | 0.31 | 0.98 | 210 |
| stroke 8 | 40 % → 36 % | 125.1 px | 0.31 | 0.90 | 193 |
| stroke 9 | 35 % → 37 % | 107.6 px | 0.31 | 1.06 | 155 |
| stroke 10 | 34 % → 38 % | 111.3 px | 0.31 | 1.10 | 158 |
| stroke 11 | 35 % → 37 % | 101.5 px | 0.31 | 1.06 | 205 |
| stroke 12 | 33 % → 35 % | 99.4 px | 0.31 | 1.08 | 151 |
| stroke 13 | 24 % → 37 % | 69.3 px | 0.31 | 1.53 | 174 |
| stroke 14 | 30 % → 39 % | 88.5 px | 0.31 | 1.30 | 211 |
| stroke 15 | 33 % → 44 % | 95.1 px | 0.32 | 1.34 | 169 |
| stroke 16 | 35 % → 45 % | 111.8 px | 0.32 | 1.28 | 210 |
| stroke 17 | 37 % → 42 % | 110.5 px | 0.32 | 1.12 | 182 |
| stroke 18 | 41 % → 40 % | 123.6 px | 0.32 | 0.98 | 206 |
| stroke 19 | 38 % → 35 % | 112.0 px | 0.32 | 0.93 | 193 |
| stroke 20 | 38 % → 34 % | 117.9 px | 0.32 | 0.90 | 211 |
| stroke 21 | 40 % → 30 % | 116.2 px | 0.33 | 0.75 | 278 |
| stroke 22 | 39 % → 28 % | 127.1 px | 0.33 | 0.73 | 178 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #07 Henry Ward blue L + black zigzag — own sheet
own sheet 600 × 600 · Impasto 1.00 · 34 px · 1.9 s

![Brush Artist · Refs · #07 Henry Ward blue L + black zigzag — own sheet](Brush-Artist-Refs-07-Henry-Ward-blue-L-black-zigzag-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 13 % → 15 % | 31.2 px | 0.58 | 1.09 | 118 |
| stroke 2 | 15 % → 14 % | 37.7 px | 0.58 | 0.90 | 85 |

## Brush Artist · Refs · #08 Henry Ward olive bands — own sheet
own sheet 600 × 600 · Gouache 1.00 · 34 px · 5.0 s

![Brush Artist · Refs · #08 Henry Ward olive bands — own sheet](Brush-Artist-Refs-08-Henry-Ward-olive-bands-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 8 % → 4 % | 15.7 px | 0.58 | 0.53 | 143 |
| stroke 2 | 12 % → 4 % | 28.0 px | 0.58 | 0.35 | 159 |
| stroke 3 | 13 % → 11 % | 27.5 px | 0.58 | 0.87 | 160 |
| stroke 4 | 17 % → 10 % | 37.3 px | 0.58 | 0.57 | 185 |
| stroke 5 | 22 % → 13 % | 45.2 px | 0.56 | 0.59 | 185 |
| stroke 6 | 16 % → 6 % | 30.5 px | 0.54 | 0.40 | 172 |

## Brush Artist · Refs · #09 Henry Ward white loops — own sheet
own sheet 600 × 600 · Gouache 1.00 · 46 px · 6.3 s

![Brush Artist · Refs · #09 Henry Ward white loops — own sheet](Brush-Artist-Refs-09-Henry-Ward-white-loops-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 23 % → 0 % | 12.1 px | 0.06 | 0.00 | 824 |
| stroke 2 | 27 % → 0 % | 27.4 px | 0.07 | 0.00 | 990 |
| stroke 3 | 34 % → 0 % | 31.4 px | 0.07 | 0.00 | 914 |
| stroke 4 | 8 % → 0 % | 18.4 px | 0.00 | 0.00 | 180 |
| stroke 5 | 5 % → 0 % | 14.8 px | 0.06 | 0.00 | 195 |
| stroke 6 | 5 % → 0 % | 13.8 px | 0.08 | 0.00 | 161 |
| stroke 7 | 10 % → 0 % | 26.8 px | 0.08 | 0.00 | 156 |
| stroke 8 | 5 % → 0 % | 8.2 px | 0.00 | 0.00 | 162 |

## Brush Artist · Refs · #10 Henry Ward maroon loops — own sheet
own sheet 600 × 600 · Impasto 1.00 · 30 px · 3.1 s

![Brush Artist · Refs · #10 Henry Ward maroon loops — own sheet](Brush-Artist-Refs-10-Henry-Ward-maroon-loops-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 12 % → 26 % | 28.9 px | 0.72 | 2.25 | 205 |
| stroke 2 | 23 % → 39 % | 51.0 px | 0.72 | 1.74 | 114 |
| stroke 3 | 30 % → 36 % | 59.6 px | 0.72 | 1.20 | 166 |
| stroke 4 | 40 % → 38 % | 91.4 px | 0.72 | 0.94 | 116 |
| stroke 5 | 33 % → 29 % | 82.1 px | 0.71 | 0.89 | 156 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #11 Henry Ward purple spun balls — own sheet
own sheet 600 × 600 · Impasto 1.00 · 36 px · 2.7 s

![Brush Artist · Refs · #11 Henry Ward purple spun balls — own sheet](Brush-Artist-Refs-11-Henry-Ward-purple-spun-balls-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 22 % → 31 % | 24.4 px | 0.69 | 1.42 | 213 |
| stroke 2 | 31 % → 44 % | 34.3 px | 0.69 | 1.39 | 207 |
| stroke 3 | 34 % → 33 % | 37.7 px | 0.69 | 0.97 | 252 |

## Brush Artist · Refs · #12 Henry Ward black-olive cage — own sheet
own sheet 600 × 600 · Gouache 1.00 · 28 px · 5.0 s

![Brush Artist · Refs · #12 Henry Ward black-olive cage — own sheet](Brush-Artist-Refs-12-Henry-Ward-black-olive-cage-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 9 % → 10 % | 17.0 px | 0.58 | 1.15 | 198 |
| stroke 2 | 7 % → 10 % | 15.8 px | 0.58 | 1.46 | 167 |
| stroke 3 | 18 % → 13 % | 28.0 px | 0.58 | 0.72 | 224 |
| stroke 4 | 20 % → 14 % | 39.4 px | 0.59 | 0.70 | 135 |
| stroke 5 | 18 % → 7 % | 33.8 px | 0.58 | 0.40 | 135 |
| stroke 6 | 29 % → 15 % | 54.8 px | 0.58 | 0.52 | 217 |

## Brush Artist · Refs · #13 Henry Ward blue streaky form — own sheet
own sheet 600 × 600 · Gouache 1.00 · 50 px · 8.9 s

![Brush Artist · Refs · #13 Henry Ward blue streaky form — own sheet](Brush-Artist-Refs-13-Henry-Ward-blue-streaky-form-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 5 % → 0 % | 15.9 px | 0.00 | 0.00 | 160 |
| stroke 2 | 13 % → 0 % | 40.6 px | 0.00 | 0.00 | 189 |
| stroke 3 | 22 % → 0 % | 62.3 px | 0.00 | 0.00 | 180 |
| stroke 4 | 24 % → 0 % | 78.4 px | 0.00 | 0.00 | 218 |
| stroke 5 | 31 % → 0 % | 90.1 px | 0.00 | 0.00 | 186 |
| stroke 6 | 37 % → 0 % | 105.3 px | 0.00 | 0.00 | 233 |
| stroke 7 | 36 % → 0 % | 107.2 px | 0.00 | 0.00 | 197 |
| stroke 8 | 40 % → 0 % | 120.3 px | 0.00 | 0.00 | 188 |
| stroke 9 | 33 % → 0 % | 102.9 px | 0.00 | 0.00 | 172 |
| stroke 10 | 32 % → 0 % | 105.4 px | 0.00 | 0.00 | 167 |
| stroke 11 | 30 % → 0 % | 92.1 px | 0.00 | 0.00 | 202 |
| stroke 12 | 26 % → 0 % | 78.3 px | 0.00 | 0.00 | 167 |
| stroke 13 | 24 % → 0 % | 74.8 px | 0.00 | 0.00 | 172 |
| stroke 14 | 29 % → 0 % | 84.9 px | 0.00 | 0.00 | 236 |
| stroke 15 | 30 % → 0 % | 86.3 px | 0.00 | 0.00 | 183 |
| stroke 16 | 35 % → 0 % | 104.8 px | 0.00 | 0.00 | 221 |
| stroke 17 | 41 % → 0 % | 103.0 px | 0.00 | 0.00 | 191 |
| stroke 18 | 49 % → 0 % | 117.7 px | 0.00 | 0.00 | 208 |
| stroke 19 | 51 % → 0 % | 104.2 px | 0.00 | 0.00 | 193 |
| stroke 20 | 60 % → 0 % | 115.5 px | 0.00 | 0.00 | 211 |
| stroke 21 | 7 % → 0 % | 15.0 px | 0.00 | 0.00 | 161 |
| stroke 22 | 6 % → 0 % | 18.5 px | 0.00 | 0.00 | 162 |
| stroke 23 | 11 % → 0 % | 35.1 px | 0.00 | 0.00 | 147 |
| stroke 24 | 4 % → 0 % | 11.0 px | 0.00 | 0.00 | 142 |
| stroke 25 | 4 % → 0 % | 9.1 px | 0.00 | 0.00 | 138 |

## Brush Artist · Refs · #14 Henry Ward olive totem — own sheet
own sheet 600 × 600 · Impasto 1.00 · 48 px · 6.8 s

![Brush Artist · Refs · #14 Henry Ward olive totem — own sheet](Brush-Artist-Refs-14-Henry-Ward-olive-totem-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 18 % → 46 % | 46.6 px | 0.38 | 2.57 | 138 |
| stroke 2 | 20 % → 50 % | 61.7 px | 0.38 | 2.53 | 133 |
| stroke 3 | 27 % → 52 % | 93.9 px | 0.39 | 1.89 | 132 |
| stroke 4 | 30 % → 54 % | 110.9 px | 0.39 | 1.82 | 151 |
| stroke 5 | 38 % → 63 % | 134.1 px | 0.39 | 1.64 | 139 |
| stroke 6 | 38 % → 64 % | 149.8 px | 0.39 | 1.67 | 288 |
| stroke 7 | 35 % → 60 % | 119.1 px | 0.39 | 1.70 | 133 |
| stroke 8 | 37 % → 62 % | 141.6 px | 0.39 | 1.67 | 150 |
| stroke 9 | 38 % → 62 % | 131.6 px | 0.39 | 1.64 | 131 |
| stroke 10 | 37 % → 61 % | 136.5 px | 0.39 | 1.65 | 142 |
| stroke 11 | 38 % → 64 % | 136.7 px | 0.39 | 1.66 | 130 |
| stroke 12 | 38 % → 64 % | 143.5 px | 0.38 | 1.68 | 131 |
| stroke 13 | 37 % → 66 % | 129.3 px | 0.39 | 1.78 | 113 |
| stroke 14 | 36 % → 61 % | 131.1 px | 0.39 | 1.70 | 157 |
| stroke 15 | 39 % → 65 % | 134.4 px | 0.39 | 1.66 | 129 |
| stroke 16 | 38 % → 63 % | 136.6 px | 0.39 | 1.67 | 144 |
| stroke 17 | 37 % → 61 % | 124.1 px | 0.39 | 1.64 | 162 |
| stroke 18 | 40 % → 65 % | 152.2 px | 0.39 | 1.63 | 137 |
| stroke 19 | 38 % → 58 % | 131.3 px | 0.39 | 1.54 | 136 |
| stroke 20 | 40 % → 53 % | 142.6 px | 0.39 | 1.31 | 173 |
| stroke 21 | 46 % → 53 % | 136.0 px | 0.39 | 1.15 | 142 |
| stroke 22 | 53 % → 51 % | 143.0 px | 0.39 | 0.97 | 145 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #15 Ultramarine brush script — own sheet
own sheet 600 × 600 · Ink 1.00 · 4 px · 8.2 s

![Brush Artist · Refs · #15 Ultramarine brush script — own sheet](Brush-Artist-Refs-15-Ultramarine-brush-script-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 40 % → 42 % | 9.0 px | 0.65 | 1.05 | 48 |
| stroke 2 | 41 % → 43 % | 9.0 px | 0.67 | 1.07 | 45 |
| stroke 3 | 39 % → 42 % | 9.4 px | 0.72 | 1.08 | 25 |
| stroke 4 | 42 % → 46 % | 10.2 px | 0.74 | 1.10 | 15 |
| stroke 5 | 46 % → 49 % | 10.1 px | 0.72 | 1.06 | 22 |
| stroke 6 | 43 % → 45 % | 9.7 px | 0.65 | 1.05 | 77 |
| stroke 7 | 44 % → 47 % | 9.3 px | 0.72 | 1.08 | 31 |
| stroke 8 | 37 % → 39 % | 8.9 px | 0.65 | 1.06 | 41 |
| stroke 9 | 39 % → 42 % | 9.1 px | 0.70 | 1.07 | 39 |
| stroke 10 | 35 % → 37 % | 9.6 px | 0.66 | 1.05 | 40 |
| stroke 11 | 44 % → 47 % | 9.9 px | 0.69 | 1.06 | 37 |
| stroke 12 | 39 % → 41 % | 9.4 px | 0.65 | 1.06 | 38 |
| stroke 13 | 45 % → 46 % | 10.1 px | 0.69 | 1.04 | 21 |
| stroke 14 | 37 % → 40 % | 9.6 px | 0.71 | 1.07 | 25 |
| stroke 15 | 37 % → 38 % | 9.0 px | 0.67 | 1.05 | 46 |
| stroke 16 | 42 % → 45 % | 9.4 px | 0.70 | 1.06 | 28 |
| stroke 17 | 41 % → 45 % | 7.1 px | 0.71 | 1.09 | 40 |
| stroke 18 | 43 % → 45 % | 9.3 px | 0.73 | 1.05 | 29 |
| stroke 19 | 40 % → 42 % | 9.0 px | 0.65 | 1.06 | 56 |
| stroke 20 | 42 % → 44 % | 9.7 px | 0.69 | 1.06 | 35 |
| stroke 21 | 39 % → 42 % | 9.6 px | 0.69 | 1.07 | 36 |
| stroke 22 | 44 % → 46 % | 8.9 px | 0.65 | 1.06 | 44 |
| stroke 23 | 38 % → 42 % | 9.5 px | 0.72 | 1.10 | 18 |
| stroke 24 | 39 % → 42 % | 9.1 px | 0.73 | 1.06 | 37 |
| stroke 25 | 41 % → 44 % | 10.0 px | 0.71 | 1.06 | 25 |
| stroke 26 | 45 % → 47 % | 9.1 px | 0.66 | 1.04 | 49 |
| stroke 27 | 43 % → 45 % | 9.0 px | 0.62 | 1.05 | 63 |
| stroke 28 | 45 % → 47 % | 9.3 px | 0.70 | 1.06 | 35 |
| stroke 29 | 35 % → 38 % | 10.4 px | 0.69 | 1.08 | 26 |
| stroke 30 | 39 % → 40 % | 8.5 px | 0.70 | 1.04 | 36 |
| stroke 31 | 43 % → 46 % | 10.4 px | 0.74 | 1.07 | 17 |
| stroke 32 | 41 % → 45 % | 9.3 px | 0.70 | 1.09 | 22 |
| stroke 33 | 35 % → 40 % | 10.9 px | 0.73 | 1.13 | 19 |
| stroke 34 | 41 % → 45 % | 10.1 px | 0.74 | 1.09 | 22 |
| stroke 35 | 36 % → 38 % | 9.4 px | 0.67 | 1.06 | 42 |

## Brush Artist · Refs · #18 Blue oil-stick scribbles — own sheet
own sheet 600 × 600 · Pastel 1.00 · 10 px · 3.0 s

![Brush Artist · Refs · #18 Blue oil-stick scribbles — own sheet](Brush-Artist-Refs-18-Blue-oil-stick-scribbles-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 16 % → 32 % | 3.9 px | 0.49 | 2.03 | 131 |
| stroke 2 | 13 % → 37 % | 3.6 px | 0.49 | 2.75 | 140 |
| stroke 3 | 16 % → 26 % | 5.8 px | 0.49 | 1.64 | 169 |
| stroke 4 | 15 % → 29 % | 7.9 px | 0.49 | 1.91 | 160 |
| stroke 5 | 29 % → 34 % | 8.5 px | 0.49 | 1.18 | 158 |
| stroke 6 | 26 % → 26 % | 9.4 px | 0.49 | 1.02 | 141 |
| stroke 7 | 26 % → 32 % | 8.4 px | 0.49 | 1.24 | 177 |
| stroke 8 | 30 % → 30 % | 17.0 px | 0.49 | 1.00 | 171 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #20 Orange-red crayon scribble — own sheet
own sheet 600 × 600 · Pastel 1.00 · 14 px · 2.7 s

![Brush Artist · Refs · #20 Orange-red crayon scribble — own sheet](Brush-Artist-Refs-20-Orange-red-crayon-scribble-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 8 % → 19 % | 5.5 px | 0.59 | 2.47 | 203 |
| stroke 2 | 9 % → 22 % | 6.6 px | 0.60 | 2.50 | 166 |
| stroke 3 | 13 % → 21 % | 8.3 px | 0.60 | 1.65 | 157 |
| stroke 4 | 24 % → 32 % | 8.8 px | 0.60 | 1.36 | 178 |
| stroke 5 | 28 % → 28 % | 7.9 px | 0.59 | 1.00 | 145 |
| stroke 6 | 22 % → 22 % | 16.4 px | 0.60 | 1.00 | 148 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #21 Gritty black contours — own sheet
own sheet 600 × 600 · Gouache 1.00 · 12 px · 3.8 s

![Brush Artist · Refs · #21 Gritty black contours — own sheet](Brush-Artist-Refs-21-Gritty-black-contours-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 6 % → 4 % | 6.2 px | 0.36 | 0.68 | 134 |
| stroke 2 | 5 % → 2 % | 7.9 px | 0.36 | 0.47 | 180 |
| stroke 3 | 9 % → 2 % | 7.8 px | 0.37 | 0.17 | 103 |
| stroke 4 | 9 % → 3 % | 10.9 px | 0.36 | 0.36 | 120 |
| stroke 5 | 10 % → 4 % | 12.7 px | 0.35 | 0.35 | 81 |

## Brush Artist · Refs · #22 Bold black brush poster — own sheet
own sheet 600 × 600 · Ink 1.00 · 20 px · 4.7 s

![Brush Artist · Refs · #22 Bold black brush poster — own sheet](Brush-Artist-Refs-22-Bold-black-brush-poster-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 24 % → 28 % | 38.8 px | 0.95 | 1.18 | 99 |
| stroke 2 | 28 % → 39 % | 42.9 px | 0.94 | 1.38 | 24 |
| stroke 3 | 30 % → 30 % | 46.0 px | 0.94 | 1.00 | 38 |
| stroke 4 | 30 % → 41 % | 57.8 px | 0.94 | 1.41 | 54 |
| stroke 5 | 27 % → 27 % | 46.3 px | 0.93 | 1.00 | 82 |

## Brush Artist · Refs · #23 Dry white on orange + black line — own sheet
own sheet 600 × 600 · Gouache 1.00 · 50 px · 7.4 s

![Brush Artist · Refs · #23 Dry white on orange + black line — own sheet](Brush-Artist-Refs-23-Dry-white-on-orange-black-line-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 4 % → 11 % | 14.5 px | 0.38 | 2.70 | 116 |
| stroke 2 | 8 % → 10 % | 26.7 px | 0.38 | 1.35 | 151 |
| stroke 3 | 13 % → 11 % | 49.0 px | 0.38 | 0.81 | 125 |
| stroke 4 | 17 % → 12 % | 68.6 px | 0.38 | 0.67 | 153 |
| stroke 5 | 23 % → 13 % | 85.0 px | 0.38 | 0.55 | 148 |
| stroke 6 | 26 % → 14 % | 106.9 px | 0.38 | 0.53 | 147 |
| stroke 7 | 23 % → 13 % | 86.4 px | 0.38 | 0.57 | 128 |
| stroke 8 | 22 % → 12 % | 87.4 px | 0.38 | 0.53 | 146 |
| stroke 9 | 19 % → 11 % | 69.7 px | 0.38 | 0.60 | 131 |
| stroke 10 | 18 % → 11 % | 68.9 px | 0.38 | 0.63 | 138 |
| stroke 11 | 20 % → 11 % | 73.3 px | 0.38 | 0.56 | 142 |
| stroke 12 | 19 % → 12 % | 72.9 px | 0.38 | 0.65 | 130 |
| stroke 13 | 20 % → 14 % | 75.6 px | 0.38 | 0.70 | 137 |
| stroke 14 | 21 % → 14 % | 84.0 px | 0.38 | 0.64 | 163 |
| stroke 15 | 21 % → 13 % | 79.6 px | 0.38 | 0.62 | 148 |
| stroke 16 | 22 % → 11 % | 87.4 px | 0.38 | 0.52 | 155 |
| stroke 17 | 22 % → 9 % | 76.2 px | 0.38 | 0.40 | 143 |
| stroke 18 | 27 % → 9 % | 99.3 px | 0.38 | 0.34 | 126 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #24 Picasso flat oil — own sheet
own sheet 600 × 600 · Oil 0.89 · Oil glaze 0.11 · 34 px · 5.1 s

![Brush Artist · Refs · #24 Picasso flat oil — own sheet](Brush-Artist-Refs-24-Picasso-flat-oil-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 14 % → 44 % | 30.0 px | 0.22 | 3.11 | 126 |
| stroke 2 | 19 % → 47 % | 44.5 px | 0.23 | 2.49 | 127 |
| stroke 3 | 27 % → 56 % | 59.7 px | 0.23 | 2.06 | 143 |
| stroke 4 | 37 % → 62 % | 82.9 px | 0.23 | 1.69 | 139 |
| stroke 5 | 41 % → 68 % | 91.2 px | 0.22 | 1.64 | 135 |
| stroke 6 | 42 % → 63 % | 96.5 px | 0.22 | 1.52 | 143 |
| stroke 7 | 42 % → 63 % | 87.5 px | 0.23 | 1.51 | 127 |
| stroke 8 | 42 % → 63 % | 101.6 px | 0.23 | 1.50 | 144 |
| stroke 9 | 34 % → 60 % | 74.4 px | 0.23 | 1.76 | 128 |
| stroke 10 | 38 % → 58 % | 89.8 px | 0.23 | 1.55 | 140 |
| stroke 11 | 35 % → 56 % | 74.6 px | 0.24 | 1.61 | 133 |
| stroke 12 | 37 % → 58 % | 88.3 px | 0.24 | 1.56 | 134 |
| stroke 13 | 35 % → 64 % | 77.9 px | 0.25 | 1.81 | 137 |
| stroke 14 | 36 % → 66 % | 82.0 px | 0.24 | 1.82 | 146 |
| stroke 15 | 36 % → 60 % | 76.0 px | 0.24 | 1.67 | 137 |
| stroke 16 | 36 % → 52 % | 83.2 px | 0.24 | 1.46 | 152 |
| stroke 17 | 41 % → 47 % | 86.1 px | 0.24 | 1.15 | 138 |
| stroke 18 | 42 % → 42 % | 101.0 px | 0.24 | 1.00 | 137 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #25 Yellow heavy flat stroke — own sheet
own sheet 600 × 600 · Impasto 1.00 · 110 px · 2.8 s

![Brush Artist · Refs · #25 Yellow heavy flat stroke — own sheet](Brush-Artist-Refs-25-Yellow-heavy-flat-stroke-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 18 % → 18 % | 103.7 px | 0.16 | 0.98 | 655 |

## Brush Artist · Refs · #27 Orange impasto swatch — own sheet
own sheet 600 × 600 · Impasto 1.00 · 60 px · 3.0 s

![Brush Artist · Refs · #27 Orange impasto swatch — own sheet](Brush-Artist-Refs-27-Orange-impasto-swatch-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 8 % → 21 % | 58.4 px | 0.32 | 2.66 | 71 |
| stroke 2 | 7 % → 33 % | 62.2 px | 0.32 | 4.61 | 47 |
| stroke 3 | 25 % → 34 % | 238.0 px | 0.32 | 1.41 | 44 |
| stroke 4 | 10 % → 12 % | 69.5 px | 0.34 | 1.26 | 79 |
| stroke 5 | 17 % → 32 % | 61.8 px | 0.31 | 1.90 | 67 |
| stroke 6 | 17 % → 31 % | 143.7 px | 0.32 | 1.77 | 67 |
| stroke 7 | 8 % → 14 % | 68.6 px | 0.31 | 1.88 | 47 |
| stroke 8 | 32 % → 33 % | 328.8 px | 0.32 | 1.04 | 59 |
| stroke 9 | 37 % → 36 % | 182.9 px | 0.32 | 0.97 | 77 |
| stroke 10 | 33 % → 32 % | 298.6 px | 0.32 | 0.97 | 58 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #28 Miles Davis black lines — own sheet
own sheet 600 × 600 · Ink 1.00 · 22 px · 5.5 s

![Brush Artist · Refs · #28 Miles Davis black lines — own sheet](Brush-Artist-Refs-28-Miles-Davis-black-lines-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 22 % → 31 % | 36.1 px | 0.88 | 1.42 | 166 |
| stroke 2 | 26 % → 47 % | 35.8 px | 0.88 | 1.79 | 123 |
| stroke 3 | 38 % → 42 % | 73.3 px | 0.88 | 1.11 | 97 |
| stroke 4 | 41 % → 47 % | 81.4 px | 0.88 | 1.16 | 150 |
| stroke 5 | 54 % → 54 % | 108.2 px | 0.88 | 1.00 | 140 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #29 Shrigley magenta asterisk — own sheet
own sheet 600 × 600 · Watercolour 1.00 · 70 px · 5.8 s

![Brush Artist · Refs · #29 Shrigley magenta asterisk — own sheet](Brush-Artist-Refs-29-Shrigley-magenta-asterisk-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 13 % → 37 % | 46.6 px | 0.67 | 2.86 | 174 |
| stroke 2 | 12 % → 12 % | 87.1 px | 0.67 | 1.00 | 176 |
| stroke 3 | 28 % → 37 % | 100.9 px | 0.67 | 1.31 | 183 |
| stroke 4 | 23 % → 23 % | 164.0 px | 0.67 | 1.02 | 195 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #30 Red gouache face patch — own sheet
own sheet 600 × 600 · Gouache 1.00 · 60 px · 11.4 s

![Brush Artist · Refs · #30 Red gouache face patch — own sheet](Brush-Artist-Refs-30-Red-gouache-face-patch-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 11 % → 37 % | 50.6 px | 0.54 | 3.29 | 154 |
| stroke 2 | 15 % → 41 % | 74.2 px | 0.54 | 2.74 | 161 |
| stroke 3 | 24 % → 50 % | 115.1 px | 0.54 | 2.08 | 176 |
| stroke 4 | 26 % → 52 % | 133.4 px | 0.54 | 1.95 | 192 |
| stroke 5 | 34 % → 60 % | 160.6 px | 0.54 | 1.77 | 193 |
| stroke 6 | 35 % → 61 % | 178.6 px | 0.54 | 1.76 | 201 |
| stroke 7 | 35 % → 59 % | 164.2 px | 0.54 | 1.70 | 177 |
| stroke 8 | 34 % → 56 % | 162.3 px | 0.54 | 1.66 | 200 |
| stroke 9 | 36 % → 60 % | 172.7 px | 0.53 | 1.66 | 171 |
| stroke 10 | 38 % → 62 % | 196.7 px | 0.53 | 1.64 | 200 |
| stroke 11 | 37 % → 61 % | 181.6 px | 0.53 | 1.67 | 189 |
| stroke 12 | 36 % → 58 % | 179.8 px | 0.53 | 1.60 | 182 |
| stroke 13 | 33 % → 46 % | 157.0 px | 0.53 | 1.38 | 168 |
| stroke 14 | 33 % → 41 % | 159.9 px | 0.53 | 1.24 | 212 |
| stroke 15 | 33 % → 37 % | 153.6 px | 0.53 | 1.12 | 180 |
| stroke 16 | 39 % → 39 % | 186.3 px | 0.53 | 0.98 | 183 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #31 Warhol blotted line — own sheet
own sheet 600 × 600 · Ink 1.00 · 6 px · 4.6 s

![Brush Artist · Refs · #31 Warhol blotted line — own sheet](Brush-Artist-Refs-31-Warhol-blotted-line-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 22 % → 43 % | 16.5 px | 0.83 | 1.94 | 77 |
| stroke 2 | 17 % → 23 % | 15.7 px | 0.81 | 1.35 | 70 |
| stroke 3 | 24 % → 25 % | 24.9 px | 0.81 | 1.03 | 79 |
| stroke 4 | 32 % → 41 % | 32.7 px | 0.83 | 1.28 | 51 |
| stroke 5 | 37 % → 45 % | 38.1 px | 0.83 | 1.21 | 63 |
| stroke 6 | 34 % → 35 % | 27.8 px | 0.81 | 1.03 | 64 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #32 Thick orange swipes — own sheet
own sheet 600 × 600 · Impasto 1.00 · 90 px · 3.5 s

![Brush Artist · Refs · #32 Thick orange swipes — own sheet](Brush-Artist-Refs-32-Thick-orange-swipes-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 14 % → 27 % | 86.6 px | 0.02 | 1.89 | 331 |
| stroke 2 | 26 % → 37 % | 177.9 px | 0.02 | 1.41 | 300 |
| stroke 3 | 27 % → 27 % | 176.1 px | 0.02 | 0.98 | 332 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #33 Red wet-in-wet band — own sheet
own sheet 600 × 600 · Watercolour 1.00 · 80 px · 9.9 s

![Brush Artist · Refs · #33 Red wet-in-wet band — own sheet](Brush-Artist-Refs-33-Red-wet-in-wet-band-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 22 % → 57 % | 83.4 px | 0.61 | 2.61 | 403 |
| stroke 2 | 28 % → 51 % | 228.4 px | 0.62 | 1.82 | 127 |
| stroke 3 | 34 % → 53 % | 330.0 px | 0.61 | 1.57 | 153 |
| stroke 4 | 40 % → 60 % | 389.9 px | 0.62 | 1.51 | 102 |
| stroke 5 | 40 % → 55 % | 339.4 px | 0.61 | 1.38 | 131 |
| stroke 6 | 41 % → 48 % | 310.3 px | 0.59 | 1.18 | 134 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #34 Magenta oil patches — own sheet
own sheet 600 × 600 · Oil 0.89 · Oil glaze 0.11 · 60 px · 3.4 s

![Brush Artist · Refs · #34 Magenta oil patches — own sheet](Brush-Artist-Refs-34-Magenta-oil-patches-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 8 % → 39 % | 57.1 px | 0.13 | 4.77 | 93 |
| stroke 2 | 8 % → 28 % | 56.8 px | 0.14 | 3.32 | 77 |
| stroke 3 | 7 % → 32 % | 58.6 px | 0.13 | 4.60 | 66 |
| stroke 4 | 15 % → 19 % | 122.2 px | 0.12 | 1.26 | 69 |
| stroke 5 | 21 % → 30 % | 112.2 px | 0.13 | 1.45 | 87 |
| stroke 6 | 19 % → 36 % | 159.7 px | 0.13 | 1.91 | 78 |
| stroke 7 | 28 % → 33 % | 226.6 px | 0.13 | 1.17 | 115 |
| stroke 8 | 30 % → 37 % | 213.6 px | 0.13 | 1.21 | 96 |
| stroke 9 | 23 % → 25 % | 147.9 px | 0.14 | 1.07 | 94 |
| stroke 10 | 27 % → 27 % | 240.6 px | 0.14 | 1.00 | 70 |
| stroke 11 | 33 % → 33 % | 297.2 px | 0.13 | 1.00 | 59 |
| stroke 12 | 24 % → 24 % | 173.6 px | 0.13 | 1.00 | 70 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #35 Red band with runs — own sheet
own sheet 600 × 600 · Watercolour 1.00 · 70 px · 7.9 s

![Brush Artist · Refs · #35 Red band with runs — own sheet](Brush-Artist-Refs-35-Red-band-with-runs-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 37 % → 47 % | 140.3 px | 0.45 | 1.27 | 328 |

## Brush Artist · Refs · #36 Magenta letters flat brush — own sheet
own sheet 600 × 600 · Gouache 1.00 · 36 px · 10.5 s

![Brush Artist · Refs · #36 Magenta letters flat brush — own sheet](Brush-Artist-Refs-36-Magenta-letters-flat-brush-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 20 % → 38 % | 58.3 px | 0.50 | 1.95 | 33 |
| stroke 2 | 20 % → 31 % | 45.2 px | 0.51 | 1.54 | 35 |
| stroke 3 | 28 % → 52 % | 84.6 px | 0.50 | 1.83 | 30 |
| stroke 4 | 26 % → 44 % | 50.3 px | 0.51 | 1.69 | 123 |
| stroke 5 | 33 % → 54 % | 96.3 px | 0.50 | 1.63 | 74 |
| stroke 6 | 43 % → 56 % | 246.0 px | 0.49 | 1.30 | 19 |
| stroke 7 | 30 % → 43 % | 56.6 px | 0.50 | 1.43 | 121 |
| stroke 8 | 31 % → 52 % | 97.7 px | 0.51 | 1.66 | 84 |
| stroke 9 | 38 % → 50 % | 158.2 px | 0.51 | 1.31 | 34 |
| stroke 10 | 37 % → 62 % | 107.5 px | 0.50 | 1.68 | 82 |
| stroke 11 | 39 % → 61 % | 225.6 px | 0.49 | 1.55 | 20 |
| stroke 12 | 44 % → 55 % | 82.9 px | 0.50 | 1.26 | 165 |
| stroke 13 | 31 % → 45 % | 113.5 px | 0.51 | 1.43 | 37 |
| stroke 14 | 34 % → 50 % | 129.9 px | 0.51 | 1.47 | 33 |
| stroke 15 | 36 % → 54 % | 105.5 px | 0.50 | 1.49 | 71 |
| stroke 16 | 39 % → 47 % | 221.7 px | 0.50 | 1.23 | 12 |
| stroke 17 | 43 % → 51 % | 81.6 px | 0.50 | 1.18 | 130 |
| stroke 18 | 26 % → 35 % | 95.6 px | 0.50 | 1.34 | 34 |
| stroke 19 | 39 % → 37 % | 112.8 px | 0.50 | 0.97 | 37 |
| stroke 20 | 45 % → 44 % | 129.9 px | 0.51 | 0.98 | 40 |
| stroke 21 | 40 % → 38 % | 78.2 px | 0.50 | 0.94 | 91 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #37 Oil still life dabs — own sheet
own sheet 600 × 600 · Oil 0.89 · Oil glaze 0.11 · 40 px · 2.5 s

![Brush Artist · Refs · #37 Oil still life dabs — own sheet](Brush-Artist-Refs-37-Oil-still-life-dabs-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 6 % → 6 % | 38.2 px | 0.37 | 1.00 | 31 |
| stroke 2 | 6 % → 26 % | 39.8 px | 0.40 | 4.69 | 22 |
| stroke 3 | 11 % → 33 % | 86.6 px | 0.39 | 3.00 | 18 |
| stroke 4 | 8 % → 8 % | 39.3 px | 0.37 | 1.00 | 45 |
| stroke 5 | 6 % → 10 % | 43.2 px | 0.38 | 1.67 | 21 |
| stroke 6 | 13 % → 29 % | 80.2 px | 0.40 | 2.26 | 28 |
| stroke 7 | 11 % → 22 % | 113.9 px | 0.38 | 2.08 | 10 |
| stroke 8 | 8 % → 13 % | 85.3 px | 0.38 | 1.59 | 15 |
| stroke 9 | 12 % → 13 % | 61.1 px | 0.36 | 1.12 | 43 |
| stroke 10 | 20 % → 24 % | 100.4 px | 0.40 | 1.20 | 39 |
| stroke 11 | 23 % → 27 % | 194.4 px | 0.41 | 1.15 | 19 |
| stroke 12 | 20 % → 20 % | 212.5 px | 0.39 | 1.00 | 9 |
| stroke 13 | 15 % → 15 % | 150.5 px | 0.42 | 1.00 | 15 |
| stroke 14 | 15 % → 15 % | 121.2 px | 0.38 | 1.00 | 13 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #38 Sanguine drawing — own sheet
own sheet 600 × 600 · Pastel 1.00 · 6 px · 2.2 s

![Brush Artist · Refs · #38 Sanguine drawing — own sheet](Brush-Artist-Refs-38-Sanguine-drawing-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 3 % → 15 % | 3.3 px | 0.57 | 4.99 | 8 |
| stroke 2 | 3 % → 8 % | 2.9 px | 0.57 | 3.03 | 7 |
| stroke 3 | 3 % → 9 % | 3.3 px | 0.57 | 3.13 | 4 |
| stroke 4 | 2 % → 18 % | 2.8 px | 0.57 | 7.17 | 6 |
| stroke 5 | 3 % → 7 % | 2.9 px | 0.57 | 2.87 | 4 |
| stroke 6 | 3 % → 19 % | 3.5 px | 0.57 | 6.36 | 5 |
| stroke 7 | 5 % → 15 % | 5.3 px | 0.57 | 3.13 | 4 |
| stroke 8 | 4 % → 16 % | 4.8 px | 0.57 | 3.71 | 5 |
| stroke 9 | 3 % → 8 % | 3.4 px | 0.57 | 2.52 | 6 |
| stroke 10 | 4 % → 16 % | 4.9 px | 0.57 | 3.75 | 7 |
| stroke 11 | 3 % → 4 % | 3.0 px | 0.57 | 1.63 | 7 |
| stroke 12 | 4 % → 16 % | 4.7 px | 0.57 | 3.75 | 6 |
| stroke 13 | 8 % → 18 % | 9.2 px | 0.57 | 2.20 | 4 |
| stroke 14 | 5 % → 14 % | 5.3 px | 0.57 | 2.95 | 7 |
| stroke 15 | 9 % → 18 % | 10.7 px | 0.57 | 1.88 | 6 |
| stroke 16 | 6 % → 16 % | 7.0 px | 0.57 | 2.64 | 6 |
| stroke 17 | 4 % → 9 % | 5.0 px | 0.57 | 2.12 | 7 |
| stroke 18 | 3 % → 5 % | 3.1 px | 0.57 | 1.89 | 4 |
| stroke 19 | 6 % → 17 % | 7.4 px | 0.57 | 2.68 | 6 |
| stroke 20 | 9 % → 14 % | 9.8 px | 0.57 | 1.66 | 5 |
| stroke 21 | 4 % → 4 % | 4.6 px | 0.57 | 1.00 | 5 |
| stroke 22 | 8 % → 14 % | 9.2 px | 0.57 | 1.71 | 7 |
| stroke 23 | 8 % → 12 % | 8.7 px | 0.57 | 1.63 | 4 |
| stroke 24 | 4 % → 8 % | 5.0 px | 0.57 | 1.72 | 6 |
| stroke 25 | 8 % → 15 % | 9.3 px | 0.57 | 1.87 | 5 |
| stroke 26 | 6 % → 8 % | 6.9 px | 0.57 | 1.32 | 6 |
| stroke 27 | 4 % → 5 % | 4.8 px | 0.57 | 1.07 | 5 |
| stroke 28 | 8 % → 13 % | 8.9 px | 0.57 | 1.61 | 6 |
| stroke 29 | 8 % → 17 % | 9.0 px | 0.57 | 2.18 | 6 |
| stroke 30 | 13 % → 17 % | 15.2 px | 0.57 | 1.29 | 4 |
| stroke 31 | 5 % → 7 % | 6.0 px | 0.57 | 1.24 | 6 |
| stroke 32 | 11 % → 14 % | 12.9 px | 0.57 | 1.23 | 7 |
| stroke 33 | 8 % → 9 % | 9.5 px | 0.57 | 1.06 | 6 |
| stroke 34 | 11 % → 14 % | 12.3 px | 0.57 | 1.34 | 4 |
| stroke 35 | 9 % → 15 % | 10.7 px | 0.57 | 1.57 | 6 |
| stroke 36 | 10 % → 13 % | 11.9 px | 0.57 | 1.26 | 7 |
| stroke 37 | 10 % → 16 % | 11.4 px | 0.57 | 1.63 | 10 |
| stroke 38 | 14 % → 20 % | 15.3 px | 0.57 | 1.46 | 5 |
| stroke 39 | 14 % → 17 % | 16.5 px | 0.57 | 1.20 | 4 |
| stroke 40 | 6 % → 7 % | 7.3 px | 0.57 | 1.15 | 4 |
| stroke 41 | 16 % → 16 % | 18.2 px | 0.57 | 1.01 | 6 |
| stroke 42 | 14 % → 16 % | 16.1 px | 0.57 | 1.15 | 4 |
| stroke 43 | 11 % → 13 % | 13.0 px | 0.57 | 1.16 | 7 |
| stroke 44 | 13 % → 16 % | 15.2 px | 0.57 | 1.19 | 5 |
| stroke 45 | 2 % → 2 % | 2.8 px | 0.56 | 1.00 | 4 |
| stroke 46 | 17 % → 17 % | 18.9 px | 0.57 | 1.00 | 8 |
| stroke 47 | 14 % → 14 % | 15.9 px | 0.57 | 1.00 | 8 |
| stroke 48 | 13 % → 14 % | 14.7 px | 0.57 | 1.06 | 7 |
| stroke 49 | 19 % → 19 % | 21.8 px | 0.57 | 1.00 | 6 |
| stroke 50 | 11 % → 11 % | 12.2 px | 0.57 | 1.00 | 7 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #39 Very thick impasto — own sheet
own sheet 600 × 600 · Impasto 1.00 · 60 px · 4.3 s

![Brush Artist · Refs · #39 Very thick impasto — own sheet](Brush-Artist-Refs-39-Very-thick-impasto-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 24 % → 35 % | 55.6 px | 0.43 | 1.44 | 296 |
| stroke 2 | 30 % → 46 % | 91.2 px | 0.43 | 1.52 | 278 |
| stroke 3 | 37 % → 48 % | 123.1 px | 0.44 | 1.31 | 290 |
| stroke 4 | 31 % → 43 % | 90.2 px | 0.43 | 1.39 | 313 |
| stroke 5 | 41 % → 39 % | 102.0 px | 0.43 | 0.97 | 270 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #40 Watercolour blooms — own sheet
own sheet 600 × 600 · Watercolour 1.00 · 90 px · 8.3 s

![Brush Artist · Refs · #40 Watercolour blooms — own sheet](Brush-Artist-Refs-40-Watercolour-blooms-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 21 % → 27 % | 92.8 px | 0.12 | 1.28 | 753 |

## Brush Artist · Refs · #41 Coloured pencil hatching — own sheet
own sheet 600 × 600 · Pastel 1.00 · 4 px · 2.4 s

![Brush Artist · Refs · #41 Coloured pencil hatching — own sheet](Brush-Artist-Refs-41-Coloured-pencil-hatching-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 3 % → 15 % | 2.3 px | 0.35 | 5.04 | 4 |
| stroke 2 | 3 % → 8 % | 2.5 px | 0.35 | 2.34 | 4 |
| stroke 3 | 3 % → 12 % | 2.2 px | 0.35 | 4.03 | 5 |
| stroke 4 | 3 % → 20 % | 2.4 px | 0.35 | 6.35 | 10 |
| stroke 5 | 4 % → 8 % | 3.5 px | 0.35 | 1.78 | 9 |
| stroke 6 | 3 % → 14 % | 2.3 px | 0.35 | 4.57 | 3 |
| stroke 7 | 4 % → 17 % | 3.0 px | 0.35 | 4.34 | 4 |
| stroke 8 | 3 % → 13 % | 2.4 px | 0.35 | 4.14 | 5 |
| stroke 9 | 5 % → 12 % | 4.1 px | 0.35 | 2.18 | 3 |
| stroke 10 | 6 % → 17 % | 4.4 px | 0.35 | 2.92 | 5 |
| stroke 11 | 4 % → 14 % | 3.2 px | 0.35 | 3.38 | 3 |
| stroke 12 | 3 % → 3 % | 2.2 px | 0.35 | 1.00 | 4 |
| stroke 13 | 8 % → 19 % | 6.0 px | 0.35 | 2.35 | 5 |
| stroke 14 | 4 % → 15 % | 2.7 px | 0.35 | 4.14 | 5 |
| stroke 15 | 6 % → 13 % | 4.6 px | 0.35 | 2.12 | 5 |
| stroke 16 | 7 % → 12 % | 5.6 px | 0.35 | 1.63 | 4 |
| stroke 17 | 3 % → 3 % | 2.4 px | 0.35 | 1.00 | 4 |
| stroke 18 | 5 % → 9 % | 4.0 px | 0.36 | 1.63 | 5 |
| stroke 19 | 5 % → 14 % | 4.0 px | 0.35 | 2.72 | 5 |
| stroke 20 | 6 % → 16 % | 4.2 px | 0.35 | 2.94 | 3 |
| stroke 21 | 5 % → 15 % | 3.6 px | 0.35 | 3.13 | 5 |
| stroke 22 | 10 % → 18 % | 7.7 px | 0.35 | 1.77 | 3 |
| stroke 23 | 10 % → 15 % | 7.2 px | 0.35 | 1.54 | 4 |
| stroke 24 | 7 % → 15 % | 5.3 px | 0.35 | 2.12 | 2 |
| stroke 25 | 5 % → 12 % | 4.0 px | 0.35 | 2.27 | 5 |
| stroke 26 | 4 % → 7 % | 3.1 px | 0.35 | 1.79 | 2 |
| stroke 27 | 3 % → 8 % | 2.6 px | 0.35 | 2.35 | 4 |
| stroke 28 | 7 % → 11 % | 5.2 px | 0.36 | 1.68 | 4 |
| stroke 29 | 3 % → 15 % | 2.6 px | 0.35 | 4.48 | 4 |
| stroke 30 | 7 % → 10 % | 5.2 px | 0.35 | 1.40 | 6 |
| stroke 31 | 7 % → 16 % | 5.8 px | 0.35 | 2.09 | 3 |
| stroke 32 | 3 % → 6 % | 2.4 px | 0.36 | 1.93 | 5 |
| stroke 33 | 8 % → 13 % | 5.9 px | 0.35 | 1.65 | 3 |
| stroke 34 | 3 % → 6 % | 2.6 px | 0.35 | 1.71 | 4 |
| stroke 35 | 7 % → 15 % | 5.4 px | 0.35 | 2.11 | 3 |
| stroke 36 | 5 % → 5 % | 4.0 px | 0.35 | 1.01 | 5 |
| stroke 37 | 8 % → 16 % | 5.9 px | 0.35 | 2.07 | 3 |
| stroke 38 | 8 % → 14 % | 6.2 px | 0.35 | 1.71 | 5 |
| stroke 39 | 7 % → 12 % | 5.4 px | 0.35 | 1.65 | 3 |
| stroke 40 | 9 % → 20 % | 6.7 px | 0.36 | 2.23 | 4 |
| stroke 41 | 10 % → 15 % | 7.7 px | 0.35 | 1.46 | 5 |
| stroke 42 | 11 % → 19 % | 8.5 px | 0.36 | 1.73 | 3 |
| stroke 43 | 5 % → 9 % | 4.1 px | 0.35 | 1.66 | 5 |
| stroke 44 | 11 % → 15 % | 8.5 px | 0.36 | 1.41 | 3 |
| stroke 45 | 14 % → 19 % | 10.5 px | 0.35 | 1.37 | 2 |
| stroke 46 | 5 % → 7 % | 4.0 px | 0.35 | 1.38 | 4 |
| stroke 47 | 11 % → 14 % | 8.7 px | 0.36 | 1.21 | 4 |
| stroke 48 | 13 % → 18 % | 10.0 px | 0.36 | 1.36 | 4 |
| stroke 49 | 6 % → 9 % | 4.3 px | 0.35 | 1.65 | 6 |
| stroke 50 | 7 % → 7 % | 5.6 px | 0.35 | 1.00 | 4 |
| stroke 51 | 10 % → 16 % | 7.4 px | 0.36 | 1.67 | 4 |
| stroke 52 | 14 % → 16 % | 10.5 px | 0.35 | 1.19 | 3 |
| stroke 53 | 12 % → 16 % | 9.0 px | 0.35 | 1.35 | 3 |
| stroke 54 | 11 % → 16 % | 8.5 px | 0.35 | 1.46 | 3 |
| stroke 55 | 12 % → 16 % | 9.0 px | 0.35 | 1.34 | 3 |
| stroke 56 | 12 % → 13 % | 9.0 px | 0.35 | 1.11 | 3 |
| stroke 57 | 11 % → 14 % | 8.2 px | 0.36 | 1.31 | 3 |
| stroke 58 | 11 % → 12 % | 8.6 px | 0.35 | 1.12 | 5 |
| stroke 59 | 13 % → 15 % | 9.8 px | 0.35 | 1.16 | 5 |
| stroke 60 | 17 % → 22 % | 13.1 px | 0.35 | 1.26 | 2 |
| stroke 61 | 21 % → 22 % | 15.6 px | 0.35 | 1.05 | 5 |
| stroke 62 | 10 % → 10 % | 7.5 px | 0.35 | 1.00 | 3 |
| stroke 63 | 12 % → 13 % | 9.5 px | 0.35 | 1.09 | 3 |
| stroke 64 | 16 % → 17 % | 12.4 px | 0.35 | 1.02 | 2 |
| stroke 65 | 17 % → 17 % | 12.7 px | 0.35 | 1.00 | 4 |
| stroke 66 | 15 % → 15 % | 11.9 px | 0.35 | 1.00 | 3 |
| stroke 67 | 13 % → 14 % | 9.9 px | 0.35 | 1.06 | 5 |
| stroke 68 | 5 % → 10 % | 4.1 px | 0.35 | 1.90 | 3 |
| stroke 69 | 6 % → 6 % | 4.3 px | 0.35 | 1.00 | 3 |
| stroke 70 | 11 % → 14 % | 8.5 px | 0.35 | 1.28 | 3 |
| stroke 71 | 10 % → 12 % | 7.7 px | 0.35 | 1.17 | 4 |
| stroke 72 | 6 % → 7 % | 4.5 px | 0.35 | 1.26 | 3 |
| stroke 73 | 14 % → 14 % | 10.4 px | 0.35 | 1.00 | 5 |
| stroke 74 | 16 % → 16 % | 12.3 px | 0.35 | 1.00 | 3 |
| stroke 75 | 17 % → 17 % | 13.1 px | 0.35 | 1.00 | 6 |
| stroke 76 | 15 % → 15 % | 11.7 px | 0.36 | 1.00 | 3 |
| stroke 77 | 8 % → 10 % | 6.0 px | 0.35 | 1.32 | 3 |
| stroke 78 | 10 % → 10 % | 7.5 px | 0.35 | 1.00 | 3 |
| stroke 79 | 8 % → 8 % | 6.2 px | 0.35 | 1.00 | 3 |
| stroke 80 | 12 % → 12 % | 9.1 px | 0.36 | 1.00 | 3 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #42 Oil pastel shaggy — own sheet
own sheet 600 × 600 · Pastel 1.00 · 18 px · 2.6 s

![Brush Artist · Refs · #42 Oil pastel shaggy — own sheet](Brush-Artist-Refs-42-Oil-pastel-shaggy-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 5 % → 27 % | 8.5 px | 0.27 | 5.25 | 10 |
| stroke 2 | 5 % → 24 % | 7.8 px | 0.29 | 5.02 | 6 |
| stroke 3 | 5 % → 29 % | 8.8 px | 0.28 | 5.49 | 12 |
| stroke 4 | 5 % → 11 % | 9.1 px | 0.26 | 1.99 | 12 |
| stroke 5 | 6 % → 11 % | 10.2 px | 0.26 | 1.77 | 7 |
| stroke 6 | 8 % → 36 % | 13.4 px | 0.28 | 4.52 | 7 |
| stroke 7 | 11 % → 30 % | 18.0 px | 0.28 | 2.79 | 9 |
| stroke 8 | 7 % → 37 % | 10.8 px | 0.28 | 5.63 | 11 |
| stroke 9 | 8 % → 21 % | 13.4 px | 0.28 | 2.61 | 7 |
| stroke 10 | 8 % → 18 % | 13.2 px | 0.29 | 2.30 | 11 |
| stroke 11 | 5 % → 26 % | 8.8 px | 0.28 | 4.89 | 11 |
| stroke 12 | 8 % → 19 % | 13.1 px | 0.28 | 2.33 | 7 |
| stroke 13 | 12 % → 23 % | 20.4 px | 0.28 | 1.91 | 11 |
| stroke 14 | 5 % → 22 % | 7.6 px | 0.28 | 4.76 | 8 |
| stroke 15 | 6 % → 24 % | 9.1 px | 0.28 | 4.28 | 12 |
| stroke 16 | 9 % → 21 % | 15.5 px | 0.29 | 2.21 | 9 |
| stroke 17 | 16 % → 37 % | 26.3 px | 0.28 | 2.36 | 9 |
| stroke 18 | 14 % → 25 % | 22.6 px | 0.28 | 1.82 | 10 |
| stroke 19 | 14 % → 30 % | 23.7 px | 0.28 | 2.08 | 7 |
| stroke 20 | 21 % → 39 % | 35.4 px | 0.28 | 1.81 | 11 |
| stroke 21 | 9 % → 16 % | 14.2 px | 0.28 | 1.88 | 9 |
| stroke 22 | 14 % → 17 % | 23.1 px | 0.27 | 1.19 | 7 |
| stroke 23 | 12 % → 17 % | 20.4 px | 0.29 | 1.37 | 12 |
| stroke 24 | 18 % → 26 % | 30.0 px | 0.29 | 1.43 | 8 |
| stroke 25 | 19 % → 34 % | 32.1 px | 0.28 | 1.75 | 7 |
| stroke 26 | 5 % → 13 % | 8.8 px | 0.28 | 2.45 | 9 |
| stroke 27 | 18 % → 26 % | 30.3 px | 0.29 | 1.41 | 11 |
| stroke 28 | 14 % → 23 % | 23.2 px | 0.29 | 1.66 | 9 |
| stroke 29 | 9 % → 26 % | 14.2 px | 0.29 | 3.08 | 7 |
| stroke 30 | 15 % → 36 % | 24.5 px | 0.28 | 2.44 | 11 |
| stroke 31 | 13 % → 17 % | 22.3 px | 0.29 | 1.24 | 9 |
| stroke 32 | 16 % → 29 % | 26.3 px | 0.29 | 1.82 | 7 |
| stroke 33 | 15 % → 16 % | 24.3 px | 0.28 | 1.09 | 7 |
| stroke 34 | 19 % → 27 % | 31.4 px | 0.28 | 1.44 | 10 |
| stroke 35 | 25 % → 35 % | 40.9 px | 0.28 | 1.39 | 11 |
| stroke 36 | 24 % → 33 % | 40.2 px | 0.28 | 1.34 | 8 |
| stroke 37 | 11 % → 12 % | 18.4 px | 0.28 | 1.04 | 12 |
| stroke 38 | 19 % → 24 % | 30.7 px | 0.29 | 1.31 | 12 |
| stroke 39 | 16 % → 22 % | 27.0 px | 0.27 | 1.35 | 10 |
| stroke 40 | 21 % → 29 % | 34.9 px | 0.28 | 1.37 | 7 |
| stroke 41 | 31 % → 34 % | 51.2 px | 0.28 | 1.12 | 9 |
| stroke 42 | 23 % → 29 % | 37.9 px | 0.28 | 1.28 | 12 |
| stroke 43 | 12 % → 12 % | 20.2 px | 0.28 | 1.00 | 9 |
| stroke 44 | 29 % → 36 % | 48.3 px | 0.28 | 1.24 | 7 |
| stroke 45 | 16 % → 16 % | 25.6 px | 0.27 | 1.00 | 12 |
| stroke 46 | 28 % → 33 % | 46.9 px | 0.28 | 1.15 | 9 |
| stroke 47 | 37 % → 41 % | 61.6 px | 0.28 | 1.09 | 7 |
| stroke 48 | 28 % → 35 % | 47.2 px | 0.28 | 1.26 | 12 |
| stroke 49 | 27 % → 30 % | 43.8 px | 0.29 | 1.11 | 10 |
| stroke 50 | 37 % → 40 % | 61.8 px | 0.28 | 1.07 | 11 |
| stroke 51 | 15 % → 15 % | 25.8 px | 0.28 | 1.00 | 12 |
| stroke 52 | 37 % → 37 % | 61.4 px | 0.28 | 1.01 | 12 |
| stroke 53 | 22 % → 26 % | 35.6 px | 0.29 | 1.20 | 11 |
| stroke 54 | 17 % → 19 % | 29.0 px | 0.29 | 1.10 | 8 |
| stroke 55 | 15 % → 15 % | 24.6 px | 0.29 | 1.00 | 7 |
| stroke 56 | 13 % → 14 % | 21.3 px | 0.27 | 1.08 | 7 |
| stroke 57 | 23 % → 23 % | 38.0 px | 0.29 | 1.00 | 9 |
| stroke 58 | 26 % → 28 % | 43.7 px | 0.28 | 1.06 | 11 |
| stroke 59 | 40 % → 40 % | 66.1 px | 0.28 | 1.00 | 10 |
| stroke 60 | 21 % → 21 % | 34.4 px | 0.29 | 1.00 | 7 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #43 Dragged black ink blocks — own sheet
own sheet 600 × 600 · Gouache 1.00 · 70 px · 6.2 s

![Brush Artist · Refs · #43 Dragged black ink blocks — own sheet](Brush-Artist-Refs-43-Dragged-black-ink-blocks-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 11 % → 4 % | 24.9 px | 0.46 | 0.40 | 328 |
| stroke 2 | 10 % → 8 % | 35.4 px | 0.46 | 0.82 | 392 |
| stroke 3 | 18 % → 14 % | 66.1 px | 0.46 | 0.77 | 402 |
| stroke 4 | 22 % → 11 % | 75.0 px | 0.43 | 0.53 | 437 |
| stroke 5 | 31 % → 13 % | 72.0 px | 0.43 | 0.43 | 411 |

## Brush Artist · Refs · #44 Blue looping ribbon — own sheet
own sheet 600 × 600 · Oil 1.00 · 80 px · 4.4 s

![Brush Artist · Refs · #44 Blue looping ribbon — own sheet](Brush-Artist-Refs-44-Blue-looping-ribbon-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 32 % → 32 % | 42.1 px | 0.78 | 1.00 | 2410 |

## Brush Artist · Refs · #45 Soft pastel pepper — own sheet
own sheet 600 × 600 · Pastel 1.00 · 40 px · 4.3 s

![Brush Artist · Refs · #45 Soft pastel pepper — own sheet](Brush-Artist-Refs-45-Soft-pastel-pepper-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 10 % → 38 % | 11.3 px | 0.50 | 3.71 | 311 |
| stroke 2 | 18 % → 33 % | 20.7 px | 0.50 | 1.88 | 276 |
| stroke 3 | 25 % → 36 % | 16.9 px | 0.50 | 1.46 | 285 |
| stroke 4 | 24 % → 34 % | 29.4 px | 0.50 | 1.45 | 290 |
| stroke 5 | 30 % → 30 % | 20.9 px | 0.49 | 1.00 | 244 |
| stroke 6 | 35 % → 44 % | 22.7 px | 0.50 | 1.24 | 299 |
| stroke 7 | 39 % → 43 % | 21.3 px | 0.50 | 1.11 | 421 |
| stroke 8 | 43 % → 43 % | 43.7 px | 0.50 | 1.00 | 372 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #46 Red-brown ink lips — own sheet
own sheet 600 × 600 · Watercolour 1.00 · 50 px · 7.2 s

![Brush Artist · Refs · #46 Red-brown ink lips — own sheet](Brush-Artist-Refs-46-Red-brown-ink-lips-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 13 % → 26 % | 54.5 px | 0.56 | 1.96 | 93 |
| stroke 2 | 17 % → 31 % | 72.4 px | 0.53 | 1.89 | 75 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #47 Pink knife slabs — own sheet
own sheet 600 × 600 · Impasto 1.00 · 90 px · 4.2 s

![Brush Artist · Refs · #47 Pink knife slabs — own sheet](Brush-Artist-Refs-47-Pink-knife-slabs-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 16 % → 32 % | 81.5 px | 0.10 | 1.97 | 283 |
| stroke 2 | 29 % → 42 % | 165.6 px | 0.11 | 1.45 | 272 |
| stroke 3 | 29 % → 43 % | 165.1 px | 0.13 | 1.47 | 322 |
| stroke 4 | 39 % → 38 % | 165.8 px | 0.14 | 0.97 | 327 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #48 Black bands with drips — own sheet
own sheet 600 × 600 · Gouache 1.00 · 70 px · 10.8 s

![Brush Artist · Refs · #48 Black bands with drips — own sheet](Brush-Artist-Refs-48-Black-bands-with-drips-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 28 % → 40 % | 72.6 px | 0.38 | 1.43 | 461 |
| stroke 2 | 43 % → 55 % | 137.3 px | 0.38 | 1.30 | 443 |
| stroke 3 | 45 % → 56 % | 141.4 px | 0.38 | 1.23 | 531 |
| stroke 4 | 48 % → 45 % | 139.2 px | 0.37 | 0.94 | 539 |

## Brush Artist · Refs · #49 Magenta letters round brush — own sheet
own sheet 600 × 600 · Ink 1.00 · 30 px · 8.7 s

![Brush Artist · Refs · #49 Magenta letters round brush — own sheet](Brush-Artist-Refs-49-Magenta-letters-round-brush-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 27 % → 46 % | 64.7 px | 0.52 | 1.68 | 32 |
| stroke 2 | 29 % → 41 % | 53.0 px | 0.53 | 1.40 | 29 |
| stroke 3 | 42 % → 68 % | 98.0 px | 0.52 | 1.62 | 32 |
| stroke 4 | 33 % → 52 % | 53.5 px | 0.52 | 1.56 | 111 |
| stroke 5 | 41 % → 66 % | 97.1 px | 0.52 | 1.62 | 71 |
| stroke 6 | 56 % → 72 % | 237.9 px | 0.52 | 1.28 | 16 |
| stroke 7 | 42 % → 58 % | 65.1 px | 0.52 | 1.36 | 114 |
| stroke 8 | 36 % → 61 % | 92.6 px | 0.53 | 1.71 | 67 |
| stroke 9 | 50 % → 62 % | 156.5 px | 0.52 | 1.24 | 26 |
| stroke 10 | 43 % → 73 % | 102.9 px | 0.52 | 1.68 | 74 |
| stroke 11 | 52 % → 72 % | 221.9 px | 0.52 | 1.39 | 17 |
| stroke 12 | 54 % → 70 % | 84.9 px | 0.52 | 1.28 | 105 |
| stroke 13 | 42 % → 53 % | 116.2 px | 0.53 | 1.27 | 34 |
| stroke 14 | 45 % → 68 % | 131.6 px | 0.53 | 1.52 | 30 |
| stroke 15 | 43 % → 63 % | 101.8 px | 0.52 | 1.47 | 74 |
| stroke 16 | 52 % → 61 % | 220.3 px | 0.52 | 1.19 | 18 |
| stroke 17 | 53 % → 64 % | 82.3 px | 0.52 | 1.19 | 124 |
| stroke 18 | 36 % → 43 % | 98.8 px | 0.53 | 1.20 | 31 |
| stroke 19 | 53 % → 52 % | 122.0 px | 0.52 | 0.99 | 27 |
| stroke 20 | 55 % → 55 % | 127.4 px | 0.52 | 1.00 | 34 |
| stroke 21 | 49 % → 49 % | 80.4 px | 0.52 | 1.00 | 81 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #50 Thick swipes on photo — own sheet
own sheet 600 × 600 · Impasto 1.00 · 40 px · 2.8 s

![Brush Artist · Refs · #50 Thick swipes on photo — own sheet](Brush-Artist-Refs-50-Thick-swipes-on-photo-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 9 % → 21 % | 43.0 px | 0.35 | 2.32 | 39 |
| stroke 2 | 9 % → 16 % | 42.2 px | 0.34 | 1.82 | 30 |
| stroke 3 | 10 % → 11 % | 42.0 px | 0.32 | 1.06 | 44 |
| stroke 4 | 11 % → 18 % | 44.0 px | 0.35 | 1.60 | 36 |
| stroke 5 | 11 % → 10 % | 42.2 px | 0.34 | 0.94 | 36 |
| stroke 6 | 17 % → 21 % | 99.5 px | 0.35 | 1.19 | 30 |
| stroke 7 | 22 % → 26 % | 92.9 px | 0.35 | 1.18 | 43 |
| stroke 8 | 21 % → 20 % | 119.7 px | 0.35 | 0.96 | 40 |
| stroke 9 | 10 % → 11 % | 43.0 px | 0.30 | 1.11 | 42 |
| stroke 10 | 22 % → 22 % | 75.4 px | 0.35 | 0.96 | 43 |
| stroke 11 | 8 % → 8 % | 41.8 px | 0.36 | 0.95 | 34 |
| stroke 12 | 17 % → 16 % | 94.4 px | 0.35 | 0.96 | 23 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Ink — dry brush — own sheet
own sheet 600 × 600 · Gouache 1.00 · 30 px · 2.8 s

![Brush Artist · Ink — dry brush — own sheet](Brush-Artist-Ink-dry-brush-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| ear | 8 % → 2 % | 9.7 px | 0.85 | 0.22 | 456 |
| drag0 | 4 % → 6 % | 7.6 px | 0.85 | 1.51 | 114 |
| drag1 | 7 % → 7 % | 15.1 px | 0.85 | 0.89 | 99 |
| drag2 | 10 % → 7 % | 22.1 px | 0.85 | 0.71 | 87 |
| drag3 | 12 % → 7 % | 30.1 px | 0.85 | 0.60 | 83 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Watercolour — blue — own sheet
own sheet 600 × 600 · Watercolour 0.93 · Ink 0.07 · 40 px · 9.7 s

![Brush Artist · Watercolour — blue — own sheet](Brush-Artist-Watercolour-blue-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| s0 | 7 % → 24 % | 28.8 px | 0.30 | 3.32 | 40 |
| s1 | 6 % → 33 % | 10.1 px | 0.37 | 6.00 | 40 |
| s2 | 10 % → 19 % | 44.2 px | 0.26 | 1.81 | 36 |
| s3 | 10 % → 18 % | 26.7 px | 0.31 | 1.92 | 50 |
| s4 | 14 % → 30 % | 38.6 px | 0.36 | 2.16 | 60 |
| s5 | 19 % → 29 % | 39.3 px | 0.37 | 1.54 | 48 |
| s6 | 18 % → 22 % | 48.7 px | 0.31 | 1.25 | 55 |
| s7 | 25 % → 36 % | 32.7 px | 0.37 | 1.46 | 38 |
| s8 | 21 % → 25 % | 79.8 px | 0.30 | 1.20 | 46 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Charcoal — stick — own sheet
own sheet 600 × 600 · Charcoal 0.78 · Pastel 0.22 · 28 px · 1.2 s

![Brush Artist · Charcoal — stick — own sheet](Brush-Artist-Charcoal-stick-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| finger0 | 12 % → 25 % | 21.2 px | 0.83 | 2.03 | 37 |
| tip0 | 13 % → 21 % | 33.8 px | 0.83 | 1.70 | 11 |
| finger1 | 23 % → 41 % | 40.4 px | 0.83 | 1.77 | 34 |
| tip1 | 21 % → 29 % | 57.3 px | 0.83 | 1.38 | 12 |
| finger2 | 25 % → 37 % | 43.8 px | 0.83 | 1.49 | 34 |
| tip2 | 21 % → 29 % | 55.7 px | 0.83 | 1.40 | 8 |
| finger3 | 24 % → 27 % | 42.7 px | 0.83 | 1.14 | 33 |
| tip3 | 20 % → 20 % | 54.1 px | 0.83 | 1.00 | 7 |
| cig0 | 34 % → 47 % | 75.0 px | 0.83 | 1.39 | 14 |
| cig1 | 36 % → 47 % | 80.5 px | 0.83 | 1.30 | 15 |
| cig2 | 39 % → 47 % | 86.7 px | 0.83 | 1.20 | 17 |
| cig3 | 41 % → 47 % | 91.3 px | 0.83 | 1.14 | 18 |
| cig4 | 44 % → 46 % | 97.5 px | 0.83 | 1.06 | 17 |
| cig5 | 46 % → 46 % | 102.9 px | 0.83 | 1.00 | 20 |

Numbers say: wet paint spreads well beyond the stroke.

## Oil · Henry Ward · HW #02 cream over wet olive — own sheet
own sheet 600 × 600 · Oil 0.81 · Ink 0.19 · 96 px · 39.2 s

![Oil · Henry Ward · HW #02 cream over wet olive — own sheet](Oil-Henry-Ward-HW-02-cream-over-wet-olive-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 44 % → 51 % | 86.6 px | 0.44 | 1.16 | 1302 |
| stroke 2 | 57 % → 56 % | 148.4 px | 0.41 | 0.98 | 1829 |
| stroke 3 | 64 % → 56 % | 201.8 px | 0.44 | 0.87 | 2030 |
| stroke 4 | 68 % → 58 % | 238.9 px | 0.45 | 0.84 | 2146 |
| stroke 5 | 68 % → 63 % | 238.8 px | 0.45 | 0.94 | 1917 |
| stroke 6 | 68 % → 53 % | 239.6 px | 0.45 | 0.77 | 1860 |
| stroke 7 | 76 % → 42 % | 239.7 px | 0.47 | 0.56 | 2672 |
| stroke 8 | 96 % → 36 % | 239.0 px | 0.50 | 0.37 | 2739 |
| stroke 9 | 100 % → 33 % | 193.2 px | 0.47 | 0.33 | 1691 |
| stroke 10 | 9 % → 55 % | 65.5 px | 0.44 | 6.15 | 463 |
| stroke 11 | 16 % → 62 % | 106.7 px | 0.45 | 3.85 | 517 |
| stroke 12 | 14 % → 46 % | 133.1 px | 0.46 | 3.16 | 196 |
| stroke 13 | 36 % → 56 % | 156.6 px | 0.42 | 1.57 | 528 |
| stroke 14 | 36 % → 57 % | 212.0 px | 0.43 | 1.56 | 489 |
| stroke 15 | 37 % → 55 % | 249.4 px | 0.44 | 1.50 | 440 |
| stroke 16 | 39 % → 54 % | 201.8 px | 0.45 | 1.37 | 821 |
| stroke 17 | 44 % → 62 % | 293.3 px | 0.45 | 1.40 | 540 |
| stroke 18 | 48 % → 62 % | 338.8 px | 0.45 | 1.29 | 573 |
| stroke 19 | 46 % → 57 % | 398.0 px | 0.45 | 1.23 | 450 |
| stroke 20 | 40 % → 47 % | 328.8 px | 0.45 | 1.17 | 342 |
| stroke 21 | 45 % → 43 % | 224.0 px | 0.46 | 0.98 | 810 |
| stroke 22 | 59 % → 57 % | 510.1 px | 0.44 | 0.97 | 371 |
| stroke 23 | 56 % → 54 % | 380.4 px | 0.45 | 0.97 | 539 |
| stroke 24 | 63 % → 62 % | 415.3 px | 0.45 | 0.98 | 453 |
| stroke 25 | 67 % → 66 % | 592.8 px | 0.44 | 0.99 | 285 |
| stroke 26 | 47 % → 46 % | 378.8 px | 0.46 | 0.97 | 555 |

Numbers say: wet paint spreads well beyond the stroke.

## Oil · Henry Ward · HW #04 grey arcs over ochre — own sheet
own sheet 600 × 600 · Gouache 1.00 · 84 px · 43.2 s

![Oil · Henry Ward · HW #04 grey arcs over ochre — own sheet](Oil-Henry-Ward-HW-04-grey-arcs-over-ochre-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 47 % → 58 % | 78.5 px | 0.21 | 1.24 | 1209 |
| stroke 2 | 63 % → 67 % | 148.9 px | 0.22 | 1.07 | 1721 |
| stroke 3 | 70 % → 60 % | 209.2 px | 0.22 | 0.86 | 1893 |
| stroke 4 | 71 % → 64 % | 217.5 px | 0.21 | 0.90 | 2065 |
| stroke 5 | 70 % → 60 % | 217.6 px | 0.20 | 0.85 | 1865 |
| stroke 6 | 71 % → 46 % | 217.1 px | 0.20 | 0.65 | 1797 |
| stroke 7 | 75 % → 33 % | 218.1 px | 0.17 | 0.44 | 2428 |
| stroke 8 | 94 % → 33 % | 217.1 px | 0.16 | 0.35 | 2633 |
| stroke 9 | 100 % → 29 % | 167.6 px | 0.16 | 0.29 | 1751 |
| stroke 10 | 12 % → 64 % | 71.2 px | 0.21 | 5.26 | 444 |
| stroke 11 | 18 % → 56 % | 95.1 px | 0.21 | 3.06 | 688 |
| stroke 12 | 24 % → 59 % | 152.2 px | 0.21 | 2.49 | 354 |
| stroke 13 | 32 % → 62 % | 200.4 px | 0.21 | 1.90 | 628 |
| stroke 14 | 31 % → 65 % | 262.0 px | 0.21 | 2.06 | 446 |
| stroke 15 | 37 % → 60 % | 284.5 px | 0.22 | 1.62 | 444 |
| stroke 16 | 32 % → 57 % | 155.4 px | 0.21 | 1.79 | 994 |
| stroke 17 | 51 % → 61 % | 219.0 px | 0.22 | 1.20 | 723 |
| stroke 18 | 45 % → 57 % | 209.7 px | 0.21 | 1.29 | 1163 |
| stroke 19 | 54 % → 59 % | 244.5 px | 0.22 | 1.11 | 845 |
| stroke 20 | 47 % → 60 % | 359.4 px | 0.21 | 1.29 | 512 |
| stroke 21 | 46 % → 60 % | 298.1 px | 0.21 | 1.32 | 623 |
| stroke 22 | 49 % → 64 % | 331.8 px | 0.21 | 1.31 | 439 |
| stroke 23 | 51 % → 59 % | 251.9 px | 0.21 | 1.14 | 1042 |
| stroke 24 | 51 % → 58 % | 260.7 px | 0.21 | 1.15 | 720 |
| stroke 25 | 53 % → 57 % | 313.3 px | 0.21 | 1.07 | 775 |
| stroke 26 | 50 % → 57 % | 259.8 px | 0.21 | 1.15 | 813 |
| stroke 27 | 35 % → 47 % | 199.0 px | 0.19 | 1.32 | 290 |
| stroke 28 | 33 % → 40 % | 222.7 px | 0.18 | 1.21 | 309 |
| stroke 29 | 32 % → 35 % | 196.0 px | 0.18 | 1.08 | 495 |
| stroke 30 | 40 % → 34 % | 188.2 px | 0.16 | 0.83 | 300 |

Numbers say: wet paint spreads well beyond the stroke.

## Oil · Henry Ward · HW #09 white arches over wet blue-grey — own sheet
own sheet 600 × 600 · Gouache 1.00 · 84 px · 46.3 s

![Oil · Henry Ward · HW #09 white arches over wet blue-grey — own sheet](Oil-Henry-Ward-HW-09-white-arches-over-wet-blue-grey-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 47 % → 22 % | 80.6 px | 0.08 | 0.46 | 1218 |
| stroke 2 | 61 % → 34 % | 143.6 px | 0.07 | 0.55 | 1753 |
| stroke 3 | 70 % → 42 % | 206.3 px | 0.07 | 0.60 | 1900 |
| stroke 4 | 71 % → 54 % | 217.0 px | 0.07 | 0.76 | 2046 |
| stroke 5 | 71 % → 66 % | 218.3 px | 0.06 | 0.93 | 1858 |
| stroke 6 | 71 % → 67 % | 217.3 px | 0.07 | 0.94 | 1828 |
| stroke 7 | 75 % → 62 % | 217.9 px | 0.08 | 0.83 | 2711 |
| stroke 8 | 93 % → 60 % | 217.3 px | 0.09 | 0.64 | 2707 |
| stroke 9 | 100 % → 55 % | 167.6 px | 0.10 | 0.55 | 1662 |
| stroke 10 | 9 % → 50 % | 25.6 px | 0.08 | 5.41 | 1077 |
| stroke 11 | 15 % → 57 % | 36.0 px | 0.08 | 3.73 | 988 |
| stroke 12 | 17 % → 60 % | 51.0 px | 0.08 | 3.58 | 805 |
| stroke 13 | 19 % → 64 % | 63.8 px | 0.08 | 3.37 | 480 |
| stroke 14 | 22 % → 62 % | 32.3 px | 0.08 | 2.79 | 864 |
| stroke 15 | 30 % → 59 % | 133.2 px | 0.08 | 1.98 | 1033 |
| stroke 16 | 40 % → 69 % | 205.3 px | 0.08 | 1.75 | 1189 |
| stroke 17 | 39 % → 54 % | 143.4 px | 0.06 | 1.39 | 998 |
| stroke 18 | 47 % → 59 % | 187.5 px | 0.08 | 1.24 | 1186 |
| stroke 19 | 53 % → 60 % | 217.3 px | 0.07 | 1.14 | 892 |
| stroke 20 | 53 % → 63 % | 218.1 px | 0.08 | 1.19 | 1238 |
| stroke 21 | 54 % → 58 % | 201.3 px | 0.09 | 1.06 | 1538 |
| stroke 22 | 64 % → 70 % | 375.6 px | 0.08 | 1.10 | 777 |
| stroke 23 | 61 % → 63 % | 285.6 px | 0.08 | 1.03 | 883 |
| stroke 24 | 63 % → 66 % | 342.1 px | 0.07 | 1.04 | 662 |
| stroke 25 | 72 % → 74 % | 503.2 px | 0.08 | 1.03 | 349 |
| stroke 26 | 61 % → 62 % | 302.9 px | 0.08 | 1.02 | 628 |
| stroke 27 | 61 % → 63 % | 400.6 px | 0.09 | 1.03 | 312 |
| stroke 28 | 64 % → 59 % | 251.6 px | 0.09 | 0.92 | 544 |

Numbers say: wet paint spreads well beyond the stroke.

## Oil · Henry Ward · HW #03 navy contours over wet band — own sheet
own sheet 600 × 600 · Gouache 1.00 · 84 px · 29.4 s

![Oil · Henry Ward · HW #03 navy contours over wet band — own sheet](Oil-Henry-Ward-HW-03-navy-contours-over-wet-band-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 50 % → 31 % | 87.6 px | 0.66 | 0.62 | 1273 |
| stroke 2 | 61 % → 37 % | 145.5 px | 0.59 | 0.61 | 1685 |
| stroke 3 | 69 % → 39 % | 202.2 px | 0.56 | 0.57 | 1917 |
| stroke 4 | 71 % → 43 % | 218.6 px | 0.54 | 0.61 | 2017 |
| stroke 5 | 71 % → 43 % | 217.2 px | 0.54 | 0.61 | 1842 |
| stroke 6 | 71 % → 34 % | 222.3 px | 0.51 | 0.48 | 1766 |
| stroke 7 | 74 % → 24 % | 218.1 px | 0.53 | 0.33 | 2517 |
| stroke 8 | 95 % → 17 % | 218.2 px | 0.61 | 0.18 | 2544 |
| stroke 9 | 100 % → 10 % | 170.3 px | 0.70 | 0.10 | 1802 |
| stroke 10 | 7 % → 41 % | 49.7 px | 0.55 | 5.70 | 356 |
| stroke 11 | 14 % → 45 % | 128.0 px | 0.55 | 3.33 | 196 |
| stroke 12 | 22 % → 46 % | 211.0 px | 0.53 | 2.08 | 206 |
| stroke 13 | 23 % → 35 % | 198.0 px | 0.52 | 1.53 | 271 |
| stroke 14 | 21 % → 44 % | 182.5 px | 0.62 | 2.06 | 145 |
| stroke 15 | 32 % → 43 % | 259.2 px | 0.58 | 1.36 | 203 |
| stroke 16 | 33 % → 34 % | 98.7 px | 0.55 | 1.03 | 738 |
| stroke 17 | 36 % → 35 % | 129.5 px | 0.56 | 0.96 | 452 |

Numbers say: wet paint spreads well beyond the stroke.

## Oil · Henry Ward · HW #01 peach cloud and legs over teal — own sheet
own sheet 600 × 600 · Gouache 1.00 · 84 px · 37.1 s

![Oil · Henry Ward · HW #01 peach cloud and legs over teal — own sheet](Oil-Henry-Ward-HW-01-peach-cloud-and-legs-over-teal-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 50 % → 52 % | 88.3 px | 0.42 | 1.04 | 1325 |
| stroke 2 | 62 % → 59 % | 146.6 px | 0.43 | 0.96 | 1685 |
| stroke 3 | 69 % → 61 % | 202.8 px | 0.43 | 0.89 | 1912 |
| stroke 4 | 71 % → 69 % | 219.6 px | 0.44 | 0.97 | 2014 |
| stroke 5 | 70 % → 60 % | 217.6 px | 0.43 | 0.85 | 1934 |
| stroke 6 | 71 % → 52 % | 218.3 px | 0.41 | 0.74 | 1819 |
| stroke 7 | 76 % → 44 % | 221.6 px | 0.37 | 0.57 | 2714 |
| stroke 8 | 95 % → 36 % | 217.7 px | 0.33 | 0.38 | 2662 |
| stroke 9 | 100 % → 28 % | 170.3 px | 0.24 | 0.28 | 1592 |
| stroke 10 | 18 % → 58 % | 67.2 px | 0.43 | 3.29 | 536 |
| stroke 11 | 26 % → 60 % | 117.4 px | 0.43 | 2.28 | 437 |
| stroke 12 | 32 % → 64 % | 164.9 px | 0.43 | 2.01 | 347 |
| stroke 13 | 39 % → 69 % | 198.6 px | 0.43 | 1.77 | 546 |
| stroke 14 | 56 % → 58 % | 211.3 px | 0.43 | 1.04 | 555 |
| stroke 15 | 44 % → 62 % | 217.7 px | 0.43 | 1.40 | 343 |
| stroke 16 | 41 % → 68 % | 215.0 px | 0.44 | 1.68 | 732 |
| stroke 17 | 36 % → 53 % | 195.1 px | 0.39 | 1.49 | 372 |
| stroke 18 | 42 % → 57 % | 356.2 px | 0.39 | 1.35 | 476 |
| stroke 19 | 54 % → 72 % | 444.3 px | 0.39 | 1.33 | 738 |
| stroke 20 | 53 % → 71 % | 410.3 px | 0.40 | 1.34 | 433 |
| stroke 21 | 49 % → 60 % | 401.9 px | 0.40 | 1.23 | 600 |
| stroke 22 | 47 % → 53 % | 328.3 px | 0.41 | 1.11 | 343 |
| stroke 23 | 39 % → 43 % | 138.2 px | 0.33 | 1.10 | 181 |
| stroke 24 | 42 % → 40 % | 154.9 px | 0.32 | 0.96 | 214 |

Numbers say: wet paint spreads well beyond the stroke.

## Oil · Henry Ward · HW #05 rust, pink, green-black — own sheet
own sheet 600 × 600 · Gouache 1.00 · 84 px · 38.3 s

![Oil · Henry Ward · HW #05 rust, pink, green-black — own sheet](Oil-Henry-Ward-HW-05-rust-pink-green-black-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 49 % → 55 % | 83.9 px | 0.57 | 1.13 | 1287 |
| stroke 2 | 63 % → 61 % | 148.1 px | 0.48 | 0.98 | 1748 |
| stroke 3 | 69 % → 61 % | 207.3 px | 0.40 | 0.89 | 1910 |
| stroke 4 | 71 % → 68 % | 218.5 px | 0.36 | 0.96 | 2011 |
| stroke 5 | 71 % → 65 % | 220.6 px | 0.37 | 0.92 | 1916 |
| stroke 6 | 70 % → 65 % | 216.1 px | 0.40 | 0.92 | 2037 |
| stroke 7 | 74 % → 57 % | 217.8 px | 0.47 | 0.77 | 2553 |
| stroke 8 | 93 % → 55 % | 217.2 px | 0.58 | 0.59 | 2551 |
| stroke 9 | 100 % → 51 % | 167.6 px | 0.73 | 0.51 | 1558 |
| stroke 10 | 16 % → 58 % | 57.3 px | 0.55 | 3.62 | 406 |
| stroke 11 | 26 % → 64 % | 111.1 px | 0.44 | 2.40 | 466 |
| stroke 12 | 30 % → 63 % | 155.7 px | 0.40 | 2.12 | 353 |
| stroke 13 | 36 % → 65 % | 190.5 px | 0.37 | 1.83 | 452 |
| stroke 14 | 51 % → 61 % | 229.7 px | 0.49 | 1.19 | 236 |
| stroke 15 | 44 % → 64 % | 221.1 px | 0.42 | 1.46 | 297 |
| stroke 16 | 38 % → 66 % | 256.1 px | 0.37 | 1.73 | 225 |
| stroke 17 | 41 % → 68 % | 209.6 px | 0.36 | 1.65 | 594 |
| stroke 18 | 42 % → 67 % | 229.5 px | 0.38 | 1.59 | 623 |
| stroke 19 | 34 % → 64 % | 172.9 px | 0.41 | 1.87 | 649 |
| stroke 20 | 44 % → 66 % | 328.9 px | 0.41 | 1.48 | 223 |
| stroke 21 | 47 % → 66 % | 344.5 px | 0.43 | 1.40 | 301 |
| stroke 22 | 48 % → 68 % | 400.6 px | 0.43 | 1.41 | 497 |
| stroke 23 | 43 % → 59 % | 248.5 px | 0.42 | 1.38 | 712 |
| stroke 24 | 44 % → 53 % | 209.7 px | 0.55 | 1.21 | 371 |
| stroke 25 | 56 % → 54 % | 199.1 px | 0.66 | 0.96 | 503 |

Numbers say: wet paint spreads well beyond the stroke.

## Oil · Henry Ward · HW #07 blue L and zigzag on lilac — own sheet
own sheet 600 × 600 · Gouache 1.00 · 90 px · 39.7 s

![Oil · Henry Ward · HW #07 blue L and zigzag on lilac — own sheet](Oil-Henry-Ward-HW-07-blue-L-and-zigzag-on-lilac-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 45 % → 28 % | 81.5 px | 0.19 | 0.62 | 1197 |
| stroke 2 | 58 % → 37 % | 140.2 px | 0.27 | 0.65 | 1687 |
| stroke 3 | 67 % → 67 % | 204.8 px | 0.27 | 1.00 | 1898 |
| stroke 4 | 70 % → 49 % | 231.4 px | 0.25 | 0.70 | 1948 |
| stroke 5 | 69 % → 59 % | 227.8 px | 0.25 | 0.86 | 1948 |
| stroke 6 | 69 % → 61 % | 227.4 px | 0.23 | 0.89 | 2569 |
| stroke 7 | 75 % → 57 % | 228.1 px | 0.19 | 0.76 | 2273 |
| stroke 8 | 96 % → 54 % | 229.2 px | 0.14 | 0.56 | 2420 |
| stroke 9 | 100 % → 57 % | 182.6 px | 0.12 | 0.57 | 1550 |
| stroke 10 | 12 % → 32 % | 34.3 px | 0.21 | 2.58 | 434 |
| stroke 11 | 22 % → 39 % | 74.6 px | 0.29 | 1.77 | 631 |
| stroke 12 | 21 % → 40 % | 76.0 px | 0.29 | 1.90 | 350 |
| stroke 13 | 23 % → 44 % | 88.7 px | 0.27 | 1.95 | 420 |
| stroke 14 | 28 % → 48 % | 128.5 px | 0.26 | 1.67 | 686 |
| stroke 15 | 31 % → 54 % | 152.5 px | 0.24 | 1.75 | 388 |
| stroke 16 | 36 % → 60 % | 162.3 px | 0.24 | 1.64 | 859 |
| stroke 17 | 34 % → 62 % | 170.3 px | 0.23 | 1.82 | 760 |
| stroke 18 | 43 % → 62 % | 190.3 px | 0.21 | 1.42 | 640 |
| stroke 19 | 47 % → 57 % | 190.9 px | 0.19 | 1.22 | 495 |
| stroke 20 | 53 % → 58 % | 204.1 px | 0.16 | 1.09 | 672 |
| stroke 21 | 63 % → 54 % | 205.5 px | 0.14 | 0.86 | 611 |
| stroke 22 | 71 % → 54 % | 221.9 px | 0.13 | 0.76 | 811 |
| stroke 23 | 61 % → 52 % | 335.0 px | 0.21 | 0.87 | 420 |
| stroke 24 | 73 % → 58 % | 483.9 px | 0.16 | 0.79 | 198 |
| stroke 25 | 65 % → 52 % | 242.0 px | 0.24 | 0.80 | 707 |
| stroke 26 | 64 % → 58 % | 692.7 px | 0.22 | 0.91 | 224 |
| stroke 27 | 72 % → 62 % | 690.3 px | 0.21 | 0.86 | 293 |
| stroke 28 | 72 % → 61 % | 546.7 px | 0.21 | 0.85 | 335 |
| stroke 29 | 72 % → 62 % | 635.8 px | 0.21 | 0.85 | 210 |
| stroke 30 | 77 % → 65 % | 597.5 px | 0.21 | 0.84 | 292 |
| stroke 31 | 77 % → 65 % | 1144.6 px | 0.20 | 0.83 | 100 |

Numbers say: wet paint spreads well beyond the stroke.

## Oil · Henry Ward · HW #08 crown and dark oval — own sheet
own sheet 600 × 600 · Gouache 1.00 · 84 px · 29.7 s

![Oil · Henry Ward · HW #08 crown and dark oval — own sheet](Oil-Henry-Ward-HW-08-crown-and-dark-oval-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 50 % → 0 % | 88.6 px | 0.00 | 0.00 | 1269 |
| stroke 2 | 61 % → 0 % | 142.3 px | 0.00 | 0.00 | 1665 |
| stroke 3 | 70 % → 3 % | 206.3 px | 0.11 | 0.04 | 1841 |
| stroke 4 | 72 % → 5 % | 223.5 px | 0.10 | 0.07 | 2991 |
| stroke 5 | 71 % → 9 % | 220.1 px | 0.09 | 0.12 | 2594 |
| stroke 6 | 71 % → 9 % | 219.6 px | 0.09 | 0.13 | 1970 |
| stroke 7 | 74 % → 9 % | 217.9 px | 0.09 | 0.13 | 2057 |
| stroke 8 | 94 % → 8 % | 217.5 px | 0.08 | 0.08 | 2179 |
| stroke 9 | 100 % → 5 % | 166.8 px | 0.06 | 0.05 | 1671 |
| stroke 10 | 17 % → 0 % | 69.7 px | 0.00 | 0.00 | 623 |
| stroke 11 | 26 % → 1 % | 134.9 px | 0.06 | 0.05 | 435 |
| stroke 12 | 32 % → 3 % | 201.5 px | 0.11 | 0.10 | 471 |
| stroke 13 | 22 % → 6 % | 66.1 px | 0.09 | 0.28 | 610 |
| stroke 14 | 32 % → 9 % | 236.3 px | 0.09 | 0.27 | 404 |
| stroke 15 | 32 % → 9 % | 266.7 px | 0.09 | 0.27 | 397 |
| stroke 16 | 33 % → 9 % | 267.9 px | 0.09 | 0.26 | 479 |
| stroke 17 | 39 % → 10 % | 247.3 px | 0.09 | 0.25 | 377 |
| stroke 18 | 7 % → 9 % | 64.2 px | 0.09 | 1.26 | 366 |
| stroke 19 | 13 % → 9 % | 110.7 px | 0.09 | 0.69 | 335 |
| stroke 20 | 19 % → 9 % | 144.0 px | 0.09 | 0.49 | 382 |

## Oil · Henry Ward · HW #10 green block over maroon — own sheet
own sheet 600 × 600 · Gouache 1.00 · 84 px · 35.2 s

![Oil · Henry Ward · HW #10 green block over maroon — own sheet](Oil-Henry-Ward-HW-10-green-block-over-maroon-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 50 % → 40 % | 86.8 px | 0.28 | 0.80 | 1249 |
| stroke 2 | 61 % → 44 % | 141.5 px | 0.37 | 0.72 | 1711 |
| stroke 3 | 70 % → 47 % | 209.1 px | 0.47 | 0.67 | 2608 |
| stroke 4 | 71 % → 51 % | 218.3 px | 0.54 | 0.72 | 2710 |
| stroke 5 | 70 % → 52 % | 215.8 px | 0.61 | 0.74 | 2256 |
| stroke 6 | 71 % → 46 % | 218.9 px | 0.64 | 0.65 | 1983 |
| stroke 7 | 75 % → 38 % | 219.1 px | 0.66 | 0.50 | 1979 |
| stroke 8 | 94 % → 33 % | 217.8 px | 0.63 | 0.35 | 2495 |
| stroke 9 | 100 % → 25 % | 172.0 px | 0.55 | 0.25 | 2064 |
| stroke 10 | 13 % → 44 % | 72.7 px | 0.31 | 3.50 | 196 |
| stroke 11 | 20 % → 45 % | 130.0 px | 0.40 | 2.29 | 214 |
| stroke 12 | 23 % → 50 % | 196.9 px | 0.50 | 2.20 | 274 |
| stroke 13 | 36 % → 47 % | 239.3 px | 0.38 | 1.29 | 423 |
| stroke 14 | 33 % → 49 % | 265.0 px | 0.44 | 1.51 | 586 |
| stroke 15 | 28 % → 50 % | 254.2 px | 0.48 | 1.79 | 370 |
| stroke 16 | 27 % → 50 % | 190.9 px | 0.52 | 1.86 | 821 |
| stroke 17 | 29 % → 52 % | 196.6 px | 0.58 | 1.77 | 470 |
| stroke 18 | 31 % → 51 % | 216.7 px | 0.62 | 1.62 | 482 |
| stroke 19 | 32 % → 46 % | 229.9 px | 0.65 | 1.44 | 262 |
| stroke 20 | 32 % → 43 % | 228.5 px | 0.65 | 1.33 | 348 |
| stroke 21 | 38 % → 42 % | 139.1 px | 0.54 | 1.10 | 677 |
| stroke 22 | 35 % → 39 % | 285.3 px | 0.66 | 1.10 | 299 |
| stroke 23 | 36 % → 36 % | 220.7 px | 0.64 | 1.02 | 353 |
| stroke 24 | 35 % → 31 % | 194.5 px | 0.61 | 0.87 | 263 |

Numbers say: wet paint spreads well beyond the stroke.

## Oil · Henry Ward · HW #11 cream mass and purple balls — own sheet
own sheet 600 × 600 · Gouache 1.00 · 84 px · 37.1 s

![Oil · Henry Ward · HW #11 cream mass and purple balls — own sheet](Oil-Henry-Ward-HW-11-cream-mass-and-purple-balls-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 49 % → 48 % | 82.9 px | 0.05 | 0.98 | 1162 |
| stroke 2 | 62 % → 51 % | 147.4 px | 0.06 | 0.81 | 1710 |
| stroke 3 | 70 % → 52 % | 209.8 px | 0.05 | 0.75 | 2806 |
| stroke 4 | 71 % → 57 % | 220.5 px | 0.06 | 0.80 | 2758 |
| stroke 5 | 70 % → 56 % | 216.9 px | 0.18 | 0.79 | 2058 |
| stroke 6 | 70 % → 56 % | 216.6 px | 0.33 | 0.80 | 2197 |
| stroke 7 | 76 % → 46 % | 221.0 px | 0.41 | 0.61 | 1929 |
| stroke 8 | 94 % → 43 % | 217.9 px | 0.53 | 0.46 | 2475 |
| stroke 9 | 100 % → 42 % | 171.2 px | 0.72 | 0.42 | 2141 |
| stroke 10 | 14 % → 50 % | 59.6 px | 0.06 | 3.56 | 336 |
| stroke 11 | 20 % → 51 % | 107.1 px | 0.05 | 2.52 | 436 |
| stroke 12 | 26 % → 52 % | 147.2 px | 0.05 | 1.99 | 497 |
| stroke 13 | 31 % → 56 % | 197.2 px | 0.05 | 1.77 | 383 |
| stroke 14 | 34 % → 56 % | 229.7 px | 0.08 | 1.63 | 538 |
| stroke 15 | 35 % → 56 % | 212.7 px | 0.15 | 1.59 | 554 |
| stroke 16 | 34 % → 56 % | 230.6 px | 0.27 | 1.64 | 536 |
| stroke 17 | 33 % → 55 % | 208.0 px | 0.32 | 1.69 | 375 |
| stroke 18 | 51 % → 50 % | 260.2 px | 0.06 | 0.99 | 382 |
| stroke 19 | 51 % → 51 % | 303.8 px | 0.05 | 1.00 | 346 |
| stroke 20 | 52 % → 53 % | 367.4 px | 0.05 | 1.00 | 473 |
| stroke 21 | 57 % → 57 % | 443.3 px | 0.06 | 1.01 | 400 |
| stroke 22 | 52 % → 56 % | 362.3 px | 0.11 | 1.07 | 362 |
| stroke 23 | 42 % → 57 % | 277.2 px | 0.24 | 1.35 | 380 |
| stroke 24 | 37 % → 56 % | 261.1 px | 0.30 | 1.52 | 406 |
| stroke 25 | 44 % → 55 % | 123.5 px | 0.40 | 1.27 | 672 |
| stroke 26 | 58 % → 63 % | 172.5 px | 0.40 | 1.08 | 564 |
| stroke 27 | 56 % → 55 % | 145.4 px | 0.38 | 0.97 | 512 |

Numbers say: wet paint spreads well beyond the stroke.

## Oil · Henry Ward · HW #13 blue scrub under red — own sheet
own sheet 600 × 600 · Gouache 1.00 · 84 px · 27.9 s

![Oil · Henry Ward · HW #13 blue scrub under red — own sheet](Oil-Henry-Ward-HW-13-blue-scrub-under-red-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 49 % → 13 % | 83.9 px | 0.07 | 0.27 | 1644 |
| stroke 2 | 61 % → 29 % | 142.6 px | 0.08 | 0.47 | 2486 |
| stroke 3 | 69 % → 38 % | 204.0 px | 0.08 | 0.54 | 2077 |
| stroke 4 | 71 % → 49 % | 220.1 px | 0.08 | 0.69 | 2225 |
| stroke 5 | 70 % → 65 % | 216.7 px | 0.07 | 0.93 | 1916 |
| stroke 6 | 71 % → 73 % | 220.4 px | 0.07 | 1.02 | 1681 |
| stroke 7 | 75 % → 72 % | 216.4 px | 0.07 | 0.96 | 1390 |
| stroke 8 | 95 % → 72 % | 222.8 px | 0.07 | 0.76 | 1430 |
| stroke 9 | 100 % → 74 % | 165.9 px | 0.07 | 0.74 | 949 |
| stroke 10 | 18 % → 18 % | 66.3 px | 0.07 | 1.00 | 216 |
| stroke 11 | 21 % → 35 % | 127.5 px | 0.07 | 1.65 | 175 |
| stroke 12 | 26 % → 37 % | 158.0 px | 0.08 | 1.45 | 199 |
| stroke 13 | 13 % → 41 % | 62.3 px | 0.08 | 3.19 | 272 |
| stroke 14 | 24 % → 54 % | 127.4 px | 0.07 | 2.25 | 336 |
| stroke 15 | 35 % → 64 % | 186.2 px | 0.07 | 1.82 | 258 |
| stroke 16 | 41 % → 71 % | 212.6 px | 0.07 | 1.73 | 240 |
| stroke 17 | 43 % → 73 % | 227.9 px | 0.07 | 1.68 | 239 |
| stroke 18 | 45 % → 72 % | 204.4 px | 0.07 | 1.59 | 275 |
| stroke 19 | 48 % → 72 % | 198.3 px | 0.07 | 1.50 | 311 |
| stroke 20 | 58 % → 72 % | 218.6 px | 0.07 | 1.24 | 267 |
| stroke 21 | 71 % → 75 % | 217.5 px | 0.07 | 1.04 | 234 |
| stroke 22 | 48 % → 48 % | 262.0 px | 0.07 | 0.99 | 246 |
| stroke 23 | 62 % → 61 % | 316.7 px | 0.07 | 0.99 | 303 |
| stroke 24 | 66 % → 66 % | 380.1 px | 0.07 | 0.99 | 242 |
| stroke 25 | 74 % → 73 % | 362.3 px | 0.07 | 0.99 | 251 |
| stroke 26 | 73 % → 72 % | 378.0 px | 0.07 | 0.99 | 348 |
| stroke 27 | 72 % → 72 % | 348.1 px | 0.07 | 1.00 | 258 |
| stroke 28 | 73 % → 72 % | 303.2 px | 0.07 | 0.99 | 320 |
| stroke 29 | 75 % → 73 % | 291.0 px | 0.07 | 0.98 | 291 |

Numbers say: wet paint spreads well beyond the stroke.

## Oil · Henry Ward · HW #14 olive totem on dark — own sheet
own sheet 600 × 600 · Gouache 1.00 · 84 px · 23.9 s

![Oil · Henry Ward · HW #14 olive totem on dark — own sheet](Oil-Henry-Ward-HW-14-olive-totem-on-dark-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 46 % → 39 % | 78.3 px | 0.29 | 0.84 | 1241 |
| stroke 2 | 62 % → 47 % | 145.7 px | 0.30 | 0.75 | 1817 |
| stroke 3 | 70 % → 46 % | 207.7 px | 0.30 | 0.65 | 1797 |
| stroke 4 | 71 % → 53 % | 218.9 px | 0.30 | 0.75 | 1788 |
| stroke 5 | 71 % → 60 % | 216.6 px | 0.29 | 0.84 | 1436 |
| stroke 6 | 71 % → 58 % | 216.8 px | 0.29 | 0.81 | 1294 |
| stroke 7 | 73 % → 47 % | 218.4 px | 0.28 | 0.65 | 1185 |
| stroke 8 | 93 % → 49 % | 216.7 px | 0.27 | 0.52 | 1197 |
| stroke 9 | 100 % → 46 % | 172.0 px | 0.27 | 0.46 | 896 |
| stroke 10 | 15 % → 69 % | 63.3 px | 0.29 | 4.62 | 323 |
| stroke 11 | 25 % → 72 % | 105.2 px | 0.29 | 2.93 | 302 |
| stroke 12 | 36 % → 63 % | 148.3 px | 0.29 | 1.77 | 272 |
| stroke 13 | 32 % → 46 % | 159.3 px | 0.30 | 1.41 | 285 |
| stroke 14 | 37 % → 50 % | 214.4 px | 0.30 | 1.35 | 300 |
| stroke 15 | 44 % → 56 % | 238.1 px | 0.30 | 1.28 | 364 |
| stroke 16 | 36 % → 51 % | 198.8 px | 0.29 | 1.41 | 325 |
| stroke 17 | 35 % → 46 % | 180.3 px | 0.28 | 1.32 | 244 |
| stroke 18 | 46 % → 49 % | 213.4 px | 0.27 | 1.07 | 252 |
| stroke 19 | 49 % → 48 % | 263.3 px | 0.30 | 0.97 | 247 |
| stroke 20 | 47 % → 48 % | 289.3 px | 0.30 | 1.04 | 276 |
| stroke 21 | 52 % → 53 % | 339.2 px | 0.30 | 1.03 | 307 |
| stroke 22 | 57 % → 58 % | 384.2 px | 0.29 | 1.02 | 225 |
| stroke 23 | 62 % → 60 % | 398.6 px | 0.28 | 0.97 | 228 |
| stroke 24 | 59 % → 57 % | 407.4 px | 0.29 | 0.96 | 160 |
| stroke 25 | 55 % → 52 % | 361.2 px | 0.29 | 0.95 | 179 |
| stroke 26 | 51 % → 47 % | 311.3 px | 0.28 | 0.93 | 244 |
| stroke 27 | 51 % → 47 % | 249.1 px | 0.27 | 0.93 | 232 |

Numbers say: wet paint spreads well beyond the stroke.

