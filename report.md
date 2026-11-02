![All brushes](contact.png)

# Brush Lab — 7 brushes · Nov 2, 2026 at 11:25 PM

Every sheet: 1500 × 600, ten strokes in a 5 × 2 grid — 1. light line · 2. heavy line · 3. pressure swell · 4. fast wave · 5. slow wave · 6. spiral · 7. loop · 8. tilted · 9. over the wet one · 10. long, no reload (cell 8 holds «tilted» and «over the wet one» crossed). The CPU reference of Mamay's paint engine; the wet layer settles 20 s at the end.

Columns: **covered** = share of the cell with paint right after the stroke → after settling; **dark** = mean darkness of the painted pixels above the paper's own grain (0 = paper, 1 = black); **spread** = how far wet paint went beyond the stroke (1.0 = stayed); **ms** = the stroke on the CPU; long stroke: paint in each quarter of its length (it should run out: wet → streaks → dry tail).

## Water
Watercolor · 20 px · 72.1 s · over bands of dense ink (it works on paint already there: look at what it does to the bands; covered counts the bands too)

![Water](Water.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 95 % → 95 % | 0.84 | 1.00 | 30 |
| heavy line | 96 % → 96 % | 0.84 | 1.00 | 63 |
| pressure swell | 96 % → 96 % | 0.84 | 1.00 | 39 |
| fast wave | 96 % → 96 % | 0.84 | 1.00 | 110 |
| slow wave | 94 % → 94 % | 0.84 | 1.00 | 151 |
| spiral | 94 % → 94 % | 0.84 | 1.00 | 185 |
| loop | 95 % → 95 % | 0.84 | 1.00 | 93 |
| tilted | 95 % → 95 % | 0.84 | 1.00 | 66 |
| over the wet one | 95 % → 95 % | 0.84 | 1.00 | 45 |
| long, no reload | 94 % → 94 % | 0.84 | 1.00 | 336 | quarters: 0.81 → 0.81 → 0.81 → 0.81

Numbers say: pressure barely changes the width; the long stroke does not run out of paint.

## Blender
Pastel · 16 px · 72.0 s · over bands of dense ink (it works on paint already there: look at what it does to the bands; covered counts the bands too)

![Blender](Blender.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 95 % → 95 % | 0.84 | 1.00 | 31 |
| heavy line | 96 % → 96 % | 0.84 | 1.00 | 36 |
| pressure swell | 96 % → 96 % | 0.84 | 1.00 | 28 |
| fast wave | 96 % → 96 % | 0.84 | 1.00 | 76 |
| slow wave | 94 % → 94 % | 0.84 | 1.00 | 87 |
| spiral | 94 % → 94 % | 0.84 | 1.00 | 138 |
| loop | 95 % → 95 % | 0.84 | 1.00 | 66 |
| tilted | 95 % → 95 % | 0.84 | 1.00 | 38 |
| over the wet one | 95 % → 95 % | 0.84 | 1.00 | 31 |
| long, no reload | 94 % → 94 % | 0.84 | 1.00 | 215 | quarters: 0.81 → 0.81 → 0.81 → 0.81

Numbers say: pressure barely changes the width; the long stroke does not run out of paint.

## Eraser
Eraser · 16 px · 71.9 s · over bands of dense ink (it works on paint already there: look at what it does to the bands; covered counts the bands too)

![Eraser](Eraser.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 95 % → 95 % | 0.84 | 1.00 | 39 |
| heavy line | 96 % → 96 % | 0.84 | 1.00 | 49 |
| pressure swell | 96 % → 96 % | 0.84 | 1.00 | 32 |
| fast wave | 96 % → 96 % | 0.84 | 1.00 | 104 |
| slow wave | 94 % → 94 % | 0.84 | 1.00 | 119 |
| spiral | 94 % → 94 % | 0.84 | 1.00 | 182 |
| loop | 95 % → 95 % | 0.84 | 1.00 | 88 |
| tilted | 95 % → 95 % | 0.84 | 1.00 | 52 |
| over the wet one | 95 % → 95 % | 0.84 | 1.00 | 43 |
| long, no reload | 94 % → 94 % | 0.84 | 1.00 | 361 | quarters: 0.81 → 0.81 → 0.81 → 0.81

Numbers say: pressure barely changes the width; the long stroke does not run out of paint.

## Finger on oil
Oil · 30 px · 12.9 s

![Finger on oil](Finger-on-oil.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 8 % → 8 % | 0.34 | 1.00 | 51 |
| heavy line | 12 % → 12 % | 0.30 | 1.00 | 59 |
| pressure swell | 8 % → 8 % | 0.35 | 1.00 | 35 |
| fast wave | 16 % → 16 % | 0.22 | 1.00 | 117 |
| slow wave | 17 % → 17 % | 0.23 | 1.00 | 194 |
| spiral | 18 % → 18 % | 0.22 | 1.00 | 191 |
| loop | 18 % → 18 % | 0.23 | 1.00 | 96 |
| tilted | 9 % → 9 % | 0.31 | 1.00 | 97 |
| over the wet one | 18 % → 18 % | 0.31 | 1.00 | 64 |
| long, no reload | 15 % → 15 % | 0.23 | 1.00 | 297 | quarters: 0.13 → 0.01 → 0.00 → 0.00

## 0.45 · Eraser
Eraser · 30 px · 75.8 s · over bands of dense ink (it works on paint already there: look at what it does to the bands; covered counts the bands too)

![0.45 · Eraser](0-45-Eraser.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 95 % → 95 % | 0.81 | 1.00 | 56 |
| heavy line | 94 % → 94 % | 0.81 | 1.00 | 60 |
| pressure swell | 94 % → 94 % | 0.81 | 1.00 | 44 |
| fast wave | 88 % → 88 % | 0.80 | 1.00 | 160 |
| slow wave | 80 % → 80 % | 0.82 | 1.00 | 243 |
| spiral | 80 % → 79 % | 0.78 | 1.00 | 343 |
| loop | 88 % → 88 % | 0.80 | 1.00 | 156 |
| tilted | 92 % → 92 % | 0.81 | 1.00 | 64 |
| over the wet one | 89 % → 89 % | 0.81 | 1.00 | 63 |
| long, no reload | 70 % → 70 % | 0.77 | 1.00 | 341 | quarters: 0.56 → 0.55 → 0.54 → 0.53

Numbers say: pressure barely changes the width; the long stroke does not run out of paint.

## Lift wet paint
Eraser · 30 px · 76.1 s · over bands of dense ink (it works on paint already there: look at what it does to the bands; covered counts the bands too)

![Lift wet paint](Lift-wet-paint.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 95 % → 95 % | 0.84 | 1.00 | 47 |
| heavy line | 96 % → 96 % | 0.84 | 1.00 | 54 |
| pressure swell | 96 % → 96 % | 0.84 | 1.00 | 41 |
| fast wave | 96 % → 96 % | 0.84 | 1.00 | 125 |
| slow wave | 94 % → 94 % | 0.84 | 1.00 | 210 |
| spiral | 94 % → 94 % | 0.84 | 1.00 | 316 |
| loop | 95 % → 95 % | 0.84 | 1.00 | 149 |
| tilted | 95 % → 95 % | 0.84 | 1.00 | 68 |
| over the wet one | 95 % → 95 % | 0.84 | 1.00 | 60 |
| long, no reload | 94 % → 94 % | 0.84 | 1.00 | 327 | quarters: 0.81 → 0.81 → 0.81 → 0.81

Numbers say: pressure barely changes the width; the long stroke does not run out of paint.

## Sgraffito
Eraser · 10 px · 70.0 s · over bands of dense ink (it works on paint already there: look at what it does to the bands; covered counts the bands too)

![Sgraffito](Sgraffito.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 95 % → 95 % | 0.84 | 1.00 | 16 |
| heavy line | 96 % → 96 % | 0.84 | 1.00 | 13 |
| pressure swell | 96 % → 96 % | 0.84 | 1.00 | 9 |
| fast wave | 96 % → 96 % | 0.84 | 1.00 | 29 |
| slow wave | 94 % → 94 % | 0.84 | 1.00 | 31 |
| spiral | 94 % → 94 % | 0.84 | 1.00 | 72 |
| loop | 95 % → 95 % | 0.84 | 1.00 | 25 |
| tilted | 95 % → 95 % | 0.84 | 1.00 | 10 |
| over the wet one | 95 % → 95 % | 0.84 | 1.00 | 11 |
| long, no reload | 94 % → 94 % | 0.84 | 1.00 | 71 | quarters: 0.81 → 0.81 → 0.81 → 0.81

Numbers say: pressure barely changes the width; the long stroke does not run out of paint.

