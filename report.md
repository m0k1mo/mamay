![All brushes](contact.png)

# Brush Lab — 1 brushes · Nov 2, 2026 at 11:57 PM

Every sheet: 1500 × 600, ten strokes in a 5 × 2 grid — 1. light line · 2. heavy line · 3. pressure swell · 4. fast wave · 5. slow wave · 6. spiral · 7. loop · 8. tilted · 9. over the wet one · 10. long, no reload (cell 8 holds «tilted» and «over the wet one» crossed). The CPU reference of Mamay's paint engine; the wet layer settles 20 s at the end.

Columns: **covered** = share of the cell with paint right after the stroke → after settling; **dark** = mean darkness of the painted pixels above the paper's own grain (0 = paper, 1 = black); **spread** = how far wet paint went beyond the stroke (1.0 = stayed); **ms** = the stroke on the CPU; long stroke: paint in each quarter of its length (it should run out: wet → streaks → dry tail).

## Ink Line
Ink · 12 px · 25.2 s

![Ink Line](Ink-Line.png)

| stroke | covered | dark | spread | ms |
|---|---|---|---|---|
| light line | 1 % → 4 % | 0.55 | 2.44 | 35 |
| heavy line | 5 % → 6 % | 0.68 | 1.13 | 65 |
| pressure swell | 3 % → 4 % | 0.64 | 1.40 | 45 |
| fast wave | 10 % → 11 % | 0.59 | 1.11 | 130 |
| slow wave | 8 % → 10 % | 0.57 | 1.16 | 123 |
| spiral | 14 % → 15 % | 0.50 | 1.07 | 226 |
| loop | 8 % → 9 % | 0.61 | 1.16 | 132 |
| tilted | 5 % → 5 % | 0.65 | 1.05 | 67 |
| over the wet one | 10 % → 11 % | 0.65 | 1.15 | 65 |
| long, no reload | 18 % → 17 % | 0.47 | 0.96 | 350 | quarters: 0.22 → 0.09 → 0.04 → 0.02

Numbers say: wet paint spreads well beyond the stroke.

