![All brushes](contact.png)

# Brush Lab — 42 brushes · Nov 3, 2026 at 12:05 AM

Every sheet: 1500 × 600, ten strokes in a 5 × 2 grid — 1. light line · 2. heavy line · 3. pressure swell · 4. fast wave · 5. slow wave · 6. spiral · 7. loop · 8. tilted · 9. over the wet one · 10. long, no reload (cell 8 holds «tilted» and «over the wet one» crossed). The CPU reference of Mamay's paint engine; the wet layer settles 20 s at the end.

Columns: **covered** = share of the cell with paint right after the stroke → after settling; **dark** = mean darkness of the painted pixels above the paper's own grain (0 = paper, 1 = black); **spread** = how far wet paint went beyond the stroke (1.0 = stayed); **ms** = the stroke on the CPU; long stroke: paint in each quarter of its length (it should run out: wet → streaks → dry tail).

## Ink Line
Ink · 12 px · 27.5 s

![Ink Line](Ink-Line.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 1 % → 4 % | 0.55 | 2.44 | 56 |
| heavy line | 5 % → 6 % | 0.68 | 1.13 | 66 |
| pressure swell | 3 % → 4 % | 0.64 | 1.40 | 41 |
| fast wave | 10 % → 11 % | 0.59 | 1.11 | 162 |
| slow wave | 8 % → 10 % | 0.57 | 1.16 | 159 |
| spiral | 14 % → 15 % | 0.50 | 1.07 | 222 |
| loop | 8 % → 9 % | 0.61 | 1.16 | 112 |
| tilted | 5 % → 5 % | 0.65 | 1.05 | 57 |
| over the wet one | 10 % → 11 % | 0.65 | 1.15 | 51 |
| long, no reload | 18 % → 17 % | 0.47 | 0.96 | 317 | quarters: 0.22 → 0.09 → 0.04 → 0.02

Numbers say: wet paint spreads well beyond the stroke.

## Dense Ink
Ink · 14 px · 28.7 s

![Dense Ink](Dense-Ink.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 5 % → 7 % | 0.72 | 1.26 | 70 |
| heavy line | 7 % → 7 % | 0.73 | 1.09 | 82 |
| pressure swell | 5 % → 6 % | 0.72 | 1.17 | 52 |
| fast wave | 13 % → 13 % | 0.69 | 1.01 | 165 |
| slow wave | 12 % → 12 % | 0.67 | 1.04 | 212 |
| spiral | 18 % → 15 % | 0.65 | 0.80 | 255 |
| loop | 11 % → 12 % | 0.69 | 1.08 | 128 |
| tilted | 5 % → 6 % | 0.72 | 1.07 | 66 |
| over the wet one | 12 % → 13 % | 0.72 | 1.11 | 60 |
| long, no reload | 23 % → 15 % | 0.64 | 0.66 | 346 | quarters: 0.30 → 0.12 → 0.04 → 0.02

## Transparent Wash
Watercolor · 22 px · 29.9 s

![Transparent Wash](Transparent-Wash.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 2 % → 5 % | 0.27 | 2.25 | 59 |
| heavy line | 7 % → 9 % | 0.27 | 1.22 | 62 |
| pressure swell | 4 % → 6 % | 0.28 | 1.54 | 40 |
| fast wave | 14 % → 16 % | 0.20 | 1.17 | 166 |
| slow wave | 12 % → 15 % | 0.21 | 1.28 | 241 |
| spiral | 18 % → 22 % | 0.16 | 1.23 | 191 |
| loop | 11 % → 13 % | 0.22 | 1.20 | 101 |
| tilted | 8 % → 8 % | 0.24 | 1.06 | 73 |
| over the wet one | 13 % → 16 % | 0.24 | 1.18 | 55 |
| long, no reload | 26 % → 32 % | 0.13 | 1.22 | 299 | quarters: 0.11 → 0.04 → 0.02 → 0.01

Numbers say: wet paint spreads well beyond the stroke.

## Dry Brush
Gouache · 24 px · 22.5 s

![Dry Brush](Dry-Brush.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 5 % → 0 % | 0.65 | 0.09 | 71 |
| heavy line | 6 % → 0 % | 0.65 | 0.02 | 119 |
| pressure swell | 5 % → 0 % | 0.65 | 0.08 | 54 |
| fast wave | 6 % → 1 % | 0.65 | 0.08 | 158 |
| slow wave | 7 % → 0 % | 0.65 | 0.06 | 257 |
| spiral | 7 % → 0 % | 0.65 | 0.07 | 292 |
| loop | 10 % → 0 % | 0.65 | 0.04 | 141 |
| tilted | 4 % → 3 % | 0.65 | 0.88 | 93 |
| over the wet one | 9 % → 1 % | 0.65 | 0.12 | 80 |
| long, no reload | 6 % → 1 % | 0.65 | 0.14 | 392 | quarters: 0.12 → 0.00 → 0.00 → 0.00

## Wax Crayon
Wax · 8 px · 10.0 s

![Wax Crayon](Wax-Crayon.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 1 % → 1 % | 0.71 | 1.00 | 21 |
| heavy line | 1 % → 1 % | 0.69 | 1.00 | 30 |
| pressure swell | 1 % → 1 % | 0.70 | 1.00 | 15 |
| fast wave | 3 % → 3 % | 0.69 | 1.00 | 62 |
| slow wave | 3 % → 3 % | 0.70 | 1.00 | 43 |
| spiral | 5 % → 5 % | 0.70 | 1.00 | 78 |
| loop | 3 % → 3 % | 0.70 | 1.00 | 47 |
| tilted | 2 % → 2 % | 0.68 | 1.00 | 31 |
| over the wet one | 3 % → 3 % | 0.68 | 1.00 | 17 |
| long, no reload | 7 % → 7 % | 0.70 | 1.00 | 122 | quarters: 0.06 → 0.06 → 0.06 → 0.06

Numbers say: the long stroke does not run out of paint.

## Oil Pastel
Wax · 12 px · 10.2 s

![Oil Pastel](Oil-Pastel.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 1 % → 1 % | 0.68 | 1.00 | 24 |
| heavy line | 2 % → 2 % | 0.68 | 1.00 | 30 |
| pressure swell | 2 % → 2 % | 0.69 | 1.00 | 21 |
| fast wave | 5 % → 5 % | 0.68 | 1.00 | 69 |
| slow wave | 5 % → 5 % | 0.68 | 1.00 | 61 |
| spiral | 8 % → 8 % | 0.68 | 1.00 | 108 |
| loop | 4 % → 4 % | 0.68 | 1.00 | 59 |
| tilted | 2 % → 2 % | 0.68 | 1.00 | 44 |
| over the wet one | 5 % → 5 % | 0.68 | 1.00 | 25 |
| long, no reload | 13 % → 13 % | 0.68 | 1.00 | 162 | quarters: 0.10 → 0.09 → 0.10 → 0.10

Numbers say: the long stroke does not run out of paint.

## Charcoal
Charcoal · 5 px · 12.0 s

![Charcoal](Charcoal.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 1 % → 1 % | 0.74 | 1.00 | 13 |
| heavy line | 1 % → 1 % | 0.74 | 1.00 | 18 |
| pressure swell | 1 % → 1 % | 0.74 | 1.00 | 18 |
| fast wave | 2 % → 2 % | 0.73 | 1.00 | 30 |
| slow wave | 2 % → 2 % | 0.74 | 1.00 | 48 |
| spiral | 4 % → 4 % | 0.74 | 1.00 | 80 |
| loop | 2 % → 2 % | 0.74 | 1.00 | 31 |
| tilted | 2 % → 2 % | 0.72 | 1.00 | 34 |
| over the wet one | 2 % → 2 % | 0.72 | 1.00 | 14 |
| long, no reload | 6 % → 6 % | 0.73 | 1.00 | 93 | quarters: 0.05 → 0.05 → 0.05 → 0.05

Numbers say: the long stroke does not run out of paint.

## Impasto
Heavy acrylic · 22 px · 18.3 s

![Impasto](Impasto.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 8 % → 8 % | 0.71 | 0.93 | 73 |
| heavy line | 10 % → 9 % | 0.70 | 0.94 | 165 |
| pressure swell | 7 % → 7 % | 0.72 | 0.94 | 82 |
| fast wave | 20 % → 13 % | 0.71 | 0.64 | 211 |
| slow wave | 21 % → 14 % | 0.71 | 0.66 | 266 |
| spiral | 30 % → 14 % | 0.71 | 0.46 | 323 |
| loop | 18 % → 14 % | 0.71 | 0.77 | 231 |
| tilted | 8 % → 8 % | 0.70 | 1.00 | 169 |
| over the wet one | 17 % → 15 % | 0.70 | 0.91 | 137 |
| long, no reload | 34 % → 14 % | 0.71 | 0.41 | 713 | quarters: 0.38 → 0.21 → 0.10 → 0.03

## Oil Round
Oil · 18 px · 19.5 s

![Oil Round](Oil-Round.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 2 % → 2 % | 0.71 | 1.00 | 46 |
| heavy line | 6 % → 6 % | 0.72 | 1.00 | 72 |
| pressure swell | 3 % → 3 % | 0.63 | 1.00 | 50 |
| fast wave | 7 % → 7 % | 0.54 | 1.00 | 155 |
| slow wave | 4 % → 4 % | 0.36 | 1.00 | 235 |
| spiral | 5 % → 5 % | 0.21 | 1.00 | 313 |
| loop | 3 % → 3 % | 0.18 | 1.00 | 149 |
| tilted | 2 % → 2 % | 0.33 | 1.00 | 70 |
| over the wet one | 3 % → 3 % | 0.33 | 1.00 | 57 |
| long, no reload | 8 % → 8 % | 0.17 | 1.00 | 363 | quarters: 0.02 → 0.02 → 0.01 → 0.01

## Palette Knife
Oil · 20 px · 19.4 s

![Palette Knife](Palette-Knife.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 8 % → 8 % | 0.67 | 1.00 | 13 |
| heavy line | 8 % → 8 % | 0.73 | 1.00 | 14 |
| pressure swell | 6 % → 6 % | 0.74 | 1.00 | 8 |
| fast wave | 17 % → 17 % | 0.49 | 1.00 | 40 |
| slow wave | 17 % → 17 % | 0.43 | 1.00 | 60 |
| spiral | 18 % → 18 % | 0.45 | 1.00 | 56 |
| loop | 16 % → 16 % | 0.58 | 1.00 | 26 |
| tilted | 5 % → 5 % | 0.72 | 1.00 | 11 |
| over the wet one | 13 % → 13 % | 0.72 | 1.00 | 19 |
| long, no reload | 17 % → 17 % | 0.47 | 1.00 | 70 | quarters: 0.29 → 0.05 → 0.00 → 0.00

Numbers say: pressure barely changes the width.

## Water
Watercolor · 20 px · 51.3 s · over bands of wet ink and oil pastel in turn (it works on paint already there: look at what it does to the bands; covered counts the bands too)

![Water](Water.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 31 % → 35 % | 0.81 | 1.15 | 26 |
| heavy line | 31 % → 35 % | 0.80 | 1.10 | 59 |
| pressure swell | 31 % → 33 % | 0.82 | 1.06 | 43 |
| fast wave | 32 % → 34 % | 0.82 | 1.07 | 153 |
| slow wave | 32 % → 34 % | 0.82 | 1.05 | 242 |
| spiral | 33 % → 34 % | 0.81 | 1.06 | 210 |
| loop | 32 % → 33 % | 0.82 | 1.03 | 123 |
| tilted | 32 % → 32 % | 0.82 | 1.00 | 498 |
| over the wet one | 32 % → 34 % | 0.82 | 1.05 | 76 |
| long, no reload | 32 % → 34 % | 0.82 | 1.06 | 436 | quarters: 0.25 → 0.34 → 0.26 → 0.34

Numbers say: pressure barely changes the width; the long stroke does not run out of paint.

## Blender
Pastel · 16 px · 44.1 s · over bands of wet ink and oil pastel in turn (it works on paint already there: look at what it does to the bands; covered counts the bands too)

![Blender](Blender.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 30 % → 33 % | 0.82 | 1.10 | 68 |
| heavy line | 31 % → 33 % | 0.82 | 1.05 | 58 |
| pressure swell | 32 % → 33 % | 0.82 | 1.03 | 31 |
| fast wave | 34 % → 34 % | 0.81 | 1.01 | 143 |
| slow wave | 34 % → 34 % | 0.81 | 1.00 | 124 |
| spiral | 36 % → 36 % | 0.79 | 1.00 | 176 |
| loop | 33 % → 33 % | 0.81 | 1.00 | 71 |
| tilted | 33 % → 33 % | 0.81 | 1.00 | 71 |
| over the wet one | 34 % → 34 % | 0.81 | 1.00 | 40 |
| long, no reload | 38 % → 38 % | 0.78 | 1.00 | 197 | quarters: 0.23 → 0.35 → 0.30 → 0.37

Numbers say: pressure barely changes the width; the long stroke does not run out of paint.

## Eraser
Eraser · 16 px · 45.1 s · over bands of wet ink and oil pastel in turn (it works on paint already there: look at what it does to the bands; covered counts the bands too)

![Eraser](Eraser.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 29 % → 32 % | 0.83 | 1.10 | 90 |
| heavy line | 31 % → 32 % | 0.83 | 1.05 | 62 |
| pressure swell | 31 % → 32 % | 0.83 | 1.03 | 40 |
| fast wave | 32 % → 32 % | 0.83 | 1.01 | 135 |
| slow wave | 32 % → 32 % | 0.83 | 1.00 | 132 |
| spiral | 32 % → 32 % | 0.83 | 1.00 | 165 |
| loop | 32 % → 32 % | 0.83 | 1.00 | 76 |
| tilted | 32 % → 32 % | 0.83 | 1.00 | 73 |
| over the wet one | 32 % → 32 % | 0.83 | 1.00 | 40 |
| long, no reload | 32 % → 32 % | 0.83 | 1.00 | 267 | quarters: 0.22 → 0.32 → 0.25 → 0.33

Numbers say: pressure barely changes the width; the long stroke does not run out of paint.

## Fan
Gouache · 30 px · 35.3 s

![Fan](Fan.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 9 % → 3 % | 0.63 | 0.37 | 42 |
| heavy line | 11 % → 4 % | 0.63 | 0.39 | 68 |
| pressure swell | 8 % → 5 % | 0.63 | 0.55 | 33 |
| fast wave | 18 % → 5 % | 0.63 | 0.26 | 134 |
| slow wave | 18 % → 5 % | 0.63 | 0.25 | 248 |
| spiral | 24 % → 5 % | 0.63 | 0.20 | 299 |
| loop | 17 % → 5 % | 0.63 | 0.29 | 313 |
| tilted | 5 % → 6 % | 0.63 | 1.05 | 58 |
| over the wet one | 16 % → 8 % | 0.63 | 0.50 | 54 |
| long, no reload | 23 % → 5 % | 0.63 | 0.22 | 313 | quarters: 0.29 → 0.07 → 0.01 → 0.00

## Sponge
Gouache · 30 px · 35.2 s

![Sponge](Sponge.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 4 % → 0 % | 0.62 | 0.12 | 50 |
| heavy line | 12 % → 2 % | 0.62 | 0.14 | 66 |
| pressure swell | 7 % → 2 % | 0.62 | 0.27 | 146 |
| fast wave | 20 % → 4 % | 0.62 | 0.19 | 462 |
| slow wave | 21 % → 4 % | 0.62 | 0.18 | 282 |
| spiral | 28 % → 4 % | 0.62 | 0.14 | 256 |
| loop | 18 % → 5 % | 0.62 | 0.29 | 124 |
| tilted | 7 % → 7 % | 0.62 | 1.04 | 124 |
| over the wet one | 16 % → 6 % | 0.62 | 0.37 | 66 |
| long, no reload | 29 % → 5 % | 0.62 | 0.17 | 324 | quarters: 0.29 → 0.13 → 0.07 → 0.04

## Ink — sumi brush
Watercolor · 22 px · 34.7 s

![Ink — sumi brush](Ink-sumi-brush.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 6 % → 7 % | 0.46 | 1.06 | 131 |
| heavy line | 10 % → 11 % | 0.38 | 1.05 | 166 |
| pressure swell | 7 % → 8 % | 0.42 | 1.04 | 112 |
| fast wave | 21 % → 21 % | 0.32 | 1.00 | 186 |
| slow wave | 19 % → 19 % | 0.37 | 1.01 | 293 |
| spiral | 28 % → 26 % | 0.30 | 0.92 | 283 |
| loop | 17 % → 18 % | 0.37 | 1.06 | 159 |
| tilted | 6 % → 7 % | 0.40 | 1.17 | 69 |
| over the wet one | 16 % → 16 % | 0.40 | 1.01 | 68 |
| long, no reload | 33 % → 29 % | 0.30 | 0.86 | 443 | quarters: 0.23 → 0.11 → 0.06 → 0.04

## Ink — wash
Watercolor · 40 px · 36.4 s

![Ink — wash](Ink-wash.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 8 % → 9 % | 0.05 | 1.26 | 92 |
| heavy line | 11 % → 13 % | 0.04 | 1.22 | 121 |
| pressure swell | 7 % → 9 % | 0.05 | 1.25 | 62 |
| fast wave | 22 % → 27 % | 0.04 | 1.21 | 274 |
| slow wave | 21 % → 26 % | 0.06 | 1.23 | 423 |
| spiral | 34 % → 41 % | 0.04 | 1.21 | 356 |
| loop | 19 % → 24 % | 0.05 | 1.25 | 170 |
| tilted | 7 % → 9 % | 0.05 | 1.21 | 120 |
| over the wet one | 18 % → 21 % | 0.05 | 1.18 | 85 |
| long, no reload | 39 % → 46 % | 0.05 | 1.19 | 613 | quarters: 0.04 → 0.03 → 0.02 → 0.01

## Ink — dry brush
Ink · 30 px · 26.5 s

![Ink — dry brush](Ink-dry-brush.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 9 % → 7 % | 0.81 | 0.78 | 98 |
| heavy line | 11 % → 8 % | 0.80 | 0.73 | 114 |
| pressure swell | 8 % → 7 % | 0.81 | 0.85 | 71 |
| fast wave | 22 % → 8 % | 0.78 | 0.38 | 219 |
| slow wave | 18 % → 6 % | 0.80 | 0.36 | 397 |
| spiral | 23 % → 8 % | 0.77 | 0.35 | 398 |
| loop | 20 % → 8 % | 0.77 | 0.41 | 239 |
| tilted | 9 % → 9 % | 0.78 | 1.01 | 196 |
| over the wet one | 19 % → 14 % | 0.78 | 0.75 | 120 |
| long, no reload | 20 % → 9 % | 0.78 | 0.42 | 698 | quarters: 0.32 → 0.01 → 0.00 → 0.00

## Ink — nib
Watercolor · 5 px · 24.0 s

![Ink — nib](Ink-nib.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 2 % → 2 % | 0.76 | 1.17 | 25 |
| heavy line | 2 % → 2 % | 0.77 | 1.16 | 29 |
| pressure swell | 1 % → 2 % | 0.78 | 1.22 | 19 |
| fast wave | 4 % → 4 % | 0.66 | 1.09 | 63 |
| slow wave | 4 % → 4 % | 0.68 | 1.11 | 82 |
| spiral | 6 % → 6 % | 0.58 | 1.08 | 128 |
| loop | 3 % → 4 % | 0.69 | 1.12 | 69 |
| tilted | 2 % → 2 % | 0.64 | 1.21 | 56 |
| over the wet one | 4 % → 4 % | 0.64 | 1.03 | 43 |
| long, no reload | 7 % → 7 % | 0.53 | 1.02 | 297 | quarters: 0.09 → 0.04 → 0.03 → 0.02

## 0.45 · Dry brush
Gouache · 34 px · 28.1 s

![0.45 · Dry brush](0-45-Dry-brush.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 11 % → 3 % | 0.67 | 0.28 | 122 |
| heavy line | 12 % → 3 % | 0.67 | 0.30 | 158 |
| pressure swell | 9 % → 4 % | 0.67 | 0.40 | 99 |
| fast wave | 20 % → 4 % | 0.67 | 0.19 | 309 |
| slow wave | 20 % → 4 % | 0.67 | 0.18 | 546 |
| spiral | 21 % → 4 % | 0.67 | 0.17 | 541 |
| loop | 21 % → 4 % | 0.67 | 0.19 | 343 |
| tilted | 9 % → 9 % | 0.67 | 0.97 | 181 |
| over the wet one | 20 % → 7 % | 0.67 | 0.33 | 129 |
| long, no reload | 20 % → 4 % | 0.67 | 0.21 | 831 | quarters: 0.38 → 0.07 → 0.00 → 0.00

Numbers say: pressure barely changes the width.

## Dry pastel
Pastel · 26 px · 12.9 s

![Dry pastel](Dry-pastel.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 5 % → 5 % | 0.36 | 1.00 | 34 |
| heavy line | 6 % → 6 % | 0.36 | 1.00 | 36 |
| pressure swell | 5 % → 5 % | 0.36 | 1.00 | 35 |
| fast wave | 15 % → 15 % | 0.36 | 1.00 | 96 |
| slow wave | 14 % → 14 % | 0.36 | 1.00 | 160 |
| spiral | 23 % → 23 % | 0.36 | 1.00 | 154 |
| loop | 11 % → 11 % | 0.36 | 1.00 | 68 |
| tilted | 5 % → 5 % | 0.37 | 1.00 | 41 |
| over the wet one | 10 % → 10 % | 0.37 | 1.00 | 34 |
| long, no reload | 26 % → 26 % | 0.36 | 1.00 | 220 | quarters: 0.11 → 0.10 → 0.10 → 0.11

Numbers say: the long stroke does not run out of paint.

## 0.45 · Charcoal
Charcoal · 18 px · 13.5 s

![0.45 · Charcoal](0-45-Charcoal.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 4 % → 4 % | 0.79 | 1.00 | 26 |
| heavy line | 4 % → 4 % | 0.79 | 1.00 | 26 |
| pressure swell | 4 % → 4 % | 0.79 | 1.00 | 12 |
| fast wave | 11 % → 11 % | 0.79 | 1.00 | 52 |
| slow wave | 11 % → 11 % | 0.78 | 1.00 | 63 |
| spiral | 20 % → 20 % | 0.79 | 1.00 | 87 |
| loop | 10 % → 10 % | 0.79 | 1.00 | 50 |
| tilted | 4 % → 4 % | 0.78 | 1.00 | 32 |
| over the wet one | 9 % → 9 % | 0.78 | 1.00 | 21 |
| long, no reload | 26 % → 26 % | 0.79 | 1.00 | 106 | quarters: 0.23 → 0.22 → 0.23 → 0.24

Numbers say: pressure barely changes the width; the long stroke does not run out of paint.

## Watercolour — wash
Watercolor · 50 px · 38.0 s

![Watercolour — wash](Watercolour-wash.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 9 % → 11 % | 0.01 | 1.22 | 152 |
| heavy line | 12 % → 14 % | 0.01 | 1.17 | 110 |
| pressure swell | 8 % → 10 % | 0.01 | 1.22 | 75 |
| fast wave | 26 % → 30 % | 0.01 | 1.18 | 329 |
| slow wave | 25 % → 29 % | 0.01 | 1.18 | 657 |
| spiral | 39 % → 46 % | 0.01 | 1.17 | 676 |
| loop | 22 % → 27 % | 0.01 | 1.21 | 268 |
| tilted | 10 % → 11 % | 0.01 | 1.18 | 162 |
| over the wet one | 22 % → 25 % | 0.01 | 1.14 | 125 |
| long, no reload | 45 % → 54 % | 0.01 | 1.18 | 608 | quarters: 0.01 → 0.01 → 0.01 → 0.00

## Watercolour — wet-in-wet
Watercolor · 44 px · 34.8 s

![Watercolour — wet-in-wet](Watercolour-wet-in-wet.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 7 % → 9 % | 0.02 | 1.26 | 81 |
| heavy line | 10 % → 12 % | 0.02 | 1.22 | 125 |
| pressure swell | 7 % → 9 % | 0.02 | 1.21 | 67 |
| fast wave | 23 % → 27 % | 0.02 | 1.17 | 240 |
| slow wave | 22 % → 26 % | 0.02 | 1.18 | 339 |
| spiral | 36 % → 43 % | 0.02 | 1.20 | 376 |
| loop | 19 % → 23 % | 0.02 | 1.20 | 186 |
| tilted | 7 % → 9 % | 0.02 | 1.19 | 125 |
| over the wet one | 17 % → 19 % | 0.02 | 1.12 | 87 |
| long, no reload | 42 % → 49 % | 0.02 | 1.18 | 529 | quarters: 0.01 → 0.01 → 0.01 → 0.01

## Watercolour — glaze
Watercolor · 38 px · 35.0 s

![Watercolour — glaze](Watercolour-glaze.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 7 % → 9 % | 0.01 | 1.28 | 71 |
| heavy line | 10 % → 13 % | 0.01 | 1.25 | 87 |
| pressure swell | 7 % → 9 % | 0.01 | 1.29 | 60 |
| fast wave | 20 % → 25 % | 0.01 | 1.24 | 196 |
| slow wave | 19 % → 24 % | 0.01 | 1.26 | 451 |
| spiral | 31 % → 37 % | 0.01 | 1.21 | 387 |
| loop | 18 % → 23 % | 0.01 | 1.27 | 187 |
| tilted | 7 % → 8 % | 0.01 | 1.20 | 131 |
| over the wet one | 17 % → 20 % | 0.01 | 1.19 | 84 |
| long, no reload | 36 % → 42 % | 0.01 | 1.17 | 517 | quarters: 0.01 → 0.00 → 0.00 → 0.00

## Watercolour — granulating
Watercolor · 44 px · 38.5 s

![Watercolour — granulating](Watercolour-granulating.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 8 % → 10 % | 0.02 | 1.18 | 88 |
| heavy line | 12 % → 14 % | 0.01 | 1.15 | 112 |
| pressure swell | 8 % → 10 % | 0.02 | 1.18 | 86 |
| fast wave | 25 % → 29 % | 0.01 | 1.15 | 246 |
| slow wave | 24 % → 27 % | 0.02 | 1.16 | 540 |
| spiral | 39 % → 44 % | 0.01 | 1.15 | 598 |
| loop | 22 % → 25 % | 0.01 | 1.17 | 273 |
| tilted | 9 % → 11 % | 0.02 | 1.15 | 125 |
| over the wet one | 21 % → 23 % | 0.02 | 1.11 | 81 |
| long, no reload | 45 % → 52 % | 0.01 | 1.15 | 567 | quarters: 0.01 → 0.01 → 0.01 → 0.01

## Watercolour — dry brush
Watercolor · 36 px · 33.1 s

![Watercolour — dry brush](Watercolour-dry-brush.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 7 % → 8 % | 0.05 | 1.07 | 157 |
| heavy line | 11 % → 12 % | 0.04 | 1.03 | 185 |
| pressure swell | 9 % → 10 % | 0.05 | 1.07 | 128 |
| fast wave | 21 % → 14 % | 0.04 | 0.68 | 341 |
| slow wave | 19 % → 13 % | 0.04 | 0.70 | 440 |
| spiral | 24 % → 15 % | 0.04 | 0.61 | 414 |
| loop | 17 % → 14 % | 0.04 | 0.85 | 217 |
| tilted | 7 % → 8 % | 0.05 | 1.19 | 125 |
| over the wet one | 17 % → 17 % | 0.05 | 0.99 | 103 |
| long, no reload | 22 % → 15 % | 0.04 | 0.68 | 654 | quarters: 0.02 → 0.00 → 0.00 → 0.00

## Gouache
Gouache · 30 px · 31.8 s

![Gouache](Gouache.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 8 % → 6 % | 0.14 | 0.67 | 70 |
| heavy line | 13 % → 6 % | 0.14 | 0.47 | 88 |
| pressure swell | 10 % → 6 % | 0.14 | 0.61 | 56 |
| fast wave | 27 % → 7 % | 0.14 | 0.27 | 188 |
| slow wave | 27 % → 7 % | 0.14 | 0.27 | 355 |
| spiral | 37 % → 8 % | 0.14 | 0.22 | 430 |
| loop | 22 % → 8 % | 0.14 | 0.36 | 255 |
| tilted | 9 % → 9 % | 0.14 | 1.02 | 98 |
| over the wet one | 20 % → 13 % | 0.14 | 0.67 | 103 |
| long, no reload | 38 % → 10 % | 0.14 | 0.25 | 515 | quarters: 0.07 → 0.04 → 0.01 → 0.01

## Oil — alla prima
Oil · 30 px · 22.8 s

![Oil — alla prima](Oil-alla-prima.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 9 % → 9 % | 0.50 | 1.00 | 107 |
| heavy line | 10 % → 10 % | 0.50 | 1.00 | 113 |
| pressure swell | 8 % → 8 % | 0.52 | 1.00 | 74 |
| fast wave | 24 % → 24 % | 0.49 | 1.00 | 252 |
| slow wave | 25 % → 25 % | 0.50 | 1.00 | 437 |
| spiral | 38 % → 38 % | 0.44 | 1.00 | 451 |
| loop | 21 % → 21 % | 0.50 | 1.00 | 204 |
| tilted | 11 % → 11 % | 0.50 | 1.00 | 194 |
| over the wet one | 20 % → 20 % | 0.50 | 1.00 | 110 |
| long, no reload | 46 % → 46 % | 0.40 | 1.00 | 836 | quarters: 0.31 → 0.24 → 0.17 → 0.10

Numbers say: pressure barely changes the width.

## Oil — impasto
Oil · 34 px · 23.8 s

![Oil — impasto](Oil-impasto.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 11 % → 11 % | 0.24 | 1.00 | 107 |
| heavy line | 12 % → 12 % | 0.23 | 1.00 | 133 |
| pressure swell | 9 % → 9 % | 0.25 | 1.00 | 85 |
| fast wave | 29 % → 29 % | 0.21 | 1.00 | 312 |
| slow wave | 29 % → 29 % | 0.21 | 1.00 | 510 |
| spiral | 48 % → 48 % | 0.17 | 1.00 | 660 |
| loop | 25 % → 25 % | 0.21 | 1.00 | 364 |
| tilted | 12 % → 12 % | 0.24 | 1.00 | 166 |
| over the wet one | 23 % → 23 % | 0.24 | 1.00 | 124 |
| long, no reload | 55 % → 55 % | 0.15 | 1.00 | 746 | quarters: 0.16 → 0.11 → 0.06 → 0.02

Numbers say: pressure barely changes the width.

## Oil — glaze
Oil · 40 px · 19.7 s

![Oil — glaze](Oil-glaze.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 10 % → 10 % | 0.49 | 1.00 | 135 |
| heavy line | 14 % → 14 % | 0.48 | 1.00 | 193 |
| pressure swell | 10 % → 10 % | 0.49 | 1.00 | 97 |
| fast wave | 28 % → 28 % | 0.46 | 1.00 | 336 |
| slow wave | 30 % → 30 % | 0.46 | 1.00 | 511 |
| spiral | 42 % → 42 % | 0.44 | 1.00 | 540 |
| loop | 24 % → 24 % | 0.47 | 1.00 | 285 |
| tilted | 11 % → 11 % | 0.47 | 1.00 | 181 |
| over the wet one | 23 % → 23 % | 0.47 | 1.00 | 112 |
| long, no reload | 47 % → 47 % | 0.43 | 1.00 | 766 | quarters: 0.33 → 0.24 → 0.18 → 0.14

## Oil — scumble
Oil · 36 px · 25.0 s

![Oil — scumble](Oil-scumble.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 11 % → 11 % | 0.06 | 1.00 | 150 |
| heavy line | 12 % → 12 % | 0.05 | 1.00 | 170 |
| pressure swell | 9 % → 9 % | 0.06 | 1.00 | 132 |
| fast wave | 18 % → 18 % | 0.04 | 1.00 | 407 |
| slow wave | 20 % → 20 % | 0.04 | 1.00 | 633 |
| spiral | 19 % → 19 % | 0.03 | 1.00 | 679 |
| loop | 22 % → 22 % | 0.04 | 1.00 | 283 |
| tilted | 10 % → 10 % | 0.05 | 1.00 | 181 |
| over the wet one | 21 % → 21 % | 0.05 | 1.00 | 156 |
| long, no reload | 18 % → 18 % | 0.04 | 1.00 | 1340 | quarters: 0.03 → 0.00 → 0.00 → 0.00

Numbers say: pressure barely changes the width.

## Acrylic — heavy body
Heavy acrylic · 30 px · 18.4 s

![Acrylic — heavy body](Acrylic-heavy-body.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 10 % → 9 % | 0.51 | 0.93 | 94 |
| heavy line | 11 % → 10 % | 0.51 | 0.93 | 112 |
| pressure swell | 8 % → 8 % | 0.52 | 0.94 | 80 |
| fast wave | 24 % → 14 % | 0.51 | 0.58 | 271 |
| slow wave | 25 % → 15 % | 0.51 | 0.59 | 393 |
| spiral | 37 % → 15 % | 0.51 | 0.40 | 437 |
| loop | 22 % → 16 % | 0.51 | 0.73 | 260 |
| tilted | 10 % → 10 % | 0.51 | 1.00 | 174 |
| over the wet one | 20 % → 17 % | 0.51 | 0.88 | 135 |
| long, no reload | 39 % → 15 % | 0.51 | 0.40 | 922 | quarters: 0.30 → 0.20 → 0.10 → 0.02

Numbers say: pressure barely changes the width.

## Acrylic — fluid
Watercolor · 36 px · 36.9 s

![Acrylic — fluid](Acrylic-fluid.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 9 % → 10 % | 0.06 | 1.11 | 78 |
| heavy line | 13 % → 14 % | 0.05 | 1.07 | 98 |
| pressure swell | 9 % → 10 % | 0.07 | 1.09 | 70 |
| fast wave | 26 % → 28 % | 0.05 | 1.07 | 226 |
| slow wave | 24 % → 26 % | 0.07 | 1.08 | 369 |
| spiral | 39 % → 41 % | 0.05 | 1.06 | 498 |
| loop | 22 % → 25 % | 0.06 | 1.11 | 193 |
| tilted | 8 % → 9 % | 0.07 | 1.17 | 111 |
| over the wet one | 21 % → 22 % | 0.07 | 1.05 | 100 |
| long, no reload | 44 % → 47 % | 0.05 | 1.06 | 525 | quarters: 0.05 → 0.03 → 0.02 → 0.01

## Acrylic — palette knife
Heavy acrylic · 42 px · 26.2 s

![Acrylic — palette knife](Acrylic-palette-knife.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 15 % → 15 % | 0.06 | 0.98 | 25 |
| heavy line | 15 % → 15 % | 0.05 | 0.98 | 36 |
| pressure swell | 12 % → 12 % | 0.06 | 0.99 | 15 |
| fast wave | 37 % → 20 % | 0.06 | 0.54 | 56 |
| slow wave | 37 % → 21 % | 0.06 | 0.56 | 105 |
| spiral | 48 % → 19 % | 0.06 | 0.38 | 112 |
| loop | 32 % → 24 % | 0.05 | 0.75 | 62 |
| tilted | 12 % → 12 % | 0.05 | 1.00 | 31 |
| over the wet one | 26 % → 26 % | 0.05 | 0.98 | 34 |
| long, no reload | 55 % → 20 % | 0.06 | 0.36 | 154 | quarters: 0.04 → 0.02 → 0.00 → 0.00

Numbers say: pressure barely changes the width.

## Finger on oil
Oil · 30 px · 17.3 s

![Finger on oil](Finger-on-oil.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 8 % → 8 % | 0.34 | 1.00 | 50 |
| heavy line | 12 % → 12 % | 0.30 | 1.00 | 70 |
| pressure swell | 8 % → 8 % | 0.35 | 1.00 | 48 |
| fast wave | 16 % → 16 % | 0.22 | 1.00 | 137 |
| slow wave | 17 % → 17 % | 0.23 | 1.00 | 254 |
| spiral | 18 % → 18 % | 0.22 | 1.00 | 255 |
| loop | 18 % → 18 % | 0.23 | 1.00 | 119 |
| tilted | 9 % → 9 % | 0.31 | 1.00 | 87 |
| over the wet one | 18 % → 18 % | 0.31 | 1.00 | 59 |
| long, no reload | 15 % → 15 % | 0.23 | 1.00 | 378 | quarters: 0.13 → 0.01 → 0.00 → 0.00

## Palette knife — oil
Oil · 44 px · 25.0 s

![Palette knife — oil](Palette-knife-oil.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 16 % → 16 % | 0.10 | 1.00 | 22 |
| heavy line | 16 % → 16 % | 0.09 | 1.00 | 27 |
| pressure swell | 12 % → 12 % | 0.10 | 1.00 | 14 |
| fast wave | 39 % → 39 % | 0.07 | 1.00 | 74 |
| slow wave | 39 % → 39 % | 0.07 | 1.00 | 189 |
| spiral | 54 % → 54 % | 0.05 | 1.00 | 184 |
| loop | 34 % → 34 % | 0.08 | 1.00 | 104 |
| tilted | 13 % → 13 % | 0.09 | 1.00 | 37 |
| over the wet one | 28 % → 28 % | 0.09 | 1.00 | 47 |
| long, no reload | 65 % → 65 % | 0.05 | 1.00 | 164 | quarters: 0.08 → 0.04 → 0.01 → 0.00

Numbers say: pressure barely changes the width.

## 0.45 · Sponge
Watercolor · 46 px · 31.1 s

![0.45 · Sponge](0-45-Sponge.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 11 % → 0 % | 0.00 | 0.00 | 78 |
| heavy line | 13 % → 0 % | 0.01 | 0.00 | 133 |
| pressure swell | 9 % → 1 % | 0.02 | 0.14 | 122 |
| fast wave | 23 % → 2 % | 0.01 | 0.08 | 281 |
| slow wave | 26 % → 8 % | 0.02 | 0.30 | 328 |
| spiral | 34 % → 11 % | 0.02 | 0.32 | 302 |
| loop | 22 % → 4 % | 0.02 | 0.19 | 168 |
| tilted | 9 % → 10 % | 0.04 | 1.19 | 104 |
| over the wet one | 22 % → 10 % | 0.04 | 0.44 | 84 |
| long, no reload | 41 % → 19 % | 0.02 | 0.47 | 434 | quarters: 0.01 → 0.01 → 0.01 → 0.01

## 0.45 · Eraser
Eraser · 30 px · 42.7 s · over bands of wet ink and oil pastel in turn (it works on paint already there: look at what it does to the bands; covered counts the bands too)

![0.45 · Eraser](0-45-Eraser.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 29 % → 32 % | 0.83 | 1.10 | 55 |
| heavy line | 30 % → 32 % | 0.83 | 1.05 | 62 |
| pressure swell | 31 % → 32 % | 0.83 | 1.03 | 53 |
| fast wave | 31 % → 31 % | 0.80 | 1.02 | 152 |
| slow wave | 28 % → 28 % | 0.82 | 1.00 | 249 |
| spiral | 28 % → 28 % | 0.80 | 1.00 | 242 |
| loop | 29 % → 29 % | 0.81 | 1.00 | 189 |
| tilted | 31 % → 31 % | 0.82 | 1.00 | 106 |
| over the wet one | 30 % → 30 % | 0.82 | 1.00 | 62 |
| long, no reload | 23 % → 23 % | 0.79 | 1.00 | 388 | quarters: 0.15 → 0.21 → 0.18 → 0.22

Numbers say: pressure barely changes the width; the long stroke does not run out of paint.

## Lift wet paint
Eraser · 30 px · 41.7 s · over bands of wet ink and oil pastel in turn (it works on paint already there: look at what it does to the bands; covered counts the bands too)

![Lift wet paint](Lift-wet-paint.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 29 % → 32 % | 0.83 | 1.10 | 39 |
| heavy line | 31 % → 32 % | 0.83 | 1.05 | 59 |
| pressure swell | 31 % → 32 % | 0.83 | 1.03 | 37 |
| fast wave | 32 % → 32 % | 0.83 | 1.01 | 163 |
| slow wave | 32 % → 32 % | 0.83 | 1.00 | 320 |
| spiral | 32 % → 32 % | 0.83 | 1.00 | 189 |
| loop | 32 % → 32 % | 0.83 | 1.00 | 110 |
| tilted | 32 % → 32 % | 0.83 | 1.00 | 67 |
| over the wet one | 32 % → 32 % | 0.83 | 1.00 | 59 |
| long, no reload | 32 % → 32 % | 0.83 | 1.00 | 313 | quarters: 0.22 → 0.32 → 0.25 → 0.33

Numbers say: pressure barely changes the width; the long stroke does not run out of paint.

## Sgraffito
Eraser · 10 px · 40.9 s · over bands of wet ink and oil pastel in turn (it works on paint already there: look at what it does to the bands; covered counts the bands too)

![Sgraffito](Sgraffito.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 29 % → 32 % | 0.82 | 1.08 | 13 |
| heavy line | 31 % → 32 % | 0.82 | 1.04 | 11 |
| pressure swell | 31 % → 32 % | 0.82 | 1.02 | 5 |
| fast wave | 32 % → 31 % | 0.82 | 0.98 | 27 |
| slow wave | 32 % → 31 % | 0.82 | 0.97 | 27 |
| spiral | 32 % → 31 % | 0.82 | 0.96 | 47 |
| loop | 32 % → 32 % | 0.82 | 0.99 | 32 |
| tilted | 32 % → 32 % | 0.82 | 0.99 | 25 |
| over the wet one | 32 % → 32 % | 0.82 | 0.99 | 17 |
| long, no reload | 32 % → 32 % | 0.82 | 1.00 | 69 | quarters: 0.21 → 0.31 → 0.25 → 0.32

Numbers say: pressure barely changes the width; the long stroke does not run out of paint.

## Brush Artist · Sumi — wetter
Watercolor · 24 px · 30.9 s

![Brush Artist · Sumi — wetter](Brush-Artist-Sumi-wetter.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 5 % → 6 % | 0.21 | 1.11 | 58 |
| heavy line | 11 % → 12 % | 0.13 | 1.13 | 71 |
| pressure swell | 7 % → 8 % | 0.16 | 1.13 | 48 |
| fast wave | 21 % → 24 % | 0.12 | 1.15 | 175 |
| slow wave | 19 % → 22 % | 0.15 | 1.14 | 285 |
| spiral | 29 % → 32 % | 0.12 | 1.13 | 297 |
| loop | 17 % → 19 % | 0.15 | 1.15 | 156 |
| tilted | 6 % → 7 % | 0.16 | 1.17 | 112 |
| over the wet one | 16 % → 17 % | 0.16 | 1.07 | 110 |
| long, no reload | 33 % → 37 % | 0.12 | 1.12 | 549 | quarters: 0.10 → 0.05 → 0.03 → 0.02

