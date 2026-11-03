![All brushes](contact.png)

# Brush Lab — 51 brushes · Nov 3, 2026 at 11:38 AM

Every sheet: 1500 × 600, ten strokes in a 5 × 2 grid — 1. light line · 2. heavy line · 3. pressure swell · 4. fast wave · 5. slow wave · 6. spiral · 7. loop · 8. tilted · 9. over the wet one · 10. long, no reload (cell 8 holds «tilted» and «over the wet one» crossed). The CPU reference of Mamay's paint engine; the wet layer settles 20 s at the end.

Columns: **covered** = share of the cell with paint right after the stroke → after settling; **dark** = mean darkness of the painted pixels above the paper's own grain (0 = paper, 1 = black); **spread** = how far wet paint went beyond the stroke (1.0 = stayed); **ms** = the stroke on the CPU; long stroke: paint in each quarter of its length (it should run out: wet → streaks → dry tail).

## Ink Line
Ink · 12 px · 29.6 s

![Ink Line](Ink-Line.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 1 % → 4 % | 0.55 | 2.44 | 61 |
| heavy line | 5 % → 6 % | 0.68 | 1.13 | 109 |
| pressure swell | 3 % → 4 % | 0.64 | 1.40 | 57 |
| fast wave | 10 % → 11 % | 0.59 | 1.11 | 150 |
| slow wave | 8 % → 10 % | 0.57 | 1.16 | 164 |
| spiral | 14 % → 15 % | 0.50 | 1.07 | 401 |
| loop | 8 % → 9 % | 0.61 | 1.16 | 238 |
| tilted | 5 % → 5 % | 0.65 | 1.05 | 105 |
| over the wet one | 10 % → 11 % | 0.65 | 1.15 | 78 |
| long, no reload | 18 % → 17 % | 0.47 | 0.96 | 514 | quarters: 0.22 → 0.09 → 0.04 → 0.02

Numbers say: wet paint spreads well beyond the stroke.

## Dense Ink
Ink · 14 px · 30.3 s

![Dense Ink](Dense-Ink.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 5 % → 7 % | 0.72 | 1.26 | 83 |
| heavy line | 7 % → 7 % | 0.73 | 1.09 | 105 |
| pressure swell | 5 % → 6 % | 0.72 | 1.17 | 67 |
| fast wave | 13 % → 13 % | 0.69 | 1.01 | 180 |
| slow wave | 12 % → 12 % | 0.67 | 1.04 | 199 |
| spiral | 18 % → 15 % | 0.65 | 0.80 | 428 |
| loop | 11 % → 12 % | 0.69 | 1.08 | 238 |
| tilted | 5 % → 6 % | 0.72 | 1.07 | 116 |
| over the wet one | 12 % → 13 % | 0.72 | 1.11 | 98 |
| long, no reload | 23 % → 15 % | 0.64 | 0.66 | 473 | quarters: 0.30 → 0.12 → 0.04 → 0.02

## Transparent Wash
Watercolor · 22 px · 30.9 s

![Transparent Wash](Transparent-Wash.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 2 % → 5 % | 0.27 | 2.25 | 46 |
| heavy line | 7 % → 9 % | 0.27 | 1.22 | 83 |
| pressure swell | 4 % → 6 % | 0.28 | 1.54 | 49 |
| fast wave | 14 % → 16 % | 0.20 | 1.17 | 152 |
| slow wave | 12 % → 15 % | 0.21 | 1.28 | 192 |
| spiral | 18 % → 22 % | 0.16 | 1.23 | 319 |
| loop | 11 % → 13 % | 0.22 | 1.20 | 209 |
| tilted | 8 % → 8 % | 0.24 | 1.06 | 118 |
| over the wet one | 13 % → 16 % | 0.24 | 1.18 | 68 |
| long, no reload | 26 % → 32 % | 0.13 | 1.22 | 489 | quarters: 0.11 → 0.04 → 0.02 → 0.01

Numbers say: wet paint spreads well beyond the stroke.

## Dry Brush
Gouache · 24 px · 22.9 s

![Dry Brush](Dry-Brush.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 5 % → 0 % | 0.65 | 0.09 | 44 |
| heavy line | 6 % → 0 % | 0.65 | 0.02 | 88 |
| pressure swell | 5 % → 0 % | 0.65 | 0.08 | 66 |
| fast wave | 6 % → 1 % | 0.65 | 0.08 | 155 |
| slow wave | 7 % → 0 % | 0.65 | 0.06 | 342 |
| spiral | 7 % → 0 % | 0.65 | 0.07 | 259 |
| loop | 10 % → 0 % | 0.65 | 0.04 | 141 |
| tilted | 4 % → 3 % | 0.65 | 0.88 | 81 |
| over the wet one | 9 % → 1 % | 0.65 | 0.12 | 66 |
| long, no reload | 6 % → 1 % | 0.65 | 0.14 | 346 | quarters: 0.12 → 0.00 → 0.00 → 0.00

## Wax Crayon
Wax · 8 px · 10.3 s

![Wax Crayon](Wax-Crayon.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 1 % → 1 % | 0.71 | 1.00 | 18 |
| heavy line | 1 % → 1 % | 0.69 | 1.00 | 20 |
| pressure swell | 1 % → 1 % | 0.70 | 1.00 | 13 |
| fast wave | 3 % → 3 % | 0.69 | 1.00 | 44 |
| slow wave | 3 % → 3 % | 0.70 | 1.00 | 43 |
| spiral | 5 % → 5 % | 0.70 | 1.00 | 82 |
| loop | 3 % → 3 % | 0.70 | 1.00 | 55 |
| tilted | 2 % → 2 % | 0.68 | 1.00 | 38 |
| over the wet one | 3 % → 3 % | 0.68 | 1.00 | 26 |
| long, no reload | 7 % → 7 % | 0.70 | 1.00 | 140 | quarters: 0.06 → 0.06 → 0.06 → 0.06

Numbers say: the long stroke does not run out of paint.

## Oil Pastel
Wax · 12 px · 10.4 s

![Oil Pastel](Oil-Pastel.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 1 % → 1 % | 0.68 | 1.00 | 26 |
| heavy line | 2 % → 2 % | 0.68 | 1.00 | 31 |
| pressure swell | 2 % → 2 % | 0.69 | 1.00 | 26 |
| fast wave | 5 % → 5 % | 0.68 | 1.00 | 67 |
| slow wave | 5 % → 5 % | 0.68 | 1.00 | 91 |
| spiral | 8 % → 8 % | 0.68 | 1.00 | 132 |
| loop | 4 % → 4 % | 0.68 | 1.00 | 84 |
| tilted | 2 % → 2 % | 0.68 | 1.00 | 39 |
| over the wet one | 5 % → 5 % | 0.68 | 1.00 | 25 |
| long, no reload | 13 % → 13 % | 0.68 | 1.00 | 156 | quarters: 0.10 → 0.09 → 0.10 → 0.10

Numbers say: the long stroke does not run out of paint.

## Charcoal
Charcoal · 5 px · 12.6 s

![Charcoal](Charcoal.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 1 % → 1 % | 0.74 | 1.00 | 12 |
| heavy line | 1 % → 1 % | 0.74 | 1.00 | 12 |
| pressure swell | 1 % → 1 % | 0.74 | 1.00 | 9 |
| fast wave | 2 % → 2 % | 0.73 | 1.00 | 33 |
| slow wave | 2 % → 2 % | 0.74 | 1.00 | 30 |
| spiral | 4 % → 4 % | 0.74 | 1.00 | 58 |
| loop | 2 % → 2 % | 0.74 | 1.00 | 29 |
| tilted | 2 % → 2 % | 0.72 | 1.00 | 21 |
| over the wet one | 2 % → 2 % | 0.72 | 1.00 | 14 |
| long, no reload | 6 % → 6 % | 0.73 | 1.00 | 103 | quarters: 0.05 → 0.05 → 0.05 → 0.05

Numbers say: the long stroke does not run out of paint.

## Impasto
Heavy acrylic · 22 px · 20.8 s

![Impasto](Impasto.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 8 % → 8 % | 0.71 | 0.93 | 51 |
| heavy line | 10 % → 9 % | 0.70 | 0.94 | 112 |
| pressure swell | 7 % → 7 % | 0.72 | 0.94 | 62 |
| fast wave | 20 % → 13 % | 0.71 | 0.64 | 201 |
| slow wave | 21 % → 14 % | 0.71 | 0.66 | 551 |
| spiral | 30 % → 14 % | 0.71 | 0.46 | 526 |
| loop | 18 % → 14 % | 0.71 | 0.77 | 236 |
| tilted | 8 % → 8 % | 0.70 | 1.00 | 119 |
| over the wet one | 17 % → 15 % | 0.70 | 0.91 | 107 |
| long, no reload | 34 % → 14 % | 0.71 | 0.41 | 656 | quarters: 0.38 → 0.21 → 0.10 → 0.03

## Oil Round
Oil · 18 px · 29.3 s

![Oil Round](Oil-Round.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 2 % → 2 % | 0.71 | 1.00 | 41 |
| heavy line | 6 % → 6 % | 0.72 | 1.00 | 98 |
| pressure swell | 3 % → 3 % | 0.63 | 1.00 | 65 |
| fast wave | 7 % → 7 % | 0.54 | 1.00 | 209 |
| slow wave | 4 % → 4 % | 0.36 | 1.00 | 292 |
| spiral | 5 % → 5 % | 0.21 | 1.00 | 441 |
| loop | 3 % → 3 % | 0.18 | 1.00 | 220 |
| tilted | 2 % → 2 % | 0.33 | 1.00 | 105 |
| over the wet one | 3 % → 3 % | 0.33 | 1.00 | 83 |
| long, no reload | 8 % → 8 % | 0.17 | 1.00 | 488 | quarters: 0.02 → 0.02 → 0.01 → 0.01

## Palette Knife
Oil · 20 px · 28.9 s

![Palette Knife](Palette-Knife.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 8 % → 8 % | 0.67 | 1.00 | 16 |
| heavy line | 8 % → 8 % | 0.73 | 1.00 | 20 |
| pressure swell | 6 % → 6 % | 0.74 | 1.00 | 7 |
| fast wave | 17 % → 17 % | 0.49 | 1.00 | 36 |
| slow wave | 17 % → 17 % | 0.43 | 1.00 | 90 |
| spiral | 18 % → 18 % | 0.45 | 1.00 | 103 |
| loop | 16 % → 16 % | 0.58 | 1.00 | 27 |
| tilted | 5 % → 5 % | 0.72 | 1.00 | 15 |
| over the wet one | 13 % → 13 % | 0.72 | 1.00 | 13 |
| long, no reload | 17 % → 17 % | 0.47 | 1.00 | 85 | quarters: 0.29 → 0.05 → 0.00 → 0.00

Numbers say: pressure barely changes the width.

## Water
Watercolor · 20 px · 53.9 s · over bands of wet oil paint and oil pastel in turn (it works on paint already there: look at what it does to the bands; covered counts the bands too)

![Water](Water.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 25 % → 26 % | 0.78 | 1.07 | 57 |
| heavy line | 23 % → 24 % | 0.80 | 1.04 | 146 |
| pressure swell | 23 % → 24 % | 0.80 | 1.03 | 71 |
| fast wave | 23 % → 25 % | 0.80 | 1.07 | 178 |
| slow wave | 23 % → 25 % | 0.80 | 1.06 | 233 |
| spiral | 23 % → 25 % | 0.79 | 1.08 | 449 |
| loop | 23 % → 24 % | 0.80 | 1.03 | 311 |
| tilted | 23 % → 23 % | 0.80 | 1.00 | 225 |
| over the wet one | 23 % → 25 % | 0.80 | 1.07 | 86 |
| long, no reload | 23 % → 25 % | 0.80 | 1.08 | 450 | quarters: 0.21 → 0.26 → 0.17 → 0.25

Numbers say: pressure barely changes the width; the long stroke does not run out of paint.

## Blender
Pastel · 16 px · 30.2 s · over bands of wet oil paint and oil pastel in turn (it works on paint already there: look at what it does to the bands; covered counts the bands too)

![Blender](Blender.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 24 % → 24 % | 0.80 | 1.00 | 37 |
| heavy line | 24 % → 24 % | 0.80 | 1.00 | 55 |
| pressure swell | 24 % → 24 % | 0.80 | 1.00 | 46 |
| fast wave | 25 % → 25 % | 0.78 | 1.00 | 110 |
| slow wave | 25 % → 25 % | 0.78 | 1.00 | 144 |
| spiral | 27 % → 27 % | 0.76 | 1.00 | 174 |
| loop | 25 % → 25 % | 0.79 | 1.00 | 125 |
| tilted | 24 % → 24 % | 0.78 | 1.00 | 110 |
| over the wet one | 25 % → 25 % | 0.78 | 1.00 | 68 |
| long, no reload | 29 % → 29 % | 0.74 | 1.00 | 358 | quarters: 0.19 → 0.26 → 0.21 → 0.28

Numbers say: pressure barely changes the width; the long stroke does not run out of paint.

## Eraser
Eraser · 16 px · 29.6 s · over bands of wet oil paint and oil pastel in turn (it works on paint already there: look at what it does to the bands; covered counts the bands too)

![Eraser](Eraser.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 23 % → 23 % | 0.81 | 1.00 | 44 |
| heavy line | 23 % → 23 % | 0.81 | 1.00 | 44 |
| pressure swell | 23 % → 23 % | 0.81 | 1.00 | 41 |
| fast wave | 22 % → 22 % | 0.81 | 1.00 | 118 |
| slow wave | 22 % → 22 % | 0.81 | 1.00 | 135 |
| spiral | 21 % → 21 % | 0.81 | 1.00 | 177 |
| loop | 22 % → 22 % | 0.81 | 1.00 | 123 |
| tilted | 23 % → 23 % | 0.81 | 1.00 | 94 |
| over the wet one | 22 % → 22 % | 0.81 | 1.00 | 66 |
| long, no reload | 19 % → 19 % | 0.81 | 1.00 | 365 | quarters: 0.15 → 0.19 → 0.14 → 0.20

Numbers say: pressure barely changes the width; the long stroke does not run out of paint.

## Fan
Gouache · 30 px · 37.4 s

![Fan](Fan.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 9 % → 3 % | 0.63 | 0.37 | 53 |
| heavy line | 11 % → 4 % | 0.63 | 0.39 | 84 |
| pressure swell | 8 % → 5 % | 0.63 | 0.55 | 47 |
| fast wave | 18 % → 5 % | 0.63 | 0.26 | 125 |
| slow wave | 18 % → 5 % | 0.63 | 0.25 | 210 |
| spiral | 24 % → 5 % | 0.63 | 0.20 | 328 |
| loop | 17 % → 5 % | 0.63 | 0.29 | 143 |
| tilted | 5 % → 6 % | 0.63 | 1.05 | 48 |
| over the wet one | 16 % → 8 % | 0.63 | 0.50 | 50 |
| long, no reload | 23 % → 5 % | 0.63 | 0.22 | 435 | quarters: 0.29 → 0.07 → 0.01 → 0.00

## Sponge
Gouache · 30 px · 37.6 s

![Sponge](Sponge.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 4 % → 0 % | 0.62 | 0.12 | 62 |
| heavy line | 12 % → 2 % | 0.62 | 0.14 | 92 |
| pressure swell | 7 % → 2 % | 0.62 | 0.27 | 72 |
| fast wave | 20 % → 4 % | 0.62 | 0.19 | 173 |
| slow wave | 21 % → 4 % | 0.62 | 0.18 | 278 |
| spiral | 28 % → 4 % | 0.62 | 0.14 | 432 |
| loop | 18 % → 5 % | 0.62 | 0.29 | 177 |
| tilted | 7 % → 7 % | 0.62 | 1.04 | 123 |
| over the wet one | 16 % → 6 % | 0.62 | 0.37 | 55 |
| long, no reload | 29 % → 5 % | 0.62 | 0.17 | 468 | quarters: 0.29 → 0.13 → 0.07 → 0.04

## Ink — sumi brush
Watercolor · 22 px · 37.3 s

![Ink — sumi brush](Ink-sumi-brush.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 6 % → 7 % | 0.46 | 1.06 | 75 |
| heavy line | 10 % → 11 % | 0.38 | 1.05 | 70 |
| pressure swell | 7 % → 8 % | 0.42 | 1.04 | 59 |
| fast wave | 21 % → 21 % | 0.32 | 1.00 | 307 |
| slow wave | 19 % → 19 % | 0.37 | 1.01 | 361 |
| spiral | 28 % → 26 % | 0.30 | 0.92 | 318 |
| loop | 17 % → 18 % | 0.37 | 1.06 | 223 |
| tilted | 6 % → 7 % | 0.40 | 1.17 | 99 |
| over the wet one | 16 % → 16 % | 0.40 | 1.01 | 88 |
| long, no reload | 33 % → 29 % | 0.30 | 0.86 | 466 | quarters: 0.23 → 0.11 → 0.06 → 0.04

## Ink — wash
Watercolor · 40 px · 39.2 s

![Ink — wash](Ink-wash.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 8 % → 9 % | 0.05 | 1.26 | 162 |
| heavy line | 11 % → 13 % | 0.04 | 1.22 | 156 |
| pressure swell | 7 % → 9 % | 0.05 | 1.25 | 80 |
| fast wave | 22 % → 27 % | 0.04 | 1.21 | 363 |
| slow wave | 21 % → 26 % | 0.06 | 1.23 | 766 |
| spiral | 34 % → 41 % | 0.04 | 1.21 | 516 |
| loop | 19 % → 24 % | 0.05 | 1.25 | 322 |
| tilted | 7 % → 9 % | 0.05 | 1.21 | 181 |
| over the wet one | 18 % → 21 % | 0.05 | 1.18 | 116 |
| long, no reload | 39 % → 46 % | 0.05 | 1.19 | 586 | quarters: 0.04 → 0.03 → 0.02 → 0.01

## Ink — dry brush
Ink · 30 px · 29.8 s

![Ink — dry brush](Ink-dry-brush.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 9 % → 7 % | 0.81 | 0.78 | 164 |
| heavy line | 11 % → 8 % | 0.80 | 0.73 | 276 |
| pressure swell | 8 % → 7 % | 0.81 | 0.85 | 97 |
| fast wave | 22 % → 8 % | 0.78 | 0.38 | 316 |
| slow wave | 18 % → 6 % | 0.80 | 0.36 | 809 |
| spiral | 23 % → 8 % | 0.77 | 0.35 | 559 |
| loop | 20 % → 8 % | 0.77 | 0.41 | 370 |
| tilted | 9 % → 9 % | 0.78 | 1.01 | 148 |
| over the wet one | 19 % → 14 % | 0.78 | 0.75 | 136 |
| long, no reload | 20 % → 9 % | 0.78 | 0.42 | 694 | quarters: 0.32 → 0.01 → 0.00 → 0.00

## Ink — nib
Watercolor · 5 px · 26.0 s

![Ink — nib](Ink-nib.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 2 % → 2 % | 0.76 | 1.17 | 41 |
| heavy line | 2 % → 2 % | 0.77 | 1.16 | 52 |
| pressure swell | 1 % → 2 % | 0.78 | 1.22 | 47 |
| fast wave | 4 % → 4 % | 0.66 | 1.09 | 90 |
| slow wave | 4 % → 4 % | 0.68 | 1.11 | 110 |
| spiral | 6 % → 6 % | 0.58 | 1.08 | 204 |
| loop | 3 % → 4 % | 0.69 | 1.12 | 91 |
| tilted | 2 % → 2 % | 0.64 | 1.21 | 44 |
| over the wet one | 4 % → 4 % | 0.64 | 1.03 | 32 |
| long, no reload | 7 % → 7 % | 0.53 | 1.02 | 217 | quarters: 0.09 → 0.04 → 0.03 → 0.02

## 0.45 · Dry brush
Gouache · 34 px · 28.5 s

![0.45 · Dry brush](0-45-Dry-brush.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 11 % → 3 % | 0.67 | 0.28 | 181 |
| heavy line | 12 % → 3 % | 0.67 | 0.30 | 137 |
| pressure swell | 9 % → 4 % | 0.67 | 0.40 | 88 |
| fast wave | 20 % → 4 % | 0.67 | 0.19 | 324 |
| slow wave | 20 % → 4 % | 0.67 | 0.18 | 544 |
| spiral | 21 % → 4 % | 0.67 | 0.17 | 486 |
| loop | 21 % → 4 % | 0.67 | 0.19 | 310 |
| tilted | 9 % → 9 % | 0.67 | 0.97 | 151 |
| over the wet one | 20 % → 7 % | 0.67 | 0.33 | 135 |
| long, no reload | 20 % → 4 % | 0.67 | 0.21 | 653 | quarters: 0.38 → 0.07 → 0.00 → 0.00

Numbers say: pressure barely changes the width.

## Dry pastel
Pastel · 26 px · 11.9 s

![Dry pastel](Dry-pastel.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 5 % → 5 % | 0.36 | 1.00 | 36 |
| heavy line | 6 % → 6 % | 0.36 | 1.00 | 42 |
| pressure swell | 5 % → 5 % | 0.36 | 1.00 | 26 |
| fast wave | 15 % → 15 % | 0.36 | 1.00 | 100 |
| slow wave | 14 % → 14 % | 0.36 | 1.00 | 157 |
| spiral | 23 % → 23 % | 0.36 | 1.00 | 168 |
| loop | 11 % → 11 % | 0.36 | 1.00 | 83 |
| tilted | 5 % → 5 % | 0.37 | 1.00 | 48 |
| over the wet one | 10 % → 10 % | 0.37 | 1.00 | 38 |
| long, no reload | 26 % → 26 % | 0.36 | 1.00 | 213 | quarters: 0.11 → 0.10 → 0.10 → 0.11

Numbers say: the long stroke does not run out of paint.

## 0.45 · Charcoal
Charcoal · 18 px · 11.6 s

![0.45 · Charcoal](0-45-Charcoal.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 4 % → 4 % | 0.79 | 1.00 | 18 |
| heavy line | 4 % → 4 % | 0.79 | 1.00 | 25 |
| pressure swell | 4 % → 4 % | 0.79 | 1.00 | 12 |
| fast wave | 11 % → 11 % | 0.79 | 1.00 | 42 |
| slow wave | 11 % → 11 % | 0.78 | 1.00 | 69 |
| spiral | 20 % → 20 % | 0.79 | 1.00 | 122 |
| loop | 10 % → 10 % | 0.79 | 1.00 | 56 |
| tilted | 4 % → 4 % | 0.78 | 1.00 | 23 |
| over the wet one | 9 % → 9 % | 0.78 | 1.00 | 16 |
| long, no reload | 26 % → 26 % | 0.79 | 1.00 | 108 | quarters: 0.23 → 0.22 → 0.23 → 0.24

Numbers say: pressure barely changes the width; the long stroke does not run out of paint.

## Watercolour — wash
Watercolor · 50 px · 43.1 s

![Watercolour — wash](Watercolour-wash.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 9 % → 11 % | 0.01 | 1.22 | 89 |
| heavy line | 12 % → 14 % | 0.01 | 1.17 | 171 |
| pressure swell | 8 % → 10 % | 0.01 | 1.22 | 73 |
| fast wave | 26 % → 30 % | 0.01 | 1.18 | 270 |
| slow wave | 25 % → 29 % | 0.01 | 1.18 | 425 |
| spiral | 39 % → 46 % | 0.01 | 1.17 | 489 |
| loop | 22 % → 27 % | 0.01 | 1.21 | 237 |
| tilted | 10 % → 11 % | 0.01 | 1.18 | 190 |
| over the wet one | 22 % → 25 % | 0.01 | 1.14 | 102 |
| long, no reload | 45 % → 54 % | 0.01 | 1.18 | 988 | quarters: 0.01 → 0.01 → 0.01 → 0.00

## Watercolour — wet-in-wet
Watercolor · 44 px · 41.9 s

![Watercolour — wet-in-wet](Watercolour-wet-in-wet.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 7 % → 9 % | 0.02 | 1.26 | 106 |
| heavy line | 10 % → 12 % | 0.02 | 1.22 | 106 |
| pressure swell | 7 % → 9 % | 0.02 | 1.21 | 167 |
| fast wave | 23 % → 27 % | 0.02 | 1.17 | 292 |
| slow wave | 22 % → 26 % | 0.02 | 1.18 | 539 |
| spiral | 36 % → 43 % | 0.02 | 1.20 | 479 |
| loop | 19 % → 23 % | 0.02 | 1.20 | 239 |
| tilted | 7 % → 9 % | 0.02 | 1.19 | 169 |
| over the wet one | 17 % → 19 % | 0.02 | 1.12 | 111 |
| long, no reload | 42 % → 49 % | 0.02 | 1.18 | 775 | quarters: 0.01 → 0.01 → 0.01 → 0.01

## Watercolour — glaze
Watercolor · 38 px · 38.8 s

![Watercolour — glaze](Watercolour-glaze.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 7 % → 9 % | 0.01 | 1.28 | 101 |
| heavy line | 10 % → 13 % | 0.01 | 1.25 | 113 |
| pressure swell | 7 % → 9 % | 0.01 | 1.29 | 75 |
| fast wave | 20 % → 25 % | 0.01 | 1.24 | 262 |
| slow wave | 19 % → 24 % | 0.01 | 1.26 | 322 |
| spiral | 31 % → 37 % | 0.01 | 1.21 | 539 |
| loop | 18 % → 23 % | 0.01 | 1.27 | 224 |
| tilted | 7 % → 8 % | 0.01 | 1.20 | 232 |
| over the wet one | 17 % → 20 % | 0.01 | 1.19 | 121 |
| long, no reload | 36 % → 42 % | 0.01 | 1.17 | 1235 | quarters: 0.01 → 0.00 → 0.00 → 0.00

## Watercolour — granulating
Watercolor · 44 px · 38.0 s

![Watercolour — granulating](Watercolour-granulating.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 8 % → 10 % | 0.02 | 1.18 | 75 |
| heavy line | 12 % → 14 % | 0.01 | 1.15 | 101 |
| pressure swell | 8 % → 10 % | 0.02 | 1.18 | 86 |
| fast wave | 25 % → 29 % | 0.01 | 1.15 | 301 |
| slow wave | 24 % → 27 % | 0.02 | 1.16 | 530 |
| spiral | 39 % → 44 % | 0.01 | 1.15 | 363 |
| loop | 22 % → 25 % | 0.01 | 1.17 | 239 |
| tilted | 9 % → 11 % | 0.02 | 1.15 | 167 |
| over the wet one | 21 % → 23 % | 0.02 | 1.11 | 123 |
| long, no reload | 45 % → 52 % | 0.01 | 1.15 | 560 | quarters: 0.01 → 0.01 → 0.01 → 0.01

## Watercolour — dry brush
Watercolor · 36 px · 31.4 s

![Watercolour — dry brush](Watercolour-dry-brush.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 7 % → 8 % | 0.05 | 1.07 | 100 |
| heavy line | 11 % → 12 % | 0.04 | 1.03 | 136 |
| pressure swell | 9 % → 10 % | 0.05 | 1.07 | 85 |
| fast wave | 21 % → 14 % | 0.04 | 0.68 | 269 |
| slow wave | 19 % → 13 % | 0.04 | 0.70 | 511 |
| spiral | 24 % → 15 % | 0.04 | 0.61 | 518 |
| loop | 17 % → 14 % | 0.04 | 0.85 | 274 |
| tilted | 7 % → 8 % | 0.05 | 1.19 | 224 |
| over the wet one | 17 % → 17 % | 0.05 | 0.99 | 197 |
| long, no reload | 22 % → 15 % | 0.04 | 0.68 | 844 | quarters: 0.02 → 0.00 → 0.00 → 0.00

## Gouache
Gouache · 30 px · 31.2 s

![Gouache](Gouache.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 8 % → 6 % | 0.14 | 0.67 | 90 |
| heavy line | 13 % → 6 % | 0.14 | 0.47 | 138 |
| pressure swell | 10 % → 6 % | 0.14 | 0.61 | 80 |
| fast wave | 27 % → 7 % | 0.14 | 0.27 | 371 |
| slow wave | 27 % → 7 % | 0.14 | 0.27 | 499 |
| spiral | 37 % → 8 % | 0.14 | 0.22 | 444 |
| loop | 22 % → 8 % | 0.14 | 0.36 | 173 |
| tilted | 9 % → 9 % | 0.14 | 1.02 | 104 |
| over the wet one | 20 % → 13 % | 0.14 | 0.67 | 100 |
| long, no reload | 38 % → 10 % | 0.14 | 0.25 | 612 | quarters: 0.07 → 0.04 → 0.01 → 0.01

## Oil — alla prima
Oil · 30 px · 24.5 s

![Oil — alla prima](Oil-alla-prima.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 9 % → 9 % | 0.50 | 1.00 | 117 |
| heavy line | 10 % → 10 % | 0.50 | 1.00 | 117 |
| pressure swell | 8 % → 8 % | 0.52 | 1.00 | 110 |
| fast wave | 24 % → 24 % | 0.49 | 1.00 | 383 |
| slow wave | 25 % → 25 % | 0.50 | 1.00 | 371 |
| spiral | 38 % → 38 % | 0.44 | 1.00 | 391 |
| loop | 21 % → 21 % | 0.50 | 1.00 | 244 |
| tilted | 11 % → 11 % | 0.50 | 1.00 | 130 |
| over the wet one | 20 % → 20 % | 0.50 | 1.00 | 105 |
| long, no reload | 46 % → 46 % | 0.40 | 1.00 | 665 | quarters: 0.31 → 0.24 → 0.17 → 0.10

Numbers say: pressure barely changes the width.

## Oil — impasto
Oil · 34 px · 25.6 s

![Oil — impasto](Oil-impasto.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 11 % → 11 % | 0.24 | 1.00 | 165 |
| heavy line | 12 % → 12 % | 0.23 | 1.00 | 164 |
| pressure swell | 9 % → 9 % | 0.25 | 1.00 | 152 |
| fast wave | 29 % → 29 % | 0.21 | 1.00 | 254 |
| slow wave | 29 % → 29 % | 0.21 | 1.00 | 462 |
| spiral | 48 % → 48 % | 0.17 | 1.00 | 583 |
| loop | 25 % → 25 % | 0.21 | 1.00 | 312 |
| tilted | 12 % → 12 % | 0.24 | 1.00 | 173 |
| over the wet one | 23 % → 23 % | 0.24 | 1.00 | 139 |
| long, no reload | 55 % → 55 % | 0.15 | 1.00 | 810 | quarters: 0.16 → 0.11 → 0.06 → 0.02

Numbers say: pressure barely changes the width.

## Oil — glaze
Oil · 40 px · 21.6 s

![Oil — glaze](Oil-glaze.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 10 % → 10 % | 0.49 | 1.00 | 113 |
| heavy line | 14 % → 14 % | 0.48 | 1.00 | 150 |
| pressure swell | 10 % → 10 % | 0.49 | 1.00 | 94 |
| fast wave | 28 % → 28 % | 0.46 | 1.00 | 317 |
| slow wave | 30 % → 30 % | 0.46 | 1.00 | 580 |
| spiral | 42 % → 42 % | 0.44 | 1.00 | 577 |
| loop | 24 % → 24 % | 0.47 | 1.00 | 319 |
| tilted | 11 % → 11 % | 0.47 | 1.00 | 166 |
| over the wet one | 23 % → 23 % | 0.47 | 1.00 | 136 |
| long, no reload | 47 % → 47 % | 0.43 | 1.00 | 850 | quarters: 0.33 → 0.24 → 0.18 → 0.14

## Oil — scumble
Oil · 36 px · 26.4 s

![Oil — scumble](Oil-scumble.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 11 % → 11 % | 0.06 | 1.00 | 177 |
| heavy line | 12 % → 12 % | 0.05 | 1.00 | 187 |
| pressure swell | 9 % → 9 % | 0.06 | 1.00 | 135 |
| fast wave | 18 % → 18 % | 0.04 | 1.00 | 401 |
| slow wave | 20 % → 20 % | 0.04 | 1.00 | 630 |
| spiral | 19 % → 19 % | 0.03 | 1.00 | 609 |
| loop | 22 % → 22 % | 0.04 | 1.00 | 355 |
| tilted | 10 % → 10 % | 0.05 | 1.00 | 205 |
| over the wet one | 21 % → 21 % | 0.05 | 1.00 | 200 |
| long, no reload | 18 % → 18 % | 0.04 | 1.00 | 1096 | quarters: 0.03 → 0.00 → 0.00 → 0.00

Numbers say: pressure barely changes the width.

## Acrylic — heavy body
Heavy acrylic · 30 px · 19.3 s

![Acrylic — heavy body](Acrylic-heavy-body.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 10 % → 9 % | 0.51 | 0.93 | 158 |
| heavy line | 11 % → 10 % | 0.51 | 0.93 | 101 |
| pressure swell | 8 % → 8 % | 0.52 | 0.94 | 72 |
| fast wave | 24 % → 14 % | 0.51 | 0.58 | 266 |
| slow wave | 25 % → 15 % | 0.51 | 0.59 | 411 |
| spiral | 37 % → 15 % | 0.51 | 0.40 | 539 |
| loop | 22 % → 16 % | 0.51 | 0.73 | 321 |
| tilted | 10 % → 10 % | 0.51 | 1.00 | 158 |
| over the wet one | 20 % → 17 % | 0.51 | 0.88 | 141 |
| long, no reload | 39 % → 15 % | 0.51 | 0.40 | 745 | quarters: 0.30 → 0.20 → 0.10 → 0.02

Numbers say: pressure barely changes the width.

## Acrylic — fluid
Watercolor · 36 px · 38.5 s

![Acrylic — fluid](Acrylic-fluid.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 9 % → 10 % | 0.06 | 1.11 | 78 |
| heavy line | 13 % → 14 % | 0.05 | 1.07 | 91 |
| pressure swell | 9 % → 10 % | 0.07 | 1.09 | 59 |
| fast wave | 26 % → 28 % | 0.05 | 1.07 | 229 |
| slow wave | 24 % → 26 % | 0.07 | 1.08 | 503 |
| spiral | 39 % → 41 % | 0.05 | 1.06 | 454 |
| loop | 22 % → 25 % | 0.06 | 1.11 | 211 |
| tilted | 8 % → 9 % | 0.07 | 1.17 | 121 |
| over the wet one | 21 % → 22 % | 0.07 | 1.05 | 90 |
| long, no reload | 44 % → 47 % | 0.05 | 1.06 | 766 | quarters: 0.05 → 0.03 → 0.02 → 0.01

## Acrylic — palette knife
Heavy acrylic · 42 px · 26.0 s

![Acrylic — palette knife](Acrylic-palette-knife.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 15 % → 15 % | 0.06 | 0.98 | 37 |
| heavy line | 15 % → 15 % | 0.05 | 0.98 | 36 |
| pressure swell | 12 % → 12 % | 0.06 | 0.99 | 13 |
| fast wave | 37 % → 20 % | 0.06 | 0.54 | 77 |
| slow wave | 37 % → 21 % | 0.06 | 0.56 | 123 |
| spiral | 48 % → 19 % | 0.06 | 0.38 | 170 |
| loop | 32 % → 24 % | 0.05 | 0.75 | 57 |
| tilted | 12 % → 12 % | 0.05 | 1.00 | 28 |
| over the wet one | 26 % → 26 % | 0.05 | 0.98 | 21 |
| long, no reload | 55 % → 20 % | 0.06 | 0.36 | 181 | quarters: 0.04 → 0.02 → 0.00 → 0.00

Numbers say: pressure barely changes the width.

## Finger on oil
Oil · 30 px · 18.8 s

![Finger on oil](Finger-on-oil.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 8 % → 8 % | 0.34 | 1.00 | 50 |
| heavy line | 12 % → 12 % | 0.30 | 1.00 | 66 |
| pressure swell | 8 % → 8 % | 0.35 | 1.00 | 55 |
| fast wave | 16 % → 16 % | 0.22 | 1.00 | 172 |
| slow wave | 17 % → 17 % | 0.23 | 1.00 | 279 |
| spiral | 18 % → 18 % | 0.22 | 1.00 | 346 |
| loop | 18 % → 18 % | 0.23 | 1.00 | 143 |
| tilted | 9 % → 9 % | 0.31 | 1.00 | 86 |
| over the wet one | 18 % → 18 % | 0.31 | 1.00 | 62 |
| long, no reload | 15 % → 15 % | 0.23 | 1.00 | 374 | quarters: 0.13 → 0.01 → 0.00 → 0.00

## Palette knife — oil
Oil · 44 px · 28.1 s

![Palette knife — oil](Palette-knife-oil.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 16 % → 16 % | 0.10 | 1.00 | 37 |
| heavy line | 16 % → 16 % | 0.09 | 1.00 | 23 |
| pressure swell | 12 % → 12 % | 0.10 | 1.00 | 9 |
| fast wave | 39 % → 39 % | 0.07 | 1.00 | 89 |
| slow wave | 39 % → 39 % | 0.07 | 1.00 | 127 |
| spiral | 54 % → 54 % | 0.05 | 1.00 | 143 |
| loop | 34 % → 34 % | 0.08 | 1.00 | 96 |
| tilted | 13 % → 13 % | 0.09 | 1.00 | 27 |
| over the wet one | 28 % → 28 % | 0.09 | 1.00 | 34 |
| long, no reload | 65 % → 65 % | 0.05 | 1.00 | 246 | quarters: 0.08 → 0.04 → 0.01 → 0.00

Numbers say: pressure barely changes the width.

## 0.45 · Sponge
Watercolor · 46 px · 33.2 s

![0.45 · Sponge](0-45-Sponge.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 11 % → 0 % | 0.00 | 0.00 | 81 |
| heavy line | 13 % → 0 % | 0.01 | 0.00 | 118 |
| pressure swell | 9 % → 1 % | 0.02 | 0.14 | 51 |
| fast wave | 23 % → 2 % | 0.01 | 0.08 | 262 |
| slow wave | 26 % → 8 % | 0.02 | 0.30 | 274 |
| spiral | 34 % → 11 % | 0.02 | 0.32 | 277 |
| loop | 22 % → 4 % | 0.02 | 0.19 | 152 |
| tilted | 9 % → 10 % | 0.04 | 1.19 | 128 |
| over the wet one | 22 % → 10 % | 0.04 | 0.44 | 73 |
| long, no reload | 41 % → 19 % | 0.02 | 0.47 | 424 | quarters: 0.01 → 0.01 → 0.01 → 0.01

## 0.45 · Eraser
Eraser · 30 px · 28.4 s · over bands of wet oil paint and oil pastel in turn (it works on paint already there: look at what it does to the bands; covered counts the bands too)

![0.45 · Eraser](0-45-Eraser.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 23 % → 23 % | 0.81 | 1.00 | 47 |
| heavy line | 22 % → 22 % | 0.81 | 1.00 | 80 |
| pressure swell | 22 % → 22 % | 0.81 | 1.00 | 37 |
| fast wave | 21 % → 21 % | 0.80 | 1.00 | 143 |
| slow wave | 20 % → 20 % | 0.81 | 1.00 | 248 |
| spiral | 20 % → 20 % | 0.79 | 1.00 | 289 |
| loop | 21 % → 21 % | 0.79 | 1.00 | 140 |
| tilted | 22 % → 22 % | 0.80 | 1.00 | 66 |
| over the wet one | 21 % → 21 % | 0.80 | 1.00 | 65 |
| long, no reload | 16 % → 16 % | 0.79 | 1.00 | 447 | quarters: 0.13 → 0.15 → 0.12 → 0.16

Numbers say: pressure barely changes the width; the long stroke does not run out of paint.

## Lift wet paint
Eraser · 30 px · 26.1 s · over bands of wet oil paint and oil pastel in turn (it works on paint already there: look at what it does to the bands; covered counts the bands too)

![Lift wet paint](Lift-wet-paint.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 23 % → 23 % | 0.81 | 1.00 | 53 |
| heavy line | 23 % → 23 % | 0.81 | 1.00 | 54 |
| pressure swell | 23 % → 23 % | 0.81 | 1.00 | 38 |
| fast wave | 23 % → 23 % | 0.81 | 1.00 | 140 |
| slow wave | 23 % → 23 % | 0.81 | 1.00 | 230 |
| spiral | 23 % → 23 % | 0.81 | 1.00 | 206 |
| loop | 23 % → 23 % | 0.81 | 1.00 | 106 |
| tilted | 23 % → 23 % | 0.81 | 1.00 | 61 |
| over the wet one | 23 % → 23 % | 0.81 | 1.00 | 55 |
| long, no reload | 23 % → 23 % | 0.81 | 1.00 | 325 | quarters: 0.18 → 0.23 → 0.16 → 0.23

Numbers say: pressure barely changes the width; the long stroke does not run out of paint.

## Sgraffito
Eraser · 10 px · 25.2 s · over bands of wet oil paint and oil pastel in turn (it works on paint already there: look at what it does to the bands; covered counts the bands too)

![Sgraffito](Sgraffito.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 23 % → 23 % | 0.80 | 1.00 | 8 |
| heavy line | 23 % → 23 % | 0.81 | 1.00 | 13 |
| pressure swell | 23 % → 23 % | 0.81 | 1.00 | 6 |
| fast wave | 23 % → 23 % | 0.81 | 1.00 | 22 |
| slow wave | 23 % → 23 % | 0.81 | 1.00 | 22 |
| spiral | 23 % → 23 % | 0.81 | 1.00 | 34 |
| loop | 23 % → 23 % | 0.81 | 1.00 | 25 |
| tilted | 23 % → 23 % | 0.81 | 1.00 | 15 |
| over the wet one | 23 % → 23 % | 0.81 | 1.00 | 23 |
| long, no reload | 23 % → 23 % | 0.81 | 1.00 | 82 | quarters: 0.17 → 0.23 → 0.16 → 0.23

Numbers say: pressure barely changes the width; the long stroke does not run out of paint.

## Brush Artist · Ink — wash
Watercolor · 38 px · 44.6 s

![Brush Artist · Ink — wash](Brush-Artist-Ink-wash.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 11 % → 11 % | 0.39 | 1.03 | 72 |
| heavy line | 19 % → 19 % | 0.32 | 1.03 | 147 |
| pressure swell | 12 % → 13 % | 0.37 | 1.03 | 84 |
| fast wave | 40 % → 41 % | 0.31 | 1.04 | 257 |
| slow wave | 37 % → 38 % | 0.37 | 1.03 | 403 |
| spiral | 59 % → 61 % | 0.31 | 1.04 | 559 |
| loop | 32 % → 33 % | 0.35 | 1.02 | 251 |
| tilted | 13 % → 14 % | 0.38 | 1.04 | 127 |
| over the wet one | 29 % → 30 % | 0.38 | 1.04 | 79 |
| long, no reload | 67 % → 73 % | 0.29 | 1.09 | 599 | quarters: 0.34 → 0.27 → 0.19 → 0.12

## Brush Artist · Ink — brush line
Ink · 16 px · 36.1 s

![Brush Artist · Ink — brush line](Brush-Artist-Ink-brush-line.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 3 % → 5 % | 0.78 | 1.81 | 55 |
| heavy line | 13 % → 13 % | 0.88 | 0.99 | 166 |
| pressure swell | 8 % → 8 % | 0.87 | 1.05 | 103 |
| fast wave | 24 % → 23 % | 0.87 | 0.96 | 190 |
| slow wave | 20 % → 19 % | 0.87 | 0.97 | 215 |
| spiral | 30 % → 27 % | 0.86 | 0.89 | 346 |
| loop | 18 % → 18 % | 0.88 | 1.00 | 187 |
| tilted | 7 % → 7 % | 0.88 | 1.01 | 87 |
| over the wet one | 17 % → 17 % | 0.88 | 1.00 | 81 |
| long, no reload | 42 % → 30 % | 0.85 | 0.71 | 533 | quarters: 0.49 → 0.40 → 0.30 → 0.20

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Ink — dry brush
Gouache · 30 px · 29.2 s

![Brush Artist · Ink — dry brush](Brush-Artist-Ink-dry-brush.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 8 % → 1 % | 0.71 | 0.13 | 90 |
| heavy line | 10 % → 1 % | 0.71 | 0.11 | 190 |
| pressure swell | 7 % → 2 % | 0.71 | 0.23 | 102 |
| fast wave | 21 % → 2 % | 0.71 | 0.10 | 316 |
| slow wave | 21 % → 2 % | 0.71 | 0.09 | 559 |
| spiral | 31 % → 2 % | 0.71 | 0.07 | 656 |
| loop | 18 % → 2 % | 0.71 | 0.13 | 422 |
| tilted | 9 % → 8 % | 0.71 | 0.96 | 207 |
| over the wet one | 17 % → 4 % | 0.71 | 0.25 | 126 |
| long, no reload | 30 % → 3 % | 0.71 | 0.09 | 764 | quarters: 0.38 → 0.31 → 0.21 → 0.08

## Brush Artist · Watercolour — blue
Watercolor · 40 px · 39.5 s

![Brush Artist · Watercolour — blue](Brush-Artist-Watercolour-blue.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 6 % → 10 % | 0.43 | 1.78 | 48 |
| heavy line | 11 % → 13 % | 0.43 | 1.17 | 82 |
| pressure swell | 7 % → 9 % | 0.45 | 1.37 | 51 |
| fast wave | 24 % → 26 % | 0.41 | 1.09 | 188 |
| slow wave | 22 % → 28 % | 0.44 | 1.25 | 297 |
| spiral | 38 % → 42 % | 0.38 | 1.11 | 310 |
| loop | 19 % → 23 % | 0.44 | 1.17 | 152 |
| tilted | 12 % → 12 % | 0.44 | 1.01 | 124 |
| over the wet one | 21 % → 25 % | 0.44 | 1.17 | 93 |
| long, no reload | 51 % → 55 % | 0.37 | 1.06 | 690 | quarters: 0.32 → 0.24 → 0.19 → 0.15

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Watercolour — violet
Watercolor · 40 px · 40.7 s

![Brush Artist · Watercolour — violet](Brush-Artist-Watercolour-violet.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 6 % → 10 % | 0.42 | 1.78 | 44 |
| heavy line | 11 % → 13 % | 0.42 | 1.17 | 129 |
| pressure swell | 7 % → 9 % | 0.43 | 1.37 | 71 |
| fast wave | 24 % → 26 % | 0.41 | 1.09 | 632 |
| slow wave | 22 % → 28 % | 0.43 | 1.25 | 508 |
| spiral | 38 % → 42 % | 0.38 | 1.11 | 320 |
| loop | 19 % → 23 % | 0.43 | 1.17 | 190 |
| tilted | 12 % → 12 % | 0.43 | 1.01 | 148 |
| over the wet one | 21 % → 25 % | 0.43 | 1.17 | 89 |
| long, no reload | 51 % → 55 % | 0.37 | 1.06 | 500 | quarters: 0.30 → 0.24 → 0.19 → 0.16

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Watercolour — teal
Watercolor · 40 px · 40.0 s

![Brush Artist · Watercolour — teal](Brush-Artist-Watercolour-teal.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 6 % → 10 % | 0.30 | 1.78 | 50 |
| heavy line | 11 % → 13 % | 0.31 | 1.17 | 86 |
| pressure swell | 7 % → 9 % | 0.31 | 1.37 | 120 |
| fast wave | 24 % → 26 % | 0.30 | 1.09 | 296 |
| slow wave | 22 % → 28 % | 0.31 | 1.25 | 515 |
| spiral | 38 % → 42 % | 0.28 | 1.11 | 329 |
| loop | 19 % → 23 % | 0.31 | 1.17 | 193 |
| tilted | 12 % → 12 % | 0.31 | 1.01 | 135 |
| over the wet one | 21 % → 25 % | 0.31 | 1.17 | 71 |
| long, no reload | 51 % → 55 % | 0.27 | 1.06 | 454 | quarters: 0.22 → 0.18 → 0.14 → 0.11

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Gouache
Gouache · 30 px · 43.3 s

![Brush Artist · Gouache](Brush-Artist-Gouache.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 8 % → 8 % | 0.16 | 0.97 | 84 |
| heavy line | 15 % → 12 % | 0.16 | 0.78 | 101 |
| pressure swell | 11 % → 9 % | 0.16 | 0.85 | 61 |
| fast wave | 30 % → 14 % | 0.16 | 0.45 | 280 |
| slow wave | 29 % → 14 % | 0.16 | 0.47 | 645 |
| spiral | 40 % → 14 % | 0.16 | 0.35 | 618 |
| loop | 24 % → 15 % | 0.16 | 0.62 | 212 |
| tilted | 10 % → 10 % | 0.16 | 1.01 | 110 |
| over the wet one | 22 % → 19 % | 0.16 | 0.89 | 125 |
| long, no reload | 43 % → 15 % | 0.16 | 0.35 | 597 | quarters: 0.10 → 0.07 → 0.04 → 0.02

## Brush Artist · Oil — bristle
Oil · 30 px · 25.4 s

![Brush Artist · Oil — bristle](Brush-Artist-Oil-bristle.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 9 % → 9 % | 0.53 | 1.00 | 138 |
| heavy line | 9 % → 9 % | 0.53 | 1.00 | 145 |
| pressure swell | 7 % → 7 % | 0.54 | 1.00 | 107 |
| fast wave | 23 % → 23 % | 0.53 | 1.00 | 375 |
| slow wave | 23 % → 23 % | 0.53 | 1.00 | 678 |
| spiral | 36 % → 36 % | 0.50 | 1.00 | 657 |
| loop | 19 % → 19 % | 0.54 | 1.00 | 312 |
| tilted | 11 % → 11 % | 0.53 | 1.00 | 192 |
| over the wet one | 19 % → 19 % | 0.53 | 1.00 | 153 |
| long, no reload | 47 % → 47 % | 0.45 | 1.00 | 883 | quarters: 0.31 → 0.27 → 0.22 → 0.14

Numbers say: pressure barely changes the width.

## Brush Artist · Charcoal — stick
Charcoal · 30 px · 13.5 s

![Brush Artist · Charcoal — stick](Brush-Artist-Charcoal-stick.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 7 % → 7 % | 0.84 | 1.00 | 28 |
| heavy line | 7 % → 7 % | 0.84 | 1.00 | 28 |
| pressure swell | 5 % → 5 % | 0.84 | 1.00 | 26 |
| fast wave | 17 % → 17 % | 0.84 | 1.00 | 75 |
| slow wave | 17 % → 17 % | 0.84 | 1.00 | 124 |
| spiral | 29 % → 29 % | 0.84 | 1.00 | 149 |
| loop | 14 % → 14 % | 0.84 | 1.00 | 60 |
| tilted | 6 % → 6 % | 0.84 | 1.00 | 33 |
| over the wet one | 13 % → 13 % | 0.84 | 1.00 | 28 |
| long, no reload | 37 % → 37 % | 0.84 | 1.00 | 193 | quarters: 0.35 → 0.34 → 0.34 → 0.35

Numbers say: pressure barely changes the width; the long stroke does not run out of paint.

## Brush Artist · Ink — dry brush — own sheet
own sheet 600 × 600 · Gouache · 30 px · 4.5 s

![Brush Artist · Ink — dry brush — own sheet](Brush-Artist-Ink-dry-brush-own-sheet.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| ear | 17 % → 4 % | 0.77 | 0.25 | 742 |
| drag0 | 20 % → 24 % | 0.77 | 1.21 | 185 |
| drag1 | 25 % → 25 % | 0.77 | 1.01 | 241 |
| drag2 | 28 % → 26 % | 0.77 | 0.92 | 123 |
| drag3 | 30 % → 26 % | 0.77 | 0.87 | 110 |

