![All brushes](contact.png)

# Brush Lab — 57 brushes · Nov 3, 2026 at 11:01 AM

Every sheet: 1500 × 600, ten strokes in a 5 × 2 grid — 1. light line · 2. heavy line · 3. pressure swell · 4. fast wave · 5. slow wave · 6. spiral · 7. loop · 8. tilted · 9. over the wet one · 10. long, no reload (cell 8 holds «tilted» and «over the wet one» crossed). The CPU reference of Mamay's paint engine; the wet layer settles 20 s at the end.

Columns: **covered** = share of the cell with paint right after the stroke → after settling; **dark** = mean darkness of the painted pixels above the paper's own grain (0 = paper, 1 = black); **spread** = how far wet paint went beyond the stroke (1.0 = stayed); **ms** = the stroke on the CPU; long stroke: paint in each quarter of its length (it should run out: wet → streaks → dry tail).

## Ink Line
Ink · 12 px · 36.6 s

![Ink Line](Ink-Line.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 1 % → 4 % | 0.55 | 2.44 | 88 |
| heavy line | 5 % → 6 % | 0.68 | 1.13 | 109 |
| pressure swell | 3 % → 4 % | 0.64 | 1.40 | 100 |
| fast wave | 10 % → 11 % | 0.59 | 1.11 | 249 |
| slow wave | 8 % → 10 % | 0.57 | 1.16 | 179 |
| spiral | 14 % → 15 % | 0.50 | 1.07 | 311 |
| loop | 8 % → 9 % | 0.61 | 1.16 | 165 |
| tilted | 5 % → 5 % | 0.65 | 1.05 | 66 |
| over the wet one | 10 % → 11 % | 0.65 | 1.15 | 91 |
| long, no reload | 18 % → 17 % | 0.47 | 0.96 | 463 | quarters: 0.22 → 0.09 → 0.04 → 0.02

Numbers say: wet paint spreads well beyond the stroke.

## Dense Ink
Ink · 14 px · 37.4 s

![Dense Ink](Dense-Ink.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 5 % → 7 % | 0.72 | 1.26 | 117 |
| heavy line | 7 % → 7 % | 0.73 | 1.09 | 130 |
| pressure swell | 5 % → 6 % | 0.72 | 1.17 | 115 |
| fast wave | 13 % → 13 % | 0.69 | 1.01 | 319 |
| slow wave | 12 % → 12 % | 0.67 | 1.04 | 217 |
| spiral | 18 % → 15 % | 0.65 | 0.80 | 308 |
| loop | 11 % → 12 % | 0.69 | 1.08 | 230 |
| tilted | 5 % → 6 % | 0.72 | 1.07 | 96 |
| over the wet one | 12 % → 13 % | 0.72 | 1.11 | 74 |
| long, no reload | 23 % → 15 % | 0.64 | 0.66 | 494 | quarters: 0.30 → 0.12 → 0.04 → 0.02

## Transparent Wash
Watercolor · 22 px · 39.0 s

![Transparent Wash](Transparent-Wash.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 2 % → 5 % | 0.27 | 2.25 | 85 |
| heavy line | 7 % → 9 % | 0.27 | 1.22 | 118 |
| pressure swell | 4 % → 6 % | 0.28 | 1.54 | 99 |
| fast wave | 14 % → 16 % | 0.20 | 1.17 | 233 |
| slow wave | 12 % → 15 % | 0.21 | 1.28 | 269 |
| spiral | 18 % → 22 % | 0.16 | 1.23 | 278 |
| loop | 11 % → 13 % | 0.22 | 1.20 | 167 |
| tilted | 8 % → 8 % | 0.24 | 1.06 | 104 |
| over the wet one | 13 % → 16 % | 0.24 | 1.18 | 77 |
| long, no reload | 26 % → 32 % | 0.13 | 1.22 | 421 | quarters: 0.11 → 0.04 → 0.02 → 0.01

Numbers say: wet paint spreads well beyond the stroke.

## Dry Brush
Gouache · 24 px · 33.4 s

![Dry Brush](Dry-Brush.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 5 % → 0 % | 0.65 | 0.09 | 61 |
| heavy line | 6 % → 0 % | 0.65 | 0.02 | 239 |
| pressure swell | 5 % → 0 % | 0.65 | 0.08 | 138 |
| fast wave | 6 % → 1 % | 0.65 | 0.08 | 700 |
| slow wave | 7 % → 0 % | 0.65 | 0.06 | 455 |
| spiral | 7 % → 0 % | 0.65 | 0.07 | 384 |
| loop | 10 % → 0 % | 0.65 | 0.04 | 243 |
| tilted | 4 % → 3 % | 0.65 | 0.88 | 94 |
| over the wet one | 9 % → 1 % | 0.65 | 0.12 | 90 |
| long, no reload | 6 % → 1 % | 0.65 | 0.14 | 569 | quarters: 0.12 → 0.00 → 0.00 → 0.00

## Wax Crayon
Wax · 8 px · 16.5 s

![Wax Crayon](Wax-Crayon.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 1 % → 1 % | 0.71 | 1.00 | 50 |
| heavy line | 1 % → 1 % | 0.69 | 1.00 | 38 |
| pressure swell | 1 % → 1 % | 0.70 | 1.00 | 40 |
| fast wave | 3 % → 3 % | 0.69 | 1.00 | 103 |
| slow wave | 3 % → 3 % | 0.70 | 1.00 | 99 |
| spiral | 5 % → 5 % | 0.70 | 1.00 | 329 |
| loop | 3 % → 3 % | 0.70 | 1.00 | 171 |
| tilted | 2 % → 2 % | 0.68 | 1.00 | 40 |
| over the wet one | 3 % → 3 % | 0.68 | 1.00 | 37 |
| long, no reload | 7 % → 7 % | 0.70 | 1.00 | 237 | quarters: 0.06 → 0.06 → 0.06 → 0.06

Numbers say: the long stroke does not run out of paint.

## Oil Pastel
Wax · 12 px · 16.4 s

![Oil Pastel](Oil-Pastel.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 1 % → 1 % | 0.68 | 1.00 | 58 |
| heavy line | 2 % → 2 % | 0.68 | 1.00 | 74 |
| pressure swell | 2 % → 2 % | 0.69 | 1.00 | 57 |
| fast wave | 5 % → 5 % | 0.68 | 1.00 | 294 |
| slow wave | 5 % → 5 % | 0.68 | 1.00 | 298 |
| spiral | 8 % → 8 % | 0.68 | 1.00 | 154 |
| loop | 4 % → 4 % | 0.68 | 1.00 | 121 |
| tilted | 2 % → 2 % | 0.68 | 1.00 | 59 |
| over the wet one | 5 % → 5 % | 0.68 | 1.00 | 35 |
| long, no reload | 13 % → 13 % | 0.68 | 1.00 | 243 | quarters: 0.10 → 0.09 → 0.10 → 0.10

Numbers say: the long stroke does not run out of paint.

## Charcoal
Charcoal · 5 px · 16.3 s

![Charcoal](Charcoal.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 1 % → 1 % | 0.74 | 1.00 | 17 |
| heavy line | 1 % → 1 % | 0.74 | 1.00 | 19 |
| pressure swell | 1 % → 1 % | 0.74 | 1.00 | 16 |
| fast wave | 2 % → 2 % | 0.73 | 1.00 | 72 |
| slow wave | 2 % → 2 % | 0.74 | 1.00 | 70 |
| spiral | 4 % → 4 % | 0.74 | 1.00 | 133 |
| loop | 2 % → 2 % | 0.74 | 1.00 | 28 |
| tilted | 2 % → 2 % | 0.72 | 1.00 | 20 |
| over the wet one | 2 % → 2 % | 0.72 | 1.00 | 15 |
| long, no reload | 6 % → 6 % | 0.73 | 1.00 | 93 | quarters: 0.05 → 0.05 → 0.05 → 0.05

Numbers say: the long stroke does not run out of paint.

## Impasto
Heavy acrylic · 22 px · 24.7 s

![Impasto](Impasto.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 8 % → 8 % | 0.71 | 0.93 | 127 |
| heavy line | 10 % → 9 % | 0.70 | 0.94 | 235 |
| pressure swell | 7 % → 7 % | 0.72 | 0.94 | 74 |
| fast wave | 20 % → 13 % | 0.71 | 0.64 | 237 |
| slow wave | 21 % → 14 % | 0.71 | 0.66 | 350 |
| spiral | 30 % → 14 % | 0.71 | 0.46 | 342 |
| loop | 18 % → 14 % | 0.71 | 0.77 | 228 |
| tilted | 8 % → 8 % | 0.70 | 1.00 | 133 |
| over the wet one | 17 % → 15 % | 0.70 | 0.91 | 137 |
| long, no reload | 34 % → 14 % | 0.71 | 0.41 | 647 | quarters: 0.38 → 0.21 → 0.10 → 0.03

## Oil Round
Oil · 18 px · 29.6 s

![Oil Round](Oil-Round.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 2 % → 2 % | 0.71 | 1.00 | 213 |
| heavy line | 6 % → 6 % | 0.72 | 1.00 | 154 |
| pressure swell | 3 % → 3 % | 0.63 | 1.00 | 56 |
| fast wave | 7 % → 7 % | 0.54 | 1.00 | 286 |
| slow wave | 4 % → 4 % | 0.36 | 1.00 | 351 |
| spiral | 5 % → 5 % | 0.21 | 1.00 | 410 |
| loop | 3 % → 3 % | 0.18 | 1.00 | 200 |
| tilted | 2 % → 2 % | 0.33 | 1.00 | 133 |
| over the wet one | 3 % → 3 % | 0.33 | 1.00 | 87 |
| long, no reload | 8 % → 8 % | 0.17 | 1.00 | 546 | quarters: 0.02 → 0.02 → 0.01 → 0.01

## Palette Knife
Oil · 20 px · 28.8 s

![Palette Knife](Palette-Knife.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 8 % → 8 % | 0.67 | 1.00 | 106 |
| heavy line | 8 % → 8 % | 0.73 | 1.00 | 23 |
| pressure swell | 6 % → 6 % | 0.74 | 1.00 | 14 |
| fast wave | 17 % → 17 % | 0.49 | 1.00 | 56 |
| slow wave | 17 % → 17 % | 0.43 | 1.00 | 73 |
| spiral | 18 % → 18 % | 0.45 | 1.00 | 104 |
| loop | 16 % → 16 % | 0.58 | 1.00 | 78 |
| tilted | 5 % → 5 % | 0.72 | 1.00 | 31 |
| over the wet one | 13 % → 13 % | 0.72 | 1.00 | 15 |
| long, no reload | 17 % → 17 % | 0.47 | 1.00 | 126 | quarters: 0.29 → 0.05 → 0.00 → 0.00

Numbers say: pressure barely changes the width.

## Water
Watercolor · 20 px · 60.3 s · over bands of wet oil paint and oil pastel in turn (it works on paint already there: look at what it does to the bands; covered counts the bands too)

![Water](Water.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 25 % → 26 % | 0.78 | 1.07 | 108 |
| heavy line | 23 % → 24 % | 0.80 | 1.04 | 88 |
| pressure swell | 23 % → 24 % | 0.80 | 1.03 | 55 |
| fast wave | 23 % → 25 % | 0.80 | 1.07 | 191 |
| slow wave | 23 % → 25 % | 0.80 | 1.06 | 233 |
| spiral | 23 % → 25 % | 0.79 | 1.08 | 339 |
| loop | 23 % → 24 % | 0.80 | 1.03 | 214 |
| tilted | 23 % → 23 % | 0.80 | 1.00 | 166 |
| over the wet one | 23 % → 25 % | 0.80 | 1.07 | 69 |
| long, no reload | 23 % → 25 % | 0.80 | 1.08 | 442 | quarters: 0.21 → 0.26 → 0.17 → 0.25

Numbers say: pressure barely changes the width; the long stroke does not run out of paint.

## Blender
Pastel · 16 px · 35.3 s · over bands of wet oil paint and oil pastel in turn (it works on paint already there: look at what it does to the bands; covered counts the bands too)

![Blender](Blender.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 24 % → 24 % | 0.80 | 1.00 | 58 |
| heavy line | 24 % → 24 % | 0.80 | 1.00 | 54 |
| pressure swell | 24 % → 24 % | 0.80 | 1.00 | 43 |
| fast wave | 25 % → 25 % | 0.78 | 1.00 | 108 |
| slow wave | 25 % → 25 % | 0.78 | 1.00 | 121 |
| spiral | 27 % → 27 % | 0.76 | 1.00 | 614 |
| loop | 25 % → 25 % | 0.79 | 1.00 | 232 |
| tilted | 24 % → 24 % | 0.78 | 1.00 | 143 |
| over the wet one | 25 % → 25 % | 0.78 | 1.00 | 68 |
| long, no reload | 29 % → 29 % | 0.74 | 1.00 | 396 | quarters: 0.19 → 0.26 → 0.21 → 0.28

Numbers say: pressure barely changes the width; the long stroke does not run out of paint.

## Eraser
Eraser · 16 px · 34.8 s · over bands of wet oil paint and oil pastel in turn (it works on paint already there: look at what it does to the bands; covered counts the bands too)

![Eraser](Eraser.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 23 % → 23 % | 0.81 | 1.00 | 69 |
| heavy line | 23 % → 23 % | 0.81 | 1.00 | 84 |
| pressure swell | 23 % → 23 % | 0.81 | 1.00 | 55 |
| fast wave | 22 % → 22 % | 0.81 | 1.00 | 124 |
| slow wave | 22 % → 22 % | 0.81 | 1.00 | 132 |
| spiral | 21 % → 21 % | 0.81 | 1.00 | 556 |
| loop | 22 % → 22 % | 0.81 | 1.00 | 214 |
| tilted | 23 % → 23 % | 0.81 | 1.00 | 126 |
| over the wet one | 22 % → 22 % | 0.81 | 1.00 | 79 |
| long, no reload | 19 % → 19 % | 0.81 | 1.00 | 353 | quarters: 0.15 → 0.19 → 0.14 → 0.20

Numbers say: pressure barely changes the width; the long stroke does not run out of paint.

## Fan
Gouache · 30 px · 50.7 s

![Fan](Fan.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 9 % → 3 % | 0.63 | 0.37 | 93 |
| heavy line | 11 % → 4 % | 0.63 | 0.39 | 160 |
| pressure swell | 8 % → 5 % | 0.63 | 0.55 | 100 |
| fast wave | 18 % → 5 % | 0.63 | 0.26 | 222 |
| slow wave | 18 % → 5 % | 0.63 | 0.25 | 287 |
| spiral | 24 % → 5 % | 0.63 | 0.20 | 318 |
| loop | 17 % → 5 % | 0.63 | 0.29 | 160 |
| tilted | 5 % → 6 % | 0.63 | 1.05 | 88 |
| over the wet one | 16 % → 8 % | 0.63 | 0.50 | 92 |
| long, no reload | 23 % → 5 % | 0.63 | 0.22 | 493 | quarters: 0.29 → 0.07 → 0.01 → 0.00

## Sponge
Gouache · 30 px · 49.9 s

![Sponge](Sponge.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 4 % → 0 % | 0.62 | 0.12 | 69 |
| heavy line | 12 % → 2 % | 0.62 | 0.14 | 179 |
| pressure swell | 7 % → 2 % | 0.62 | 0.27 | 110 |
| fast wave | 20 % → 4 % | 0.62 | 0.19 | 246 |
| slow wave | 21 % → 4 % | 0.62 | 0.18 | 370 |
| spiral | 28 % → 4 % | 0.62 | 0.14 | 359 |
| loop | 18 % → 5 % | 0.62 | 0.29 | 186 |
| tilted | 7 % → 7 % | 0.62 | 1.04 | 198 |
| over the wet one | 16 % → 6 % | 0.62 | 0.37 | 102 |
| long, no reload | 29 % → 5 % | 0.62 | 0.17 | 646 | quarters: 0.29 → 0.13 → 0.07 → 0.04

## Ink — sumi brush
Watercolor · 22 px · 48.1 s

![Ink — sumi brush](Ink-sumi-brush.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 6 % → 7 % | 0.46 | 1.06 | 87 |
| heavy line | 10 % → 11 % | 0.38 | 1.05 | 92 |
| pressure swell | 7 % → 8 % | 0.42 | 1.04 | 82 |
| fast wave | 21 % → 21 % | 0.32 | 1.00 | 237 |
| slow wave | 19 % → 19 % | 0.37 | 1.01 | 361 |
| spiral | 28 % → 26 % | 0.30 | 0.92 | 499 |
| loop | 17 % → 18 % | 0.37 | 1.06 | 236 |
| tilted | 6 % → 7 % | 0.40 | 1.17 | 158 |
| over the wet one | 16 % → 16 % | 0.40 | 1.01 | 216 |
| long, no reload | 33 % → 29 % | 0.30 | 0.86 | 566 | quarters: 0.23 → 0.11 → 0.06 → 0.04

## Ink — wash
Watercolor · 40 px · 48.0 s

![Ink — wash](Ink-wash.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 8 % → 9 % | 0.05 | 1.26 | 155 |
| heavy line | 11 % → 13 % | 0.04 | 1.22 | 155 |
| pressure swell | 7 % → 9 % | 0.05 | 1.25 | 80 |
| fast wave | 22 % → 27 % | 0.04 | 1.21 | 325 |
| slow wave | 21 % → 26 % | 0.06 | 1.23 | 716 |
| spiral | 34 % → 41 % | 0.04 | 1.21 | 854 |
| loop | 19 % → 24 % | 0.05 | 1.25 | 290 |
| tilted | 7 % → 9 % | 0.05 | 1.21 | 170 |
| over the wet one | 18 % → 21 % | 0.05 | 1.18 | 128 |
| long, no reload | 39 % → 46 % | 0.05 | 1.19 | 699 | quarters: 0.04 → 0.03 → 0.02 → 0.01

## Ink — dry brush
Ink · 30 px · 36.0 s

![Ink — dry brush](Ink-dry-brush.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 9 % → 7 % | 0.81 | 0.78 | 146 |
| heavy line | 11 % → 8 % | 0.80 | 0.73 | 177 |
| pressure swell | 8 % → 7 % | 0.81 | 0.85 | 124 |
| fast wave | 22 % → 8 % | 0.78 | 0.38 | 369 |
| slow wave | 18 % → 6 % | 0.80 | 0.36 | 819 |
| spiral | 23 % → 8 % | 0.77 | 0.35 | 835 |
| loop | 20 % → 8 % | 0.77 | 0.41 | 309 |
| tilted | 9 % → 9 % | 0.78 | 1.01 | 231 |
| over the wet one | 19 % → 14 % | 0.78 | 0.75 | 120 |
| long, no reload | 20 % → 9 % | 0.78 | 0.42 | 707 | quarters: 0.32 → 0.01 → 0.00 → 0.00

## Ink — nib
Watercolor · 5 px · 31.9 s

![Ink — nib](Ink-nib.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 2 % → 2 % | 0.76 | 1.17 | 49 |
| heavy line | 2 % → 2 % | 0.77 | 1.16 | 37 |
| pressure swell | 1 % → 2 % | 0.78 | 1.22 | 32 |
| fast wave | 4 % → 4 % | 0.66 | 1.09 | 151 |
| slow wave | 4 % → 4 % | 0.68 | 1.11 | 95 |
| spiral | 6 % → 6 % | 0.58 | 1.08 | 175 |
| loop | 3 % → 4 % | 0.69 | 1.12 | 114 |
| tilted | 2 % → 2 % | 0.64 | 1.21 | 47 |
| over the wet one | 4 % → 4 % | 0.64 | 1.03 | 45 |
| long, no reload | 7 % → 7 % | 0.53 | 1.02 | 236 | quarters: 0.09 → 0.04 → 0.03 → 0.02

## 0.45 · Dry brush
Gouache · 34 px · 36.4 s

![0.45 · Dry brush](0-45-Dry-brush.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 11 % → 3 % | 0.67 | 0.28 | 138 |
| heavy line | 12 % → 3 % | 0.67 | 0.30 | 175 |
| pressure swell | 9 % → 4 % | 0.67 | 0.40 | 103 |
| fast wave | 20 % → 4 % | 0.67 | 0.19 | 384 |
| slow wave | 20 % → 4 % | 0.67 | 0.18 | 729 |
| spiral | 21 % → 4 % | 0.67 | 0.17 | 670 |
| loop | 21 % → 4 % | 0.67 | 0.19 | 464 |
| tilted | 9 % → 9 % | 0.67 | 0.97 | 239 |
| over the wet one | 20 % → 7 % | 0.67 | 0.33 | 173 |
| long, no reload | 20 % → 4 % | 0.67 | 0.21 | 914 | quarters: 0.38 → 0.07 → 0.00 → 0.00

Numbers say: pressure barely changes the width.

## Dry pastel
Pastel · 26 px · 15.4 s

![Dry pastel](Dry-pastel.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 5 % → 5 % | 0.36 | 1.00 | 56 |
| heavy line | 6 % → 6 % | 0.36 | 1.00 | 50 |
| pressure swell | 5 % → 5 % | 0.36 | 1.00 | 37 |
| fast wave | 15 % → 15 % | 0.36 | 1.00 | 106 |
| slow wave | 14 % → 14 % | 0.36 | 1.00 | 163 |
| spiral | 23 % → 23 % | 0.36 | 1.00 | 240 |
| loop | 11 % → 11 % | 0.36 | 1.00 | 98 |
| tilted | 5 % → 5 % | 0.37 | 1.00 | 52 |
| over the wet one | 10 % → 10 % | 0.37 | 1.00 | 47 |
| long, no reload | 26 % → 26 % | 0.36 | 1.00 | 326 | quarters: 0.11 → 0.10 → 0.10 → 0.11

Numbers say: the long stroke does not run out of paint.

## 0.45 · Charcoal
Charcoal · 18 px · 14.4 s

![0.45 · Charcoal](0-45-Charcoal.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 4 % → 4 % | 0.79 | 1.00 | 27 |
| heavy line | 4 % → 4 % | 0.79 | 1.00 | 32 |
| pressure swell | 4 % → 4 % | 0.79 | 1.00 | 13 |
| fast wave | 11 % → 11 % | 0.79 | 1.00 | 49 |
| slow wave | 11 % → 11 % | 0.78 | 1.00 | 74 |
| spiral | 20 % → 20 % | 0.79 | 1.00 | 121 |
| loop | 10 % → 10 % | 0.79 | 1.00 | 47 |
| tilted | 4 % → 4 % | 0.78 | 1.00 | 34 |
| over the wet one | 9 % → 9 % | 0.78 | 1.00 | 22 |
| long, no reload | 26 % → 26 % | 0.79 | 1.00 | 152 | quarters: 0.23 → 0.22 → 0.23 → 0.24

Numbers say: pressure barely changes the width; the long stroke does not run out of paint.

## Watercolour — wash
Watercolor · 50 px · 49.1 s

![Watercolour — wash](Watercolour-wash.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 9 % → 11 % | 0.01 | 1.22 | 126 |
| heavy line | 12 % → 14 % | 0.01 | 1.17 | 132 |
| pressure swell | 8 % → 10 % | 0.01 | 1.22 | 95 |
| fast wave | 26 % → 30 % | 0.01 | 1.18 | 327 |
| slow wave | 25 % → 29 % | 0.01 | 1.18 | 697 |
| spiral | 39 % → 46 % | 0.01 | 1.17 | 880 |
| loop | 22 % → 27 % | 0.01 | 1.21 | 371 |
| tilted | 10 % → 11 % | 0.01 | 1.18 | 225 |
| over the wet one | 22 % → 25 % | 0.01 | 1.14 | 133 |
| long, no reload | 45 % → 54 % | 0.01 | 1.18 | 1337 | quarters: 0.01 → 0.01 → 0.01 → 0.00

## Watercolour — wet-in-wet
Watercolor · 44 px · 45.7 s

![Watercolour — wet-in-wet](Watercolour-wet-in-wet.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 7 % → 9 % | 0.02 | 1.26 | 93 |
| heavy line | 10 % → 12 % | 0.02 | 1.22 | 129 |
| pressure swell | 7 % → 9 % | 0.02 | 1.21 | 78 |
| fast wave | 23 % → 27 % | 0.02 | 1.17 | 521 |
| slow wave | 22 % → 26 % | 0.02 | 1.18 | 834 |
| spiral | 36 % → 43 % | 0.02 | 1.20 | 492 |
| loop | 19 % → 23 % | 0.02 | 1.20 | 395 |
| tilted | 7 % → 9 % | 0.02 | 1.19 | 185 |
| over the wet one | 17 % → 19 % | 0.02 | 1.12 | 122 |
| long, no reload | 42 % → 49 % | 0.02 | 1.18 | 801 | quarters: 0.01 → 0.01 → 0.01 → 0.01

## Watercolour — glaze
Watercolor · 38 px · 42.2 s

![Watercolour — glaze](Watercolour-glaze.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 7 % → 9 % | 0.01 | 1.28 | 118 |
| heavy line | 10 % → 13 % | 0.01 | 1.25 | 189 |
| pressure swell | 7 % → 9 % | 0.01 | 1.29 | 94 |
| fast wave | 20 % → 25 % | 0.01 | 1.24 | 236 |
| slow wave | 19 % → 24 % | 0.01 | 1.26 | 477 |
| spiral | 31 % → 37 % | 0.01 | 1.21 | 452 |
| loop | 18 % → 23 % | 0.01 | 1.27 | 224 |
| tilted | 7 % → 8 % | 0.01 | 1.20 | 135 |
| over the wet one | 17 % → 20 % | 0.01 | 1.19 | 90 |
| long, no reload | 36 % → 42 % | 0.01 | 1.17 | 533 | quarters: 0.01 → 0.00 → 0.00 → 0.00

## Watercolour — granulating
Watercolor · 44 px · 44.7 s

![Watercolour — granulating](Watercolour-granulating.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 8 % → 10 % | 0.02 | 1.18 | 114 |
| heavy line | 12 % → 14 % | 0.01 | 1.15 | 123 |
| pressure swell | 8 % → 10 % | 0.02 | 1.18 | 109 |
| fast wave | 25 % → 29 % | 0.01 | 1.15 | 329 |
| slow wave | 24 % → 27 % | 0.02 | 1.16 | 551 |
| spiral | 39 % → 44 % | 0.01 | 1.15 | 541 |
| loop | 22 % → 25 % | 0.01 | 1.17 | 284 |
| tilted | 9 % → 11 % | 0.02 | 1.15 | 200 |
| over the wet one | 21 % → 23 % | 0.02 | 1.11 | 155 |
| long, no reload | 45 % → 52 % | 0.01 | 1.15 | 669 | quarters: 0.01 → 0.01 → 0.01 → 0.01

## Watercolour — dry brush
Watercolor · 36 px · 37.9 s

![Watercolour — dry brush](Watercolour-dry-brush.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 7 % → 8 % | 0.05 | 1.07 | 117 |
| heavy line | 11 % → 12 % | 0.04 | 1.03 | 137 |
| pressure swell | 9 % → 10 % | 0.05 | 1.07 | 137 |
| fast wave | 21 % → 14 % | 0.04 | 0.68 | 504 |
| slow wave | 19 % → 13 % | 0.04 | 0.70 | 519 |
| spiral | 24 % → 15 % | 0.04 | 0.61 | 565 |
| loop | 17 % → 14 % | 0.04 | 0.85 | 297 |
| tilted | 7 % → 8 % | 0.05 | 1.19 | 154 |
| over the wet one | 17 % → 17 % | 0.05 | 0.99 | 134 |
| long, no reload | 22 % → 15 % | 0.04 | 0.68 | 812 | quarters: 0.02 → 0.00 → 0.00 → 0.00

## Gouache
Gouache · 30 px · 37.5 s

![Gouache](Gouache.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 8 % → 6 % | 0.14 | 0.67 | 88 |
| heavy line | 13 % → 6 % | 0.14 | 0.47 | 108 |
| pressure swell | 10 % → 6 % | 0.14 | 0.61 | 75 |
| fast wave | 27 % → 7 % | 0.14 | 0.27 | 231 |
| slow wave | 27 % → 7 % | 0.14 | 0.27 | 446 |
| spiral | 37 % → 8 % | 0.14 | 0.22 | 479 |
| loop | 22 % → 8 % | 0.14 | 0.36 | 214 |
| tilted | 9 % → 9 % | 0.14 | 1.02 | 180 |
| over the wet one | 20 % → 13 % | 0.14 | 0.67 | 176 |
| long, no reload | 38 % → 10 % | 0.14 | 0.25 | 612 | quarters: 0.07 → 0.04 → 0.01 → 0.01

## Oil — alla prima
Oil · 30 px · 27.8 s

![Oil — alla prima](Oil-alla-prima.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 9 % → 9 % | 0.50 | 1.00 | 139 |
| heavy line | 10 % → 10 % | 0.50 | 1.00 | 106 |
| pressure swell | 8 % → 8 % | 0.52 | 1.00 | 79 |
| fast wave | 24 % → 24 % | 0.49 | 1.00 | 339 |
| slow wave | 25 % → 25 % | 0.50 | 1.00 | 834 |
| spiral | 38 % → 38 % | 0.44 | 1.00 | 865 |
| loop | 21 % → 21 % | 0.50 | 1.00 | 268 |
| tilted | 11 % → 11 % | 0.50 | 1.00 | 160 |
| over the wet one | 20 % → 20 % | 0.50 | 1.00 | 204 |
| long, no reload | 46 % → 46 % | 0.40 | 1.00 | 731 | quarters: 0.31 → 0.24 → 0.17 → 0.10

Numbers say: pressure barely changes the width.

## Oil — impasto
Oil · 34 px · 28.6 s

![Oil — impasto](Oil-impasto.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 11 % → 11 % | 0.24 | 1.00 | 135 |
| heavy line | 12 % → 12 % | 0.23 | 1.00 | 160 |
| pressure swell | 9 % → 9 % | 0.25 | 1.00 | 98 |
| fast wave | 29 % → 29 % | 0.21 | 1.00 | 456 |
| slow wave | 29 % → 29 % | 0.21 | 1.00 | 1101 |
| spiral | 48 % → 48 % | 0.17 | 1.00 | 910 |
| loop | 25 % → 25 % | 0.21 | 1.00 | 336 |
| tilted | 12 % → 12 % | 0.24 | 1.00 | 278 |
| over the wet one | 23 % → 23 % | 0.24 | 1.00 | 144 |
| long, no reload | 55 % → 55 % | 0.15 | 1.00 | 919 | quarters: 0.16 → 0.11 → 0.06 → 0.02

Numbers say: pressure barely changes the width.

## Oil — glaze
Oil · 40 px · 22.4 s

![Oil — glaze](Oil-glaze.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 10 % → 10 % | 0.49 | 1.00 | 111 |
| heavy line | 14 % → 14 % | 0.48 | 1.00 | 165 |
| pressure swell | 10 % → 10 % | 0.49 | 1.00 | 116 |
| fast wave | 28 % → 28 % | 0.46 | 1.00 | 408 |
| slow wave | 30 % → 30 % | 0.46 | 1.00 | 581 |
| spiral | 42 % → 42 % | 0.44 | 1.00 | 670 |
| loop | 24 % → 24 % | 0.47 | 1.00 | 305 |
| tilted | 11 % → 11 % | 0.47 | 1.00 | 253 |
| over the wet one | 23 % → 23 % | 0.47 | 1.00 | 137 |
| long, no reload | 47 % → 47 % | 0.43 | 1.00 | 1091 | quarters: 0.33 → 0.24 → 0.18 → 0.14

## Oil — scumble
Oil · 36 px · 29.5 s

![Oil — scumble](Oil-scumble.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 11 % → 11 % | 0.06 | 1.00 | 156 |
| heavy line | 12 % → 12 % | 0.05 | 1.00 | 219 |
| pressure swell | 9 % → 9 % | 0.06 | 1.00 | 180 |
| fast wave | 18 % → 18 % | 0.04 | 1.00 | 601 |
| slow wave | 20 % → 20 % | 0.04 | 1.00 | 756 |
| spiral | 19 % → 19 % | 0.03 | 1.00 | 744 |
| loop | 22 % → 22 % | 0.04 | 1.00 | 370 |
| tilted | 10 % → 10 % | 0.05 | 1.00 | 212 |
| over the wet one | 21 % → 21 % | 0.05 | 1.00 | 228 |
| long, no reload | 18 % → 18 % | 0.04 | 1.00 | 1222 | quarters: 0.03 → 0.00 → 0.00 → 0.00

Numbers say: pressure barely changes the width.

## Acrylic — heavy body
Heavy acrylic · 30 px · 21.8 s

![Acrylic — heavy body](Acrylic-heavy-body.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 10 % → 9 % | 0.51 | 0.93 | 213 |
| heavy line | 11 % → 10 % | 0.51 | 0.93 | 185 |
| pressure swell | 8 % → 8 % | 0.52 | 0.94 | 132 |
| fast wave | 24 % → 14 % | 0.51 | 0.58 | 428 |
| slow wave | 25 % → 15 % | 0.51 | 0.59 | 480 |
| spiral | 37 % → 15 % | 0.51 | 0.40 | 502 |
| loop | 22 % → 16 % | 0.51 | 0.73 | 288 |
| tilted | 10 % → 10 % | 0.51 | 1.00 | 141 |
| over the wet one | 20 % → 17 % | 0.51 | 0.88 | 126 |
| long, no reload | 39 % → 15 % | 0.51 | 0.40 | 949 | quarters: 0.30 → 0.20 → 0.10 → 0.02

Numbers say: pressure barely changes the width.

## Acrylic — fluid
Watercolor · 36 px · 45.8 s

![Acrylic — fluid](Acrylic-fluid.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 9 % → 10 % | 0.06 | 1.11 | 186 |
| heavy line | 13 % → 14 % | 0.05 | 1.07 | 154 |
| pressure swell | 9 % → 10 % | 0.07 | 1.09 | 103 |
| fast wave | 26 % → 28 % | 0.05 | 1.07 | 235 |
| slow wave | 24 % → 26 % | 0.07 | 1.08 | 440 |
| spiral | 39 % → 41 % | 0.05 | 1.06 | 441 |
| loop | 22 % → 25 % | 0.06 | 1.11 | 286 |
| tilted | 8 % → 9 % | 0.07 | 1.17 | 130 |
| over the wet one | 21 % → 22 % | 0.07 | 1.05 | 107 |
| long, no reload | 44 % → 47 % | 0.05 | 1.06 | 799 | quarters: 0.05 → 0.03 → 0.02 → 0.01

## Acrylic — palette knife
Heavy acrylic · 42 px · 30.8 s

![Acrylic — palette knife](Acrylic-palette-knife.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 15 % → 15 % | 0.06 | 0.98 | 34 |
| heavy line | 15 % → 15 % | 0.05 | 0.98 | 46 |
| pressure swell | 12 % → 12 % | 0.06 | 0.99 | 10 |
| fast wave | 37 % → 20 % | 0.06 | 0.54 | 72 |
| slow wave | 37 % → 21 % | 0.06 | 0.56 | 126 |
| spiral | 48 % → 19 % | 0.06 | 0.38 | 154 |
| loop | 32 % → 24 % | 0.05 | 0.75 | 96 |
| tilted | 12 % → 12 % | 0.05 | 1.00 | 63 |
| over the wet one | 26 % → 26 % | 0.05 | 0.98 | 44 |
| long, no reload | 55 % → 20 % | 0.06 | 0.36 | 172 | quarters: 0.04 → 0.02 → 0.00 → 0.00

Numbers say: pressure barely changes the width.

## Finger on oil
Oil · 30 px · 22.5 s

![Finger on oil](Finger-on-oil.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 8 % → 8 % | 0.34 | 1.00 | 71 |
| heavy line | 12 % → 12 % | 0.30 | 1.00 | 78 |
| pressure swell | 8 % → 8 % | 0.35 | 1.00 | 42 |
| fast wave | 16 % → 16 % | 0.22 | 1.00 | 212 |
| slow wave | 17 % → 17 % | 0.23 | 1.00 | 314 |
| spiral | 18 % → 18 % | 0.22 | 1.00 | 294 |
| loop | 18 % → 18 % | 0.23 | 1.00 | 151 |
| tilted | 9 % → 9 % | 0.31 | 1.00 | 105 |
| over the wet one | 18 % → 18 % | 0.31 | 1.00 | 80 |
| long, no reload | 15 % → 15 % | 0.23 | 1.00 | 927 | quarters: 0.13 → 0.01 → 0.00 → 0.00

## Palette knife — oil
Oil · 44 px · 26.4 s

![Palette knife — oil](Palette-knife-oil.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 16 % → 16 % | 0.10 | 1.00 | 35 |
| heavy line | 16 % → 16 % | 0.09 | 1.00 | 33 |
| pressure swell | 12 % → 12 % | 0.10 | 1.00 | 16 |
| fast wave | 39 % → 39 % | 0.07 | 1.00 | 77 |
| slow wave | 39 % → 39 % | 0.07 | 1.00 | 142 |
| spiral | 54 % → 54 % | 0.05 | 1.00 | 145 |
| loop | 34 % → 34 % | 0.08 | 1.00 | 90 |
| tilted | 13 % → 13 % | 0.09 | 1.00 | 30 |
| over the wet one | 28 % → 28 % | 0.09 | 1.00 | 47 |
| long, no reload | 65 % → 65 % | 0.05 | 1.00 | 304 | quarters: 0.08 → 0.04 → 0.01 → 0.00

Numbers say: pressure barely changes the width.

## 0.45 · Sponge
Watercolor · 46 px · 33.0 s

![0.45 · Sponge](0-45-Sponge.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 11 % → 0 % | 0.00 | 0.00 | 71 |
| heavy line | 13 % → 0 % | 0.01 | 0.00 | 131 |
| pressure swell | 9 % → 1 % | 0.02 | 0.14 | 103 |
| fast wave | 23 % → 2 % | 0.01 | 0.08 | 195 |
| slow wave | 26 % → 8 % | 0.02 | 0.30 | 407 |
| spiral | 34 % → 11 % | 0.02 | 0.32 | 369 |
| loop | 22 % → 4 % | 0.02 | 0.19 | 172 |
| tilted | 9 % → 10 % | 0.04 | 1.19 | 130 |
| over the wet one | 22 % → 10 % | 0.04 | 0.44 | 89 |
| long, no reload | 41 % → 19 % | 0.02 | 0.47 | 506 | quarters: 0.01 → 0.01 → 0.01 → 0.01

## 0.45 · Eraser
Eraser · 30 px · 28.3 s · over bands of wet oil paint and oil pastel in turn (it works on paint already there: look at what it does to the bands; covered counts the bands too)

![0.45 · Eraser](0-45-Eraser.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 23 % → 23 % | 0.81 | 1.00 | 69 |
| heavy line | 22 % → 22 % | 0.81 | 1.00 | 70 |
| pressure swell | 22 % → 22 % | 0.81 | 1.00 | 58 |
| fast wave | 21 % → 21 % | 0.80 | 1.00 | 167 |
| slow wave | 20 % → 20 % | 0.81 | 1.00 | 283 |
| spiral | 20 % → 20 % | 0.79 | 1.00 | 309 |
| loop | 21 % → 21 % | 0.79 | 1.00 | 152 |
| tilted | 22 % → 22 % | 0.80 | 1.00 | 83 |
| over the wet one | 21 % → 21 % | 0.80 | 1.00 | 66 |
| long, no reload | 16 % → 16 % | 0.79 | 1.00 | 432 | quarters: 0.13 → 0.15 → 0.12 → 0.16

Numbers say: pressure barely changes the width; the long stroke does not run out of paint.

## Lift wet paint
Eraser · 30 px · 28.6 s · over bands of wet oil paint and oil pastel in turn (it works on paint already there: look at what it does to the bands; covered counts the bands too)

![Lift wet paint](Lift-wet-paint.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 23 % → 23 % | 0.81 | 1.00 | 65 |
| heavy line | 23 % → 23 % | 0.81 | 1.00 | 61 |
| pressure swell | 23 % → 23 % | 0.81 | 1.00 | 54 |
| fast wave | 23 % → 23 % | 0.81 | 1.00 | 224 |
| slow wave | 23 % → 23 % | 0.81 | 1.00 | 281 |
| spiral | 23 % → 23 % | 0.81 | 1.00 | 244 |
| loop | 23 % → 23 % | 0.81 | 1.00 | 107 |
| tilted | 23 % → 23 % | 0.81 | 1.00 | 65 |
| over the wet one | 23 % → 23 % | 0.81 | 1.00 | 50 |
| long, no reload | 23 % → 23 % | 0.81 | 1.00 | 374 | quarters: 0.18 → 0.23 → 0.16 → 0.23

Numbers say: pressure barely changes the width; the long stroke does not run out of paint.

## Sgraffito
Eraser · 10 px · 29.5 s · over bands of wet oil paint and oil pastel in turn (it works on paint already there: look at what it does to the bands; covered counts the bands too)

![Sgraffito](Sgraffito.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 23 % → 23 % | 0.80 | 1.00 | 18 |
| heavy line | 23 % → 23 % | 0.81 | 1.00 | 16 |
| pressure swell | 23 % → 23 % | 0.81 | 1.00 | 8 |
| fast wave | 23 % → 23 % | 0.81 | 1.00 | 23 |
| slow wave | 23 % → 23 % | 0.81 | 1.00 | 25 |
| spiral | 23 % → 23 % | 0.81 | 1.00 | 46 |
| loop | 23 % → 23 % | 0.81 | 1.00 | 24 |
| tilted | 23 % → 23 % | 0.81 | 1.00 | 8 |
| over the wet one | 23 % → 23 % | 0.81 | 1.00 | 9 |
| long, no reload | 23 % → 23 % | 0.81 | 1.00 | 94 | quarters: 0.17 → 0.23 → 0.16 → 0.23

Numbers say: pressure barely changes the width; the long stroke does not run out of paint.

## Brush Artist · Ink wash W1
Watercolor · 38 px · 50.1 s

![Brush Artist · Ink wash W1](Brush-Artist-Ink-wash-W1.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 11 % → 11 % | 0.55 | 1.02 | 71 |
| heavy line | 19 % → 19 % | 0.47 | 1.01 | 141 |
| pressure swell | 12 % → 13 % | 0.53 | 1.02 | 81 |
| fast wave | 41 % → 41 % | 0.45 | 1.02 | 253 |
| slow wave | 38 % → 38 % | 0.54 | 1.02 | 418 |
| spiral | 60 % → 61 % | 0.45 | 1.02 | 421 |
| loop | 33 % → 33 % | 0.51 | 1.01 | 326 |
| tilted | 14 % → 14 % | 0.54 | 1.04 | 159 |
| over the wet one | 29 % → 30 % | 0.54 | 1.02 | 122 |
| long, no reload | 69 % → 73 % | 0.43 | 1.05 | 698 | quarters: 0.48 → 0.39 → 0.29 → 0.19

## Brush Artist · Ink wash W2
Watercolor · 38 px · 48.5 s

![Brush Artist · Ink wash W2](Brush-Artist-Ink-wash-W2.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 11 % → 11 % | 0.41 | 1.03 | 94 |
| heavy line | 19 % → 19 % | 0.34 | 1.03 | 152 |
| pressure swell | 12 % → 13 % | 0.39 | 1.03 | 123 |
| fast wave | 40 % → 41 % | 0.33 | 1.04 | 651 |
| slow wave | 37 % → 38 % | 0.40 | 1.03 | 771 |
| spiral | 59 % → 61 % | 0.33 | 1.04 | 789 |
| loop | 32 % → 33 % | 0.38 | 1.02 | 233 |
| tilted | 13 % → 14 % | 0.40 | 1.04 | 148 |
| over the wet one | 29 % → 30 % | 0.40 | 1.04 | 126 |
| long, no reload | 67 % → 73 % | 0.31 | 1.09 | 621 | quarters: 0.36 → 0.29 → 0.21 → 0.13

## Brush Artist · Ink wash W3
Watercolor · 38 px · 46.6 s

![Brush Artist · Ink wash W3](Brush-Artist-Ink-wash-W3.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 11 % → 11 % | 0.29 | 1.05 | 72 |
| heavy line | 19 % → 19 % | 0.24 | 1.05 | 125 |
| pressure swell | 12 % → 13 % | 0.28 | 1.06 | 83 |
| fast wave | 38 % → 41 % | 0.23 | 1.07 | 321 |
| slow wave | 36 % → 38 % | 0.28 | 1.06 | 419 |
| spiral | 57 % → 61 % | 0.23 | 1.06 | 789 |
| loop | 32 % → 33 % | 0.27 | 1.04 | 288 |
| tilted | 13 % → 13 % | 0.29 | 1.03 | 131 |
| over the wet one | 28 % → 30 % | 0.29 | 1.08 | 86 |
| long, no reload | 64 % → 73 % | 0.22 | 1.14 | 802 | quarters: 0.26 → 0.20 → 0.14 → 0.09

## Brush Artist · Ink dry D1
Ink · 30 px · 38.1 s

![Brush Artist · Ink dry D1](Brush-Artist-Ink-dry-D1.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 8 % → 8 % | 0.86 | 1.01 | 103 |
| heavy line | 11 % → 11 % | 0.84 | 0.99 | 163 |
| pressure swell | 8 % → 8 % | 0.85 | 1.01 | 98 |
| fast wave | 26 % → 22 % | 0.84 | 0.86 | 334 |
| slow wave | 24 % → 19 % | 0.84 | 0.79 | 589 |
| spiral | 40 % → 24 % | 0.83 | 0.59 | 507 |
| loop | 22 % → 21 % | 0.83 | 0.94 | 248 |
| tilted | 10 % → 10 % | 0.85 | 1.01 | 229 |
| over the wet one | 20 % → 20 % | 0.85 | 0.99 | 196 |
| long, no reload | 49 % → 24 % | 0.82 | 0.50 | 782 | quarters: 0.51 → 0.40 → 0.21 → 0.07

## Brush Artist · Ink dry D2
Ink · 30 px · 41.7 s

![Brush Artist · Ink dry D2](Brush-Artist-Ink-dry-D2.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 9 % → 9 % | 0.87 | 1.04 | 74 |
| heavy line | 12 % → 12 % | 0.86 | 1.01 | 181 |
| pressure swell | 8 % → 8 % | 0.86 | 1.03 | 140 |
| fast wave | 28 % → 26 % | 0.85 | 0.95 | 346 |
| slow wave | 26 % → 24 % | 0.85 | 0.92 | 507 |
| spiral | 44 % → 32 % | 0.84 | 0.72 | 916 |
| loop | 23 % → 23 % | 0.85 | 0.98 | 288 |
| tilted | 10 % → 10 % | 0.87 | 1.00 | 177 |
| over the wet one | 21 % → 21 % | 0.87 | 1.01 | 136 |
| long, no reload | 54 % → 34 % | 0.83 | 0.63 | 809 | quarters: 0.56 → 0.49 → 0.35 → 0.18

## Brush Artist · Ink dry D3
Ink · 34 px · 41.0 s

![Brush Artist · Ink dry D3](Brush-Artist-Ink-dry-D3.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 9 % → 10 % | 0.86 | 1.04 | 107 |
| heavy line | 12 % → 12 % | 0.85 | 1.00 | 188 |
| pressure swell | 9 % → 9 % | 0.85 | 1.04 | 101 |
| fast wave | 29 % → 26 % | 0.85 | 0.89 | 376 |
| slow wave | 27 % → 23 % | 0.84 | 0.86 | 555 |
| spiral | 46 % → 30 % | 0.83 | 0.65 | 571 |
| loop | 24 % → 23 % | 0.84 | 0.96 | 292 |
| tilted | 11 % → 11 % | 0.86 | 1.00 | 205 |
| over the wet one | 22 % → 22 % | 0.86 | 1.00 | 148 |
| long, no reload | 54 % → 31 % | 0.82 | 0.57 | 1398 | quarters: 0.57 → 0.46 → 0.28 → 0.13

## Brush Artist · Watercolour wash V1
Watercolor · 46 px · 48.3 s

![Brush Artist · Watercolour wash V1](Brush-Artist-Watercolour-wash-V1.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 13 % → 13 % | 0.27 | 1.00 | 96 |
| heavy line | 22 % → 22 % | 0.23 | 0.99 | 165 |
| pressure swell | 14 % → 14 % | 0.26 | 1.00 | 86 |
| fast wave | 46 % → 46 % | 0.22 | 1.01 | 693 |
| slow wave | 44 % → 44 % | 0.29 | 1.00 | 976 |
| spiral | 65 % → 65 % | 0.25 | 1.00 | 491 |
| loop | 38 % → 38 % | 0.26 | 1.00 | 406 |
| tilted | 17 % → 17 % | 0.27 | 1.01 | 159 |
| over the wet one | 34 % → 34 % | 0.27 | 1.00 | 123 |
| long, no reload | 82 % → 82 % | 0.24 | 1.01 | 724 | quarters: 0.27 → 0.24 → 0.19 → 0.14

## Brush Artist · Watercolour wash V2
Watercolor · 46 px · 47.3 s

![Brush Artist · Watercolour wash V2](Brush-Artist-Watercolour-wash-V2.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 13 % → 13 % | 0.39 | 1.00 | 137 |
| heavy line | 22 % → 22 % | 0.33 | 0.99 | 152 |
| pressure swell | 14 % → 14 % | 0.38 | 1.00 | 82 |
| fast wave | 46 % → 46 % | 0.32 | 1.01 | 509 |
| slow wave | 44 % → 44 % | 0.41 | 1.00 | 669 |
| spiral | 65 % → 65 % | 0.36 | 1.00 | 478 |
| loop | 38 % → 38 % | 0.37 | 1.00 | 253 |
| tilted | 17 % → 17 % | 0.39 | 1.01 | 229 |
| over the wet one | 34 % → 34 % | 0.39 | 1.00 | 99 |
| long, no reload | 82 % → 82 % | 0.34 | 1.01 | 701 | quarters: 0.39 → 0.34 → 0.28 → 0.20

## Brush Artist · Watercolour wash V3 purple
Watercolor · 46 px · 46.6 s

![Brush Artist · Watercolour wash V3 purple](Brush-Artist-Watercolour-wash-V3-purple.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 13 % → 13 % | 0.29 | 1.00 | 88 |
| heavy line | 22 % → 22 % | 0.25 | 0.99 | 143 |
| pressure swell | 14 % → 14 % | 0.29 | 1.00 | 101 |
| fast wave | 46 % → 46 % | 0.25 | 1.01 | 396 |
| slow wave | 44 % → 44 % | 0.31 | 1.00 | 639 |
| spiral | 65 % → 65 % | 0.27 | 1.00 | 475 |
| loop | 38 % → 38 % | 0.28 | 1.00 | 250 |
| tilted | 17 % → 17 % | 0.30 | 1.01 | 233 |
| over the wet one | 34 % → 34 % | 0.30 | 1.00 | 148 |
| long, no reload | 82 % → 82 % | 0.26 | 1.01 | 706 | quarters: 0.29 → 0.26 → 0.21 → 0.16

## Brush Artist · Gouache A
Gouache · 30 px · 46.4 s

![Brush Artist · Gouache A](Brush-Artist-Gouache-A.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 8 % → 8 % | 0.16 | 0.97 | 179 |
| heavy line | 15 % → 12 % | 0.16 | 0.78 | 146 |
| pressure swell | 11 % → 9 % | 0.16 | 0.85 | 85 |
| fast wave | 30 % → 14 % | 0.16 | 0.45 | 259 |
| slow wave | 29 % → 14 % | 0.16 | 0.47 | 493 |
| spiral | 40 % → 14 % | 0.16 | 0.35 | 416 |
| loop | 24 % → 15 % | 0.16 | 0.62 | 214 |
| tilted | 10 % → 10 % | 0.16 | 1.01 | 133 |
| over the wet one | 22 % → 19 % | 0.16 | 0.89 | 94 |
| long, no reload | 43 % → 15 % | 0.16 | 0.35 | 917 | quarters: 0.10 → 0.07 → 0.04 → 0.02

## Brush Artist · Gouache A2
Gouache · 30 px · 48.9 s

![Brush Artist · Gouache A2](Brush-Artist-Gouache-A2.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 7 % → 7 % | 0.17 | 1.00 | 91 |
| heavy line | 16 % → 13 % | 0.17 | 0.80 | 164 |
| pressure swell | 11 % → 9 % | 0.17 | 0.88 | 87 |
| fast wave | 32 % → 20 % | 0.17 | 0.63 | 298 |
| slow wave | 30 % → 20 % | 0.16 | 0.68 | 473 |
| spiral | 44 % → 22 % | 0.16 | 0.49 | 785 |
| loop | 26 % → 21 % | 0.16 | 0.82 | 367 |
| tilted | 11 % → 11 % | 0.17 | 1.01 | 147 |
| over the wet one | 24 % → 22 % | 0.17 | 0.93 | 122 |
| long, no reload | 52 % → 23 % | 0.16 | 0.44 | 650 | quarters: 0.12 → 0.09 → 0.06 → 0.04

## Brush Artist · Oil A
Oil · 30 px · 28.5 s

![Brush Artist · Oil A](Brush-Artist-Oil-A.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 8 % → 8 % | 0.53 | 1.00 | 158 |
| heavy line | 9 % → 9 % | 0.53 | 1.00 | 150 |
| pressure swell | 7 % → 7 % | 0.54 | 1.00 | 148 |
| fast wave | 22 % → 22 % | 0.50 | 1.00 | 1030 |
| slow wave | 22 % → 22 % | 0.50 | 1.00 | 1036 |
| spiral | 34 % → 34 % | 0.41 | 1.00 | 664 |
| loop | 19 % → 19 % | 0.52 | 1.00 | 330 |
| tilted | 10 % → 10 % | 0.52 | 1.00 | 169 |
| over the wet one | 19 % → 19 % | 0.52 | 1.00 | 134 |
| long, no reload | 42 % → 42 % | 0.35 | 1.00 | 917 | quarters: 0.29 → 0.22 → 0.10 → 0.03

Numbers say: pressure barely changes the width.

## Brush Artist · Oil A2
Oil · 30 px · 26.1 s

![Brush Artist · Oil A2](Brush-Artist-Oil-A2.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 9 % → 9 % | 0.53 | 1.00 | 147 |
| heavy line | 9 % → 9 % | 0.53 | 1.00 | 165 |
| pressure swell | 7 % → 7 % | 0.54 | 1.00 | 104 |
| fast wave | 23 % → 23 % | 0.53 | 1.00 | 429 |
| slow wave | 23 % → 23 % | 0.53 | 1.00 | 685 |
| spiral | 36 % → 36 % | 0.50 | 1.00 | 815 |
| loop | 19 % → 19 % | 0.54 | 1.00 | 408 |
| tilted | 11 % → 11 % | 0.53 | 1.00 | 176 |
| over the wet one | 19 % → 19 % | 0.53 | 1.00 | 178 |
| long, no reload | 47 % → 47 % | 0.45 | 1.00 | 921 | quarters: 0.31 → 0.27 → 0.22 → 0.14

Numbers say: pressure barely changes the width.

## Brush Artist · Charcoal C1 (pastel path)
Pastel · 20 px · 14.0 s

![Brush Artist · Charcoal C1 (pastel path)](Brush-Artist-Charcoal-C1-pastel-path.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 4 % → 4 % | 0.74 | 1.00 | 34 |
| heavy line | 5 % → 5 % | 0.74 | 1.00 | 65 |
| pressure swell | 4 % → 4 % | 0.74 | 1.00 | 24 |
| fast wave | 12 % → 12 % | 0.74 | 1.00 | 92 |
| slow wave | 11 % → 11 % | 0.74 | 1.00 | 130 |
| spiral | 20 % → 20 % | 0.74 | 1.00 | 142 |
| loop | 10 % → 10 % | 0.74 | 1.00 | 76 |
| tilted | 4 % → 4 % | 0.74 | 1.00 | 30 |
| over the wet one | 8 % → 8 % | 0.74 | 1.00 | 38 |
| long, no reload | 27 % → 27 % | 0.74 | 1.00 | 259 | quarters: 0.23 → 0.22 → 0.22 → 0.23

Numbers say: the long stroke does not run out of paint.

## Brush Artist · Charcoal C2 (big stick)
Charcoal · 40 px · 14.2 s

![Brush Artist · Charcoal C2 (big stick)](Brush-Artist-Charcoal-C2-big-stick.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 8 % → 8 % | 0.77 | 1.00 | 38 |
| heavy line | 9 % → 9 % | 0.77 | 1.00 | 60 |
| pressure swell | 7 % → 7 % | 0.77 | 1.00 | 40 |
| fast wave | 21 % → 21 % | 0.77 | 1.00 | 97 |
| slow wave | 20 % → 20 % | 0.77 | 1.00 | 174 |
| spiral | 36 % → 36 % | 0.77 | 1.00 | 187 |
| loop | 18 % → 18 % | 0.77 | 1.00 | 95 |
| tilted | 8 % → 8 % | 0.77 | 1.00 | 65 |
| over the wet one | 16 % → 16 % | 0.77 | 1.00 | 41 |
| long, no reload | 43 % → 43 % | 0.78 | 1.00 | 255 | quarters: 0.37 → 0.36 → 0.36 → 0.36

Numbers say: the long stroke does not run out of paint.

## Brush Artist · Charcoal C3 (pastel, charcoal tip)
Pastel · 20 px · 13.4 s

![Brush Artist · Charcoal C3 (pastel, charcoal tip)](Brush-Artist-Charcoal-C3-pastel-charcoal-tip.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 3 % → 3 % | 0.73 | 1.00 | 21 |
| heavy line | 4 % → 4 % | 0.74 | 1.00 | 35 |
| pressure swell | 3 % → 3 % | 0.73 | 1.00 | 20 |
| fast wave | 11 % → 11 % | 0.74 | 1.00 | 80 |
| slow wave | 10 % → 10 % | 0.74 | 1.00 | 119 |
| spiral | 15 % → 15 % | 0.74 | 1.00 | 140 |
| loop | 7 % → 7 % | 0.74 | 1.00 | 83 |
| tilted | 3 % → 3 % | 0.74 | 1.00 | 34 |
| over the wet one | 6 % → 6 % | 0.74 | 1.00 | 35 |
| long, no reload | 15 % → 15 % | 0.74 | 1.00 | 224 | quarters: 0.13 → 0.12 → 0.13 → 0.13

Numbers say: the long stroke does not run out of paint.

