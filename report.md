![All brushes](contact.png)

# Brush Lab — 143 brushes · Nov 3, 2026 at 12:14 PM

Every sheet: 1500 × 600, ten strokes in a 5 × 2 grid — 1. light line · 2. heavy line · 3. pressure swell · 4. fast wave · 5. slow wave · 6. spiral · 7. loop · 8. tilted · 9. over the wet one · 10. long, no reload (cell 8 holds «tilted» and «over the wet one» crossed). The CPU reference of Mamay's paint engine; the wet layer settles 20 s at the end.

Columns: **covered** = share of the cell with paint right after the stroke → after settling; **dark** = mean darkness of the painted pixels above the paper's own grain (0 = paper, 1 = black); **spread** = how far wet paint went beyond the stroke (1.0 = stayed); **ms** = the stroke on the CPU; long stroke: paint in each quarter of its length (it should run out: wet → streaks → dry tail).

## Ink Line
Ink · 12 px · 34.9 s

![Ink Line](Ink-Line.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 1 % → 4 % | 0.55 | 2.44 | 51 |
| heavy line | 5 % → 6 % | 0.68 | 1.13 | 121 |
| pressure swell | 3 % → 4 % | 0.64 | 1.40 | 56 |
| fast wave | 10 % → 11 % | 0.59 | 1.11 | 172 |
| slow wave | 8 % → 10 % | 0.57 | 1.16 | 143 |
| spiral | 14 % → 15 % | 0.50 | 1.07 | 393 |
| loop | 8 % → 9 % | 0.61 | 1.16 | 148 |
| tilted | 5 % → 5 % | 0.65 | 1.05 | 72 |
| over the wet one | 10 % → 11 % | 0.65 | 1.15 | 65 |
| long, no reload | 18 % → 17 % | 0.47 | 0.96 | 520 | quarters: 0.22 → 0.09 → 0.04 → 0.02

Numbers say: wet paint spreads well beyond the stroke.

## Dense Ink
Ink · 14 px · 36.1 s

![Dense Ink](Dense-Ink.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 5 % → 7 % | 0.72 | 1.26 | 83 |
| heavy line | 7 % → 7 % | 0.73 | 1.09 | 115 |
| pressure swell | 5 % → 6 % | 0.72 | 1.17 | 62 |
| fast wave | 13 % → 13 % | 0.69 | 1.01 | 171 |
| slow wave | 12 % → 12 % | 0.67 | 1.04 | 203 |
| spiral | 18 % → 15 % | 0.65 | 0.80 | 348 |
| loop | 11 % → 12 % | 0.69 | 1.08 | 162 |
| tilted | 5 % → 6 % | 0.72 | 1.07 | 89 |
| over the wet one | 12 % → 13 % | 0.72 | 1.11 | 92 |
| long, no reload | 23 % → 15 % | 0.64 | 0.66 | 695 | quarters: 0.30 → 0.12 → 0.04 → 0.02

## Transparent Wash
Watercolor · 22 px · 36.9 s

![Transparent Wash](Transparent-Wash.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 2 % → 5 % | 0.27 | 2.25 | 49 |
| heavy line | 7 % → 9 % | 0.27 | 1.22 | 93 |
| pressure swell | 4 % → 6 % | 0.28 | 1.54 | 55 |
| fast wave | 14 % → 16 % | 0.20 | 1.17 | 166 |
| slow wave | 12 % → 15 % | 0.21 | 1.28 | 218 |
| spiral | 18 % → 22 % | 0.16 | 1.23 | 271 |
| loop | 11 % → 13 % | 0.22 | 1.20 | 145 |
| tilted | 8 % → 8 % | 0.24 | 1.06 | 89 |
| over the wet one | 13 % → 16 % | 0.24 | 1.18 | 60 |
| long, no reload | 26 % → 32 % | 0.13 | 1.22 | 566 | quarters: 0.11 → 0.04 → 0.02 → 0.01

Numbers say: wet paint spreads well beyond the stroke.

## Dry Brush
Gouache · 24 px · 27.5 s

![Dry Brush](Dry-Brush.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 5 % → 0 % | 0.65 | 0.09 | 89 |
| heavy line | 6 % → 0 % | 0.65 | 0.02 | 134 |
| pressure swell | 5 % → 0 % | 0.65 | 0.08 | 76 |
| fast wave | 6 % → 1 % | 0.65 | 0.08 | 203 |
| slow wave | 7 % → 0 % | 0.65 | 0.06 | 335 |
| spiral | 7 % → 0 % | 0.65 | 0.07 | 328 |
| loop | 10 % → 0 % | 0.65 | 0.04 | 177 |
| tilted | 4 % → 3 % | 0.65 | 0.88 | 108 |
| over the wet one | 9 % → 1 % | 0.65 | 0.12 | 96 |
| long, no reload | 6 % → 1 % | 0.65 | 0.14 | 536 | quarters: 0.12 → 0.00 → 0.00 → 0.00

## Wax Crayon
Wax · 8 px · 13.3 s

![Wax Crayon](Wax-Crayon.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 1 % → 1 % | 0.71 | 1.00 | 19 |
| heavy line | 1 % → 1 % | 0.69 | 1.00 | 28 |
| pressure swell | 1 % → 1 % | 0.70 | 1.00 | 20 |
| fast wave | 3 % → 3 % | 0.69 | 1.00 | 59 |
| slow wave | 3 % → 3 % | 0.70 | 1.00 | 60 |
| spiral | 5 % → 5 % | 0.70 | 1.00 | 102 |
| loop | 3 % → 3 % | 0.70 | 1.00 | 54 |
| tilted | 2 % → 2 % | 0.68 | 1.00 | 33 |
| over the wet one | 3 % → 3 % | 0.68 | 1.00 | 24 |
| long, no reload | 7 % → 7 % | 0.70 | 1.00 | 136 | quarters: 0.06 → 0.06 → 0.06 → 0.06

Numbers say: the long stroke does not run out of paint.

## Oil Pastel
Wax · 12 px · 13.4 s

![Oil Pastel](Oil-Pastel.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 1 % → 1 % | 0.68 | 1.00 | 25 |
| heavy line | 2 % → 2 % | 0.68 | 1.00 | 43 |
| pressure swell | 2 % → 2 % | 0.69 | 1.00 | 25 |
| fast wave | 5 % → 5 % | 0.68 | 1.00 | 104 |
| slow wave | 5 % → 5 % | 0.68 | 1.00 | 79 |
| spiral | 8 % → 8 % | 0.68 | 1.00 | 129 |
| loop | 4 % → 4 % | 0.68 | 1.00 | 61 |
| tilted | 2 % → 2 % | 0.68 | 1.00 | 50 |
| over the wet one | 5 % → 5 % | 0.68 | 1.00 | 31 |
| long, no reload | 13 % → 13 % | 0.68 | 1.00 | 205 | quarters: 0.10 → 0.09 → 0.10 → 0.10

Numbers say: the long stroke does not run out of paint.

## Charcoal
Charcoal · 5 px · 13.4 s

![Charcoal](Charcoal.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 1 % → 1 % | 0.74 | 1.00 | 29 |
| heavy line | 1 % → 1 % | 0.74 | 1.00 | 14 |
| pressure swell | 1 % → 1 % | 0.74 | 1.00 | 16 |
| fast wave | 2 % → 2 % | 0.73 | 1.00 | 37 |
| slow wave | 2 % → 2 % | 0.74 | 1.00 | 33 |
| spiral | 4 % → 4 % | 0.74 | 1.00 | 78 |
| loop | 2 % → 2 % | 0.74 | 1.00 | 28 |
| tilted | 2 % → 2 % | 0.72 | 1.00 | 32 |
| over the wet one | 2 % → 2 % | 0.72 | 1.00 | 23 |
| long, no reload | 6 % → 6 % | 0.73 | 1.00 | 128 | quarters: 0.05 → 0.05 → 0.05 → 0.05

Numbers say: the long stroke does not run out of paint.

## Impasto
Heavy acrylic · 22 px · 20.3 s

![Impasto](Impasto.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 8 % → 8 % | 0.71 | 0.93 | 70 |
| heavy line | 10 % → 9 % | 0.70 | 0.94 | 117 |
| pressure swell | 7 % → 7 % | 0.72 | 0.94 | 70 |
| fast wave | 20 % → 13 % | 0.71 | 0.64 | 243 |
| slow wave | 21 % → 14 % | 0.71 | 0.66 | 390 |
| spiral | 30 % → 14 % | 0.71 | 0.46 | 364 |
| loop | 18 % → 14 % | 0.71 | 0.77 | 206 |
| tilted | 8 % → 8 % | 0.70 | 1.00 | 150 |
| over the wet one | 17 % → 15 % | 0.70 | 0.91 | 95 |
| long, no reload | 34 % → 14 % | 0.71 | 0.41 | 483 | quarters: 0.38 → 0.21 → 0.10 → 0.03

## Oil Round
Oil · 18 px · 24.2 s

![Oil Round](Oil-Round.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 2 % → 2 % | 0.71 | 1.00 | 62 |
| heavy line | 6 % → 6 % | 0.72 | 1.00 | 129 |
| pressure swell | 3 % → 3 % | 0.63 | 1.00 | 57 |
| fast wave | 7 % → 7 % | 0.54 | 1.00 | 182 |
| slow wave | 4 % → 4 % | 0.36 | 1.00 | 236 |
| spiral | 5 % → 5 % | 0.21 | 1.00 | 301 |
| loop | 3 % → 3 % | 0.18 | 1.00 | 163 |
| tilted | 2 % → 2 % | 0.33 | 1.00 | 112 |
| over the wet one | 3 % → 3 % | 0.33 | 1.00 | 86 |
| long, no reload | 8 % → 8 % | 0.17 | 1.00 | 475 | quarters: 0.02 → 0.02 → 0.01 → 0.01

## Palette Knife
Oil · 20 px · 23.9 s

![Palette Knife](Palette-Knife.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 8 % → 8 % | 0.67 | 1.00 | 37 |
| heavy line | 8 % → 8 % | 0.73 | 1.00 | 20 |
| pressure swell | 6 % → 6 % | 0.74 | 1.00 | 6 |
| fast wave | 17 % → 17 % | 0.49 | 1.00 | 30 |
| slow wave | 17 % → 17 % | 0.43 | 1.00 | 51 |
| spiral | 18 % → 18 % | 0.45 | 1.00 | 65 |
| loop | 16 % → 16 % | 0.58 | 1.00 | 37 |
| tilted | 5 % → 5 % | 0.72 | 1.00 | 11 |
| over the wet one | 13 % → 13 % | 0.72 | 1.00 | 15 |
| long, no reload | 17 % → 17 % | 0.47 | 1.00 | 82 | quarters: 0.29 → 0.05 → 0.00 → 0.00

Numbers say: pressure barely changes the width.

## Water
Watercolor · 20 px · 46.9 s · over bands of wet oil paint and oil pastel in turn (it works on paint already there: look at what it does to the bands; covered counts the bands too)

![Water](Water.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 25 % → 26 % | 0.78 | 1.07 | 37 |
| heavy line | 23 % → 24 % | 0.80 | 1.04 | 71 |
| pressure swell | 23 % → 24 % | 0.80 | 1.03 | 44 |
| fast wave | 23 % → 25 % | 0.80 | 1.07 | 139 |
| slow wave | 23 % → 25 % | 0.80 | 1.06 | 194 |
| spiral | 23 % → 25 % | 0.79 | 1.08 | 203 |
| loop | 23 % → 24 % | 0.80 | 1.03 | 102 |
| tilted | 23 % → 23 % | 0.80 | 1.00 | 223 |
| over the wet one | 23 % → 25 % | 0.80 | 1.07 | 115 |
| long, no reload | 23 % → 25 % | 0.80 | 1.08 | 327 | quarters: 0.21 → 0.26 → 0.17 → 0.25

Numbers say: pressure barely changes the width; the long stroke does not run out of paint.

## Blender
Pastel · 16 px · 26.8 s · over bands of wet oil paint and oil pastel in turn (it works on paint already there: look at what it does to the bands; covered counts the bands too)

![Blender](Blender.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 24 % → 24 % | 0.80 | 1.00 | 36 |
| heavy line | 24 % → 24 % | 0.80 | 1.00 | 56 |
| pressure swell | 24 % → 24 % | 0.80 | 1.00 | 31 |
| fast wave | 25 % → 25 % | 0.78 | 1.00 | 95 |
| slow wave | 25 % → 25 % | 0.78 | 1.00 | 116 |
| spiral | 27 % → 27 % | 0.76 | 1.00 | 160 |
| loop | 25 % → 25 % | 0.79 | 1.00 | 126 |
| tilted | 24 % → 24 % | 0.78 | 1.00 | 56 |
| over the wet one | 25 % → 25 % | 0.78 | 1.00 | 55 |
| long, no reload | 29 % → 29 % | 0.74 | 1.00 | 298 | quarters: 0.19 → 0.26 → 0.21 → 0.28

Numbers say: pressure barely changes the width; the long stroke does not run out of paint.

## Eraser
Eraser · 16 px · 26.3 s · over bands of wet oil paint and oil pastel in turn (it works on paint already there: look at what it does to the bands; covered counts the bands too)

![Eraser](Eraser.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 23 % → 23 % | 0.81 | 1.00 | 34 |
| heavy line | 23 % → 23 % | 0.81 | 1.00 | 39 |
| pressure swell | 23 % → 23 % | 0.81 | 1.00 | 29 |
| fast wave | 22 % → 22 % | 0.81 | 1.00 | 101 |
| slow wave | 22 % → 22 % | 0.81 | 1.00 | 117 |
| spiral | 21 % → 21 % | 0.81 | 1.00 | 144 |
| loop | 22 % → 22 % | 0.81 | 1.00 | 114 |
| tilted | 23 % → 23 % | 0.81 | 1.00 | 61 |
| over the wet one | 22 % → 22 % | 0.81 | 1.00 | 49 |
| long, no reload | 19 % → 19 % | 0.81 | 1.00 | 337 | quarters: 0.15 → 0.19 → 0.14 → 0.20

Numbers say: pressure barely changes the width; the long stroke does not run out of paint.

## Fan
Gouache · 30 px · 37.9 s

![Fan](Fan.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 9 % → 3 % | 0.63 | 0.37 | 60 |
| heavy line | 11 % → 4 % | 0.63 | 0.39 | 70 |
| pressure swell | 8 % → 5 % | 0.63 | 0.55 | 38 |
| fast wave | 18 % → 5 % | 0.63 | 0.26 | 155 |
| slow wave | 18 % → 5 % | 0.63 | 0.25 | 210 |
| spiral | 24 % → 5 % | 0.63 | 0.20 | 235 |
| loop | 17 % → 5 % | 0.63 | 0.29 | 230 |
| tilted | 5 % → 6 % | 0.63 | 1.05 | 74 |
| over the wet one | 16 % → 8 % | 0.63 | 0.50 | 63 |
| long, no reload | 23 % → 5 % | 0.63 | 0.22 | 418 | quarters: 0.29 → 0.07 → 0.01 → 0.00

## Sponge
Gouache · 30 px · 38.2 s

![Sponge](Sponge.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 4 % → 0 % | 0.62 | 0.12 | 59 |
| heavy line | 12 % → 2 % | 0.62 | 0.14 | 103 |
| pressure swell | 7 % → 2 % | 0.62 | 0.27 | 77 |
| fast wave | 20 % → 4 % | 0.62 | 0.19 | 155 |
| slow wave | 21 % → 4 % | 0.62 | 0.18 | 339 |
| spiral | 28 % → 4 % | 0.62 | 0.14 | 327 |
| loop | 18 % → 5 % | 0.62 | 0.29 | 150 |
| tilted | 7 % → 7 % | 0.62 | 1.04 | 144 |
| over the wet one | 16 % → 6 % | 0.62 | 0.37 | 70 |
| long, no reload | 29 % → 5 % | 0.62 | 0.17 | 413 | quarters: 0.29 → 0.13 → 0.07 → 0.04

## Ink — sumi brush
Watercolor · 22 px · 38.2 s

![Ink — sumi brush](Ink-sumi-brush.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 6 % → 7 % | 0.46 | 1.06 | 71 |
| heavy line | 10 % → 11 % | 0.38 | 1.05 | 94 |
| pressure swell | 7 % → 8 % | 0.42 | 1.04 | 58 |
| fast wave | 21 % → 21 % | 0.32 | 1.00 | 282 |
| slow wave | 19 % → 19 % | 0.37 | 1.01 | 403 |
| spiral | 28 % → 26 % | 0.30 | 0.92 | 375 |
| loop | 17 % → 18 % | 0.37 | 1.06 | 203 |
| tilted | 6 % → 7 % | 0.40 | 1.17 | 85 |
| over the wet one | 16 % → 16 % | 0.40 | 1.01 | 93 |
| long, no reload | 33 % → 29 % | 0.30 | 0.86 | 501 | quarters: 0.23 → 0.11 → 0.06 → 0.04

## Ink — wash
Watercolor · 40 px · 45.6 s

![Ink — wash](Ink-wash.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 8 % → 9 % | 0.05 | 1.26 | 97 |
| heavy line | 11 % → 13 % | 0.04 | 1.22 | 107 |
| pressure swell | 7 % → 9 % | 0.05 | 1.25 | 69 |
| fast wave | 22 % → 27 % | 0.04 | 1.21 | 273 |
| slow wave | 21 % → 26 % | 0.06 | 1.23 | 628 |
| spiral | 34 % → 41 % | 0.04 | 1.21 | 976 |
| loop | 19 % → 24 % | 0.05 | 1.25 | 242 |
| tilted | 7 % → 9 % | 0.05 | 1.21 | 137 |
| over the wet one | 18 % → 21 % | 0.05 | 1.18 | 98 |
| long, no reload | 39 % → 46 % | 0.05 | 1.19 | 629 | quarters: 0.04 → 0.03 → 0.02 → 0.01

## Ink — dry brush
Ink · 30 px · 33.5 s

![Ink — dry brush](Ink-dry-brush.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 9 % → 7 % | 0.81 | 0.78 | 101 |
| heavy line | 11 % → 8 % | 0.80 | 0.73 | 132 |
| pressure swell | 8 % → 7 % | 0.81 | 0.85 | 81 |
| fast wave | 22 % → 8 % | 0.78 | 0.38 | 497 |
| slow wave | 18 % → 6 % | 0.80 | 0.36 | 818 |
| spiral | 23 % → 8 % | 0.77 | 0.35 | 797 |
| loop | 20 % → 8 % | 0.77 | 0.41 | 253 |
| tilted | 9 % → 9 % | 0.78 | 1.01 | 136 |
| over the wet one | 19 % → 14 % | 0.78 | 0.75 | 119 |
| long, no reload | 20 % → 9 % | 0.78 | 0.42 | 675 | quarters: 0.32 → 0.01 → 0.00 → 0.00

## Ink — nib
Watercolor · 5 px · 30.4 s

![Ink — nib](Ink-nib.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 2 % → 2 % | 0.76 | 1.17 | 56 |
| heavy line | 2 % → 2 % | 0.77 | 1.16 | 47 |
| pressure swell | 1 % → 2 % | 0.78 | 1.22 | 47 |
| fast wave | 4 % → 4 % | 0.66 | 1.09 | 103 |
| slow wave | 4 % → 4 % | 0.68 | 1.11 | 87 |
| spiral | 6 % → 6 % | 0.58 | 1.08 | 157 |
| loop | 3 % → 4 % | 0.69 | 1.12 | 75 |
| tilted | 2 % → 2 % | 0.64 | 1.21 | 40 |
| over the wet one | 4 % → 4 % | 0.64 | 1.03 | 49 |
| long, no reload | 7 % → 7 % | 0.53 | 1.02 | 197 | quarters: 0.09 → 0.04 → 0.03 → 0.02

## 0.45 · Dry brush
Gouache · 34 px · 33.9 s

![0.45 · Dry brush](0-45-Dry-brush.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 11 % → 3 % | 0.67 | 0.28 | 192 |
| heavy line | 12 % → 3 % | 0.67 | 0.30 | 215 |
| pressure swell | 9 % → 4 % | 0.67 | 0.40 | 181 |
| fast wave | 20 % → 4 % | 0.67 | 0.19 | 438 |
| slow wave | 20 % → 4 % | 0.67 | 0.18 | 828 |
| spiral | 21 % → 4 % | 0.67 | 0.17 | 645 |
| loop | 21 % → 4 % | 0.67 | 0.19 | 436 |
| tilted | 9 % → 9 % | 0.67 | 0.97 | 315 |
| over the wet one | 20 % → 7 % | 0.67 | 0.33 | 219 |
| long, no reload | 20 % → 4 % | 0.67 | 0.21 | 917 | quarters: 0.38 → 0.07 → 0.00 → 0.00

Numbers say: pressure barely changes the width.

## Dry pastel
Pastel · 26 px · 15.0 s

![Dry pastel](Dry-pastel.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 5 % → 5 % | 0.36 | 1.00 | 47 |
| heavy line | 6 % → 6 % | 0.36 | 1.00 | 43 |
| pressure swell | 5 % → 5 % | 0.36 | 1.00 | 35 |
| fast wave | 15 % → 15 % | 0.36 | 1.00 | 141 |
| slow wave | 14 % → 14 % | 0.36 | 1.00 | 189 |
| spiral | 23 % → 23 % | 0.36 | 1.00 | 259 |
| loop | 11 % → 11 % | 0.36 | 1.00 | 96 |
| tilted | 5 % → 5 % | 0.37 | 1.00 | 56 |
| over the wet one | 10 % → 10 % | 0.37 | 1.00 | 45 |
| long, no reload | 26 % → 26 % | 0.36 | 1.00 | 373 | quarters: 0.11 → 0.10 → 0.10 → 0.11

Numbers say: the long stroke does not run out of paint.

## 0.45 · Charcoal
Charcoal · 18 px · 14.7 s

![0.45 · Charcoal](0-45-Charcoal.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 4 % → 4 % | 0.79 | 1.00 | 35 |
| heavy line | 4 % → 4 % | 0.79 | 1.00 | 34 |
| pressure swell | 4 % → 4 % | 0.79 | 1.00 | 15 |
| fast wave | 11 % → 11 % | 0.79 | 1.00 | 66 |
| slow wave | 11 % → 11 % | 0.78 | 1.00 | 74 |
| spiral | 20 % → 20 % | 0.79 | 1.00 | 107 |
| loop | 10 % → 10 % | 0.79 | 1.00 | 47 |
| tilted | 4 % → 4 % | 0.78 | 1.00 | 32 |
| over the wet one | 9 % → 9 % | 0.78 | 1.00 | 23 |
| long, no reload | 26 % → 26 % | 0.79 | 1.00 | 138 | quarters: 0.23 → 0.22 → 0.23 → 0.24

Numbers say: pressure barely changes the width; the long stroke does not run out of paint.

## Watercolour — wash
Watercolor · 50 px · 46.4 s

![Watercolour — wash](Watercolour-wash.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 9 % → 11 % | 0.01 | 1.22 | 109 |
| heavy line | 12 % → 14 % | 0.01 | 1.17 | 122 |
| pressure swell | 8 % → 10 % | 0.01 | 1.22 | 84 |
| fast wave | 26 % → 30 % | 0.01 | 1.18 | 284 |
| slow wave | 25 % → 29 % | 0.01 | 1.18 | 520 |
| spiral | 39 % → 46 % | 0.01 | 1.17 | 493 |
| loop | 22 % → 27 % | 0.01 | 1.21 | 409 |
| tilted | 10 % → 11 % | 0.01 | 1.18 | 191 |
| over the wet one | 22 % → 25 % | 0.01 | 1.14 | 105 |
| long, no reload | 45 % → 54 % | 0.01 | 1.18 | 860 | quarters: 0.01 → 0.01 → 0.01 → 0.00

## Watercolour — wet-in-wet
Watercolor · 44 px · 42.7 s

![Watercolour — wet-in-wet](Watercolour-wet-in-wet.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 7 % → 9 % | 0.02 | 1.26 | 84 |
| heavy line | 10 % → 12 % | 0.02 | 1.22 | 97 |
| pressure swell | 7 % → 9 % | 0.02 | 1.21 | 69 |
| fast wave | 23 % → 27 % | 0.02 | 1.17 | 247 |
| slow wave | 22 % → 26 % | 0.02 | 1.18 | 406 |
| spiral | 36 % → 43 % | 0.02 | 1.20 | 396 |
| loop | 19 % → 23 % | 0.02 | 1.20 | 273 |
| tilted | 7 % → 9 % | 0.02 | 1.19 | 140 |
| over the wet one | 17 % → 19 % | 0.02 | 1.12 | 92 |
| long, no reload | 42 % → 49 % | 0.02 | 1.18 | 823 | quarters: 0.01 → 0.01 → 0.01 → 0.01

## Watercolour — glaze
Watercolor · 38 px · 42.3 s

![Watercolour — glaze](Watercolour-glaze.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 7 % → 9 % | 0.01 | 1.28 | 97 |
| heavy line | 10 % → 13 % | 0.01 | 1.25 | 97 |
| pressure swell | 7 % → 9 % | 0.01 | 1.29 | 112 |
| fast wave | 20 % → 25 % | 0.01 | 1.24 | 306 |
| slow wave | 19 % → 24 % | 0.01 | 1.26 | 370 |
| spiral | 31 % → 37 % | 0.01 | 1.21 | 642 |
| loop | 18 % → 23 % | 0.01 | 1.27 | 348 |
| tilted | 7 % → 8 % | 0.01 | 1.20 | 248 |
| over the wet one | 17 % → 20 % | 0.01 | 1.19 | 110 |
| long, no reload | 36 % → 42 % | 0.01 | 1.17 | 571 | quarters: 0.01 → 0.00 → 0.00 → 0.00

## Watercolour — granulating
Watercolor · 44 px · 42.6 s

![Watercolour — granulating](Watercolour-granulating.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 8 % → 10 % | 0.02 | 1.18 | 122 |
| heavy line | 12 % → 14 % | 0.01 | 1.15 | 100 |
| pressure swell | 8 % → 10 % | 0.02 | 1.18 | 104 |
| fast wave | 25 % → 29 % | 0.01 | 1.15 | 237 |
| slow wave | 24 % → 27 % | 0.02 | 1.16 | 436 |
| spiral | 39 % → 44 % | 0.01 | 1.15 | 409 |
| loop | 22 % → 25 % | 0.01 | 1.17 | 228 |
| tilted | 9 % → 11 % | 0.02 | 1.15 | 148 |
| over the wet one | 21 % → 23 % | 0.02 | 1.11 | 119 |
| long, no reload | 45 % → 52 % | 0.01 | 1.15 | 734 | quarters: 0.01 → 0.01 → 0.01 → 0.01

## Watercolour — dry brush
Watercolor · 36 px · 35.3 s

![Watercolour — dry brush](Watercolour-dry-brush.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 7 % → 8 % | 0.05 | 1.07 | 118 |
| heavy line | 11 % → 12 % | 0.04 | 1.03 | 139 |
| pressure swell | 9 % → 10 % | 0.05 | 1.07 | 95 |
| fast wave | 21 % → 14 % | 0.04 | 0.68 | 300 |
| slow wave | 19 % → 13 % | 0.04 | 0.70 | 691 |
| spiral | 24 % → 15 % | 0.04 | 0.61 | 545 |
| loop | 17 % → 14 % | 0.04 | 0.85 | 259 |
| tilted | 7 % → 8 % | 0.05 | 1.19 | 139 |
| over the wet one | 17 % → 17 % | 0.05 | 0.99 | 139 |
| long, no reload | 22 % → 15 % | 0.04 | 0.68 | 721 | quarters: 0.02 → 0.00 → 0.00 → 0.00

## Gouache
Gouache · 30 px · 34.2 s

![Gouache](Gouache.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 8 % → 6 % | 0.14 | 0.67 | 80 |
| heavy line | 13 % → 6 % | 0.14 | 0.47 | 97 |
| pressure swell | 10 % → 6 % | 0.14 | 0.61 | 86 |
| fast wave | 27 % → 7 % | 0.14 | 0.27 | 241 |
| slow wave | 27 % → 7 % | 0.14 | 0.27 | 464 |
| spiral | 37 % → 8 % | 0.14 | 0.22 | 465 |
| loop | 22 % → 8 % | 0.14 | 0.36 | 210 |
| tilted | 9 % → 9 % | 0.14 | 1.02 | 172 |
| over the wet one | 20 % → 13 % | 0.14 | 0.67 | 144 |
| long, no reload | 38 % → 10 % | 0.14 | 0.25 | 579 | quarters: 0.07 → 0.04 → 0.01 → 0.01

## Oil — alla prima
Oil · 30 px · 26.2 s

![Oil — alla prima](Oil-alla-prima.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 9 % → 9 % | 0.50 | 1.00 | 120 |
| heavy line | 10 % → 10 % | 0.50 | 1.00 | 108 |
| pressure swell | 8 % → 8 % | 0.52 | 1.00 | 74 |
| fast wave | 24 % → 24 % | 0.49 | 1.00 | 280 |
| slow wave | 25 % → 25 % | 0.50 | 1.00 | 484 |
| spiral | 38 % → 38 % | 0.44 | 1.00 | 522 |
| loop | 21 % → 21 % | 0.50 | 1.00 | 223 |
| tilted | 11 % → 11 % | 0.50 | 1.00 | 169 |
| over the wet one | 20 % → 20 % | 0.50 | 1.00 | 174 |
| long, no reload | 46 % → 46 % | 0.40 | 1.00 | 840 | quarters: 0.31 → 0.24 → 0.17 → 0.10

Numbers say: pressure barely changes the width.

## Oil — impasto
Oil · 34 px · 27.0 s

![Oil — impasto](Oil-impasto.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 11 % → 11 % | 0.24 | 1.00 | 118 |
| heavy line | 12 % → 12 % | 0.23 | 1.00 | 123 |
| pressure swell | 9 % → 9 % | 0.25 | 1.00 | 106 |
| fast wave | 29 % → 29 % | 0.21 | 1.00 | 349 |
| slow wave | 29 % → 29 % | 0.21 | 1.00 | 662 |
| spiral | 48 % → 48 % | 0.17 | 1.00 | 590 |
| loop | 25 % → 25 % | 0.21 | 1.00 | 404 |
| tilted | 12 % → 12 % | 0.24 | 1.00 | 245 |
| over the wet one | 23 % → 23 % | 0.24 | 1.00 | 192 |
| long, no reload | 55 % → 55 % | 0.15 | 1.00 | 1600 | quarters: 0.16 → 0.11 → 0.06 → 0.02

Numbers say: pressure barely changes the width.

## Oil — glaze
Oil · 40 px · 22.6 s

![Oil — glaze](Oil-glaze.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 10 % → 10 % | 0.49 | 1.00 | 292 |
| heavy line | 14 % → 14 % | 0.48 | 1.00 | 220 |
| pressure swell | 10 % → 10 % | 0.49 | 1.00 | 101 |
| fast wave | 28 % → 28 % | 0.46 | 1.00 | 701 |
| slow wave | 30 % → 30 % | 0.46 | 1.00 | 989 |
| spiral | 42 % → 42 % | 0.44 | 1.00 | 573 |
| loop | 24 % → 24 % | 0.47 | 1.00 | 255 |
| tilted | 11 % → 11 % | 0.47 | 1.00 | 176 |
| over the wet one | 23 % → 23 % | 0.47 | 1.00 | 125 |
| long, no reload | 47 % → 47 % | 0.43 | 1.00 | 793 | quarters: 0.33 → 0.24 → 0.18 → 0.14

## Oil — scumble
Oil · 36 px · 26.4 s

![Oil — scumble](Oil-scumble.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 11 % → 11 % | 0.06 | 1.00 | 156 |
| heavy line | 12 % → 12 % | 0.05 | 1.00 | 160 |
| pressure swell | 9 % → 9 % | 0.06 | 1.00 | 119 |
| fast wave | 18 % → 18 % | 0.04 | 1.00 | 380 |
| slow wave | 20 % → 20 % | 0.04 | 1.00 | 932 |
| spiral | 19 % → 19 % | 0.03 | 1.00 | 974 |
| loop | 22 % → 22 % | 0.04 | 1.00 | 382 |
| tilted | 10 % → 10 % | 0.05 | 1.00 | 184 |
| over the wet one | 21 % → 21 % | 0.05 | 1.00 | 154 |
| long, no reload | 18 % → 18 % | 0.04 | 1.00 | 956 | quarters: 0.03 → 0.00 → 0.00 → 0.00

Numbers say: pressure barely changes the width.

## Acrylic — heavy body
Heavy acrylic · 30 px · 20.1 s

![Acrylic — heavy body](Acrylic-heavy-body.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 10 % → 9 % | 0.51 | 0.93 | 120 |
| heavy line | 11 % → 10 % | 0.51 | 0.93 | 101 |
| pressure swell | 8 % → 8 % | 0.52 | 0.94 | 105 |
| fast wave | 24 % → 14 % | 0.51 | 0.58 | 368 |
| slow wave | 25 % → 15 % | 0.51 | 0.59 | 611 |
| spiral | 37 % → 15 % | 0.51 | 0.40 | 643 |
| loop | 22 % → 16 % | 0.51 | 0.73 | 262 |
| tilted | 10 % → 10 % | 0.51 | 1.00 | 121 |
| over the wet one | 20 % → 17 % | 0.51 | 0.88 | 111 |
| long, no reload | 39 % → 15 % | 0.51 | 0.40 | 666 | quarters: 0.30 → 0.20 → 0.10 → 0.02

Numbers say: pressure barely changes the width.

## Acrylic — fluid
Watercolor · 36 px · 40.2 s

![Acrylic — fluid](Acrylic-fluid.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 9 % → 10 % | 0.06 | 1.11 | 136 |
| heavy line | 13 % → 14 % | 0.05 | 1.07 | 118 |
| pressure swell | 9 % → 10 % | 0.07 | 1.09 | 146 |
| fast wave | 26 % → 28 % | 0.05 | 1.07 | 231 |
| slow wave | 24 % → 26 % | 0.07 | 1.08 | 368 |
| spiral | 39 % → 41 % | 0.05 | 1.06 | 415 |
| loop | 22 % → 25 % | 0.06 | 1.11 | 240 |
| tilted | 8 % → 9 % | 0.07 | 1.17 | 125 |
| over the wet one | 21 % → 22 % | 0.07 | 1.05 | 111 |
| long, no reload | 44 % → 47 % | 0.05 | 1.06 | 587 | quarters: 0.05 → 0.03 → 0.02 → 0.01

## Acrylic — palette knife
Heavy acrylic · 42 px · 26.3 s

![Acrylic — palette knife](Acrylic-palette-knife.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 15 % → 15 % | 0.06 | 0.98 | 37 |
| heavy line | 15 % → 15 % | 0.05 | 0.98 | 34 |
| pressure swell | 12 % → 12 % | 0.06 | 0.99 | 16 |
| fast wave | 37 % → 20 % | 0.06 | 0.54 | 58 |
| slow wave | 37 % → 21 % | 0.06 | 0.56 | 105 |
| spiral | 48 % → 19 % | 0.06 | 0.38 | 127 |
| loop | 32 % → 24 % | 0.05 | 0.75 | 57 |
| tilted | 12 % → 12 % | 0.05 | 1.00 | 21 |
| over the wet one | 26 % → 26 % | 0.05 | 0.98 | 21 |
| long, no reload | 55 % → 20 % | 0.06 | 0.36 | 136 | quarters: 0.04 → 0.02 → 0.00 → 0.00

Numbers say: pressure barely changes the width.

## Finger on oil
Oil · 30 px · 19.1 s

![Finger on oil](Finger-on-oil.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 8 % → 8 % | 0.34 | 1.00 | 57 |
| heavy line | 12 % → 12 % | 0.30 | 1.00 | 86 |
| pressure swell | 8 % → 8 % | 0.35 | 1.00 | 49 |
| fast wave | 16 % → 16 % | 0.22 | 1.00 | 151 |
| slow wave | 17 % → 17 % | 0.23 | 1.00 | 381 |
| spiral | 18 % → 18 % | 0.22 | 1.00 | 387 |
| loop | 18 % → 18 % | 0.23 | 1.00 | 151 |
| tilted | 9 % → 9 % | 0.31 | 1.00 | 92 |
| over the wet one | 18 % → 18 % | 0.31 | 1.00 | 77 |
| long, no reload | 15 % → 15 % | 0.23 | 1.00 | 385 | quarters: 0.13 → 0.01 → 0.00 → 0.00

## Palette knife — oil
Oil · 44 px · 29.6 s

![Palette knife — oil](Palette-knife-oil.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 16 % → 16 % | 0.10 | 1.00 | 37 |
| heavy line | 16 % → 16 % | 0.09 | 1.00 | 37 |
| pressure swell | 12 % → 12 % | 0.10 | 1.00 | 12 |
| fast wave | 39 % → 39 % | 0.07 | 1.00 | 58 |
| slow wave | 39 % → 39 % | 0.07 | 1.00 | 107 |
| spiral | 54 % → 54 % | 0.05 | 1.00 | 119 |
| loop | 34 % → 34 % | 0.08 | 1.00 | 60 |
| tilted | 13 % → 13 % | 0.09 | 1.00 | 24 |
| over the wet one | 28 % → 28 % | 0.09 | 1.00 | 33 |
| long, no reload | 65 % → 65 % | 0.05 | 1.00 | 158 | quarters: 0.08 → 0.04 → 0.01 → 0.00

Numbers say: pressure barely changes the width.

## 0.45 · Sponge
Watercolor · 46 px · 35.3 s

![0.45 · Sponge](0-45-Sponge.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 11 % → 0 % | 0.00 | 0.00 | 59 |
| heavy line | 13 % → 0 % | 0.01 | 0.00 | 86 |
| pressure swell | 9 % → 1 % | 0.02 | 0.14 | 62 |
| fast wave | 23 % → 2 % | 0.01 | 0.08 | 189 |
| slow wave | 26 % → 8 % | 0.02 | 0.30 | 327 |
| spiral | 34 % → 11 % | 0.02 | 0.32 | 409 |
| loop | 22 % → 4 % | 0.02 | 0.19 | 521 |
| tilted | 9 % → 10 % | 0.04 | 1.19 | 143 |
| over the wet one | 22 % → 10 % | 0.04 | 0.44 | 80 |
| long, no reload | 41 % → 19 % | 0.02 | 0.47 | 500 | quarters: 0.01 → 0.01 → 0.01 → 0.01

## 0.45 · Eraser
Eraser · 30 px · 29.9 s · over bands of wet oil paint and oil pastel in turn (it works on paint already there: look at what it does to the bands; covered counts the bands too)

![0.45 · Eraser](0-45-Eraser.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 23 % → 23 % | 0.81 | 1.00 | 63 |
| heavy line | 22 % → 22 % | 0.81 | 1.00 | 259 |
| pressure swell | 22 % → 22 % | 0.81 | 1.00 | 64 |
| fast wave | 21 % → 21 % | 0.80 | 1.00 | 167 |
| slow wave | 20 % → 20 % | 0.81 | 1.00 | 340 |
| spiral | 20 % → 20 % | 0.79 | 1.00 | 273 |
| loop | 21 % → 21 % | 0.79 | 1.00 | 133 |
| tilted | 22 % → 22 % | 0.80 | 1.00 | 83 |
| over the wet one | 21 % → 21 % | 0.80 | 1.00 | 67 |
| long, no reload | 16 % → 16 % | 0.79 | 1.00 | 401 | quarters: 0.13 → 0.15 → 0.12 → 0.16

Numbers say: pressure barely changes the width; the long stroke does not run out of paint.

## Lift wet paint
Eraser · 30 px · 26.8 s · over bands of wet oil paint and oil pastel in turn (it works on paint already there: look at what it does to the bands; covered counts the bands too)

![Lift wet paint](Lift-wet-paint.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 23 % → 23 % | 0.81 | 1.00 | 47 |
| heavy line | 23 % → 23 % | 0.81 | 1.00 | 62 |
| pressure swell | 23 % → 23 % | 0.81 | 1.00 | 68 |
| fast wave | 23 % → 23 % | 0.81 | 1.00 | 202 |
| slow wave | 23 % → 23 % | 0.81 | 1.00 | 223 |
| spiral | 23 % → 23 % | 0.81 | 1.00 | 207 |
| loop | 23 % → 23 % | 0.81 | 1.00 | 122 |
| tilted | 23 % → 23 % | 0.81 | 1.00 | 60 |
| over the wet one | 23 % → 23 % | 0.81 | 1.00 | 48 |
| long, no reload | 23 % → 23 % | 0.81 | 1.00 | 318 | quarters: 0.18 → 0.23 → 0.16 → 0.23

Numbers say: pressure barely changes the width; the long stroke does not run out of paint.

## Sgraffito
Eraser · 10 px · 26.7 s · over bands of wet oil paint and oil pastel in turn (it works on paint already there: look at what it does to the bands; covered counts the bands too)

![Sgraffito](Sgraffito.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 23 % → 23 % | 0.80 | 1.00 | 19 |
| heavy line | 23 % → 23 % | 0.81 | 1.00 | 19 |
| pressure swell | 23 % → 23 % | 0.81 | 1.00 | 6 |
| fast wave | 23 % → 23 % | 0.81 | 1.00 | 23 |
| slow wave | 23 % → 23 % | 0.81 | 1.00 | 33 |
| spiral | 23 % → 23 % | 0.81 | 1.00 | 41 |
| loop | 23 % → 23 % | 0.81 | 1.00 | 20 |
| tilted | 23 % → 23 % | 0.81 | 1.00 | 8 |
| over the wet one | 23 % → 23 % | 0.81 | 1.00 | 8 |
| long, no reload | 23 % → 23 % | 0.81 | 1.00 | 65 | quarters: 0.17 → 0.23 → 0.16 → 0.23

Numbers say: pressure barely changes the width; the long stroke does not run out of paint.

## Brush Artist · Refs · #01 Henry Ward peach cloud
Gouache · 44 px · 34.2 s

![Brush Artist · Refs · #01 Henry Ward peach cloud](Brush-Artist-Refs-01-Henry-Ward-peach-cloud.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 14 % → 3 % | 0.10 | 0.25 | 185 |
| heavy line | 15 % → 5 % | 0.10 | 0.32 | 194 |
| pressure swell | 11 % → 5 % | 0.10 | 0.42 | 137 |
| fast wave | 34 % → 5 % | 0.10 | 0.16 | 480 |
| slow wave | 34 % → 6 % | 0.10 | 0.17 | 930 |
| spiral | 46 % → 6 % | 0.10 | 0.13 | 950 |
| loop | 30 % → 6 % | 0.10 | 0.21 | 486 |
| tilted | 12 % → 12 % | 0.10 | 1.01 | 291 |
| over the wet one | 26 % → 11 % | 0.10 | 0.42 | 296 |
| long, no reload | 44 % → 8 % | 0.10 | 0.18 | 1324 | quarters: 0.06 → 0.01 → 0.00 → 0.00

Numbers say: pressure barely changes the width.

## Brush Artist · Refs · #02 Henry Ward cream strokes
Gouache · 46 px · 36.3 s

![Brush Artist · Refs · #02 Henry Ward cream strokes](Brush-Artist-Refs-02-Henry-Ward-cream-strokes.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 13 % → 3 % | 0.03 | 0.20 | 198 |
| heavy line | 14 % → 4 % | 0.03 | 0.27 | 226 |
| pressure swell | 11 % → 5 % | 0.03 | 0.44 | 133 |
| fast wave | 32 % → 5 % | 0.03 | 0.15 | 750 |
| slow wave | 32 % → 5 % | 0.03 | 0.17 | 915 |
| spiral | 45 % → 5 % | 0.03 | 0.12 | 891 |
| loop | 29 % → 6 % | 0.03 | 0.21 | 432 |
| tilted | 12 % → 12 % | 0.03 | 1.00 | 264 |
| over the wet one | 24 % → 11 % | 0.03 | 0.43 | 238 |
| long, no reload | 43 % → 8 % | 0.03 | 0.18 | 1251 | quarters: 0.02 → 0.01 → 0.00 → 0.00

Numbers say: pressure barely changes the width.

## Brush Artist · Refs · #03 Henry Ward navy contours
Heavy acrylic · 22 px · 19.9 s

![Brush Artist · Refs · #03 Henry Ward navy contours](Brush-Artist-Refs-03-Henry-Ward-navy-contours.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 7 % → 7 % | 0.70 | 0.94 | 92 |
| heavy line | 8 % → 8 % | 0.70 | 0.95 | 80 |
| pressure swell | 6 % → 6 % | 0.73 | 0.94 | 61 |
| fast wave | 19 % → 12 % | 0.72 | 0.65 | 255 |
| slow wave | 19 % → 13 % | 0.72 | 0.68 | 418 |
| spiral | 30 % → 13 % | 0.72 | 0.45 | 444 |
| loop | 17 % → 13 % | 0.72 | 0.81 | 207 |
| tilted | 8 % → 8 % | 0.71 | 1.00 | 133 |
| over the wet one | 16 % → 14 % | 0.71 | 0.89 | 108 |
| long, no reload | 34 % → 13 % | 0.72 | 0.40 | 593 | quarters: 0.35 → 0.29 → 0.19 → 0.07

Numbers say: pressure barely changes the width.

## Brush Artist · Refs · #04 Henry Ward grey cloud
Gouache · 50 px · 37.5 s

![Brush Artist · Refs · #04 Henry Ward grey cloud](Brush-Artist-Refs-04-Henry-Ward-grey-cloud.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 15 % → 3 % | 0.10 | 0.18 | 286 |
| heavy line | 16 % → 4 % | 0.10 | 0.26 | 270 |
| pressure swell | 12 % → 5 % | 0.10 | 0.40 | 160 |
| fast wave | 37 % → 5 % | 0.10 | 0.15 | 602 |
| slow wave | 36 % → 5 % | 0.10 | 0.15 | 1003 |
| spiral | 47 % → 6 % | 0.10 | 0.13 | 1700 |
| loop | 32 % → 7 % | 0.10 | 0.21 | 813 |
| tilted | 13 % → 13 % | 0.10 | 1.01 | 370 |
| over the wet one | 27 % → 12 % | 0.10 | 0.44 | 289 |
| long, no reload | 49 % → 9 % | 0.10 | 0.18 | 1287 | quarters: 0.06 → 0.01 → 0.00 → 0.00

Numbers say: pressure barely changes the width.

## Brush Artist · Refs · #05 Henry Ward green in rust loops
Heavy acrylic · 20 px · 20.4 s

![Brush Artist · Refs · #05 Henry Ward green in rust loops](Brush-Artist-Refs-05-Henry-Ward-green-in-rust-loops.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 7 % → 6 % | 0.55 | 0.94 | 177 |
| heavy line | 7 % → 7 % | 0.55 | 0.94 | 147 |
| pressure swell | 6 % → 5 % | 0.57 | 0.92 | 108 |
| fast wave | 17 % → 11 % | 0.56 | 0.64 | 309 |
| slow wave | 18 % → 12 % | 0.56 | 0.66 | 495 |
| spiral | 27 % → 11 % | 0.55 | 0.42 | 545 |
| loop | 15 % → 12 % | 0.55 | 0.79 | 220 |
| tilted | 8 % → 8 % | 0.56 | 1.00 | 117 |
| over the wet one | 15 % → 13 % | 0.56 | 0.87 | 105 |
| long, no reload | 30 % → 12 % | 0.56 | 0.39 | 626 | quarters: 0.25 → 0.18 → 0.10 → 0.02

Numbers say: pressure barely changes the width.

## Brush Artist · Refs · #06 Henry Ward scrubbed grey
Gouache · 50 px · 35.4 s

![Brush Artist · Refs · #06 Henry Ward scrubbed grey](Brush-Artist-Refs-06-Henry-Ward-scrubbed-grey.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 15 % → 3 % | 0.09 | 0.18 | 205 |
| heavy line | 16 % → 4 % | 0.09 | 0.26 | 205 |
| pressure swell | 12 % → 5 % | 0.09 | 0.40 | 139 |
| fast wave | 37 % → 5 % | 0.09 | 0.15 | 534 |
| slow wave | 36 % → 5 % | 0.09 | 0.15 | 1402 |
| spiral | 47 % → 6 % | 0.09 | 0.13 | 948 |
| loop | 32 % → 7 % | 0.09 | 0.21 | 477 |
| tilted | 13 % → 13 % | 0.09 | 1.01 | 258 |
| over the wet one | 27 % → 12 % | 0.09 | 0.44 | 211 |
| long, no reload | 49 % → 9 % | 0.08 | 0.18 | 1313 | quarters: 0.05 → 0.01 → 0.00 → 0.00

Numbers say: pressure barely changes the width.

## Brush Artist · Refs · #07 Henry Ward blue L + black zigzag
Heavy acrylic · 34 px · 22.2 s

![Brush Artist · Refs · #07 Henry Ward blue L + black zigzag](Brush-Artist-Refs-07-Henry-Ward-blue-L-black-zigzag.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 11 % → 11 % | 0.57 | 0.93 | 144 |
| heavy line | 12 % → 12 % | 0.57 | 0.93 | 135 |
| pressure swell | 9 % → 9 % | 0.59 | 0.94 | 81 |
| fast wave | 29 % → 20 % | 0.59 | 0.68 | 304 |
| slow wave | 30 % → 21 % | 0.58 | 0.72 | 566 |
| spiral | 47 % → 22 % | 0.58 | 0.46 | 575 |
| loop | 25 % → 21 % | 0.58 | 0.82 | 285 |
| tilted | 11 % → 11 % | 0.58 | 1.00 | 160 |
| over the wet one | 22 % → 20 % | 0.58 | 0.91 | 125 |
| long, no reload | 53 % → 22 % | 0.59 | 0.42 | 1188 | quarters: 0.40 → 0.32 → 0.21 → 0.10

Numbers say: pressure barely changes the width.

## Brush Artist · Refs · #08 Henry Ward olive bands
Gouache · 34 px · 31.4 s

![Brush Artist · Refs · #08 Henry Ward olive bands](Brush-Artist-Refs-08-Henry-Ward-olive-bands.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 9 % → 2 % | 0.57 | 0.29 | 146 |
| heavy line | 12 % → 3 % | 0.57 | 0.23 | 273 |
| pressure swell | 8 % → 3 % | 0.57 | 0.39 | 118 |
| fast wave | 26 % → 4 % | 0.57 | 0.16 | 352 |
| slow wave | 25 % → 4 % | 0.57 | 0.16 | 598 |
| spiral | 39 % → 4 % | 0.57 | 0.10 | 666 |
| loop | 22 % → 5 % | 0.57 | 0.21 | 328 |
| tilted | 10 % → 10 % | 0.57 | 0.98 | 163 |
| over the wet one | 21 % → 8 % | 0.57 | 0.41 | 132 |
| long, no reload | 44 % → 6 % | 0.57 | 0.13 | 998 | quarters: 0.35 → 0.26 → 0.16 → 0.07

## Brush Artist · Refs · #09 Henry Ward white loops
Gouache · 46 px · 37.8 s

![Brush Artist · Refs · #09 Henry Ward white loops](Brush-Artist-Refs-09-Henry-Ward-white-loops.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 13 % → 3 % | 0.02 | 0.20 | 218 |
| heavy line | 14 % → 4 % | 0.01 | 0.27 | 183 |
| pressure swell | 11 % → 5 % | 0.02 | 0.44 | 137 |
| fast wave | 32 % → 5 % | 0.01 | 0.15 | 556 |
| slow wave | 32 % → 5 % | 0.02 | 0.17 | 893 |
| spiral | 45 % → 5 % | 0.02 | 0.12 | 836 |
| loop | 29 % → 6 % | 0.02 | 0.21 | 441 |
| tilted | 12 % → 12 % | 0.02 | 1.00 | 340 |
| over the wet one | 24 % → 11 % | 0.02 | 0.43 | 314 |
| long, no reload | 43 % → 8 % | 0.02 | 0.18 | 1304 | quarters: 0.02 → 0.00 → 0.00 → 0.00

Numbers say: pressure barely changes the width.

## Brush Artist · Refs · #10 Henry Ward maroon loops
Heavy acrylic · 30 px · 21.3 s

![Brush Artist · Refs · #10 Henry Ward maroon loops](Brush-Artist-Refs-10-Henry-Ward-maroon-loops.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 10 % → 9 % | 0.69 | 0.94 | 116 |
| heavy line | 10 % → 10 % | 0.69 | 0.95 | 132 |
| pressure swell | 8 % → 8 % | 0.73 | 0.94 | 82 |
| fast wave | 25 % → 17 % | 0.73 | 0.70 | 318 |
| slow wave | 25 % → 18 % | 0.72 | 0.73 | 503 |
| spiral | 39 % → 18 % | 0.72 | 0.47 | 528 |
| loop | 21 % → 18 % | 0.72 | 0.85 | 257 |
| tilted | 10 % → 10 % | 0.72 | 1.00 | 138 |
| over the wet one | 20 % → 18 % | 0.72 | 0.91 | 146 |
| long, no reload | 46 % → 18 % | 0.73 | 0.40 | 981 | quarters: 0.44 → 0.38 → 0.31 → 0.22

Numbers say: pressure barely changes the width.

## Brush Artist · Refs · #11 Henry Ward purple spun balls
Heavy acrylic · 36 px · 26.5 s

![Brush Artist · Refs · #11 Henry Ward purple spun balls](Brush-Artist-Refs-11-Henry-Ward-purple-spun-balls.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 12 % → 11 % | 0.70 | 0.96 | 156 |
| heavy line | 13 % → 12 % | 0.70 | 0.96 | 124 |
| pressure swell | 10 % → 9 % | 0.74 | 0.95 | 99 |
| fast wave | 30 % → 22 % | 0.73 | 0.75 | 426 |
| slow wave | 30 % → 24 % | 0.73 | 0.79 | 631 |
| spiral | 49 % → 24 % | 0.73 | 0.50 | 722 |
| loop | 26 % → 23 % | 0.73 | 0.88 | 618 |
| tilted | 11 % → 11 % | 0.72 | 1.00 | 246 |
| over the wet one | 23 % → 21 % | 0.72 | 0.93 | 178 |
| long, no reload | 55 % → 24 % | 0.73 | 0.44 | 1856 | quarters: 0.51 → 0.46 → 0.39 → 0.28

Numbers say: pressure barely changes the width.

## Brush Artist · Refs · #12 Henry Ward black-olive cage
Gouache · 28 px · 30.6 s

![Brush Artist · Refs · #12 Henry Ward black-olive cage](Brush-Artist-Refs-12-Henry-Ward-black-olive-cage.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 7 % → 3 % | 0.62 | 0.37 | 127 |
| heavy line | 9 % → 4 % | 0.62 | 0.43 | 309 |
| pressure swell | 6 % → 4 % | 0.62 | 0.62 | 141 |
| fast wave | 21 % → 4 % | 0.62 | 0.21 | 502 |
| slow wave | 20 % → 4 % | 0.62 | 0.22 | 561 |
| spiral | 32 % → 5 % | 0.62 | 0.14 | 542 |
| loop | 18 % → 5 % | 0.62 | 0.29 | 398 |
| tilted | 9 % → 9 % | 0.62 | 0.98 | 158 |
| over the wet one | 17 % → 8 % | 0.62 | 0.47 | 127 |
| long, no reload | 39 % → 6 % | 0.62 | 0.15 | 563 | quarters: 0.32 → 0.26 → 0.19 → 0.09

## Brush Artist · Refs · #13 Henry Ward blue streaky form
Gouache · 50 px · 30.0 s

![Brush Artist · Refs · #13 Henry Ward blue streaky form](Brush-Artist-Refs-13-Henry-Ward-blue-streaky-form.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 15 % → 3 % | 0.09 | 0.18 | 167 |
| heavy line | 16 % → 4 % | 0.09 | 0.26 | 167 |
| pressure swell | 12 % → 5 % | 0.09 | 0.40 | 163 |
| fast wave | 37 % → 5 % | 0.09 | 0.15 | 471 |
| slow wave | 36 % → 5 % | 0.09 | 0.15 | 845 |
| spiral | 47 % → 6 % | 0.09 | 0.13 | 839 |
| loop | 32 % → 7 % | 0.09 | 0.21 | 393 |
| tilted | 13 % → 13 % | 0.09 | 1.01 | 203 |
| over the wet one | 27 % → 12 % | 0.09 | 0.44 | 247 |
| long, no reload | 49 % → 9 % | 0.09 | 0.18 | 1202 | quarters: 0.05 → 0.01 → 0.00 → 0.00

Numbers say: pressure barely changes the width.

## Brush Artist · Refs · #14 Henry Ward olive totem
Heavy acrylic · 48 px · 22.0 s

![Brush Artist · Refs · #14 Henry Ward olive totem](Brush-Artist-Refs-14-Henry-Ward-olive-totem.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 15 % → 15 % | 0.31 | 0.95 | 162 |
| heavy line | 16 % → 16 % | 0.31 | 0.95 | 148 |
| pressure swell | 13 % → 12 % | 0.32 | 0.95 | 110 |
| fast wave | 38 % → 30 % | 0.30 | 0.78 | 390 |
| slow wave | 39 % → 31 % | 0.30 | 0.81 | 672 |
| spiral | 58 % → 32 % | 0.30 | 0.55 | 937 |
| loop | 33 % → 29 % | 0.30 | 0.89 | 347 |
| tilted | 13 % → 13 % | 0.31 | 1.00 | 182 |
| over the wet one | 28 % → 26 % | 0.31 | 0.93 | 156 |
| long, no reload | 67 % → 33 % | 0.30 | 0.49 | 1111 | quarters: 0.26 → 0.18 → 0.09 → 0.03

Numbers say: pressure barely changes the width.

## Brush Artist · Refs · #15 Ultramarine brush script
Ink · 8 px · 28.3 s

![Brush Artist · Refs · #15 Ultramarine brush script](Brush-Artist-Refs-15-Ultramarine-brush-script.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 1 % → 4 % | 0.53 | 2.96 | 43 |
| heavy line | 9 % → 9 % | 0.65 | 1.00 | 89 |
| pressure swell | 5 % → 5 % | 0.68 | 1.15 | 83 |
| fast wave | 15 % → 14 % | 0.56 | 0.90 | 215 |
| slow wave | 12 % → 12 % | 0.56 | 0.97 | 210 |
| spiral | 19 % → 13 % | 0.53 | 0.72 | 271 |
| loop | 12 % → 12 % | 0.57 | 1.01 | 124 |
| tilted | 5 % → 5 % | 0.65 | 1.02 | 59 |
| over the wet one | 11 % → 12 % | 0.65 | 1.06 | 56 |
| long, no reload | 28 % → 14 % | 0.51 | 0.52 | 345 | quarters: 0.24 → 0.09 → 0.03 → 0.01

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #18 Blue oil-stick scribbles
Pastel · 10 px · 12.2 s

![Brush Artist · Refs · #18 Blue oil-stick scribbles](Brush-Artist-Refs-18-Blue-oil-stick-scribbles.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 2 % → 2 % | 0.50 | 1.00 | 39 |
| heavy line | 3 % → 3 % | 0.51 | 1.00 | 34 |
| pressure swell | 2 % → 2 % | 0.51 | 1.00 | 23 |
| fast wave | 6 % → 6 % | 0.52 | 1.00 | 71 |
| slow wave | 6 % → 6 % | 0.51 | 1.00 | 66 |
| spiral | 10 % → 10 % | 0.52 | 1.00 | 118 |
| loop | 5 % → 5 % | 0.51 | 1.00 | 66 |
| tilted | 2 % → 2 % | 0.51 | 1.00 | 32 |
| over the wet one | 5 % → 5 % | 0.51 | 1.00 | 39 |
| long, no reload | 14 % → 14 % | 0.52 | 1.00 | 193 | quarters: 0.08 → 0.08 → 0.08 → 0.08

Numbers say: the long stroke does not run out of paint.

## Brush Artist · Refs · #20 Orange-red crayon scribble
Pastel · 14 px · 12.5 s

![Brush Artist · Refs · #20 Orange-red crayon scribble](Brush-Artist-Refs-20-Orange-red-crayon-scribble.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 3 % → 3 % | 0.53 | 1.00 | 20 |
| heavy line | 4 % → 4 % | 0.53 | 1.00 | 38 |
| pressure swell | 3 % → 3 % | 0.53 | 1.00 | 29 |
| fast wave | 9 % → 9 % | 0.53 | 1.00 | 85 |
| slow wave | 9 % → 9 % | 0.53 | 1.00 | 102 |
| spiral | 14 % → 14 % | 0.53 | 1.00 | 136 |
| loop | 7 % → 7 % | 0.53 | 1.00 | 63 |
| tilted | 3 % → 3 % | 0.53 | 1.00 | 40 |
| over the wet one | 7 % → 7 % | 0.53 | 1.00 | 34 |
| long, no reload | 18 % → 18 % | 0.53 | 1.00 | 284 | quarters: 0.11 → 0.11 → 0.11 → 0.11

Numbers say: the long stroke does not run out of paint.

## Brush Artist · Refs · #21 Gritty black contours
Gouache · 12 px · 27.2 s

![Brush Artist · Refs · #21 Gritty black contours](Brush-Artist-Refs-21-Gritty-black-contours.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 3 % → 0 % | 0.79 | 0.14 | 114 |
| heavy line | 4 % → 0 % | 0.79 | 0.10 | 212 |
| pressure swell | 3 % → 0 % | 0.79 | 0.16 | 85 |
| fast wave | 7 % → 1 % | 0.79 | 0.10 | 263 |
| slow wave | 8 % → 1 % | 0.79 | 0.09 | 227 |
| spiral | 9 % → 1 % | 0.79 | 0.10 | 522 |
| loop | 8 % → 1 % | 0.79 | 0.09 | 334 |
| tilted | 4 % → 4 % | 0.79 | 0.91 | 93 |
| over the wet one | 7 % → 1 % | 0.79 | 0.18 | 94 |
| long, no reload | 7 % → 1 % | 0.79 | 0.12 | 613 | quarters: 0.20 → 0.07 → 0.00 → 0.00

## Brush Artist · Refs · #22 Bold black brush poster
Ink · 20 px · 37.3 s

![Brush Artist · Refs · #22 Bold black brush poster](Brush-Artist-Refs-22-Bold-black-brush-poster.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 3 % → 5 % | 0.79 | 1.63 | 40 |
| heavy line | 15 % → 15 % | 0.88 | 0.99 | 96 |
| pressure swell | 9 % → 9 % | 0.87 | 1.04 | 55 |
| fast wave | 27 % → 27 % | 0.87 | 0.98 | 216 |
| slow wave | 22 % → 22 % | 0.87 | 0.98 | 356 |
| spiral | 34 % → 32 % | 0.87 | 0.94 | 261 |
| loop | 20 % → 20 % | 0.88 | 1.00 | 164 |
| tilted | 8 % → 8 % | 0.88 | 1.01 | 90 |
| over the wet one | 19 % → 19 % | 0.88 | 1.00 | 75 |
| long, no reload | 45 % → 38 % | 0.86 | 0.83 | 476 | quarters: 0.54 → 0.45 → 0.35 → 0.26

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #23 Dry white on orange + black line
Gouache · 50 px · 34.2 s

![Brush Artist · Refs · #23 Dry white on orange + black line](Brush-Artist-Refs-23-Dry-white-on-orange-black-line.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 12 % → 2 % | 0.00 | 0.16 | 152 |
| heavy line | 16 % → 2 % | 0.00 | 0.12 | 240 |
| pressure swell | 11 % → 2 % | 0.00 | 0.20 | 162 |
| fast wave | 35 % → 3 % | 0.00 | 0.10 | 486 |
| slow wave | 34 % → 4 % | 0.00 | 0.11 | 828 |
| spiral | 49 % → 4 % | 0.00 | 0.08 | 848 |
| loop | 30 % → 4 % | 0.00 | 0.13 | 525 |
| tilted | 13 % → 13 % | 0.00 | 0.98 | 264 |
| over the wet one | 26 % → 8 % | 0.00 | 0.29 | 215 |
| long, no reload | 58 % → 5 % | 0.00 | 0.09 | 2212 | quarters: 0.01 → 0.01 → 0.00 → 0.00

## Brush Artist · Refs · #24 Picasso flat oil
Oil · 34 px · 26.3 s

![Brush Artist · Refs · #24 Picasso flat oil](Brush-Artist-Refs-24-Picasso-flat-oil.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 11 % → 11 % | 0.39 | 1.00 | 139 |
| heavy line | 12 % → 12 % | 0.39 | 1.00 | 156 |
| pressure swell | 9 % → 9 % | 0.41 | 1.00 | 124 |
| fast wave | 29 % → 29 % | 0.38 | 1.00 | 417 |
| slow wave | 29 % → 29 % | 0.38 | 1.00 | 1012 |
| spiral | 49 % → 49 % | 0.32 | 1.00 | 783 |
| loop | 25 % → 25 % | 0.39 | 1.00 | 349 |
| tilted | 11 % → 11 % | 0.39 | 1.00 | 189 |
| over the wet one | 22 % → 22 % | 0.39 | 1.00 | 156 |
| long, no reload | 58 % → 58 % | 0.29 | 1.00 | 1092 | quarters: 0.28 → 0.23 → 0.15 → 0.08

Numbers say: pressure barely changes the width.

## Brush Artist · Refs · #25 Yellow heavy flat stroke
Heavy acrylic · 110 px · 48.9 s

![Brush Artist · Refs · #25 Yellow heavy flat stroke](Brush-Artist-Refs-25-Yellow-heavy-flat-stroke.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 35 % → 36 % | 0.17 | 1.02 | 489 |
| heavy line | 36 % → 35 % | 0.17 | 0.97 | 533 |
| pressure swell | 28 % → 29 % | 0.17 | 1.04 | 429 |
| fast wave | 73 % → 76 % | 0.17 | 1.05 | 1743 |
| slow wave | 73 % → 72 % | 0.18 | 0.98 | 2250 |
| spiral | 86 % → 83 % | 0.17 | 0.97 | 2298 |
| loop | 65 % → 64 % | 0.17 | 0.99 | 1167 |
| tilted | 26 % → 26 % | 0.17 | 1.00 | 738 |
| over the wet one | 55 % → 54 % | 0.17 | 0.97 | 832 |
| long, no reload | 98 % → 97 % | 0.17 | 0.99 | 3525 | quarters: 0.18 → 0.17 → 0.17 → 0.16

Numbers say: pressure barely changes the width; the long stroke does not run out of paint.

## Brush Artist · Refs · #27 Orange impasto swatch
Heavy acrylic · 60 px · 33.6 s

![Brush Artist · Refs · #27 Orange impasto swatch](Brush-Artist-Refs-27-Orange-impasto-swatch.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 20 % → 19 % | 0.35 | 0.97 | 242 |
| heavy line | 20 % → 20 % | 0.35 | 0.97 | 251 |
| pressure swell | 16 % → 15 % | 0.36 | 0.97 | 246 |
| fast wave | 48 % → 47 % | 0.35 | 0.98 | 884 |
| slow wave | 48 % → 47 % | 0.36 | 0.98 | 1069 |
| spiral | 69 % → 62 % | 0.35 | 0.91 | 1055 |
| loop | 42 % → 40 % | 0.35 | 0.97 | 554 |
| tilted | 16 % → 16 % | 0.36 | 1.00 | 298 |
| over the wet one | 34 % → 33 % | 0.36 | 0.97 | 255 |
| long, no reload | 85 % → 75 % | 0.35 | 0.88 | 1520 | quarters: 0.33 → 0.31 → 0.30 → 0.26

Numbers say: pressure barely changes the width.

## Brush Artist · Refs · #28 Miles Davis black lines
Ink · 22 px · 36.7 s

![Brush Artist · Refs · #28 Miles Davis black lines](Brush-Artist-Refs-28-Miles-Davis-black-lines.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 4 % → 6 % | 0.81 | 1.49 | 62 |
| heavy line | 17 % → 17 % | 0.88 | 0.99 | 192 |
| pressure swell | 10 % → 10 % | 0.87 | 1.03 | 120 |
| fast wave | 31 % → 30 % | 0.87 | 0.98 | 221 |
| slow wave | 25 % → 25 % | 0.87 | 0.99 | 328 |
| spiral | 39 % → 37 % | 0.87 | 0.95 | 367 |
| loop | 23 % → 23 % | 0.88 | 1.00 | 183 |
| tilted | 9 % → 9 % | 0.88 | 1.01 | 85 |
| over the wet one | 21 % → 21 % | 0.88 | 1.00 | 79 |
| long, no reload | 51 % → 43 % | 0.86 | 0.84 | 490 | quarters: 0.59 → 0.51 → 0.40 → 0.31

## Brush Artist · Refs · #29 Shrigley magenta asterisk
Watercolor · 70 px · 47.1 s

![Brush Artist · Refs · #29 Shrigley magenta asterisk](Brush-Artist-Refs-29-Shrigley-magenta-asterisk.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 10 % → 14 % | 0.51 | 1.41 | 71 |
| heavy line | 17 % → 18 % | 0.51 | 1.05 | 176 |
| pressure swell | 11 % → 13 % | 0.51 | 1.15 | 99 |
| fast wave | 38 % → 39 % | 0.51 | 1.02 | 322 |
| slow wave | 36 % → 40 % | 0.51 | 1.12 | 524 |
| spiral | 61 % → 61 % | 0.51 | 1.01 | 709 |
| loop | 31 % → 32 % | 0.51 | 1.05 | 247 |
| tilted | 18 % → 18 % | 0.51 | 1.01 | 244 |
| over the wet one | 32 % → 35 % | 0.51 | 1.09 | 122 |
| long, no reload | 75 % → 76 % | 0.50 | 1.02 | 801 | quarters: 0.44 → 0.42 → 0.41 → 0.38

Numbers say: the long stroke does not run out of paint.

## Brush Artist · Refs · #30 Red gouache face patch
Gouache · 60 px · 53.6 s

![Brush Artist · Refs · #30 Red gouache face patch](Brush-Artist-Refs-30-Red-gouache-face-patch.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 16 % → 15 % | 0.49 | 0.91 | 205 |
| heavy line | 25 % → 20 % | 0.49 | 0.80 | 243 |
| pressure swell | 19 % → 17 % | 0.49 | 0.86 | 469 |
| fast wave | 49 % → 28 % | 0.49 | 0.58 | 949 |
| slow wave | 48 % → 28 % | 0.49 | 0.59 | 1099 |
| spiral | 60 % → 28 % | 0.49 | 0.47 | 1063 |
| loop | 40 % → 29 % | 0.49 | 0.74 | 499 |
| tilted | 16 % → 17 % | 0.49 | 1.00 | 405 |
| over the wet one | 36 % → 32 % | 0.49 | 0.89 | 253 |
| long, no reload | 67 % → 30 % | 0.49 | 0.44 | 1282 | quarters: 0.43 → 0.39 → 0.32 → 0.26

## Brush Artist · Refs · #31 Warhol blotted line
Ink · 6 px · 31.5 s

![Brush Artist · Refs · #31 Warhol blotted line](Brush-Artist-Refs-31-Warhol-blotted-line.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 1 % → 3 % | 0.75 | 3.30 | 46 |
| heavy line | 7 % → 7 % | 0.83 | 0.98 | 141 |
| pressure swell | 4 % → 4 % | 0.84 | 1.12 | 56 |
| fast wave | 12 % → 9 % | 0.82 | 0.76 | 300 |
| slow wave | 10 % → 8 % | 0.80 | 0.84 | 155 |
| spiral | 15 % → 8 % | 0.80 | 0.57 | 322 |
| loop | 9 % → 9 % | 0.80 | 0.93 | 164 |
| tilted | 3 % → 3 % | 0.84 | 1.03 | 55 |
| over the wet one | 8 % → 8 % | 0.84 | 1.02 | 58 |
| long, no reload | 21 % → 9 % | 0.78 | 0.43 | 702 | quarters: 0.25 → 0.13 → 0.05 → 0.01

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #32 Thick orange swipes
Heavy acrylic · 90 px · 43.4 s

![Brush Artist · Refs · #32 Thick orange swipes](Brush-Artist-Refs-32-Thick-orange-swipes.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 29 % → 29 % | 0.38 | 1.00 | 406 |
| heavy line | 30 % → 29 % | 0.38 | 0.97 | 443 |
| pressure swell | 23 % → 23 % | 0.38 | 1.01 | 326 |
| fast wave | 63 % → 65 % | 0.38 | 1.03 | 1298 |
| slow wave | 64 % → 63 % | 0.39 | 0.98 | 2005 |
| spiral | 79 % → 77 % | 0.38 | 0.98 | 2292 |
| loop | 57 % → 56 % | 0.38 | 0.99 | 899 |
| tilted | 21 % → 21 % | 0.38 | 1.00 | 477 |
| over the wet one | 47 % → 45 % | 0.38 | 0.97 | 400 |
| long, no reload | 95 % → 93 % | 0.38 | 0.98 | 2483 | quarters: 0.38 → 0.38 → 0.37 → 0.35

Numbers say: pressure barely changes the width; the long stroke does not run out of paint.

## Brush Artist · Refs · #33 Red wet-in-wet band
Watercolor · 80 px · 60.6 s

![Brush Artist · Refs · #33 Red wet-in-wet band](Brush-Artist-Refs-33-Red-wet-in-wet-band.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 22 % → 23 % | 0.54 | 1.02 | 197 |
| heavy line | 34 % → 34 % | 0.53 | 0.99 | 345 |
| pressure swell | 22 % → 23 % | 0.54 | 1.04 | 241 |
| fast wave | 65 % → 68 % | 0.53 | 1.04 | 675 |
| slow wave | 63 % → 63 % | 0.54 | 1.00 | 1045 |
| spiral | 77 % → 77 % | 0.54 | 1.00 | 1299 |
| loop | 54 % → 55 % | 0.54 | 1.01 | 482 |
| tilted | 24 % → 24 % | 0.53 | 1.01 | 350 |
| over the wet one | 49 % → 53 % | 0.53 | 1.07 | 242 |
| long, no reload | 96 % → 97 % | 0.54 | 1.00 | 1324 | quarters: 0.55 → 0.55 → 0.54 → 0.50

Numbers say: the long stroke does not run out of paint.

## Brush Artist · Refs · #34 Magenta oil patches
Oil · 60 px · 32.8 s

![Brush Artist · Refs · #34 Magenta oil patches](Brush-Artist-Refs-34-Magenta-oil-patches.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 19 % → 19 % | 0.58 | 1.00 | 373 |
| heavy line | 20 % → 20 % | 0.59 | 1.00 | 281 |
| pressure swell | 15 % → 15 % | 0.62 | 1.01 | 178 |
| fast wave | 46 % → 47 % | 0.61 | 1.02 | 687 |
| slow wave | 47 % → 47 % | 0.61 | 1.00 | 1190 |
| spiral | 69 % → 69 % | 0.59 | 1.00 | 1342 |
| loop | 41 % → 41 % | 0.61 | 1.00 | 632 |
| tilted | 17 % → 17 % | 0.61 | 1.00 | 300 |
| over the wet one | 34 % → 34 % | 0.61 | 1.00 | 298 |
| long, no reload | 84 % → 84 % | 0.59 | 1.00 | 2453 | quarters: 0.58 → 0.55 → 0.51 → 0.45

Numbers say: pressure barely changes the width.

## Brush Artist · Refs · #35 Red band with runs
Watercolor · 70 px · 58.2 s

![Brush Artist · Refs · #35 Red band with runs](Brush-Artist-Refs-35-Red-band-with-runs.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 20 % → 20 % | 0.54 | 1.01 | 233 |
| heavy line | 30 % → 30 % | 0.53 | 0.99 | 303 |
| pressure swell | 20 % → 20 % | 0.55 | 1.03 | 148 |
| fast wave | 60 % → 62 % | 0.53 | 1.04 | 477 |
| slow wave | 58 % → 58 % | 0.54 | 1.00 | 841 |
| spiral | 74 % → 74 % | 0.54 | 1.00 | 759 |
| loop | 50 % → 50 % | 0.55 | 1.00 | 400 |
| tilted | 21 % → 22 % | 0.54 | 1.01 | 276 |
| over the wet one | 45 % → 47 % | 0.54 | 1.06 | 189 |
| long, no reload | 94 % → 95 % | 0.54 | 1.00 | 1591 | quarters: 0.54 → 0.54 → 0.53 → 0.50

Numbers say: the long stroke does not run out of paint.

## Brush Artist · Refs · #36 Magenta letters flat brush
Gouache · 36 px · 46.8 s

![Brush Artist · Refs · #36 Magenta letters flat brush](Brush-Artist-Refs-36-Magenta-letters-flat-brush.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 10 % → 10 % | 0.45 | 0.98 | 97 |
| heavy line | 17 % → 14 % | 0.45 | 0.85 | 138 |
| pressure swell | 13 % → 12 % | 0.45 | 0.89 | 95 |
| fast wave | 35 % → 19 % | 0.45 | 0.54 | 433 |
| slow wave | 35 % → 19 % | 0.45 | 0.54 | 494 |
| spiral | 46 % → 19 % | 0.45 | 0.42 | 502 |
| loop | 27 % → 20 % | 0.45 | 0.72 | 268 |
| tilted | 11 % → 11 % | 0.45 | 1.00 | 135 |
| over the wet one | 24 % → 23 % | 0.45 | 0.92 | 152 |
| long, no reload | 47 % → 19 % | 0.45 | 0.40 | 740 | quarters: 0.29 → 0.26 → 0.22 → 0.18

## Brush Artist · Refs · #37 Oil still life dabs
Oil · 26 px · 25.0 s

![Brush Artist · Refs · #37 Oil still life dabs](Brush-Artist-Refs-37-Oil-still-life-dabs.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 8 % → 8 % | 0.38 | 1.00 | 150 |
| heavy line | 9 % → 9 % | 0.38 | 1.00 | 120 |
| pressure swell | 7 % → 7 % | 0.39 | 1.00 | 93 |
| fast wave | 21 % → 21 % | 0.34 | 1.00 | 306 |
| slow wave | 21 % → 21 % | 0.35 | 1.00 | 617 |
| spiral | 34 % → 34 % | 0.27 | 1.00 | 496 |
| loop | 18 % → 18 % | 0.36 | 1.00 | 288 |
| tilted | 9 % → 9 % | 0.37 | 1.00 | 150 |
| over the wet one | 17 % → 17 % | 0.37 | 1.00 | 116 |
| long, no reload | 43 % → 43 % | 0.23 | 1.00 | 794 | quarters: 0.20 → 0.14 → 0.07 → 0.03

Numbers say: pressure barely changes the width.

## Brush Artist · Refs · #38 Sanguine drawing
Pastel · 6 px · 13.8 s

![Brush Artist · Refs · #38 Sanguine drawing](Brush-Artist-Refs-38-Sanguine-drawing.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 1 % → 1 % | 0.60 | 1.00 | 27 |
| heavy line | 2 % → 2 % | 0.61 | 1.00 | 25 |
| pressure swell | 1 % → 1 % | 0.61 | 1.00 | 27 |
| fast wave | 4 % → 4 % | 0.61 | 1.00 | 69 |
| slow wave | 4 % → 4 % | 0.61 | 1.00 | 68 |
| spiral | 7 % → 7 % | 0.61 | 1.00 | 104 |
| loop | 4 % → 4 % | 0.61 | 1.00 | 60 |
| tilted | 2 % → 2 % | 0.60 | 1.00 | 23 |
| over the wet one | 3 % → 3 % | 0.60 | 1.00 | 40 |
| long, no reload | 10 % → 10 % | 0.61 | 1.00 | 186 | quarters: 0.07 → 0.07 → 0.07 → 0.07

Numbers say: the long stroke does not run out of paint.

## Brush Artist · Refs · #39 Very thick impasto
Heavy acrylic · 60 px · 38.0 s

![Brush Artist · Refs · #39 Very thick impasto](Brush-Artist-Refs-39-Very-thick-impasto.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 20 % → 19 % | 0.61 | 0.97 | 250 |
| heavy line | 20 % → 20 % | 0.61 | 0.97 | 260 |
| pressure swell | 16 % → 15 % | 0.62 | 0.97 | 173 |
| fast wave | 48 % → 47 % | 0.62 | 0.98 | 602 |
| slow wave | 48 % → 47 % | 0.62 | 0.98 | 1196 |
| spiral | 69 % → 65 % | 0.62 | 0.93 | 1026 |
| loop | 42 % → 41 % | 0.62 | 0.97 | 752 |
| tilted | 16 % → 16 % | 0.62 | 1.00 | 416 |
| over the wet one | 34 % → 33 % | 0.62 | 0.97 | 270 |
| long, no reload | 85 % → 79 % | 0.62 | 0.93 | 1990 | quarters: 0.58 → 0.57 → 0.55 → 0.52

Numbers say: pressure barely changes the width; the long stroke does not run out of paint.

## Brush Artist · Refs · #40 Watercolour blooms
Watercolor · 90 px · 63.9 s

![Brush Artist · Refs · #40 Watercolour blooms](Brush-Artist-Refs-40-Watercolour-blooms.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 26 % → 27 % | 0.12 | 1.05 | 197 |
| heavy line | 38 % → 38 % | 0.11 | 0.99 | 384 |
| pressure swell | 25 % → 27 % | 0.12 | 1.06 | 251 |
| fast wave | 70 % → 74 % | 0.11 | 1.05 | 715 |
| slow wave | 68 % → 68 % | 0.15 | 1.00 | 1268 |
| spiral | 80 % → 80 % | 0.14 | 1.01 | 1511 |
| loop | 59 % → 59 % | 0.13 | 1.01 | 1126 |
| tilted | 27 % → 27 % | 0.13 | 1.00 | 661 |
| over the wet one | 55 % → 59 % | 0.13 | 1.07 | 269 |
| long, no reload | 98 % → 98 % | 0.14 | 1.01 | 2363 | quarters: 0.17 → 0.17 → 0.15 → 0.11

## Brush Artist · Refs · #41 Coloured pencil hatching
Pastel · 4 px · 15.3 s

![Brush Artist · Refs · #41 Coloured pencil hatching](Brush-Artist-Refs-41-Coloured-pencil-hatching.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 1 % → 1 % | 0.42 | 1.00 | 20 |
| heavy line | 2 % → 2 % | 0.43 | 1.00 | 18 |
| pressure swell | 1 % → 1 % | 0.43 | 1.00 | 10 |
| fast wave | 3 % → 3 % | 0.43 | 1.00 | 44 |
| slow wave | 3 % → 3 % | 0.42 | 1.00 | 48 |
| spiral | 5 % → 5 % | 0.43 | 1.00 | 67 |
| loop | 3 % → 3 % | 0.43 | 1.00 | 31 |
| tilted | 2 % → 2 % | 0.42 | 1.00 | 23 |
| over the wet one | 3 % → 3 % | 0.42 | 1.00 | 14 |
| long, no reload | 8 % → 8 % | 0.43 | 1.00 | 112 | quarters: 0.04 → 0.04 → 0.04 → 0.04

Numbers say: the long stroke does not run out of paint.

## Brush Artist · Refs · #42 Oil pastel shaggy
Pastel · 18 px · 13.7 s

![Brush Artist · Refs · #42 Oil pastel shaggy](Brush-Artist-Refs-42-Oil-pastel-shaggy.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 3 % → 3 % | 0.07 | 1.00 | 32 |
| heavy line | 5 % → 5 % | 0.07 | 1.00 | 50 |
| pressure swell | 4 % → 4 % | 0.07 | 1.00 | 24 |
| fast wave | 11 % → 11 % | 0.07 | 1.00 | 112 |
| slow wave | 10 % → 10 % | 0.07 | 1.00 | 174 |
| spiral | 17 % → 17 % | 0.07 | 1.00 | 260 |
| loop | 9 % → 9 % | 0.07 | 1.00 | 108 |
| tilted | 4 % → 4 % | 0.07 | 1.00 | 56 |
| over the wet one | 8 % → 8 % | 0.07 | 1.00 | 43 |
| long, no reload | 21 % → 21 % | 0.07 | 1.00 | 277 | quarters: 0.02 → 0.02 → 0.02 → 0.02

Numbers say: the long stroke does not run out of paint.

## Brush Artist · Refs · #43 Dragged black ink blocks
Gouache · 70 px · 40.8 s

![Brush Artist · Refs · #43 Dragged black ink blocks](Brush-Artist-Refs-43-Dragged-black-ink-blocks.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 19 % → 6 % | 0.57 | 0.32 | 208 |
| heavy line | 24 % → 9 % | 0.57 | 0.39 | 620 |
| pressure swell | 17 % → 9 % | 0.57 | 0.55 | 327 |
| fast wave | 52 % → 12 % | 0.57 | 0.23 | 608 |
| slow wave | 50 % → 10 % | 0.57 | 0.21 | 1110 |
| spiral | 64 % → 15 % | 0.57 | 0.23 | 1061 |
| loop | 45 % → 13 % | 0.57 | 0.29 | 468 |
| tilted | 17 % → 17 % | 0.57 | 0.98 | 278 |
| over the wet one | 37 % → 21 % | 0.57 | 0.57 | 227 |
| long, no reload | 82 % → 17 % | 0.57 | 0.21 | 1742 | quarters: 0.54 → 0.52 → 0.47 → 0.39

## Brush Artist · Refs · #44 Blue looping ribbon
Oil · 46 px · 27.3 s

![Brush Artist · Refs · #44 Blue looping ribbon](Brush-Artist-Refs-44-Blue-looping-ribbon.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 14 % → 14 % | 0.70 | 1.00 | 200 |
| heavy line | 15 % → 15 % | 0.70 | 1.00 | 171 |
| pressure swell | 12 % → 12 % | 0.72 | 1.00 | 117 |
| fast wave | 37 % → 37 % | 0.72 | 1.00 | 534 |
| slow wave | 37 % → 37 % | 0.72 | 1.00 | 679 |
| spiral | 63 % → 63 % | 0.71 | 1.00 | 726 |
| loop | 31 % → 31 % | 0.72 | 1.00 | 359 |
| tilted | 14 % → 14 % | 0.71 | 1.00 | 189 |
| over the wet one | 27 % → 27 % | 0.71 | 1.00 | 161 |
| long, no reload | 72 % → 72 % | 0.70 | 1.00 | 1382 | quarters: 0.59 → 0.57 → 0.54 → 0.48

Numbers say: pressure barely changes the width.

## Brush Artist · Refs · #45 Soft pastel pepper
Pastel · 30 px · 15.8 s

![Brush Artist · Refs · #45 Soft pastel pepper](Brush-Artist-Refs-45-Soft-pastel-pepper.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 5 % → 5 % | 0.53 | 1.00 | 79 |
| heavy line | 7 % → 7 % | 0.53 | 1.00 | 80 |
| pressure swell | 6 % → 6 % | 0.53 | 1.00 | 42 |
| fast wave | 17 % → 17 % | 0.53 | 1.00 | 154 |
| slow wave | 16 % → 16 % | 0.53 | 1.00 | 266 |
| spiral | 27 % → 27 % | 0.53 | 1.00 | 246 |
| loop | 13 % → 13 % | 0.53 | 1.00 | 121 |
| tilted | 5 % → 5 % | 0.53 | 1.00 | 89 |
| over the wet one | 11 % → 11 % | 0.53 | 1.00 | 95 |
| long, no reload | 32 % → 32 % | 0.53 | 1.00 | 399 | quarters: 0.19 → 0.19 → 0.19 → 0.19

Numbers say: the long stroke does not run out of paint.

## Brush Artist · Refs · #46 Red-brown ink lips
Watercolor · 70 px · 56.8 s

![Brush Artist · Refs · #46 Red-brown ink lips](Brush-Artist-Refs-46-Red-brown-ink-lips.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 20 % → 20 % | 0.54 | 1.01 | 196 |
| heavy line | 30 % → 30 % | 0.53 | 0.99 | 364 |
| pressure swell | 20 % → 20 % | 0.55 | 1.03 | 179 |
| fast wave | 60 % → 62 % | 0.53 | 1.04 | 833 |
| slow wave | 58 % → 58 % | 0.56 | 1.00 | 1114 |
| spiral | 74 % → 74 % | 0.55 | 1.00 | 924 |
| loop | 50 % → 50 % | 0.55 | 1.00 | 449 |
| tilted | 21 % → 22 % | 0.54 | 1.01 | 308 |
| over the wet one | 45 % → 47 % | 0.54 | 1.06 | 248 |
| long, no reload | 94 % → 95 % | 0.54 | 1.00 | 1283 | quarters: 0.56 → 0.55 → 0.54 → 0.49

Numbers say: the long stroke does not run out of paint.

## Brush Artist · Refs · #47 Pink knife slabs
Heavy acrylic · 90 px · 35.1 s

![Brush Artist · Refs · #47 Pink knife slabs](Brush-Artist-Refs-47-Pink-knife-slabs.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 32 % → 31 % | 0.18 | 0.99 | 105 |
| heavy line | 32 % → 31 % | 0.18 | 0.99 | 100 |
| pressure swell | 24 % → 25 % | 0.19 | 1.04 | 20 |
| fast wave | 66 % → 57 % | 0.17 | 0.86 | 209 |
| slow wave | 67 % → 59 % | 0.18 | 0.87 | 301 |
| spiral | 67 % → 41 % | 0.18 | 0.61 | 287 |
| loop | 60 % → 54 % | 0.18 | 0.89 | 194 |
| tilted | 20 % → 20 % | 0.18 | 1.00 | 58 |
| over the wet one | 48 % → 48 % | 0.18 | 1.00 | 91 |
| long, no reload | 94 % → 60 % | 0.17 | 0.64 | 463 | quarters: 0.18 → 0.15 → 0.11 → 0.07

Numbers say: pressure barely changes the width.

## Brush Artist · Refs · #48 Black bands with drips
Gouache · 70 px · 56.0 s

![Brush Artist · Refs · #48 Black bands with drips](Brush-Artist-Refs-48-Black-bands-with-drips.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 19 % → 18 % | 0.68 | 0.94 | 332 |
| heavy line | 29 % → 24 % | 0.68 | 0.85 | 537 |
| pressure swell | 23 % → 21 % | 0.68 | 0.92 | 438 |
| fast wave | 54 % → 37 % | 0.68 | 0.67 | 1086 |
| slow wave | 54 % → 36 % | 0.68 | 0.67 | 1241 |
| spiral | 64 % → 35 % | 0.68 | 0.54 | 1144 |
| loop | 45 % → 37 % | 0.68 | 0.82 | 848 |
| tilted | 19 % → 19 % | 0.68 | 1.00 | 414 |
| over the wet one | 41 % → 38 % | 0.68 | 0.92 | 325 |
| long, no reload | 74 % → 37 % | 0.68 | 0.50 | 1740 | quarters: 0.64 → 0.61 → 0.54 → 0.44

## Brush Artist · Refs · #49 Magenta letters round brush
Ink · 30 px · 35.9 s

![Brush Artist · Refs · #49 Magenta letters round brush](Brush-Artist-Refs-49-Magenta-letters-round-brush.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 6 % → 8 % | 0.50 | 1.29 | 72 |
| heavy line | 21 % → 21 % | 0.51 | 0.99 | 211 |
| pressure swell | 12 % → 13 % | 0.52 | 1.02 | 95 |
| fast wave | 39 % → 38 % | 0.51 | 0.99 | 231 |
| slow wave | 32 % → 31 % | 0.51 | 0.99 | 361 |
| spiral | 50 % → 49 % | 0.51 | 0.97 | 388 |
| loop | 29 % → 29 % | 0.51 | 1.00 | 232 |
| tilted | 11 % → 11 % | 0.52 | 1.01 | 94 |
| over the wet one | 26 % → 26 % | 0.52 | 1.01 | 74 |
| long, no reload | 62 % → 56 % | 0.50 | 0.91 | 543 | quarters: 0.41 → 0.36 → 0.30 → 0.25

## Brush Artist · Refs · #50 Thick swipes on photo
Heavy acrylic · 40 px · 20.3 s

![Brush Artist · Refs · #50 Thick swipes on photo](Brush-Artist-Refs-50-Thick-swipes-on-photo.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 13 % → 13 % | 0.06 | 0.96 | 186 |
| heavy line | 14 % → 13 % | 0.06 | 0.96 | 128 |
| pressure swell | 11 % → 10 % | 0.05 | 0.95 | 91 |
| fast wave | 33 % → 31 % | 0.04 | 0.93 | 397 |
| slow wave | 34 % → 32 % | 0.04 | 0.95 | 607 |
| spiral | 58 % → 46 % | 0.03 | 0.80 | 682 |
| loop | 28 % → 27 % | 0.04 | 0.95 | 302 |
| tilted | 12 % → 12 % | 0.05 | 1.00 | 140 |
| over the wet one | 25 % → 24 % | 0.05 | 0.95 | 114 |
| long, no reload | 66 % → 46 % | 0.04 | 0.69 | 705 | quarters: 0.04 → 0.02 → 0.02 → 0.02

Numbers say: pressure barely changes the width.

## Brush Artist · Ink — wash
Watercolor · 38 px · 44.0 s

![Brush Artist · Ink — wash](Brush-Artist-Ink-wash.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 11 % → 11 % | 0.39 | 1.03 | 72 |
| heavy line | 19 % → 19 % | 0.32 | 1.03 | 113 |
| pressure swell | 12 % → 13 % | 0.37 | 1.03 | 70 |
| fast wave | 40 % → 41 % | 0.31 | 1.04 | 230 |
| slow wave | 37 % → 38 % | 0.37 | 1.03 | 345 |
| spiral | 59 % → 61 % | 0.31 | 1.04 | 333 |
| loop | 32 % → 33 % | 0.35 | 1.02 | 155 |
| tilted | 13 % → 14 % | 0.38 | 1.04 | 105 |
| over the wet one | 29 % → 30 % | 0.38 | 1.04 | 116 |
| long, no reload | 67 % → 73 % | 0.29 | 1.09 | 607 | quarters: 0.34 → 0.27 → 0.19 → 0.12

## Brush Artist · Ink — brush line
Ink · 16 px · 35.3 s

![Brush Artist · Ink — brush line](Brush-Artist-Ink-brush-line.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 3 % → 5 % | 0.78 | 1.81 | 35 |
| heavy line | 13 % → 13 % | 0.88 | 0.99 | 82 |
| pressure swell | 8 % → 8 % | 0.87 | 1.05 | 69 |
| fast wave | 24 % → 23 % | 0.87 | 0.96 | 194 |
| slow wave | 20 % → 19 % | 0.87 | 0.97 | 205 |
| spiral | 30 % → 27 % | 0.86 | 0.89 | 283 |
| loop | 18 % → 18 % | 0.88 | 1.00 | 150 |
| tilted | 7 % → 7 % | 0.88 | 1.01 | 64 |
| over the wet one | 17 % → 17 % | 0.88 | 1.00 | 81 |
| long, no reload | 42 % → 30 % | 0.85 | 0.71 | 442 | quarters: 0.49 → 0.40 → 0.30 → 0.20

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Ink — dry brush
Gouache · 30 px · 29.0 s

![Brush Artist · Ink — dry brush](Brush-Artist-Ink-dry-brush.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 8 % → 1 % | 0.71 | 0.13 | 60 |
| heavy line | 10 % → 1 % | 0.71 | 0.11 | 177 |
| pressure swell | 7 % → 2 % | 0.71 | 0.23 | 99 |
| fast wave | 21 % → 2 % | 0.71 | 0.10 | 225 |
| slow wave | 21 % → 2 % | 0.71 | 0.09 | 424 |
| spiral | 31 % → 2 % | 0.71 | 0.07 | 435 |
| loop | 18 % → 2 % | 0.71 | 0.13 | 258 |
| tilted | 9 % → 8 % | 0.71 | 0.96 | 143 |
| over the wet one | 17 % → 4 % | 0.71 | 0.25 | 108 |
| long, no reload | 30 % → 3 % | 0.71 | 0.09 | 620 | quarters: 0.38 → 0.31 → 0.21 → 0.08

## Brush Artist · Watercolour — blue
Watercolor · 40 px · 41.6 s

![Brush Artist · Watercolour — blue](Brush-Artist-Watercolour-blue.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 6 % → 10 % | 0.43 | 1.78 | 44 |
| heavy line | 11 % → 13 % | 0.43 | 1.17 | 81 |
| pressure swell | 7 % → 9 % | 0.45 | 1.37 | 53 |
| fast wave | 24 % → 26 % | 0.41 | 1.09 | 235 |
| slow wave | 22 % → 28 % | 0.44 | 1.25 | 281 |
| spiral | 38 % → 42 % | 0.38 | 1.11 | 355 |
| loop | 19 % → 23 % | 0.44 | 1.17 | 184 |
| tilted | 12 % → 12 % | 0.44 | 1.01 | 126 |
| over the wet one | 21 % → 25 % | 0.44 | 1.17 | 94 |
| long, no reload | 51 % → 55 % | 0.37 | 1.06 | 937 | quarters: 0.32 → 0.24 → 0.19 → 0.15

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Watercolour — violet
Watercolor · 40 px · 41.3 s

![Brush Artist · Watercolour — violet](Brush-Artist-Watercolour-violet.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 6 % → 10 % | 0.42 | 1.78 | 47 |
| heavy line | 11 % → 13 % | 0.42 | 1.17 | 86 |
| pressure swell | 7 % → 9 % | 0.43 | 1.37 | 65 |
| fast wave | 24 % → 26 % | 0.41 | 1.09 | 301 |
| slow wave | 22 % → 28 % | 0.43 | 1.25 | 462 |
| spiral | 38 % → 42 % | 0.38 | 1.11 | 332 |
| loop | 19 % → 23 % | 0.43 | 1.17 | 229 |
| tilted | 12 % → 12 % | 0.43 | 1.01 | 127 |
| over the wet one | 21 % → 25 % | 0.43 | 1.17 | 95 |
| long, no reload | 51 % → 55 % | 0.37 | 1.06 | 488 | quarters: 0.30 → 0.24 → 0.19 → 0.16

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Watercolour — teal
Watercolor · 40 px · 40.1 s

![Brush Artist · Watercolour — teal](Brush-Artist-Watercolour-teal.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 6 % → 10 % | 0.30 | 1.78 | 58 |
| heavy line | 11 % → 13 % | 0.31 | 1.17 | 141 |
| pressure swell | 7 % → 9 % | 0.31 | 1.37 | 89 |
| fast wave | 24 % → 26 % | 0.30 | 1.09 | 223 |
| slow wave | 22 % → 28 % | 0.31 | 1.25 | 351 |
| spiral | 38 % → 42 % | 0.28 | 1.11 | 339 |
| loop | 19 % → 23 % | 0.31 | 1.17 | 169 |
| tilted | 12 % → 12 % | 0.31 | 1.01 | 127 |
| over the wet one | 21 % → 25 % | 0.31 | 1.17 | 73 |
| long, no reload | 51 % → 55 % | 0.27 | 1.06 | 689 | quarters: 0.22 → 0.18 → 0.14 → 0.11

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Gouache
Gouache · 30 px · 38.9 s

![Brush Artist · Gouache](Brush-Artist-Gouache.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 8 % → 8 % | 0.16 | 0.97 | 81 |
| heavy line | 15 % → 12 % | 0.16 | 0.78 | 99 |
| pressure swell | 11 % → 9 % | 0.16 | 0.85 | 71 |
| fast wave | 30 % → 14 % | 0.16 | 0.45 | 209 |
| slow wave | 29 % → 14 % | 0.16 | 0.47 | 566 |
| spiral | 40 % → 14 % | 0.16 | 0.35 | 479 |
| loop | 24 % → 15 % | 0.16 | 0.62 | 162 |
| tilted | 10 % → 10 % | 0.16 | 1.01 | 89 |
| over the wet one | 22 % → 19 % | 0.16 | 0.89 | 83 |
| long, no reload | 43 % → 15 % | 0.16 | 0.35 | 641 | quarters: 0.10 → 0.07 → 0.04 → 0.02

## Brush Artist · Oil — bristle
Oil · 30 px · 23.0 s

![Brush Artist · Oil — bristle](Brush-Artist-Oil-bristle.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 9 % → 9 % | 0.53 | 1.00 | 172 |
| heavy line | 9 % → 9 % | 0.53 | 1.00 | 198 |
| pressure swell | 7 % → 7 % | 0.54 | 1.00 | 118 |
| fast wave | 23 % → 23 % | 0.53 | 1.00 | 455 |
| slow wave | 23 % → 23 % | 0.53 | 1.00 | 528 |
| spiral | 36 % → 36 % | 0.50 | 1.00 | 542 |
| loop | 19 % → 19 % | 0.54 | 1.00 | 266 |
| tilted | 11 % → 11 % | 0.53 | 1.00 | 151 |
| over the wet one | 19 % → 19 % | 0.53 | 1.00 | 137 |
| long, no reload | 47 % → 47 % | 0.45 | 1.00 | 1899 | quarters: 0.31 → 0.27 → 0.22 → 0.14

Numbers say: pressure barely changes the width.

## Brush Artist · Charcoal — stick
Charcoal · 30 px · 13.9 s

![Brush Artist · Charcoal — stick](Brush-Artist-Charcoal-stick.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 7 % → 7 % | 0.84 | 1.00 | 39 |
| heavy line | 7 % → 7 % | 0.84 | 1.00 | 43 |
| pressure swell | 5 % → 5 % | 0.84 | 1.00 | 29 |
| fast wave | 17 % → 17 % | 0.84 | 1.00 | 59 |
| slow wave | 17 % → 17 % | 0.84 | 1.00 | 98 |
| spiral | 29 % → 29 % | 0.84 | 1.00 | 91 |
| loop | 14 % → 14 % | 0.84 | 1.00 | 48 |
| tilted | 6 % → 6 % | 0.84 | 1.00 | 32 |
| over the wet one | 13 % → 13 % | 0.84 | 1.00 | 32 |
| long, no reload | 37 % → 37 % | 0.84 | 1.00 | 145 | quarters: 0.35 → 0.34 → 0.34 → 0.35

Numbers say: pressure barely changes the width; the long stroke does not run out of paint.

## Brush Artist · Refs · #01 Henry Ward peach cloud — own sheet
own sheet 600 × 600 · Gouache · 44 px · 9.1 s

![Brush Artist · Refs · #01 Henry Ward peach cloud — own sheet](Brush-Artist-Refs-01-Henry-Ward-peach-cloud-own-sheet.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| stroke 1 | 33 % → 24 % | 0.10 | 0.72 | 239 |
| stroke 2 | 39 % → 32 % | 0.10 | 0.80 | 163 |
| stroke 3 | 43 % → 43 % | 0.10 | 1.00 | 150 |
| stroke 4 | 48 % → 43 % | 0.10 | 0.89 | 154 |
| stroke 5 | 39 % → 38 % | 0.10 | 0.96 | 157 |
| stroke 6 | 47 % → 35 % | 0.10 | 0.75 | 152 |
| stroke 7 | 63 % → 24 % | 0.10 | 0.37 | 1605 |

## Brush Artist · Refs · #02 Henry Ward cream strokes — own sheet
own sheet 600 × 600 · Gouache · 46 px · 8.7 s

![Brush Artist · Refs · #02 Henry Ward cream strokes — own sheet](Brush-Artist-Refs-02-Henry-Ward-cream-strokes-own-sheet.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| stroke 1 | 30 % → 15 % | 0.03 | 0.51 | 259 |
| stroke 2 | 34 % → 16 % | 0.03 | 0.48 | 230 |
| stroke 3 | 29 % → 20 % | 0.03 | 0.68 | 223 |
| stroke 4 | 35 % → 32 % | 0.03 | 0.93 | 326 |
| stroke 5 | 52 % → 31 % | 0.03 | 0.60 | 288 |
| stroke 6 | 33 % → 26 % | 0.03 | 0.79 | 506 |
| stroke 7 | 44 % → 25 % | 0.03 | 0.57 | 278 |

## Brush Artist · Refs · #03 Henry Ward navy contours — own sheet
own sheet 600 × 600 · Heavy acrylic · 22 px · 3.5 s

![Brush Artist · Refs · #03 Henry Ward navy contours — own sheet](Brush-Artist-Refs-03-Henry-Ward-navy-contours-own-sheet.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| stroke 1 | 15 % → 20 % | 0.75 | 1.28 | 170 |
| stroke 2 | 28 % → 30 % | 0.75 | 1.09 | 137 |
| stroke 3 | 28 % → 28 % | 0.75 | 0.99 | 149 |
| stroke 4 | 26 % → 24 % | 0.75 | 0.92 | 208 |

## Brush Artist · Refs · #04 Henry Ward grey cloud — own sheet
own sheet 600 × 600 · Gouache · 50 px · 6.2 s

![Brush Artist · Refs · #04 Henry Ward grey cloud — own sheet](Brush-Artist-Refs-04-Henry-Ward-grey-cloud-own-sheet.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| stroke 1 | 18 % → 5 % | 0.10 | 0.27 | 2372 |

## Brush Artist · Refs · #05 Henry Ward green in rust loops — own sheet
own sheet 600 × 600 · Heavy acrylic · 20 px · 2.9 s

![Brush Artist · Refs · #05 Henry Ward green in rust loops — own sheet](Brush-Artist-Refs-05-Henry-Ward-green-in-rust-loops-own-sheet.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| stroke 1 | 16 % → 24 % | 0.57 | 1.48 | 301 |
| stroke 2 | 15 % → 13 % | 0.58 | 0.90 | 246 |
| stroke 3 | 25 % → 24 % | 0.58 | 0.94 | 210 |

## Brush Artist · Refs · #06 Henry Ward scrubbed grey — own sheet
own sheet 600 × 600 · Gouache · 50 px · 6.2 s

![Brush Artist · Refs · #06 Henry Ward scrubbed grey — own sheet](Brush-Artist-Refs-06-Henry-Ward-scrubbed-grey-own-sheet.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| stroke 1 | 17 % → 4 % | 0.09 | 0.25 | 2270 |

## Brush Artist · Refs · #07 Henry Ward blue L + black zigzag — own sheet
own sheet 600 × 600 · Heavy acrylic · 34 px · 2.0 s

![Brush Artist · Refs · #07 Henry Ward blue L + black zigzag — own sheet](Brush-Artist-Refs-07-Henry-Ward-blue-L-black-zigzag-own-sheet.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| stroke 1 | 30 % → 31 % | 0.63 | 1.05 | 110 |
| stroke 2 | 31 % → 30 % | 0.63 | 0.94 | 81 |

## Brush Artist · Refs · #08 Henry Ward olive bands — own sheet
own sheet 600 × 600 · Gouache · 34 px · 6.7 s

![Brush Artist · Refs · #08 Henry Ward olive bands — own sheet](Brush-Artist-Refs-08-Henry-Ward-olive-bands-own-sheet.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| stroke 1 | 33 % → 19 % | 0.61 | 0.57 | 159 |
| stroke 2 | 37 % → 20 % | 0.61 | 0.52 | 182 |
| stroke 3 | 31 % → 23 % | 0.61 | 0.75 | 183 |
| stroke 4 | 38 % → 37 % | 0.61 | 0.98 | 254 |
| stroke 5 | 50 % → 35 % | 0.61 | 0.71 | 178 |
| stroke 6 | 36 % → 22 % | 0.61 | 0.61 | 231 |

## Brush Artist · Refs · #09 Henry Ward white loops — own sheet
own sheet 600 × 600 · Gouache · 46 px · 8.3 s

![Brush Artist · Refs · #09 Henry Ward white loops — own sheet](Brush-Artist-Refs-09-Henry-Ward-white-loops-own-sheet.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| stroke 1 | 46 % → 14 % | 0.02 | 0.29 | 1496 |
| stroke 2 | 49 % → 15 % | 0.02 | 0.31 | 1331 |
| stroke 3 | 57 % → 21 % | 0.02 | 0.37 | 1119 |

## Brush Artist · Refs · #10 Henry Ward maroon loops — own sheet
own sheet 600 × 600 · Heavy acrylic · 30 px · 3.5 s

![Brush Artist · Refs · #10 Henry Ward maroon loops — own sheet](Brush-Artist-Refs-10-Henry-Ward-maroon-loops-own-sheet.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| stroke 1 | 16 % → 33 % | 0.77 | 2.08 | 268 |
| stroke 2 | 29 % → 47 % | 0.77 | 1.60 | 127 |
| stroke 3 | 40 % → 50 % | 0.77 | 1.24 | 169 |
| stroke 4 | 45 % → 43 % | 0.77 | 0.96 | 123 |
| stroke 5 | 41 % → 38 % | 0.77 | 0.93 | 151 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #11 Henry Ward purple spun balls — own sheet
own sheet 600 × 600 · Heavy acrylic · 36 px · 3.5 s

![Brush Artist · Refs · #11 Henry Ward purple spun balls — own sheet](Brush-Artist-Refs-11-Henry-Ward-purple-spun-balls-own-sheet.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| stroke 1 | 35 % → 43 % | 0.79 | 1.23 | 366 |
| stroke 2 | 45 % → 52 % | 0.80 | 1.15 | 322 |
| stroke 3 | 45 % → 43 % | 0.80 | 0.96 | 455 |

## Brush Artist · Refs · #12 Henry Ward black-olive cage — own sheet
own sheet 600 × 600 · Gouache · 28 px · 6.1 s

![Brush Artist · Refs · #12 Henry Ward black-olive cage — own sheet](Brush-Artist-Refs-12-Henry-Ward-black-olive-cage-own-sheet.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| stroke 1 | 18 % → 22 % | 0.65 | 1.23 | 221 |
| stroke 2 | 16 % → 26 % | 0.65 | 1.60 | 180 |
| stroke 3 | 34 % → 34 % | 0.65 | 1.00 | 277 |
| stroke 4 | 34 % → 34 % | 0.65 | 1.02 | 138 |
| stroke 5 | 35 % → 21 % | 0.65 | 0.60 | 127 |
| stroke 6 | 52 % → 37 % | 0.65 | 0.72 | 162 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #13 Henry Ward blue streaky form — own sheet
own sheet 600 × 600 · Gouache · 50 px · 6.1 s

![Brush Artist · Refs · #13 Henry Ward blue streaky form — own sheet](Brush-Artist-Refs-13-Henry-Ward-blue-streaky-form-own-sheet.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| stroke 1 | 18 % → 5 % | 0.09 | 0.26 | 2004 |

## Brush Artist · Refs · #14 Henry Ward olive totem — own sheet
own sheet 600 × 600 · Heavy acrylic · 48 px · 3.7 s

![Brush Artist · Refs · #14 Henry Ward olive totem — own sheet](Brush-Artist-Refs-14-Henry-Ward-olive-totem-own-sheet.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| stroke 1 | 33 % → 14 % | 0.29 | 0.43 | 1437 |

## Brush Artist · Refs · #15 Ultramarine brush script — own sheet
own sheet 600 × 600 · Ink · 8 px · 7.4 s

![Brush Artist · Refs · #15 Ultramarine brush script — own sheet](Brush-Artist-Refs-15-Ultramarine-brush-script-own-sheet.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| stroke 1 | 54 % → 40 % | 0.45 | 0.73 | 721 |
| stroke 2 | 56 % → 39 % | 0.44 | 0.70 | 572 |
| stroke 3 | 59 % → 41 % | 0.46 | 0.70 | 384 |
| stroke 4 | 56 % → 41 % | 0.43 | 0.74 | 303 |
| stroke 5 | 54 % → 39 % | 0.45 | 0.73 | 324 |
| stroke 6 | 57 % → 44 % | 0.44 | 0.77 | 331 |

## Brush Artist · Refs · #18 Blue oil-stick scribbles — own sheet
own sheet 600 × 600 · Pastel · 10 px · 3.5 s

![Brush Artist · Refs · #18 Blue oil-stick scribbles — own sheet](Brush-Artist-Refs-18-Blue-oil-stick-scribbles-own-sheet.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| stroke 1 | 26 % → 49 % | 0.52 | 1.92 | 299 |
| stroke 2 | 22 % → 54 % | 0.52 | 2.43 | 278 |
| stroke 3 | 25 % → 39 % | 0.52 | 1.55 | 256 |
| stroke 4 | 23 % → 43 % | 0.52 | 1.85 | 232 |
| stroke 5 | 43 % → 49 % | 0.52 | 1.14 | 151 |
| stroke 6 | 40 % → 41 % | 0.52 | 1.02 | 135 |
| stroke 7 | 39 % → 48 % | 0.52 | 1.24 | 162 |
| stroke 8 | 44 % → 44 % | 0.52 | 1.00 | 174 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #20 Orange-red crayon scribble — own sheet
own sheet 600 × 600 · Pastel · 14 px · 2.8 s

![Brush Artist · Refs · #20 Orange-red crayon scribble — own sheet](Brush-Artist-Refs-20-Orange-red-crayon-scribble-own-sheet.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| stroke 1 | 12 % → 27 % | 0.53 | 2.26 | 189 |
| stroke 2 | 14 % → 34 % | 0.53 | 2.38 | 168 |
| stroke 3 | 21 % → 33 % | 0.53 | 1.57 | 161 |
| stroke 4 | 38 % → 47 % | 0.53 | 1.25 | 184 |
| stroke 5 | 43 % → 43 % | 0.53 | 1.00 | 171 |
| stroke 6 | 33 % → 33 % | 0.53 | 1.00 | 183 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #21 Gritty black contours — own sheet
own sheet 600 × 600 · Gouache · 12 px · 4.2 s

![Brush Artist · Refs · #21 Gritty black contours — own sheet](Brush-Artist-Refs-21-Gritty-black-contours-own-sheet.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| stroke 1 | 12 % → 9 % | 0.80 | 0.73 | 151 |
| stroke 2 | 10 % → 6 % | 0.80 | 0.61 | 172 |
| stroke 3 | 18 % → 5 % | 0.80 | 0.28 | 123 |
| stroke 4 | 19 % → 9 % | 0.80 | 0.47 | 128 |
| stroke 5 | 19 % → 10 % | 0.80 | 0.50 | 89 |

## Brush Artist · Refs · #22 Bold black brush poster — own sheet
own sheet 600 × 600 · Ink · 20 px · 5.0 s

![Brush Artist · Refs · #22 Bold black brush poster — own sheet](Brush-Artist-Refs-22-Bold-black-brush-poster-own-sheet.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| stroke 1 | 34 % → 37 % | 0.89 | 1.10 | 96 |
| stroke 2 | 55 % → 66 % | 0.89 | 1.21 | 23 |
| stroke 3 | 49 % → 49 % | 0.89 | 1.00 | 43 |
| stroke 4 | 36 % → 43 % | 0.89 | 1.20 | 52 |
| stroke 5 | 36 % → 36 % | 0.89 | 1.00 | 79 |

## Brush Artist · Refs · #23 Dry white on orange + black line — own sheet
own sheet 600 × 600 · Gouache · 50 px · 4.6 s

![Brush Artist · Refs · #23 Dry white on orange + black line — own sheet](Brush-Artist-Refs-23-Dry-white-on-orange-black-line-own-sheet.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| stroke 1 | 26 % → 4 % | 0.01 | 0.15 | 1662 |

## Brush Artist · Refs · #24 Picasso flat oil — own sheet
own sheet 600 × 600 · Oil · 34 px · 3.4 s

![Brush Artist · Refs · #24 Picasso flat oil — own sheet](Brush-Artist-Refs-24-Picasso-flat-oil-own-sheet.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| stroke 1 | 38 % → 38 % | 0.21 | 1.00 | 1202 |

## Brush Artist · Refs · #25 Yellow heavy flat stroke — own sheet
own sheet 600 × 600 · Heavy acrylic · 110 px · 3.1 s

![Brush Artist · Refs · #25 Yellow heavy flat stroke — own sheet](Brush-Artist-Refs-25-Yellow-heavy-flat-stroke-own-sheet.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| stroke 1 | 35 % → 35 % | 0.17 | 0.98 | 615 |

## Brush Artist · Refs · #27 Orange impasto swatch — own sheet
own sheet 600 × 600 · Heavy acrylic · 60 px · 3.8 s

![Brush Artist · Refs · #27 Orange impasto swatch — own sheet](Brush-Artist-Refs-27-Orange-impasto-swatch-own-sheet.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| stroke 1 | 23 % → 29 % | 0.37 | 1.29 | 94 |
| stroke 2 | 19 % → 40 % | 0.37 | 2.07 | 104 |
| stroke 3 | 26 % → 38 % | 0.37 | 1.48 | 53 |
| stroke 4 | 22 % → 22 % | 0.36 | 0.96 | 131 |
| stroke 5 | 32 % → 41 % | 0.36 | 1.28 | 131 |
| stroke 6 | 39 % → 40 % | 0.36 | 1.02 | 65 |
| stroke 7 | 19 % → 21 % | 0.36 | 1.11 | 67 |
| stroke 8 | 42 % → 40 % | 0.36 | 0.97 | 65 |
| stroke 9 | 49 % → 48 % | 0.37 | 0.97 | 117 |
| stroke 10 | 28 % → 27 % | 0.36 | 0.96 | 67 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #28 Miles Davis black lines — own sheet
own sheet 600 × 600 · Ink · 22 px · 6.9 s

![Brush Artist · Refs · #28 Miles Davis black lines — own sheet](Brush-Artist-Refs-28-Miles-Davis-black-lines-own-sheet.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| stroke 1 | 29 % → 37 % | 0.89 | 1.27 | 288 |
| stroke 2 | 37 % → 57 % | 0.89 | 1.52 | 289 |
| stroke 3 | 47 % → 48 % | 0.89 | 1.02 | 120 |
| stroke 4 | 50 % → 58 % | 0.89 | 1.16 | 246 |
| stroke 5 | 64 % → 64 % | 0.89 | 1.00 | 169 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #29 Shrigley magenta asterisk — own sheet
own sheet 600 × 600 · Watercolor · 70 px · 6.5 s

![Brush Artist · Refs · #29 Shrigley magenta asterisk — own sheet](Brush-Artist-Refs-29-Shrigley-magenta-asterisk-own-sheet.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| stroke 1 | 25 % → 44 % | 0.52 | 1.77 | 268 |
| stroke 2 | 17 % → 17 % | 0.51 | 1.00 | 249 |
| stroke 3 | 37 % → 44 % | 0.52 | 1.18 | 170 |
| stroke 4 | 33 % → 33 % | 0.51 | 1.02 | 176 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #30 Red gouache face patch — own sheet
own sheet 600 × 600 · Gouache · 60 px · 5.7 s

![Brush Artist · Refs · #30 Red gouache face patch — own sheet](Brush-Artist-Refs-30-Red-gouache-face-patch-own-sheet.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| stroke 1 | 38 % → 16 % | 0.49 | 0.42 | 1250 |

## Brush Artist · Refs · #31 Warhol blotted line — own sheet
own sheet 600 × 600 · Ink · 6 px · 4.6 s

![Brush Artist · Refs · #31 Warhol blotted line — own sheet](Brush-Artist-Refs-31-Warhol-blotted-line-own-sheet.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| stroke 1 | 24 % → 47 % | 0.83 | 1.93 | 125 |
| stroke 2 | 19 % → 24 % | 0.83 | 1.27 | 71 |
| stroke 3 | 27 % → 28 % | 0.82 | 1.02 | 76 |
| stroke 4 | 31 % → 41 % | 0.83 | 1.32 | 49 |
| stroke 5 | 38 % → 46 % | 0.83 | 1.21 | 73 |
| stroke 6 | 35 % → 36 % | 0.82 | 1.02 | 65 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #32 Thick orange swipes — own sheet
own sheet 600 × 600 · Heavy acrylic · 90 px · 3.6 s

![Brush Artist · Refs · #32 Thick orange swipes — own sheet](Brush-Artist-Refs-32-Thick-orange-swipes-own-sheet.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| stroke 1 | 28 % → 28 % | 0.39 | 1.00 | 292 |
| stroke 2 | 29 % → 32 % | 0.39 | 1.13 | 276 |
| stroke 3 | 32 % → 32 % | 0.39 | 0.98 | 268 |

## Brush Artist · Refs · #33 Red wet-in-wet band — own sheet
own sheet 600 × 600 · Watercolor · 80 px · 9.2 s

![Brush Artist · Refs · #33 Red wet-in-wet band — own sheet](Brush-Artist-Refs-33-Red-wet-in-wet-band-own-sheet.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| stroke 1 | 46 % → 65 % | 0.54 | 1.41 | 397 |
| stroke 2 | 53 % → 66 % | 0.54 | 1.26 | 106 |
| stroke 3 | 64 % → 78 % | 0.55 | 1.21 | 95 |
| stroke 4 | 66 % → 77 % | 0.54 | 1.16 | 87 |
| stroke 5 | 61 % → 74 % | 0.54 | 1.20 | 102 |
| stroke 6 | 64 % → 64 % | 0.54 | 1.00 | 105 |

## Brush Artist · Refs · #34 Magenta oil patches — own sheet
own sheet 600 × 600 · Oil · 60 px · 5.0 s

![Brush Artist · Refs · #34 Magenta oil patches — own sheet](Brush-Artist-Refs-34-Magenta-oil-patches-own-sheet.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| stroke 1 | 24 % → 44 % | 0.62 | 1.87 | 88 |
| stroke 2 | 22 % → 37 % | 0.62 | 1.69 | 70 |
| stroke 3 | 21 % → 51 % | 0.62 | 2.42 | 65 |
| stroke 4 | 31 % → 31 % | 0.62 | 1.00 | 62 |
| stroke 5 | 27 % → 40 % | 0.62 | 1.46 | 88 |
| stroke 6 | 27 % → 45 % | 0.62 | 1.66 | 60 |
| stroke 7 | 29 % → 41 % | 0.62 | 1.42 | 79 |
| stroke 8 | 52 % → 55 % | 0.62 | 1.07 | 213 |
| stroke 9 | 34 % → 38 % | 0.62 | 1.13 | 139 |
| stroke 10 | 48 % → 48 % | 0.62 | 1.00 | 100 |
| stroke 11 | 60 % → 60 % | 0.62 | 1.00 | 86 |
| stroke 12 | 35 % → 35 % | 0.62 | 1.00 | 94 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #35 Red band with runs — own sheet
own sheet 600 × 600 · Watercolor · 70 px · 5.2 s

![Brush Artist · Refs · #35 Red band with runs — own sheet](Brush-Artist-Refs-35-Red-band-with-runs-own-sheet.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| stroke 1 | 43 % → 43 % | 0.54 | 1.00 | 282 |

## Brush Artist · Refs · #36 Magenta letters flat brush — own sheet
own sheet 600 × 600 · Gouache · 36 px · 12.3 s

![Brush Artist · Refs · #36 Magenta letters flat brush — own sheet](Brush-Artist-Refs-36-Magenta-letters-flat-brush-own-sheet.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| stroke 1 | 46 % → 46 % | 0.50 | 1.00 | 32 |
| stroke 2 | 38 % → 48 % | 0.50 | 1.25 | 34 |
| stroke 3 | 56 % → 63 % | 0.50 | 1.12 | 29 |
| stroke 4 | 45 % → 53 % | 0.50 | 1.19 | 108 |
| stroke 5 | 41 % → 53 % | 0.50 | 1.29 | 67 |
| stroke 6 | 78 % → 76 % | 0.50 | 0.97 | 14 |
| stroke 7 | 43 % → 50 % | 0.50 | 1.15 | 104 |
| stroke 8 | 39 % → 59 % | 0.50 | 1.52 | 58 |
| stroke 9 | 54 % → 53 % | 0.50 | 0.98 | 38 |
| stroke 10 | 42 % → 61 % | 0.50 | 1.44 | 122 |
| stroke 11 | 78 % → 77 % | 0.50 | 0.98 | 34 |
| stroke 12 | 58 % → 68 % | 0.50 | 1.17 | 433 |
| stroke 13 | 43 % → 50 % | 0.50 | 1.18 | 67 |
| stroke 14 | 52 % → 73 % | 0.50 | 1.40 | 50 |
| stroke 15 | 44 % → 52 % | 0.50 | 1.18 | 108 |
| stroke 16 | 78 % → 76 % | 0.50 | 0.98 | 32 |
| stroke 17 | 53 % → 61 % | 0.50 | 1.15 | 190 |
| stroke 18 | 40 % → 47 % | 0.50 | 1.17 | 32 |
| stroke 19 | 65 % → 63 % | 0.50 | 0.97 | 32 |
| stroke 20 | 56 % → 55 % | 0.50 | 0.97 | 30 |
| stroke 21 | 47 % → 46 % | 0.50 | 0.96 | 109 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #37 Oil still life dabs — own sheet
own sheet 600 × 600 · Oil · 26 px · 4.4 s

![Brush Artist · Refs · #37 Oil still life dabs — own sheet](Brush-Artist-Refs-37-Oil-still-life-dabs-own-sheet.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| stroke 1 | 22 % → 22 % | 0.39 | 1.00 | 22 |
| stroke 2 | 20 % → 42 % | 0.40 | 2.04 | 15 |
| stroke 3 | 20 % → 31 % | 0.40 | 1.53 | 12 |
| stroke 4 | 23 % → 23 % | 0.40 | 1.00 | 24 |
| stroke 5 | 19 % → 19 % | 0.39 | 1.00 | 14 |
| stroke 6 | 42 % → 42 % | 0.40 | 1.01 | 19 |
| stroke 7 | 15 % → 19 % | 0.38 | 1.32 | 9 |
| stroke 8 | 16 % → 23 % | 0.39 | 1.46 | 9 |
| stroke 9 | 24 % → 24 % | 0.40 | 1.00 | 23 |
| stroke 10 | 25 % → 33 % | 0.39 | 1.33 | 24 |
| stroke 11 | 45 % → 45 % | 0.40 | 1.00 | 12 |
| stroke 12 | 25 % → 25 % | 0.38 | 1.00 | 20 |
| stroke 13 | 15 % → 15 % | 0.38 | 1.00 | 20 |
| stroke 14 | 27 % → 27 % | 0.39 | 1.00 | 20 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #38 Sanguine drawing — own sheet
own sheet 600 × 600 · Pastel · 6 px · 2.8 s

![Brush Artist · Refs · #38 Sanguine drawing — own sheet](Brush-Artist-Refs-38-Sanguine-drawing-own-sheet.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| stroke 1 | 5 % → 22 % | 0.61 | 4.30 | 21 |
| stroke 2 | 5 % → 11 % | 0.61 | 2.18 | 8 |
| stroke 3 | 5 % → 13 % | 0.61 | 2.67 | 13 |
| stroke 4 | 5 % → 30 % | 0.61 | 5.95 | 12 |
| stroke 5 | 5 % → 13 % | 0.61 | 2.56 | 19 |
| stroke 6 | 5 % → 31 % | 0.61 | 5.75 | 8 |
| stroke 7 | 8 % → 23 % | 0.61 | 2.82 | 11 |
| stroke 8 | 7 % → 24 % | 0.60 | 3.35 | 6 |
| stroke 9 | 5 % → 12 % | 0.61 | 2.27 | 11 |
| stroke 10 | 7 % → 26 % | 0.61 | 3.69 | 11 |
| stroke 11 | 5 % → 7 % | 0.61 | 1.48 | 7 |
| stroke 12 | 8 % → 25 % | 0.61 | 3.04 | 7 |
| stroke 13 | 13 % → 27 % | 0.61 | 2.02 | 10 |
| stroke 14 | 8 % → 22 % | 0.61 | 2.84 | 6 |
| stroke 15 | 16 % → 28 % | 0.61 | 1.75 | 12 |
| stroke 16 | 10 % → 25 % | 0.61 | 2.58 | 12 |
| stroke 17 | 7 % → 14 % | 0.61 | 2.05 | 11 |
| stroke 18 | 5 % → 9 % | 0.60 | 1.71 | 9 |
| stroke 19 | 10 % → 26 % | 0.61 | 2.72 | 7 |
| stroke 20 | 12 % → 22 % | 0.61 | 1.77 | 13 |
| stroke 21 | 7 % → 7 % | 0.61 | 1.00 | 7 |
| stroke 22 | 14 % → 21 % | 0.61 | 1.58 | 10 |
| stroke 23 | 11 % → 17 % | 0.61 | 1.54 | 10 |
| stroke 24 | 7 % → 11 % | 0.60 | 1.48 | 10 |
| stroke 25 | 13 % → 24 % | 0.61 | 1.86 | 12 |
| stroke 26 | 9 % → 12 % | 0.61 | 1.30 | 10 |
| stroke 27 | 7 % → 7 % | 0.60 | 1.04 | 12 |
| stroke 28 | 12 % → 19 % | 0.61 | 1.54 | 8 |
| stroke 29 | 13 % → 27 % | 0.61 | 2.17 | 11 |
| stroke 30 | 23 % → 28 % | 0.61 | 1.26 | 9 |
| stroke 31 | 9 % → 11 % | 0.61 | 1.21 | 10 |
| stroke 32 | 18 % → 21 % | 0.61 | 1.14 | 11 |
| stroke 33 | 12 % → 12 % | 0.61 | 1.05 | 8 |
| stroke 34 | 17 % → 22 % | 0.61 | 1.30 | 9 |
| stroke 35 | 15 % → 24 % | 0.61 | 1.56 | 12 |
| stroke 36 | 16 % → 21 % | 0.61 | 1.27 | 11 |
| stroke 37 | 17 % → 27 % | 0.61 | 1.57 | 9 |
| stroke 38 | 21 % → 32 % | 0.61 | 1.48 | 10 |
| stroke 39 | 23 % → 28 % | 0.61 | 1.20 | 6 |
| stroke 40 | 10 % → 11 % | 0.61 | 1.16 | 10 |
| stroke 41 | 26 % → 26 % | 0.61 | 1.00 | 11 |
| stroke 42 | 22 % → 26 % | 0.61 | 1.15 | 8 |
| stroke 43 | 17 % → 20 % | 0.61 | 1.17 | 12 |
| stroke 44 | 20 % → 24 % | 0.61 | 1.19 | 8 |
| stroke 45 | 5 % → 5 % | 0.61 | 1.00 | 10 |
| stroke 46 | 27 % → 27 % | 0.61 | 1.00 | 11 |
| stroke 47 | 22 % → 22 % | 0.61 | 1.00 | 12 |
| stroke 48 | 20 % → 21 % | 0.61 | 1.04 | 15 |
| stroke 49 | 31 % → 31 % | 0.61 | 1.00 | 9 |
| stroke 50 | 16 % → 16 % | 0.61 | 1.00 | 11 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #39 Very thick impasto — own sheet
own sheet 600 × 600 · Heavy acrylic · 60 px · 4.8 s

![Brush Artist · Refs · #39 Very thick impasto — own sheet](Brush-Artist-Refs-39-Very-thick-impasto-own-sheet.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| stroke 1 | 38 % → 37 % | 0.63 | 0.97 | 286 |
| stroke 2 | 37 % → 40 % | 0.63 | 1.08 | 268 |
| stroke 3 | 40 % → 39 % | 0.63 | 0.97 | 250 |
| stroke 4 | 39 % → 38 % | 0.63 | 0.97 | 279 |
| stroke 5 | 35 % → 34 % | 0.63 | 0.97 | 286 |

## Brush Artist · Refs · #40 Watercolour blooms — own sheet
own sheet 600 × 600 · Watercolor · 90 px · 6.2 s

![Brush Artist · Refs · #40 Watercolour blooms — own sheet](Brush-Artist-Refs-40-Watercolour-blooms-own-sheet.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| stroke 1 | 41 % → 41 % | 0.13 | 1.00 | 754 |

## Brush Artist · Refs · #41 Coloured pencil hatching — own sheet
own sheet 600 × 600 · Pastel · 4 px · 2.5 s

![Brush Artist · Refs · #41 Coloured pencil hatching — own sheet](Brush-Artist-Refs-41-Coloured-pencil-hatching-own-sheet.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| stroke 1 | 6 % → 22 % | 0.42 | 4.02 | 6 |
| stroke 2 | 6 % → 12 % | 0.42 | 2.09 | 6 |
| stroke 3 | 5 % → 18 % | 0.42 | 3.60 | 7 |
| stroke 4 | 6 % → 30 % | 0.43 | 5.26 | 5 |
| stroke 5 | 8 % → 11 % | 0.42 | 1.44 | 6 |
| stroke 6 | 6 % → 21 % | 0.43 | 3.59 | 5 |
| stroke 7 | 6 % → 24 % | 0.42 | 3.73 | 7 |
| stroke 8 | 6 % → 18 % | 0.42 | 3.29 | 5 |
| stroke 9 | 9 % → 18 % | 0.42 | 2.09 | 6 |
| stroke 10 | 8 % → 26 % | 0.42 | 3.18 | 8 |
| stroke 11 | 7 % → 21 % | 0.42 | 3.00 | 5 |
| stroke 12 | 5 % → 5 % | 0.41 | 1.00 | 10 |
| stroke 13 | 12 % → 26 % | 0.43 | 2.17 | 6 |
| stroke 14 | 6 % → 23 % | 0.42 | 4.07 | 6 |
| stroke 15 | 11 % → 20 % | 0.43 | 1.80 | 5 |
| stroke 16 | 12 % → 17 % | 0.42 | 1.47 | 5 |
| stroke 17 | 6 % → 6 % | 0.42 | 1.00 | 4 |
| stroke 18 | 8 % → 13 % | 0.43 | 1.55 | 6 |
| stroke 19 | 9 % → 21 % | 0.43 | 2.34 | 5 |
| stroke 20 | 9 % → 24 % | 0.42 | 2.78 | 7 |
| stroke 21 | 7 % → 24 % | 0.42 | 3.21 | 5 |
| stroke 22 | 16 % → 27 % | 0.42 | 1.72 | 4 |
| stroke 23 | 16 % → 22 % | 0.42 | 1.39 | 5 |
| stroke 24 | 11 % → 23 % | 0.42 | 2.09 | 6 |
| stroke 25 | 8 % → 16 % | 0.43 | 1.93 | 6 |
| stroke 26 | 6 % → 9 % | 0.42 | 1.36 | 5 |
| stroke 27 | 6 % → 12 % | 0.42 | 1.89 | 4 |
| stroke 28 | 9 % → 14 % | 0.42 | 1.62 | 4 |
| stroke 29 | 6 % → 22 % | 0.43 | 3.79 | 4 |
| stroke 30 | 10 % → 15 % | 0.42 | 1.45 | 4 |
| stroke 31 | 12 % → 24 % | 0.43 | 2.00 | 4 |
| stroke 32 | 6 % → 11 % | 0.43 | 1.85 | 4 |
| stroke 33 | 10 % → 17 % | 0.42 | 1.70 | 4 |
| stroke 34 | 6 % → 10 % | 0.43 | 1.49 | 4 |
| stroke 35 | 11 % → 22 % | 0.43 | 1.98 | 5 |
| stroke 36 | 9 % → 9 % | 0.43 | 1.00 | 4 |
| stroke 37 | 12 % → 23 % | 0.42 | 1.89 | 4 |
| stroke 38 | 13 % → 22 % | 0.42 | 1.61 | 4 |
| stroke 39 | 12 % → 19 % | 0.43 | 1.56 | 4 |
| stroke 40 | 12 % → 27 % | 0.43 | 2.16 | 6 |
| stroke 41 | 15 % → 20 % | 0.43 | 1.37 | 4 |
| stroke 42 | 16 % → 26 % | 0.43 | 1.68 | 4 |
| stroke 43 | 9 % → 14 % | 0.42 | 1.65 | 4 |
| stroke 44 | 17 % → 23 % | 0.42 | 1.32 | 4 |
| stroke 45 | 21 % → 28 % | 0.42 | 1.32 | 4 |
| stroke 46 | 9 % → 11 % | 0.42 | 1.29 | 4 |
| stroke 47 | 18 % → 21 % | 0.42 | 1.20 | 4 |
| stroke 48 | 19 % → 25 % | 0.43 | 1.33 | 4 |
| stroke 49 | 9 % → 16 % | 0.42 | 1.73 | 4 |
| stroke 50 | 12 % → 12 % | 0.42 | 1.00 | 4 |
| stroke 51 | 16 % → 27 % | 0.42 | 1.72 | 4 |
| stroke 52 | 20 % → 24 % | 0.42 | 1.19 | 4 |
| stroke 53 | 17 % → 23 % | 0.43 | 1.34 | 4 |
| stroke 54 | 16 % → 24 % | 0.43 | 1.52 | 4 |
| stroke 55 | 17 % → 22 % | 0.43 | 1.29 | 4 |
| stroke 56 | 18 % → 20 % | 0.43 | 1.09 | 4 |
| stroke 57 | 17 % → 23 % | 0.42 | 1.35 | 6 |
| stroke 58 | 18 % → 21 % | 0.42 | 1.12 | 4 |
| stroke 59 | 19 % → 22 % | 0.43 | 1.15 | 4 |
| stroke 60 | 25 % → 31 % | 0.43 | 1.24 | 4 |
| stroke 61 | 31 % → 32 % | 0.43 | 1.03 | 4 |
| stroke 62 | 17 % → 17 % | 0.42 | 1.00 | 5 |
| stroke 63 | 18 % → 19 % | 0.43 | 1.09 | 4 |
| stroke 64 | 25 % → 26 % | 0.42 | 1.02 | 4 |
| stroke 65 | 27 % → 27 % | 0.42 | 1.00 | 4 |
| stroke 66 | 23 % → 23 % | 0.42 | 1.00 | 4 |
| stroke 67 | 20 % → 21 % | 0.42 | 1.03 | 4 |
| stroke 68 | 8 % → 15 % | 0.42 | 1.83 | 4 |
| stroke 69 | 10 % → 10 % | 0.42 | 1.00 | 4 |
| stroke 70 | 17 % → 21 % | 0.43 | 1.26 | 4 |
| stroke 71 | 15 % → 18 % | 0.42 | 1.19 | 4 |
| stroke 72 | 10 % → 12 % | 0.42 | 1.17 | 4 |
| stroke 73 | 22 % → 22 % | 0.42 | 1.00 | 4 |
| stroke 74 | 24 % → 24 % | 0.43 | 1.00 | 5 |
| stroke 75 | 25 % → 25 % | 0.42 | 1.00 | 4 |
| stroke 76 | 21 % → 21 % | 0.43 | 1.00 | 4 |
| stroke 77 | 11 % → 16 % | 0.42 | 1.38 | 4 |
| stroke 78 | 17 % → 17 % | 0.42 | 1.00 | 4 |
| stroke 79 | 13 % → 13 % | 0.42 | 1.00 | 4 |
| stroke 80 | 18 % → 18 % | 0.42 | 1.00 | 4 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #42 Oil pastel shaggy — own sheet
own sheet 600 × 600 · Pastel · 18 px · 2.5 s

![Brush Artist · Refs · #42 Oil pastel shaggy — own sheet](Brush-Artist-Refs-42-Oil-pastel-shaggy-own-sheet.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| stroke 1 | 13 % → 28 % | 0.07 | 2.12 | 10 |
| stroke 2 | 15 % → 35 % | 0.07 | 2.34 | 9 |
| stroke 3 | 15 % → 44 % | 0.07 | 2.94 | 9 |
| stroke 4 | 15 % → 28 % | 0.07 | 1.95 | 9 |
| stroke 5 | 17 % → 29 % | 0.07 | 1.72 | 9 |
| stroke 6 | 15 % → 41 % | 0.07 | 2.70 | 9 |
| stroke 7 | 22 % → 53 % | 0.07 | 2.47 | 9 |
| stroke 8 | 16 % → 59 % | 0.07 | 3.60 | 12 |
| stroke 9 | 19 % → 31 % | 0.07 | 1.66 | 9 |
| stroke 10 | 15 % → 28 % | 0.07 | 1.82 | 9 |
| stroke 11 | 15 % → 38 % | 0.07 | 2.57 | 9 |
| stroke 12 | 20 % → 27 % | 0.07 | 1.38 | 9 |
| stroke 13 | 26 % → 41 % | 0.07 | 1.57 | 10 |
| stroke 14 | 14 % → 29 % | 0.07 | 2.09 | 9 |
| stroke 15 | 15 % → 46 % | 0.07 | 3.08 | 9 |
| stroke 16 | 22 % → 43 % | 0.08 | 1.90 | 9 |
| stroke 17 | 31 % → 53 % | 0.07 | 1.71 | 9 |
| stroke 18 | 32 % → 44 % | 0.08 | 1.35 | 9 |
| stroke 19 | 31 % → 54 % | 0.07 | 1.73 | 9 |
| stroke 20 | 34 % → 56 % | 0.07 | 1.66 | 11 |
| stroke 21 | 20 % → 27 % | 0.07 | 1.35 | 9 |
| stroke 22 | 20 % → 23 % | 0.07 | 1.15 | 10 |
| stroke 23 | 27 % → 34 % | 0.07 | 1.28 | 9 |
| stroke 24 | 38 % → 44 % | 0.08 | 1.14 | 9 |
| stroke 25 | 30 % → 45 % | 0.07 | 1.52 | 9 |
| stroke 26 | 15 % → 31 % | 0.07 | 2.00 | 9 |
| stroke 27 | 40 % → 44 % | 0.08 | 1.11 | 9 |
| stroke 28 | 27 % → 42 % | 0.07 | 1.55 | 9 |
| stroke 29 | 15 % → 38 % | 0.07 | 2.46 | 9 |
| stroke 30 | 19 % → 49 % | 0.07 | 2.59 | 9 |
| stroke 31 | 23 % → 24 % | 0.07 | 1.01 | 9 |
| stroke 32 | 29 % → 44 % | 0.07 | 1.55 | 10 |
| stroke 33 | 28 % → 28 % | 0.07 | 1.02 | 9 |
| stroke 34 | 41 % → 48 % | 0.07 | 1.16 | 9 |
| stroke 35 | 41 % → 51 % | 0.07 | 1.25 | 9 |
| stroke 36 | 36 % → 38 % | 0.07 | 1.05 | 9 |
| stroke 37 | 29 % → 29 % | 0.07 | 1.00 | 9 |
| stroke 38 | 39 % → 47 % | 0.07 | 1.22 | 11 |
| stroke 39 | 23 % → 36 % | 0.07 | 1.59 | 9 |
| stroke 40 | 48 % → 56 % | 0.07 | 1.18 | 9 |
| stroke 41 | 44 % → 47 % | 0.07 | 1.05 | 9 |
| stroke 42 | 29 % → 39 % | 0.07 | 1.33 | 9 |
| stroke 43 | 21 % → 21 % | 0.07 | 1.00 | 9 |
| stroke 44 | 41 % → 52 % | 0.07 | 1.27 | 9 |
| stroke 45 | 36 % → 36 % | 0.07 | 1.00 | 9 |
| stroke 46 | 53 % → 57 % | 0.07 | 1.09 | 9 |
| stroke 47 | 54 % → 60 % | 0.07 | 1.11 | 9 |
| stroke 48 | 35 % → 39 % | 0.07 | 1.11 | 9 |
| stroke 49 | 41 % → 44 % | 0.07 | 1.06 | 9 |
| stroke 50 | 53 % → 56 % | 0.07 | 1.05 | 9 |
| stroke 51 | 27 % → 27 % | 0.07 | 1.00 | 9 |
| stroke 52 | 48 % → 48 % | 0.07 | 1.00 | 11 |
| stroke 53 | 32 % → 33 % | 0.07 | 1.02 | 9 |
| stroke 54 | 36 % → 39 % | 0.07 | 1.09 | 9 |
| stroke 55 | 23 % → 23 % | 0.07 | 1.00 | 9 |
| stroke 56 | 29 % → 29 % | 0.07 | 1.00 | 9 |
| stroke 57 | 45 % → 45 % | 0.08 | 1.00 | 10 |
| stroke 58 | 40 % → 40 % | 0.07 | 1.00 | 12 |
| stroke 59 | 65 % → 65 % | 0.07 | 1.00 | 9 |
| stroke 60 | 25 % → 25 % | 0.07 | 1.00 | 9 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #43 Dragged black ink blocks — own sheet
own sheet 600 × 600 · Gouache · 70 px · 8.0 s

![Brush Artist · Refs · #43 Dragged black ink blocks — own sheet](Brush-Artist-Refs-43-Dragged-black-ink-blocks-own-sheet.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| stroke 1 | 46 % → 29 % | 0.64 | 0.62 | 377 |
| stroke 2 | 35 % → 22 % | 0.64 | 0.62 | 406 |
| stroke 3 | 36 % → 25 % | 0.64 | 0.70 | 398 |
| stroke 4 | 39 % → 24 % | 0.64 | 0.60 | 405 |
| stroke 5 | 44 % → 29 % | 0.64 | 0.66 | 411 |

## Brush Artist · Refs · #44 Blue looping ribbon — own sheet
own sheet 600 × 600 · Oil · 46 px · 4.0 s

![Brush Artist · Refs · #44 Blue looping ribbon — own sheet](Brush-Artist-Refs-44-Blue-looping-ribbon-own-sheet.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| stroke 1 | 44 % → 44 % | 0.72 | 1.00 | 1246 |

## Brush Artist · Refs · #45 Soft pastel pepper — own sheet
own sheet 600 × 600 · Pastel · 30 px · 2.7 s

![Brush Artist · Refs · #45 Soft pastel pepper — own sheet](Brush-Artist-Refs-45-Soft-pastel-pepper-own-sheet.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| stroke 1 | 17 % → 36 % | 0.53 | 2.08 | 226 |
| stroke 2 | 29 % → 41 % | 0.53 | 1.44 | 211 |
| stroke 3 | 38 % → 48 % | 0.53 | 1.26 | 209 |
| stroke 4 | 36 % → 41 % | 0.53 | 1.13 | 216 |
| stroke 5 | 41 % → 41 % | 0.53 | 1.00 | 148 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #46 Red-brown ink lips — own sheet
own sheet 600 × 600 · Watercolor · 70 px · 5.3 s

![Brush Artist · Refs · #46 Red-brown ink lips — own sheet](Brush-Artist-Refs-46-Red-brown-ink-lips-own-sheet.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| stroke 1 | 32 % → 45 % | 0.55 | 1.43 | 185 |
| stroke 2 | 48 % → 48 % | 0.55 | 1.00 | 160 |

## Brush Artist · Refs · #47 Pink knife slabs — own sheet
own sheet 600 × 600 · Heavy acrylic · 90 px · 5.1 s

![Brush Artist · Refs · #47 Pink knife slabs — own sheet](Brush-Artist-Refs-47-Pink-knife-slabs-own-sheet.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| stroke 1 | 32 % → 39 % | 0.19 | 1.23 | 42 |
| stroke 2 | 41 % → 49 % | 0.19 | 1.17 | 43 |
| stroke 3 | 41 % → 49 % | 0.19 | 1.18 | 40 |
| stroke 4 | 43 % → 42 % | 0.19 | 0.99 | 45 |

## Brush Artist · Refs · #48 Black bands with drips — own sheet
own sheet 600 × 600 · Gouache · 70 px · 10.6 s

![Brush Artist · Refs · #48 Black bands with drips — own sheet](Brush-Artist-Refs-48-Black-bands-with-drips-own-sheet.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| stroke 1 | 33 % → 31 % | 0.80 | 0.91 | 596 |
| stroke 2 | 35 % → 32 % | 0.80 | 0.92 | 542 |
| stroke 3 | 33 % → 31 % | 0.80 | 0.93 | 422 |
| stroke 4 | 33 % → 32 % | 0.80 | 0.95 | 412 |

## Brush Artist · Refs · #49 Magenta letters round brush — own sheet
own sheet 600 × 600 · Ink · 30 px · 10.0 s

![Brush Artist · Refs · #49 Magenta letters round brush — own sheet](Brush-Artist-Refs-49-Magenta-letters-round-brush-own-sheet.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| stroke 1 | 61 % → 65 % | 0.52 | 1.06 | 33 |
| stroke 2 | 59 % → 64 % | 0.53 | 1.07 | 38 |
| stroke 3 | 71 % → 80 % | 0.53 | 1.13 | 42 |
| stroke 4 | 54 % → 64 % | 0.52 | 1.18 | 110 |
| stroke 5 | 48 % → 65 % | 0.52 | 1.35 | 67 |
| stroke 6 | 93 % → 94 % | 0.53 | 1.01 | 14 |
| stroke 7 | 61 % → 70 % | 0.52 | 1.15 | 110 |
| stroke 8 | 44 % → 72 % | 0.53 | 1.61 | 63 |
| stroke 9 | 71 % → 71 % | 0.53 | 1.00 | 26 |
| stroke 10 | 51 % → 72 % | 0.52 | 1.42 | 64 |
| stroke 11 | 93 % → 94 % | 0.53 | 1.01 | 15 |
| stroke 12 | 71 % → 83 % | 0.52 | 1.18 | 104 |
| stroke 13 | 61 % → 65 % | 0.53 | 1.05 | 30 |
| stroke 14 | 69 % → 92 % | 0.53 | 1.33 | 30 |
| stroke 15 | 52 % → 63 % | 0.52 | 1.20 | 65 |
| stroke 16 | 93 % → 93 % | 0.53 | 1.00 | 19 |
| stroke 17 | 68 % → 76 % | 0.52 | 1.12 | 102 |
| stroke 18 | 59 % → 62 % | 0.52 | 1.05 | 29 |
| stroke 19 | 81 % → 80 % | 0.53 | 0.99 | 28 |
| stroke 20 | 71 % → 70 % | 0.52 | 1.00 | 27 |
| stroke 21 | 60 % → 59 % | 0.52 | 1.00 | 78 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Refs · #50 Thick swipes on photo — own sheet
own sheet 600 × 600 · Heavy acrylic · 40 px · 2.8 s

![Brush Artist · Refs · #50 Thick swipes on photo — own sheet](Brush-Artist-Refs-50-Thick-swipes-on-photo-own-sheet.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| stroke 1 | 24 % → 27 % | 0.06 | 1.12 | 51 |
| stroke 2 | 21 % → 28 % | 0.06 | 1.33 | 36 |
| stroke 3 | 26 % → 24 % | 0.06 | 0.95 | 42 |
| stroke 4 | 26 % → 24 % | 0.06 | 0.94 | 31 |
| stroke 5 | 24 % → 22 % | 0.06 | 0.95 | 33 |
| stroke 6 | 21 % → 19 % | 0.06 | 0.94 | 24 |
| stroke 7 | 36 % → 37 % | 0.06 | 1.02 | 48 |
| stroke 8 | 34 % → 33 % | 0.06 | 0.97 | 30 |
| stroke 9 | 25 % → 23 % | 0.06 | 0.95 | 39 |
| stroke 10 | 28 % → 27 % | 0.06 | 0.95 | 38 |
| stroke 11 | 23 % → 21 % | 0.06 | 0.95 | 33 |
| stroke 12 | 24 % → 23 % | 0.05 | 0.95 | 18 |

## Brush Artist · Ink — dry brush — own sheet
own sheet 600 × 600 · Gouache · 30 px · 2.9 s

![Brush Artist · Ink — dry brush — own sheet](Brush-Artist-Ink-dry-brush-own-sheet.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| ear | 17 % → 4 % | 0.77 | 0.25 | 480 |
| drag0 | 20 % → 24 % | 0.77 | 1.21 | 122 |
| drag1 | 25 % → 25 % | 0.77 | 1.01 | 105 |
| drag2 | 28 % → 26 % | 0.77 | 0.92 | 88 |
| drag3 | 30 % → 26 % | 0.77 | 0.87 | 71 |

