![All brushes](contact.png)

# Brush Lab — 6 brushes · Nov 2, 2026 at 11:28 PM

Every sheet: 1500 × 600, ten strokes in a 5 × 2 grid — 1. light line · 2. heavy line · 3. pressure swell · 4. fast wave · 5. slow wave · 6. spiral · 7. loop · 8. tilted · 9. over the wet one · 10. long, no reload (cell 8 holds «tilted» and «over the wet one» crossed). The CPU reference of Mamay's paint engine; the wet layer settles 20 s at the end.

Columns: **covered** = share of the cell with paint right after the stroke → after settling; **dark** = mean darkness of the painted pixels above the paper's own grain (0 = paper, 1 = black); **spread** = how far wet paint went beyond the stroke (1.0 = stayed); **ms** = the stroke on the CPU; long stroke: paint in each quarter of its length (it should run out: wet → streaks → dry tail).

## Water
Watercolor · 20 px · 36.7 s · over bands of wet ink and oil pastel in turn (it works on paint already there: look at what it does to the bands; covered counts the bands too)

![Water](Water.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 31 % → 35 % | 0.81 | 1.15 | 26 |
| heavy line | 31 % → 35 % | 0.80 | 1.10 | 55 |
| pressure swell | 31 % → 33 % | 0.82 | 1.06 | 31 |
| fast wave | 32 % → 34 % | 0.82 | 1.07 | 101 |
| slow wave | 32 % → 34 % | 0.82 | 1.05 | 192 |
| spiral | 33 % → 34 % | 0.81 | 1.06 | 180 |
| loop | 32 % → 33 % | 0.82 | 1.03 | 85 |
| tilted | 32 % → 32 % | 0.82 | 1.00 | 56 |
| over the wet one | 32 % → 34 % | 0.82 | 1.05 | 44 |
| long, no reload | 32 % → 34 % | 0.82 | 1.06 | 253 | quarters: 0.25 → 0.34 → 0.26 → 0.34

Numbers say: pressure barely changes the width; the long stroke does not run out of paint.

## Blender
Pastel · 16 px · 31.5 s · over bands of wet ink and oil pastel in turn (it works on paint already there: look at what it does to the bands; covered counts the bands too)

![Blender](Blender.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 30 % → 33 % | 0.82 | 1.10 | 29 |
| heavy line | 31 % → 33 % | 0.82 | 1.05 | 34 |
| pressure swell | 32 % → 33 % | 0.82 | 1.03 | 21 |
| fast wave | 34 % → 34 % | 0.81 | 1.01 | 70 |
| slow wave | 34 % → 34 % | 0.81 | 1.00 | 108 |
| spiral | 36 % → 36 % | 0.79 | 1.00 | 164 |
| loop | 33 % → 33 % | 0.81 | 1.00 | 61 |
| tilted | 33 % → 33 % | 0.81 | 1.00 | 44 |
| over the wet one | 34 % → 34 % | 0.81 | 1.00 | 29 |
| long, no reload | 38 % → 38 % | 0.78 | 1.00 | 193 | quarters: 0.23 → 0.35 → 0.30 → 0.37

Numbers say: pressure barely changes the width; the long stroke does not run out of paint.

## Eraser
Eraser · 16 px · 31.5 s · over bands of wet ink and oil pastel in turn (it works on paint already there: look at what it does to the bands; covered counts the bands too)

![Eraser](Eraser.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 29 % → 32 % | 0.83 | 1.10 | 32 |
| heavy line | 31 % → 32 % | 0.83 | 1.05 | 34 |
| pressure swell | 31 % → 32 % | 0.83 | 1.03 | 22 |
| fast wave | 32 % → 32 % | 0.83 | 1.01 | 73 |
| slow wave | 32 % → 32 % | 0.83 | 1.00 | 112 |
| spiral | 32 % → 32 % | 0.83 | 1.00 | 168 |
| loop | 32 % → 32 % | 0.83 | 1.00 | 66 |
| tilted | 32 % → 32 % | 0.83 | 1.00 | 45 |
| over the wet one | 32 % → 32 % | 0.83 | 1.00 | 31 |
| long, no reload | 32 % → 32 % | 0.83 | 1.00 | 212 | quarters: 0.22 → 0.32 → 0.25 → 0.33

Numbers say: pressure barely changes the width; the long stroke does not run out of paint.

## 0.45 · Eraser
Eraser · 30 px · 32.6 s · over bands of wet ink and oil pastel in turn (it works on paint already there: look at what it does to the bands; covered counts the bands too)

![0.45 · Eraser](0-45-Eraser.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 29 % → 32 % | 0.83 | 1.10 | 38 |
| heavy line | 30 % → 32 % | 0.83 | 1.05 | 77 |
| pressure swell | 31 % → 32 % | 0.83 | 1.03 | 52 |
| fast wave | 31 % → 31 % | 0.80 | 1.02 | 114 |
| slow wave | 28 % → 28 % | 0.82 | 1.00 | 196 |
| spiral | 28 % → 28 % | 0.80 | 1.00 | 197 |
| loop | 29 % → 29 % | 0.81 | 1.00 | 107 |
| tilted | 31 % → 31 % | 0.82 | 1.00 | 54 |
| over the wet one | 30 % → 30 % | 0.82 | 1.00 | 67 |
| long, no reload | 23 % → 23 % | 0.79 | 1.00 | 350 | quarters: 0.15 → 0.21 → 0.18 → 0.22

Numbers say: pressure barely changes the width; the long stroke does not run out of paint.

## Lift wet paint
Eraser · 30 px · 32.0 s · over bands of wet ink and oil pastel in turn (it works on paint already there: look at what it does to the bands; covered counts the bands too)

![Lift wet paint](Lift-wet-paint.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 29 % → 32 % | 0.83 | 1.10 | 30 |
| heavy line | 31 % → 32 % | 0.83 | 1.05 | 67 |
| pressure swell | 31 % → 32 % | 0.83 | 1.03 | 40 |
| fast wave | 32 % → 32 % | 0.83 | 1.01 | 91 |
| slow wave | 32 % → 32 % | 0.83 | 1.00 | 154 |
| spiral | 32 % → 32 % | 0.83 | 1.00 | 154 |
| loop | 32 % → 32 % | 0.83 | 1.00 | 84 |
| tilted | 32 % → 32 % | 0.83 | 1.00 | 47 |
| over the wet one | 32 % → 32 % | 0.83 | 1.00 | 38 |
| long, no reload | 32 % → 32 % | 0.83 | 1.00 | 302 | quarters: 0.22 → 0.32 → 0.25 → 0.33

Numbers say: pressure barely changes the width; the long stroke does not run out of paint.

## Sgraffito
Eraser · 10 px · 29.9 s · over bands of wet ink and oil pastel in turn (it works on paint already there: look at what it does to the bands; covered counts the bands too)

![Sgraffito](Sgraffito.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 29 % → 32 % | 0.82 | 1.08 | 9 |
| heavy line | 31 % → 32 % | 0.82 | 1.04 | 8 |
| pressure swell | 31 % → 32 % | 0.82 | 1.02 | 5 |
| fast wave | 32 % → 31 % | 0.82 | 0.98 | 19 |
| slow wave | 32 % → 31 % | 0.82 | 0.97 | 21 |
| spiral | 32 % → 31 % | 0.82 | 0.96 | 51 |
| loop | 32 % → 32 % | 0.82 | 0.99 | 20 |
| tilted | 32 % → 32 % | 0.82 | 0.99 | 8 |
| over the wet one | 32 % → 32 % | 0.82 | 0.99 | 8 |
| long, no reload | 32 % → 32 % | 0.82 | 1.00 | 46 | quarters: 0.21 → 0.31 → 0.25 → 0.32

Numbers say: pressure barely changes the width; the long stroke does not run out of paint.

