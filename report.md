![All brushes](contact.png)

# Brush Lab — 42 brushes · Nov 2, 2026 at 11:37 PM

Every sheet: 1500 × 600, ten strokes in a 5 × 2 grid — 1. light line · 2. heavy line · 3. pressure swell · 4. fast wave · 5. slow wave · 6. spiral · 7. loop · 8. tilted · 9. over the wet one · 10. long, no reload (cell 8 holds «tilted» and «over the wet one» crossed). The CPU reference of Mamay's paint engine; the wet layer settles 20 s at the end.

Columns: **covered** = share of the cell with paint right after the stroke → after settling; **dark** = mean darkness of the painted pixels above the paper's own grain (0 = paper, 1 = black); **spread** = how far wet paint went beyond the stroke (1.0 = stayed); **ms** = the stroke on the CPU; long stroke: paint in each quarter of its length (it should run out: wet → streaks → dry tail).

## Ink Line
Ink · 12 px · 25.1 s

![Ink Line](Ink-Line.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 1 % → 4 % | 0.55 | 2.44 | 93 |
| heavy line | 5 % → 6 % | 0.68 | 1.13 | 82 |
| pressure swell | 3 % → 4 % | 0.64 | 1.40 | 41 |
| fast wave | 10 % → 11 % | 0.59 | 1.11 | 131 |
| slow wave | 8 % → 10 % | 0.57 | 1.16 | 117 |
| spiral | 14 % → 15 % | 0.50 | 1.07 | 242 |
| loop | 8 % → 9 % | 0.61 | 1.16 | 107 |
| tilted | 5 % → 5 % | 0.65 | 1.05 | 61 |
| over the wet one | 10 % → 11 % | 0.65 | 1.15 | 55 |
| long, no reload | 18 % → 17 % | 0.47 | 0.96 | 313 | quarters: 0.22 → 0.09 → 0.04 → 0.02

Numbers say: wet paint spreads well beyond the stroke.

## Dense Ink
Ink · 14 px · 26.3 s

![Dense Ink](Dense-Ink.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 5 % → 7 % | 0.72 | 1.26 | 147 |
| heavy line | 7 % → 7 % | 0.73 | 1.09 | 82 |
| pressure swell | 5 % → 6 % | 0.72 | 1.17 | 52 |
| fast wave | 13 % → 13 % | 0.69 | 1.01 | 148 |
| slow wave | 12 % → 12 % | 0.67 | 1.04 | 152 |
| spiral | 18 % → 15 % | 0.65 | 0.80 | 295 |
| loop | 11 % → 12 % | 0.69 | 1.08 | 125 |
| tilted | 5 % → 6 % | 0.72 | 1.07 | 74 |
| over the wet one | 12 % → 13 % | 0.72 | 1.11 | 62 |
| long, no reload | 23 % → 15 % | 0.64 | 0.66 | 429 | quarters: 0.30 → 0.12 → 0.04 → 0.02

## Transparent Wash
Watercolor · 22 px · 27.3 s

![Transparent Wash](Transparent-Wash.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 2 % → 5 % | 0.27 | 2.25 | 89 |
| heavy line | 7 % → 9 % | 0.27 | 1.22 | 62 |
| pressure swell | 4 % → 6 % | 0.28 | 1.54 | 39 |
| fast wave | 14 % → 16 % | 0.20 | 1.17 | 117 |
| slow wave | 12 % → 15 % | 0.21 | 1.28 | 172 |
| spiral | 18 % → 22 % | 0.16 | 1.23 | 232 |
| loop | 11 % → 13 % | 0.22 | 1.20 | 96 |
| tilted | 8 % → 8 % | 0.24 | 1.06 | 83 |
| over the wet one | 13 % → 16 % | 0.24 | 1.18 | 53 |
| long, no reload | 26 % → 32 % | 0.13 | 1.22 | 287 | quarters: 0.11 → 0.04 → 0.02 → 0.01

Numbers say: wet paint spreads well beyond the stroke.

## Dry Brush
Gouache · 24 px · 20.5 s

![Dry Brush](Dry-Brush.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 5 % → 0 % | 0.65 | 0.09 | 68 |
| heavy line | 6 % → 0 % | 0.65 | 0.02 | 152 |
| pressure swell | 5 % → 0 % | 0.65 | 0.08 | 83 |
| fast wave | 6 % → 1 % | 0.65 | 0.08 | 148 |
| slow wave | 7 % → 0 % | 0.65 | 0.06 | 297 |
| spiral | 7 % → 0 % | 0.65 | 0.07 | 251 |
| loop | 10 % → 0 % | 0.65 | 0.04 | 141 |
| tilted | 4 % → 3 % | 0.65 | 0.88 | 74 |
| over the wet one | 9 % → 1 % | 0.65 | 0.12 | 68 |
| long, no reload | 6 % → 1 % | 0.65 | 0.14 | 357 | quarters: 0.12 → 0.00 → 0.00 → 0.00

## Wax Crayon
Wax · 8 px · 10.8 s

![Wax Crayon](Wax-Crayon.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 1 % → 1 % | 0.71 | 1.00 | 34 |
| heavy line | 1 % → 1 % | 0.69 | 1.00 | 29 |
| pressure swell | 1 % → 1 % | 0.70 | 1.00 | 37 |
| fast wave | 3 % → 3 % | 0.69 | 1.00 | 45 |
| slow wave | 3 % → 3 % | 0.70 | 1.00 | 42 |
| spiral | 5 % → 5 % | 0.70 | 1.00 | 76 |
| loop | 3 % → 3 % | 0.70 | 1.00 | 42 |
| tilted | 2 % → 2 % | 0.68 | 1.00 | 33 |
| over the wet one | 3 % → 3 % | 0.68 | 1.00 | 27 |
| long, no reload | 7 % → 7 % | 0.70 | 1.00 | 123 | quarters: 0.06 → 0.06 → 0.06 → 0.06

Numbers say: the long stroke does not run out of paint.

## Oil Pastel
Wax · 12 px · 10.6 s

![Oil Pastel](Oil-Pastel.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 1 % → 1 % | 0.68 | 1.00 | 37 |
| heavy line | 2 % → 2 % | 0.68 | 1.00 | 30 |
| pressure swell | 2 % → 2 % | 0.69 | 1.00 | 23 |
| fast wave | 5 % → 5 % | 0.68 | 1.00 | 64 |
| slow wave | 5 % → 5 % | 0.68 | 1.00 | 66 |
| spiral | 8 % → 8 % | 0.68 | 1.00 | 110 |
| loop | 4 % → 4 % | 0.68 | 1.00 | 65 |
| tilted | 2 % → 2 % | 0.68 | 1.00 | 43 |
| over the wet one | 5 % → 5 % | 0.68 | 1.00 | 26 |
| long, no reload | 13 % → 13 % | 0.68 | 1.00 | 157 | quarters: 0.10 → 0.09 → 0.10 → 0.10

Numbers say: the long stroke does not run out of paint.

## Charcoal
Charcoal · 5 px · 9.1 s

![Charcoal](Charcoal.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 1 % → 1 % | 0.74 | 1.00 | 13 |
| heavy line | 1 % → 1 % | 0.74 | 1.00 | 17 |
| pressure swell | 1 % → 1 % | 0.74 | 1.00 | 8 |
| fast wave | 2 % → 2 % | 0.73 | 1.00 | 31 |
| slow wave | 2 % → 2 % | 0.74 | 1.00 | 28 |
| spiral | 4 % → 4 % | 0.74 | 1.00 | 48 |
| loop | 2 % → 2 % | 0.74 | 1.00 | 25 |
| tilted | 2 % → 2 % | 0.72 | 1.00 | 17 |
| over the wet one | 2 % → 2 % | 0.72 | 1.00 | 12 |
| long, no reload | 6 % → 6 % | 0.73 | 1.00 | 73 | quarters: 0.05 → 0.05 → 0.05 → 0.05

Numbers say: the long stroke does not run out of paint.

## Impasto
Heavy acrylic · 22 px · 14.8 s

![Impasto](Impasto.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 8 % → 8 % | 0.71 | 0.93 | 44 |
| heavy line | 10 % → 9 % | 0.70 | 0.94 | 92 |
| pressure swell | 7 % → 7 % | 0.72 | 0.94 | 53 |
| fast wave | 20 % → 13 % | 0.71 | 0.64 | 160 |
| slow wave | 21 % → 14 % | 0.71 | 0.66 | 268 |
| spiral | 30 % → 14 % | 0.71 | 0.46 | 282 |
| loop | 18 % → 14 % | 0.71 | 0.77 | 147 |
| tilted | 8 % → 8 % | 0.70 | 1.00 | 77 |
| over the wet one | 17 % → 15 % | 0.70 | 0.91 | 67 |
| long, no reload | 34 % → 14 % | 0.71 | 0.41 | 384 | quarters: 0.38 → 0.21 → 0.10 → 0.03

## Oil Round
Oil · 18 px · 17.2 s

![Oil Round](Oil-Round.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 2 % → 2 % | 0.71 | 1.00 | 36 |
| heavy line | 6 % → 6 % | 0.72 | 1.00 | 71 |
| pressure swell | 3 % → 3 % | 0.63 | 1.00 | 43 |
| fast wave | 7 % → 7 % | 0.54 | 1.00 | 176 |
| slow wave | 4 % → 4 % | 0.36 | 1.00 | 184 |
| spiral | 5 % → 5 % | 0.21 | 1.00 | 230 |
| loop | 3 % → 3 % | 0.18 | 1.00 | 131 |
| tilted | 2 % → 2 % | 0.33 | 1.00 | 67 |
| over the wet one | 3 % → 3 % | 0.33 | 1.00 | 54 |
| long, no reload | 8 % → 8 % | 0.17 | 1.00 | 333 | quarters: 0.02 → 0.02 → 0.01 → 0.01

## Palette Knife
Oil · 20 px · 17.0 s

![Palette Knife](Palette-Knife.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 8 % → 8 % | 0.67 | 1.00 | 11 |
| heavy line | 8 % → 8 % | 0.73 | 1.00 | 13 |
| pressure swell | 6 % → 6 % | 0.74 | 1.00 | 8 |
| fast wave | 17 % → 17 % | 0.49 | 1.00 | 44 |
| slow wave | 17 % → 17 % | 0.43 | 1.00 | 44 |
| spiral | 18 % → 18 % | 0.45 | 1.00 | 61 |
| loop | 16 % → 16 % | 0.58 | 1.00 | 23 |
| tilted | 5 % → 5 % | 0.72 | 1.00 | 13 |
| over the wet one | 13 % → 13 % | 0.72 | 1.00 | 11 |
| long, no reload | 17 % → 17 % | 0.47 | 1.00 | 61 | quarters: 0.29 → 0.05 → 0.00 → 0.00

Numbers say: pressure barely changes the width.

## Water
Watercolor · 20 px · 39.2 s · over bands of wet ink and oil pastel in turn (it works on paint already there: look at what it does to the bands; covered counts the bands too)

![Water](Water.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 31 % → 35 % | 0.81 | 1.15 | 27 |
| heavy line | 31 % → 35 % | 0.80 | 1.10 | 54 |
| pressure swell | 31 % → 33 % | 0.82 | 1.06 | 51 |
| fast wave | 32 % → 34 % | 0.82 | 1.07 | 107 |
| slow wave | 32 % → 34 % | 0.82 | 1.05 | 150 |
| spiral | 33 % → 34 % | 0.81 | 1.06 | 229 |
| loop | 32 % → 33 % | 0.82 | 1.03 | 89 |
| tilted | 32 % → 32 % | 0.82 | 1.00 | 56 |
| over the wet one | 32 % → 34 % | 0.82 | 1.05 | 41 |
| long, no reload | 32 % → 34 % | 0.82 | 1.06 | 258 | quarters: 0.25 → 0.34 → 0.26 → 0.34

Numbers say: pressure barely changes the width; the long stroke does not run out of paint.

## Blender
Pastel · 16 px · 38.1 s · over bands of wet ink and oil pastel in turn (it works on paint already there: look at what it does to the bands; covered counts the bands too)

![Blender](Blender.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 30 % → 33 % | 0.82 | 1.10 | 20 |
| heavy line | 31 % → 33 % | 0.82 | 1.05 | 35 |
| pressure swell | 32 % → 33 % | 0.82 | 1.03 | 21 |
| fast wave | 34 % → 34 % | 0.81 | 1.01 | 76 |
| slow wave | 34 % → 34 % | 0.81 | 1.00 | 83 |
| spiral | 36 % → 36 % | 0.79 | 1.00 | 127 |
| loop | 33 % → 33 % | 0.81 | 1.00 | 98 |
| tilted | 33 % → 33 % | 0.81 | 1.00 | 57 |
| over the wet one | 34 % → 34 % | 0.81 | 1.00 | 40 |
| long, no reload | 38 % → 38 % | 0.78 | 1.00 | 207 | quarters: 0.23 → 0.35 → 0.30 → 0.37

Numbers say: pressure barely changes the width; the long stroke does not run out of paint.

## Eraser
Eraser · 16 px · 37.4 s · over bands of wet ink and oil pastel in turn (it works on paint already there: look at what it does to the bands; covered counts the bands too)

![Eraser](Eraser.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 29 % → 32 % | 0.83 | 1.10 | 26 |
| heavy line | 31 % → 32 % | 0.83 | 1.05 | 36 |
| pressure swell | 31 % → 32 % | 0.83 | 1.03 | 26 |
| fast wave | 32 % → 32 % | 0.83 | 1.01 | 73 |
| slow wave | 32 % → 32 % | 0.83 | 1.00 | 93 |
| spiral | 32 % → 32 % | 0.83 | 1.00 | 180 |
| loop | 32 % → 32 % | 0.83 | 1.00 | 155 |
| tilted | 32 % → 32 % | 0.83 | 1.00 | 62 |
| over the wet one | 32 % → 32 % | 0.83 | 1.00 | 46 |
| long, no reload | 32 % → 32 % | 0.83 | 1.00 | 190 | quarters: 0.22 → 0.32 → 0.25 → 0.33

Numbers say: pressure barely changes the width; the long stroke does not run out of paint.

## Fan
Gouache · 30 px · 30.7 s

![Fan](Fan.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 9 % → 3 % | 0.63 | 0.37 | 30 |
| heavy line | 11 % → 4 % | 0.63 | 0.39 | 53 |
| pressure swell | 8 % → 5 % | 0.63 | 0.55 | 33 |
| fast wave | 18 % → 5 % | 0.63 | 0.26 | 106 |
| slow wave | 18 % → 5 % | 0.63 | 0.25 | 387 |
| spiral | 24 % → 5 % | 0.63 | 0.20 | 528 |
| loop | 17 % → 5 % | 0.63 | 0.29 | 110 |
| tilted | 5 % → 6 % | 0.63 | 1.05 | 50 |
| over the wet one | 16 % → 8 % | 0.63 | 0.50 | 51 |
| long, no reload | 23 % → 5 % | 0.63 | 0.22 | 305 | quarters: 0.29 → 0.07 → 0.01 → 0.00

## Sponge
Gouache · 30 px · 28.8 s

![Sponge](Sponge.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 4 % → 0 % | 0.62 | 0.12 | 48 |
| heavy line | 12 % → 2 % | 0.62 | 0.14 | 78 |
| pressure swell | 7 % → 2 % | 0.62 | 0.27 | 47 |
| fast wave | 20 % → 4 % | 0.62 | 0.19 | 128 |
| slow wave | 21 % → 4 % | 0.62 | 0.18 | 232 |
| spiral | 28 % → 4 % | 0.62 | 0.14 | 201 |
| loop | 18 % → 5 % | 0.62 | 0.29 | 109 |
| tilted | 7 % → 7 % | 0.62 | 1.04 | 113 |
| over the wet one | 16 % → 6 % | 0.62 | 0.37 | 54 |
| long, no reload | 29 % → 5 % | 0.62 | 0.17 | 324 | quarters: 0.29 → 0.13 → 0.07 → 0.04

## Ink — sumi brush
Watercolor · 22 px · 28.2 s

![Ink — sumi brush](Ink-sumi-brush.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 6 % → 7 % | 0.46 | 1.06 | 63 |
| heavy line | 10 % → 11 % | 0.38 | 1.05 | 71 |
| pressure swell | 7 % → 8 % | 0.42 | 1.04 | 53 |
| fast wave | 21 % → 21 % | 0.32 | 1.00 | 156 |
| slow wave | 19 % → 19 % | 0.37 | 1.01 | 225 |
| spiral | 28 % → 26 % | 0.30 | 0.92 | 247 |
| loop | 17 % → 18 % | 0.37 | 1.06 | 155 |
| tilted | 6 % → 7 % | 0.40 | 1.17 | 89 |
| over the wet one | 16 % → 16 % | 0.40 | 1.01 | 62 |
| long, no reload | 33 % → 29 % | 0.30 | 0.86 | 408 | quarters: 0.23 → 0.11 → 0.06 → 0.04

## Ink — wash
Watercolor · 40 px · 33.3 s

![Ink — wash](Ink-wash.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 8 % → 9 % | 0.05 | 1.26 | 79 |
| heavy line | 11 % → 13 % | 0.04 | 1.22 | 147 |
| pressure swell | 7 % → 9 % | 0.05 | 1.25 | 65 |
| fast wave | 22 % → 27 % | 0.04 | 1.21 | 209 |
| slow wave | 21 % → 26 % | 0.06 | 1.23 | 370 |
| spiral | 34 % → 41 % | 0.04 | 1.21 | 346 |
| loop | 19 % → 24 % | 0.05 | 1.25 | 185 |
| tilted | 7 % → 9 % | 0.05 | 1.21 | 136 |
| over the wet one | 18 % → 21 % | 0.05 | 1.18 | 83 |
| long, no reload | 39 % → 46 % | 0.05 | 1.19 | 587 | quarters: 0.04 → 0.03 → 0.02 → 0.01

## Ink — dry brush
Ink · 30 px · 24.9 s

![Ink — dry brush](Ink-dry-brush.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 9 % → 7 % | 0.81 | 0.78 | 88 |
| heavy line | 11 % → 8 % | 0.80 | 0.73 | 134 |
| pressure swell | 8 % → 7 % | 0.81 | 0.85 | 85 |
| fast wave | 22 % → 8 % | 0.78 | 0.38 | 244 |
| slow wave | 18 % → 6 % | 0.80 | 0.36 | 422 |
| spiral | 23 % → 8 % | 0.77 | 0.35 | 440 |
| loop | 20 % → 8 % | 0.77 | 0.41 | 287 |
| tilted | 9 % → 9 % | 0.78 | 1.01 | 167 |
| over the wet one | 19 % → 14 % | 0.78 | 0.75 | 128 |
| long, no reload | 20 % → 9 % | 0.78 | 0.42 | 507 | quarters: 0.32 → 0.01 → 0.00 → 0.00

## Ink — nib
Watercolor · 5 px · 22.8 s

![Ink — nib](Ink-nib.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 2 % → 2 % | 0.76 | 1.17 | 26 |
| heavy line | 2 % → 2 % | 0.77 | 1.16 | 26 |
| pressure swell | 1 % → 2 % | 0.78 | 1.22 | 22 |
| fast wave | 4 % → 4 % | 0.66 | 1.09 | 76 |
| slow wave | 4 % → 4 % | 0.68 | 1.11 | 72 |
| spiral | 6 % → 6 % | 0.58 | 1.08 | 128 |
| loop | 3 % → 4 % | 0.69 | 1.12 | 75 |
| tilted | 2 % → 2 % | 0.64 | 1.21 | 45 |
| over the wet one | 4 % → 4 % | 0.64 | 1.03 | 40 |
| long, no reload | 7 % → 7 % | 0.53 | 1.02 | 240 | quarters: 0.09 → 0.04 → 0.03 → 0.02

## 0.45 · Dry brush
Gouache · 34 px · 25.6 s

![0.45 · Dry brush](0-45-Dry-brush.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 11 % → 3 % | 0.67 | 0.28 | 110 |
| heavy line | 12 % → 3 % | 0.67 | 0.30 | 112 |
| pressure swell | 9 % → 4 % | 0.67 | 0.40 | 83 |
| fast wave | 20 % → 4 % | 0.67 | 0.19 | 265 |
| slow wave | 20 % → 4 % | 0.67 | 0.18 | 524 |
| spiral | 21 % → 4 % | 0.67 | 0.17 | 538 |
| loop | 21 % → 4 % | 0.67 | 0.19 | 257 |
| tilted | 9 % → 9 % | 0.67 | 0.97 | 169 |
| over the wet one | 20 % → 7 % | 0.67 | 0.33 | 182 |
| long, no reload | 20 % → 4 % | 0.67 | 0.21 | 644 | quarters: 0.38 → 0.07 → 0.00 → 0.00

Numbers say: pressure barely changes the width.

## Dry pastel
Pastel · 26 px · 10.9 s

![Dry pastel](Dry-pastel.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 5 % → 5 % | 0.36 | 1.00 | 27 |
| heavy line | 6 % → 6 % | 0.36 | 1.00 | 30 |
| pressure swell | 5 % → 5 % | 0.36 | 1.00 | 22 |
| fast wave | 15 % → 15 % | 0.36 | 1.00 | 82 |
| slow wave | 14 % → 14 % | 0.36 | 1.00 | 135 |
| spiral | 23 % → 23 % | 0.36 | 1.00 | 135 |
| loop | 11 % → 11 % | 0.36 | 1.00 | 74 |
| tilted | 5 % → 5 % | 0.37 | 1.00 | 68 |
| over the wet one | 10 % → 10 % | 0.37 | 1.00 | 31 |
| long, no reload | 26 % → 26 % | 0.36 | 1.00 | 238 | quarters: 0.11 → 0.10 → 0.10 → 0.11

Numbers say: the long stroke does not run out of paint.

## 0.45 · Charcoal
Charcoal · 18 px · 11.5 s

![0.45 · Charcoal](0-45-Charcoal.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 4 % → 4 % | 0.79 | 1.00 | 17 |
| heavy line | 4 % → 4 % | 0.79 | 1.00 | 24 |
| pressure swell | 4 % → 4 % | 0.79 | 1.00 | 16 |
| fast wave | 11 % → 11 % | 0.79 | 1.00 | 40 |
| slow wave | 11 % → 11 % | 0.78 | 1.00 | 67 |
| spiral | 20 % → 20 % | 0.79 | 1.00 | 77 |
| loop | 10 % → 10 % | 0.79 | 1.00 | 36 |
| tilted | 4 % → 4 % | 0.78 | 1.00 | 22 |
| over the wet one | 9 % → 9 % | 0.78 | 1.00 | 16 |
| long, no reload | 26 % → 26 % | 0.79 | 1.00 | 110 | quarters: 0.23 → 0.22 → 0.23 → 0.24

Numbers say: pressure barely changes the width; the long stroke does not run out of paint.

## Watercolour — wash
Watercolor · 50 px · 35.8 s

![Watercolour — wash](Watercolour-wash.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 9 % → 11 % | 0.01 | 1.22 | 94 |
| heavy line | 12 % → 14 % | 0.01 | 1.17 | 183 |
| pressure swell | 8 % → 10 % | 0.01 | 1.22 | 132 |
| fast wave | 26 % → 30 % | 0.01 | 1.18 | 447 |
| slow wave | 25 % → 29 % | 0.01 | 1.18 | 477 |
| spiral | 39 % → 46 % | 0.01 | 1.17 | 505 |
| loop | 22 % → 27 % | 0.01 | 1.21 | 273 |
| tilted | 10 % → 11 % | 0.01 | 1.18 | 147 |
| over the wet one | 22 % → 25 % | 0.01 | 1.14 | 94 |
| long, no reload | 45 % → 54 % | 0.01 | 1.18 | 609 | quarters: 0.01 → 0.01 → 0.01 → 0.00

## Watercolour — wet-in-wet
Watercolor · 44 px · 31.6 s

![Watercolour — wet-in-wet](Watercolour-wet-in-wet.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 7 % → 9 % | 0.02 | 1.26 | 121 |
| heavy line | 10 % → 12 % | 0.02 | 1.22 | 159 |
| pressure swell | 7 % → 9 % | 0.02 | 1.21 | 76 |
| fast wave | 23 % → 27 % | 0.02 | 1.17 | 191 |
| slow wave | 22 % → 26 % | 0.02 | 1.18 | 454 |
| spiral | 36 % → 43 % | 0.02 | 1.20 | 449 |
| loop | 19 % → 23 % | 0.02 | 1.20 | 169 |
| tilted | 7 % → 9 % | 0.02 | 1.19 | 111 |
| over the wet one | 17 % → 19 % | 0.02 | 1.12 | 77 |
| long, no reload | 42 % → 49 % | 0.02 | 1.18 | 487 | quarters: 0.01 → 0.01 → 0.01 → 0.01

## Watercolour — glaze
Watercolor · 38 px · 29.5 s

![Watercolour — glaze](Watercolour-glaze.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 7 % → 9 % | 0.01 | 1.28 | 64 |
| heavy line | 10 % → 13 % | 0.01 | 1.25 | 72 |
| pressure swell | 7 % → 9 % | 0.01 | 1.29 | 54 |
| fast wave | 20 % → 25 % | 0.01 | 1.24 | 169 |
| slow wave | 19 % → 24 % | 0.01 | 1.26 | 308 |
| spiral | 31 % → 37 % | 0.01 | 1.21 | 330 |
| loop | 18 % → 23 % | 0.01 | 1.27 | 147 |
| tilted | 7 % → 8 % | 0.01 | 1.20 | 103 |
| over the wet one | 17 % → 20 % | 0.01 | 1.19 | 91 |
| long, no reload | 36 % → 42 % | 0.01 | 1.17 | 565 | quarters: 0.01 → 0.00 → 0.00 → 0.00

## Watercolour — granulating
Watercolor · 44 px · 31.6 s

![Watercolour — granulating](Watercolour-granulating.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 8 % → 10 % | 0.02 | 1.18 | 68 |
| heavy line | 12 % → 14 % | 0.01 | 1.15 | 88 |
| pressure swell | 8 % → 10 % | 0.02 | 1.18 | 58 |
| fast wave | 25 % → 29 % | 0.01 | 1.15 | 200 |
| slow wave | 24 % → 27 % | 0.02 | 1.16 | 331 |
| spiral | 39 % → 44 % | 0.01 | 1.15 | 353 |
| loop | 22 % → 25 % | 0.01 | 1.17 | 206 |
| tilted | 9 % → 11 % | 0.02 | 1.15 | 117 |
| over the wet one | 21 % → 23 % | 0.02 | 1.11 | 89 |
| long, no reload | 45 % → 52 % | 0.01 | 1.15 | 548 | quarters: 0.01 → 0.01 → 0.01 → 0.01

## Watercolour — dry brush
Watercolor · 36 px · 27.1 s

![Watercolour — dry brush](Watercolour-dry-brush.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 7 % → 8 % | 0.05 | 1.07 | 93 |
| heavy line | 11 % → 12 % | 0.04 | 1.03 | 107 |
| pressure swell | 9 % → 10 % | 0.05 | 1.07 | 70 |
| fast wave | 21 % → 14 % | 0.04 | 0.68 | 261 |
| slow wave | 19 % → 13 % | 0.04 | 0.70 | 408 |
| spiral | 24 % → 15 % | 0.04 | 0.61 | 486 |
| loop | 17 % → 14 % | 0.04 | 0.85 | 237 |
| tilted | 7 % → 8 % | 0.05 | 1.19 | 116 |
| over the wet one | 17 % → 17 % | 0.05 | 0.99 | 106 |
| long, no reload | 22 % → 15 % | 0.04 | 0.68 | 791 | quarters: 0.02 → 0.00 → 0.00 → 0.00

## Gouache
Gouache · 30 px · 26.3 s

![Gouache](Gouache.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 8 % → 6 % | 0.14 | 0.67 | 68 |
| heavy line | 13 % → 6 % | 0.14 | 0.47 | 104 |
| pressure swell | 10 % → 6 % | 0.14 | 0.61 | 82 |
| fast wave | 27 % → 7 % | 0.14 | 0.27 | 230 |
| slow wave | 27 % → 7 % | 0.14 | 0.27 | 439 |
| spiral | 37 % → 8 % | 0.14 | 0.22 | 431 |
| loop | 22 % → 8 % | 0.14 | 0.36 | 163 |
| tilted | 9 % → 9 % | 0.14 | 1.02 | 87 |
| over the wet one | 20 % → 13 % | 0.14 | 0.67 | 74 |
| long, no reload | 38 % → 10 % | 0.14 | 0.25 | 497 | quarters: 0.07 → 0.04 → 0.01 → 0.01

## Oil — alla prima
Oil · 30 px · 20.0 s

![Oil — alla prima](Oil-alla-prima.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 9 % → 9 % | 0.50 | 1.00 | 80 |
| heavy line | 10 % → 10 % | 0.50 | 1.00 | 79 |
| pressure swell | 8 % → 8 % | 0.52 | 1.00 | 62 |
| fast wave | 24 % → 24 % | 0.49 | 1.00 | 204 |
| slow wave | 25 % → 25 % | 0.50 | 1.00 | 353 |
| spiral | 38 % → 38 % | 0.44 | 1.00 | 388 |
| loop | 21 % → 21 % | 0.50 | 1.00 | 178 |
| tilted | 11 % → 11 % | 0.50 | 1.00 | 98 |
| over the wet one | 20 % → 20 % | 0.50 | 1.00 | 91 |
| long, no reload | 46 % → 46 % | 0.40 | 1.00 | 652 | quarters: 0.31 → 0.24 → 0.17 → 0.10

Numbers say: pressure barely changes the width.

## Oil — impasto
Oil · 34 px · 20.3 s

![Oil — impasto](Oil-impasto.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 11 % → 11 % | 0.24 | 1.00 | 91 |
| heavy line | 12 % → 12 % | 0.23 | 1.00 | 101 |
| pressure swell | 9 % → 9 % | 0.25 | 1.00 | 78 |
| fast wave | 29 % → 29 % | 0.21 | 1.00 | 244 |
| slow wave | 29 % → 29 % | 0.21 | 1.00 | 614 |
| spiral | 48 % → 48 % | 0.17 | 1.00 | 579 |
| loop | 25 % → 25 % | 0.21 | 1.00 | 221 |
| tilted | 12 % → 12 % | 0.24 | 1.00 | 125 |
| over the wet one | 23 % → 23 % | 0.24 | 1.00 | 98 |
| long, no reload | 55 % → 55 % | 0.15 | 1.00 | 1034 | quarters: 0.16 → 0.11 → 0.06 → 0.02

Numbers say: pressure barely changes the width.

## Oil — glaze
Oil · 40 px · 17.0 s

![Oil — glaze](Oil-glaze.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 10 % → 10 % | 0.49 | 1.00 | 117 |
| heavy line | 14 % → 14 % | 0.48 | 1.00 | 120 |
| pressure swell | 10 % → 10 % | 0.49 | 1.00 | 77 |
| fast wave | 28 % → 28 % | 0.46 | 1.00 | 248 |
| slow wave | 30 % → 30 % | 0.46 | 1.00 | 417 |
| spiral | 42 % → 42 % | 0.44 | 1.00 | 688 |
| loop | 24 % → 24 % | 0.47 | 1.00 | 359 |
| tilted | 11 % → 11 % | 0.47 | 1.00 | 228 |
| over the wet one | 23 % → 23 % | 0.47 | 1.00 | 160 |
| long, no reload | 47 % → 47 % | 0.43 | 1.00 | 604 | quarters: 0.33 → 0.24 → 0.18 → 0.14

## Oil — scumble
Oil · 36 px · 19.5 s

![Oil — scumble](Oil-scumble.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 11 % → 11 % | 0.06 | 1.00 | 119 |
| heavy line | 12 % → 12 % | 0.05 | 1.00 | 118 |
| pressure swell | 9 % → 9 % | 0.06 | 1.00 | 82 |
| fast wave | 18 % → 18 % | 0.04 | 1.00 | 301 |
| slow wave | 20 % → 20 % | 0.04 | 1.00 | 516 |
| spiral | 19 % → 19 % | 0.03 | 1.00 | 511 |
| loop | 22 % → 22 % | 0.04 | 1.00 | 263 |
| tilted | 10 % → 10 % | 0.05 | 1.00 | 134 |
| over the wet one | 21 % → 21 % | 0.05 | 1.00 | 128 |
| long, no reload | 18 % → 18 % | 0.04 | 1.00 | 776 | quarters: 0.03 → 0.00 → 0.00 → 0.00

Numbers say: pressure barely changes the width.

## Acrylic — heavy body
Heavy acrylic · 30 px · 15.0 s

![Acrylic — heavy body](Acrylic-heavy-body.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 10 % → 9 % | 0.51 | 0.93 | 83 |
| heavy line | 11 % → 10 % | 0.51 | 0.93 | 81 |
| pressure swell | 8 % → 8 % | 0.52 | 0.94 | 60 |
| fast wave | 24 % → 14 % | 0.51 | 0.58 | 208 |
| slow wave | 25 % → 15 % | 0.51 | 0.59 | 363 |
| spiral | 37 % → 15 % | 0.51 | 0.40 | 383 |
| loop | 22 % → 16 % | 0.51 | 0.73 | 187 |
| tilted | 10 % → 10 % | 0.51 | 1.00 | 113 |
| over the wet one | 20 % → 17 % | 0.51 | 0.88 | 91 |
| long, no reload | 39 % → 15 % | 0.51 | 0.40 | 507 | quarters: 0.30 → 0.20 → 0.10 → 0.02

Numbers say: pressure barely changes the width.

## Acrylic — fluid
Watercolor · 36 px · 29.0 s

![Acrylic — fluid](Acrylic-fluid.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 9 % → 10 % | 0.06 | 1.11 | 61 |
| heavy line | 13 % → 14 % | 0.05 | 1.07 | 74 |
| pressure swell | 9 % → 10 % | 0.07 | 1.09 | 52 |
| fast wave | 26 % → 28 % | 0.05 | 1.07 | 186 |
| slow wave | 24 % → 26 % | 0.07 | 1.08 | 300 |
| spiral | 39 % → 41 % | 0.05 | 1.06 | 300 |
| loop | 22 % → 25 % | 0.06 | 1.11 | 157 |
| tilted | 8 % → 9 % | 0.07 | 1.17 | 141 |
| over the wet one | 21 % → 22 % | 0.07 | 1.05 | 72 |
| long, no reload | 44 % → 47 % | 0.05 | 1.06 | 456 | quarters: 0.05 → 0.03 → 0.02 → 0.01

## Acrylic — palette knife
Heavy acrylic · 42 px · 18.9 s

![Acrylic — palette knife](Acrylic-palette-knife.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 15 % → 15 % | 0.06 | 0.98 | 27 |
| heavy line | 15 % → 15 % | 0.05 | 0.98 | 21 |
| pressure swell | 12 % → 12 % | 0.06 | 0.99 | 10 |
| fast wave | 37 % → 20 % | 0.06 | 0.54 | 48 |
| slow wave | 37 % → 21 % | 0.06 | 0.56 | 85 |
| spiral | 48 % → 19 % | 0.06 | 0.38 | 88 |
| loop | 32 % → 24 % | 0.05 | 0.75 | 68 |
| tilted | 12 % → 12 % | 0.05 | 1.00 | 30 |
| over the wet one | 26 % → 26 % | 0.05 | 0.98 | 30 |
| long, no reload | 55 % → 20 % | 0.06 | 0.36 | 112 | quarters: 0.04 → 0.02 → 0.00 → 0.00

Numbers say: pressure barely changes the width.

## Finger on oil
Oil · 30 px · 14.1 s

![Finger on oil](Finger-on-oil.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 8 % → 8 % | 0.34 | 1.00 | 43 |
| heavy line | 12 % → 12 % | 0.30 | 1.00 | 57 |
| pressure swell | 8 % → 8 % | 0.35 | 1.00 | 37 |
| fast wave | 16 % → 16 % | 0.22 | 1.00 | 122 |
| slow wave | 17 % → 17 % | 0.23 | 1.00 | 289 |
| spiral | 18 % → 18 % | 0.22 | 1.00 | 273 |
| loop | 18 % → 18 % | 0.23 | 1.00 | 127 |
| tilted | 9 % → 9 % | 0.31 | 1.00 | 70 |
| over the wet one | 18 % → 18 % | 0.31 | 1.00 | 45 |
| long, no reload | 15 % → 15 % | 0.23 | 1.00 | 297 | quarters: 0.13 → 0.01 → 0.00 → 0.00

## Palette knife — oil
Oil · 44 px · 19.0 s

![Palette knife — oil](Palette-knife-oil.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 16 % → 16 % | 0.10 | 1.00 | 25 |
| heavy line | 16 % → 16 % | 0.09 | 1.00 | 22 |
| pressure swell | 12 % → 12 % | 0.10 | 1.00 | 13 |
| fast wave | 39 % → 39 % | 0.07 | 1.00 | 73 |
| slow wave | 39 % → 39 % | 0.07 | 1.00 | 104 |
| spiral | 54 % → 54 % | 0.05 | 1.00 | 116 |
| loop | 34 % → 34 % | 0.08 | 1.00 | 48 |
| tilted | 13 % → 13 % | 0.09 | 1.00 | 20 |
| over the wet one | 28 % → 28 % | 0.09 | 1.00 | 22 |
| long, no reload | 65 % → 65 % | 0.05 | 1.00 | 130 | quarters: 0.08 → 0.04 → 0.01 → 0.00

Numbers say: pressure barely changes the width.

## 0.45 · Sponge
Watercolor · 46 px · 25.1 s

![0.45 · Sponge](0-45-Sponge.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 11 % → 0 % | 0.00 | 0.00 | 80 |
| heavy line | 13 % → 0 % | 0.01 | 0.00 | 75 |
| pressure swell | 9 % → 1 % | 0.02 | 0.14 | 51 |
| fast wave | 23 % → 2 % | 0.01 | 0.08 | 155 |
| slow wave | 26 % → 8 % | 0.02 | 0.30 | 267 |
| spiral | 34 % → 11 % | 0.02 | 0.32 | 245 |
| loop | 22 % → 4 % | 0.02 | 0.19 | 130 |
| tilted | 9 % → 10 % | 0.04 | 1.19 | 94 |
| over the wet one | 22 % → 10 % | 0.04 | 0.44 | 60 |
| long, no reload | 41 % → 19 % | 0.02 | 0.47 | 388 | quarters: 0.01 → 0.01 → 0.01 → 0.01

## 0.45 · Eraser
Eraser · 30 px · 34.5 s · over bands of wet ink and oil pastel in turn (it works on paint already there: look at what it does to the bands; covered counts the bands too)

![0.45 · Eraser](0-45-Eraser.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 29 % → 32 % | 0.83 | 1.10 | 42 |
| heavy line | 30 % → 32 % | 0.83 | 1.05 | 48 |
| pressure swell | 31 % → 32 % | 0.83 | 1.03 | 36 |
| fast wave | 31 % → 31 % | 0.80 | 1.02 | 127 |
| slow wave | 28 % → 28 % | 0.82 | 1.00 | 205 |
| spiral | 28 % → 28 % | 0.80 | 1.00 | 211 |
| loop | 29 % → 29 % | 0.81 | 1.00 | 154 |
| tilted | 31 % → 31 % | 0.82 | 1.00 | 59 |
| over the wet one | 30 % → 30 % | 0.82 | 1.00 | 50 |
| long, no reload | 23 % → 23 % | 0.79 | 1.00 | 306 | quarters: 0.15 → 0.21 → 0.18 → 0.22

Numbers say: pressure barely changes the width; the long stroke does not run out of paint.

## Lift wet paint
Eraser · 30 px · 34.3 s · over bands of wet ink and oil pastel in turn (it works on paint already there: look at what it does to the bands; covered counts the bands too)

![Lift wet paint](Lift-wet-paint.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 29 % → 32 % | 0.83 | 1.10 | 31 |
| heavy line | 31 % → 32 % | 0.83 | 1.05 | 42 |
| pressure swell | 31 % → 32 % | 0.83 | 1.03 | 31 |
| fast wave | 32 % → 32 % | 0.83 | 1.01 | 97 |
| slow wave | 32 % → 32 % | 0.83 | 1.00 | 262 |
| spiral | 32 % → 32 % | 0.83 | 1.00 | 162 |
| loop | 32 % → 32 % | 0.83 | 1.00 | 159 |
| tilted | 32 % → 32 % | 0.83 | 1.00 | 93 |
| over the wet one | 32 % → 32 % | 0.83 | 1.00 | 63 |
| long, no reload | 32 % → 32 % | 0.83 | 1.00 | 252 | quarters: 0.22 → 0.32 → 0.25 → 0.33

Numbers say: pressure barely changes the width; the long stroke does not run out of paint.

## Sgraffito
Eraser · 10 px · 34.3 s · over bands of wet ink and oil pastel in turn (it works on paint already there: look at what it does to the bands; covered counts the bands too)

![Sgraffito](Sgraffito.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 29 % → 32 % | 0.82 | 1.08 | 20 |
| heavy line | 31 % → 32 % | 0.82 | 1.04 | 11 |
| pressure swell | 31 % → 32 % | 0.82 | 1.02 | 6 |
| fast wave | 32 % → 31 % | 0.82 | 0.98 | 21 |
| slow wave | 32 % → 31 % | 0.82 | 0.97 | 20 |
| spiral | 32 % → 31 % | 0.82 | 0.96 | 39 |
| loop | 32 % → 32 % | 0.82 | 0.99 | 20 |
| tilted | 32 % → 32 % | 0.82 | 0.99 | 9 |
| over the wet one | 32 % → 32 % | 0.82 | 0.99 | 13 |
| long, no reload | 32 % → 32 % | 0.82 | 1.00 | 48 | quarters: 0.21 → 0.31 → 0.25 → 0.32

Numbers say: pressure barely changes the width; the long stroke does not run out of paint.

## Brush Artist · Sumi — wetter
Watercolor · 24 px · 27.2 s

![Brush Artist · Sumi — wetter](Brush-Artist-Sumi-wetter.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 5 % → 6 % | 0.21 | 1.11 | 43 |
| heavy line | 11 % → 12 % | 0.13 | 1.13 | 77 |
| pressure swell | 7 % → 8 % | 0.16 | 1.13 | 44 |
| fast wave | 21 % → 24 % | 0.12 | 1.15 | 153 |
| slow wave | 19 % → 22 % | 0.15 | 1.14 | 234 |
| spiral | 29 % → 32 % | 0.12 | 1.13 | 250 |
| loop | 17 % → 19 % | 0.15 | 1.15 | 124 |
| tilted | 6 % → 7 % | 0.16 | 1.17 | 67 |
| over the wet one | 16 % → 17 % | 0.16 | 1.07 | 60 |
| long, no reload | 33 % → 37 % | 0.12 | 1.12 | 377 | quarters: 0.10 → 0.05 → 0.03 → 0.02

