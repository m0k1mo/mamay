![All brushes](contact.png)

# Brush Lab — 53 brushes · Nov 3, 2026 at 11:25 AM

Every sheet: 1500 × 600, ten strokes in a 5 × 2 grid — 1. light line · 2. heavy line · 3. pressure swell · 4. fast wave · 5. slow wave · 6. spiral · 7. loop · 8. tilted · 9. over the wet one · 10. long, no reload (cell 8 holds «tilted» and «over the wet one» crossed). The CPU reference of Mamay's paint engine; the wet layer settles 20 s at the end.

Columns: **covered** = share of the cell with paint right after the stroke → after settling; **dark** = mean darkness of the painted pixels above the paper's own grain (0 = paper, 1 = black); **spread** = how far wet paint went beyond the stroke (1.0 = stayed); **ms** = the stroke on the CPU; long stroke: paint in each quarter of its length (it should run out: wet → streaks → dry tail).

## Ink Line
Ink · 12 px · 23.9 s

![Ink Line](Ink-Line.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 1 % → 4 % | 0.55 | 2.44 | 38 |
| heavy line | 5 % → 6 % | 0.68 | 1.13 | 66 |
| pressure swell | 3 % → 4 % | 0.64 | 1.40 | 40 |
| fast wave | 10 % → 11 % | 0.59 | 1.11 | 119 |
| slow wave | 8 % → 10 % | 0.57 | 1.16 | 114 |
| spiral | 14 % → 15 % | 0.50 | 1.07 | 246 |
| loop | 8 % → 9 % | 0.61 | 1.16 | 126 |
| tilted | 5 % → 5 % | 0.65 | 1.05 | 56 |
| over the wet one | 10 % → 11 % | 0.65 | 1.15 | 60 |
| long, no reload | 18 % → 17 % | 0.47 | 0.96 | 344 | quarters: 0.22 → 0.09 → 0.04 → 0.02

Numbers say: wet paint spreads well beyond the stroke.

## Dense Ink
Ink · 14 px · 24.6 s

![Dense Ink](Dense-Ink.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 5 % → 7 % | 0.72 | 1.26 | 44 |
| heavy line | 7 % → 7 % | 0.73 | 1.09 | 74 |
| pressure swell | 5 % → 6 % | 0.72 | 1.17 | 50 |
| fast wave | 13 % → 13 % | 0.69 | 1.01 | 129 |
| slow wave | 12 % → 12 % | 0.67 | 1.04 | 143 |
| spiral | 18 % → 15 % | 0.65 | 0.80 | 315 |
| loop | 11 % → 12 % | 0.69 | 1.08 | 168 |
| tilted | 5 % → 6 % | 0.72 | 1.07 | 71 |
| over the wet one | 12 % → 13 % | 0.72 | 1.11 | 67 |
| long, no reload | 23 % → 15 % | 0.64 | 0.66 | 333 | quarters: 0.30 → 0.12 → 0.04 → 0.02

## Transparent Wash
Watercolor · 22 px · 25.0 s

![Transparent Wash](Transparent-Wash.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 2 % → 5 % | 0.27 | 2.25 | 33 |
| heavy line | 7 % → 9 % | 0.27 | 1.22 | 61 |
| pressure swell | 4 % → 6 % | 0.28 | 1.54 | 35 |
| fast wave | 14 % → 16 % | 0.20 | 1.17 | 114 |
| slow wave | 12 % → 15 % | 0.21 | 1.28 | 166 |
| spiral | 18 % → 22 % | 0.16 | 1.23 | 194 |
| loop | 11 % → 13 % | 0.22 | 1.20 | 120 |
| tilted | 8 % → 8 % | 0.24 | 1.06 | 57 |
| over the wet one | 13 % → 16 % | 0.24 | 1.18 | 55 |
| long, no reload | 26 % → 32 % | 0.13 | 1.22 | 333 | quarters: 0.11 → 0.04 → 0.02 → 0.01

Numbers say: wet paint spreads well beyond the stroke.

## Dry Brush
Gouache · 24 px · 21.7 s

![Dry Brush](Dry-Brush.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 5 % → 0 % | 0.65 | 0.09 | 42 |
| heavy line | 6 % → 0 % | 0.65 | 0.02 | 130 |
| pressure swell | 5 % → 0 % | 0.65 | 0.08 | 58 |
| fast wave | 6 % → 1 % | 0.65 | 0.08 | 143 |
| slow wave | 7 % → 0 % | 0.65 | 0.06 | 620 |
| spiral | 7 % → 0 % | 0.65 | 0.07 | 455 |
| loop | 10 % → 0 % | 0.65 | 0.04 | 138 |
| tilted | 4 % → 3 % | 0.65 | 0.88 | 74 |
| over the wet one | 9 % → 1 % | 0.65 | 0.12 | 65 |
| long, no reload | 6 % → 1 % | 0.65 | 0.14 | 350 | quarters: 0.12 → 0.00 → 0.00 → 0.00

## Wax Crayon
Wax · 8 px · 11.2 s

![Wax Crayon](Wax-Crayon.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 1 % → 1 % | 0.71 | 1.00 | 18 |
| heavy line | 1 % → 1 % | 0.69 | 1.00 | 24 |
| pressure swell | 1 % → 1 % | 0.70 | 1.00 | 15 |
| fast wave | 3 % → 3 % | 0.69 | 1.00 | 42 |
| slow wave | 3 % → 3 % | 0.70 | 1.00 | 48 |
| spiral | 5 % → 5 % | 0.70 | 1.00 | 88 |
| loop | 3 % → 3 % | 0.70 | 1.00 | 90 |
| tilted | 2 % → 2 % | 0.68 | 1.00 | 45 |
| over the wet one | 3 % → 3 % | 0.68 | 1.00 | 57 |
| long, no reload | 7 % → 7 % | 0.70 | 1.00 | 315 | quarters: 0.06 → 0.06 → 0.06 → 0.06

Numbers say: the long stroke does not run out of paint.

## Oil Pastel
Wax · 12 px · 11.4 s

![Oil Pastel](Oil-Pastel.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 1 % → 1 % | 0.68 | 1.00 | 25 |
| heavy line | 2 % → 2 % | 0.68 | 1.00 | 34 |
| pressure swell | 2 % → 2 % | 0.69 | 1.00 | 18 |
| fast wave | 5 % → 5 % | 0.68 | 1.00 | 64 |
| slow wave | 5 % → 5 % | 0.68 | 1.00 | 73 |
| spiral | 8 % → 8 % | 0.68 | 1.00 | 183 |
| loop | 4 % → 4 % | 0.68 | 1.00 | 151 |
| tilted | 2 % → 2 % | 0.68 | 1.00 | 122 |
| over the wet one | 5 % → 5 % | 0.68 | 1.00 | 46 |
| long, no reload | 13 % → 13 % | 0.68 | 1.00 | 288 | quarters: 0.10 → 0.09 → 0.10 → 0.10

Numbers say: the long stroke does not run out of paint.

## Charcoal
Charcoal · 5 px · 10.1 s

![Charcoal](Charcoal.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 1 % → 1 % | 0.74 | 1.00 | 13 |
| heavy line | 1 % → 1 % | 0.74 | 1.00 | 12 |
| pressure swell | 1 % → 1 % | 0.74 | 1.00 | 9 |
| fast wave | 2 % → 2 % | 0.73 | 1.00 | 34 |
| slow wave | 2 % → 2 % | 0.74 | 1.00 | 28 |
| spiral | 4 % → 4 % | 0.74 | 1.00 | 47 |
| loop | 2 % → 2 % | 0.74 | 1.00 | 24 |
| tilted | 2 % → 2 % | 0.72 | 1.00 | 17 |
| over the wet one | 2 % → 2 % | 0.72 | 1.00 | 11 |
| long, no reload | 6 % → 6 % | 0.73 | 1.00 | 71 | quarters: 0.05 → 0.05 → 0.05 → 0.05

Numbers say: the long stroke does not run out of paint.

## Impasto
Heavy acrylic · 22 px · 15.2 s

![Impasto](Impasto.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 8 % → 8 % | 0.71 | 0.93 | 44 |
| heavy line | 10 % → 9 % | 0.70 | 0.94 | 95 |
| pressure swell | 7 % → 7 % | 0.72 | 0.94 | 52 |
| fast wave | 20 % → 13 % | 0.71 | 0.64 | 159 |
| slow wave | 21 % → 14 % | 0.71 | 0.66 | 251 |
| spiral | 30 % → 14 % | 0.71 | 0.46 | 376 |
| loop | 18 % → 14 % | 0.71 | 0.77 | 267 |
| tilted | 8 % → 8 % | 0.70 | 1.00 | 91 |
| over the wet one | 17 % → 15 % | 0.70 | 0.91 | 67 |
| long, no reload | 34 % → 14 % | 0.71 | 0.41 | 398 | quarters: 0.38 → 0.21 → 0.10 → 0.03

## Oil Round
Oil · 18 px · 17.5 s

![Oil Round](Oil-Round.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 2 % → 2 % | 0.71 | 1.00 | 40 |
| heavy line | 6 % → 6 % | 0.72 | 1.00 | 68 |
| pressure swell | 3 % → 3 % | 0.63 | 1.00 | 40 |
| fast wave | 7 % → 7 % | 0.54 | 1.00 | 134 |
| slow wave | 4 % → 4 % | 0.36 | 1.00 | 162 |
| spiral | 5 % → 5 % | 0.21 | 1.00 | 204 |
| loop | 3 % → 3 % | 0.18 | 1.00 | 118 |
| tilted | 2 % → 2 % | 0.33 | 1.00 | 63 |
| over the wet one | 3 % → 3 % | 0.33 | 1.00 | 54 |
| long, no reload | 8 % → 8 % | 0.17 | 1.00 | 328 | quarters: 0.02 → 0.02 → 0.01 → 0.01

## Palette Knife
Oil · 20 px · 16.8 s

![Palette Knife](Palette-Knife.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 8 % → 8 % | 0.67 | 1.00 | 13 |
| heavy line | 8 % → 8 % | 0.73 | 1.00 | 16 |
| pressure swell | 6 % → 6 % | 0.74 | 1.00 | 6 |
| fast wave | 17 % → 17 % | 0.49 | 1.00 | 24 |
| slow wave | 17 % → 17 % | 0.43 | 1.00 | 36 |
| spiral | 18 % → 18 % | 0.45 | 1.00 | 44 |
| loop | 16 % → 16 % | 0.58 | 1.00 | 22 |
| tilted | 5 % → 5 % | 0.72 | 1.00 | 12 |
| over the wet one | 13 % → 13 % | 0.72 | 1.00 | 10 |
| long, no reload | 17 % → 17 % | 0.47 | 1.00 | 58 | quarters: 0.29 → 0.05 → 0.00 → 0.00

Numbers say: pressure barely changes the width.

## Water
Watercolor · 20 px · 34.5 s · over bands of wet oil paint and oil pastel in turn (it works on paint already there: look at what it does to the bands; covered counts the bands too)

![Water](Water.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 25 % → 26 % | 0.78 | 1.07 | 25 |
| heavy line | 23 % → 24 % | 0.80 | 1.04 | 59 |
| pressure swell | 23 % → 24 % | 0.80 | 1.03 | 35 |
| fast wave | 23 % → 25 % | 0.80 | 1.07 | 108 |
| slow wave | 23 % → 25 % | 0.80 | 1.06 | 142 |
| spiral | 23 % → 25 % | 0.79 | 1.08 | 188 |
| loop | 23 % → 24 % | 0.80 | 1.03 | 87 |
| tilted | 23 % → 23 % | 0.80 | 1.00 | 61 |
| over the wet one | 23 % → 25 % | 0.80 | 1.07 | 46 |
| long, no reload | 23 % → 25 % | 0.80 | 1.08 | 338 | quarters: 0.21 → 0.26 → 0.17 → 0.25

Numbers say: pressure barely changes the width; the long stroke does not run out of paint.

## Blender
Pastel · 16 px · 20.1 s · over bands of wet oil paint and oil pastel in turn (it works on paint already there: look at what it does to the bands; covered counts the bands too)

![Blender](Blender.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 24 % → 24 % | 0.80 | 1.00 | 25 |
| heavy line | 24 % → 24 % | 0.80 | 1.00 | 35 |
| pressure swell | 24 % → 24 % | 0.80 | 1.00 | 23 |
| fast wave | 25 % → 25 % | 0.78 | 1.00 | 76 |
| slow wave | 25 % → 25 % | 0.78 | 1.00 | 83 |
| spiral | 27 % → 27 % | 0.76 | 1.00 | 126 |
| loop | 25 % → 25 % | 0.79 | 1.00 | 65 |
| tilted | 24 % → 24 % | 0.78 | 1.00 | 41 |
| over the wet one | 25 % → 25 % | 0.78 | 1.00 | 32 |
| long, no reload | 29 % → 29 % | 0.74 | 1.00 | 181 | quarters: 0.19 → 0.26 → 0.21 → 0.28

Numbers say: pressure barely changes the width; the long stroke does not run out of paint.

## Eraser
Eraser · 16 px · 20.1 s · over bands of wet oil paint and oil pastel in turn (it works on paint already there: look at what it does to the bands; covered counts the bands too)

![Eraser](Eraser.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 23 % → 23 % | 0.81 | 1.00 | 24 |
| heavy line | 23 % → 23 % | 0.81 | 1.00 | 33 |
| pressure swell | 23 % → 23 % | 0.81 | 1.00 | 22 |
| fast wave | 22 % → 22 % | 0.81 | 1.00 | 72 |
| slow wave | 22 % → 22 % | 0.81 | 1.00 | 91 |
| spiral | 21 % → 21 % | 0.81 | 1.00 | 118 |
| loop | 22 % → 22 % | 0.81 | 1.00 | 64 |
| tilted | 23 % → 23 % | 0.81 | 1.00 | 43 |
| over the wet one | 22 % → 22 % | 0.81 | 1.00 | 30 |
| long, no reload | 19 % → 19 % | 0.81 | 1.00 | 180 | quarters: 0.15 → 0.19 → 0.14 → 0.20

Numbers say: pressure barely changes the width; the long stroke does not run out of paint.

## Fan
Gouache · 30 px · 30.3 s

![Fan](Fan.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 9 % → 3 % | 0.63 | 0.37 | 33 |
| heavy line | 11 % → 4 % | 0.63 | 0.39 | 51 |
| pressure swell | 8 % → 5 % | 0.63 | 0.55 | 43 |
| fast wave | 18 % → 5 % | 0.63 | 0.26 | 198 |
| slow wave | 18 % → 5 % | 0.63 | 0.25 | 301 |
| spiral | 24 % → 5 % | 0.63 | 0.20 | 169 |
| loop | 17 % → 5 % | 0.63 | 0.29 | 102 |
| tilted | 5 % → 6 % | 0.63 | 1.05 | 37 |
| over the wet one | 16 % → 8 % | 0.63 | 0.50 | 44 |
| long, no reload | 23 % → 5 % | 0.63 | 0.22 | 254 | quarters: 0.29 → 0.07 → 0.01 → 0.00

## Sponge
Gouache · 30 px · 30.1 s

![Sponge](Sponge.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 4 % → 0 % | 0.62 | 0.12 | 33 |
| heavy line | 12 % → 2 % | 0.62 | 0.14 | 63 |
| pressure swell | 7 % → 2 % | 0.62 | 0.27 | 60 |
| fast wave | 20 % → 4 % | 0.62 | 0.19 | 196 |
| slow wave | 21 % → 4 % | 0.62 | 0.18 | 387 |
| spiral | 28 % → 4 % | 0.62 | 0.14 | 191 |
| loop | 18 % → 5 % | 0.62 | 0.29 | 104 |
| tilted | 7 % → 7 % | 0.62 | 1.04 | 138 |
| over the wet one | 16 % → 6 % | 0.62 | 0.37 | 49 |
| long, no reload | 29 % → 5 % | 0.62 | 0.17 | 293 | quarters: 0.29 → 0.13 → 0.07 → 0.04

## Ink — sumi brush
Watercolor · 22 px · 29.0 s

![Ink — sumi brush](Ink-sumi-brush.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 6 % → 7 % | 0.46 | 1.06 | 67 |
| heavy line | 10 % → 11 % | 0.38 | 1.05 | 110 |
| pressure swell | 7 % → 8 % | 0.42 | 1.04 | 59 |
| fast wave | 21 % → 21 % | 0.32 | 1.00 | 140 |
| slow wave | 19 % → 19 % | 0.37 | 1.01 | 226 |
| spiral | 28 % → 26 % | 0.30 | 0.92 | 251 |
| loop | 17 % → 18 % | 0.37 | 1.06 | 125 |
| tilted | 6 % → 7 % | 0.40 | 1.17 | 66 |
| over the wet one | 16 % → 16 % | 0.40 | 1.01 | 59 |
| long, no reload | 33 % → 29 % | 0.30 | 0.86 | 391 | quarters: 0.23 → 0.11 → 0.06 → 0.04

## Ink — wash
Watercolor · 40 px · 29.5 s

![Ink — wash](Ink-wash.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 8 % → 9 % | 0.05 | 1.26 | 65 |
| heavy line | 11 % → 13 % | 0.04 | 1.22 | 77 |
| pressure swell | 7 % → 9 % | 0.05 | 1.25 | 56 |
| fast wave | 22 % → 27 % | 0.04 | 1.21 | 193 |
| slow wave | 21 % → 26 % | 0.06 | 1.23 | 304 |
| spiral | 34 % → 41 % | 0.04 | 1.21 | 299 |
| loop | 19 % → 24 % | 0.05 | 1.25 | 158 |
| tilted | 7 % → 9 % | 0.05 | 1.21 | 98 |
| over the wet one | 18 % → 21 % | 0.05 | 1.18 | 73 |
| long, no reload | 39 % → 46 % | 0.05 | 1.19 | 483 | quarters: 0.04 → 0.03 → 0.02 → 0.01

## Ink — dry brush
Ink · 30 px · 22.2 s

![Ink — dry brush](Ink-dry-brush.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 9 % → 7 % | 0.81 | 0.78 | 77 |
| heavy line | 11 % → 8 % | 0.80 | 0.73 | 110 |
| pressure swell | 8 % → 7 % | 0.81 | 0.85 | 77 |
| fast wave | 22 % → 8 % | 0.78 | 0.38 | 211 |
| slow wave | 18 % → 6 % | 0.80 | 0.36 | 360 |
| spiral | 23 % → 8 % | 0.77 | 0.35 | 327 |
| loop | 20 % → 8 % | 0.77 | 0.41 | 175 |
| tilted | 9 % → 9 % | 0.78 | 1.01 | 109 |
| over the wet one | 19 % → 14 % | 0.78 | 0.75 | 83 |
| long, no reload | 20 % → 9 % | 0.78 | 0.42 | 515 | quarters: 0.32 → 0.01 → 0.00 → 0.00

## Ink — nib
Watercolor · 5 px · 20.1 s

![Ink — nib](Ink-nib.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 2 % → 2 % | 0.76 | 1.17 | 25 |
| heavy line | 2 % → 2 % | 0.77 | 1.16 | 24 |
| pressure swell | 1 % → 2 % | 0.78 | 1.22 | 19 |
| fast wave | 4 % → 4 % | 0.66 | 1.09 | 65 |
| slow wave | 4 % → 4 % | 0.68 | 1.11 | 60 |
| spiral | 6 % → 6 % | 0.58 | 1.08 | 125 |
| loop | 3 % → 4 % | 0.69 | 1.12 | 57 |
| tilted | 2 % → 2 % | 0.64 | 1.21 | 27 |
| over the wet one | 4 % → 4 % | 0.64 | 1.03 | 25 |
| long, no reload | 7 % → 7 % | 0.53 | 1.02 | 161 | quarters: 0.09 → 0.04 → 0.03 → 0.02

## 0.45 · Dry brush
Gouache · 34 px · 22.8 s

![0.45 · Dry brush](0-45-Dry-brush.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 11 % → 3 % | 0.67 | 0.28 | 144 |
| heavy line | 12 % → 3 % | 0.67 | 0.30 | 108 |
| pressure swell | 9 % → 4 % | 0.67 | 0.40 | 77 |
| fast wave | 20 % → 4 % | 0.67 | 0.19 | 263 |
| slow wave | 20 % → 4 % | 0.67 | 0.18 | 445 |
| spiral | 21 % → 4 % | 0.67 | 0.17 | 431 |
| loop | 21 % → 4 % | 0.67 | 0.19 | 232 |
| tilted | 9 % → 9 % | 0.67 | 0.97 | 124 |
| over the wet one | 20 % → 7 % | 0.67 | 0.33 | 110 |
| long, no reload | 20 % → 4 % | 0.67 | 0.21 | 637 | quarters: 0.38 → 0.07 → 0.00 → 0.00

Numbers say: pressure barely changes the width.

## Dry pastel
Pastel · 26 px · 9.6 s

![Dry pastel](Dry-pastel.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 5 % → 5 % | 0.36 | 1.00 | 39 |
| heavy line | 6 % → 6 % | 0.36 | 1.00 | 30 |
| pressure swell | 5 % → 5 % | 0.36 | 1.00 | 21 |
| fast wave | 15 % → 15 % | 0.36 | 1.00 | 75 |
| slow wave | 14 % → 14 % | 0.36 | 1.00 | 131 |
| spiral | 23 % → 23 % | 0.36 | 1.00 | 128 |
| loop | 11 % → 11 % | 0.36 | 1.00 | 66 |
| tilted | 5 % → 5 % | 0.37 | 1.00 | 35 |
| over the wet one | 10 % → 10 % | 0.37 | 1.00 | 33 |
| long, no reload | 26 % → 26 % | 0.36 | 1.00 | 178 | quarters: 0.11 → 0.10 → 0.10 → 0.11

Numbers say: the long stroke does not run out of paint.

## 0.45 · Charcoal
Charcoal · 18 px · 9.7 s

![0.45 · Charcoal](0-45-Charcoal.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 4 % → 4 % | 0.79 | 1.00 | 16 |
| heavy line | 4 % → 4 % | 0.79 | 1.00 | 15 |
| pressure swell | 4 % → 4 % | 0.79 | 1.00 | 11 |
| fast wave | 11 % → 11 % | 0.79 | 1.00 | 38 |
| slow wave | 11 % → 11 % | 0.78 | 1.00 | 53 |
| spiral | 20 % → 20 % | 0.79 | 1.00 | 69 |
| loop | 10 % → 10 % | 0.79 | 1.00 | 34 |
| tilted | 4 % → 4 % | 0.78 | 1.00 | 21 |
| over the wet one | 9 % → 9 % | 0.78 | 1.00 | 15 |
| long, no reload | 26 % → 26 % | 0.79 | 1.00 | 101 | quarters: 0.23 → 0.22 → 0.23 → 0.24

Numbers say: pressure barely changes the width; the long stroke does not run out of paint.

## Watercolour — wash
Watercolor · 50 px · 33.4 s

![Watercolour — wash](Watercolour-wash.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 9 % → 11 % | 0.01 | 1.22 | 81 |
| heavy line | 12 % → 14 % | 0.01 | 1.17 | 146 |
| pressure swell | 8 % → 10 % | 0.01 | 1.22 | 92 |
| fast wave | 26 % → 30 % | 0.01 | 1.18 | 227 |
| slow wave | 25 % → 29 % | 0.01 | 1.18 | 401 |
| spiral | 39 % → 46 % | 0.01 | 1.17 | 383 |
| loop | 22 % → 27 % | 0.01 | 1.21 | 198 |
| tilted | 10 % → 11 % | 0.01 | 1.18 | 145 |
| over the wet one | 22 % → 25 % | 0.01 | 1.14 | 89 |
| long, no reload | 45 % → 54 % | 0.01 | 1.18 | 567 | quarters: 0.01 → 0.01 → 0.01 → 0.00

## Watercolour — wet-in-wet
Watercolor · 44 px · 31.1 s

![Watercolour — wet-in-wet](Watercolour-wet-in-wet.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 7 % → 9 % | 0.02 | 1.26 | 65 |
| heavy line | 10 % → 12 % | 0.02 | 1.22 | 81 |
| pressure swell | 7 % → 9 % | 0.02 | 1.21 | 54 |
| fast wave | 23 % → 27 % | 0.02 | 1.17 | 207 |
| slow wave | 22 % → 26 % | 0.02 | 1.18 | 380 |
| spiral | 36 % → 43 % | 0.02 | 1.20 | 311 |
| loop | 19 % → 23 % | 0.02 | 1.20 | 203 |
| tilted | 7 % → 9 % | 0.02 | 1.19 | 128 |
| over the wet one | 17 % → 19 % | 0.02 | 1.12 | 78 |
| long, no reload | 42 % → 49 % | 0.02 | 1.18 | 488 | quarters: 0.01 → 0.01 → 0.01 → 0.01

## Watercolour — glaze
Watercolor · 38 px · 30.3 s

![Watercolour — glaze](Watercolour-glaze.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 7 % → 9 % | 0.01 | 1.28 | 97 |
| heavy line | 10 % → 13 % | 0.01 | 1.25 | 92 |
| pressure swell | 7 % → 9 % | 0.01 | 1.29 | 52 |
| fast wave | 20 % → 25 % | 0.01 | 1.24 | 182 |
| slow wave | 19 % → 24 % | 0.01 | 1.26 | 292 |
| spiral | 31 % → 37 % | 0.01 | 1.21 | 317 |
| loop | 18 % → 23 % | 0.01 | 1.27 | 153 |
| tilted | 7 % → 8 % | 0.01 | 1.20 | 98 |
| over the wet one | 17 % → 20 % | 0.01 | 1.19 | 70 |
| long, no reload | 36 % → 42 % | 0.01 | 1.17 | 498 | quarters: 0.01 → 0.00 → 0.00 → 0.00

## Watercolour — granulating
Watercolor · 44 px · 30.0 s

![Watercolour — granulating](Watercolour-granulating.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 8 % → 10 % | 0.02 | 1.18 | 72 |
| heavy line | 12 % → 14 % | 0.01 | 1.15 | 86 |
| pressure swell | 8 % → 10 % | 0.02 | 1.18 | 66 |
| fast wave | 25 % → 29 % | 0.01 | 1.15 | 202 |
| slow wave | 24 % → 27 % | 0.02 | 1.16 | 426 |
| spiral | 39 % → 44 % | 0.01 | 1.15 | 331 |
| loop | 22 % → 25 % | 0.01 | 1.17 | 172 |
| tilted | 9 % → 11 % | 0.02 | 1.15 | 109 |
| over the wet one | 21 % → 23 % | 0.02 | 1.11 | 82 |
| long, no reload | 45 % → 52 % | 0.01 | 1.15 | 496 | quarters: 0.01 → 0.01 → 0.01 → 0.01

## Watercolour — dry brush
Watercolor · 36 px · 25.1 s

![Watercolour — dry brush](Watercolour-dry-brush.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 7 % → 8 % | 0.05 | 1.07 | 84 |
| heavy line | 11 % → 12 % | 0.04 | 1.03 | 98 |
| pressure swell | 9 % → 10 % | 0.05 | 1.07 | 68 |
| fast wave | 21 % → 14 % | 0.04 | 0.68 | 250 |
| slow wave | 19 % → 13 % | 0.04 | 0.70 | 386 |
| spiral | 24 % → 15 % | 0.04 | 0.61 | 392 |
| loop | 17 % → 14 % | 0.04 | 0.85 | 222 |
| tilted | 7 % → 8 % | 0.05 | 1.19 | 110 |
| over the wet one | 17 % → 17 % | 0.05 | 0.99 | 96 |
| long, no reload | 22 % → 15 % | 0.04 | 0.68 | 566 | quarters: 0.02 → 0.00 → 0.00 → 0.00

## Gouache
Gouache · 30 px · 24.8 s

![Gouache](Gouache.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 8 % → 6 % | 0.14 | 0.67 | 69 |
| heavy line | 13 % → 6 % | 0.14 | 0.47 | 82 |
| pressure swell | 10 % → 6 % | 0.14 | 0.61 | 59 |
| fast wave | 27 % → 7 % | 0.14 | 0.27 | 192 |
| slow wave | 27 % → 7 % | 0.14 | 0.27 | 318 |
| spiral | 37 % → 8 % | 0.14 | 0.22 | 420 |
| loop | 22 % → 8 % | 0.14 | 0.36 | 242 |
| tilted | 9 % → 9 % | 0.14 | 1.02 | 89 |
| over the wet one | 20 % → 13 % | 0.14 | 0.67 | 73 |
| long, no reload | 38 % → 10 % | 0.14 | 0.25 | 440 | quarters: 0.07 → 0.04 → 0.01 → 0.01

## Oil — alla prima
Oil · 30 px · 18.2 s

![Oil — alla prima](Oil-alla-prima.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 9 % → 9 % | 0.50 | 1.00 | 79 |
| heavy line | 10 % → 10 % | 0.50 | 1.00 | 79 |
| pressure swell | 8 % → 8 % | 0.52 | 1.00 | 68 |
| fast wave | 24 % → 24 % | 0.49 | 1.00 | 198 |
| slow wave | 25 % → 25 % | 0.50 | 1.00 | 339 |
| spiral | 38 % → 38 % | 0.44 | 1.00 | 360 |
| loop | 21 % → 21 % | 0.50 | 1.00 | 187 |
| tilted | 11 % → 11 % | 0.50 | 1.00 | 122 |
| over the wet one | 20 % → 20 % | 0.50 | 1.00 | 94 |
| long, no reload | 46 % → 46 % | 0.40 | 1.00 | 501 | quarters: 0.31 → 0.24 → 0.17 → 0.10

Numbers say: pressure barely changes the width.

## Oil — impasto
Oil · 34 px · 18.8 s

![Oil — impasto](Oil-impasto.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 11 % → 11 % | 0.24 | 1.00 | 87 |
| heavy line | 12 % → 12 % | 0.23 | 1.00 | 96 |
| pressure swell | 9 % → 9 % | 0.25 | 1.00 | 66 |
| fast wave | 29 % → 29 % | 0.21 | 1.00 | 241 |
| slow wave | 29 % → 29 % | 0.21 | 1.00 | 410 |
| spiral | 48 % → 48 % | 0.17 | 1.00 | 419 |
| loop | 25 % → 25 % | 0.21 | 1.00 | 278 |
| tilted | 12 % → 12 % | 0.24 | 1.00 | 118 |
| over the wet one | 23 % → 23 % | 0.24 | 1.00 | 97 |
| long, no reload | 55 % → 55 % | 0.15 | 1.00 | 588 | quarters: 0.16 → 0.11 → 0.06 → 0.02

Numbers say: pressure barely changes the width.

## Oil — glaze
Oil · 40 px · 15.9 s

![Oil — glaze](Oil-glaze.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 10 % → 10 % | 0.49 | 1.00 | 82 |
| heavy line | 14 % → 14 % | 0.48 | 1.00 | 102 |
| pressure swell | 10 % → 10 % | 0.49 | 1.00 | 69 |
| fast wave | 28 % → 28 % | 0.46 | 1.00 | 234 |
| slow wave | 30 % → 30 % | 0.46 | 1.00 | 436 |
| spiral | 42 % → 42 % | 0.44 | 1.00 | 404 |
| loop | 24 % → 24 % | 0.47 | 1.00 | 241 |
| tilted | 11 % → 11 % | 0.47 | 1.00 | 119 |
| over the wet one | 23 % → 23 % | 0.47 | 1.00 | 239 |
| long, no reload | 47 % → 47 % | 0.43 | 1.00 | 619 | quarters: 0.33 → 0.24 → 0.18 → 0.14

## Oil — scumble
Oil · 36 px · 21.0 s

![Oil — scumble](Oil-scumble.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 11 % → 11 % | 0.06 | 1.00 | 106 |
| heavy line | 12 % → 12 % | 0.05 | 1.00 | 121 |
| pressure swell | 9 % → 9 % | 0.06 | 1.00 | 85 |
| fast wave | 18 % → 18 % | 0.04 | 1.00 | 289 |
| slow wave | 20 % → 20 % | 0.04 | 1.00 | 688 |
| spiral | 19 % → 19 % | 0.03 | 1.00 | 550 |
| loop | 22 % → 22 % | 0.04 | 1.00 | 249 |
| tilted | 10 % → 10 % | 0.05 | 1.00 | 136 |
| over the wet one | 21 % → 21 % | 0.05 | 1.00 | 114 |
| long, no reload | 18 % → 18 % | 0.04 | 1.00 | 724 | quarters: 0.03 → 0.00 → 0.00 → 0.00

Numbers say: pressure barely changes the width.

## Acrylic — heavy body
Heavy acrylic · 30 px · 16.0 s

![Acrylic — heavy body](Acrylic-heavy-body.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 10 % → 9 % | 0.51 | 0.93 | 78 |
| heavy line | 11 % → 10 % | 0.51 | 0.93 | 79 |
| pressure swell | 8 % → 8 % | 0.52 | 0.94 | 59 |
| fast wave | 24 % → 14 % | 0.51 | 0.58 | 258 |
| slow wave | 25 % → 15 % | 0.51 | 0.59 | 469 |
| spiral | 37 % → 15 % | 0.51 | 0.40 | 344 |
| loop | 22 % → 16 % | 0.51 | 0.73 | 175 |
| tilted | 10 % → 10 % | 0.51 | 1.00 | 95 |
| over the wet one | 20 % → 17 % | 0.51 | 0.88 | 84 |
| long, no reload | 39 % → 15 % | 0.51 | 0.40 | 492 | quarters: 0.30 → 0.20 → 0.10 → 0.02

Numbers say: pressure barely changes the width.

## Acrylic — fluid
Watercolor · 36 px · 29.8 s

![Acrylic — fluid](Acrylic-fluid.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 9 % → 10 % | 0.06 | 1.11 | 86 |
| heavy line | 13 % → 14 % | 0.05 | 1.07 | 102 |
| pressure swell | 9 % → 10 % | 0.07 | 1.09 | 54 |
| fast wave | 26 % → 28 % | 0.05 | 1.07 | 170 |
| slow wave | 24 % → 26 % | 0.07 | 1.08 | 294 |
| spiral | 39 % → 41 % | 0.05 | 1.06 | 291 |
| loop | 22 % → 25 % | 0.06 | 1.11 | 152 |
| tilted | 8 % → 9 % | 0.07 | 1.17 | 110 |
| over the wet one | 21 % → 22 % | 0.07 | 1.05 | 90 |
| long, no reload | 44 % → 47 % | 0.05 | 1.06 | 503 | quarters: 0.05 → 0.03 → 0.02 → 0.01

## Acrylic — palette knife
Heavy acrylic · 42 px · 18.7 s

![Acrylic — palette knife](Acrylic-palette-knife.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 15 % → 15 % | 0.06 | 0.98 | 31 |
| heavy line | 15 % → 15 % | 0.05 | 0.98 | 21 |
| pressure swell | 12 % → 12 % | 0.06 | 0.99 | 9 |
| fast wave | 37 % → 20 % | 0.06 | 0.54 | 47 |
| slow wave | 37 % → 21 % | 0.06 | 0.56 | 81 |
| spiral | 48 % → 19 % | 0.06 | 0.38 | 105 |
| loop | 32 % → 24 % | 0.05 | 0.75 | 52 |
| tilted | 12 % → 12 % | 0.05 | 1.00 | 18 |
| over the wet one | 26 % → 26 % | 0.05 | 0.98 | 21 |
| long, no reload | 55 % → 20 % | 0.06 | 0.36 | 110 | quarters: 0.04 → 0.02 → 0.00 → 0.00

Numbers say: pressure barely changes the width.

## Finger on oil
Oil · 30 px · 13.6 s

![Finger on oil](Finger-on-oil.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 8 % → 8 % | 0.34 | 1.00 | 41 |
| heavy line | 12 % → 12 % | 0.30 | 1.00 | 56 |
| pressure swell | 8 % → 8 % | 0.35 | 1.00 | 35 |
| fast wave | 16 % → 16 % | 0.22 | 1.00 | 124 |
| slow wave | 17 % → 17 % | 0.23 | 1.00 | 202 |
| spiral | 18 % → 18 % | 0.22 | 1.00 | 199 |
| loop | 18 % → 18 % | 0.23 | 1.00 | 100 |
| tilted | 9 % → 9 % | 0.31 | 1.00 | 69 |
| over the wet one | 18 % → 18 % | 0.31 | 1.00 | 45 |
| long, no reload | 15 % → 15 % | 0.23 | 1.00 | 314 | quarters: 0.13 → 0.01 → 0.00 → 0.00

## Palette knife — oil
Oil · 44 px · 19.6 s

![Palette knife — oil](Palette-knife-oil.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 16 % → 16 % | 0.10 | 1.00 | 21 |
| heavy line | 16 % → 16 % | 0.09 | 1.00 | 24 |
| pressure swell | 12 % → 12 % | 0.10 | 1.00 | 9 |
| fast wave | 39 % → 39 % | 0.07 | 1.00 | 51 |
| slow wave | 39 % → 39 % | 0.07 | 1.00 | 84 |
| spiral | 54 % → 54 % | 0.05 | 1.00 | 93 |
| loop | 34 % → 34 % | 0.08 | 1.00 | 47 |
| tilted | 13 % → 13 % | 0.09 | 1.00 | 20 |
| over the wet one | 28 % → 28 % | 0.09 | 1.00 | 21 |
| long, no reload | 65 % → 65 % | 0.05 | 1.00 | 143 | quarters: 0.08 → 0.04 → 0.01 → 0.00

Numbers say: pressure barely changes the width.

## 0.45 · Sponge
Watercolor · 46 px · 24.2 s

![0.45 · Sponge](0-45-Sponge.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 11 % → 0 % | 0.00 | 0.00 | 44 |
| heavy line | 13 % → 0 % | 0.01 | 0.00 | 65 |
| pressure swell | 9 % → 1 % | 0.02 | 0.14 | 41 |
| fast wave | 23 % → 2 % | 0.01 | 0.08 | 201 |
| slow wave | 26 % → 8 % | 0.02 | 0.30 | 480 |
| spiral | 34 % → 11 % | 0.02 | 0.32 | 325 |
| loop | 22 % → 4 % | 0.02 | 0.19 | 142 |
| tilted | 9 % → 10 % | 0.04 | 1.19 | 109 |
| over the wet one | 22 % → 10 % | 0.04 | 0.44 | 91 |
| long, no reload | 41 % → 19 % | 0.02 | 0.47 | 416 | quarters: 0.01 → 0.01 → 0.01 → 0.01

## 0.45 · Eraser
Eraser · 30 px · 20.8 s · over bands of wet oil paint and oil pastel in turn (it works on paint already there: look at what it does to the bands; covered counts the bands too)

![0.45 · Eraser](0-45-Eraser.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 23 % → 23 % | 0.81 | 1.00 | 58 |
| heavy line | 22 % → 22 % | 0.81 | 1.00 | 50 |
| pressure swell | 22 % → 22 % | 0.81 | 1.00 | 34 |
| fast wave | 21 % → 21 % | 0.80 | 1.00 | 123 |
| slow wave | 20 % → 20 % | 0.81 | 1.00 | 241 |
| spiral | 20 % → 20 % | 0.79 | 1.00 | 252 |
| loop | 21 % → 21 % | 0.79 | 1.00 | 124 |
| tilted | 22 % → 22 % | 0.80 | 1.00 | 54 |
| over the wet one | 21 % → 21 % | 0.80 | 1.00 | 53 |
| long, no reload | 16 % → 16 % | 0.79 | 1.00 | 296 | quarters: 0.13 → 0.15 → 0.12 → 0.16

Numbers say: pressure barely changes the width; the long stroke does not run out of paint.

## Lift wet paint
Eraser · 30 px · 19.2 s · over bands of wet oil paint and oil pastel in turn (it works on paint already there: look at what it does to the bands; covered counts the bands too)

![Lift wet paint](Lift-wet-paint.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 23 % → 23 % | 0.81 | 1.00 | 40 |
| heavy line | 23 % → 23 % | 0.81 | 1.00 | 51 |
| pressure swell | 23 % → 23 % | 0.81 | 1.00 | 27 |
| fast wave | 23 % → 23 % | 0.81 | 1.00 | 93 |
| slow wave | 23 % → 23 % | 0.81 | 1.00 | 158 |
| spiral | 23 % → 23 % | 0.81 | 1.00 | 150 |
| loop | 23 % → 23 % | 0.81 | 1.00 | 86 |
| tilted | 23 % → 23 % | 0.81 | 1.00 | 46 |
| over the wet one | 23 % → 23 % | 0.81 | 1.00 | 38 |
| long, no reload | 23 % → 23 % | 0.81 | 1.00 | 229 | quarters: 0.18 → 0.23 → 0.16 → 0.23

Numbers say: pressure barely changes the width; the long stroke does not run out of paint.

## Sgraffito
Eraser · 10 px · 18.9 s · over bands of wet oil paint and oil pastel in turn (it works on paint already there: look at what it does to the bands; covered counts the bands too)

![Sgraffito](Sgraffito.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 23 % → 23 % | 0.80 | 1.00 | 7 |
| heavy line | 23 % → 23 % | 0.81 | 1.00 | 10 |
| pressure swell | 23 % → 23 % | 0.81 | 1.00 | 5 |
| fast wave | 23 % → 23 % | 0.81 | 1.00 | 18 |
| slow wave | 23 % → 23 % | 0.81 | 1.00 | 29 |
| spiral | 23 % → 23 % | 0.81 | 1.00 | 45 |
| loop | 23 % → 23 % | 0.81 | 1.00 | 16 |
| tilted | 23 % → 23 % | 0.81 | 1.00 | 7 |
| over the wet one | 23 % → 23 % | 0.81 | 1.00 | 7 |
| long, no reload | 23 % → 23 % | 0.81 | 1.00 | 47 | quarters: 0.17 → 0.23 → 0.16 → 0.23

Numbers say: pressure barely changes the width; the long stroke does not run out of paint.

## Brush Artist · Ink brush · caricature 2
Ink · 16 px · 24.8 s

![Brush Artist · Ink brush · caricature 2](Brush-Artist-Ink-brush-caricature-2.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 3 % → 5 % | 0.78 | 1.81 | 36 |
| heavy line | 13 % → 13 % | 0.88 | 0.99 | 75 |
| pressure swell | 8 % → 8 % | 0.87 | 1.05 | 45 |
| fast wave | 24 % → 23 % | 0.87 | 0.96 | 204 |
| slow wave | 20 % → 19 % | 0.87 | 0.97 | 232 |
| spiral | 30 % → 27 % | 0.86 | 0.89 | 241 |
| loop | 18 % → 18 % | 0.88 | 1.00 | 124 |
| tilted | 7 % → 7 % | 0.88 | 1.01 | 63 |
| over the wet one | 17 % → 17 % | 0.88 | 1.00 | 58 |
| long, no reload | 42 % → 30 % | 0.85 | 0.71 | 365 | quarters: 0.49 → 0.40 → 0.30 → 0.20

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Ink dry G (opaque) · Krovostok
Gouache · 30 px · 19.7 s

![Brush Artist · Ink dry G (opaque) · Krovostok](Brush-Artist-Ink-dry-G-opaque-Krovostok.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 7 % → 0 % | 0.73 | 0.01 | 57 |
| heavy line | 9 % → 0 % | 0.00 | 0.00 | 124 |
| pressure swell | 6 % → 0 % | 0.73 | 0.03 | 70 |
| fast wave | 16 % → 0 % | 0.73 | 0.02 | 293 |
| slow wave | 17 % → 0 % | 0.73 | 0.01 | 402 |
| spiral | 20 % → 0 % | 0.73 | 0.02 | 365 |
| loop | 16 % → 0 % | 0.73 | 0.01 | 202 |
| tilted | 8 % → 7 % | 0.73 | 0.89 | 106 |
| over the wet one | 15 % → 1 % | 0.73 | 0.07 | 97 |
| long, no reload | 17 % → 1 % | 0.73 | 0.04 | 525 | quarters: 0.36 → 0.18 → 0.03 → 0.00

## Brush Artist · Ink dry G2 (opaque)
Gouache · 30 px · 22.7 s

![Brush Artist · Ink dry G2 (opaque)](Brush-Artist-Ink-dry-G2-opaque.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 8 % → 1 % | 0.71 | 0.13 | 57 |
| heavy line | 10 % → 1 % | 0.71 | 0.11 | 120 |
| pressure swell | 7 % → 2 % | 0.71 | 0.23 | 77 |
| fast wave | 21 % → 2 % | 0.71 | 0.10 | 237 |
| slow wave | 21 % → 2 % | 0.71 | 0.09 | 373 |
| spiral | 31 % → 2 % | 0.71 | 0.07 | 391 |
| loop | 18 % → 2 % | 0.71 | 0.13 | 227 |
| tilted | 9 % → 8 % | 0.71 | 0.96 | 123 |
| over the wet one | 17 % → 4 % | 0.71 | 0.25 | 96 |
| long, no reload | 30 % → 3 % | 0.71 | 0.09 | 556 | quarters: 0.38 → 0.31 → 0.21 → 0.08

## Brush Artist · Watercolour wash V6 · Shrigley
Watercolor · 40 px · 28.9 s

![Brush Artist · Watercolour wash V6 · Shrigley](Brush-Artist-Watercolour-wash-V6-Shrigley.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 6 % → 10 % | 0.43 | 1.78 | 37 |
| heavy line | 11 % → 13 % | 0.43 | 1.17 | 106 |
| pressure swell | 7 % → 9 % | 0.45 | 1.37 | 97 |
| fast wave | 24 % → 26 % | 0.41 | 1.09 | 246 |
| slow wave | 22 % → 28 % | 0.44 | 1.25 | 392 |
| spiral | 38 % → 42 % | 0.38 | 1.11 | 256 |
| loop | 19 % → 23 % | 0.44 | 1.17 | 113 |
| tilted | 12 % → 12 % | 0.44 | 1.01 | 92 |
| over the wet one | 21 % → 25 % | 0.44 | 1.17 | 53 |
| long, no reload | 51 % → 55 % | 0.37 | 1.06 | 340 | quarters: 0.32 → 0.24 → 0.19 → 0.15

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Watercolour wash V6 purple
Watercolor · 40 px · 26.4 s

![Brush Artist · Watercolour wash V6 purple](Brush-Artist-Watercolour-wash-V6-purple.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 6 % → 10 % | 0.42 | 1.78 | 32 |
| heavy line | 11 % → 13 % | 0.42 | 1.17 | 68 |
| pressure swell | 7 % → 9 % | 0.43 | 1.37 | 41 |
| fast wave | 24 % → 26 % | 0.41 | 1.09 | 134 |
| slow wave | 22 % → 28 % | 0.43 | 1.25 | 227 |
| spiral | 38 % → 42 % | 0.38 | 1.11 | 218 |
| loop | 19 % → 23 % | 0.43 | 1.17 | 116 |
| tilted | 12 % → 12 % | 0.43 | 1.01 | 108 |
| over the wet one | 21 % → 25 % | 0.43 | 1.17 | 70 |
| long, no reload | 51 % → 55 % | 0.37 | 1.06 | 367 | quarters: 0.30 → 0.24 → 0.19 → 0.16

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Watercolour wash V6 teal
Watercolor · 40 px · 26.2 s

![Brush Artist · Watercolour wash V6 teal](Brush-Artist-Watercolour-wash-V6-teal.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 6 % → 10 % | 0.30 | 1.78 | 30 |
| heavy line | 11 % → 13 % | 0.31 | 1.17 | 63 |
| pressure swell | 7 % → 9 % | 0.31 | 1.37 | 36 |
| fast wave | 24 % → 26 % | 0.30 | 1.09 | 154 |
| slow wave | 22 % → 28 % | 0.31 | 1.25 | 214 |
| spiral | 38 % → 42 % | 0.28 | 1.11 | 205 |
| loop | 19 % → 23 % | 0.31 | 1.17 | 108 |
| tilted | 12 % → 12 % | 0.31 | 1.01 | 87 |
| over the wet one | 21 % → 25 % | 0.31 | 1.17 | 52 |
| long, no reload | 51 % → 55 % | 0.27 | 1.06 | 320 | quarters: 0.22 → 0.18 → 0.14 → 0.11

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Charcoal C6 · Guston hand
Charcoal · 30 px · 10.0 s

![Brush Artist · Charcoal C6 · Guston hand](Brush-Artist-Charcoal-C6-Guston-hand.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 7 % → 7 % | 0.84 | 1.00 | 20 |
| heavy line | 7 % → 7 % | 0.84 | 1.00 | 28 |
| pressure swell | 5 % → 5 % | 0.84 | 1.00 | 19 |
| fast wave | 17 % → 17 % | 0.84 | 1.00 | 67 |
| slow wave | 17 % → 17 % | 0.84 | 1.00 | 90 |
| spiral | 29 % → 29 % | 0.84 | 1.00 | 93 |
| loop | 14 % → 14 % | 0.84 | 1.00 | 46 |
| tilted | 6 % → 6 % | 0.84 | 1.00 | 29 |
| over the wet one | 13 % → 13 % | 0.84 | 1.00 | 22 |
| long, no reload | 37 % → 37 % | 0.84 | 1.00 | 153 | quarters: 0.35 → 0.34 → 0.34 → 0.35

Numbers say: pressure barely changes the width; the long stroke does not run out of paint.

## Brush Artist · Charcoal C7 (pastel path, charcoal tip)
Pastel · 26 px · 10.4 s

![Brush Artist · Charcoal C7 (pastel path, charcoal tip)](Brush-Artist-Charcoal-C7-pastel-path-charcoal-tip.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 4 % → 4 % | 0.80 | 1.00 | 22 |
| heavy line | 5 % → 5 % | 0.80 | 1.00 | 29 |
| pressure swell | 4 % → 4 % | 0.80 | 1.00 | 20 |
| fast wave | 14 % → 14 % | 0.80 | 1.00 | 85 |
| slow wave | 13 % → 13 % | 0.80 | 1.00 | 127 |
| spiral | 20 % → 20 % | 0.80 | 1.00 | 126 |
| loop | 10 % → 10 % | 0.80 | 1.00 | 61 |
| tilted | 4 % → 4 % | 0.80 | 1.00 | 62 |
| over the wet one | 9 % → 9 % | 0.80 | 1.00 | 42 |
| long, no reload | 23 % → 23 % | 0.80 | 1.00 | 271 | quarters: 0.21 → 0.20 → 0.21 → 0.21

Numbers say: the long stroke does not run out of paint.

## Brush Artist · Ink brush · caricature 2 — own sheet
own sheet 600 × 600 · Ink · 16 px · 4.9 s

![Brush Artist · Ink brush · caricature 2 — own sheet](Brush-Artist-Ink-brush-caricature-2-own-sheet.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| lens L | 34 % → 40 % | 0.88 | 1.17 | 120 |
| lens R | 34 % → 35 % | 0.88 | 1.04 | 95 |
| brow L | 29 % → 31 % | 0.87 | 1.08 | 45 |
| brow R | 32 % → 34 % | 0.88 | 1.06 | 42 |
| nose | 28 % → 30 % | 0.86 | 1.09 | 33 |
| beard0 | 18 % → 23 % | 0.83 | 1.33 | 13 |
| beard1 | 18 % → 25 % | 0.83 | 1.38 | 10 |
| beard2 | 19 % → 25 % | 0.83 | 1.33 | 13 |
| beard3 | 19 % → 26 % | 0.83 | 1.33 | 10 |
| beard4 | 19 % → 24 % | 0.84 | 1.26 | 11 |
| beard5 | 18 % → 24 % | 0.84 | 1.31 | 11 |
| beard6 | 18 % → 24 % | 0.83 | 1.32 | 24 |

## Brush Artist · Ink dry G (opaque) · Krovostok — own sheet
own sheet 600 × 600 · Gouache · 30 px · 3.0 s

![Brush Artist · Ink dry G (opaque) · Krovostok — own sheet](Brush-Artist-Ink-dry-G-opaque-Krovostok-own-sheet.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| ear | 10 % → 2 % | 0.79 | 0.20 | 555 |
| drag0 | 18 % → 17 % | 0.79 | 0.91 | 122 |
| drag1 | 22 % → 17 % | 0.79 | 0.79 | 106 |
| drag2 | 24 % → 17 % | 0.79 | 0.71 | 88 |
| drag3 | 26 % → 17 % | 0.79 | 0.64 | 77 |

## Brush Artist · Watercolour wash V6 · Shrigley — own sheet
own sheet 600 × 600 · Watercolor · 40 px · 10.5 s

![Brush Artist · Watercolour wash V6 · Shrigley — own sheet](Brush-Artist-Watercolour-wash-V6-Shrigley-own-sheet.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| s0 | 14 % → 28 % | 0.46 | 2.08 | 38 |
| s1 | 8 % → 38 % | 0.47 | 4.51 | 39 |
| s2 | 13 % → 22 % | 0.44 | 1.80 | 36 |
| s3 | 11 % → 19 % | 0.44 | 1.70 | 45 |
| s4 | 18 % → 35 % | 0.48 | 2.01 | 58 |
| s5 | 25 % → 33 % | 0.50 | 1.35 | 46 |
| s6 | 25 % → 31 % | 0.47 | 1.24 | 53 |
| s7 | 27 % → 36 % | 0.45 | 1.31 | 41 |
| s8 | 22 % → 26 % | 0.44 | 1.21 | 51 |

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Charcoal C6 · Guston hand — own sheet
own sheet 600 × 600 · Charcoal · 30 px · 1.2 s

![Brush Artist · Charcoal C6 · Guston hand — own sheet](Brush-Artist-Charcoal-C6-Guston-hand-own-sheet.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| finger0 | 20 % → 26 % | 0.84 | 1.29 | 61 |
| tip0 | 19 % → 28 % | 0.84 | 1.45 | 10 |
| finger1 | 20 % → 31 % | 0.84 | 1.53 | 37 |
| tip1 | 25 % → 34 % | 0.84 | 1.34 | 12 |
| finger2 | 20 % → 28 % | 0.84 | 1.40 | 32 |
| tip2 | 25 % → 33 % | 0.84 | 1.35 | 10 |
| finger3 | 20 % → 23 % | 0.84 | 1.13 | 31 |
| tip3 | 25 % → 25 % | 0.84 | 1.00 | 11 |
| cig0 | 41 % → 51 % | 0.84 | 1.25 | 13 |
| cig1 | 45 % → 56 % | 0.85 | 1.24 | 12 |
| cig2 | 49 % → 59 % | 0.85 | 1.21 | 13 |
| cig3 | 52 % → 60 % | 0.84 | 1.15 | 13 |
| cig4 | 52 % → 56 % | 0.84 | 1.08 | 12 |
| cig5 | 53 % → 53 % | 0.84 | 1.00 | 13 |

Numbers say: wet paint spreads well beyond the stroke.

