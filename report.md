![All brushes](contact.png)

# Brush Lab — 60 brushes · Nov 3, 2026 at 11:12 AM

Every sheet: 1500 × 600, ten strokes in a 5 × 2 grid — 1. light line · 2. heavy line · 3. pressure swell · 4. fast wave · 5. slow wave · 6. spiral · 7. loop · 8. tilted · 9. over the wet one · 10. long, no reload (cell 8 holds «tilted» and «over the wet one» crossed). The CPU reference of Mamay's paint engine; the wet layer settles 20 s at the end.

Columns: **covered** = share of the cell with paint right after the stroke → after settling; **dark** = mean darkness of the painted pixels above the paper's own grain (0 = paper, 1 = black); **spread** = how far wet paint went beyond the stroke (1.0 = stayed); **ms** = the stroke on the CPU; long stroke: paint in each quarter of its length (it should run out: wet → streaks → dry tail).

## Ink Line
Ink · 12 px · 24.4 s

![Ink Line](Ink-Line.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 1 % → 4 % | 0.55 | 2.44 | 50 |
| heavy line | 5 % → 6 % | 0.68 | 1.13 | 71 |
| pressure swell | 3 % → 4 % | 0.64 | 1.40 | 38 |
| fast wave | 10 % → 11 % | 0.59 | 1.11 | 120 |
| slow wave | 8 % → 10 % | 0.57 | 1.16 | 111 |
| spiral | 14 % → 15 % | 0.50 | 1.07 | 346 |
| loop | 8 % → 9 % | 0.61 | 1.16 | 213 |
| tilted | 5 % → 5 % | 0.65 | 1.05 | 101 |
| over the wet one | 10 % → 11 % | 0.65 | 1.15 | 75 |
| long, no reload | 18 % → 17 % | 0.47 | 0.96 | 308 | quarters: 0.22 → 0.09 → 0.04 → 0.02

Numbers say: wet paint spreads well beyond the stroke.

## Dense Ink
Ink · 14 px · 25.2 s

![Dense Ink](Dense-Ink.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 5 % → 7 % | 0.72 | 1.26 | 59 |
| heavy line | 7 % → 7 % | 0.73 | 1.09 | 86 |
| pressure swell | 5 % → 6 % | 0.72 | 1.17 | 45 |
| fast wave | 13 % → 13 % | 0.69 | 1.01 | 133 |
| slow wave | 12 % → 12 % | 0.67 | 1.04 | 145 |
| spiral | 18 % → 15 % | 0.65 | 0.80 | 401 |
| loop | 11 % → 12 % | 0.69 | 1.08 | 221 |
| tilted | 5 % → 6 % | 0.72 | 1.07 | 93 |
| over the wet one | 12 % → 13 % | 0.72 | 1.11 | 92 |
| long, no reload | 23 % → 15 % | 0.64 | 0.66 | 363 | quarters: 0.30 → 0.12 → 0.04 → 0.02

## Transparent Wash
Watercolor · 22 px · 25.5 s

![Transparent Wash](Transparent-Wash.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 2 % → 5 % | 0.27 | 2.25 | 64 |
| heavy line | 7 % → 9 % | 0.27 | 1.22 | 67 |
| pressure swell | 4 % → 6 % | 0.28 | 1.54 | 35 |
| fast wave | 14 % → 16 % | 0.20 | 1.17 | 114 |
| slow wave | 12 % → 15 % | 0.21 | 1.28 | 163 |
| spiral | 18 % → 22 % | 0.16 | 1.23 | 298 |
| loop | 11 % → 13 % | 0.22 | 1.20 | 193 |
| tilted | 8 % → 8 % | 0.24 | 1.06 | 186 |
| over the wet one | 13 % → 16 % | 0.24 | 1.18 | 72 |
| long, no reload | 26 % → 32 % | 0.13 | 1.22 | 284 | quarters: 0.11 → 0.04 → 0.02 → 0.01

Numbers say: wet paint spreads well beyond the stroke.

## Dry Brush
Gouache · 24 px · 19.2 s

![Dry Brush](Dry-Brush.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 5 % → 0 % | 0.65 | 0.09 | 43 |
| heavy line | 6 % → 0 % | 0.65 | 0.02 | 96 |
| pressure swell | 5 % → 0 % | 0.65 | 0.08 | 49 |
| fast wave | 6 % → 1 % | 0.65 | 0.08 | 149 |
| slow wave | 7 % → 0 % | 0.65 | 0.06 | 258 |
| spiral | 7 % → 0 % | 0.65 | 0.07 | 245 |
| loop | 10 % → 0 % | 0.65 | 0.04 | 133 |
| tilted | 4 % → 3 % | 0.65 | 0.88 | 89 |
| over the wet one | 9 % → 1 % | 0.65 | 0.12 | 88 |
| long, no reload | 6 % → 1 % | 0.65 | 0.14 | 469 | quarters: 0.12 → 0.00 → 0.00 → 0.00

## Wax Crayon
Wax · 8 px · 9.5 s

![Wax Crayon](Wax-Crayon.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 1 % → 1 % | 0.71 | 1.00 | 16 |
| heavy line | 1 % → 1 % | 0.69 | 1.00 | 18 |
| pressure swell | 1 % → 1 % | 0.70 | 1.00 | 12 |
| fast wave | 3 % → 3 % | 0.69 | 1.00 | 40 |
| slow wave | 3 % → 3 % | 0.70 | 1.00 | 57 |
| spiral | 5 % → 5 % | 0.70 | 1.00 | 87 |
| loop | 3 % → 3 % | 0.70 | 1.00 | 41 |
| tilted | 2 % → 2 % | 0.68 | 1.00 | 32 |
| over the wet one | 3 % → 3 % | 0.68 | 1.00 | 19 |
| long, no reload | 7 % → 7 % | 0.70 | 1.00 | 109 | quarters: 0.06 → 0.06 → 0.06 → 0.06

Numbers say: the long stroke does not run out of paint.

## Oil Pastel
Wax · 12 px · 9.7 s

![Oil Pastel](Oil-Pastel.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 1 % → 1 % | 0.68 | 1.00 | 22 |
| heavy line | 2 % → 2 % | 0.68 | 1.00 | 27 |
| pressure swell | 2 % → 2 % | 0.69 | 1.00 | 19 |
| fast wave | 5 % → 5 % | 0.68 | 1.00 | 77 |
| slow wave | 5 % → 5 % | 0.68 | 1.00 | 72 |
| spiral | 8 % → 8 % | 0.68 | 1.00 | 110 |
| loop | 4 % → 4 % | 0.68 | 1.00 | 56 |
| tilted | 2 % → 2 % | 0.68 | 1.00 | 42 |
| over the wet one | 5 % → 5 % | 0.68 | 1.00 | 24 |
| long, no reload | 13 % → 13 % | 0.68 | 1.00 | 152 | quarters: 0.10 → 0.09 → 0.10 → 0.10

Numbers say: the long stroke does not run out of paint.

## Charcoal
Charcoal · 5 px · 9.3 s

![Charcoal](Charcoal.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 1 % → 1 % | 0.74 | 1.00 | 12 |
| heavy line | 1 % → 1 % | 0.74 | 1.00 | 14 |
| pressure swell | 1 % → 1 % | 0.74 | 1.00 | 8 |
| fast wave | 2 % → 2 % | 0.73 | 1.00 | 28 |
| slow wave | 2 % → 2 % | 0.74 | 1.00 | 27 |
| spiral | 4 % → 4 % | 0.74 | 1.00 | 51 |
| loop | 2 % → 2 % | 0.74 | 1.00 | 24 |
| tilted | 2 % → 2 % | 0.72 | 1.00 | 17 |
| over the wet one | 2 % → 2 % | 0.72 | 1.00 | 11 |
| long, no reload | 6 % → 6 % | 0.73 | 1.00 | 69 | quarters: 0.05 → 0.05 → 0.05 → 0.05

Numbers say: the long stroke does not run out of paint.

## Impasto
Heavy acrylic · 22 px · 14.2 s

![Impasto](Impasto.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 8 % → 8 % | 0.71 | 0.93 | 43 |
| heavy line | 10 % → 9 % | 0.70 | 0.94 | 91 |
| pressure swell | 7 % → 7 % | 0.72 | 0.94 | 50 |
| fast wave | 20 % → 13 % | 0.71 | 0.64 | 154 |
| slow wave | 21 % → 14 % | 0.71 | 0.66 | 244 |
| spiral | 30 % → 14 % | 0.71 | 0.46 | 267 |
| loop | 18 % → 14 % | 0.71 | 0.77 | 143 |
| tilted | 8 % → 8 % | 0.70 | 1.00 | 72 |
| over the wet one | 17 % → 15 % | 0.70 | 0.91 | 66 |
| long, no reload | 34 % → 14 % | 0.71 | 0.41 | 379 | quarters: 0.38 → 0.21 → 0.10 → 0.03

## Oil Round
Oil · 18 px · 16.2 s

![Oil Round](Oil-Round.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 2 % → 2 % | 0.71 | 1.00 | 47 |
| heavy line | 6 % → 6 % | 0.72 | 1.00 | 74 |
| pressure swell | 3 % → 3 % | 0.63 | 1.00 | 40 |
| fast wave | 7 % → 7 % | 0.54 | 1.00 | 136 |
| slow wave | 4 % → 4 % | 0.36 | 1.00 | 162 |
| spiral | 5 % → 5 % | 0.21 | 1.00 | 213 |
| loop | 3 % → 3 % | 0.18 | 1.00 | 113 |
| tilted | 2 % → 2 % | 0.33 | 1.00 | 62 |
| over the wet one | 3 % → 3 % | 0.33 | 1.00 | 53 |
| long, no reload | 8 % → 8 % | 0.17 | 1.00 | 327 | quarters: 0.02 → 0.02 → 0.01 → 0.01

## Palette Knife
Oil · 20 px · 15.9 s

![Palette Knife](Palette-Knife.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 8 % → 8 % | 0.67 | 1.00 | 14 |
| heavy line | 8 % → 8 % | 0.73 | 1.00 | 15 |
| pressure swell | 6 % → 6 % | 0.74 | 1.00 | 6 |
| fast wave | 17 % → 17 % | 0.49 | 1.00 | 24 |
| slow wave | 17 % → 17 % | 0.43 | 1.00 | 35 |
| spiral | 18 % → 18 % | 0.45 | 1.00 | 46 |
| loop | 16 % → 16 % | 0.58 | 1.00 | 26 |
| tilted | 5 % → 5 % | 0.72 | 1.00 | 12 |
| over the wet one | 13 % → 13 % | 0.72 | 1.00 | 10 |
| long, no reload | 17 % → 17 % | 0.47 | 1.00 | 58 | quarters: 0.29 → 0.05 → 0.00 → 0.00

Numbers say: pressure barely changes the width.

## Water
Watercolor · 20 px · 33.1 s · over bands of wet oil paint and oil pastel in turn (it works on paint already there: look at what it does to the bands; covered counts the bands too)

![Water](Water.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 25 % → 26 % | 0.78 | 1.07 | 24 |
| heavy line | 23 % → 24 % | 0.80 | 1.04 | 54 |
| pressure swell | 23 % → 24 % | 0.80 | 1.03 | 32 |
| fast wave | 23 % → 25 % | 0.80 | 1.07 | 140 |
| slow wave | 23 % → 25 % | 0.80 | 1.06 | 199 |
| spiral | 23 % → 25 % | 0.79 | 1.08 | 163 |
| loop | 23 % → 24 % | 0.80 | 1.03 | 85 |
| tilted | 23 % → 23 % | 0.80 | 1.00 | 54 |
| over the wet one | 23 % → 25 % | 0.80 | 1.07 | 40 |
| long, no reload | 23 % → 25 % | 0.80 | 1.08 | 258 | quarters: 0.21 → 0.26 → 0.17 → 0.25

Numbers say: pressure barely changes the width; the long stroke does not run out of paint.

## Blender
Pastel · 16 px · 20.5 s · over bands of wet oil paint and oil pastel in turn (it works on paint already there: look at what it does to the bands; covered counts the bands too)

![Blender](Blender.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 24 % → 24 % | 0.80 | 1.00 | 20 |
| heavy line | 24 % → 24 % | 0.80 | 1.00 | 34 |
| pressure swell | 24 % → 24 % | 0.80 | 1.00 | 20 |
| fast wave | 25 % → 25 % | 0.78 | 1.00 | 80 |
| slow wave | 25 % → 25 % | 0.78 | 1.00 | 82 |
| spiral | 27 % → 27 % | 0.76 | 1.00 | 116 |
| loop | 25 % → 25 % | 0.79 | 1.00 | 60 |
| tilted | 24 % → 24 % | 0.78 | 1.00 | 53 |
| over the wet one | 25 % → 25 % | 0.78 | 1.00 | 35 |
| long, no reload | 29 % → 29 % | 0.74 | 1.00 | 242 | quarters: 0.19 → 0.26 → 0.21 → 0.28

Numbers say: pressure barely changes the width; the long stroke does not run out of paint.

## Eraser
Eraser · 16 px · 20.6 s · over bands of wet oil paint and oil pastel in turn (it works on paint already there: look at what it does to the bands; covered counts the bands too)

![Eraser](Eraser.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 23 % → 23 % | 0.81 | 1.00 | 23 |
| heavy line | 23 % → 23 % | 0.81 | 1.00 | 32 |
| pressure swell | 23 % → 23 % | 0.81 | 1.00 | 21 |
| fast wave | 22 % → 22 % | 0.81 | 1.00 | 75 |
| slow wave | 22 % → 22 % | 0.81 | 1.00 | 83 |
| spiral | 21 % → 21 % | 0.81 | 1.00 | 114 |
| loop | 22 % → 22 % | 0.81 | 1.00 | 68 |
| tilted | 23 % → 23 % | 0.81 | 1.00 | 54 |
| over the wet one | 22 % → 22 % | 0.81 | 1.00 | 44 |
| long, no reload | 19 % → 19 % | 0.81 | 1.00 | 247 | quarters: 0.15 → 0.19 → 0.14 → 0.20

Numbers say: pressure barely changes the width; the long stroke does not run out of paint.

## Fan
Gouache · 30 px · 25.8 s

![Fan](Fan.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 9 % → 3 % | 0.63 | 0.37 | 27 |
| heavy line | 11 % → 4 % | 0.63 | 0.39 | 50 |
| pressure swell | 8 % → 5 % | 0.63 | 0.55 | 30 |
| fast wave | 18 % → 5 % | 0.63 | 0.26 | 101 |
| slow wave | 18 % → 5 % | 0.63 | 0.25 | 163 |
| spiral | 24 % → 5 % | 0.63 | 0.20 | 158 |
| loop | 17 % → 5 % | 0.63 | 0.29 | 86 |
| tilted | 5 % → 6 % | 0.63 | 1.05 | 37 |
| over the wet one | 16 % → 8 % | 0.63 | 0.50 | 40 |
| long, no reload | 23 % → 5 % | 0.63 | 0.22 | 237 | quarters: 0.29 → 0.07 → 0.01 → 0.00

## Sponge
Gouache · 30 px · 25.7 s

![Sponge](Sponge.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 4 % → 0 % | 0.62 | 0.12 | 33 |
| heavy line | 12 % → 2 % | 0.62 | 0.14 | 61 |
| pressure swell | 7 % → 2 % | 0.62 | 0.27 | 40 |
| fast wave | 20 % → 4 % | 0.62 | 0.19 | 118 |
| slow wave | 21 % → 4 % | 0.62 | 0.18 | 218 |
| spiral | 28 % → 4 % | 0.62 | 0.14 | 196 |
| loop | 18 % → 5 % | 0.62 | 0.29 | 100 |
| tilted | 7 % → 7 % | 0.62 | 1.04 | 84 |
| over the wet one | 16 % → 6 % | 0.62 | 0.37 | 52 |
| long, no reload | 29 % → 5 % | 0.62 | 0.17 | 278 | quarters: 0.29 → 0.13 → 0.07 → 0.04

## Ink — sumi brush
Watercolor · 22 px · 25.1 s

![Ink — sumi brush](Ink-sumi-brush.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 6 % → 7 % | 0.46 | 1.06 | 53 |
| heavy line | 10 % → 11 % | 0.38 | 1.05 | 59 |
| pressure swell | 7 % → 8 % | 0.42 | 1.04 | 41 |
| fast wave | 21 % → 21 % | 0.32 | 1.00 | 148 |
| slow wave | 19 % → 19 % | 0.37 | 1.01 | 222 |
| spiral | 28 % → 26 % | 0.30 | 0.92 | 243 |
| loop | 17 % → 18 % | 0.37 | 1.06 | 133 |
| tilted | 6 % → 7 % | 0.40 | 1.17 | 64 |
| over the wet one | 16 % → 16 % | 0.40 | 1.01 | 56 |
| long, no reload | 33 % → 29 % | 0.30 | 0.86 | 342 | quarters: 0.23 → 0.11 → 0.06 → 0.04

## Ink — wash
Watercolor · 40 px · 33.4 s

![Ink — wash](Ink-wash.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 8 % → 9 % | 0.05 | 1.26 | 62 |
| heavy line | 11 % → 13 % | 0.04 | 1.22 | 74 |
| pressure swell | 7 % → 9 % | 0.05 | 1.25 | 53 |
| fast wave | 22 % → 27 % | 0.04 | 1.21 | 176 |
| slow wave | 21 % → 26 % | 0.06 | 1.23 | 297 |
| spiral | 34 % → 41 % | 0.04 | 1.21 | 295 |
| loop | 19 % → 24 % | 0.05 | 1.25 | 172 |
| tilted | 7 % → 9 % | 0.05 | 1.21 | 98 |
| over the wet one | 18 % → 21 % | 0.05 | 1.18 | 72 |
| long, no reload | 39 % → 46 % | 0.05 | 1.19 | 475 | quarters: 0.04 → 0.03 → 0.02 → 0.01

## Ink — dry brush
Ink · 30 px · 24.6 s

![Ink — dry brush](Ink-dry-brush.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 9 % → 7 % | 0.81 | 0.78 | 80 |
| heavy line | 11 % → 8 % | 0.80 | 0.73 | 107 |
| pressure swell | 8 % → 7 % | 0.81 | 0.85 | 66 |
| fast wave | 22 % → 8 % | 0.78 | 0.38 | 198 |
| slow wave | 18 % → 6 % | 0.80 | 0.36 | 335 |
| spiral | 23 % → 8 % | 0.77 | 0.35 | 323 |
| loop | 20 % → 8 % | 0.77 | 0.41 | 212 |
| tilted | 9 % → 9 % | 0.78 | 1.01 | 108 |
| over the wet one | 19 % → 14 % | 0.78 | 0.75 | 80 |
| long, no reload | 20 % → 9 % | 0.78 | 0.42 | 549 | quarters: 0.32 → 0.01 → 0.00 → 0.00

## Ink — nib
Watercolor · 5 px · 22.2 s

![Ink — nib](Ink-nib.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 2 % → 2 % | 0.76 | 1.17 | 25 |
| heavy line | 2 % → 2 % | 0.77 | 1.16 | 24 |
| pressure swell | 1 % → 2 % | 0.78 | 1.22 | 18 |
| fast wave | 4 % → 4 % | 0.66 | 1.09 | 59 |
| slow wave | 4 % → 4 % | 0.68 | 1.11 | 64 |
| spiral | 6 % → 6 % | 0.58 | 1.08 | 114 |
| loop | 3 % → 4 % | 0.69 | 1.12 | 55 |
| tilted | 2 % → 2 % | 0.64 | 1.21 | 28 |
| over the wet one | 4 % → 4 % | 0.64 | 1.03 | 25 |
| long, no reload | 7 % → 7 % | 0.53 | 1.02 | 165 | quarters: 0.09 → 0.04 → 0.03 → 0.02

## 0.45 · Dry brush
Gouache · 34 px · 30.5 s

![0.45 · Dry brush](0-45-Dry-brush.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 11 % → 3 % | 0.67 | 0.28 | 143 |
| heavy line | 12 % → 3 % | 0.67 | 0.30 | 130 |
| pressure swell | 9 % → 4 % | 0.67 | 0.40 | 77 |
| fast wave | 20 % → 4 % | 0.67 | 0.19 | 285 |
| slow wave | 20 % → 4 % | 0.67 | 0.18 | 534 |
| spiral | 21 % → 4 % | 0.67 | 0.17 | 480 |
| loop | 21 % → 4 % | 0.67 | 0.19 | 246 |
| tilted | 9 % → 9 % | 0.67 | 0.97 | 140 |
| over the wet one | 20 % → 7 % | 0.67 | 0.33 | 115 |
| long, no reload | 20 % → 4 % | 0.67 | 0.21 | 1044 | quarters: 0.38 → 0.07 → 0.00 → 0.00

Numbers say: pressure barely changes the width.

## Dry pastel
Pastel · 26 px · 11.8 s

![Dry pastel](Dry-pastel.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 5 % → 5 % | 0.36 | 1.00 | 33 |
| heavy line | 6 % → 6 % | 0.36 | 1.00 | 39 |
| pressure swell | 5 % → 5 % | 0.36 | 1.00 | 26 |
| fast wave | 15 % → 15 % | 0.36 | 1.00 | 85 |
| slow wave | 14 % → 14 % | 0.36 | 1.00 | 139 |
| spiral | 23 % → 23 % | 0.36 | 1.00 | 153 |
| loop | 11 % → 11 % | 0.36 | 1.00 | 75 |
| tilted | 5 % → 5 % | 0.37 | 1.00 | 43 |
| over the wet one | 10 % → 10 % | 0.37 | 1.00 | 54 |
| long, no reload | 26 % → 26 % | 0.36 | 1.00 | 207 | quarters: 0.11 → 0.10 → 0.10 → 0.11

Numbers say: the long stroke does not run out of paint.

## 0.45 · Charcoal
Charcoal · 18 px · 14.6 s

![0.45 · Charcoal](0-45-Charcoal.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 4 % → 4 % | 0.79 | 1.00 | 40 |
| heavy line | 4 % → 4 % | 0.79 | 1.00 | 27 |
| pressure swell | 4 % → 4 % | 0.79 | 1.00 | 21 |
| fast wave | 11 % → 11 % | 0.79 | 1.00 | 70 |
| slow wave | 11 % → 11 % | 0.78 | 1.00 | 120 |
| spiral | 20 % → 20 % | 0.79 | 1.00 | 94 |
| loop | 10 % → 10 % | 0.79 | 1.00 | 43 |
| tilted | 4 % → 4 % | 0.78 | 1.00 | 22 |
| over the wet one | 9 % → 9 % | 0.78 | 1.00 | 16 |
| long, no reload | 26 % → 26 % | 0.79 | 1.00 | 124 | quarters: 0.23 → 0.22 → 0.23 → 0.24

Numbers say: pressure barely changes the width; the long stroke does not run out of paint.

## Watercolour — wash
Watercolor · 50 px · 41.2 s

![Watercolour — wash](Watercolour-wash.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 9 % → 11 % | 0.01 | 1.22 | 124 |
| heavy line | 12 % → 14 % | 0.01 | 1.17 | 110 |
| pressure swell | 8 % → 10 % | 0.01 | 1.22 | 83 |
| fast wave | 26 % → 30 % | 0.01 | 1.18 | 337 |
| slow wave | 25 % → 29 % | 0.01 | 1.18 | 804 |
| spiral | 39 % → 46 % | 0.01 | 1.17 | 924 |
| loop | 22 % → 27 % | 0.01 | 1.21 | 328 |
| tilted | 10 % → 11 % | 0.01 | 1.18 | 239 |
| over the wet one | 22 % → 25 % | 0.01 | 1.14 | 168 |
| long, no reload | 45 % → 54 % | 0.01 | 1.18 | 762 | quarters: 0.01 → 0.01 → 0.01 → 0.00

## Watercolour — wet-in-wet
Watercolor · 44 px · 35.1 s

![Watercolour — wet-in-wet](Watercolour-wet-in-wet.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 7 % → 9 % | 0.02 | 1.26 | 120 |
| heavy line | 10 % → 12 % | 0.02 | 1.22 | 92 |
| pressure swell | 7 % → 9 % | 0.02 | 1.21 | 71 |
| fast wave | 23 % → 27 % | 0.02 | 1.17 | 254 |
| slow wave | 22 % → 26 % | 0.02 | 1.18 | 378 |
| spiral | 36 % → 43 % | 0.02 | 1.20 | 478 |
| loop | 19 % → 23 % | 0.02 | 1.20 | 230 |
| tilted | 7 % → 9 % | 0.02 | 1.19 | 152 |
| over the wet one | 17 % → 19 % | 0.02 | 1.12 | 113 |
| long, no reload | 42 % → 49 % | 0.02 | 1.18 | 754 | quarters: 0.01 → 0.01 → 0.01 → 0.01

## Watercolour — glaze
Watercolor · 38 px · 31.9 s

![Watercolour — glaze](Watercolour-glaze.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 7 % → 9 % | 0.01 | 1.28 | 109 |
| heavy line | 10 % → 13 % | 0.01 | 1.25 | 93 |
| pressure swell | 7 % → 9 % | 0.01 | 1.29 | 90 |
| fast wave | 20 % → 25 % | 0.01 | 1.24 | 258 |
| slow wave | 19 % → 24 % | 0.01 | 1.26 | 391 |
| spiral | 31 % → 37 % | 0.01 | 1.21 | 564 |
| loop | 18 % → 23 % | 0.01 | 1.27 | 247 |
| tilted | 7 % → 8 % | 0.01 | 1.20 | 123 |
| over the wet one | 17 % → 20 % | 0.01 | 1.19 | 71 |
| long, no reload | 36 % → 42 % | 0.01 | 1.17 | 425 | quarters: 0.01 → 0.00 → 0.00 → 0.00

## Watercolour — granulating
Watercolor · 44 px · 29.8 s

![Watercolour — granulating](Watercolour-granulating.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 8 % → 10 % | 0.02 | 1.18 | 77 |
| heavy line | 12 % → 14 % | 0.01 | 1.15 | 84 |
| pressure swell | 8 % → 10 % | 0.02 | 1.18 | 72 |
| fast wave | 25 % → 29 % | 0.01 | 1.15 | 211 |
| slow wave | 24 % → 27 % | 0.02 | 1.16 | 338 |
| spiral | 39 % → 44 % | 0.01 | 1.15 | 346 |
| loop | 22 % → 25 % | 0.01 | 1.17 | 166 |
| tilted | 9 % → 11 % | 0.02 | 1.15 | 148 |
| over the wet one | 21 % → 23 % | 0.02 | 1.11 | 116 |
| long, no reload | 45 % → 52 % | 0.01 | 1.15 | 542 | quarters: 0.01 → 0.01 → 0.01 → 0.01

## Watercolour — dry brush
Watercolor · 36 px · 25.7 s

![Watercolour — dry brush](Watercolour-dry-brush.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 7 % → 8 % | 0.05 | 1.07 | 110 |
| heavy line | 11 % → 12 % | 0.04 | 1.03 | 129 |
| pressure swell | 9 % → 10 % | 0.05 | 1.07 | 89 |
| fast wave | 21 % → 14 % | 0.04 | 0.68 | 224 |
| slow wave | 19 % → 13 % | 0.04 | 0.70 | 568 |
| spiral | 24 % → 15 % | 0.04 | 0.61 | 405 |
| loop | 17 % → 14 % | 0.04 | 0.85 | 204 |
| tilted | 7 % → 8 % | 0.05 | 1.19 | 102 |
| over the wet one | 17 % → 17 % | 0.05 | 0.99 | 91 |
| long, no reload | 22 % → 15 % | 0.04 | 0.68 | 571 | quarters: 0.02 → 0.00 → 0.00 → 0.00

## Gouache
Gouache · 30 px · 24.3 s

![Gouache](Gouache.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 8 % → 6 % | 0.14 | 0.67 | 88 |
| heavy line | 13 % → 6 % | 0.14 | 0.47 | 100 |
| pressure swell | 10 % → 6 % | 0.14 | 0.61 | 53 |
| fast wave | 27 % → 7 % | 0.14 | 0.27 | 177 |
| slow wave | 27 % → 7 % | 0.14 | 0.27 | 307 |
| spiral | 37 % → 8 % | 0.14 | 0.22 | 301 |
| loop | 22 % → 8 % | 0.14 | 0.36 | 160 |
| tilted | 9 % → 9 % | 0.14 | 1.02 | 83 |
| over the wet one | 20 % → 13 % | 0.14 | 0.67 | 74 |
| long, no reload | 38 % → 10 % | 0.14 | 0.25 | 429 | quarters: 0.07 → 0.04 → 0.01 → 0.01

## Oil — alla prima
Oil · 30 px · 29.1 s

![Oil — alla prima](Oil-alla-prima.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 9 % → 9 % | 0.50 | 1.00 | 97 |
| heavy line | 10 % → 10 % | 0.50 | 1.00 | 124 |
| pressure swell | 8 % → 8 % | 0.52 | 1.00 | 69 |
| fast wave | 24 % → 24 % | 0.49 | 1.00 | 192 |
| slow wave | 25 % → 25 % | 0.50 | 1.00 | 370 |
| spiral | 38 % → 38 % | 0.44 | 1.00 | 411 |
| loop | 21 % → 21 % | 0.50 | 1.00 | 449 |
| tilted | 11 % → 11 % | 0.50 | 1.00 | 193 |
| over the wet one | 20 % → 20 % | 0.50 | 1.00 | 164 |
| long, no reload | 46 % → 46 % | 0.40 | 1.00 | 577 | quarters: 0.31 → 0.24 → 0.17 → 0.10

Numbers say: pressure barely changes the width.

## Oil — impasto
Oil · 34 px · 28.0 s

![Oil — impasto](Oil-impasto.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 11 % → 11 % | 0.24 | 1.00 | 128 |
| heavy line | 12 % → 12 % | 0.23 | 1.00 | 97 |
| pressure swell | 9 % → 9 % | 0.25 | 1.00 | 95 |
| fast wave | 29 % → 29 % | 0.21 | 1.00 | 285 |
| slow wave | 29 % → 29 % | 0.21 | 1.00 | 511 |
| spiral | 48 % → 48 % | 0.17 | 1.00 | 686 |
| loop | 25 % → 25 % | 0.21 | 1.00 | 443 |
| tilted | 12 % → 12 % | 0.24 | 1.00 | 283 |
| over the wet one | 23 % → 23 % | 0.24 | 1.00 | 132 |
| long, no reload | 55 % → 55 % | 0.15 | 1.00 | 759 | quarters: 0.16 → 0.11 → 0.06 → 0.02

Numbers say: pressure barely changes the width.

## Oil — glaze
Oil · 40 px · 23.5 s

![Oil — glaze](Oil-glaze.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 10 % → 10 % | 0.49 | 1.00 | 101 |
| heavy line | 14 % → 14 % | 0.48 | 1.00 | 113 |
| pressure swell | 10 % → 10 % | 0.49 | 1.00 | 159 |
| fast wave | 28 % → 28 % | 0.46 | 1.00 | 401 |
| slow wave | 30 % → 30 % | 0.46 | 1.00 | 767 |
| spiral | 42 % → 42 % | 0.44 | 1.00 | 770 |
| loop | 24 % → 24 % | 0.47 | 1.00 | 235 |
| tilted | 11 % → 11 % | 0.47 | 1.00 | 117 |
| over the wet one | 23 % → 23 % | 0.47 | 1.00 | 118 |
| long, no reload | 47 % → 47 % | 0.43 | 1.00 | 786 | quarters: 0.33 → 0.24 → 0.18 → 0.14

## Oil — scumble
Oil · 36 px · 28.2 s

![Oil — scumble](Oil-scumble.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 11 % → 11 % | 0.06 | 1.00 | 260 |
| heavy line | 12 % → 12 % | 0.05 | 1.00 | 154 |
| pressure swell | 9 % → 9 % | 0.06 | 1.00 | 98 |
| fast wave | 18 % → 18 % | 0.04 | 1.00 | 481 |
| slow wave | 20 % → 20 % | 0.04 | 1.00 | 820 |
| spiral | 19 % → 19 % | 0.03 | 1.00 | 751 |
| loop | 22 % → 22 % | 0.04 | 1.00 | 340 |
| tilted | 10 % → 10 % | 0.05 | 1.00 | 172 |
| over the wet one | 21 % → 21 % | 0.05 | 1.00 | 162 |
| long, no reload | 18 % → 18 % | 0.04 | 1.00 | 1020 | quarters: 0.03 → 0.00 → 0.00 → 0.00

Numbers say: pressure barely changes the width.

## Acrylic — heavy body
Heavy acrylic · 30 px · 21.3 s

![Acrylic — heavy body](Acrylic-heavy-body.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 10 % → 9 % | 0.51 | 0.93 | 159 |
| heavy line | 11 % → 10 % | 0.51 | 0.93 | 104 |
| pressure swell | 8 % → 8 % | 0.52 | 0.94 | 127 |
| fast wave | 24 % → 14 % | 0.51 | 0.58 | 333 |
| slow wave | 25 % → 15 % | 0.51 | 0.59 | 450 |
| spiral | 37 % → 15 % | 0.51 | 0.40 | 473 |
| loop | 22 % → 16 % | 0.51 | 0.73 | 281 |
| tilted | 10 % → 10 % | 0.51 | 1.00 | 141 |
| over the wet one | 20 % → 17 % | 0.51 | 0.88 | 142 |
| long, no reload | 39 % → 15 % | 0.51 | 0.40 | 701 | quarters: 0.30 → 0.20 → 0.10 → 0.02

Numbers say: pressure barely changes the width.

## Acrylic — fluid
Watercolor · 36 px · 40.2 s

![Acrylic — fluid](Acrylic-fluid.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 9 % → 10 % | 0.06 | 1.11 | 110 |
| heavy line | 13 % → 14 % | 0.05 | 1.07 | 145 |
| pressure swell | 9 % → 10 % | 0.07 | 1.09 | 63 |
| fast wave | 26 % → 28 % | 0.05 | 1.07 | 285 |
| slow wave | 24 % → 26 % | 0.07 | 1.08 | 391 |
| spiral | 39 % → 41 % | 0.05 | 1.06 | 429 |
| loop | 22 % → 25 % | 0.06 | 1.11 | 196 |
| tilted | 8 % → 9 % | 0.07 | 1.17 | 230 |
| over the wet one | 21 % → 22 % | 0.07 | 1.05 | 112 |
| long, no reload | 44 % → 47 % | 0.05 | 1.06 | 1009 | quarters: 0.05 → 0.03 → 0.02 → 0.01

## Acrylic — palette knife
Heavy acrylic · 42 px · 24.5 s

![Acrylic — palette knife](Acrylic-palette-knife.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 15 % → 15 % | 0.06 | 0.98 | 36 |
| heavy line | 15 % → 15 % | 0.05 | 0.98 | 30 |
| pressure swell | 12 % → 12 % | 0.06 | 0.99 | 21 |
| fast wave | 37 % → 20 % | 0.06 | 0.54 | 132 |
| slow wave | 37 % → 21 % | 0.06 | 0.56 | 135 |
| spiral | 48 % → 19 % | 0.06 | 0.38 | 113 |
| loop | 32 % → 24 % | 0.05 | 0.75 | 82 |
| tilted | 12 % → 12 % | 0.05 | 1.00 | 20 |
| over the wet one | 26 % → 26 % | 0.05 | 0.98 | 24 |
| long, no reload | 55 % → 20 % | 0.06 | 0.36 | 141 | quarters: 0.04 → 0.02 → 0.00 → 0.00

Numbers say: pressure barely changes the width.

## Finger on oil
Oil · 30 px · 17.8 s

![Finger on oil](Finger-on-oil.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 8 % → 8 % | 0.34 | 1.00 | 61 |
| heavy line | 12 % → 12 % | 0.30 | 1.00 | 82 |
| pressure swell | 8 % → 8 % | 0.35 | 1.00 | 46 |
| fast wave | 16 % → 16 % | 0.22 | 1.00 | 128 |
| slow wave | 17 % → 17 % | 0.23 | 1.00 | 228 |
| spiral | 18 % → 18 % | 0.22 | 1.00 | 235 |
| loop | 18 % → 18 % | 0.23 | 1.00 | 124 |
| tilted | 9 % → 9 % | 0.31 | 1.00 | 96 |
| over the wet one | 18 % → 18 % | 0.31 | 1.00 | 57 |
| long, no reload | 15 % → 15 % | 0.23 | 1.00 | 352 | quarters: 0.13 → 0.01 → 0.00 → 0.00

## Palette knife — oil
Oil · 44 px · 25.9 s

![Palette knife — oil](Palette-knife-oil.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 16 % → 16 % | 0.10 | 1.00 | 49 |
| heavy line | 16 % → 16 % | 0.09 | 1.00 | 22 |
| pressure swell | 12 % → 12 % | 0.10 | 1.00 | 14 |
| fast wave | 39 % → 39 % | 0.07 | 1.00 | 83 |
| slow wave | 39 % → 39 % | 0.07 | 1.00 | 112 |
| spiral | 54 % → 54 % | 0.05 | 1.00 | 135 |
| loop | 34 % → 34 % | 0.08 | 1.00 | 56 |
| tilted | 13 % → 13 % | 0.09 | 1.00 | 23 |
| over the wet one | 28 % → 28 % | 0.09 | 1.00 | 43 |
| long, no reload | 65 % → 65 % | 0.05 | 1.00 | 288 | quarters: 0.08 → 0.04 → 0.01 → 0.00

Numbers say: pressure barely changes the width.

## 0.45 · Sponge
Watercolor · 46 px · 33.2 s

![0.45 · Sponge](0-45-Sponge.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 11 % → 0 % | 0.00 | 0.00 | 61 |
| heavy line | 13 % → 0 % | 0.01 | 0.00 | 78 |
| pressure swell | 9 % → 1 % | 0.02 | 0.14 | 55 |
| fast wave | 23 % → 2 % | 0.01 | 0.08 | 303 |
| slow wave | 26 % → 8 % | 0.02 | 0.30 | 809 |
| spiral | 34 % → 11 % | 0.02 | 0.32 | 303 |
| loop | 22 % → 4 % | 0.02 | 0.19 | 147 |
| tilted | 9 % → 10 % | 0.04 | 1.19 | 121 |
| over the wet one | 22 % → 10 % | 0.04 | 0.44 | 74 |
| long, no reload | 41 % → 19 % | 0.02 | 0.47 | 445 | quarters: 0.01 → 0.01 → 0.01 → 0.01

## 0.45 · Eraser
Eraser · 30 px · 28.8 s · over bands of wet oil paint and oil pastel in turn (it works on paint already there: look at what it does to the bands; covered counts the bands too)

![0.45 · Eraser](0-45-Eraser.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 23 % → 23 % | 0.81 | 1.00 | 41 |
| heavy line | 22 % → 22 % | 0.81 | 1.00 | 55 |
| pressure swell | 22 % → 22 % | 0.81 | 1.00 | 58 |
| fast wave | 21 % → 21 % | 0.80 | 1.00 | 153 |
| slow wave | 20 % → 20 % | 0.81 | 1.00 | 263 |
| spiral | 20 % → 20 % | 0.79 | 1.00 | 265 |
| loop | 21 % → 21 % | 0.79 | 1.00 | 136 |
| tilted | 22 % → 22 % | 0.80 | 1.00 | 59 |
| over the wet one | 21 % → 21 % | 0.80 | 1.00 | 52 |
| long, no reload | 16 % → 16 % | 0.79 | 1.00 | 392 | quarters: 0.13 → 0.15 → 0.12 → 0.16

Numbers say: pressure barely changes the width; the long stroke does not run out of paint.

## Lift wet paint
Eraser · 30 px · 25.6 s · over bands of wet oil paint and oil pastel in turn (it works on paint already there: look at what it does to the bands; covered counts the bands too)

![Lift wet paint](Lift-wet-paint.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 23 % → 23 % | 0.81 | 1.00 | 60 |
| heavy line | 23 % → 23 % | 0.81 | 1.00 | 63 |
| pressure swell | 23 % → 23 % | 0.81 | 1.00 | 40 |
| fast wave | 23 % → 23 % | 0.81 | 1.00 | 139 |
| slow wave | 23 % → 23 % | 0.81 | 1.00 | 368 |
| spiral | 23 % → 23 % | 0.81 | 1.00 | 242 |
| loop | 23 % → 23 % | 0.81 | 1.00 | 158 |
| tilted | 23 % → 23 % | 0.81 | 1.00 | 82 |
| over the wet one | 23 % → 23 % | 0.81 | 1.00 | 60 |
| long, no reload | 23 % → 23 % | 0.81 | 1.00 | 369 | quarters: 0.18 → 0.23 → 0.16 → 0.23

Numbers say: pressure barely changes the width; the long stroke does not run out of paint.

## Sgraffito
Eraser · 10 px · 23.4 s · over bands of wet oil paint and oil pastel in turn (it works on paint already there: look at what it does to the bands; covered counts the bands too)

![Sgraffito](Sgraffito.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 23 % → 23 % | 0.80 | 1.00 | 19 |
| heavy line | 23 % → 23 % | 0.81 | 1.00 | 10 |
| pressure swell | 23 % → 23 % | 0.81 | 1.00 | 6 |
| fast wave | 23 % → 23 % | 0.81 | 1.00 | 19 |
| slow wave | 23 % → 23 % | 0.81 | 1.00 | 19 |
| spiral | 23 % → 23 % | 0.81 | 1.00 | 41 |
| loop | 23 % → 23 % | 0.81 | 1.00 | 22 |
| tilted | 23 % → 23 % | 0.81 | 1.00 | 10 |
| over the wet one | 23 % → 23 % | 0.81 | 1.00 | 8 |
| long, no reload | 23 % → 23 % | 0.81 | 1.00 | 56 | quarters: 0.17 → 0.23 → 0.16 → 0.23

Numbers say: pressure barely changes the width; the long stroke does not run out of paint.

## Brush Artist · Ink wash W2
Watercolor · 38 px · 36.5 s

![Brush Artist · Ink wash W2](Brush-Artist-Ink-wash-W2.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 11 % → 11 % | 0.39 | 1.03 | 98 |
| heavy line | 19 % → 19 % | 0.32 | 1.03 | 153 |
| pressure swell | 12 % → 13 % | 0.37 | 1.03 | 78 |
| fast wave | 40 % → 41 % | 0.31 | 1.04 | 207 |
| slow wave | 37 % → 38 % | 0.37 | 1.03 | 330 |
| spiral | 59 % → 61 % | 0.31 | 1.04 | 339 |
| loop | 32 % → 33 % | 0.35 | 1.02 | 191 |
| tilted | 13 % → 14 % | 0.38 | 1.04 | 140 |
| over the wet one | 29 % → 30 % | 0.38 | 1.04 | 132 |
| long, no reload | 67 % → 73 % | 0.29 | 1.09 | 806 | quarters: 0.34 → 0.27 → 0.19 → 0.12

## Brush Artist · Ink wash W4 wetter
Watercolor · 40 px · 38.7 s

![Brush Artist · Ink wash W4 wetter](Brush-Artist-Ink-wash-W4-wetter.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 11 % → 12 % | 0.41 | 1.04 | 66 |
| heavy line | 19 % → 19 % | 0.35 | 1.03 | 93 |
| pressure swell | 12 % → 12 % | 0.40 | 1.03 | 59 |
| fast wave | 39 % → 40 % | 0.34 | 1.03 | 192 |
| slow wave | 37 % → 38 % | 0.43 | 1.03 | 356 |
| spiral | 61 % → 62 % | 0.35 | 1.02 | 341 |
| loop | 32 % → 33 % | 0.39 | 1.02 | 181 |
| tilted | 13 % → 14 % | 0.42 | 1.04 | 146 |
| over the wet one | 29 % → 30 % | 0.42 | 1.05 | 86 |
| long, no reload | 71 % → 75 % | 0.34 | 1.06 | 465 | quarters: 0.37 → 0.32 → 0.24 → 0.16

## Brush Artist · Ink dry F1
Ink · 30 px · 28.6 s

![Brush Artist · Ink dry F1](Brush-Artist-Ink-dry-F1.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 8 % → 6 % | 0.83 | 0.78 | 89 |
| heavy line | 10 % → 8 % | 0.82 | 0.82 | 154 |
| pressure swell | 7 % → 6 % | 0.82 | 0.92 | 115 |
| fast wave | 24 % → 12 % | 0.80 | 0.49 | 233 |
| slow wave | 22 % → 11 % | 0.81 | 0.49 | 379 |
| spiral | 37 % → 12 % | 0.80 | 0.33 | 427 |
| loop | 20 % → 12 % | 0.80 | 0.60 | 208 |
| tilted | 9 % → 9 % | 0.80 | 1.00 | 110 |
| over the wet one | 18 % → 15 % | 0.80 | 0.82 | 101 |
| long, no reload | 44 % → 14 % | 0.79 | 0.33 | 609 | quarters: 0.43 → 0.25 → 0.11 → 0.04

## Brush Artist · Ink dry F2
Ink · 30 px · 29.9 s

![Brush Artist · Ink dry F2](Brush-Artist-Ink-dry-F2.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 8 % → 7 % | 0.85 | 0.94 | 69 |
| heavy line | 10 % → 10 % | 0.84 | 0.94 | 153 |
| pressure swell | 7 % → 7 % | 0.84 | 0.98 | 85 |
| fast wave | 24 % → 16 % | 0.82 | 0.65 | 268 |
| slow wave | 23 % → 14 % | 0.82 | 0.62 | 687 |
| spiral | 38 % → 17 % | 0.81 | 0.44 | 863 |
| loop | 21 % → 16 % | 0.81 | 0.79 | 262 |
| tilted | 10 % → 10 % | 0.83 | 1.00 | 130 |
| over the wet one | 19 % → 17 % | 0.83 | 0.92 | 105 |
| long, no reload | 46 % → 18 % | 0.81 | 0.39 | 936 | quarters: 0.47 → 0.31 → 0.14 → 0.06

## Brush Artist · Ink dry F3
Ink · 30 px · 24.7 s

![Brush Artist · Ink dry F3](Brush-Artist-Ink-dry-F3.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 7 % → 5 % | 0.82 | 0.72 | 56 |
| heavy line | 10 % → 7 % | 0.81 | 0.76 | 124 |
| pressure swell | 7 % → 6 % | 0.81 | 0.86 | 76 |
| fast wave | 24 % → 12 % | 0.79 | 0.51 | 229 |
| slow wave | 23 % → 14 % | 0.80 | 0.59 | 407 |
| spiral | 39 % → 15 % | 0.77 | 0.37 | 408 |
| loop | 20 % → 14 % | 0.78 | 0.69 | 269 |
| tilted | 9 % → 9 % | 0.78 | 1.00 | 147 |
| over the wet one | 18 % → 14 % | 0.78 | 0.80 | 127 |
| long, no reload | 48 % → 18 % | 0.77 | 0.37 | 959 | quarters: 0.43 → 0.32 → 0.20 → 0.11

## Brush Artist · Ink dry F2 · Krovostok ear
Ink · 30 px · 25.8 s

![Brush Artist · Ink dry F2 · Krovostok ear](Brush-Artist-Ink-dry-F2-Krovostok-ear.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 8 % → 7 % | 0.85 | 0.94 | 55 |
| heavy line | 10 % → 10 % | 0.84 | 0.94 | 129 |
| pressure swell | 7 % → 7 % | 0.84 | 0.98 | 88 |
| fast wave | 24 % → 16 % | 0.82 | 0.65 | 308 |
| slow wave | 23 % → 14 % | 0.82 | 0.62 | 441 |
| spiral | 38 % → 17 % | 0.81 | 0.44 | 651 |
| loop | 21 % → 16 % | 0.81 | 0.79 | 288 |
| tilted | 10 % → 10 % | 0.83 | 1.00 | 110 |
| over the wet one | 19 % → 17 % | 0.83 | 0.92 | 101 |
| long, no reload | 46 % → 18 % | 0.81 | 0.39 | 612 | quarters: 0.47 → 0.31 → 0.14 → 0.06

## Brush Artist · Ink brush · caricature
Ink · 22 px · 30.8 s

![Brush Artist · Ink brush · caricature](Brush-Artist-Ink-brush-caricature.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 6 % → 7 % | 0.84 | 1.21 | 42 |
| heavy line | 17 % → 17 % | 0.89 | 0.99 | 77 |
| pressure swell | 10 % → 10 % | 0.88 | 1.02 | 66 |
| fast wave | 33 % → 32 % | 0.88 | 0.98 | 156 |
| slow wave | 28 % → 27 % | 0.88 | 0.99 | 224 |
| spiral | 45 % → 43 % | 0.88 | 0.96 | 245 |
| loop | 26 % → 26 % | 0.88 | 1.00 | 193 |
| tilted | 9 % → 9 % | 0.88 | 1.00 | 97 |
| over the wet one | 22 % → 22 % | 0.88 | 1.00 | 94 |
| long, no reload | 55 % → 50 % | 0.86 | 0.91 | 392 | quarters: 0.64 → 0.56 → 0.46 → 0.37

## Brush Artist · Watercolour wash V4
Watercolor · 46 px · 35.2 s

![Brush Artist · Watercolour wash V4](Brush-Artist-Watercolour-wash-V4.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 13 % → 13 % | 0.37 | 1.00 | 64 |
| heavy line | 22 % → 22 % | 0.32 | 0.99 | 108 |
| pressure swell | 14 % → 14 % | 0.37 | 1.00 | 70 |
| fast wave | 46 % → 46 % | 0.31 | 1.01 | 234 |
| slow wave | 44 % → 44 % | 0.40 | 1.00 | 402 |
| spiral | 65 % → 65 % | 0.34 | 1.00 | 397 |
| loop | 38 % → 38 % | 0.36 | 1.00 | 192 |
| tilted | 17 % → 17 % | 0.38 | 1.01 | 146 |
| over the wet one | 34 % → 34 % | 0.38 | 1.00 | 86 |
| long, no reload | 82 % → 82 % | 0.33 | 1.01 | 736 | quarters: 0.38 → 0.33 → 0.27 → 0.19

## Brush Artist · Watercolour wash V5
Watercolor · 46 px · 37.8 s

![Brush Artist · Watercolour wash V5](Brush-Artist-Watercolour-wash-V5.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 13 % → 13 % | 0.32 | 1.00 | 70 |
| heavy line | 22 % → 22 % | 0.27 | 0.99 | 111 |
| pressure swell | 14 % → 14 % | 0.31 | 1.00 | 81 |
| fast wave | 46 % → 46 % | 0.26 | 1.01 | 222 |
| slow wave | 44 % → 44 % | 0.34 | 1.00 | 492 |
| spiral | 65 % → 65 % | 0.29 | 1.00 | 610 |
| loop | 38 % → 38 % | 0.30 | 1.00 | 206 |
| tilted | 17 % → 17 % | 0.32 | 1.01 | 131 |
| over the wet one | 34 % → 34 % | 0.32 | 1.00 | 88 |
| long, no reload | 82 % → 82 % | 0.28 | 1.01 | 575 | quarters: 0.32 → 0.28 → 0.22 → 0.16

## Brush Artist · Watercolour wash V4 · Shrigley
Watercolor · 40 px · 38.1 s

![Brush Artist · Watercolour wash V4 · Shrigley](Brush-Artist-Watercolour-wash-V4-Shrigley.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 12 % → 12 % | 0.38 | 1.00 | 90 |
| heavy line | 20 % → 20 % | 0.32 | 1.00 | 145 |
| pressure swell | 12 % → 12 % | 0.37 | 1.01 | 60 |
| fast wave | 41 % → 41 % | 0.32 | 1.00 | 223 |
| slow wave | 39 % → 39 % | 0.39 | 1.00 | 331 |
| spiral | 62 % → 62 % | 0.33 | 1.00 | 370 |
| loop | 34 % → 34 % | 0.36 | 1.00 | 160 |
| tilted | 15 % → 15 % | 0.38 | 1.01 | 140 |
| over the wet one | 31 % → 31 % | 0.38 | 1.01 | 83 |
| long, no reload | 77 % → 77 % | 0.32 | 1.01 | 464 | quarters: 0.35 → 0.30 → 0.24 → 0.18

## Brush Artist · Gouache A
Gouache · 30 px · 38.8 s

![Brush Artist · Gouache A](Brush-Artist-Gouache-A.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 8 % → 8 % | 0.16 | 0.97 | 116 |
| heavy line | 15 % → 12 % | 0.16 | 0.78 | 102 |
| pressure swell | 11 % → 9 % | 0.16 | 0.85 | 64 |
| fast wave | 30 % → 14 % | 0.16 | 0.45 | 342 |
| slow wave | 29 % → 14 % | 0.16 | 0.47 | 397 |
| spiral | 40 % → 14 % | 0.16 | 0.35 | 390 |
| loop | 24 % → 15 % | 0.16 | 0.62 | 197 |
| tilted | 10 % → 10 % | 0.16 | 1.01 | 112 |
| over the wet one | 22 % → 19 % | 0.16 | 0.89 | 134 |
| long, no reload | 43 % → 15 % | 0.16 | 0.35 | 873 | quarters: 0.10 → 0.07 → 0.04 → 0.02

## Brush Artist · Oil A2
Oil · 30 px · 24.1 s

![Brush Artist · Oil A2](Brush-Artist-Oil-A2.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 9 % → 9 % | 0.53 | 1.00 | 125 |
| heavy line | 9 % → 9 % | 0.53 | 1.00 | 130 |
| pressure swell | 7 % → 7 % | 0.54 | 1.00 | 100 |
| fast wave | 23 % → 23 % | 0.53 | 1.00 | 359 |
| slow wave | 23 % → 23 % | 0.53 | 1.00 | 652 |
| spiral | 36 % → 36 % | 0.50 | 1.00 | 864 |
| loop | 19 % → 19 % | 0.54 | 1.00 | 355 |
| tilted | 11 % → 11 % | 0.53 | 1.00 | 169 |
| over the wet one | 19 % → 19 % | 0.53 | 1.00 | 141 |
| long, no reload | 47 % → 47 % | 0.45 | 1.00 | 888 | quarters: 0.31 → 0.27 → 0.22 → 0.14

Numbers say: pressure barely changes the width.

## Brush Artist · Charcoal C4
Charcoal · 30 px · 11.2 s

![Brush Artist · Charcoal C4](Brush-Artist-Charcoal-C4.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 6 % → 6 % | 0.82 | 1.00 | 36 |
| heavy line | 7 % → 7 % | 0.82 | 1.00 | 29 |
| pressure swell | 5 % → 5 % | 0.82 | 1.00 | 27 |
| fast wave | 17 % → 17 % | 0.82 | 1.00 | 71 |
| slow wave | 16 % → 16 % | 0.82 | 1.00 | 109 |
| spiral | 29 % → 29 % | 0.82 | 1.00 | 120 |
| loop | 14 % → 14 % | 0.82 | 1.00 | 49 |
| tilted | 6 % → 6 % | 0.82 | 1.00 | 35 |
| over the wet one | 13 % → 13 % | 0.82 | 1.00 | 27 |
| long, no reload | 36 % → 36 % | 0.82 | 1.00 | 155 | quarters: 0.34 → 0.32 → 0.33 → 0.34

Numbers say: pressure barely changes the width; the long stroke does not run out of paint.

## Brush Artist · Charcoal C5
Charcoal · 24 px · 10.1 s

![Brush Artist · Charcoal C5](Brush-Artist-Charcoal-C5.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 5 % → 5 % | 0.81 | 1.00 | 17 |
| heavy line | 6 % → 6 % | 0.82 | 1.00 | 21 |
| pressure swell | 4 % → 4 % | 0.82 | 1.00 | 16 |
| fast wave | 14 % → 14 % | 0.82 | 1.00 | 41 |
| slow wave | 14 % → 14 % | 0.82 | 1.00 | 83 |
| spiral | 24 % → 24 % | 0.82 | 1.00 | 74 |
| loop | 12 % → 12 % | 0.82 | 1.00 | 40 |
| tilted | 5 % → 5 % | 0.82 | 1.00 | 37 |
| over the wet one | 11 % → 11 % | 0.82 | 1.00 | 21 |
| long, no reload | 32 % → 32 % | 0.82 | 1.00 | 103 | quarters: 0.29 → 0.28 → 0.29 → 0.30

Numbers say: the long stroke does not run out of paint.

## Brush Artist · Charcoal C4 · Guston hand
Charcoal · 30 px · 10.7 s

![Brush Artist · Charcoal C4 · Guston hand](Brush-Artist-Charcoal-C4-Guston-hand.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 6 % → 6 % | 0.82 | 1.00 | 26 |
| heavy line | 7 % → 7 % | 0.82 | 1.00 | 38 |
| pressure swell | 5 % → 5 % | 0.82 | 1.00 | 22 |
| fast wave | 17 % → 17 % | 0.82 | 1.00 | 64 |
| slow wave | 16 % → 16 % | 0.82 | 1.00 | 88 |
| spiral | 29 % → 29 % | 0.82 | 1.00 | 88 |
| loop | 14 % → 14 % | 0.82 | 1.00 | 44 |
| tilted | 6 % → 6 % | 0.82 | 1.00 | 28 |
| over the wet one | 13 % → 13 % | 0.82 | 1.00 | 28 |
| long, no reload | 36 % → 36 % | 0.82 | 1.00 | 121 | quarters: 0.34 → 0.32 → 0.33 → 0.34

Numbers say: pressure barely changes the width; the long stroke does not run out of paint.

## Brush Artist · Ink dry F2 · Krovostok ear — own sheet
own sheet 600 × 600 · Ink · 30 px · 3.5 s

![Brush Artist · Ink dry F2 · Krovostok ear — own sheet](Brush-Artist-Ink-dry-F2-Krovostok-ear-own-sheet.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| ear | 27 % → 19 % | 0.70 | 0.70 | 571 |
| drag0 | 21 % → 32 % | 0.86 | 1.47 | 120 |
| drag1 | 28 % → 33 % | 0.86 | 1.20 | 102 |
| drag2 | 32 % → 34 % | 0.87 | 1.05 | 84 |
| drag3 | 36 % → 34 % | 0.86 | 0.93 | 67 |

## Brush Artist · Ink brush · caricature — own sheet
own sheet 600 × 600 · Ink · 22 px · 6.3 s

![Brush Artist · Ink brush · caricature — own sheet](Brush-Artist-Ink-brush-caricature-own-sheet.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| lens L | 44 % → 51 % | 0.89 | 1.14 | 169 |
| lens R | 44 % → 45 % | 0.89 | 1.00 | 113 |
| brow L | 38 % → 39 % | 0.89 | 1.02 | 62 |
| brow R | 42 % → 43 % | 0.89 | 1.01 | 50 |
| nose | 41 % → 41 % | 0.89 | 1.01 | 53 |
| beard0 | 33 % → 40 % | 0.89 | 1.19 | 14 |
| beard1 | 38 % → 44 % | 0.89 | 1.15 | 13 |
| beard2 | 38 % → 43 % | 0.89 | 1.13 | 15 |
| beard3 | 39 % → 43 % | 0.89 | 1.11 | 13 |
| beard4 | 38 % → 43 % | 0.89 | 1.13 | 17 |
| beard5 | 36 % → 42 % | 0.89 | 1.17 | 13 |
| beard6 | 35 % → 36 % | 0.89 | 1.02 | 13 |

## Brush Artist · Watercolour wash V4 · Shrigley — own sheet
own sheet 600 × 600 · Watercolor · 40 px · 13.2 s

![Brush Artist · Watercolour wash V4 · Shrigley — own sheet](Brush-Artist-Watercolour-wash-V4-Shrigley-own-sheet.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| s0 | 25 % → 38 % | 0.38 | 1.52 | 72 |
| s1 | 16 % → 48 % | 0.39 | 3.04 | 66 |
| s2 | 23 % → 32 % | 0.35 | 1.36 | 77 |
| s3 | 21 % → 27 % | 0.35 | 1.30 | 88 |
| s4 | 30 % → 44 % | 0.41 | 1.47 | 81 |
| s5 | 40 % → 41 % | 0.44 | 1.03 | 67 |
| s6 | 42 % → 42 % | 0.38 | 1.00 | 78 |
| s7 | 45 % → 46 % | 0.38 | 1.03 | 63 |
| s8 | 38 % → 38 % | 0.34 | 1.00 | 85 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Charcoal C4 · Guston hand — own sheet
own sheet 600 × 600 · Charcoal · 30 px · 1.4 s

![Brush Artist · Charcoal C4 · Guston hand — own sheet](Brush-Artist-Charcoal-C4-Guston-hand-own-sheet.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| finger0 | 19 % → 25 % | 0.82 | 1.30 | 50 |
| tip0 | 19 % → 27 % | 0.82 | 1.46 | 9 |
| finger1 | 20 % → 31 % | 0.82 | 1.54 | 43 |
| tip1 | 25 % → 33 % | 0.82 | 1.35 | 9 |
| finger2 | 20 % → 28 % | 0.82 | 1.41 | 30 |
| tip2 | 24 % → 33 % | 0.82 | 1.35 | 9 |
| finger3 | 20 % → 23 % | 0.82 | 1.13 | 33 |
| tip3 | 25 % → 25 % | 0.82 | 1.00 | 10 |
| cig0 | 41 % → 51 % | 0.83 | 1.26 | 15 |
| cig1 | 45 % → 56 % | 0.83 | 1.24 | 12 |
| cig2 | 49 % → 59 % | 0.83 | 1.21 | 12 |
| cig3 | 52 % → 60 % | 0.83 | 1.16 | 13 |
| cig4 | 52 % → 56 % | 0.83 | 1.08 | 17 |
| cig5 | 53 % → 53 % | 0.83 | 1.00 | 18 |

Numbers say: wet paint spreads well beyond the stroke.

