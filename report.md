![All brushes](contact.png)

# Brush Lab — 42 brushes · Nov 2, 2026 at 11:20 PM

Every sheet: 1500 × 600, ten strokes in a 5 × 2 grid — 1. light line · 2. heavy line · 3. pressure swell · 4. fast wave · 5. slow wave · 6. spiral · 7. loop · 8. tilted · 9. over the wet one · 10. long, no reload (cell 8 holds «tilted» and «over the wet one» crossed). The CPU reference of Mamay's paint engine; the wet layer settles 20 s at the end.

Columns: **covered** = share of the cell with paint right after the stroke → after settling; **dark** = mean darkness of the painted pixels above the paper's own grain (0 = paper, 1 = black); **spread** = how far wet paint went beyond the stroke (1.0 = stayed); **ms** = the stroke on the CPU; long stroke: paint in each quarter of its length (it should run out: wet → streaks → dry tail).

## Ink Line
Ink · 12 px · 34.9 s

![Ink Line](Ink-Line.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 1 % → 4 % | 0.55 | 2.44 | 55 |
| heavy line | 5 % → 6 % | 0.68 | 1.13 | 99 |
| pressure swell | 3 % → 4 % | 0.64 | 1.40 | 61 |
| fast wave | 10 % → 11 % | 0.59 | 1.11 | 170 |
| slow wave | 8 % → 10 % | 0.57 | 1.16 | 166 |
| spiral | 14 % → 15 % | 0.50 | 1.07 | 301 |
| loop | 8 % → 9 % | 0.61 | 1.16 | 136 |
| tilted | 5 % → 5 % | 0.65 | 1.05 | 93 |
| over the wet one | 10 % → 11 % | 0.65 | 1.15 | 69 |
| long, no reload | 18 % → 17 % | 0.47 | 0.96 | 540 | quarters: 0.22 → 0.09 → 0.04 → 0.02

Numbers say: wet paint spreads well beyond the stroke.

## Dense Ink
Ink · 14 px · 35.9 s

![Dense Ink](Dense-Ink.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 5 % → 7 % | 0.72 | 1.26 | 68 |
| heavy line | 7 % → 7 % | 0.73 | 1.09 | 93 |
| pressure swell | 5 % → 6 % | 0.72 | 1.17 | 63 |
| fast wave | 13 % → 13 % | 0.69 | 1.01 | 185 |
| slow wave | 12 % → 12 % | 0.67 | 1.04 | 189 |
| spiral | 18 % → 15 % | 0.65 | 0.80 | 331 |
| loop | 11 % → 12 % | 0.69 | 1.08 | 164 |
| tilted | 5 % → 6 % | 0.72 | 1.07 | 111 |
| over the wet one | 12 % → 13 % | 0.72 | 1.11 | 77 |
| long, no reload | 23 % → 15 % | 0.64 | 0.66 | 508 | quarters: 0.30 → 0.12 → 0.04 → 0.02

## Transparent Wash
Watercolor · 22 px · 36.8 s

![Transparent Wash](Transparent-Wash.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 2 % → 5 % | 0.27 | 2.25 | 61 |
| heavy line | 7 % → 9 % | 0.27 | 1.22 | 94 |
| pressure swell | 4 % → 6 % | 0.28 | 1.54 | 54 |
| fast wave | 14 % → 16 % | 0.20 | 1.17 | 189 |
| slow wave | 12 % → 15 % | 0.21 | 1.28 | 231 |
| spiral | 18 % → 22 % | 0.16 | 1.23 | 248 |
| loop | 11 % → 13 % | 0.22 | 1.20 | 137 |
| tilted | 8 % → 8 % | 0.24 | 1.06 | 94 |
| over the wet one | 13 % → 16 % | 0.24 | 1.18 | 65 |
| long, no reload | 26 % → 32 % | 0.13 | 1.22 | 482 | quarters: 0.11 → 0.04 → 0.02 → 0.01

Numbers say: wet paint spreads well beyond the stroke.

## Dry Brush
Gouache · 24 px · 25.1 s

![Dry Brush](Dry-Brush.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 5 % → 0 % | 0.65 | 0.09 | 66 |
| heavy line | 6 % → 0 % | 0.65 | 0.02 | 207 |
| pressure swell | 5 % → 0 % | 0.65 | 0.08 | 100 |
| fast wave | 6 % → 1 % | 0.65 | 0.08 | 185 |
| slow wave | 7 % → 0 % | 0.65 | 0.06 | 355 |
| spiral | 7 % → 0 % | 0.65 | 0.07 | 332 |
| loop | 10 % → 0 % | 0.65 | 0.04 | 173 |
| tilted | 4 % → 3 % | 0.65 | 0.88 | 112 |
| over the wet one | 9 % → 1 % | 0.65 | 0.12 | 94 |
| long, no reload | 6 % → 1 % | 0.65 | 0.14 | 422 | quarters: 0.12 → 0.00 → 0.00 → 0.00

## Wax Crayon
Wax · 8 px · 13.2 s

![Wax Crayon](Wax-Crayon.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 1 % → 1 % | 0.71 | 1.00 | 47 |
| heavy line | 1 % → 1 % | 0.69 | 1.00 | 38 |
| pressure swell | 1 % → 1 % | 0.70 | 1.00 | 30 |
| fast wave | 3 % → 3 % | 0.69 | 1.00 | 73 |
| slow wave | 3 % → 3 % | 0.70 | 1.00 | 47 |
| spiral | 5 % → 5 % | 0.70 | 1.00 | 92 |
| loop | 3 % → 3 % | 0.70 | 1.00 | 47 |
| tilted | 2 % → 2 % | 0.68 | 1.00 | 42 |
| over the wet one | 3 % → 3 % | 0.68 | 1.00 | 40 |
| long, no reload | 7 % → 7 % | 0.70 | 1.00 | 123 | quarters: 0.06 → 0.06 → 0.06 → 0.06

Numbers say: the long stroke does not run out of paint.

## Oil Pastel
Wax · 12 px · 13.3 s

![Oil Pastel](Oil-Pastel.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 1 % → 1 % | 0.68 | 1.00 | 56 |
| heavy line | 2 % → 2 % | 0.68 | 1.00 | 54 |
| pressure swell | 2 % → 2 % | 0.69 | 1.00 | 19 |
| fast wave | 5 % → 5 % | 0.68 | 1.00 | 71 |
| slow wave | 5 % → 5 % | 0.68 | 1.00 | 114 |
| spiral | 8 % → 8 % | 0.68 | 1.00 | 130 |
| loop | 4 % → 4 % | 0.68 | 1.00 | 70 |
| tilted | 2 % → 2 % | 0.68 | 1.00 | 66 |
| over the wet one | 5 % → 5 % | 0.68 | 1.00 | 39 |
| long, no reload | 13 % → 13 % | 0.68 | 1.00 | 201 | quarters: 0.10 → 0.09 → 0.10 → 0.10

Numbers say: the long stroke does not run out of paint.

## Charcoal
Charcoal · 5 px · 11.1 s

![Charcoal](Charcoal.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 1 % → 1 % | 0.74 | 1.00 | 41 |
| heavy line | 1 % → 1 % | 0.74 | 1.00 | 19 |
| pressure swell | 1 % → 1 % | 0.74 | 1.00 | 13 |
| fast wave | 2 % → 2 % | 0.73 | 1.00 | 35 |
| slow wave | 2 % → 2 % | 0.74 | 1.00 | 29 |
| spiral | 4 % → 4 % | 0.74 | 1.00 | 54 |
| loop | 2 % → 2 % | 0.74 | 1.00 | 29 |
| tilted | 2 % → 2 % | 0.72 | 1.00 | 19 |
| over the wet one | 2 % → 2 % | 0.72 | 1.00 | 12 |
| long, no reload | 6 % → 6 % | 0.73 | 1.00 | 75 | quarters: 0.05 → 0.05 → 0.05 → 0.05

Numbers say: the long stroke does not run out of paint.

## Impasto
Heavy acrylic · 22 px · 17.4 s

![Impasto](Impasto.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 8 % → 8 % | 0.71 | 0.93 | 76 |
| heavy line | 10 % → 9 % | 0.70 | 0.94 | 102 |
| pressure swell | 7 % → 7 % | 0.72 | 0.94 | 77 |
| fast wave | 20 % → 13 % | 0.71 | 0.64 | 180 |
| slow wave | 21 % → 14 % | 0.71 | 0.66 | 337 |
| spiral | 30 % → 14 % | 0.71 | 0.46 | 296 |
| loop | 18 % → 14 % | 0.71 | 0.77 | 161 |
| tilted | 8 % → 8 % | 0.70 | 1.00 | 91 |
| over the wet one | 17 % → 15 % | 0.70 | 0.91 | 94 |
| long, no reload | 34 % → 14 % | 0.71 | 0.41 | 468 | quarters: 0.38 → 0.21 → 0.10 → 0.03

## Oil Round
Oil · 18 px · 24.0 s

![Oil Round](Oil-Round.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 2 % → 2 % | 0.71 | 1.00 | 52 |
| heavy line | 6 % → 6 % | 0.72 | 1.00 | 119 |
| pressure swell | 3 % → 3 % | 0.63 | 1.00 | 69 |
| fast wave | 7 % → 7 % | 0.54 | 1.00 | 197 |
| slow wave | 4 % → 4 % | 0.36 | 1.00 | 174 |
| spiral | 5 % → 5 % | 0.21 | 1.00 | 231 |
| loop | 3 % → 3 % | 0.18 | 1.00 | 120 |
| tilted | 2 % → 2 % | 0.33 | 1.00 | 91 |
| over the wet one | 3 % → 3 % | 0.33 | 1.00 | 100 |
| long, no reload | 8 % → 8 % | 0.17 | 1.00 | 449 | quarters: 0.02 → 0.02 → 0.01 → 0.01

## Palette Knife
Oil · 20 px · 23.6 s

![Palette Knife](Palette-Knife.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 8 % → 8 % | 0.67 | 1.00 | 13 |
| heavy line | 8 % → 8 % | 0.73 | 1.00 | 19 |
| pressure swell | 6 % → 6 % | 0.74 | 1.00 | 9 |
| fast wave | 17 % → 17 % | 0.49 | 1.00 | 29 |
| slow wave | 17 % → 17 % | 0.43 | 1.00 | 44 |
| spiral | 18 % → 18 % | 0.45 | 1.00 | 45 |
| loop | 16 % → 16 % | 0.58 | 1.00 | 25 |
| tilted | 5 % → 5 % | 0.72 | 1.00 | 13 |
| over the wet one | 13 % → 13 % | 0.72 | 1.00 | 11 |
| long, no reload | 17 % → 17 % | 0.47 | 1.00 | 118 | quarters: 0.29 → 0.05 → 0.00 → 0.00

Numbers say: pressure barely changes the width.

## Water
Watercolor · 20 px · 36.1 s

![Water](Water.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 0 % → 0 % | 0.00 | 1.00 | 52 |
| heavy line | 0 % → 0 % | 0.00 | 1.00 | 72 |
| pressure swell | 0 % → 0 % | 0.00 | 1.00 | 44 |
| fast wave | 0 % → 0 % | 0.00 | 1.00 | 146 |
| slow wave | 0 % → 0 % | 0.00 | 1.00 | 220 |
| spiral | 0 % → 0 % | 0.00 | 1.00 | 512 |
| loop | 0 % → 0 % | 0.00 | 1.00 | 211 |
| tilted | 0 % → 0 % | 0.00 | 1.00 | 77 |
| over the wet one | 0 % → 0 % | 0.00 | 1.00 | 58 |
| long, no reload | 0 % → 0 % | 0.00 | 1.00 | 354 | quarters: 0.00 → 0.00 → 0.00 → 0.00

Numbers say: **paints nothing**.

## Blender
Pastel · 16 px · 14.3 s

![Blender](Blender.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 0 % → 0 % | 0.00 | 1.00 | 41 |
| heavy line | 0 % → 0 % | 0.00 | 1.00 | 37 |
| pressure swell | 0 % → 0 % | 0.00 | 1.00 | 25 |
| fast wave | 0 % → 0 % | 0.00 | 1.00 | 184 |
| slow wave | 0 % → 0 % | 0.00 | 1.00 | 325 |
| spiral | 0 % → 0 % | 0.00 | 1.00 | 188 |
| loop | 0 % → 0 % | 0.00 | 1.00 | 89 |
| tilted | 0 % → 0 % | 0.00 | 1.00 | 79 |
| over the wet one | 0 % → 0 % | 0.00 | 1.00 | 42 |
| long, no reload | 0 % → 0 % | 0.00 | 1.00 | 192 | quarters: 0.00 → 0.00 → 0.00 → 0.00

Numbers say: **paints nothing**.

## Eraser
Eraser · 16 px · 14.7 s

![Eraser](Eraser.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 0 % → 0 % | 0.00 | 1.00 | 36 |
| heavy line | 0 % → 0 % | 0.00 | 1.00 | 55 |
| pressure swell | 0 % → 0 % | 0.00 | 1.00 | 30 |
| fast wave | 0 % → 0 % | 0.00 | 1.00 | 317 |
| slow wave | 0 % → 0 % | 0.00 | 1.00 | 262 |
| spiral | 0 % → 0 % | 0.00 | 1.00 | 231 |
| loop | 0 % → 0 % | 0.00 | 1.00 | 112 |
| tilted | 0 % → 0 % | 0.00 | 1.00 | 80 |
| over the wet one | 0 % → 0 % | 0.00 | 1.00 | 58 |
| long, no reload | 0 % → 0 % | 0.00 | 1.00 | 184 | quarters: 0.00 → 0.00 → 0.00 → 0.00

Numbers say: **paints nothing**.

## Fan
Gouache · 30 px · 36.9 s

![Fan](Fan.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 9 % → 3 % | 0.63 | 0.37 | 115 |
| heavy line | 11 % → 4 % | 0.63 | 0.39 | 125 |
| pressure swell | 8 % → 5 % | 0.63 | 0.55 | 50 |
| fast wave | 18 % → 5 % | 0.63 | 0.26 | 147 |
| slow wave | 18 % → 5 % | 0.63 | 0.25 | 195 |
| spiral | 24 % → 5 % | 0.63 | 0.20 | 424 |
| loop | 17 % → 5 % | 0.63 | 0.29 | 235 |
| tilted | 5 % → 6 % | 0.63 | 1.05 | 89 |
| over the wet one | 16 % → 8 % | 0.63 | 0.50 | 105 |
| long, no reload | 23 % → 5 % | 0.63 | 0.22 | 730 | quarters: 0.29 → 0.07 → 0.01 → 0.00

## Sponge
Gouache · 30 px · 36.6 s

![Sponge](Sponge.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 4 % → 0 % | 0.62 | 0.12 | 104 |
| heavy line | 12 % → 2 % | 0.62 | 0.14 | 123 |
| pressure swell | 7 % → 2 % | 0.62 | 0.27 | 83 |
| fast wave | 20 % → 4 % | 0.62 | 0.19 | 143 |
| slow wave | 21 % → 4 % | 0.62 | 0.18 | 317 |
| spiral | 28 % → 4 % | 0.62 | 0.14 | 661 |
| loop | 18 % → 5 % | 0.62 | 0.29 | 232 |
| tilted | 7 % → 7 % | 0.62 | 1.04 | 310 |
| over the wet one | 16 % → 6 % | 0.62 | 0.37 | 180 |
| long, no reload | 29 % → 5 % | 0.62 | 0.17 | 684 | quarters: 0.29 → 0.13 → 0.07 → 0.04

## Ink — sumi brush
Watercolor · 22 px · 34.8 s

![Ink — sumi brush](Ink-sumi-brush.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 6 % → 7 % | 0.46 | 1.06 | 57 |
| heavy line | 10 % → 11 % | 0.38 | 1.05 | 63 |
| pressure swell | 7 % → 8 % | 0.42 | 1.04 | 105 |
| fast wave | 21 % → 21 % | 0.32 | 1.00 | 454 |
| slow wave | 19 % → 19 % | 0.37 | 1.01 | 541 |
| spiral | 28 % → 26 % | 0.30 | 0.92 | 813 |
| loop | 17 % → 18 % | 0.37 | 1.06 | 274 |
| tilted | 6 % → 7 % | 0.40 | 1.17 | 73 |
| over the wet one | 16 % → 16 % | 0.40 | 1.01 | 61 |
| long, no reload | 33 % → 29 % | 0.30 | 0.86 | 411 | quarters: 0.23 → 0.11 → 0.06 → 0.04

## Ink — wash
Watercolor · 40 px · 38.3 s

![Ink — wash](Ink-wash.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 8 % → 9 % | 0.05 | 1.26 | 75 |
| heavy line | 11 % → 13 % | 0.04 | 1.22 | 80 |
| pressure swell | 7 % → 9 % | 0.05 | 1.25 | 88 |
| fast wave | 22 % → 27 % | 0.04 | 1.21 | 300 |
| slow wave | 21 % → 26 % | 0.06 | 1.23 | 374 |
| spiral | 34 % → 41 % | 0.04 | 1.21 | 339 |
| loop | 19 % → 24 % | 0.05 | 1.25 | 220 |
| tilted | 7 % → 9 % | 0.05 | 1.21 | 121 |
| over the wet one | 18 % → 21 % | 0.05 | 1.18 | 74 |
| long, no reload | 39 % → 46 % | 0.05 | 1.19 | 502 | quarters: 0.04 → 0.03 → 0.02 → 0.01

## Ink — dry brush
Ink · 30 px · 27.7 s

![Ink — dry brush](Ink-dry-brush.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 9 % → 7 % | 0.81 | 0.78 | 83 |
| heavy line | 11 % → 8 % | 0.80 | 0.73 | 175 |
| pressure swell | 8 % → 7 % | 0.81 | 0.85 | 112 |
| fast wave | 22 % → 8 % | 0.78 | 0.38 | 243 |
| slow wave | 18 % → 6 % | 0.80 | 0.36 | 430 |
| spiral | 23 % → 8 % | 0.77 | 0.35 | 417 |
| loop | 20 % → 8 % | 0.77 | 0.41 | 217 |
| tilted | 9 % → 9 % | 0.78 | 1.01 | 168 |
| over the wet one | 19 % → 14 % | 0.78 | 0.75 | 113 |
| long, no reload | 20 % → 9 % | 0.78 | 0.42 | 582 | quarters: 0.32 → 0.01 → 0.00 → 0.00

## Ink — nib
Watercolor · 5 px · 24.6 s

![Ink — nib](Ink-nib.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 2 % → 2 % | 0.76 | 1.17 | 29 |
| heavy line | 2 % → 2 % | 0.77 | 1.16 | 34 |
| pressure swell | 1 % → 2 % | 0.78 | 1.22 | 21 |
| fast wave | 4 % → 4 % | 0.66 | 1.09 | 66 |
| slow wave | 4 % → 4 % | 0.68 | 1.11 | 79 |
| spiral | 6 % → 6 % | 0.58 | 1.08 | 115 |
| loop | 3 % → 4 % | 0.69 | 1.12 | 77 |
| tilted | 2 % → 2 % | 0.64 | 1.21 | 32 |
| over the wet one | 4 % → 4 % | 0.64 | 1.03 | 32 |
| long, no reload | 7 % → 7 % | 0.53 | 1.02 | 205 | quarters: 0.09 → 0.04 → 0.03 → 0.02

## 0.45 · Dry brush
Gouache · 34 px · 34.9 s

![0.45 · Dry brush](0-45-Dry-brush.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 11 % → 3 % | 0.67 | 0.28 | 130 |
| heavy line | 12 % → 3 % | 0.67 | 0.30 | 167 |
| pressure swell | 9 % → 4 % | 0.67 | 0.40 | 105 |
| fast wave | 20 % → 4 % | 0.67 | 0.19 | 469 |
| slow wave | 20 % → 4 % | 0.67 | 0.18 | 658 |
| spiral | 21 % → 4 % | 0.67 | 0.17 | 719 |
| loop | 21 % → 4 % | 0.67 | 0.19 | 391 |
| tilted | 9 % → 9 % | 0.67 | 0.97 | 294 |
| over the wet one | 20 % → 7 % | 0.67 | 0.33 | 207 |
| long, no reload | 20 % → 4 % | 0.67 | 0.21 | 848 | quarters: 0.38 → 0.07 → 0.00 → 0.00

Numbers say: pressure barely changes the width.

## Dry pastel
Pastel · 26 px · 14.2 s

![Dry pastel](Dry-pastel.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 5 % → 5 % | 0.36 | 1.00 | 47 |
| heavy line | 6 % → 6 % | 0.36 | 1.00 | 45 |
| pressure swell | 5 % → 5 % | 0.36 | 1.00 | 26 |
| fast wave | 15 % → 15 % | 0.36 | 1.00 | 108 |
| slow wave | 14 % → 14 % | 0.36 | 1.00 | 184 |
| spiral | 23 % → 23 % | 0.36 | 1.00 | 166 |
| loop | 11 % → 11 % | 0.36 | 1.00 | 103 |
| tilted | 5 % → 5 % | 0.37 | 1.00 | 49 |
| over the wet one | 10 % → 10 % | 0.37 | 1.00 | 38 |
| long, no reload | 26 % → 26 % | 0.36 | 1.00 | 259 | quarters: 0.11 → 0.10 → 0.10 → 0.11

Numbers say: the long stroke does not run out of paint.

## 0.45 · Charcoal
Charcoal · 18 px · 13.6 s

![0.45 · Charcoal](0-45-Charcoal.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 4 % → 4 % | 0.79 | 1.00 | 50 |
| heavy line | 4 % → 4 % | 0.79 | 1.00 | 19 |
| pressure swell | 4 % → 4 % | 0.79 | 1.00 | 18 |
| fast wave | 11 % → 11 % | 0.79 | 1.00 | 84 |
| slow wave | 11 % → 11 % | 0.78 | 1.00 | 67 |
| spiral | 20 % → 20 % | 0.79 | 1.00 | 93 |
| loop | 10 % → 10 % | 0.79 | 1.00 | 53 |
| tilted | 4 % → 4 % | 0.78 | 1.00 | 25 |
| over the wet one | 9 % → 9 % | 0.78 | 1.00 | 22 |
| long, no reload | 26 % → 26 % | 0.79 | 1.00 | 170 | quarters: 0.23 → 0.22 → 0.23 → 0.24

Numbers say: pressure barely changes the width; the long stroke does not run out of paint.

## Watercolour — wash
Watercolor · 50 px · 43.4 s

![Watercolour — wash](Watercolour-wash.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 9 % → 11 % | 0.01 | 1.22 | 118 |
| heavy line | 12 % → 14 % | 0.01 | 1.17 | 127 |
| pressure swell | 8 % → 10 % | 0.01 | 1.22 | 100 |
| fast wave | 26 % → 30 % | 0.01 | 1.18 | 311 |
| slow wave | 25 % → 29 % | 0.01 | 1.18 | 544 |
| spiral | 39 % → 46 % | 0.01 | 1.17 | 577 |
| loop | 22 % → 27 % | 0.01 | 1.21 | 324 |
| tilted | 10 % → 11 % | 0.01 | 1.18 | 247 |
| over the wet one | 22 % → 25 % | 0.01 | 1.14 | 167 |
| long, no reload | 45 % → 54 % | 0.01 | 1.18 | 859 | quarters: 0.01 → 0.01 → 0.01 → 0.00

## Watercolour — wet-in-wet
Watercolor · 44 px · 41.0 s

![Watercolour — wet-in-wet](Watercolour-wet-in-wet.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 7 % → 9 % | 0.02 | 1.26 | 134 |
| heavy line | 10 % → 12 % | 0.02 | 1.22 | 113 |
| pressure swell | 7 % → 9 % | 0.02 | 1.21 | 93 |
| fast wave | 23 % → 27 % | 0.02 | 1.17 | 248 |
| slow wave | 22 % → 26 % | 0.02 | 1.18 | 459 |
| spiral | 36 % → 43 % | 0.02 | 1.20 | 437 |
| loop | 19 % → 23 % | 0.02 | 1.20 | 285 |
| tilted | 7 % → 9 % | 0.02 | 1.19 | 165 |
| over the wet one | 17 % → 19 % | 0.02 | 1.12 | 113 |
| long, no reload | 42 % → 49 % | 0.02 | 1.18 | 758 | quarters: 0.01 → 0.01 → 0.01 → 0.01

## Watercolour — glaze
Watercolor · 38 px · 41.0 s

![Watercolour — glaze](Watercolour-glaze.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 7 % → 9 % | 0.01 | 1.28 | 98 |
| heavy line | 10 % → 13 % | 0.01 | 1.25 | 125 |
| pressure swell | 7 % → 9 % | 0.01 | 1.29 | 71 |
| fast wave | 20 % → 25 % | 0.01 | 1.24 | 244 |
| slow wave | 19 % → 24 % | 0.01 | 1.26 | 388 |
| spiral | 31 % → 37 % | 0.01 | 1.21 | 434 |
| loop | 18 % → 23 % | 0.01 | 1.27 | 226 |
| tilted | 7 % → 8 % | 0.01 | 1.20 | 158 |
| over the wet one | 17 % → 20 % | 0.01 | 1.19 | 101 |
| long, no reload | 36 % → 42 % | 0.01 | 1.17 | 545 | quarters: 0.01 → 0.00 → 0.00 → 0.00

## Watercolour — granulating
Watercolor · 44 px · 37.3 s

![Watercolour — granulating](Watercolour-granulating.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 8 % → 10 % | 0.02 | 1.18 | 97 |
| heavy line | 12 % → 14 % | 0.01 | 1.15 | 164 |
| pressure swell | 8 % → 10 % | 0.02 | 1.18 | 152 |
| fast wave | 25 % → 29 % | 0.01 | 1.15 | 288 |
| slow wave | 24 % → 27 % | 0.02 | 1.16 | 405 |
| spiral | 39 % → 44 % | 0.01 | 1.15 | 685 |
| loop | 22 % → 25 % | 0.01 | 1.17 | 389 |
| tilted | 9 % → 11 % | 0.02 | 1.15 | 179 |
| over the wet one | 21 % → 23 % | 0.02 | 1.11 | 124 |
| long, no reload | 45 % → 52 % | 0.01 | 1.15 | 615 | quarters: 0.01 → 0.01 → 0.01 → 0.01

## Watercolour — dry brush
Watercolor · 36 px · 29.2 s

![Watercolour — dry brush](Watercolour-dry-brush.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 7 % → 8 % | 0.05 | 1.07 | 199 |
| heavy line | 11 % → 12 % | 0.04 | 1.03 | 244 |
| pressure swell | 9 % → 10 % | 0.05 | 1.07 | 175 |
| fast wave | 21 % → 14 % | 0.04 | 0.68 | 384 |
| slow wave | 19 % → 13 % | 0.04 | 0.70 | 461 |
| spiral | 24 % → 15 % | 0.04 | 0.61 | 635 |
| loop | 17 % → 14 % | 0.04 | 0.85 | 235 |
| tilted | 7 % → 8 % | 0.05 | 1.19 | 118 |
| over the wet one | 17 % → 17 % | 0.05 | 0.99 | 101 |
| long, no reload | 22 % → 15 % | 0.04 | 0.68 | 556 | quarters: 0.02 → 0.00 → 0.00 → 0.00

## Gouache
Gouache · 30 px · 27.1 s

![Gouache](Gouache.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 8 % → 6 % | 0.14 | 0.67 | 67 |
| heavy line | 13 % → 6 % | 0.14 | 0.47 | 80 |
| pressure swell | 10 % → 6 % | 0.14 | 0.61 | 62 |
| fast wave | 27 % → 7 % | 0.14 | 0.27 | 223 |
| slow wave | 27 % → 7 % | 0.14 | 0.27 | 326 |
| spiral | 37 % → 8 % | 0.14 | 0.22 | 307 |
| loop | 22 % → 8 % | 0.14 | 0.36 | 182 |
| tilted | 9 % → 9 % | 0.14 | 1.02 | 133 |
| over the wet one | 20 % → 13 % | 0.14 | 0.67 | 135 |
| long, no reload | 38 % → 10 % | 0.14 | 0.25 | 518 | quarters: 0.07 → 0.04 → 0.01 → 0.01

## Oil — alla prima
Oil · 30 px · 22.1 s

![Oil — alla prima](Oil-alla-prima.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 9 % → 9 % | 0.50 | 1.00 | 77 |
| heavy line | 10 % → 10 % | 0.50 | 1.00 | 77 |
| pressure swell | 8 % → 8 % | 0.52 | 1.00 | 68 |
| fast wave | 24 % → 24 % | 0.49 | 1.00 | 330 |
| slow wave | 25 % → 25 % | 0.50 | 1.00 | 608 |
| spiral | 38 % → 38 % | 0.44 | 1.00 | 372 |
| loop | 21 % → 21 % | 0.50 | 1.00 | 222 |
| tilted | 11 % → 11 % | 0.50 | 1.00 | 111 |
| over the wet one | 20 % → 20 % | 0.50 | 1.00 | 98 |
| long, no reload | 46 % → 46 % | 0.40 | 1.00 | 590 | quarters: 0.31 → 0.24 → 0.17 → 0.10

Numbers say: pressure barely changes the width.

## Oil — impasto
Oil · 34 px · 23.0 s

![Oil — impasto](Oil-impasto.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 11 % → 11 % | 0.24 | 1.00 | 128 |
| heavy line | 12 % → 12 % | 0.23 | 1.00 | 137 |
| pressure swell | 9 % → 9 % | 0.25 | 1.00 | 132 |
| fast wave | 29 % → 29 % | 0.21 | 1.00 | 281 |
| slow wave | 29 % → 29 % | 0.21 | 1.00 | 459 |
| spiral | 48 % → 48 % | 0.17 | 1.00 | 491 |
| loop | 25 % → 25 % | 0.21 | 1.00 | 258 |
| tilted | 12 % → 12 % | 0.24 | 1.00 | 151 |
| over the wet one | 23 % → 23 % | 0.24 | 1.00 | 153 |
| long, no reload | 55 % → 55 % | 0.15 | 1.00 | 799 | quarters: 0.16 → 0.11 → 0.06 → 0.02

Numbers say: pressure barely changes the width.

## Oil — glaze
Oil · 40 px · 19.7 s

![Oil — glaze](Oil-glaze.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 10 % → 10 % | 0.49 | 1.00 | 119 |
| heavy line | 14 % → 14 % | 0.48 | 1.00 | 139 |
| pressure swell | 10 % → 10 % | 0.49 | 1.00 | 108 |
| fast wave | 28 % → 28 % | 0.46 | 1.00 | 296 |
| slow wave | 30 % → 30 % | 0.46 | 1.00 | 538 |
| spiral | 42 % → 42 % | 0.44 | 1.00 | 514 |
| loop | 24 % → 24 % | 0.47 | 1.00 | 397 |
| tilted | 11 % → 11 % | 0.47 | 1.00 | 242 |
| over the wet one | 23 % → 23 % | 0.47 | 1.00 | 115 |
| long, no reload | 47 % → 47 % | 0.43 | 1.00 | 828 | quarters: 0.33 → 0.24 → 0.18 → 0.14

## Oil — scumble
Oil · 36 px · 25.6 s

![Oil — scumble](Oil-scumble.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 11 % → 11 % | 0.06 | 1.00 | 146 |
| heavy line | 12 % → 12 % | 0.05 | 1.00 | 163 |
| pressure swell | 9 % → 9 % | 0.06 | 1.00 | 116 |
| fast wave | 18 % → 18 % | 0.04 | 1.00 | 382 |
| slow wave | 20 % → 20 % | 0.04 | 1.00 | 1021 |
| spiral | 19 % → 19 % | 0.03 | 1.00 | 839 |
| loop | 22 % → 22 % | 0.04 | 1.00 | 335 |
| tilted | 10 % → 10 % | 0.05 | 1.00 | 173 |
| over the wet one | 21 % → 21 % | 0.05 | 1.00 | 172 |
| long, no reload | 18 % → 18 % | 0.04 | 1.00 | 1026 | quarters: 0.03 → 0.00 → 0.00 → 0.00

Numbers say: pressure barely changes the width.

## Acrylic — heavy body
Heavy acrylic · 30 px · 19.2 s

![Acrylic — heavy body](Acrylic-heavy-body.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 10 % → 9 % | 0.51 | 0.93 | 139 |
| heavy line | 11 % → 10 % | 0.51 | 0.93 | 106 |
| pressure swell | 8 % → 8 % | 0.52 | 0.94 | 119 |
| fast wave | 24 % → 14 % | 0.51 | 0.58 | 382 |
| slow wave | 25 % → 15 % | 0.51 | 0.59 | 556 |
| spiral | 37 % → 15 % | 0.51 | 0.40 | 452 |
| loop | 22 % → 16 % | 0.51 | 0.73 | 205 |
| tilted | 10 % → 10 % | 0.51 | 1.00 | 133 |
| over the wet one | 20 % → 17 % | 0.51 | 0.88 | 129 |
| long, no reload | 39 % → 15 % | 0.51 | 0.40 | 657 | quarters: 0.30 → 0.20 → 0.10 → 0.02

Numbers say: pressure barely changes the width.

## Acrylic — fluid
Watercolor · 36 px · 37.8 s

![Acrylic — fluid](Acrylic-fluid.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 9 % → 10 % | 0.06 | 1.11 | 68 |
| heavy line | 13 % → 14 % | 0.05 | 1.07 | 121 |
| pressure swell | 9 % → 10 % | 0.07 | 1.09 | 70 |
| fast wave | 26 % → 28 % | 0.05 | 1.07 | 215 |
| slow wave | 24 % → 26 % | 0.07 | 1.08 | 386 |
| spiral | 39 % → 41 % | 0.05 | 1.06 | 319 |
| loop | 22 % → 25 % | 0.06 | 1.11 | 152 |
| tilted | 8 % → 9 % | 0.07 | 1.17 | 100 |
| over the wet one | 21 % → 22 % | 0.07 | 1.05 | 72 |
| long, no reload | 44 % → 47 % | 0.05 | 1.06 | 547 | quarters: 0.05 → 0.03 → 0.02 → 0.01

## Acrylic — palette knife
Heavy acrylic · 42 px · 23.3 s

![Acrylic — palette knife](Acrylic-palette-knife.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 15 % → 15 % | 0.06 | 0.98 | 54 |
| heavy line | 15 % → 15 % | 0.05 | 0.98 | 41 |
| pressure swell | 12 % → 12 % | 0.06 | 0.99 | 16 |
| fast wave | 37 % → 20 % | 0.06 | 0.54 | 47 |
| slow wave | 37 % → 21 % | 0.06 | 0.56 | 98 |
| spiral | 48 % → 19 % | 0.06 | 0.38 | 123 |
| loop | 32 % → 24 % | 0.05 | 0.75 | 44 |
| tilted | 12 % → 12 % | 0.05 | 1.00 | 27 |
| over the wet one | 26 % → 26 % | 0.05 | 0.98 | 30 |
| long, no reload | 55 % → 20 % | 0.06 | 0.36 | 207 | quarters: 0.04 → 0.02 → 0.00 → 0.00

Numbers say: pressure barely changes the width.

## Finger on oil
Oil · 30 px · 17.7 s

![Finger on oil](Finger-on-oil.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 8 % → 8 % | 0.34 | 1.00 | 43 |
| heavy line | 12 % → 12 % | 0.30 | 1.00 | 88 |
| pressure swell | 8 % → 8 % | 0.35 | 1.00 | 54 |
| fast wave | 16 % → 16 % | 0.22 | 1.00 | 166 |
| slow wave | 17 % → 17 % | 0.23 | 1.00 | 379 |
| spiral | 18 % → 18 % | 0.22 | 1.00 | 386 |
| loop | 18 % → 18 % | 0.23 | 1.00 | 138 |
| tilted | 9 % → 9 % | 0.31 | 1.00 | 92 |
| over the wet one | 18 % → 18 % | 0.31 | 1.00 | 72 |
| long, no reload | 15 % → 15 % | 0.23 | 1.00 | 486 | quarters: 0.13 → 0.01 → 0.00 → 0.00

## Palette knife — oil
Oil · 44 px · 20.0 s

![Palette knife — oil](Palette-knife-oil.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 16 % → 16 % | 0.10 | 1.00 | 23 |
| heavy line | 16 % → 16 % | 0.09 | 1.00 | 21 |
| pressure swell | 12 % → 12 % | 0.10 | 1.00 | 18 |
| fast wave | 39 % → 39 % | 0.07 | 1.00 | 51 |
| slow wave | 39 % → 39 % | 0.07 | 1.00 | 93 |
| spiral | 54 % → 54 % | 0.05 | 1.00 | 93 |
| loop | 34 % → 34 % | 0.08 | 1.00 | 57 |
| tilted | 13 % → 13 % | 0.09 | 1.00 | 30 |
| over the wet one | 28 % → 28 % | 0.09 | 1.00 | 27 |
| long, no reload | 65 % → 65 % | 0.05 | 1.00 | 149 | quarters: 0.08 → 0.04 → 0.01 → 0.00

Numbers say: pressure barely changes the width.

## 0.45 · Sponge
Watercolor · 46 px · 24.7 s

![0.45 · Sponge](0-45-Sponge.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 11 % → 0 % | 0.00 | 0.00 | 59 |
| heavy line | 13 % → 0 % | 0.01 | 0.00 | 71 |
| pressure swell | 9 % → 1 % | 0.02 | 0.14 | 46 |
| fast wave | 23 % → 2 % | 0.01 | 0.08 | 174 |
| slow wave | 26 % → 8 % | 0.02 | 0.30 | 363 |
| spiral | 34 % → 11 % | 0.02 | 0.32 | 252 |
| loop | 22 % → 4 % | 0.02 | 0.19 | 132 |
| tilted | 9 % → 10 % | 0.04 | 1.19 | 119 |
| over the wet one | 22 % → 10 % | 0.04 | 0.44 | 126 |
| long, no reload | 41 % → 19 % | 0.02 | 0.47 | 451 | quarters: 0.01 → 0.01 → 0.01 → 0.01

## 0.45 · Eraser
Eraser · 30 px · 10.6 s

![0.45 · Eraser](0-45-Eraser.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 0 % → 0 % | 0.00 | 1.00 | 42 |
| heavy line | 0 % → 0 % | 0.00 | 1.00 | 44 |
| pressure swell | 0 % → 0 % | 0.00 | 1.00 | 33 |
| fast wave | 0 % → 0 % | 0.00 | 1.00 | 125 |
| slow wave | 0 % → 0 % | 0.00 | 1.00 | 216 |
| spiral | 0 % → 0 % | 0.00 | 1.00 | 226 |
| loop | 0 % → 0 % | 0.00 | 1.00 | 103 |
| tilted | 0 % → 0 % | 0.00 | 1.00 | 77 |
| over the wet one | 0 % → 0 % | 0.00 | 1.00 | 61 |
| long, no reload | 0 % → 0 % | 0.00 | 1.00 | 374 | quarters: 0.00 → 0.00 → 0.00 → 0.00

Numbers say: **paints nothing**; the long stroke does not run out of paint.

## Lift wet paint
Eraser · 30 px · 9.9 s

![Lift wet paint](Lift-wet-paint.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 0 % → 0 % | 0.00 | 1.00 | 28 |
| heavy line | 0 % → 0 % | 0.00 | 1.00 | 40 |
| pressure swell | 0 % → 0 % | 0.00 | 1.00 | 27 |
| fast wave | 0 % → 0 % | 0.00 | 1.00 | 90 |
| slow wave | 0 % → 0 % | 0.00 | 1.00 | 146 |
| spiral | 0 % → 0 % | 0.00 | 1.00 | 148 |
| loop | 0 % → 0 % | 0.00 | 1.00 | 73 |
| tilted | 0 % → 0 % | 0.00 | 1.00 | 49 |
| over the wet one | 0 % → 0 % | 0.00 | 1.00 | 34 |
| long, no reload | 0 % → 0 % | 0.00 | 1.00 | 211 | quarters: 0.00 → 0.00 → 0.00 → 0.00

Numbers say: **paints nothing**.

## Sgraffito
Eraser · 10 px · 8.6 s

![Sgraffito](Sgraffito.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 0 % → 0 % | 0.00 | 1.00 | 14 |
| heavy line | 0 % → 0 % | 0.00 | 1.00 | 9 |
| pressure swell | 0 % → 0 % | 0.00 | 1.00 | 6 |
| fast wave | 0 % → 0 % | 0.00 | 1.00 | 16 |
| slow wave | 0 % → 0 % | 0.00 | 1.00 | 14 |
| spiral | 0 % → 0 % | 0.00 | 1.00 | 29 |
| loop | 0 % → 0 % | 0.00 | 1.00 | 17 |
| tilted | 0 % → 0 % | 0.00 | 1.00 | 6 |
| over the wet one | 0 % → 0 % | 0.00 | 1.00 | 6 |
| long, no reload | 0 % → 0 % | 0.00 | 1.00 | 34 | quarters: 0.00 → 0.00 → 0.00 → 0.00

Numbers say: **paints nothing**.

## Brush Artist · Sumi — wetter
Watercolor · 24 px · 23.2 s

![Brush Artist · Sumi — wetter](Brush-Artist-Sumi-wetter.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 5 % → 6 % | 0.21 | 1.11 | 54 |
| heavy line | 11 % → 12 % | 0.13 | 1.13 | 70 |
| pressure swell | 7 % → 8 % | 0.16 | 1.13 | 43 |
| fast wave | 21 % → 24 % | 0.12 | 1.15 | 140 |
| slow wave | 19 % → 22 % | 0.15 | 1.14 | 233 |
| spiral | 29 % → 32 % | 0.12 | 1.13 | 249 |
| loop | 17 % → 19 % | 0.15 | 1.15 | 123 |
| tilted | 6 % → 7 % | 0.16 | 1.17 | 59 |
| over the wet one | 16 % → 17 % | 0.16 | 1.07 | 53 |
| long, no reload | 33 % → 37 % | 0.12 | 1.12 | 355 | quarters: 0.10 → 0.05 → 0.03 → 0.02

