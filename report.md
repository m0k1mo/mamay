![All brushes](contact.png)

# Brush Lab — 143 brushes · Nov 3, 2026 at 12:41 PM

Every sheet: 1500 × 600, ten strokes in a 5 × 2 grid — 1. light line · 2. heavy line · 3. pressure swell · 4. fast wave · 5. slow wave · 6. spiral · 7. loop · 8. tilted · 9. over the wet one · 10. long, no reload (cell 8 holds «tilted» and «over the wet one» crossed). The CPU reference of Mamay's paint engine; the wet layer settles 20 s at the end.

Columns: **covered** = share of the cell with paint right after the stroke → after settling; **dark** = mean darkness of the painted pixels above the paper's own grain (0 = paper, 1 = black); **spread** = how far wet paint went beyond the stroke (1.0 = stayed); **ms** = the stroke on the CPU; long stroke: paint in each quarter of its length (it should run out: wet → streaks → dry tail).

## Ink Line
Ink · 12 px · 27.6 s

![Ink Line](Ink-Line.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 1 % → 4 % | 0.55 | 2.44 | 98 |
| heavy line | 5 % → 6 % | 0.68 | 1.13 | 150 |
| pressure swell | 3 % → 4 % | 0.64 | 1.40 | 55 |
| fast wave | 10 % → 11 % | 0.59 | 1.11 | 230 |
| slow wave | 8 % → 10 % | 0.57 | 1.16 | 176 |
| spiral | 14 % → 15 % | 0.50 | 1.07 | 347 |
| loop | 8 % → 9 % | 0.61 | 1.16 | 119 |
| tilted | 5 % → 5 % | 0.65 | 1.05 | 67 |
| over the wet one | 10 % → 11 % | 0.65 | 1.15 | 58 |
| long, no reload | 18 % → 17 % | 0.47 | 0.96 | 328 | quarters: 0.22 → 0.09 → 0.04 → 0.02

Numbers say: wet paint spreads well beyond the stroke.

## Dense Ink
Ink · 14 px · 27.7 s

![Dense Ink](Dense-Ink.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 5 % → 7 % | 0.72 | 1.26 | 130 |
| heavy line | 7 % → 7 % | 0.73 | 1.09 | 147 |
| pressure swell | 5 % → 6 % | 0.72 | 1.17 | 55 |
| fast wave | 13 % → 13 % | 0.69 | 1.01 | 240 |
| slow wave | 12 % → 12 % | 0.67 | 1.04 | 223 |
| spiral | 18 % → 15 % | 0.65 | 0.80 | 385 |
| loop | 11 % → 12 % | 0.69 | 1.08 | 129 |
| tilted | 5 % → 6 % | 0.72 | 1.07 | 70 |
| over the wet one | 12 % → 13 % | 0.72 | 1.11 | 64 |
| long, no reload | 23 % → 15 % | 0.64 | 0.66 | 343 | quarters: 0.30 → 0.12 → 0.04 → 0.02

## Transparent Wash
Watercolor · 22 px · 28.6 s

![Transparent Wash](Transparent-Wash.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 2 % → 5 % | 0.27 | 2.25 | 99 |
| heavy line | 7 % → 9 % | 0.27 | 1.22 | 116 |
| pressure swell | 4 % → 6 % | 0.28 | 1.54 | 51 |
| fast wave | 14 % → 16 % | 0.20 | 1.17 | 247 |
| slow wave | 12 % → 15 % | 0.21 | 1.28 | 240 |
| spiral | 18 % → 22 % | 0.16 | 1.23 | 280 |
| loop | 11 % → 13 % | 0.22 | 1.20 | 106 |
| tilted | 8 % → 8 % | 0.24 | 1.06 | 71 |
| over the wet one | 13 % → 16 % | 0.24 | 1.18 | 72 |
| long, no reload | 26 % → 32 % | 0.13 | 1.22 | 314 | quarters: 0.11 → 0.04 → 0.02 → 0.01

Numbers say: wet paint spreads well beyond the stroke.

## Dry Brush
Gouache · 24 px · 22.9 s

![Dry Brush](Dry-Brush.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 5 % → 0 % | 0.65 | 0.09 | 43 |
| heavy line | 6 % → 0 % | 0.65 | 0.02 | 102 |
| pressure swell | 5 % → 0 % | 0.65 | 0.08 | 77 |
| fast wave | 6 % → 1 % | 0.65 | 0.08 | 397 |
| slow wave | 7 % → 0 % | 0.65 | 0.06 | 465 |
| spiral | 7 % → 0 % | 0.65 | 0.07 | 268 |
| loop | 10 % → 0 % | 0.65 | 0.04 | 153 |
| tilted | 4 % → 3 % | 0.65 | 0.88 | 72 |
| over the wet one | 9 % → 1 % | 0.65 | 0.12 | 66 |
| long, no reload | 6 % → 1 % | 0.65 | 0.14 | 368 | quarters: 0.12 → 0.00 → 0.00 → 0.00

## Wax Crayon
Wax · 8 px · 12.0 s

![Wax Crayon](Wax-Crayon.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 1 % → 1 % | 0.71 | 1.00 | 22 |
| heavy line | 1 % → 1 % | 0.69 | 1.00 | 20 |
| pressure swell | 1 % → 1 % | 0.70 | 1.00 | 13 |
| fast wave | 3 % → 3 % | 0.69 | 1.00 | 43 |
| slow wave | 3 % → 3 % | 0.70 | 1.00 | 61 |
| spiral | 5 % → 5 % | 0.70 | 1.00 | 153 |
| loop | 3 % → 3 % | 0.70 | 1.00 | 105 |
| tilted | 2 % → 2 % | 0.68 | 1.00 | 92 |
| over the wet one | 3 % → 3 % | 0.68 | 1.00 | 33 |
| long, no reload | 7 % → 7 % | 0.70 | 1.00 | 179 | quarters: 0.06 → 0.06 → 0.06 → 0.06

Numbers say: the long stroke does not run out of paint.

## Oil Pastel
Wax · 12 px · 12.2 s

![Oil Pastel](Oil-Pastel.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 1 % → 1 % | 0.68 | 1.00 | 21 |
| heavy line | 2 % → 2 % | 0.68 | 1.00 | 46 |
| pressure swell | 2 % → 2 % | 0.69 | 1.00 | 33 |
| fast wave | 5 % → 5 % | 0.68 | 1.00 | 164 |
| slow wave | 5 % → 5 % | 0.68 | 1.00 | 116 |
| spiral | 8 % → 8 % | 0.68 | 1.00 | 193 |
| loop | 4 % → 4 % | 0.68 | 1.00 | 89 |
| tilted | 2 % → 2 % | 0.68 | 1.00 | 82 |
| over the wet one | 5 % → 5 % | 0.68 | 1.00 | 44 |
| long, no reload | 13 % → 13 % | 0.68 | 1.00 | 159 | quarters: 0.10 → 0.09 → 0.10 → 0.10

Numbers say: the long stroke does not run out of paint.

## Charcoal
Charcoal · 5 px · 10.7 s

![Charcoal](Charcoal.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 1 % → 1 % | 0.74 | 1.00 | 11 |
| heavy line | 1 % → 1 % | 0.74 | 1.00 | 13 |
| pressure swell | 1 % → 1 % | 0.74 | 1.00 | 10 |
| fast wave | 2 % → 2 % | 0.73 | 1.00 | 29 |
| slow wave | 2 % → 2 % | 0.74 | 1.00 | 37 |
| spiral | 4 % → 4 % | 0.74 | 1.00 | 53 |
| loop | 2 % → 2 % | 0.74 | 1.00 | 36 |
| tilted | 2 % → 2 % | 0.72 | 1.00 | 28 |
| over the wet one | 2 % → 2 % | 0.72 | 1.00 | 20 |
| long, no reload | 6 % → 6 % | 0.73 | 1.00 | 116 | quarters: 0.05 → 0.05 → 0.05 → 0.05

Numbers say: the long stroke does not run out of paint.

## Impasto
Heavy acrylic · 22 px · 16.7 s

![Impasto](Impasto.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 8 % → 8 % | 0.71 | 0.93 | 44 |
| heavy line | 10 % → 9 % | 0.70 | 0.94 | 104 |
| pressure swell | 7 % → 7 % | 0.72 | 0.94 | 73 |
| fast wave | 20 % → 13 % | 0.71 | 0.64 | 321 |
| slow wave | 21 % → 14 % | 0.71 | 0.66 | 417 |
| spiral | 30 % → 14 % | 0.71 | 0.46 | 295 |
| loop | 18 % → 14 % | 0.71 | 0.77 | 177 |
| tilted | 8 % → 8 % | 0.70 | 1.00 | 93 |
| over the wet one | 17 % → 15 % | 0.70 | 0.91 | 75 |
| long, no reload | 34 % → 14 % | 0.71 | 0.41 | 421 | quarters: 0.38 → 0.21 → 0.10 → 0.03

## Oil Round
Oil · 18 px · 18.7 s

![Oil Round](Oil-Round.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 2 % → 2 % | 0.71 | 1.00 | 38 |
| heavy line | 6 % → 6 % | 0.72 | 1.00 | 68 |
| pressure swell | 3 % → 3 % | 0.63 | 1.00 | 40 |
| fast wave | 7 % → 7 % | 0.54 | 1.00 | 146 |
| slow wave | 4 % → 4 % | 0.36 | 1.00 | 175 |
| spiral | 5 % → 5 % | 0.21 | 1.00 | 241 |
| loop | 3 % → 3 % | 0.18 | 1.00 | 134 |
| tilted | 2 % → 2 % | 0.33 | 1.00 | 97 |
| over the wet one | 3 % → 3 % | 0.33 | 1.00 | 86 |
| long, no reload | 8 % → 8 % | 0.17 | 1.00 | 605 | quarters: 0.02 → 0.02 → 0.01 → 0.01

## Palette Knife
Oil · 20 px · 18.1 s

![Palette Knife](Palette-Knife.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 8 % → 8 % | 0.67 | 1.00 | 11 |
| heavy line | 8 % → 8 % | 0.73 | 1.00 | 13 |
| pressure swell | 6 % → 6 % | 0.74 | 1.00 | 6 |
| fast wave | 17 % → 17 % | 0.49 | 1.00 | 28 |
| slow wave | 17 % → 17 % | 0.43 | 1.00 | 37 |
| spiral | 18 % → 18 % | 0.45 | 1.00 | 46 |
| loop | 16 % → 16 % | 0.58 | 1.00 | 36 |
| tilted | 5 % → 5 % | 0.72 | 1.00 | 10 |
| over the wet one | 13 % → 13 % | 0.72 | 1.00 | 13 |
| long, no reload | 17 % → 17 % | 0.47 | 1.00 | 91 | quarters: 0.29 → 0.05 → 0.00 → 0.00

Numbers say: pressure barely changes the width.

## Water
Watercolor · 20 px · 35.8 s · over bands of wet oil paint and oil pastel in turn (it works on paint already there: look at what it does to the bands; covered counts the bands too)

![Water](Water.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 25 % → 26 % | 0.78 | 1.07 | 25 |
| heavy line | 23 % → 24 % | 0.80 | 1.04 | 57 |
| pressure swell | 23 % → 24 % | 0.80 | 1.03 | 33 |
| fast wave | 23 % → 25 % | 0.80 | 1.07 | 115 |
| slow wave | 23 % → 25 % | 0.80 | 1.06 | 155 |
| spiral | 23 % → 25 % | 0.79 | 1.08 | 173 |
| loop | 23 % → 24 % | 0.80 | 1.03 | 92 |
| tilted | 23 % → 23 % | 0.80 | 1.00 | 90 |
| over the wet one | 23 % → 25 % | 0.80 | 1.07 | 64 |
| long, no reload | 23 % → 25 % | 0.80 | 1.08 | 304 | quarters: 0.21 → 0.26 → 0.17 → 0.25

Numbers say: pressure barely changes the width; the long stroke does not run out of paint.

## Blender
Pastel · 16 px · 21.3 s · over bands of wet oil paint and oil pastel in turn (it works on paint already there: look at what it does to the bands; covered counts the bands too)

![Blender](Blender.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 24 % → 24 % | 0.80 | 1.00 | 22 |
| heavy line | 24 % → 24 % | 0.80 | 1.00 | 35 |
| pressure swell | 24 % → 24 % | 0.80 | 1.00 | 28 |
| fast wave | 25 % → 25 % | 0.78 | 1.00 | 82 |
| slow wave | 25 % → 25 % | 0.78 | 1.00 | 100 |
| spiral | 27 % → 27 % | 0.76 | 1.00 | 129 |
| loop | 25 % → 25 % | 0.79 | 1.00 | 66 |
| tilted | 24 % → 24 % | 0.78 | 1.00 | 47 |
| over the wet one | 25 % → 25 % | 0.78 | 1.00 | 29 |
| long, no reload | 29 % → 29 % | 0.74 | 1.00 | 198 | quarters: 0.19 → 0.26 → 0.21 → 0.28

Numbers say: pressure barely changes the width; the long stroke does not run out of paint.

## Eraser
Eraser · 16 px · 21.0 s · over bands of wet oil paint and oil pastel in turn (it works on paint already there: look at what it does to the bands; covered counts the bands too)

![Eraser](Eraser.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 23 % → 23 % | 0.81 | 1.00 | 35 |
| heavy line | 23 % → 23 % | 0.81 | 1.00 | 34 |
| pressure swell | 23 % → 23 % | 0.81 | 1.00 | 28 |
| fast wave | 22 % → 22 % | 0.81 | 1.00 | 84 |
| slow wave | 22 % → 22 % | 0.81 | 1.00 | 102 |
| spiral | 21 % → 21 % | 0.81 | 1.00 | 123 |
| loop | 22 % → 22 % | 0.81 | 1.00 | 73 |
| tilted | 23 % → 23 % | 0.81 | 1.00 | 41 |
| over the wet one | 22 % → 22 % | 0.81 | 1.00 | 66 |
| long, no reload | 19 % → 19 % | 0.81 | 1.00 | 196 | quarters: 0.15 → 0.19 → 0.14 → 0.20

Numbers say: pressure barely changes the width; the long stroke does not run out of paint.

## Fan
Gouache · 30 px · 36.9 s

![Fan](Fan.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 9 % → 3 % | 0.63 | 0.37 | 28 |
| heavy line | 11 % → 4 % | 0.63 | 0.39 | 57 |
| pressure swell | 8 % → 5 % | 0.63 | 0.55 | 49 |
| fast wave | 18 % → 5 % | 0.63 | 0.26 | 127 |
| slow wave | 18 % → 5 % | 0.63 | 0.25 | 180 |
| spiral | 24 % → 5 % | 0.63 | 0.20 | 181 |
| loop | 17 % → 5 % | 0.63 | 0.29 | 86 |
| tilted | 5 % → 6 % | 0.63 | 1.05 | 37 |
| over the wet one | 16 % → 8 % | 0.63 | 0.50 | 45 |
| long, no reload | 23 % → 5 % | 0.63 | 0.22 | 451 | quarters: 0.29 → 0.07 → 0.01 → 0.00

## Sponge
Gouache · 30 px · 36.6 s

![Sponge](Sponge.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 4 % → 0 % | 0.62 | 0.12 | 43 |
| heavy line | 12 % → 2 % | 0.62 | 0.14 | 71 |
| pressure swell | 7 % → 2 % | 0.62 | 0.27 | 68 |
| fast wave | 20 % → 4 % | 0.62 | 0.19 | 179 |
| slow wave | 21 % → 4 % | 0.62 | 0.18 | 235 |
| spiral | 28 % → 4 % | 0.62 | 0.14 | 205 |
| loop | 18 % → 5 % | 0.62 | 0.29 | 126 |
| tilted | 7 % → 7 % | 0.62 | 1.04 | 95 |
| over the wet one | 16 % → 6 % | 0.62 | 0.37 | 51 |
| long, no reload | 29 % → 5 % | 0.62 | 0.17 | 494 | quarters: 0.29 → 0.13 → 0.07 → 0.04

## Ink — sumi brush
Watercolor · 22 px · 35.9 s

![Ink — sumi brush](Ink-sumi-brush.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 6 % → 7 % | 0.46 | 1.06 | 79 |
| heavy line | 10 % → 11 % | 0.38 | 1.05 | 64 |
| pressure swell | 7 % → 8 % | 0.42 | 1.04 | 47 |
| fast wave | 21 % → 21 % | 0.32 | 1.00 | 145 |
| slow wave | 19 % → 19 % | 0.37 | 1.01 | 222 |
| spiral | 28 % → 26 % | 0.30 | 0.92 | 271 |
| loop | 17 % → 18 % | 0.37 | 1.06 | 181 |
| tilted | 6 % → 7 % | 0.40 | 1.17 | 97 |
| over the wet one | 16 % → 16 % | 0.40 | 1.01 | 75 |
| long, no reload | 33 % → 29 % | 0.30 | 0.86 | 724 | quarters: 0.23 → 0.11 → 0.06 → 0.04

## Ink — wash
Watercolor · 40 px · 38.3 s

![Ink — wash](Ink-wash.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 8 % → 9 % | 0.05 | 1.26 | 87 |
| heavy line | 11 % → 13 % | 0.04 | 1.22 | 102 |
| pressure swell | 7 % → 9 % | 0.05 | 1.25 | 81 |
| fast wave | 22 % → 27 % | 0.04 | 1.21 | 265 |
| slow wave | 21 % → 26 % | 0.06 | 1.23 | 516 |
| spiral | 34 % → 41 % | 0.04 | 1.21 | 454 |
| loop | 19 % → 24 % | 0.05 | 1.25 | 179 |
| tilted | 7 % → 9 % | 0.05 | 1.21 | 103 |
| over the wet one | 18 % → 21 % | 0.05 | 1.18 | 76 |
| long, no reload | 39 % → 46 % | 0.05 | 1.19 | 463 | quarters: 0.04 → 0.03 → 0.02 → 0.01

## Ink — dry brush
Ink · 30 px · 28.7 s

![Ink — dry brush](Ink-dry-brush.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 9 % → 7 % | 0.81 | 0.78 | 100 |
| heavy line | 11 % → 8 % | 0.80 | 0.73 | 145 |
| pressure swell | 8 % → 7 % | 0.81 | 0.85 | 93 |
| fast wave | 22 % → 8 % | 0.78 | 0.38 | 283 |
| slow wave | 18 % → 6 % | 0.80 | 0.36 | 623 |
| spiral | 23 % → 8 % | 0.77 | 0.35 | 510 |
| loop | 20 % → 8 % | 0.77 | 0.41 | 192 |
| tilted | 9 % → 9 % | 0.78 | 1.01 | 137 |
| over the wet one | 19 % → 14 % | 0.78 | 0.75 | 84 |
| long, no reload | 20 % → 9 % | 0.78 | 0.42 | 528 | quarters: 0.32 → 0.01 → 0.00 → 0.00

## Ink — nib
Watercolor · 5 px · 26.0 s

![Ink — nib](Ink-nib.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 2 % → 2 % | 0.76 | 1.17 | 34 |
| heavy line | 2 % → 2 % | 0.77 | 1.16 | 29 |
| pressure swell | 1 % → 2 % | 0.78 | 1.22 | 42 |
| fast wave | 4 % → 4 % | 0.66 | 1.09 | 120 |
| slow wave | 4 % → 4 % | 0.68 | 1.11 | 89 |
| spiral | 6 % → 6 % | 0.58 | 1.08 | 123 |
| loop | 3 % → 4 % | 0.69 | 1.12 | 55 |
| tilted | 2 % → 2 % | 0.64 | 1.21 | 28 |
| over the wet one | 4 % → 4 % | 0.64 | 1.03 | 27 |
| long, no reload | 7 % → 7 % | 0.53 | 1.02 | 154 | quarters: 0.09 → 0.04 → 0.03 → 0.02

## 0.45 · Dry brush
Gouache · 34 px · 30.5 s

![0.45 · Dry brush](0-45-Dry-brush.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 11 % → 3 % | 0.67 | 0.28 | 108 |
| heavy line | 12 % → 3 % | 0.67 | 0.30 | 185 |
| pressure swell | 9 % → 4 % | 0.67 | 0.40 | 135 |
| fast wave | 20 % → 4 % | 0.67 | 0.19 | 409 |
| slow wave | 20 % → 4 % | 0.67 | 0.18 | 705 |
| spiral | 21 % → 4 % | 0.67 | 0.17 | 580 |
| loop | 21 % → 4 % | 0.67 | 0.19 | 280 |
| tilted | 9 % → 9 % | 0.67 | 0.97 | 159 |
| over the wet one | 20 % → 7 % | 0.67 | 0.33 | 131 |
| long, no reload | 20 % → 4 % | 0.67 | 0.21 | 723 | quarters: 0.38 → 0.07 → 0.00 → 0.00

Numbers say: pressure barely changes the width.

## Dry pastel
Pastel · 26 px · 13.0 s

![Dry pastel](Dry-pastel.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 5 % → 5 % | 0.36 | 1.00 | 35 |
| heavy line | 6 % → 6 % | 0.36 | 1.00 | 50 |
| pressure swell | 5 % → 5 % | 0.36 | 1.00 | 41 |
| fast wave | 15 % → 15 % | 0.36 | 1.00 | 157 |
| slow wave | 14 % → 14 % | 0.36 | 1.00 | 220 |
| spiral | 23 % → 23 % | 0.36 | 1.00 | 272 |
| loop | 11 % → 11 % | 0.36 | 1.00 | 104 |
| tilted | 5 % → 5 % | 0.37 | 1.00 | 50 |
| over the wet one | 10 % → 10 % | 0.37 | 1.00 | 34 |
| long, no reload | 26 % → 26 % | 0.36 | 1.00 | 247 | quarters: 0.11 → 0.10 → 0.10 → 0.11

Numbers say: the long stroke does not run out of paint.

## 0.45 · Charcoal
Charcoal · 18 px · 12.9 s

![0.45 · Charcoal](0-45-Charcoal.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 4 % → 4 % | 0.79 | 1.00 | 17 |
| heavy line | 4 % → 4 % | 0.79 | 1.00 | 18 |
| pressure swell | 4 % → 4 % | 0.79 | 1.00 | 44 |
| fast wave | 11 % → 11 % | 0.79 | 1.00 | 42 |
| slow wave | 11 % → 11 % | 0.78 | 1.00 | 65 |
| spiral | 20 % → 20 % | 0.79 | 1.00 | 79 |
| loop | 10 % → 10 % | 0.79 | 1.00 | 36 |
| tilted | 4 % → 4 % | 0.78 | 1.00 | 24 |
| over the wet one | 9 % → 9 % | 0.78 | 1.00 | 16 |
| long, no reload | 26 % → 26 % | 0.79 | 1.00 | 106 | quarters: 0.23 → 0.22 → 0.23 → 0.24

Numbers say: pressure barely changes the width; the long stroke does not run out of paint.

## Watercolour — wash
Watercolor · 50 px · 37.3 s

![Watercolour — wash](Watercolour-wash.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 9 % → 11 % | 0.01 | 1.22 | 94 |
| heavy line | 12 % → 14 % | 0.01 | 1.17 | 177 |
| pressure swell | 8 % → 10 % | 0.01 | 1.22 | 120 |
| fast wave | 26 % → 30 % | 0.01 | 1.18 | 406 |
| slow wave | 25 % → 29 % | 0.01 | 1.18 | 722 |
| spiral | 39 % → 46 % | 0.01 | 1.17 | 421 |
| loop | 22 % → 27 % | 0.01 | 1.21 | 232 |
| tilted | 10 % → 11 % | 0.01 | 1.18 | 152 |
| over the wet one | 22 % → 25 % | 0.01 | 1.14 | 102 |
| long, no reload | 45 % → 54 % | 0.01 | 1.18 | 630 | quarters: 0.01 → 0.01 → 0.01 → 0.00

## Watercolour — wet-in-wet
Watercolor · 44 px · 34.5 s

![Watercolour — wet-in-wet](Watercolour-wet-in-wet.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 7 % → 9 % | 0.02 | 1.26 | 79 |
| heavy line | 10 % → 12 % | 0.02 | 1.22 | 95 |
| pressure swell | 7 % → 9 % | 0.02 | 1.21 | 57 |
| fast wave | 23 % → 27 % | 0.02 | 1.17 | 263 |
| slow wave | 22 % → 26 % | 0.02 | 1.18 | 370 |
| spiral | 36 % → 43 % | 0.02 | 1.20 | 601 |
| loop | 19 % → 23 % | 0.02 | 1.20 | 193 |
| tilted | 7 % → 9 % | 0.02 | 1.19 | 126 |
| over the wet one | 17 % → 19 % | 0.02 | 1.12 | 99 |
| long, no reload | 42 % → 49 % | 0.02 | 1.18 | 584 | quarters: 0.01 → 0.01 → 0.01 → 0.01

## Watercolour — glaze
Watercolor · 38 px · 31.5 s

![Watercolour — glaze](Watercolour-glaze.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 7 % → 9 % | 0.01 | 1.28 | 75 |
| heavy line | 10 % → 13 % | 0.01 | 1.25 | 107 |
| pressure swell | 7 % → 9 % | 0.01 | 1.29 | 78 |
| fast wave | 20 % → 25 % | 0.01 | 1.24 | 229 |
| slow wave | 19 % → 24 % | 0.01 | 1.26 | 305 |
| spiral | 31 % → 37 % | 0.01 | 1.21 | 320 |
| loop | 18 % → 23 % | 0.01 | 1.27 | 182 |
| tilted | 7 % → 8 % | 0.01 | 1.20 | 113 |
| over the wet one | 17 % → 20 % | 0.01 | 1.19 | 72 |
| long, no reload | 36 % → 42 % | 0.01 | 1.17 | 413 | quarters: 0.01 → 0.00 → 0.00 → 0.00

## Watercolour — granulating
Watercolor · 44 px · 40.4 s

![Watercolour — granulating](Watercolour-granulating.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 8 % → 10 % | 0.02 | 1.18 | 78 |
| heavy line | 12 % → 14 % | 0.01 | 1.15 | 102 |
| pressure swell | 8 % → 10 % | 0.02 | 1.18 | 101 |
| fast wave | 25 % → 29 % | 0.01 | 1.15 | 342 |
| slow wave | 24 % → 27 % | 0.02 | 1.16 | 445 |
| spiral | 39 % → 44 % | 0.01 | 1.15 | 372 |
| loop | 22 % → 25 % | 0.01 | 1.17 | 190 |
| tilted | 9 % → 11 % | 0.02 | 1.15 | 139 |
| over the wet one | 21 % → 23 % | 0.02 | 1.11 | 97 |
| long, no reload | 45 % → 52 % | 0.01 | 1.15 | 654 | quarters: 0.01 → 0.01 → 0.01 → 0.01

## Watercolour — dry brush
Watercolor · 36 px · 35.6 s

![Watercolour — dry brush](Watercolour-dry-brush.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 7 % → 8 % | 0.05 | 1.07 | 105 |
| heavy line | 11 % → 12 % | 0.04 | 1.03 | 107 |
| pressure swell | 9 % → 10 % | 0.05 | 1.07 | 81 |
| fast wave | 21 % → 14 % | 0.04 | 0.68 | 289 |
| slow wave | 19 % → 13 % | 0.04 | 0.70 | 487 |
| spiral | 24 % → 15 % | 0.04 | 0.61 | 456 |
| loop | 17 % → 14 % | 0.04 | 0.85 | 232 |
| tilted | 7 % → 8 % | 0.05 | 1.19 | 130 |
| over the wet one | 17 % → 17 % | 0.05 | 0.99 | 99 |
| long, no reload | 22 % → 15 % | 0.04 | 0.68 | 1064 | quarters: 0.02 → 0.00 → 0.00 → 0.00

## Gouache
Gouache · 30 px · 36.3 s

![Gouache](Gouache.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 8 % → 6 % | 0.14 | 0.67 | 74 |
| heavy line | 13 % → 6 % | 0.14 | 0.47 | 85 |
| pressure swell | 10 % → 6 % | 0.14 | 0.61 | 61 |
| fast wave | 27 % → 7 % | 0.14 | 0.27 | 477 |
| slow wave | 27 % → 7 % | 0.14 | 0.27 | 613 |
| spiral | 37 % → 8 % | 0.14 | 0.22 | 439 |
| loop | 22 % → 8 % | 0.14 | 0.36 | 276 |
| tilted | 9 % → 9 % | 0.14 | 1.02 | 120 |
| over the wet one | 20 % → 13 % | 0.14 | 0.67 | 98 |
| long, no reload | 38 % → 10 % | 0.14 | 0.25 | 652 | quarters: 0.07 → 0.04 → 0.01 → 0.01

## Oil — alla prima
Oil · 30 px · 24.5 s

![Oil — alla prima](Oil-alla-prima.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 9 % → 9 % | 0.50 | 1.00 | 313 |
| heavy line | 10 % → 10 % | 0.50 | 1.00 | 143 |
| pressure swell | 8 % → 8 % | 0.52 | 1.00 | 116 |
| fast wave | 24 % → 24 % | 0.49 | 1.00 | 274 |
| slow wave | 25 % → 25 % | 0.50 | 1.00 | 481 |
| spiral | 38 % → 38 % | 0.44 | 1.00 | 379 |
| loop | 21 % → 21 % | 0.50 | 1.00 | 186 |
| tilted | 11 % → 11 % | 0.50 | 1.00 | 128 |
| over the wet one | 20 % → 20 % | 0.50 | 1.00 | 95 |
| long, no reload | 46 % → 46 % | 0.40 | 1.00 | 575 | quarters: 0.31 → 0.24 → 0.17 → 0.10

Numbers say: pressure barely changes the width.

## Oil — impasto
Oil · 34 px · 25.3 s

![Oil — impasto](Oil-impasto.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 11 % → 11 % | 0.24 | 1.00 | 190 |
| heavy line | 12 % → 12 % | 0.23 | 1.00 | 126 |
| pressure swell | 9 % → 9 % | 0.25 | 1.00 | 80 |
| fast wave | 29 % → 29 % | 0.21 | 1.00 | 277 |
| slow wave | 29 % → 29 % | 0.21 | 1.00 | 521 |
| spiral | 48 % → 48 % | 0.17 | 1.00 | 562 |
| loop | 25 % → 25 % | 0.21 | 1.00 | 271 |
| tilted | 12 % → 12 % | 0.24 | 1.00 | 147 |
| over the wet one | 23 % → 23 % | 0.24 | 1.00 | 111 |
| long, no reload | 55 % → 55 % | 0.15 | 1.00 | 820 | quarters: 0.16 → 0.11 → 0.06 → 0.02

Numbers say: pressure barely changes the width.

## Oil — glaze
Oil · 40 px · 20.9 s

![Oil — glaze](Oil-glaze.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 10 % → 10 % | 0.49 | 1.00 | 100 |
| heavy line | 14 % → 14 % | 0.48 | 1.00 | 106 |
| pressure swell | 10 % → 10 % | 0.49 | 1.00 | 113 |
| fast wave | 28 % → 28 % | 0.46 | 1.00 | 281 |
| slow wave | 30 % → 30 % | 0.46 | 1.00 | 561 |
| spiral | 42 % → 42 % | 0.44 | 1.00 | 622 |
| loop | 24 % → 24 % | 0.47 | 1.00 | 296 |
| tilted | 11 % → 11 % | 0.47 | 1.00 | 236 |
| over the wet one | 23 % → 23 % | 0.47 | 1.00 | 167 |
| long, no reload | 47 % → 47 % | 0.43 | 1.00 | 1115 | quarters: 0.33 → 0.24 → 0.18 → 0.14

## Oil — scumble
Oil · 36 px · 26.7 s

![Oil — scumble](Oil-scumble.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 11 % → 11 % | 0.06 | 1.00 | 141 |
| heavy line | 12 % → 12 % | 0.05 | 1.00 | 227 |
| pressure swell | 9 % → 9 % | 0.06 | 1.00 | 154 |
| fast wave | 18 % → 18 % | 0.04 | 1.00 | 496 |
| slow wave | 20 % → 20 % | 0.04 | 1.00 | 615 |
| spiral | 19 % → 19 % | 0.03 | 1.00 | 638 |
| loop | 22 % → 22 % | 0.04 | 1.00 | 410 |
| tilted | 10 % → 10 % | 0.05 | 1.00 | 235 |
| over the wet one | 21 % → 21 % | 0.05 | 1.00 | 193 |
| long, no reload | 18 % → 18 % | 0.04 | 1.00 | 1124 | quarters: 0.03 → 0.00 → 0.00 → 0.00

Numbers say: pressure barely changes the width.

## Acrylic — heavy body
Heavy acrylic · 30 px · 20.3 s

![Acrylic — heavy body](Acrylic-heavy-body.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 10 % → 9 % | 0.51 | 0.93 | 133 |
| heavy line | 11 % → 10 % | 0.51 | 0.93 | 81 |
| pressure swell | 8 % → 8 % | 0.52 | 0.94 | 72 |
| fast wave | 24 % → 14 % | 0.51 | 0.58 | 220 |
| slow wave | 25 % → 15 % | 0.51 | 0.59 | 540 |
| spiral | 37 % → 15 % | 0.51 | 0.40 | 587 |
| loop | 22 % → 16 % | 0.51 | 0.73 | 274 |
| tilted | 10 % → 10 % | 0.51 | 1.00 | 172 |
| over the wet one | 20 % → 17 % | 0.51 | 0.88 | 171 |
| long, no reload | 39 % → 15 % | 0.51 | 0.40 | 673 | quarters: 0.30 → 0.20 → 0.10 → 0.02

Numbers say: pressure barely changes the width.

## Acrylic — fluid
Watercolor · 36 px · 39.2 s

![Acrylic — fluid](Acrylic-fluid.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 9 % → 10 % | 0.06 | 1.11 | 88 |
| heavy line | 13 % → 14 % | 0.05 | 1.07 | 114 |
| pressure swell | 9 % → 10 % | 0.07 | 1.09 | 86 |
| fast wave | 26 % → 28 % | 0.05 | 1.07 | 280 |
| slow wave | 24 % → 26 % | 0.07 | 1.08 | 455 |
| spiral | 39 % → 41 % | 0.05 | 1.06 | 427 |
| loop | 22 % → 25 % | 0.06 | 1.11 | 209 |
| tilted | 8 % → 9 % | 0.07 | 1.17 | 153 |
| over the wet one | 21 % → 22 % | 0.07 | 1.05 | 90 |
| long, no reload | 44 % → 47 % | 0.05 | 1.06 | 931 | quarters: 0.05 → 0.03 → 0.02 → 0.01

## Acrylic — palette knife
Heavy acrylic · 42 px · 26.7 s

![Acrylic — palette knife](Acrylic-palette-knife.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 15 % → 15 % | 0.06 | 0.98 | 34 |
| heavy line | 15 % → 15 % | 0.05 | 0.98 | 24 |
| pressure swell | 12 % → 12 % | 0.06 | 0.99 | 10 |
| fast wave | 37 % → 20 % | 0.06 | 0.54 | 68 |
| slow wave | 37 % → 21 % | 0.06 | 0.56 | 136 |
| spiral | 48 % → 19 % | 0.06 | 0.38 | 157 |
| loop | 32 % → 24 % | 0.05 | 0.75 | 115 |
| tilted | 12 % → 12 % | 0.05 | 1.00 | 34 |
| over the wet one | 26 % → 26 % | 0.05 | 0.98 | 39 |
| long, no reload | 55 % → 20 % | 0.06 | 0.36 | 180 | quarters: 0.04 → 0.02 → 0.00 → 0.00

Numbers say: pressure barely changes the width.

## Finger on oil
Oil · 30 px · 20.5 s

![Finger on oil](Finger-on-oil.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 8 % → 8 % | 0.34 | 1.00 | 104 |
| heavy line | 12 % → 12 % | 0.30 | 1.00 | 106 |
| pressure swell | 8 % → 8 % | 0.35 | 1.00 | 66 |
| fast wave | 16 % → 16 % | 0.22 | 1.00 | 215 |
| slow wave | 17 % → 17 % | 0.23 | 1.00 | 242 |
| spiral | 18 % → 18 % | 0.22 | 1.00 | 303 |
| loop | 18 % → 18 % | 0.23 | 1.00 | 110 |
| tilted | 9 % → 9 % | 0.31 | 1.00 | 101 |
| over the wet one | 18 % → 18 % | 0.31 | 1.00 | 75 |
| long, no reload | 15 % → 15 % | 0.23 | 1.00 | 380 | quarters: 0.13 → 0.01 → 0.00 → 0.00

## Palette knife — oil
Oil · 44 px · 28.0 s

![Palette knife — oil](Palette-knife-oil.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 16 % → 16 % | 0.10 | 1.00 | 62 |
| heavy line | 16 % → 16 % | 0.09 | 1.00 | 56 |
| pressure swell | 12 % → 12 % | 0.10 | 1.00 | 22 |
| fast wave | 39 % → 39 % | 0.07 | 1.00 | 118 |
| slow wave | 39 % → 39 % | 0.07 | 1.00 | 123 |
| spiral | 54 % → 54 % | 0.05 | 1.00 | 129 |
| loop | 34 % → 34 % | 0.08 | 1.00 | 67 |
| tilted | 13 % → 13 % | 0.09 | 1.00 | 28 |
| over the wet one | 28 % → 28 % | 0.09 | 1.00 | 26 |
| long, no reload | 65 % → 65 % | 0.05 | 1.00 | 168 | quarters: 0.08 → 0.04 → 0.01 → 0.00

Numbers say: pressure barely changes the width.

## 0.45 · Sponge
Watercolor · 46 px · 30.1 s

![0.45 · Sponge](0-45-Sponge.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 11 % → 0 % | 0.00 | 0.00 | 73 |
| heavy line | 13 % → 0 % | 0.01 | 0.00 | 91 |
| pressure swell | 9 % → 1 % | 0.02 | 0.14 | 51 |
| fast wave | 23 % → 2 % | 0.01 | 0.08 | 149 |
| slow wave | 26 % → 8 % | 0.02 | 0.30 | 324 |
| spiral | 34 % → 11 % | 0.02 | 0.32 | 460 |
| loop | 22 % → 4 % | 0.02 | 0.19 | 231 |
| tilted | 9 % → 10 % | 0.04 | 1.19 | 115 |
| over the wet one | 22 % → 10 % | 0.04 | 0.44 | 81 |
| long, no reload | 41 % → 19 % | 0.02 | 0.47 | 439 | quarters: 0.01 → 0.01 → 0.01 → 0.01

## 0.45 · Eraser
Eraser · 30 px · 26.2 s · over bands of wet oil paint and oil pastel in turn (it works on paint already there: look at what it does to the bands; covered counts the bands too)

![0.45 · Eraser](0-45-Eraser.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 23 % → 23 % | 0.81 | 1.00 | 65 |
| heavy line | 22 % → 22 % | 0.81 | 1.00 | 107 |
| pressure swell | 22 % → 22 % | 0.81 | 1.00 | 52 |
| fast wave | 21 % → 21 % | 0.80 | 1.00 | 174 |
| slow wave | 20 % → 20 % | 0.81 | 1.00 | 272 |
| spiral | 20 % → 20 % | 0.79 | 1.00 | 259 |
| loop | 21 % → 21 % | 0.79 | 1.00 | 140 |
| tilted | 22 % → 22 % | 0.80 | 1.00 | 75 |
| over the wet one | 21 % → 21 % | 0.80 | 1.00 | 74 |
| long, no reload | 16 % → 16 % | 0.79 | 1.00 | 397 | quarters: 0.13 → 0.15 → 0.12 → 0.16

Numbers say: pressure barely changes the width; the long stroke does not run out of paint.

## Lift wet paint
Eraser · 30 px · 25.6 s · over bands of wet oil paint and oil pastel in turn (it works on paint already there: look at what it does to the bands; covered counts the bands too)

![Lift wet paint](Lift-wet-paint.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 23 % → 23 % | 0.81 | 1.00 | 36 |
| heavy line | 23 % → 23 % | 0.81 | 1.00 | 42 |
| pressure swell | 23 % → 23 % | 0.81 | 1.00 | 35 |
| fast wave | 23 % → 23 % | 0.81 | 1.00 | 124 |
| slow wave | 23 % → 23 % | 0.81 | 1.00 | 208 |
| spiral | 23 % → 23 % | 0.81 | 1.00 | 271 |
| loop | 23 % → 23 % | 0.81 | 1.00 | 124 |
| tilted | 23 % → 23 % | 0.81 | 1.00 | 70 |
| over the wet one | 23 % → 23 % | 0.81 | 1.00 | 47 |
| long, no reload | 23 % → 23 % | 0.81 | 1.00 | 305 | quarters: 0.18 → 0.23 → 0.16 → 0.23

Numbers say: pressure barely changes the width; the long stroke does not run out of paint.

## Sgraffito
Eraser · 10 px · 25.5 s · over bands of wet oil paint and oil pastel in turn (it works on paint already there: look at what it does to the bands; covered counts the bands too)

![Sgraffito](Sgraffito.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 23 % → 23 % | 0.80 | 1.00 | 7 |
| heavy line | 23 % → 23 % | 0.81 | 1.00 | 7 |
| pressure swell | 23 % → 23 % | 0.81 | 1.00 | 7 |
| fast wave | 23 % → 23 % | 0.81 | 1.00 | 24 |
| slow wave | 23 % → 23 % | 0.81 | 1.00 | 30 |
| spiral | 23 % → 23 % | 0.81 | 1.00 | 53 |
| loop | 23 % → 23 % | 0.81 | 1.00 | 24 |
| tilted | 23 % → 23 % | 0.81 | 1.00 | 7 |
| over the wet one | 23 % → 23 % | 0.81 | 1.00 | 14 |
| long, no reload | 23 % → 23 % | 0.81 | 1.00 | 73 | quarters: 0.17 → 0.23 → 0.16 → 0.23

Numbers say: pressure barely changes the width; the long stroke does not run out of paint.

## Brush Artist · Refs · #01 Henry Ward peach cloud
Gouache · 44 px · 38.9 s

![Brush Artist · Refs · #01 Henry Ward peach cloud](Brush-Artist-Refs-01-Henry-Ward-peach-cloud.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 14 % → 7 % | 0.10 | 0.50 | 212 |
| heavy line | 16 % → 9 % | 0.10 | 0.58 | 257 |
| pressure swell | 12 % → 8 % | 0.10 | 0.65 | 186 |
| fast wave | 37 % → 11 % | 0.10 | 0.29 | 469 |
| slow wave | 36 % → 11 % | 0.10 | 0.31 | 842 |
| spiral | 57 % → 11 % | 0.10 | 0.20 | 855 |
| loop | 31 % → 12 % | 0.10 | 0.39 | 476 |
| tilted | 13 % → 13 % | 0.10 | 1.01 | 226 |
| over the wet one | 27 % → 18 % | 0.10 | 0.67 | 205 |
| long, no reload | 64 % → 15 % | 0.10 | 0.23 | 1710 | quarters: 0.07 → 0.04 → 0.01 → 0.00

Numbers say: pressure barely changes the width.

## Brush Artist · Refs · #02 Henry Ward cream strokes
Gouache · 46 px · 39.4 s

![Brush Artist · Refs · #02 Henry Ward cream strokes](Brush-Artist-Refs-02-Henry-Ward-cream-strokes.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 13 % → 6 % | 0.03 | 0.46 | 155 |
| heavy line | 14 % → 9 % | 0.03 | 0.64 | 179 |
| pressure swell | 11 % → 8 % | 0.03 | 0.72 | 126 |
| fast wave | 34 % → 10 % | 0.03 | 0.30 | 443 |
| slow wave | 34 % → 11 % | 0.03 | 0.31 | 836 |
| spiral | 55 % → 12 % | 0.03 | 0.21 | 1085 |
| loop | 30 % → 12 % | 0.03 | 0.39 | 654 |
| tilted | 13 % → 13 % | 0.03 | 1.00 | 270 |
| over the wet one | 26 % → 18 % | 0.03 | 0.69 | 236 |
| long, no reload | 62 % → 14 % | 0.03 | 0.23 | 1157 | quarters: 0.02 → 0.02 → 0.01 → 0.00

Numbers say: pressure barely changes the width.

## Brush Artist · Refs · #03 Henry Ward navy contours
Heavy acrylic · 22 px · 21.4 s

![Brush Artist · Refs · #03 Henry Ward navy contours](Brush-Artist-Refs-03-Henry-Ward-navy-contours.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 7 % → 7 % | 0.70 | 0.94 | 93 |
| heavy line | 8 % → 8 % | 0.70 | 0.95 | 124 |
| pressure swell | 6 % → 6 % | 0.73 | 0.94 | 60 |
| fast wave | 19 % → 12 % | 0.72 | 0.65 | 233 |
| slow wave | 19 % → 13 % | 0.72 | 0.68 | 608 |
| spiral | 30 % → 13 % | 0.72 | 0.45 | 591 |
| loop | 17 % → 13 % | 0.72 | 0.81 | 305 |
| tilted | 8 % → 8 % | 0.71 | 1.00 | 124 |
| over the wet one | 16 % → 14 % | 0.71 | 0.89 | 107 |
| long, no reload | 34 % → 13 % | 0.72 | 0.40 | 624 | quarters: 0.35 → 0.29 → 0.19 → 0.07

Numbers say: pressure barely changes the width.

## Brush Artist · Refs · #04 Henry Ward grey cloud
Gouache · 50 px · 41.3 s

![Brush Artist · Refs · #04 Henry Ward grey cloud](Brush-Artist-Refs-04-Henry-Ward-grey-cloud.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 15 % → 6 % | 0.10 | 0.42 | 636 |
| heavy line | 17 % → 10 % | 0.10 | 0.60 | 300 |
| pressure swell | 12 % → 8 % | 0.10 | 0.68 | 169 |
| fast wave | 39 % → 11 % | 0.10 | 0.29 | 573 |
| slow wave | 39 % → 12 % | 0.10 | 0.31 | 952 |
| spiral | 58 % → 13 % | 0.10 | 0.23 | 960 |
| loop | 34 % → 13 % | 0.10 | 0.39 | 543 |
| tilted | 14 % → 14 % | 0.10 | 1.01 | 264 |
| over the wet one | 29 % → 20 % | 0.10 | 0.69 | 303 |
| long, no reload | 68 % → 16 % | 0.10 | 0.23 | 1547 | quarters: 0.08 → 0.04 → 0.01 → 0.00

Numbers say: pressure barely changes the width.

## Brush Artist · Refs · #05 Henry Ward green in rust loops
Heavy acrylic · 20 px · 18.5 s

![Brush Artist · Refs · #05 Henry Ward green in rust loops](Brush-Artist-Refs-05-Henry-Ward-green-in-rust-loops.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 7 % → 6 % | 0.55 | 0.94 | 95 |
| heavy line | 7 % → 7 % | 0.55 | 0.94 | 89 |
| pressure swell | 6 % → 5 % | 0.57 | 0.92 | 65 |
| fast wave | 17 % → 11 % | 0.56 | 0.64 | 237 |
| slow wave | 18 % → 12 % | 0.56 | 0.66 | 357 |
| spiral | 27 % → 11 % | 0.55 | 0.42 | 440 |
| loop | 15 % → 12 % | 0.55 | 0.79 | 238 |
| tilted | 8 % → 8 % | 0.56 | 1.00 | 145 |
| over the wet one | 15 % → 13 % | 0.56 | 0.87 | 123 |
| long, no reload | 30 % → 12 % | 0.56 | 0.39 | 656 | quarters: 0.25 → 0.18 → 0.10 → 0.02

Numbers say: pressure barely changes the width.

## Brush Artist · Refs · #06 Henry Ward scrubbed grey
Gouache · 50 px · 39.7 s

![Brush Artist · Refs · #06 Henry Ward scrubbed grey](Brush-Artist-Refs-06-Henry-Ward-scrubbed-grey.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 15 % → 6 % | 0.09 | 0.42 | 220 |
| heavy line | 17 % → 10 % | 0.09 | 0.60 | 208 |
| pressure swell | 12 % → 8 % | 0.09 | 0.68 | 154 |
| fast wave | 39 % → 11 % | 0.09 | 0.29 | 615 |
| slow wave | 39 % → 12 % | 0.09 | 0.31 | 1106 |
| spiral | 58 % → 13 % | 0.09 | 0.23 | 1368 |
| loop | 34 % → 13 % | 0.09 | 0.39 | 423 |
| tilted | 14 % → 14 % | 0.09 | 1.01 | 262 |
| over the wet one | 29 % → 20 % | 0.09 | 0.69 | 192 |
| long, no reload | 68 % → 16 % | 0.09 | 0.23 | 1317 | quarters: 0.06 → 0.04 → 0.01 → 0.00

Numbers say: pressure barely changes the width.

## Brush Artist · Refs · #07 Henry Ward blue L + black zigzag
Heavy acrylic · 34 px · 22.0 s

![Brush Artist · Refs · #07 Henry Ward blue L + black zigzag](Brush-Artist-Refs-07-Henry-Ward-blue-L-black-zigzag.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 11 % → 11 % | 0.57 | 0.93 | 116 |
| heavy line | 12 % → 12 % | 0.57 | 0.93 | 197 |
| pressure swell | 9 % → 9 % | 0.59 | 0.94 | 143 |
| fast wave | 29 % → 20 % | 0.59 | 0.68 | 502 |
| slow wave | 30 % → 21 % | 0.58 | 0.72 | 747 |
| spiral | 47 % → 22 % | 0.58 | 0.46 | 590 |
| loop | 25 % → 21 % | 0.58 | 0.82 | 258 |
| tilted | 11 % → 11 % | 0.58 | 1.00 | 168 |
| over the wet one | 22 % → 20 % | 0.58 | 0.91 | 122 |
| long, no reload | 53 % → 22 % | 0.59 | 0.42 | 741 | quarters: 0.40 → 0.32 → 0.21 → 0.10

Numbers say: pressure barely changes the width.

## Brush Artist · Refs · #08 Henry Ward olive bands
Gouache · 34 px · 33.5 s

![Brush Artist · Refs · #08 Henry Ward olive bands](Brush-Artist-Refs-08-Henry-Ward-olive-bands.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 9 % → 2 % | 0.57 | 0.29 | 89 |
| heavy line | 12 % → 3 % | 0.57 | 0.23 | 157 |
| pressure swell | 8 % → 3 % | 0.57 | 0.39 | 110 |
| fast wave | 26 % → 4 % | 0.57 | 0.16 | 349 |
| slow wave | 25 % → 4 % | 0.57 | 0.16 | 598 |
| spiral | 39 % → 4 % | 0.57 | 0.10 | 605 |
| loop | 22 % → 5 % | 0.57 | 0.21 | 325 |
| tilted | 10 % → 10 % | 0.57 | 0.98 | 171 |
| over the wet one | 21 % → 8 % | 0.57 | 0.41 | 159 |
| long, no reload | 44 % → 6 % | 0.57 | 0.13 | 1152 | quarters: 0.35 → 0.26 → 0.16 → 0.07

## Brush Artist · Refs · #09 Henry Ward white loops
Gouache · 46 px · 40.7 s

![Brush Artist · Refs · #09 Henry Ward white loops](Brush-Artist-Refs-09-Henry-Ward-white-loops.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 13 % → 6 % | 0.01 | 0.46 | 185 |
| heavy line | 14 % → 9 % | 0.01 | 0.64 | 214 |
| pressure swell | 11 % → 8 % | 0.01 | 0.72 | 143 |
| fast wave | 34 % → 10 % | 0.01 | 0.30 | 496 |
| slow wave | 34 % → 11 % | 0.01 | 0.31 | 1120 |
| spiral | 55 % → 12 % | 0.01 | 0.21 | 1040 |
| loop | 30 % → 12 % | 0.01 | 0.39 | 533 |
| tilted | 13 % → 13 % | 0.01 | 1.00 | 267 |
| over the wet one | 26 % → 18 % | 0.01 | 0.69 | 208 |
| long, no reload | 62 % → 14 % | 0.02 | 0.23 | 1340 | quarters: 0.01 → 0.02 → 0.00 → 0.00

Numbers say: pressure barely changes the width.

## Brush Artist · Refs · #10 Henry Ward maroon loops
Heavy acrylic · 30 px · 23.2 s

![Brush Artist · Refs · #10 Henry Ward maroon loops](Brush-Artist-Refs-10-Henry-Ward-maroon-loops.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 10 % → 9 % | 0.69 | 0.94 | 132 |
| heavy line | 10 % → 10 % | 0.69 | 0.95 | 117 |
| pressure swell | 8 % → 8 % | 0.73 | 0.94 | 95 |
| fast wave | 25 % → 17 % | 0.73 | 0.70 | 282 |
| slow wave | 25 % → 18 % | 0.72 | 0.73 | 476 |
| spiral | 39 % → 18 % | 0.72 | 0.47 | 600 |
| loop | 21 % → 18 % | 0.72 | 0.85 | 265 |
| tilted | 10 % → 10 % | 0.72 | 1.00 | 150 |
| over the wet one | 20 % → 18 % | 0.72 | 0.91 | 178 |
| long, no reload | 46 % → 18 % | 0.73 | 0.40 | 1082 | quarters: 0.44 → 0.38 → 0.31 → 0.22

Numbers say: pressure barely changes the width.

## Brush Artist · Refs · #11 Henry Ward purple spun balls
Heavy acrylic · 36 px · 23.7 s

![Brush Artist · Refs · #11 Henry Ward purple spun balls](Brush-Artist-Refs-11-Henry-Ward-purple-spun-balls.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 12 % → 11 % | 0.70 | 0.96 | 142 |
| heavy line | 13 % → 12 % | 0.70 | 0.96 | 147 |
| pressure swell | 10 % → 9 % | 0.74 | 0.95 | 121 |
| fast wave | 30 % → 22 % | 0.73 | 0.75 | 385 |
| slow wave | 30 % → 24 % | 0.73 | 0.79 | 995 |
| spiral | 49 % → 24 % | 0.73 | 0.50 | 900 |
| loop | 26 % → 23 % | 0.73 | 0.88 | 356 |
| tilted | 11 % → 11 % | 0.72 | 1.00 | 185 |
| over the wet one | 23 % → 21 % | 0.72 | 0.93 | 152 |
| long, no reload | 55 % → 24 % | 0.73 | 0.44 | 910 | quarters: 0.51 → 0.46 → 0.39 → 0.28

Numbers say: pressure barely changes the width.

## Brush Artist · Refs · #12 Henry Ward black-olive cage
Gouache · 28 px · 31.2 s

![Brush Artist · Refs · #12 Henry Ward black-olive cage](Brush-Artist-Refs-12-Henry-Ward-black-olive-cage.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 7 % → 3 % | 0.62 | 0.37 | 95 |
| heavy line | 9 % → 4 % | 0.62 | 0.43 | 150 |
| pressure swell | 6 % → 4 % | 0.62 | 0.62 | 93 |
| fast wave | 21 % → 4 % | 0.62 | 0.21 | 279 |
| slow wave | 20 % → 4 % | 0.62 | 0.22 | 511 |
| spiral | 32 % → 5 % | 0.62 | 0.14 | 521 |
| loop | 18 % → 5 % | 0.62 | 0.29 | 250 |
| tilted | 9 % → 9 % | 0.62 | 0.98 | 189 |
| over the wet one | 17 % → 8 % | 0.62 | 0.47 | 150 |
| long, no reload | 39 % → 6 % | 0.62 | 0.15 | 831 | quarters: 0.32 → 0.26 → 0.19 → 0.09

## Brush Artist · Refs · #13 Henry Ward blue streaky form
Gouache · 50 px · 40.3 s

![Brush Artist · Refs · #13 Henry Ward blue streaky form](Brush-Artist-Refs-13-Henry-Ward-blue-streaky-form.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 15 % → 6 % | 0.09 | 0.42 | 219 |
| heavy line | 17 % → 10 % | 0.09 | 0.60 | 268 |
| pressure swell | 12 % → 8 % | 0.09 | 0.68 | 162 |
| fast wave | 39 % → 11 % | 0.09 | 0.29 | 875 |
| slow wave | 39 % → 12 % | 0.09 | 0.31 | 1134 |
| spiral | 58 % → 13 % | 0.09 | 0.23 | 1011 |
| loop | 34 % → 13 % | 0.09 | 0.39 | 542 |
| tilted | 14 % → 14 % | 0.09 | 1.01 | 288 |
| over the wet one | 29 % → 20 % | 0.09 | 0.69 | 228 |
| long, no reload | 68 % → 16 % | 0.09 | 0.23 | 1439 | quarters: 0.07 → 0.04 → 0.01 → 0.00

Numbers say: pressure barely changes the width.

## Brush Artist · Refs · #14 Henry Ward olive totem
Heavy acrylic · 48 px · 27.0 s

![Brush Artist · Refs · #14 Henry Ward olive totem](Brush-Artist-Refs-14-Henry-Ward-olive-totem.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 15 % → 15 % | 0.31 | 0.95 | 187 |
| heavy line | 16 % → 16 % | 0.31 | 0.95 | 206 |
| pressure swell | 13 % → 12 % | 0.32 | 0.95 | 160 |
| fast wave | 38 % → 30 % | 0.30 | 0.78 | 528 |
| slow wave | 39 % → 31 % | 0.30 | 0.81 | 855 |
| spiral | 58 % → 32 % | 0.30 | 0.55 | 1197 |
| loop | 33 % → 29 % | 0.30 | 0.89 | 611 |
| tilted | 13 % → 13 % | 0.31 | 1.00 | 236 |
| over the wet one | 28 % → 26 % | 0.31 | 0.93 | 207 |
| long, no reload | 67 % → 33 % | 0.30 | 0.49 | 1224 | quarters: 0.26 → 0.18 → 0.09 → 0.03

Numbers say: pressure barely changes the width.

## Brush Artist · Refs · #15 Ultramarine brush script
Ink · 10 px · 35.5 s

![Brush Artist · Refs · #15 Ultramarine brush script](Brush-Artist-Refs-15-Ultramarine-brush-script.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 2 % → 5 % | 0.53 | 2.65 | 73 |
| heavy line | 10 % → 10 % | 0.66 | 1.00 | 117 |
| pressure swell | 6 % → 6 % | 0.68 | 1.12 | 74 |
| fast wave | 18 % → 17 % | 0.59 | 0.95 | 233 |
| slow wave | 14 % → 14 % | 0.59 | 1.00 | 290 |
| spiral | 22 % → 18 % | 0.54 | 0.81 | 454 |
| loop | 13 % → 14 % | 0.61 | 1.02 | 199 |
| tilted | 6 % → 6 % | 0.68 | 1.01 | 93 |
| over the wet one | 13 % → 14 % | 0.68 | 1.04 | 88 |
| long, no reload | 33 % → 19 % | 0.52 | 0.59 | 488 | quarters: 0.30 → 0.13 → 0.05 → 0.02

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #18 Blue oil-stick scribbles
Pastel · 10 px · 14.9 s

![Brush Artist · Refs · #18 Blue oil-stick scribbles](Brush-Artist-Refs-18-Blue-oil-stick-scribbles.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 2 % → 2 % | 0.50 | 1.00 | 39 |
| heavy line | 3 % → 3 % | 0.51 | 1.00 | 46 |
| pressure swell | 2 % → 2 % | 0.51 | 1.00 | 40 |
| fast wave | 6 % → 6 % | 0.52 | 1.00 | 102 |
| slow wave | 6 % → 6 % | 0.51 | 1.00 | 83 |
| spiral | 10 % → 10 % | 0.52 | 1.00 | 156 |
| loop | 5 % → 5 % | 0.51 | 1.00 | 75 |
| tilted | 2 % → 2 % | 0.51 | 1.00 | 31 |
| over the wet one | 5 % → 5 % | 0.51 | 1.00 | 56 |
| long, no reload | 14 % → 14 % | 0.52 | 1.00 | 312 | quarters: 0.08 → 0.08 → 0.08 → 0.08

Numbers say: the long stroke does not run out of paint.

## Brush Artist · Refs · #20 Orange-red crayon scribble
Pastel · 14 px · 15.8 s

![Brush Artist · Refs · #20 Orange-red crayon scribble](Brush-Artist-Refs-20-Orange-red-crayon-scribble.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 3 % → 3 % | 0.53 | 1.00 | 33 |
| heavy line | 4 % → 4 % | 0.53 | 1.00 | 42 |
| pressure swell | 3 % → 3 % | 0.53 | 1.00 | 19 |
| fast wave | 9 % → 9 % | 0.53 | 1.00 | 93 |
| slow wave | 9 % → 9 % | 0.53 | 1.00 | 135 |
| spiral | 14 % → 14 % | 0.53 | 1.00 | 191 |
| loop | 7 % → 7 % | 0.53 | 1.00 | 82 |
| tilted | 3 % → 3 % | 0.53 | 1.00 | 90 |
| over the wet one | 7 % → 7 % | 0.53 | 1.00 | 64 |
| long, no reload | 18 % → 18 % | 0.53 | 1.00 | 241 | quarters: 0.11 → 0.11 → 0.11 → 0.11

Numbers say: the long stroke does not run out of paint.

## Brush Artist · Refs · #21 Gritty black contours
Gouache · 12 px · 28.4 s

![Brush Artist · Refs · #21 Gritty black contours](Brush-Artist-Refs-21-Gritty-black-contours.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 3 % → 0 % | 0.79 | 0.14 | 136 |
| heavy line | 4 % → 0 % | 0.79 | 0.10 | 221 |
| pressure swell | 3 % → 0 % | 0.79 | 0.16 | 134 |
| fast wave | 7 % → 1 % | 0.79 | 0.10 | 414 |
| slow wave | 8 % → 1 % | 0.79 | 0.09 | 306 |
| spiral | 9 % → 1 % | 0.79 | 0.10 | 589 |
| loop | 8 % → 1 % | 0.79 | 0.09 | 262 |
| tilted | 4 % → 4 % | 0.79 | 0.91 | 130 |
| over the wet one | 7 % → 1 % | 0.79 | 0.18 | 121 |
| long, no reload | 7 % → 1 % | 0.79 | 0.12 | 684 | quarters: 0.20 → 0.07 → 0.00 → 0.00

## Brush Artist · Refs · #22 Bold black brush poster
Ink · 20 px · 36.0 s

![Brush Artist · Refs · #22 Bold black brush poster](Brush-Artist-Refs-22-Bold-black-brush-poster.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 3 % → 5 % | 0.79 | 1.63 | 90 |
| heavy line | 15 % → 15 % | 0.88 | 0.99 | 189 |
| pressure swell | 9 % → 9 % | 0.87 | 1.04 | 55 |
| fast wave | 27 % → 27 % | 0.87 | 0.98 | 223 |
| slow wave | 22 % → 22 % | 0.87 | 0.98 | 334 |
| spiral | 34 % → 32 % | 0.87 | 0.94 | 355 |
| loop | 20 % → 20 % | 0.88 | 1.00 | 181 |
| tilted | 8 % → 8 % | 0.88 | 1.01 | 77 |
| over the wet one | 19 % → 19 % | 0.88 | 1.00 | 81 |
| long, no reload | 45 % → 38 % | 0.86 | 0.83 | 484 | quarters: 0.54 → 0.45 → 0.35 → 0.26

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #23 Dry white on orange + black line
Gouache · 50 px · 32.9 s

![Brush Artist · Refs · #23 Dry white on orange + black line](Brush-Artist-Refs-23-Dry-white-on-orange-black-line.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 12 % → 2 % | 0.00 | 0.16 | 137 |
| heavy line | 16 % → 2 % | 0.00 | 0.12 | 315 |
| pressure swell | 11 % → 2 % | 0.00 | 0.20 | 159 |
| fast wave | 35 % → 3 % | 0.00 | 0.10 | 532 |
| slow wave | 34 % → 4 % | 0.00 | 0.11 | 879 |
| spiral | 49 % → 4 % | 0.00 | 0.08 | 1259 |
| loop | 30 % → 4 % | 0.00 | 0.13 | 474 |
| tilted | 13 % → 13 % | 0.00 | 0.98 | 256 |
| over the wet one | 26 % → 8 % | 0.00 | 0.29 | 210 |
| long, no reload | 58 % → 5 % | 0.00 | 0.09 | 1334 | quarters: 0.01 → 0.01 → 0.00 → 0.00

## Brush Artist · Refs · #24 Picasso flat oil
Oil · 34 px · 27.9 s

![Brush Artist · Refs · #24 Picasso flat oil](Brush-Artist-Refs-24-Picasso-flat-oil.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 11 % → 11 % | 0.39 | 1.00 | 197 |
| heavy line | 12 % → 12 % | 0.39 | 1.00 | 234 |
| pressure swell | 9 % → 9 % | 0.41 | 1.00 | 160 |
| fast wave | 29 % → 29 % | 0.38 | 1.00 | 433 |
| slow wave | 29 % → 29 % | 0.38 | 1.00 | 742 |
| spiral | 49 % → 49 % | 0.32 | 1.00 | 754 |
| loop | 25 % → 25 % | 0.39 | 1.00 | 360 |
| tilted | 11 % → 11 % | 0.39 | 1.00 | 194 |
| over the wet one | 22 % → 22 % | 0.39 | 1.00 | 175 |
| long, no reload | 58 % → 58 % | 0.29 | 1.00 | 989 | quarters: 0.28 → 0.23 → 0.15 → 0.08

Numbers say: pressure barely changes the width.

## Brush Artist · Refs · #25 Yellow heavy flat stroke
Heavy acrylic · 110 px · 51.5 s

![Brush Artist · Refs · #25 Yellow heavy flat stroke](Brush-Artist-Refs-25-Yellow-heavy-flat-stroke.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 35 % → 36 % | 0.17 | 1.02 | 544 |
| heavy line | 36 % → 35 % | 0.17 | 0.97 | 516 |
| pressure swell | 28 % → 29 % | 0.17 | 1.04 | 511 |
| fast wave | 73 % → 76 % | 0.17 | 1.05 | 1714 |
| slow wave | 73 % → 72 % | 0.18 | 0.98 | 2668 |
| spiral | 86 % → 83 % | 0.17 | 0.97 | 2474 |
| loop | 65 % → 64 % | 0.17 | 0.99 | 1450 |
| tilted | 26 % → 26 % | 0.17 | 1.00 | 972 |
| over the wet one | 55 % → 54 % | 0.17 | 0.97 | 786 |
| long, no reload | 98 % → 97 % | 0.17 | 0.99 | 3683 | quarters: 0.18 → 0.17 → 0.17 → 0.16

Numbers say: pressure barely changes the width; the long stroke does not run out of paint.

## Brush Artist · Refs · #27 Orange impasto swatch
Heavy acrylic · 60 px · 35.1 s

![Brush Artist · Refs · #27 Orange impasto swatch](Brush-Artist-Refs-27-Orange-impasto-swatch.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 20 % → 19 % | 0.35 | 0.97 | 347 |
| heavy line | 20 % → 20 % | 0.35 | 0.97 | 318 |
| pressure swell | 16 % → 15 % | 0.36 | 0.97 | 178 |
| fast wave | 48 % → 47 % | 0.35 | 0.98 | 804 |
| slow wave | 48 % → 47 % | 0.36 | 0.98 | 1142 |
| spiral | 69 % → 62 % | 0.35 | 0.91 | 1160 |
| loop | 42 % → 40 % | 0.35 | 0.97 | 589 |
| tilted | 16 % → 16 % | 0.36 | 1.00 | 338 |
| over the wet one | 34 % → 33 % | 0.36 | 0.97 | 298 |
| long, no reload | 85 % → 75 % | 0.35 | 0.88 | 2175 | quarters: 0.33 → 0.31 → 0.30 → 0.26

Numbers say: pressure barely changes the width.

## Brush Artist · Refs · #28 Miles Davis black lines
Ink · 22 px · 38.8 s

![Brush Artist · Refs · #28 Miles Davis black lines](Brush-Artist-Refs-28-Miles-Davis-black-lines.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 4 % → 6 % | 0.81 | 1.49 | 65 |
| heavy line | 17 % → 17 % | 0.88 | 0.99 | 132 |
| pressure swell | 10 % → 10 % | 0.87 | 1.03 | 62 |
| fast wave | 31 % → 30 % | 0.87 | 0.98 | 223 |
| slow wave | 25 % → 25 % | 0.87 | 0.99 | 342 |
| spiral | 39 % → 37 % | 0.87 | 0.95 | 345 |
| loop | 23 % → 23 % | 0.88 | 1.00 | 165 |
| tilted | 9 % → 9 % | 0.88 | 1.01 | 91 |
| over the wet one | 21 % → 21 % | 0.88 | 1.00 | 87 |
| long, no reload | 51 % → 43 % | 0.86 | 0.84 | 501 | quarters: 0.59 → 0.51 → 0.40 → 0.31

## Brush Artist · Refs · #29 Shrigley magenta asterisk
Watercolor · 70 px · 45.6 s

![Brush Artist · Refs · #29 Shrigley magenta asterisk](Brush-Artist-Refs-29-Shrigley-magenta-asterisk.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 10 % → 14 % | 0.51 | 1.41 | 64 |
| heavy line | 17 % → 18 % | 0.51 | 1.05 | 207 |
| pressure swell | 11 % → 13 % | 0.51 | 1.15 | 108 |
| fast wave | 38 % → 39 % | 0.51 | 1.02 | 503 |
| slow wave | 36 % → 40 % | 0.51 | 1.12 | 908 |
| spiral | 61 % → 61 % | 0.51 | 1.01 | 547 |
| loop | 31 % → 32 % | 0.51 | 1.05 | 303 |
| tilted | 18 % → 18 % | 0.51 | 1.01 | 272 |
| over the wet one | 32 % → 35 % | 0.51 | 1.09 | 173 |
| long, no reload | 75 % → 76 % | 0.50 | 1.02 | 961 | quarters: 0.44 → 0.42 → 0.41 → 0.38

Numbers say: the long stroke does not run out of paint.

## Brush Artist · Refs · #30 Red gouache face patch
Gouache · 60 px · 52.9 s

![Brush Artist · Refs · #30 Red gouache face patch](Brush-Artist-Refs-30-Red-gouache-face-patch.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 16 % → 15 % | 0.49 | 0.91 | 189 |
| heavy line | 25 % → 20 % | 0.49 | 0.80 | 301 |
| pressure swell | 19 % → 17 % | 0.49 | 0.86 | 246 |
| fast wave | 49 % → 28 % | 0.49 | 0.58 | 648 |
| slow wave | 48 % → 28 % | 0.49 | 0.59 | 1247 |
| spiral | 60 % → 28 % | 0.49 | 0.47 | 976 |
| loop | 40 % → 29 % | 0.49 | 0.74 | 542 |
| tilted | 16 % → 17 % | 0.49 | 1.00 | 335 |
| over the wet one | 36 % → 32 % | 0.49 | 0.89 | 338 |
| long, no reload | 67 % → 30 % | 0.49 | 0.44 | 1353 | quarters: 0.43 → 0.39 → 0.32 → 0.26

## Brush Artist · Refs · #31 Warhol blotted line
Ink · 6 px · 29.3 s

![Brush Artist · Refs · #31 Warhol blotted line](Brush-Artist-Refs-31-Warhol-blotted-line.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 1 % → 3 % | 0.75 | 3.30 | 38 |
| heavy line | 7 % → 7 % | 0.83 | 0.98 | 93 |
| pressure swell | 4 % → 4 % | 0.84 | 1.12 | 52 |
| fast wave | 12 % → 9 % | 0.82 | 0.76 | 194 |
| slow wave | 10 % → 8 % | 0.80 | 0.84 | 143 |
| spiral | 15 % → 8 % | 0.80 | 0.57 | 257 |
| loop | 9 % → 9 % | 0.80 | 0.93 | 108 |
| tilted | 3 % → 3 % | 0.84 | 1.03 | 48 |
| over the wet one | 8 % → 8 % | 0.84 | 1.02 | 59 |
| long, no reload | 21 % → 9 % | 0.78 | 0.43 | 393 | quarters: 0.25 → 0.13 → 0.05 → 0.01

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #32 Thick orange swipes
Heavy acrylic · 90 px · 45.2 s

![Brush Artist · Refs · #32 Thick orange swipes](Brush-Artist-Refs-32-Thick-orange-swipes.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 29 % → 29 % | 0.38 | 1.00 | 390 |
| heavy line | 30 % → 29 % | 0.38 | 0.97 | 423 |
| pressure swell | 23 % → 23 % | 0.38 | 1.01 | 312 |
| fast wave | 63 % → 65 % | 0.38 | 1.03 | 1031 |
| slow wave | 64 % → 63 % | 0.39 | 0.98 | 1833 |
| spiral | 79 % → 77 % | 0.38 | 0.98 | 1721 |
| loop | 57 % → 56 % | 0.38 | 0.99 | 1235 |
| tilted | 21 % → 21 % | 0.38 | 1.00 | 454 |
| over the wet one | 47 % → 45 % | 0.38 | 0.97 | 439 |
| long, no reload | 95 % → 93 % | 0.38 | 0.98 | 2612 | quarters: 0.38 → 0.38 → 0.37 → 0.35

Numbers say: pressure barely changes the width; the long stroke does not run out of paint.

## Brush Artist · Refs · #33 Red wet-in-wet band
Watercolor · 80 px · 56.8 s

![Brush Artist · Refs · #33 Red wet-in-wet band](Brush-Artist-Refs-33-Red-wet-in-wet-band.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 22 % → 23 % | 0.55 | 1.02 | 172 |
| heavy line | 34 % → 34 % | 0.54 | 0.99 | 296 |
| pressure swell | 22 % → 23 % | 0.55 | 1.04 | 186 |
| fast wave | 65 % → 68 % | 0.54 | 1.04 | 578 |
| slow wave | 63 % → 63 % | 0.57 | 1.00 | 888 |
| spiral | 77 % → 77 % | 0.56 | 1.00 | 1454 |
| loop | 54 % → 55 % | 0.56 | 1.01 | 507 |
| tilted | 24 % → 24 % | 0.55 | 1.01 | 341 |
| over the wet one | 49 % → 53 % | 0.55 | 1.07 | 200 |
| long, no reload | 96 % → 97 % | 0.56 | 1.00 | 1988 | quarters: 0.58 → 0.57 → 0.56 → 0.51

Numbers say: the long stroke does not run out of paint.

## Brush Artist · Refs · #34 Magenta oil patches
Oil · 60 px · 33.2 s

![Brush Artist · Refs · #34 Magenta oil patches](Brush-Artist-Refs-34-Magenta-oil-patches.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 19 % → 19 % | 0.58 | 1.00 | 267 |
| heavy line | 20 % → 20 % | 0.59 | 1.00 | 423 |
| pressure swell | 15 % → 15 % | 0.62 | 1.01 | 319 |
| fast wave | 46 % → 47 % | 0.61 | 1.02 | 1054 |
| slow wave | 47 % → 47 % | 0.61 | 1.00 | 1254 |
| spiral | 69 % → 69 % | 0.59 | 1.00 | 1324 |
| loop | 41 % → 41 % | 0.61 | 1.00 | 665 |
| tilted | 17 % → 17 % | 0.61 | 1.00 | 358 |
| over the wet one | 34 % → 34 % | 0.61 | 1.00 | 390 |
| long, no reload | 84 % → 84 % | 0.59 | 1.00 | 1978 | quarters: 0.58 → 0.55 → 0.51 → 0.45

Numbers say: pressure barely changes the width.

## Brush Artist · Refs · #35 Red band with runs
Watercolor · 70 px · 52.9 s

![Brush Artist · Refs · #35 Red band with runs](Brush-Artist-Refs-35-Red-band-with-runs.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 20 % → 21 % | 0.52 | 1.07 | 143 |
| heavy line | 30 % → 30 % | 0.51 | 0.98 | 298 |
| pressure swell | 20 % → 20 % | 0.54 | 1.04 | 147 |
| fast wave | 60 % → 60 % | 0.52 | 1.01 | 679 |
| slow wave | 58 % → 58 % | 0.55 | 1.01 | 807 |
| spiral | 74 % → 74 % | 0.54 | 1.00 | 836 |
| loop | 50 % → 51 % | 0.54 | 1.02 | 394 |
| tilted | 21 % → 21 % | 0.53 | 1.00 | 283 |
| over the wet one | 44 % → 48 % | 0.53 | 1.08 | 180 |
| long, no reload | 94 % → 94 % | 0.54 | 1.00 | 1107 | quarters: 0.55 → 0.55 → 0.53 → 0.49

Numbers say: the long stroke does not run out of paint.

## Brush Artist · Refs · #36 Magenta letters flat brush
Gouache · 36 px · 46.3 s

![Brush Artist · Refs · #36 Magenta letters flat brush](Brush-Artist-Refs-36-Magenta-letters-flat-brush.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 10 % → 10 % | 0.45 | 0.98 | 113 |
| heavy line | 17 % → 14 % | 0.45 | 0.85 | 141 |
| pressure swell | 13 % → 12 % | 0.45 | 0.89 | 90 |
| fast wave | 35 % → 19 % | 0.45 | 0.54 | 362 |
| slow wave | 35 % → 19 % | 0.45 | 0.54 | 515 |
| spiral | 46 % → 19 % | 0.45 | 0.42 | 665 |
| loop | 27 % → 20 % | 0.45 | 0.72 | 286 |
| tilted | 11 % → 11 % | 0.45 | 1.00 | 138 |
| over the wet one | 24 % → 23 % | 0.45 | 0.92 | 180 |
| long, no reload | 47 % → 19 % | 0.45 | 0.40 | 708 | quarters: 0.29 → 0.26 → 0.22 → 0.18

## Brush Artist · Refs · #37 Oil still life dabs
Oil · 40 px · 29.2 s

![Brush Artist · Refs · #37 Oil still life dabs](Brush-Artist-Refs-37-Oil-still-life-dabs.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 13 % → 13 % | 0.37 | 1.00 | 163 |
| heavy line | 14 % → 14 % | 0.37 | 1.00 | 176 |
| pressure swell | 11 % → 11 % | 0.39 | 1.00 | 159 |
| fast wave | 34 % → 34 % | 0.35 | 1.00 | 720 |
| slow wave | 34 % → 34 % | 0.36 | 1.00 | 1136 |
| spiral | 56 % → 56 % | 0.29 | 1.00 | 831 |
| loop | 29 % → 29 % | 0.37 | 1.00 | 516 |
| tilted | 13 % → 13 % | 0.38 | 1.00 | 230 |
| over the wet one | 25 % → 25 % | 0.38 | 1.00 | 173 |
| long, no reload | 64 % → 64 % | 0.26 | 1.00 | 1183 | quarters: 0.30 → 0.23 → 0.14 → 0.07

Numbers say: pressure barely changes the width.

## Brush Artist · Refs · #38 Sanguine drawing
Pastel · 6 px · 14.8 s

![Brush Artist · Refs · #38 Sanguine drawing](Brush-Artist-Refs-38-Sanguine-drawing.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 1 % → 1 % | 0.60 | 1.00 | 66 |
| heavy line | 2 % → 2 % | 0.61 | 1.00 | 40 |
| pressure swell | 1 % → 1 % | 0.61 | 1.00 | 30 |
| fast wave | 4 % → 4 % | 0.61 | 1.00 | 116 |
| slow wave | 4 % → 4 % | 0.61 | 1.00 | 101 |
| spiral | 7 % → 7 % | 0.61 | 1.00 | 145 |
| loop | 4 % → 4 % | 0.61 | 1.00 | 48 |
| tilted | 2 % → 2 % | 0.60 | 1.00 | 24 |
| over the wet one | 3 % → 3 % | 0.60 | 1.00 | 23 |
| long, no reload | 10 % → 10 % | 0.61 | 1.00 | 145 | quarters: 0.07 → 0.07 → 0.07 → 0.07

Numbers say: the long stroke does not run out of paint.

## Brush Artist · Refs · #39 Very thick impasto
Heavy acrylic · 60 px · 36.9 s

![Brush Artist · Refs · #39 Very thick impasto](Brush-Artist-Refs-39-Very-thick-impasto.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 20 % → 19 % | 0.61 | 0.97 | 235 |
| heavy line | 20 % → 20 % | 0.61 | 0.97 | 261 |
| pressure swell | 16 % → 15 % | 0.62 | 0.97 | 248 |
| fast wave | 48 % → 47 % | 0.62 | 0.98 | 824 |
| slow wave | 48 % → 47 % | 0.62 | 0.98 | 1230 |
| spiral | 69 % → 65 % | 0.62 | 0.93 | 1057 |
| loop | 42 % → 41 % | 0.62 | 0.97 | 516 |
| tilted | 16 % → 16 % | 0.62 | 1.00 | 300 |
| over the wet one | 34 % → 33 % | 0.62 | 0.97 | 278 |
| long, no reload | 85 % → 79 % | 0.62 | 0.93 | 1587 | quarters: 0.58 → 0.57 → 0.55 → 0.52

Numbers say: pressure barely changes the width; the long stroke does not run out of paint.

## Brush Artist · Refs · #40 Watercolour blooms
Watercolor · 90 px · 57.3 s

![Brush Artist · Refs · #40 Watercolour blooms](Brush-Artist-Refs-40-Watercolour-blooms.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 26 % → 27 % | 0.23 | 1.05 | 305 |
| heavy line | 38 % → 38 % | 0.22 | 0.99 | 373 |
| pressure swell | 25 % → 27 % | 0.24 | 1.06 | 228 |
| fast wave | 70 % → 74 % | 0.22 | 1.05 | 700 |
| slow wave | 68 % → 68 % | 0.30 | 1.00 | 1213 |
| spiral | 80 % → 80 % | 0.28 | 1.01 | 1139 |
| loop | 59 % → 59 % | 0.26 | 1.01 | 599 |
| tilted | 27 % → 27 % | 0.27 | 1.00 | 586 |
| over the wet one | 55 % → 59 % | 0.27 | 1.07 | 441 |
| long, no reload | 98 % → 98 % | 0.29 | 1.01 | 1915 | quarters: 0.34 → 0.33 → 0.29 → 0.22

## Brush Artist · Refs · #41 Coloured pencil hatching
Pastel · 4 px · 12.7 s

![Brush Artist · Refs · #41 Coloured pencil hatching](Brush-Artist-Refs-41-Coloured-pencil-hatching.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 1 % → 1 % | 0.42 | 1.00 | 15 |
| heavy line | 2 % → 2 % | 0.43 | 1.00 | 13 |
| pressure swell | 1 % → 1 % | 0.43 | 1.00 | 11 |
| fast wave | 3 % → 3 % | 0.43 | 1.00 | 42 |
| slow wave | 3 % → 3 % | 0.42 | 1.00 | 47 |
| spiral | 5 % → 5 % | 0.43 | 1.00 | 80 |
| loop | 3 % → 3 % | 0.43 | 1.00 | 34 |
| tilted | 2 % → 2 % | 0.42 | 1.00 | 21 |
| over the wet one | 3 % → 3 % | 0.42 | 1.00 | 21 |
| long, no reload | 8 % → 8 % | 0.43 | 1.00 | 113 | quarters: 0.04 → 0.04 → 0.04 → 0.04

Numbers say: the long stroke does not run out of paint.

## Brush Artist · Refs · #42 Oil pastel shaggy
Pastel · 18 px · 14.0 s

![Brush Artist · Refs · #42 Oil pastel shaggy](Brush-Artist-Refs-42-Oil-pastel-shaggy.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 3 % → 3 % | 0.07 | 1.00 | 27 |
| heavy line | 5 % → 5 % | 0.07 | 1.00 | 55 |
| pressure swell | 4 % → 4 % | 0.07 | 1.00 | 25 |
| fast wave | 11 % → 11 % | 0.07 | 1.00 | 107 |
| slow wave | 10 % → 10 % | 0.07 | 1.00 | 144 |
| spiral | 17 % → 17 % | 0.07 | 1.00 | 148 |
| loop | 9 % → 9 % | 0.07 | 1.00 | 96 |
| tilted | 4 % → 4 % | 0.07 | 1.00 | 35 |
| over the wet one | 8 % → 8 % | 0.07 | 1.00 | 38 |
| long, no reload | 21 % → 21 % | 0.07 | 1.00 | 241 | quarters: 0.02 → 0.02 → 0.02 → 0.02

Numbers say: the long stroke does not run out of paint.

## Brush Artist · Refs · #43 Dragged black ink blocks
Gouache · 70 px · 41.7 s

![Brush Artist · Refs · #43 Dragged black ink blocks](Brush-Artist-Refs-43-Dragged-black-ink-blocks.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 19 % → 6 % | 0.57 | 0.32 | 300 |
| heavy line | 24 % → 9 % | 0.57 | 0.39 | 434 |
| pressure swell | 17 % → 9 % | 0.57 | 0.55 | 311 |
| fast wave | 52 % → 12 % | 0.57 | 0.23 | 896 |
| slow wave | 50 % → 10 % | 0.57 | 0.21 | 1570 |
| spiral | 64 % → 15 % | 0.57 | 0.23 | 1572 |
| loop | 45 % → 13 % | 0.57 | 0.29 | 577 |
| tilted | 17 % → 17 % | 0.57 | 0.98 | 302 |
| over the wet one | 37 % → 21 % | 0.57 | 0.57 | 248 |
| long, no reload | 82 % → 17 % | 0.57 | 0.21 | 1909 | quarters: 0.54 → 0.52 → 0.47 → 0.39

## Brush Artist · Refs · #44 Blue looping ribbon
Oil · 80 px · 36.0 s

![Brush Artist · Refs · #44 Blue looping ribbon](Brush-Artist-Refs-44-Blue-looping-ribbon.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 26 % → 26 % | 0.70 | 1.03 | 467 |
| heavy line | 27 % → 27 % | 0.71 | 1.00 | 508 |
| pressure swell | 21 % → 21 % | 0.72 | 1.03 | 374 |
| fast wave | 60 % → 63 % | 0.72 | 1.05 | 1333 |
| slow wave | 60 % → 60 % | 0.72 | 1.00 | 1926 |
| spiral | 77 % → 77 % | 0.71 | 1.00 | 1433 |
| loop | 54 % → 54 % | 0.72 | 1.00 | 720 |
| tilted | 20 % → 20 % | 0.71 | 1.00 | 564 |
| over the wet one | 43 % → 44 % | 0.71 | 1.00 | 388 |
| long, no reload | 95 % → 95 % | 0.72 | 1.00 | 2431 | quarters: 0.72 → 0.72 → 0.72 → 0.66

Numbers say: pressure barely changes the width; the long stroke does not run out of paint.

## Brush Artist · Refs · #45 Soft pastel pepper
Pastel · 40 px · 14.8 s

![Brush Artist · Refs · #45 Soft pastel pepper](Brush-Artist-Refs-45-Soft-pastel-pepper.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 7 % → 7 % | 0.53 | 1.00 | 52 |
| heavy line | 9 % → 9 % | 0.53 | 1.00 | 58 |
| pressure swell | 7 % → 7 % | 0.53 | 1.00 | 46 |
| fast wave | 22 % → 22 % | 0.53 | 1.00 | 227 |
| slow wave | 20 % → 20 % | 0.53 | 1.00 | 466 |
| spiral | 34 % → 34 % | 0.53 | 1.00 | 498 |
| loop | 17 % → 17 % | 0.53 | 1.00 | 226 |
| tilted | 6 % → 6 % | 0.53 | 1.00 | 119 |
| over the wet one | 15 % → 15 % | 0.53 | 1.00 | 131 |
| long, no reload | 39 % → 39 % | 0.53 | 1.00 | 427 | quarters: 0.23 → 0.23 → 0.23 → 0.23

Numbers say: the long stroke does not run out of paint.

## Brush Artist · Refs · #46 Red-brown ink lips
Watercolor · 70 px · 44.3 s

![Brush Artist · Refs · #46 Red-brown ink lips](Brush-Artist-Refs-46-Red-brown-ink-lips.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 20 % → 20 % | 0.59 | 1.01 | 139 |
| heavy line | 30 % → 30 % | 0.56 | 0.99 | 250 |
| pressure swell | 20 % → 20 % | 0.59 | 1.03 | 130 |
| fast wave | 60 % → 62 % | 0.56 | 1.04 | 403 |
| slow wave | 58 % → 58 % | 0.61 | 1.00 | 742 |
| spiral | 74 % → 74 % | 0.60 | 1.00 | 963 |
| loop | 50 % → 50 % | 0.59 | 1.00 | 456 |
| tilted | 21 % → 22 % | 0.59 | 1.01 | 246 |
| over the wet one | 45 % → 47 % | 0.59 | 1.06 | 150 |
| long, no reload | 94 % → 95 % | 0.59 | 1.00 | 1082 | quarters: 0.62 → 0.60 → 0.58 → 0.52

## Brush Artist · Refs · #47 Pink knife slabs
Heavy acrylic · 90 px · 35.2 s

![Brush Artist · Refs · #47 Pink knife slabs](Brush-Artist-Refs-47-Pink-knife-slabs.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 28 % → 27 % | 0.17 | 0.97 | 255 |
| heavy line | 29 % → 28 % | 0.17 | 0.97 | 276 |
| pressure swell | 22 % → 22 % | 0.18 | 1.01 | 152 |
| fast wave | 61 % → 60 % | 0.17 | 0.99 | 641 |
| slow wave | 61 % → 59 % | 0.17 | 0.96 | 1135 |
| spiral | 76 % → 57 % | 0.16 | 0.76 | 1434 |
| loop | 55 % → 54 % | 0.17 | 0.97 | 713 |
| tilted | 21 % → 21 % | 0.17 | 1.00 | 365 |
| over the wet one | 46 % → 44 % | 0.17 | 0.96 | 309 |
| long, no reload | 92 % → 76 % | 0.16 | 0.83 | 1612 | quarters: 0.18 → 0.16 → 0.14 → 0.09

Numbers say: pressure barely changes the width.

## Brush Artist · Refs · #48 Black bands with drips
Gouache · 70 px · 48.9 s

![Brush Artist · Refs · #48 Black bands with drips](Brush-Artist-Refs-48-Black-bands-with-drips.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 19 % → 18 % | 0.68 | 0.94 | 207 |
| heavy line | 29 % → 24 % | 0.68 | 0.85 | 319 |
| pressure swell | 23 % → 21 % | 0.68 | 0.92 | 173 |
| fast wave | 54 % → 37 % | 0.68 | 0.67 | 715 |
| slow wave | 54 % → 36 % | 0.68 | 0.67 | 1330 |
| spiral | 64 % → 35 % | 0.68 | 0.54 | 1054 |
| loop | 45 % → 37 % | 0.68 | 0.82 | 607 |
| tilted | 19 % → 19 % | 0.68 | 1.00 | 362 |
| over the wet one | 41 % → 38 % | 0.68 | 0.92 | 284 |
| long, no reload | 74 % → 37 % | 0.68 | 0.50 | 1538 | quarters: 0.64 → 0.61 → 0.54 → 0.44

## Brush Artist · Refs · #49 Magenta letters round brush
Ink · 30 px · 39.4 s

![Brush Artist · Refs · #49 Magenta letters round brush](Brush-Artist-Refs-49-Magenta-letters-round-brush.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 6 % → 8 % | 0.50 | 1.29 | 41 |
| heavy line | 21 % → 21 % | 0.51 | 0.99 | 105 |
| pressure swell | 12 % → 13 % | 0.52 | 1.02 | 61 |
| fast wave | 39 % → 38 % | 0.51 | 0.99 | 180 |
| slow wave | 32 % → 31 % | 0.51 | 0.99 | 440 |
| spiral | 50 % → 49 % | 0.51 | 0.97 | 394 |
| loop | 29 % → 29 % | 0.51 | 1.00 | 169 |
| tilted | 11 % → 11 % | 0.52 | 1.01 | 76 |
| over the wet one | 26 % → 26 % | 0.52 | 1.01 | 69 |
| long, no reload | 62 % → 56 % | 0.50 | 0.91 | 601 | quarters: 0.41 → 0.36 → 0.30 → 0.25

## Brush Artist · Refs · #50 Thick swipes on photo
Heavy acrylic · 40 px · 26.3 s

![Brush Artist · Refs · #50 Thick swipes on photo](Brush-Artist-Refs-50-Thick-swipes-on-photo.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 13 % → 13 % | 0.21 | 0.96 | 169 |
| heavy line | 14 % → 13 % | 0.21 | 0.96 | 166 |
| pressure swell | 11 % → 10 % | 0.22 | 0.95 | 116 |
| fast wave | 33 % → 31 % | 0.21 | 0.93 | 342 |
| slow wave | 34 % → 32 % | 0.20 | 0.95 | 521 |
| spiral | 58 % → 46 % | 0.20 | 0.80 | 530 |
| loop | 28 % → 27 % | 0.20 | 0.95 | 329 |
| tilted | 12 % → 12 % | 0.22 | 1.00 | 166 |
| over the wet one | 25 % → 24 % | 0.22 | 0.95 | 169 |
| long, no reload | 66 % → 46 % | 0.20 | 0.69 | 1083 | quarters: 0.16 → 0.13 → 0.11 → 0.07

Numbers say: pressure barely changes the width.

## Brush Artist · Ink — wash
Watercolor · 38 px · 45.8 s

![Brush Artist · Ink — wash](Brush-Artist-Ink-wash.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 11 % → 11 % | 0.39 | 1.03 | 77 |
| heavy line | 19 % → 19 % | 0.32 | 1.03 | 130 |
| pressure swell | 12 % → 13 % | 0.37 | 1.03 | 80 |
| fast wave | 40 % → 41 % | 0.31 | 1.04 | 223 |
| slow wave | 37 % → 38 % | 0.37 | 1.03 | 410 |
| spiral | 59 % → 61 % | 0.31 | 1.04 | 422 |
| loop | 32 % → 33 % | 0.35 | 1.02 | 254 |
| tilted | 13 % → 14 % | 0.38 | 1.04 | 137 |
| over the wet one | 29 % → 30 % | 0.38 | 1.04 | 93 |
| long, no reload | 67 % → 73 % | 0.29 | 1.09 | 994 | quarters: 0.34 → 0.27 → 0.19 → 0.12

## Brush Artist · Ink — brush line
Ink · 16 px · 36.1 s

![Brush Artist · Ink — brush line](Brush-Artist-Ink-brush-line.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 3 % → 5 % | 0.78 | 1.81 | 98 |
| heavy line | 13 % → 13 % | 0.88 | 0.99 | 152 |
| pressure swell | 8 % → 8 % | 0.87 | 1.05 | 65 |
| fast wave | 24 % → 23 % | 0.87 | 0.96 | 220 |
| slow wave | 20 % → 19 % | 0.87 | 0.97 | 310 |
| spiral | 30 % → 27 % | 0.86 | 0.89 | 362 |
| loop | 18 % → 18 % | 0.88 | 1.00 | 184 |
| tilted | 7 % → 7 % | 0.88 | 1.01 | 103 |
| over the wet one | 17 % → 17 % | 0.88 | 1.00 | 97 |
| long, no reload | 42 % → 30 % | 0.85 | 0.71 | 493 | quarters: 0.49 → 0.40 → 0.30 → 0.20

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Ink — dry brush
Gouache · 30 px · 30.9 s

![Brush Artist · Ink — dry brush](Brush-Artist-Ink-dry-brush.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 8 % → 1 % | 0.71 | 0.13 | 86 |
| heavy line | 10 % → 1 % | 0.71 | 0.11 | 172 |
| pressure swell | 7 % → 2 % | 0.71 | 0.23 | 106 |
| fast wave | 21 % → 2 % | 0.71 | 0.10 | 377 |
| slow wave | 21 % → 2 % | 0.71 | 0.09 | 616 |
| spiral | 31 % → 2 % | 0.71 | 0.07 | 570 |
| loop | 18 % → 2 % | 0.71 | 0.13 | 441 |
| tilted | 9 % → 8 % | 0.71 | 0.96 | 221 |
| over the wet one | 17 % → 4 % | 0.71 | 0.25 | 172 |
| long, no reload | 30 % → 3 % | 0.71 | 0.09 | 846 | quarters: 0.38 → 0.31 → 0.21 → 0.08

## Brush Artist · Watercolour — blue
Watercolor · 40 px · 37.2 s

![Brush Artist · Watercolour — blue](Brush-Artist-Watercolour-blue.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 6 % → 10 % | 0.43 | 1.78 | 71 |
| heavy line | 11 % → 13 % | 0.43 | 1.17 | 148 |
| pressure swell | 7 % → 9 % | 0.45 | 1.37 | 54 |
| fast wave | 24 % → 26 % | 0.41 | 1.09 | 196 |
| slow wave | 22 % → 28 % | 0.44 | 1.25 | 342 |
| spiral | 38 % → 42 % | 0.38 | 1.11 | 263 |
| loop | 19 % → 23 % | 0.44 | 1.17 | 169 |
| tilted | 12 % → 12 % | 0.44 | 1.01 | 135 |
| over the wet one | 21 % → 25 % | 0.44 | 1.17 | 72 |
| long, no reload | 51 % → 55 % | 0.37 | 1.06 | 591 | quarters: 0.32 → 0.24 → 0.19 → 0.15

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Watercolour — violet
Watercolor · 40 px · 35.2 s

![Brush Artist · Watercolour — violet](Brush-Artist-Watercolour-violet.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 6 % → 10 % | 0.42 | 1.78 | 57 |
| heavy line | 11 % → 13 % | 0.42 | 1.17 | 136 |
| pressure swell | 7 % → 9 % | 0.43 | 1.37 | 53 |
| fast wave | 24 % → 26 % | 0.41 | 1.09 | 236 |
| slow wave | 22 % → 28 % | 0.43 | 1.25 | 410 |
| spiral | 38 % → 42 % | 0.38 | 1.11 | 366 |
| loop | 19 % → 23 % | 0.43 | 1.17 | 156 |
| tilted | 12 % → 12 % | 0.43 | 1.01 | 126 |
| over the wet one | 21 % → 25 % | 0.43 | 1.17 | 70 |
| long, no reload | 51 % → 55 % | 0.37 | 1.06 | 439 | quarters: 0.30 → 0.24 → 0.19 → 0.16

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Watercolour — teal
Watercolor · 40 px · 35.6 s

![Brush Artist · Watercolour — teal](Brush-Artist-Watercolour-teal.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 6 % → 10 % | 0.30 | 1.78 | 57 |
| heavy line | 11 % → 13 % | 0.31 | 1.17 | 85 |
| pressure swell | 7 % → 9 % | 0.31 | 1.37 | 94 |
| fast wave | 24 % → 26 % | 0.30 | 1.09 | 316 |
| slow wave | 22 % → 28 % | 0.31 | 1.25 | 420 |
| spiral | 38 % → 42 % | 0.28 | 1.11 | 296 |
| loop | 19 % → 23 % | 0.31 | 1.17 | 145 |
| tilted | 12 % → 12 % | 0.31 | 1.01 | 117 |
| over the wet one | 21 % → 25 % | 0.31 | 1.17 | 112 |
| long, no reload | 51 % → 55 % | 0.27 | 1.06 | 459 | quarters: 0.22 → 0.18 → 0.14 → 0.11

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Gouache
Gouache · 30 px · 36.7 s

![Brush Artist · Gouache](Brush-Artist-Gouache.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 8 % → 8 % | 0.16 | 0.97 | 120 |
| heavy line | 15 % → 12 % | 0.16 | 0.78 | 128 |
| pressure swell | 11 % → 9 % | 0.16 | 0.85 | 86 |
| fast wave | 30 % → 14 % | 0.16 | 0.45 | 221 |
| slow wave | 29 % → 14 % | 0.16 | 0.47 | 377 |
| spiral | 40 % → 14 % | 0.16 | 0.35 | 338 |
| loop | 24 % → 15 % | 0.16 | 0.62 | 168 |
| tilted | 10 % → 10 % | 0.16 | 1.01 | 104 |
| over the wet one | 22 % → 19 % | 0.16 | 0.89 | 102 |
| long, no reload | 43 % → 15 % | 0.16 | 0.35 | 520 | quarters: 0.10 → 0.07 → 0.04 → 0.02

## Brush Artist · Oil — bristle
Oil · 30 px · 21.8 s

![Brush Artist · Oil — bristle](Brush-Artist-Oil-bristle.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 9 % → 9 % | 0.53 | 1.00 | 102 |
| heavy line | 9 % → 9 % | 0.53 | 1.00 | 117 |
| pressure swell | 7 % → 7 % | 0.54 | 1.00 | 90 |
| fast wave | 23 % → 23 % | 0.53 | 1.00 | 333 |
| slow wave | 23 % → 23 % | 0.53 | 1.00 | 523 |
| spiral | 36 % → 36 % | 0.50 | 1.00 | 528 |
| loop | 19 % → 19 % | 0.54 | 1.00 | 303 |
| tilted | 11 % → 11 % | 0.53 | 1.00 | 155 |
| over the wet one | 19 % → 19 % | 0.53 | 1.00 | 124 |
| long, no reload | 47 % → 47 % | 0.45 | 1.00 | 1219 | quarters: 0.31 → 0.27 → 0.22 → 0.14

Numbers say: pressure barely changes the width.

## Brush Artist · Charcoal — stick
Charcoal · 30 px · 11.5 s

![Brush Artist · Charcoal — stick](Brush-Artist-Charcoal-stick.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 7 % → 7 % | 0.84 | 1.00 | 22 |
| heavy line | 7 % → 7 % | 0.84 | 1.00 | 34 |
| pressure swell | 5 % → 5 % | 0.84 | 1.00 | 18 |
| fast wave | 17 % → 17 % | 0.84 | 1.00 | 57 |
| slow wave | 17 % → 17 % | 0.84 | 1.00 | 107 |
| spiral | 29 % → 29 % | 0.84 | 1.00 | 99 |
| loop | 14 % → 14 % | 0.84 | 1.00 | 55 |
| tilted | 6 % → 6 % | 0.84 | 1.00 | 37 |
| over the wet one | 13 % → 13 % | 0.84 | 1.00 | 25 |
| long, no reload | 37 % → 37 % | 0.84 | 1.00 | 211 | quarters: 0.35 → 0.34 → 0.34 → 0.35

Numbers say: pressure barely changes the width; the long stroke does not run out of paint.

## Brush Artist · Refs · #01 Henry Ward peach cloud — own sheet
own sheet 600 × 600 · Gouache · 44 px · 17.0 s

![Brush Artist · Refs · #01 Henry Ward peach cloud — own sheet](Brush-Artist-Refs-01-Henry-Ward-peach-cloud-own-sheet.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| stroke 1 | 34 % → 41 % | 0.11 | 1.19 | 207 |
| stroke 2 | 41 % → 55 % | 0.11 | 1.36 | 189 |
| stroke 3 | 44 % → 65 % | 0.11 | 1.47 | 173 |
| stroke 4 | 48 % → 62 % | 0.11 | 1.27 | 152 |
| stroke 5 | 40 % → 61 % | 0.11 | 1.51 | 163 |
| stroke 6 | 48 % → 49 % | 0.11 | 1.02 | 142 |
| stroke 7 | 32 % → 57 % | 0.10 | 1.80 | 165 |
| stroke 8 | 37 % → 60 % | 0.11 | 1.63 | 166 |
| stroke 9 | 46 % → 67 % | 0.11 | 1.46 | 155 |
| stroke 10 | 51 % → 72 % | 0.11 | 1.42 | 197 |
| stroke 11 | 53 % → 75 % | 0.10 | 1.43 | 174 |
| stroke 12 | 61 % → 87 % | 0.11 | 1.42 | 176 |
| stroke 13 | 61 % → 84 % | 0.11 | 1.39 | 186 |
| stroke 14 | 59 % → 84 % | 0.11 | 1.42 | 169 |
| stroke 15 | 66 % → 86 % | 0.11 | 1.30 | 173 |
| stroke 16 | 71 % → 89 % | 0.11 | 1.24 | 228 |
| stroke 17 | 68 % → 85 % | 0.11 | 1.25 | 324 |
| stroke 18 | 70 % → 85 % | 0.11 | 1.22 | 275 |
| stroke 19 | 73 % → 85 % | 0.11 | 1.17 | 194 |
| stroke 20 | 73 % → 82 % | 0.11 | 1.14 | 323 |
| stroke 21 | 73 % → 77 % | 0.11 | 1.06 | 300 |
| stroke 22 | 75 % → 78 % | 0.11 | 1.04 | 194 |
| stroke 23 | 74 % → 74 % | 0.11 | 0.99 | 221 |
| stroke 24 | 79 % → 78 % | 0.11 | 0.98 | 208 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #02 Henry Ward cream strokes — own sheet
own sheet 600 × 600 · Gouache · 46 px · 10.4 s

![Brush Artist · Refs · #02 Henry Ward cream strokes — own sheet](Brush-Artist-Refs-02-Henry-Ward-cream-strokes-own-sheet.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| stroke 1 | 32 % → 29 % | 0.03 | 0.93 | 346 |
| stroke 2 | 35 % → 28 % | 0.03 | 0.80 | 316 |
| stroke 3 | 30 % → 33 % | 0.03 | 1.11 | 302 |
| stroke 4 | 36 % → 49 % | 0.03 | 1.35 | 343 |
| stroke 5 | 53 % → 47 % | 0.03 | 0.89 | 285 |
| stroke 6 | 34 % → 42 % | 0.03 | 1.24 | 262 |
| stroke 7 | 46 % → 40 % | 0.03 | 0.87 | 286 |

## Brush Artist · Refs · #03 Henry Ward navy contours — own sheet
own sheet 600 × 600 · Heavy acrylic · 22 px · 3.6 s

![Brush Artist · Refs · #03 Henry Ward navy contours — own sheet](Brush-Artist-Refs-03-Henry-Ward-navy-contours-own-sheet.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| stroke 1 | 15 % → 20 % | 0.75 | 1.28 | 167 |
| stroke 2 | 28 % → 30 % | 0.75 | 1.09 | 124 |
| stroke 3 | 28 % → 28 % | 0.75 | 0.99 | 167 |
| stroke 4 | 26 % → 24 % | 0.75 | 0.92 | 180 |

## Brush Artist · Refs · #04 Henry Ward grey cloud — own sheet
own sheet 600 × 600 · Gouache · 50 px · 17.6 s

![Brush Artist · Refs · #04 Henry Ward grey cloud — own sheet](Brush-Artist-Refs-04-Henry-Ward-grey-cloud-own-sheet.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| stroke 1 | 31 % → 57 % | 0.12 | 1.81 | 240 |
| stroke 2 | 37 % → 61 % | 0.12 | 1.64 | 287 |
| stroke 3 | 57 % → 79 % | 0.12 | 1.38 | 283 |
| stroke 4 | 58 % → 82 % | 0.12 | 1.41 | 289 |
| stroke 5 | 60 % → 85 % | 0.12 | 1.41 | 323 |
| stroke 6 | 61 % → 88 % | 0.12 | 1.45 | 274 |
| stroke 7 | 59 % → 83 % | 0.12 | 1.41 | 309 |
| stroke 8 | 56 % → 83 % | 0.12 | 1.49 | 281 |
| stroke 9 | 58 % → 85 % | 0.12 | 1.45 | 263 |
| stroke 10 | 61 % → 87 % | 0.12 | 1.44 | 239 |
| stroke 11 | 61 % → 85 % | 0.12 | 1.40 | 234 |
| stroke 12 | 62 % → 85 % | 0.12 | 1.38 | 259 |
| stroke 13 | 61 % → 85 % | 0.12 | 1.40 | 289 |
| stroke 14 | 60 % → 83 % | 0.12 | 1.39 | 282 |
| stroke 15 | 59 % → 82 % | 0.12 | 1.40 | 279 |
| stroke 16 | 60 % → 83 % | 0.12 | 1.38 | 275 |
| stroke 17 | 59 % → 83 % | 0.12 | 1.41 | 252 |
| stroke 18 | 60 % → 82 % | 0.12 | 1.36 | 256 |
| stroke 19 | 59 % → 60 % | 0.12 | 1.01 | 275 |
| stroke 20 | 61 % → 58 % | 0.12 | 0.96 | 307 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #05 Henry Ward green in rust loops — own sheet
own sheet 600 × 600 · Heavy acrylic · 20 px · 2.9 s

![Brush Artist · Refs · #05 Henry Ward green in rust loops — own sheet](Brush-Artist-Refs-05-Henry-Ward-green-in-rust-loops-own-sheet.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| stroke 1 | 16 % → 24 % | 0.57 | 1.48 | 160 |
| stroke 2 | 15 % → 13 % | 0.58 | 0.90 | 189 |
| stroke 3 | 25 % → 24 % | 0.58 | 0.94 | 143 |

## Brush Artist · Refs · #06 Henry Ward scrubbed grey — own sheet
own sheet 600 × 600 · Gouache · 50 px · 18.3 s

![Brush Artist · Refs · #06 Henry Ward scrubbed grey — own sheet](Brush-Artist-Refs-06-Henry-Ward-scrubbed-grey-own-sheet.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| stroke 1 | 33 % → 56 % | 0.10 | 1.68 | 277 |
| stroke 2 | 41 % → 62 % | 0.10 | 1.53 | 239 |
| stroke 3 | 57 % → 88 % | 0.10 | 1.53 | 213 |
| stroke 4 | 58 % → 87 % | 0.10 | 1.51 | 276 |
| stroke 5 | 55 % → 85 % | 0.10 | 1.55 | 263 |
| stroke 6 | 59 % → 85 % | 0.10 | 1.44 | 291 |
| stroke 7 | 60 % → 83 % | 0.10 | 1.39 | 279 |
| stroke 8 | 61 % → 87 % | 0.10 | 1.43 | 283 |
| stroke 9 | 59 % → 88 % | 0.10 | 1.48 | 277 |
| stroke 10 | 58 % → 88 % | 0.10 | 1.50 | 278 |
| stroke 11 | 58 % → 83 % | 0.10 | 1.43 | 271 |
| stroke 12 | 57 % → 82 % | 0.10 | 1.43 | 266 |
| stroke 13 | 57 % → 82 % | 0.10 | 1.45 | 303 |
| stroke 14 | 55 % → 83 % | 0.10 | 1.49 | 268 |
| stroke 15 | 57 % → 84 % | 0.10 | 1.47 | 269 |
| stroke 16 | 62 % → 89 % | 0.10 | 1.44 | 264 |
| stroke 17 | 60 % → 85 % | 0.10 | 1.42 | 308 |
| stroke 18 | 60 % → 84 % | 0.10 | 1.39 | 290 |
| stroke 19 | 56 % → 84 % | 0.10 | 1.49 | 233 |
| stroke 20 | 57 % → 82 % | 0.10 | 1.44 | 261 |
| stroke 21 | 57 % → 65 % | 0.10 | 1.15 | 320 |
| stroke 22 | 61 % → 59 % | 0.10 | 0.96 | 259 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #07 Henry Ward blue L + black zigzag — own sheet
own sheet 600 × 600 · Heavy acrylic · 34 px · 2.6 s

![Brush Artist · Refs · #07 Henry Ward blue L + black zigzag — own sheet](Brush-Artist-Refs-07-Henry-Ward-blue-L-black-zigzag-own-sheet.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| stroke 1 | 30 % → 31 % | 0.63 | 1.05 | 156 |
| stroke 2 | 31 % → 30 % | 0.63 | 0.94 | 110 |

## Brush Artist · Refs · #08 Henry Ward olive bands — own sheet
own sheet 600 × 600 · Gouache · 34 px · 7.6 s

![Brush Artist · Refs · #08 Henry Ward olive bands — own sheet](Brush-Artist-Refs-08-Henry-Ward-olive-bands-own-sheet.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| stroke 1 | 33 % → 19 % | 0.61 | 0.57 | 230 |
| stroke 2 | 37 % → 20 % | 0.61 | 0.52 | 216 |
| stroke 3 | 31 % → 23 % | 0.61 | 0.75 | 210 |
| stroke 4 | 38 % → 37 % | 0.61 | 0.98 | 233 |
| stroke 5 | 50 % → 35 % | 0.61 | 0.71 | 228 |
| stroke 6 | 36 % → 22 % | 0.61 | 0.61 | 222 |

## Brush Artist · Refs · #09 Henry Ward white loops — own sheet
own sheet 600 × 600 · Gouache · 46 px · 8.4 s

![Brush Artist · Refs · #09 Henry Ward white loops — own sheet](Brush-Artist-Refs-09-Henry-Ward-white-loops-own-sheet.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| stroke 1 | 48 % → 32 % | 0.02 | 0.67 | 1127 |
| stroke 2 | 51 % → 37 % | 0.02 | 0.71 | 1095 |
| stroke 3 | 59 % → 44 % | 0.02 | 0.75 | 1029 |

## Brush Artist · Refs · #10 Henry Ward maroon loops — own sheet
own sheet 600 × 600 · Heavy acrylic · 30 px · 3.2 s

![Brush Artist · Refs · #10 Henry Ward maroon loops — own sheet](Brush-Artist-Refs-10-Henry-Ward-maroon-loops-own-sheet.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| stroke 1 | 16 % → 33 % | 0.77 | 2.08 | 227 |
| stroke 2 | 29 % → 47 % | 0.77 | 1.60 | 115 |
| stroke 3 | 40 % → 50 % | 0.77 | 1.24 | 151 |
| stroke 4 | 45 % → 43 % | 0.77 | 0.96 | 152 |
| stroke 5 | 41 % → 38 % | 0.77 | 0.93 | 148 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #11 Henry Ward purple spun balls — own sheet
own sheet 600 × 600 · Heavy acrylic · 36 px · 4.0 s

![Brush Artist · Refs · #11 Henry Ward purple spun balls — own sheet](Brush-Artist-Refs-11-Henry-Ward-purple-spun-balls-own-sheet.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| stroke 1 | 35 % → 43 % | 0.79 | 1.23 | 355 |
| stroke 2 | 45 % → 52 % | 0.80 | 1.15 | 410 |
| stroke 3 | 45 % → 43 % | 0.80 | 0.96 | 343 |

## Brush Artist · Refs · #12 Henry Ward black-olive cage — own sheet
own sheet 600 × 600 · Gouache · 28 px · 7.5 s

![Brush Artist · Refs · #12 Henry Ward black-olive cage — own sheet](Brush-Artist-Refs-12-Henry-Ward-black-olive-cage-own-sheet.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| stroke 1 | 18 % → 22 % | 0.65 | 1.23 | 239 |
| stroke 2 | 16 % → 26 % | 0.65 | 1.60 | 174 |
| stroke 3 | 34 % → 34 % | 0.65 | 1.00 | 304 |
| stroke 4 | 34 % → 34 % | 0.65 | 1.02 | 171 |
| stroke 5 | 35 % → 21 % | 0.65 | 0.60 | 197 |
| stroke 6 | 52 % → 37 % | 0.65 | 0.72 | 219 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #13 Henry Ward blue streaky form — own sheet
own sheet 600 × 600 · Gouache · 50 px · 22.1 s

![Brush Artist · Refs · #13 Henry Ward blue streaky form — own sheet](Brush-Artist-Refs-13-Henry-Ward-blue-streaky-form-own-sheet.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| stroke 1 | 33 % → 60 % | 0.10 | 1.83 | 258 |
| stroke 2 | 41 % → 63 % | 0.10 | 1.56 | 281 |
| stroke 3 | 58 % → 85 % | 0.10 | 1.46 | 298 |
| stroke 4 | 59 % → 87 % | 0.10 | 1.49 | 300 |
| stroke 5 | 59 % → 85 % | 0.10 | 1.44 | 292 |
| stroke 6 | 55 % → 81 % | 0.10 | 1.47 | 451 |
| stroke 7 | 60 % → 84 % | 0.10 | 1.40 | 385 |
| stroke 8 | 61 % → 84 % | 0.10 | 1.37 | 330 |
| stroke 9 | 61 % → 86 % | 0.10 | 1.42 | 367 |
| stroke 10 | 62 % → 88 % | 0.10 | 1.40 | 370 |
| stroke 11 | 57 % → 85 % | 0.10 | 1.49 | 277 |
| stroke 12 | 57 % → 81 % | 0.10 | 1.42 | 298 |
| stroke 13 | 60 % → 86 % | 0.10 | 1.44 | 264 |
| stroke 14 | 53 % → 81 % | 0.10 | 1.53 | 277 |
| stroke 15 | 56 % → 82 % | 0.10 | 1.47 | 325 |
| stroke 16 | 55 % → 83 % | 0.10 | 1.51 | 439 |
| stroke 17 | 60 % → 83 % | 0.10 | 1.39 | 516 |
| stroke 18 | 60 % → 80 % | 0.10 | 1.34 | 583 |
| stroke 19 | 66 % → 77 % | 0.10 | 1.16 | 684 |
| stroke 20 | 77 % → 74 % | 0.10 | 0.97 | 634 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #14 Henry Ward olive totem — own sheet
own sheet 600 × 600 · Heavy acrylic · 48 px · 11.5 s

![Brush Artist · Refs · #14 Henry Ward olive totem — own sheet](Brush-Artist-Refs-14-Henry-Ward-olive-totem-own-sheet.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| stroke 1 | 31 % → 50 % | 0.33 | 1.58 | 173 |
| stroke 2 | 36 % → 62 % | 0.33 | 1.71 | 187 |
| stroke 3 | 54 % → 76 % | 0.34 | 1.42 | 160 |
| stroke 4 | 50 % → 74 % | 0.34 | 1.46 | 172 |
| stroke 5 | 56 % → 78 % | 0.33 | 1.39 | 163 |
| stroke 6 | 54 % → 81 % | 0.34 | 1.50 | 165 |
| stroke 7 | 52 % → 75 % | 0.34 | 1.45 | 257 |
| stroke 8 | 51 % → 77 % | 0.34 | 1.53 | 245 |
| stroke 9 | 56 % → 81 % | 0.34 | 1.44 | 216 |
| stroke 10 | 56 % → 78 % | 0.34 | 1.40 | 198 |
| stroke 11 | 57 % → 79 % | 0.34 | 1.38 | 202 |
| stroke 12 | 53 % → 80 % | 0.34 | 1.53 | 184 |
| stroke 13 | 55 % → 83 % | 0.34 | 1.51 | 180 |
| stroke 14 | 52 % → 76 % | 0.34 | 1.48 | 269 |
| stroke 15 | 58 % → 82 % | 0.34 | 1.41 | 209 |
| stroke 16 | 54 % → 80 % | 0.34 | 1.47 | 224 |
| stroke 17 | 53 % → 78 % | 0.34 | 1.45 | 160 |
| stroke 18 | 57 % → 84 % | 0.34 | 1.47 | 169 |
| stroke 19 | 57 % → 80 % | 0.34 | 1.41 | 169 |
| stroke 20 | 55 % → 76 % | 0.34 | 1.40 | 187 |
| stroke 21 | 52 % → 67 % | 0.34 | 1.30 | 210 |
| stroke 22 | 60 % → 59 % | 0.34 | 0.98 | 178 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #15 Ultramarine brush script — own sheet
own sheet 600 × 600 · Ink · 10 px · 15.7 s

![Brush Artist · Refs · #15 Ultramarine brush script — own sheet](Brush-Artist-Refs-15-Ultramarine-brush-script-own-sheet.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| stroke 1 | 69 % → 73 % | 0.70 | 1.05 | 97 |
| stroke 2 | 70 % → 72 % | 0.69 | 1.04 | 106 |
| stroke 3 | 70 % → 74 % | 0.69 | 1.05 | 90 |
| stroke 4 | 71 % → 72 % | 0.67 | 1.01 | 126 |
| stroke 5 | 66 % → 69 % | 0.67 | 1.04 | 146 |
| stroke 6 | 67 % → 71 % | 0.70 | 1.05 | 73 |
| stroke 7 | 69 % → 71 % | 0.67 | 1.04 | 130 |
| stroke 8 | 70 % → 71 % | 0.70 | 1.02 | 95 |
| stroke 9 | 67 % → 70 % | 0.68 | 1.05 | 102 |
| stroke 10 | 65 % → 69 % | 0.69 | 1.05 | 91 |
| stroke 11 | 72 % → 75 % | 0.70 | 1.04 | 93 |
| stroke 12 | 68 % → 69 % | 0.67 | 1.01 | 153 |
| stroke 13 | 66 % → 69 % | 0.67 | 1.04 | 116 |
| stroke 14 | 67 % → 71 % | 0.70 | 1.05 | 106 |
| stroke 15 | 69 % → 73 % | 0.71 | 1.05 | 105 |
| stroke 16 | 69 % → 72 % | 0.70 | 1.04 | 143 |
| stroke 17 | 68 % → 69 % | 0.70 | 1.02 | 124 |
| stroke 18 | 68 % → 71 % | 0.70 | 1.05 | 147 |
| stroke 19 | 66 % → 71 % | 0.71 | 1.07 | 112 |
| stroke 20 | 68 % → 72 % | 0.71 | 1.06 | 143 |
| stroke 21 | 71 % → 73 % | 0.67 | 1.03 | 328 |
| stroke 22 | 77 % → 79 % | 0.70 | 1.02 | 292 |
| stroke 23 | 67 % → 71 % | 0.70 | 1.05 | 174 |
| stroke 24 | 66 % → 69 % | 0.71 | 1.05 | 158 |
| stroke 25 | 69 % → 72 % | 0.68 | 1.04 | 231 |
| stroke 26 | 71 % → 71 % | 0.66 | 1.01 | 109 |

## Brush Artist · Refs · #18 Blue oil-stick scribbles — own sheet
own sheet 600 × 600 · Pastel · 10 px · 4.4 s

![Brush Artist · Refs · #18 Blue oil-stick scribbles — own sheet](Brush-Artist-Refs-18-Blue-oil-stick-scribbles-own-sheet.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| stroke 1 | 26 % → 49 % | 0.52 | 1.92 | 173 |
| stroke 2 | 22 % → 54 % | 0.52 | 2.43 | 230 |
| stroke 3 | 25 % → 39 % | 0.52 | 1.55 | 237 |
| stroke 4 | 23 % → 43 % | 0.52 | 1.85 | 244 |
| stroke 5 | 43 % → 49 % | 0.52 | 1.14 | 187 |
| stroke 6 | 40 % → 41 % | 0.52 | 1.02 | 148 |
| stroke 7 | 39 % → 48 % | 0.52 | 1.24 | 179 |
| stroke 8 | 44 % → 44 % | 0.52 | 1.00 | 236 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #20 Orange-red crayon scribble — own sheet
own sheet 600 × 600 · Pastel · 14 px · 4.0 s

![Brush Artist · Refs · #20 Orange-red crayon scribble — own sheet](Brush-Artist-Refs-20-Orange-red-crayon-scribble-own-sheet.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| stroke 1 | 12 % → 27 % | 0.53 | 2.26 | 312 |
| stroke 2 | 14 % → 34 % | 0.53 | 2.38 | 210 |
| stroke 3 | 21 % → 33 % | 0.53 | 1.57 | 361 |
| stroke 4 | 38 % → 47 % | 0.53 | 1.25 | 314 |
| stroke 5 | 43 % → 43 % | 0.53 | 1.00 | 305 |
| stroke 6 | 33 % → 33 % | 0.53 | 1.00 | 280 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #21 Gritty black contours — own sheet
own sheet 600 × 600 · Gouache · 12 px · 5.4 s

![Brush Artist · Refs · #21 Gritty black contours — own sheet](Brush-Artist-Refs-21-Gritty-black-contours-own-sheet.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| stroke 1 | 12 % → 9 % | 0.80 | 0.73 | 245 |
| stroke 2 | 10 % → 6 % | 0.80 | 0.61 | 211 |
| stroke 3 | 18 % → 5 % | 0.80 | 0.28 | 155 |
| stroke 4 | 19 % → 9 % | 0.80 | 0.47 | 163 |
| stroke 5 | 19 % → 10 % | 0.80 | 0.50 | 129 |

## Brush Artist · Refs · #22 Bold black brush poster — own sheet
own sheet 600 × 600 · Ink · 20 px · 6.2 s

![Brush Artist · Refs · #22 Bold black brush poster — own sheet](Brush-Artist-Refs-22-Bold-black-brush-poster-own-sheet.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| stroke 1 | 34 % → 37 % | 0.89 | 1.10 | 160 |
| stroke 2 | 55 % → 66 % | 0.89 | 1.21 | 29 |
| stroke 3 | 49 % → 49 % | 0.89 | 1.00 | 45 |
| stroke 4 | 36 % → 43 % | 0.89 | 1.20 | 88 |
| stroke 5 | 36 % → 36 % | 0.89 | 1.00 | 103 |

## Brush Artist · Refs · #23 Dry white on orange + black line — own sheet
own sheet 600 × 600 · Gouache · 50 px · 12.1 s

![Brush Artist · Refs · #23 Dry white on orange + black line — own sheet](Brush-Artist-Refs-23-Dry-white-on-orange-black-line-own-sheet.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| stroke 1 | 27 % → 48 % | 0.00 | 1.80 | 206 |
| stroke 2 | 31 % → 49 % | 0.00 | 1.56 | 237 |
| stroke 3 | 51 % → 70 % | 0.00 | 1.37 | 182 |
| stroke 4 | 48 % → 65 % | 0.00 | 1.35 | 211 |
| stroke 5 | 50 % → 54 % | 0.01 | 1.08 | 172 |
| stroke 6 | 49 % → 60 % | 0.01 | 1.21 | 252 |
| stroke 7 | 40 % → 57 % | 0.01 | 1.44 | 231 |
| stroke 8 | 42 % → 54 % | 0.01 | 1.30 | 212 |
| stroke 9 | 51 % → 68 % | 0.01 | 1.32 | 213 |
| stroke 10 | 54 % → 71 % | 0.01 | 1.31 | 222 |
| stroke 11 | 50 % → 70 % | 0.01 | 1.40 | 192 |
| stroke 12 | 49 % → 65 % | 0.01 | 1.31 | 218 |
| stroke 13 | 53 % → 63 % | 0.01 | 1.20 | 200 |
| stroke 14 | 49 % → 62 % | 0.01 | 1.28 | 220 |
| stroke 15 | 49 % → 66 % | 0.01 | 1.35 | 179 |
| stroke 16 | 46 % → 63 % | 0.01 | 1.35 | 146 |
| stroke 17 | 47 % → 52 % | 0.01 | 1.12 | 166 |
| stroke 18 | 56 % → 50 % | 0.01 | 0.91 | 140 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #24 Picasso flat oil — own sheet
own sheet 600 × 600 · Oil · 34 px · 6.8 s

![Brush Artist · Refs · #24 Picasso flat oil — own sheet](Brush-Artist-Refs-24-Picasso-flat-oil-own-sheet.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| stroke 1 | 34 % → 60 % | 0.41 | 1.76 | 146 |
| stroke 2 | 39 % → 65 % | 0.42 | 1.66 | 158 |
| stroke 3 | 56 % → 84 % | 0.42 | 1.50 | 179 |
| stroke 4 | 56 % → 82 % | 0.42 | 1.48 | 145 |
| stroke 5 | 54 % → 86 % | 0.42 | 1.57 | 121 |
| stroke 6 | 56 % → 85 % | 0.42 | 1.52 | 124 |
| stroke 7 | 60 % → 74 % | 0.42 | 1.23 | 119 |
| stroke 8 | 56 % → 71 % | 0.42 | 1.28 | 178 |
| stroke 9 | 41 % → 66 % | 0.41 | 1.63 | 126 |
| stroke 10 | 45 % → 68 % | 0.41 | 1.50 | 132 |
| stroke 11 | 59 % → 73 % | 0.41 | 1.24 | 133 |
| stroke 12 | 58 % → 77 % | 0.41 | 1.32 | 215 |
| stroke 13 | 46 % → 71 % | 0.41 | 1.56 | 245 |
| stroke 14 | 48 % → 74 % | 0.41 | 1.55 | 202 |
| stroke 15 | 52 % → 82 % | 0.41 | 1.57 | 190 |
| stroke 16 | 48 % → 78 % | 0.42 | 1.60 | 264 |
| stroke 17 | 60 % → 71 % | 0.42 | 1.19 | 230 |
| stroke 18 | 56 % → 56 % | 0.42 | 1.00 | 223 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #25 Yellow heavy flat stroke — own sheet
own sheet 600 × 600 · Heavy acrylic · 110 px · 3.9 s

![Brush Artist · Refs · #25 Yellow heavy flat stroke — own sheet](Brush-Artist-Refs-25-Yellow-heavy-flat-stroke-own-sheet.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| stroke 1 | 35 % → 35 % | 0.17 | 0.98 | 637 |

## Brush Artist · Refs · #27 Orange impasto swatch — own sheet
own sheet 600 × 600 · Heavy acrylic · 60 px · 3.6 s

![Brush Artist · Refs · #27 Orange impasto swatch — own sheet](Brush-Artist-Refs-27-Orange-impasto-swatch-own-sheet.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| stroke 1 | 23 % → 29 % | 0.37 | 1.29 | 105 |
| stroke 2 | 19 % → 40 % | 0.37 | 2.07 | 45 |
| stroke 3 | 26 % → 38 % | 0.37 | 1.48 | 35 |
| stroke 4 | 22 % → 22 % | 0.36 | 0.96 | 58 |
| stroke 5 | 32 % → 41 % | 0.36 | 1.28 | 100 |
| stroke 6 | 39 % → 40 % | 0.36 | 1.02 | 74 |
| stroke 7 | 19 % → 21 % | 0.36 | 1.11 | 76 |
| stroke 8 | 42 % → 40 % | 0.36 | 0.97 | 55 |
| stroke 9 | 49 % → 48 % | 0.37 | 0.97 | 98 |
| stroke 10 | 28 % → 27 % | 0.36 | 0.96 | 58 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #28 Miles Davis black lines — own sheet
own sheet 600 × 600 · Ink · 22 px · 6.7 s

![Brush Artist · Refs · #28 Miles Davis black lines — own sheet](Brush-Artist-Refs-28-Miles-Davis-black-lines-own-sheet.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| stroke 1 | 29 % → 37 % | 0.89 | 1.27 | 203 |
| stroke 2 | 37 % → 57 % | 0.89 | 1.52 | 123 |
| stroke 3 | 47 % → 48 % | 0.89 | 1.02 | 97 |
| stroke 4 | 50 % → 58 % | 0.89 | 1.16 | 157 |
| stroke 5 | 64 % → 64 % | 0.89 | 1.00 | 117 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #29 Shrigley magenta asterisk — own sheet
own sheet 600 × 600 · Watercolor · 70 px · 7.2 s

![Brush Artist · Refs · #29 Shrigley magenta asterisk — own sheet](Brush-Artist-Refs-29-Shrigley-magenta-asterisk-own-sheet.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| stroke 1 | 25 % → 44 % | 0.52 | 1.77 | 247 |
| stroke 2 | 17 % → 17 % | 0.51 | 1.00 | 165 |
| stroke 3 | 37 % → 44 % | 0.52 | 1.18 | 203 |
| stroke 4 | 33 % → 33 % | 0.51 | 1.02 | 173 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #30 Red gouache face patch — own sheet
own sheet 600 × 600 · Gouache · 60 px · 14.0 s

![Brush Artist · Refs · #30 Red gouache face patch — own sheet](Brush-Artist-Refs-30-Red-gouache-face-patch-own-sheet.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| stroke 1 | 27 % → 51 % | 0.59 | 1.89 | 189 |
| stroke 2 | 33 % → 57 % | 0.59 | 1.74 | 147 |
| stroke 3 | 50 % → 77 % | 0.59 | 1.54 | 191 |
| stroke 4 | 50 % → 77 % | 0.59 | 1.54 | 179 |
| stroke 5 | 49 % → 78 % | 0.59 | 1.61 | 148 |
| stroke 6 | 50 % → 80 % | 0.59 | 1.59 | 176 |
| stroke 7 | 51 % → 78 % | 0.59 | 1.53 | 244 |
| stroke 8 | 49 % → 76 % | 0.59 | 1.55 | 209 |
| stroke 9 | 52 % → 80 % | 0.59 | 1.53 | 180 |
| stroke 10 | 54 % → 76 % | 0.59 | 1.39 | 231 |
| stroke 11 | 52 % → 74 % | 0.59 | 1.43 | 192 |
| stroke 12 | 50 % → 74 % | 0.59 | 1.48 | 246 |
| stroke 13 | 45 % → 72 % | 0.59 | 1.61 | 200 |
| stroke 14 | 45 % → 63 % | 0.59 | 1.42 | 192 |
| stroke 15 | 48 % → 58 % | 0.59 | 1.21 | 159 |
| stroke 16 | 55 % → 54 % | 0.59 | 0.99 | 189 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #31 Warhol blotted line — own sheet
own sheet 600 × 600 · Ink · 6 px · 6.3 s

![Brush Artist · Refs · #31 Warhol blotted line — own sheet](Brush-Artist-Refs-31-Warhol-blotted-line-own-sheet.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| stroke 1 | 24 % → 47 % | 0.83 | 1.93 | 115 |
| stroke 2 | 19 % → 24 % | 0.83 | 1.27 | 95 |
| stroke 3 | 27 % → 28 % | 0.82 | 1.02 | 100 |
| stroke 4 | 31 % → 41 % | 0.83 | 1.32 | 75 |
| stroke 5 | 38 % → 46 % | 0.83 | 1.21 | 108 |
| stroke 6 | 35 % → 36 % | 0.82 | 1.02 | 110 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #32 Thick orange swipes — own sheet
own sheet 600 × 600 · Heavy acrylic · 90 px · 5.2 s

![Brush Artist · Refs · #32 Thick orange swipes — own sheet](Brush-Artist-Refs-32-Thick-orange-swipes-own-sheet.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| stroke 1 | 28 % → 28 % | 0.39 | 1.00 | 567 |
| stroke 2 | 29 % → 32 % | 0.39 | 1.13 | 482 |
| stroke 3 | 32 % → 32 % | 0.39 | 0.98 | 560 |

## Brush Artist · Refs · #33 Red wet-in-wet band — own sheet
own sheet 600 × 600 · Watercolor · 80 px · 8.0 s

![Brush Artist · Refs · #33 Red wet-in-wet band — own sheet](Brush-Artist-Refs-33-Red-wet-in-wet-band-own-sheet.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| stroke 1 | 46 % → 65 % | 0.55 | 1.41 | 495 |
| stroke 2 | 53 % → 66 % | 0.56 | 1.26 | 105 |
| stroke 3 | 64 % → 78 % | 0.56 | 1.21 | 112 |
| stroke 4 | 66 % → 77 % | 0.56 | 1.16 | 89 |
| stroke 5 | 61 % → 74 % | 0.56 | 1.20 | 119 |
| stroke 6 | 64 % → 64 % | 0.56 | 1.00 | 142 |

## Brush Artist · Refs · #34 Magenta oil patches — own sheet
own sheet 600 × 600 · Oil · 60 px · 4.5 s

![Brush Artist · Refs · #34 Magenta oil patches — own sheet](Brush-Artist-Refs-34-Magenta-oil-patches-own-sheet.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| stroke 1 | 24 % → 44 % | 0.62 | 1.87 | 96 |
| stroke 2 | 22 % → 37 % | 0.62 | 1.69 | 86 |
| stroke 3 | 21 % → 51 % | 0.62 | 2.42 | 85 |
| stroke 4 | 31 % → 31 % | 0.62 | 1.00 | 70 |
| stroke 5 | 27 % → 40 % | 0.62 | 1.46 | 93 |
| stroke 6 | 27 % → 45 % | 0.62 | 1.66 | 60 |
| stroke 7 | 29 % → 41 % | 0.62 | 1.42 | 71 |
| stroke 8 | 52 % → 55 % | 0.62 | 1.07 | 91 |
| stroke 9 | 34 % → 38 % | 0.62 | 1.13 | 86 |
| stroke 10 | 48 % → 48 % | 0.62 | 1.00 | 67 |
| stroke 11 | 60 % → 60 % | 0.62 | 1.00 | 78 |
| stroke 12 | 35 % → 35 % | 0.62 | 1.00 | 80 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #35 Red band with runs — own sheet
own sheet 600 × 600 · Watercolor · 70 px · 4.5 s

![Brush Artist · Refs · #35 Red band with runs — own sheet](Brush-Artist-Refs-35-Red-band-with-runs-own-sheet.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| stroke 1 | 43 % → 42 % | 0.53 | 1.00 | 335 |

## Brush Artist · Refs · #36 Magenta letters flat brush — own sheet
own sheet 600 × 600 · Gouache · 36 px · 11.1 s

![Brush Artist · Refs · #36 Magenta letters flat brush — own sheet](Brush-Artist-Refs-36-Magenta-letters-flat-brush-own-sheet.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| stroke 1 | 46 % → 46 % | 0.50 | 1.00 | 34 |
| stroke 2 | 38 % → 48 % | 0.50 | 1.25 | 32 |
| stroke 3 | 56 % → 63 % | 0.50 | 1.12 | 29 |
| stroke 4 | 45 % → 53 % | 0.50 | 1.19 | 101 |
| stroke 5 | 41 % → 53 % | 0.50 | 1.29 | 71 |
| stroke 6 | 78 % → 76 % | 0.50 | 0.97 | 16 |
| stroke 7 | 43 % → 50 % | 0.50 | 1.15 | 118 |
| stroke 8 | 39 % → 59 % | 0.50 | 1.52 | 66 |
| stroke 9 | 54 % → 53 % | 0.50 | 0.98 | 28 |
| stroke 10 | 42 % → 61 % | 0.50 | 1.44 | 77 |
| stroke 11 | 78 % → 77 % | 0.50 | 0.98 | 21 |
| stroke 12 | 58 % → 68 % | 0.50 | 1.17 | 108 |
| stroke 13 | 43 % → 50 % | 0.50 | 1.18 | 31 |
| stroke 14 | 52 % → 73 % | 0.50 | 1.40 | 31 |
| stroke 15 | 44 % → 52 % | 0.50 | 1.18 | 68 |
| stroke 16 | 78 % → 76 % | 0.50 | 0.98 | 26 |
| stroke 17 | 53 % → 61 % | 0.50 | 1.15 | 141 |
| stroke 18 | 40 % → 47 % | 0.50 | 1.17 | 49 |
| stroke 19 | 65 % → 63 % | 0.50 | 0.97 | 41 |
| stroke 20 | 56 % → 55 % | 0.50 | 0.97 | 38 |
| stroke 21 | 47 % → 46 % | 0.50 | 0.96 | 125 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #37 Oil still life dabs — own sheet
own sheet 600 × 600 · Oil · 40 px · 4.1 s

![Brush Artist · Refs · #37 Oil still life dabs — own sheet](Brush-Artist-Refs-37-Oil-still-life-dabs-own-sheet.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| stroke 1 | 20 % → 20 % | 0.39 | 1.00 | 30 |
| stroke 2 | 18 % → 48 % | 0.39 | 2.67 | 22 |
| stroke 3 | 22 % → 48 % | 0.40 | 2.12 | 20 |
| stroke 4 | 22 % → 22 % | 0.39 | 1.00 | 39 |
| stroke 5 | 17 % → 18 % | 0.38 | 1.04 | 21 |
| stroke 6 | 37 % → 45 % | 0.39 | 1.24 | 29 |
| stroke 7 | 16 % → 27 % | 0.38 | 1.71 | 13 |
| stroke 8 | 14 % → 29 % | 0.38 | 2.08 | 15 |
| stroke 9 | 23 % → 23 % | 0.39 | 1.00 | 35 |
| stroke 10 | 31 % → 36 % | 0.39 | 1.18 | 46 |
| stroke 11 | 39 % → 39 % | 0.39 | 1.00 | 30 |
| stroke 12 | 31 % → 31 % | 0.38 | 1.00 | 19 |
| stroke 13 | 17 % → 17 % | 0.37 | 1.00 | 22 |
| stroke 14 | 35 % → 35 % | 0.39 | 1.00 | 19 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #38 Sanguine drawing — own sheet
own sheet 600 × 600 · Pastel · 6 px · 2.7 s

![Brush Artist · Refs · #38 Sanguine drawing — own sheet](Brush-Artist-Refs-38-Sanguine-drawing-own-sheet.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| stroke 1 | 5 % → 22 % | 0.61 | 4.30 | 8 |
| stroke 2 | 5 % → 11 % | 0.61 | 2.18 | 7 |
| stroke 3 | 5 % → 13 % | 0.61 | 2.67 | 8 |
| stroke 4 | 5 % → 30 % | 0.61 | 5.95 | 9 |
| stroke 5 | 5 % → 13 % | 0.61 | 2.56 | 6 |
| stroke 6 | 5 % → 31 % | 0.61 | 5.75 | 7 |
| stroke 7 | 8 % → 23 % | 0.61 | 2.82 | 10 |
| stroke 8 | 7 % → 24 % | 0.60 | 3.35 | 7 |
| stroke 9 | 5 % → 12 % | 0.61 | 2.27 | 13 |
| stroke 10 | 7 % → 26 % | 0.61 | 3.69 | 8 |
| stroke 11 | 5 % → 7 % | 0.61 | 1.48 | 9 |
| stroke 12 | 8 % → 25 % | 0.61 | 3.04 | 11 |
| stroke 13 | 13 % → 27 % | 0.61 | 2.02 | 9 |
| stroke 14 | 8 % → 22 % | 0.61 | 2.84 | 8 |
| stroke 15 | 16 % → 28 % | 0.61 | 1.75 | 7 |
| stroke 16 | 10 % → 25 % | 0.61 | 2.58 | 9 |
| stroke 17 | 7 % → 14 % | 0.61 | 2.05 | 7 |
| stroke 18 | 5 % → 9 % | 0.60 | 1.71 | 8 |
| stroke 19 | 10 % → 26 % | 0.61 | 2.72 | 9 |
| stroke 20 | 12 % → 22 % | 0.61 | 1.77 | 14 |
| stroke 21 | 7 % → 7 % | 0.61 | 1.00 | 7 |
| stroke 22 | 14 % → 21 % | 0.61 | 1.58 | 7 |
| stroke 23 | 11 % → 17 % | 0.61 | 1.54 | 7 |
| stroke 24 | 7 % → 11 % | 0.60 | 1.48 | 6 |
| stroke 25 | 13 % → 24 % | 0.61 | 1.86 | 7 |
| stroke 26 | 9 % → 12 % | 0.61 | 1.30 | 6 |
| stroke 27 | 7 % → 7 % | 0.60 | 1.04 | 6 |
| stroke 28 | 12 % → 19 % | 0.61 | 1.54 | 6 |
| stroke 29 | 13 % → 27 % | 0.61 | 2.17 | 7 |
| stroke 30 | 23 % → 28 % | 0.61 | 1.26 | 10 |
| stroke 31 | 9 % → 11 % | 0.61 | 1.21 | 8 |
| stroke 32 | 18 % → 21 % | 0.61 | 1.14 | 10 |
| stroke 33 | 12 % → 12 % | 0.61 | 1.05 | 10 |
| stroke 34 | 17 % → 22 % | 0.61 | 1.30 | 9 |
| stroke 35 | 15 % → 24 % | 0.61 | 1.56 | 11 |
| stroke 36 | 16 % → 21 % | 0.61 | 1.27 | 7 |
| stroke 37 | 17 % → 27 % | 0.61 | 1.57 | 9 |
| stroke 38 | 21 % → 32 % | 0.61 | 1.48 | 10 |
| stroke 39 | 23 % → 28 % | 0.61 | 1.20 | 9 |
| stroke 40 | 10 % → 11 % | 0.61 | 1.16 | 8 |
| stroke 41 | 26 % → 26 % | 0.61 | 1.00 | 13 |
| stroke 42 | 22 % → 26 % | 0.61 | 1.15 | 9 |
| stroke 43 | 17 % → 20 % | 0.61 | 1.17 | 8 |
| stroke 44 | 20 % → 24 % | 0.61 | 1.19 | 8 |
| stroke 45 | 5 % → 5 % | 0.61 | 1.00 | 13 |
| stroke 46 | 27 % → 27 % | 0.61 | 1.00 | 8 |
| stroke 47 | 22 % → 22 % | 0.61 | 1.00 | 9 |
| stroke 48 | 20 % → 21 % | 0.61 | 1.04 | 7 |
| stroke 49 | 31 % → 31 % | 0.61 | 1.00 | 9 |
| stroke 50 | 16 % → 16 % | 0.61 | 1.00 | 11 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #39 Very thick impasto — own sheet
own sheet 600 × 600 · Heavy acrylic · 60 px · 4.5 s

![Brush Artist · Refs · #39 Very thick impasto — own sheet](Brush-Artist-Refs-39-Very-thick-impasto-own-sheet.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| stroke 1 | 38 % → 37 % | 0.63 | 0.97 | 284 |
| stroke 2 | 37 % → 40 % | 0.63 | 1.08 | 286 |
| stroke 3 | 40 % → 39 % | 0.63 | 0.97 | 247 |
| stroke 4 | 39 % → 38 % | 0.63 | 0.97 | 269 |
| stroke 5 | 35 % → 34 % | 0.63 | 0.97 | 258 |

## Brush Artist · Refs · #40 Watercolour blooms — own sheet
own sheet 600 × 600 · Watercolor · 90 px · 5.6 s

![Brush Artist · Refs · #40 Watercolour blooms — own sheet](Brush-Artist-Refs-40-Watercolour-blooms-own-sheet.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| stroke 1 | 41 % → 41 % | 0.25 | 1.00 | 736 |

## Brush Artist · Refs · #41 Coloured pencil hatching — own sheet
own sheet 600 × 600 · Pastel · 4 px · 2.7 s

![Brush Artist · Refs · #41 Coloured pencil hatching — own sheet](Brush-Artist-Refs-41-Coloured-pencil-hatching-own-sheet.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| stroke 1 | 6 % → 22 % | 0.42 | 4.02 | 5 |
| stroke 2 | 6 % → 12 % | 0.42 | 2.09 | 5 |
| stroke 3 | 5 % → 18 % | 0.42 | 3.60 | 4 |
| stroke 4 | 6 % → 30 % | 0.43 | 5.26 | 4 |
| stroke 5 | 8 % → 11 % | 0.42 | 1.44 | 4 |
| stroke 6 | 6 % → 21 % | 0.43 | 3.59 | 4 |
| stroke 7 | 6 % → 24 % | 0.42 | 3.73 | 4 |
| stroke 8 | 6 % → 18 % | 0.42 | 3.29 | 4 |
| stroke 9 | 9 % → 18 % | 0.42 | 2.09 | 4 |
| stroke 10 | 8 % → 26 % | 0.42 | 3.18 | 4 |
| stroke 11 | 7 % → 21 % | 0.42 | 3.00 | 4 |
| stroke 12 | 5 % → 5 % | 0.41 | 1.00 | 4 |
| stroke 13 | 12 % → 26 % | 0.43 | 2.17 | 4 |
| stroke 14 | 6 % → 23 % | 0.42 | 4.07 | 4 |
| stroke 15 | 11 % → 20 % | 0.43 | 1.80 | 5 |
| stroke 16 | 12 % → 17 % | 0.42 | 1.47 | 4 |
| stroke 17 | 6 % → 6 % | 0.42 | 1.00 | 4 |
| stroke 18 | 8 % → 13 % | 0.43 | 1.55 | 4 |
| stroke 19 | 9 % → 21 % | 0.43 | 2.34 | 4 |
| stroke 20 | 9 % → 24 % | 0.42 | 2.78 | 4 |
| stroke 21 | 7 % → 24 % | 0.42 | 3.21 | 4 |
| stroke 22 | 16 % → 27 % | 0.42 | 1.72 | 4 |
| stroke 23 | 16 % → 22 % | 0.42 | 1.39 | 4 |
| stroke 24 | 11 % → 23 % | 0.42 | 2.09 | 4 |
| stroke 25 | 8 % → 16 % | 0.43 | 1.93 | 4 |
| stroke 26 | 6 % → 9 % | 0.42 | 1.36 | 4 |
| stroke 27 | 6 % → 12 % | 0.42 | 1.89 | 4 |
| stroke 28 | 9 % → 14 % | 0.42 | 1.62 | 4 |
| stroke 29 | 6 % → 22 % | 0.43 | 3.79 | 4 |
| stroke 30 | 10 % → 15 % | 0.42 | 1.45 | 4 |
| stroke 31 | 12 % → 24 % | 0.43 | 2.00 | 4 |
| stroke 32 | 6 % → 11 % | 0.43 | 1.85 | 5 |
| stroke 33 | 10 % → 17 % | 0.42 | 1.70 | 5 |
| stroke 34 | 6 % → 10 % | 0.43 | 1.49 | 5 |
| stroke 35 | 11 % → 22 % | 0.43 | 1.98 | 4 |
| stroke 36 | 9 % → 9 % | 0.43 | 1.00 | 5 |
| stroke 37 | 12 % → 23 % | 0.42 | 1.89 | 4 |
| stroke 38 | 13 % → 22 % | 0.42 | 1.61 | 4 |
| stroke 39 | 12 % → 19 % | 0.43 | 1.56 | 4 |
| stroke 40 | 12 % → 27 % | 0.43 | 2.16 | 6 |
| stroke 41 | 15 % → 20 % | 0.43 | 1.37 | 12 |
| stroke 42 | 16 % → 26 % | 0.43 | 1.68 | 14 |
| stroke 43 | 9 % → 14 % | 0.42 | 1.65 | 10 |
| stroke 44 | 17 % → 23 % | 0.42 | 1.32 | 4 |
| stroke 45 | 21 % → 28 % | 0.42 | 1.32 | 6 |
| stroke 46 | 9 % → 11 % | 0.42 | 1.29 | 4 |
| stroke 47 | 18 % → 21 % | 0.42 | 1.20 | 5 |
| stroke 48 | 19 % → 25 % | 0.43 | 1.33 | 4 |
| stroke 49 | 9 % → 16 % | 0.42 | 1.73 | 5 |
| stroke 50 | 12 % → 12 % | 0.42 | 1.00 | 4 |
| stroke 51 | 16 % → 27 % | 0.42 | 1.72 | 4 |
| stroke 52 | 20 % → 24 % | 0.42 | 1.19 | 4 |
| stroke 53 | 17 % → 23 % | 0.43 | 1.34 | 4 |
| stroke 54 | 16 % → 24 % | 0.43 | 1.52 | 4 |
| stroke 55 | 17 % → 22 % | 0.43 | 1.29 | 6 |
| stroke 56 | 18 % → 20 % | 0.43 | 1.09 | 4 |
| stroke 57 | 17 % → 23 % | 0.42 | 1.35 | 4 |
| stroke 58 | 18 % → 21 % | 0.42 | 1.12 | 4 |
| stroke 59 | 19 % → 22 % | 0.43 | 1.15 | 4 |
| stroke 60 | 25 % → 31 % | 0.43 | 1.24 | 4 |
| stroke 61 | 31 % → 32 % | 0.43 | 1.03 | 6 |
| stroke 62 | 17 % → 17 % | 0.42 | 1.00 | 6 |
| stroke 63 | 18 % → 19 % | 0.43 | 1.09 | 5 |
| stroke 64 | 25 % → 26 % | 0.42 | 1.02 | 4 |
| stroke 65 | 27 % → 27 % | 0.42 | 1.00 | 4 |
| stroke 66 | 23 % → 23 % | 0.42 | 1.00 | 4 |
| stroke 67 | 20 % → 21 % | 0.42 | 1.03 | 4 |
| stroke 68 | 8 % → 15 % | 0.42 | 1.83 | 4 |
| stroke 69 | 10 % → 10 % | 0.42 | 1.00 | 5 |
| stroke 70 | 17 % → 21 % | 0.43 | 1.26 | 4 |
| stroke 71 | 15 % → 18 % | 0.42 | 1.19 | 4 |
| stroke 72 | 10 % → 12 % | 0.42 | 1.17 | 4 |
| stroke 73 | 22 % → 22 % | 0.42 | 1.00 | 4 |
| stroke 74 | 24 % → 24 % | 0.43 | 1.00 | 5 |
| stroke 75 | 25 % → 25 % | 0.42 | 1.00 | 4 |
| stroke 76 | 21 % → 21 % | 0.43 | 1.00 | 4 |
| stroke 77 | 11 % → 16 % | 0.42 | 1.38 | 4 |
| stroke 78 | 17 % → 17 % | 0.42 | 1.00 | 4 |
| stroke 79 | 13 % → 13 % | 0.42 | 1.00 | 6 |
| stroke 80 | 18 % → 18 % | 0.42 | 1.00 | 4 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #42 Oil pastel shaggy — own sheet
own sheet 600 × 600 · Pastel · 18 px · 2.7 s

![Brush Artist · Refs · #42 Oil pastel shaggy — own sheet](Brush-Artist-Refs-42-Oil-pastel-shaggy-own-sheet.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| stroke 1 | 13 % → 28 % | 0.07 | 2.12 | 11 |
| stroke 2 | 15 % → 35 % | 0.07 | 2.34 | 10 |
| stroke 3 | 15 % → 44 % | 0.07 | 2.94 | 10 |
| stroke 4 | 15 % → 28 % | 0.07 | 1.95 | 10 |
| stroke 5 | 17 % → 29 % | 0.07 | 1.72 | 10 |
| stroke 6 | 15 % → 41 % | 0.07 | 2.70 | 10 |
| stroke 7 | 22 % → 53 % | 0.07 | 2.47 | 10 |
| stroke 8 | 16 % → 59 % | 0.07 | 3.60 | 10 |
| stroke 9 | 19 % → 31 % | 0.07 | 1.66 | 10 |
| stroke 10 | 15 % → 28 % | 0.07 | 1.82 | 10 |
| stroke 11 | 15 % → 38 % | 0.07 | 2.57 | 9 |
| stroke 12 | 20 % → 27 % | 0.07 | 1.38 | 9 |
| stroke 13 | 26 % → 41 % | 0.07 | 1.57 | 10 |
| stroke 14 | 14 % → 29 % | 0.07 | 2.09 | 9 |
| stroke 15 | 15 % → 46 % | 0.07 | 3.08 | 10 |
| stroke 16 | 22 % → 43 % | 0.08 | 1.90 | 10 |
| stroke 17 | 31 % → 53 % | 0.07 | 1.71 | 10 |
| stroke 18 | 32 % → 44 % | 0.08 | 1.35 | 10 |
| stroke 19 | 31 % → 54 % | 0.07 | 1.73 | 10 |
| stroke 20 | 34 % → 56 % | 0.07 | 1.66 | 10 |
| stroke 21 | 20 % → 27 % | 0.07 | 1.35 | 9 |
| stroke 22 | 20 % → 23 % | 0.07 | 1.15 | 10 |
| stroke 23 | 27 % → 34 % | 0.07 | 1.28 | 10 |
| stroke 24 | 38 % → 44 % | 0.08 | 1.14 | 10 |
| stroke 25 | 30 % → 45 % | 0.07 | 1.52 | 20 |
| stroke 26 | 15 % → 31 % | 0.07 | 2.00 | 9 |
| stroke 27 | 40 % → 44 % | 0.08 | 1.11 | 10 |
| stroke 28 | 27 % → 42 % | 0.07 | 1.55 | 12 |
| stroke 29 | 15 % → 38 % | 0.07 | 2.46 | 10 |
| stroke 30 | 19 % → 49 % | 0.07 | 2.59 | 30 |
| stroke 31 | 23 % → 24 % | 0.07 | 1.01 | 10 |
| stroke 32 | 29 % → 44 % | 0.07 | 1.55 | 10 |
| stroke 33 | 28 % → 28 % | 0.07 | 1.02 | 10 |
| stroke 34 | 41 % → 48 % | 0.07 | 1.16 | 14 |
| stroke 35 | 41 % → 51 % | 0.07 | 1.25 | 9 |
| stroke 36 | 36 % → 38 % | 0.07 | 1.05 | 10 |
| stroke 37 | 29 % → 29 % | 0.07 | 1.00 | 10 |
| stroke 38 | 39 % → 47 % | 0.07 | 1.22 | 14 |
| stroke 39 | 23 % → 36 % | 0.07 | 1.59 | 9 |
| stroke 40 | 48 % → 56 % | 0.07 | 1.18 | 11 |
| stroke 41 | 44 % → 47 % | 0.07 | 1.05 | 11 |
| stroke 42 | 29 % → 39 % | 0.07 | 1.33 | 9 |
| stroke 43 | 21 % → 21 % | 0.07 | 1.00 | 10 |
| stroke 44 | 41 % → 52 % | 0.07 | 1.27 | 11 |
| stroke 45 | 36 % → 36 % | 0.07 | 1.00 | 10 |
| stroke 46 | 53 % → 57 % | 0.07 | 1.09 | 10 |
| stroke 47 | 54 % → 60 % | 0.07 | 1.11 | 11 |
| stroke 48 | 35 % → 39 % | 0.07 | 1.11 | 18 |
| stroke 49 | 41 % → 44 % | 0.07 | 1.06 | 10 |
| stroke 50 | 53 % → 56 % | 0.07 | 1.05 | 10 |
| stroke 51 | 27 % → 27 % | 0.07 | 1.00 | 15 |
| stroke 52 | 48 % → 48 % | 0.07 | 1.00 | 18 |
| stroke 53 | 32 % → 33 % | 0.07 | 1.02 | 10 |
| stroke 54 | 36 % → 39 % | 0.07 | 1.09 | 9 |
| stroke 55 | 23 % → 23 % | 0.07 | 1.00 | 9 |
| stroke 56 | 29 % → 29 % | 0.07 | 1.00 | 9 |
| stroke 57 | 45 % → 45 % | 0.08 | 1.00 | 10 |
| stroke 58 | 40 % → 40 % | 0.07 | 1.00 | 11 |
| stroke 59 | 65 % → 65 % | 0.07 | 1.00 | 9 |
| stroke 60 | 25 % → 25 % | 0.07 | 1.00 | 9 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #43 Dragged black ink blocks — own sheet
own sheet 600 × 600 · Gouache · 70 px · 8.7 s

![Brush Artist · Refs · #43 Dragged black ink blocks — own sheet](Brush-Artist-Refs-43-Dragged-black-ink-blocks-own-sheet.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| stroke 1 | 46 % → 29 % | 0.64 | 0.62 | 477 |
| stroke 2 | 35 % → 22 % | 0.64 | 0.62 | 470 |
| stroke 3 | 36 % → 25 % | 0.64 | 0.70 | 460 |
| stroke 4 | 39 % → 24 % | 0.64 | 0.60 | 395 |
| stroke 5 | 44 % → 29 % | 0.64 | 0.66 | 451 |

## Brush Artist · Refs · #44 Blue looping ribbon — own sheet
own sheet 600 × 600 · Oil · 80 px · 6.2 s

![Brush Artist · Refs · #44 Blue looping ribbon — own sheet](Brush-Artist-Refs-44-Blue-looping-ribbon-own-sheet.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| stroke 1 | 48 % → 48 % | 0.72 | 1.00 | 2623 |

## Brush Artist · Refs · #45 Soft pastel pepper — own sheet
own sheet 600 × 600 · Pastel · 40 px · 3.8 s

![Brush Artist · Refs · #45 Soft pastel pepper — own sheet](Brush-Artist-Refs-45-Soft-pastel-pepper-own-sheet.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| stroke 1 | 19 % → 39 % | 0.53 | 2.12 | 331 |
| stroke 2 | 30 % → 44 % | 0.53 | 1.44 | 344 |
| stroke 3 | 39 % → 49 % | 0.53 | 1.24 | 383 |
| stroke 4 | 37 % → 42 % | 0.53 | 1.12 | 403 |
| stroke 5 | 43 % → 43 % | 0.53 | 1.00 | 291 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #46 Red-brown ink lips — own sheet
own sheet 600 × 600 · Watercolor · 70 px · 4.7 s

![Brush Artist · Refs · #46 Red-brown ink lips — own sheet](Brush-Artist-Refs-46-Red-brown-ink-lips-own-sheet.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| stroke 1 | 32 % → 45 % | 0.59 | 1.43 | 201 |
| stroke 2 | 48 % → 48 % | 0.59 | 1.00 | 168 |

## Brush Artist · Refs · #47 Pink knife slabs — own sheet
own sheet 600 × 600 · Heavy acrylic · 90 px · 4.2 s

![Brush Artist · Refs · #47 Pink knife slabs — own sheet](Brush-Artist-Refs-47-Pink-knife-slabs-own-sheet.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| stroke 1 | 28 % → 34 % | 0.18 | 1.18 | 276 |
| stroke 2 | 36 % → 41 % | 0.18 | 1.13 | 273 |
| stroke 3 | 36 % → 41 % | 0.18 | 1.14 | 257 |
| stroke 4 | 37 % → 36 % | 0.18 | 0.98 | 241 |

## Brush Artist · Refs · #48 Black bands with drips — own sheet
own sheet 600 × 600 · Gouache · 70 px · 11.5 s

![Brush Artist · Refs · #48 Black bands with drips — own sheet](Brush-Artist-Refs-48-Black-bands-with-drips-own-sheet.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| stroke 1 | 33 % → 31 % | 0.80 | 0.91 | 414 |
| stroke 2 | 35 % → 32 % | 0.80 | 0.92 | 467 |
| stroke 3 | 33 % → 31 % | 0.80 | 0.93 | 425 |
| stroke 4 | 33 % → 32 % | 0.80 | 0.95 | 415 |

## Brush Artist · Refs · #49 Magenta letters round brush — own sheet
own sheet 600 × 600 · Ink · 30 px · 11.2 s

![Brush Artist · Refs · #49 Magenta letters round brush — own sheet](Brush-Artist-Refs-49-Magenta-letters-round-brush-own-sheet.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| stroke 1 | 61 % → 65 % | 0.52 | 1.06 | 27 |
| stroke 2 | 59 % → 64 % | 0.53 | 1.07 | 29 |
| stroke 3 | 71 % → 80 % | 0.53 | 1.13 | 32 |
| stroke 4 | 54 % → 64 % | 0.52 | 1.18 | 98 |
| stroke 5 | 48 % → 65 % | 0.52 | 1.35 | 68 |
| stroke 6 | 93 % → 94 % | 0.53 | 1.01 | 14 |
| stroke 7 | 61 % → 70 % | 0.52 | 1.15 | 103 |
| stroke 8 | 44 % → 72 % | 0.53 | 1.61 | 58 |
| stroke 9 | 71 % → 71 % | 0.53 | 1.00 | 23 |
| stroke 10 | 51 % → 72 % | 0.52 | 1.42 | 65 |
| stroke 11 | 93 % → 94 % | 0.53 | 1.01 | 14 |
| stroke 12 | 71 % → 83 % | 0.52 | 1.18 | 98 |
| stroke 13 | 61 % → 65 % | 0.53 | 1.05 | 31 |
| stroke 14 | 69 % → 92 % | 0.53 | 1.33 | 29 |
| stroke 15 | 52 % → 63 % | 0.52 | 1.20 | 73 |
| stroke 16 | 93 % → 93 % | 0.53 | 1.00 | 15 |
| stroke 17 | 68 % → 76 % | 0.52 | 1.12 | 133 |
| stroke 18 | 59 % → 62 % | 0.52 | 1.05 | 41 |
| stroke 19 | 81 % → 80 % | 0.53 | 0.99 | 28 |
| stroke 20 | 71 % → 70 % | 0.52 | 1.00 | 29 |
| stroke 21 | 60 % → 59 % | 0.52 | 1.00 | 86 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #50 Thick swipes on photo — own sheet
own sheet 600 × 600 · Heavy acrylic · 40 px · 2.9 s

![Brush Artist · Refs · #50 Thick swipes on photo — own sheet](Brush-Artist-Refs-50-Thick-swipes-on-photo-own-sheet.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| stroke 1 | 24 % → 27 % | 0.23 | 1.12 | 32 |
| stroke 2 | 21 % → 28 % | 0.23 | 1.33 | 29 |
| stroke 3 | 26 % → 24 % | 0.23 | 0.95 | 37 |
| stroke 4 | 26 % → 24 % | 0.23 | 0.94 | 30 |
| stroke 5 | 24 % → 22 % | 0.23 | 0.95 | 32 |
| stroke 6 | 21 % → 19 % | 0.22 | 0.94 | 24 |
| stroke 7 | 36 % → 37 % | 0.23 | 1.02 | 37 |
| stroke 8 | 34 % → 33 % | 0.23 | 0.97 | 29 |
| stroke 9 | 25 % → 23 % | 0.23 | 0.95 | 37 |
| stroke 10 | 28 % → 27 % | 0.22 | 0.95 | 36 |
| stroke 11 | 23 % → 21 % | 0.22 | 0.95 | 29 |
| stroke 12 | 24 % → 23 % | 0.22 | 0.95 | 19 |

## Brush Artist · Ink — dry brush — own sheet
own sheet 600 × 600 · Gouache · 30 px · 4.9 s

![Brush Artist · Ink — dry brush — own sheet](Brush-Artist-Ink-dry-brush-own-sheet.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| ear | 17 % → 4 % | 0.77 | 0.25 | 490 |
| drag0 | 20 % → 24 % | 0.77 | 1.21 | 224 |
| drag1 | 25 % → 25 % | 0.77 | 1.01 | 343 |
| drag2 | 28 % → 26 % | 0.77 | 0.92 | 230 |
| drag3 | 30 % → 26 % | 0.77 | 0.87 | 170 |

