![All brushes](contact.png)

# Brush Lab — 5 brushes · Nov 2, 2026 at 11:11 PM

Every sheet: 1500 × 600, ten strokes in a 5 × 2 grid — 1. light line · 2. heavy line · 3. pressure swell · 4. fast wave · 5. slow wave · 6. spiral · 7. loop · 8. tilted · 9. over the wet one · 10. long, no reload (cell 8 holds «tilted» and «over the wet one» crossed). The CPU reference of Mamay's paint engine; the wet layer settles 20 s at the end.

Columns: **covered** = share of the cell with paint right after the stroke → after settling; **dark** = mean darkness of the painted pixels; **spread** = how far wet paint went beyond the stroke (1.0 = stayed); **ms** = the stroke on the CPU; long stroke: paint in each quarter of its length (it should run out: wet → streaks → dry tail).

## Ink Line
Ink · 12 px · 22.1 s

![Ink Line](Ink-Line.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 1 % → 4 % | 0.08 | 2.44 | 39 |
| heavy line | 5 % → 6 % | 0.10 | 1.13 | 67 |
| pressure swell | 3 % → 4 % | 0.08 | 1.40 | 38 |
| fast wave | 10 % → 11 % | 0.12 | 1.11 | 119 |
| slow wave | 8 % → 10 % | 0.11 | 1.16 | 111 |
| spiral | 14 % → 15 % | 0.13 | 1.07 | 214 |
| loop | 8 % → 9 % | 0.11 | 1.16 | 109 |
| tilted | 5 % → 11 % | 0.13 | 2.14 | 60 |
| over the wet one | 10 % → 11 % | 0.13 | 1.15 | 50 |
| long, no reload | 18 % → 17 % | 0.14 | 0.96 | 387 | quarters: 0.27 → 0.15 → 0.10 → 0.08

Numbers say: wet paint spreads well beyond the stroke.

## Charcoal
Charcoal · 5 px · 9.4 s

![Charcoal](Charcoal.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 1 % → 1 % | 0.06 | 1.00 | 18 |
| heavy line | 1 % → 1 % | 0.06 | 1.00 | 15 |
| pressure swell | 1 % → 1 % | 0.06 | 1.00 | 9 |
| fast wave | 2 % → 2 % | 0.07 | 1.00 | 31 |
| slow wave | 2 % → 2 % | 0.07 | 1.00 | 30 |
| spiral | 4 % → 4 % | 0.08 | 1.00 | 64 |
| loop | 2 % → 2 % | 0.07 | 1.00 | 27 |
| tilted | 2 % → 2 % | 0.07 | 1.56 | 19 |
| over the wet one | 2 % → 2 % | 0.07 | 1.00 | 11 |
| long, no reload | 6 % → 6 % | 0.10 | 1.00 | 75 | quarters: 0.10 → 0.10 → 0.10 → 0.11

Numbers say: the long stroke does not run out of paint; wet paint spreads well beyond the stroke.

## Watercolour — wash
Watercolor · 50 px · 34.3 s

![Watercolour — wash](Watercolour-wash.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 9 % → 11 % | 0.06 | 1.22 | 103 |
| heavy line | 12 % → 14 % | 0.06 | 1.17 | 105 |
| pressure swell | 8 % → 10 % | 0.06 | 1.22 | 70 |
| fast wave | 26 % → 30 % | 0.06 | 1.18 | 233 |
| slow wave | 25 % → 29 % | 0.06 | 1.18 | 385 |
| spiral | 39 % → 46 % | 0.06 | 1.17 | 446 |
| loop | 22 % → 27 % | 0.06 | 1.21 | 201 |
| tilted | 10 % → 25 % | 0.06 | 2.57 | 182 |
| over the wet one | 22 % → 25 % | 0.06 | 1.14 | 127 |
| long, no reload | 45 % → 54 % | 0.06 | 1.18 | 563 | quarters: 0.06 → 0.06 → 0.06 → 0.06

Numbers say: the long stroke does not run out of paint; wet paint spreads well beyond the stroke.

## Gouache
Gouache · 30 px · 28.3 s

![Gouache](Gouache.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 8 % → 6 % | 0.07 | 0.67 | 67 |
| heavy line | 13 % → 6 % | 0.07 | 0.47 | 79 |
| pressure swell | 10 % → 6 % | 0.07 | 0.61 | 55 |
| fast wave | 27 % → 7 % | 0.09 | 0.27 | 184 |
| slow wave | 27 % → 7 % | 0.09 | 0.27 | 317 |
| spiral | 37 % → 8 % | 0.09 | 0.22 | 313 |
| loop | 22 % → 8 % | 0.08 | 0.36 | 161 |
| tilted | 9 % → 13 % | 0.08 | 1.52 | 93 |
| over the wet one | 20 % → 13 % | 0.08 | 0.67 | 76 |
| long, no reload | 38 % → 10 % | 0.09 | 0.25 | 434 | quarters: 0.14 → 0.10 → 0.08 → 0.06

Numbers say: wet paint spreads well beyond the stroke.

## Brush Artist · Sumi — wetter
Watercolor · 24 px · 30.4 s

![Brush Artist · Sumi — wetter](Brush-Artist-Sumi-wetter.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 5 % → 6 % | 0.07 | 1.11 | 43 |
| heavy line | 11 % → 12 % | 0.07 | 1.13 | 72 |
| pressure swell | 7 % → 8 % | 0.07 | 1.13 | 48 |
| fast wave | 21 % → 24 % | 0.09 | 1.15 | 176 |
| slow wave | 19 % → 22 % | 0.09 | 1.14 | 262 |
| spiral | 29 % → 32 % | 0.10 | 1.13 | 293 |
| loop | 17 % → 19 % | 0.08 | 1.15 | 152 |
| tilted | 6 % → 17 % | 0.08 | 2.83 | 125 |
| over the wet one | 16 % → 17 % | 0.08 | 1.07 | 97 |
| long, no reload | 33 % → 37 % | 0.10 | 1.12 | 724 | quarters: 0.16 → 0.11 → 0.09 → 0.08

Numbers say: wet paint spreads well beyond the stroke.

