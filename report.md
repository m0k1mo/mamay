![All brushes](contact.png)

# Brush Lab — 100 brushes · Nov 9, 2026 at 4:05 AM

Every sheet: 1500 × 600, ten strokes in a 5 × 2 grid — 1. light line · 2. heavy line · 3. pressure swell · 4. fast wave · 5. slow wave · 6. spiral · 7. loop · 8. tilted · 9. over the wet one · 10. long, no reload (cell 8 holds «tilted» and «over the wet one» crossed). The CPU reference of Mamay's paint engine; the wet layer settles 20 s at the end.

Columns: **covered** = share of the cell with paint right after the stroke → after settling; **width** = painted area of the stroke ÷ its length (px); **dark** = mean darkness of the painted pixels above the paper's own grain (0 = paper, 1 = black); **spread** = how far wet paint went beyond the stroke (1.0 = stayed); **ms** = the stroke on the CPU; long stroke: paint in each quarter of its length (it should run out: wet → streaks → dry tail).

## Refs v3 · #01 HW peach cloud
Gouache 1.00 + turpentine 35 % · 240 px · 115.7 s

![Refs v3 · #01 HW peach cloud](Refs-v3-01-HW-peach-cloud.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 69 % → 67 % | 201.0 px | 0.31 | 0.97 | 1434 |
| heavy line | 71 % → 63 % | 206.5 px | 0.31 | 0.89 | 2128 |
| pressure swell | 61 % → 70 % | 230.0 px | 0.28 | 1.14 | 1483 |
| fast wave | 98 % → 82 % | 113.5 px | 0.25 | 0.84 | 6372 |
| slow wave | 99 % → 65 % | 114.5 px | 0.27 | 0.65 | 8239 |
| spiral | 100 % → 66 % | 65.7 px | 0.26 | 0.66 | 8019 |
| loop | 99 % → 78 % | 128.4 px | 0.28 | 0.78 | 4631 |
| tilted | 53 % → 53 % | 148.0 px | 0.27 | 1.00 | 2315 |
| over the wet one | 90 % → 83 % | 103.1 px | 0.27 | 0.92 | 1861 |
| long, no reload | 100 % → 68 % | 44.8 px | 0.26 | 0.68 | 11679 | quarters: 0.00 → 0.00 → 0.00 → 0.00

Numbers say: light vs heavy: width 201.0 → 206.5 px, dark 0.31 → 0.31; pressure barely changes the width.

## Refs v3 · #02 HW cream strokes
Gouache 1.00 + turpentine 35 % · 240 px · 116.5 s

![Refs v3 · #02 HW cream strokes](Refs-v3-02-HW-cream-strokes.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 69 % → 67 % | 201.0 px | 0.33 | 0.97 | 1352 |
| heavy line | 71 % → 63 % | 206.5 px | 0.33 | 0.89 | 2108 |
| pressure swell | 61 % → 70 % | 230.0 px | 0.31 | 1.14 | 1411 |
| fast wave | 98 % → 82 % | 113.5 px | 0.29 | 0.84 | 6562 |
| slow wave | 99 % → 65 % | 114.5 px | 0.30 | 0.65 | 8183 |
| spiral | 100 % → 66 % | 65.7 px | 0.30 | 0.66 | 8029 |
| loop | 99 % → 78 % | 128.4 px | 0.31 | 0.78 | 4519 |
| tilted | 53 % → 53 % | 148.0 px | 0.30 | 1.00 | 2306 |
| over the wet one | 90 % → 83 % | 103.1 px | 0.30 | 0.92 | 1845 |
| long, no reload | 100 % → 68 % | 44.8 px | 0.30 | 0.68 | 11626 | quarters: 0.00 → 0.00 → 0.00 → 0.00

Numbers say: light vs heavy: width 201.0 → 206.5 px, dark 0.33 → 0.33; pressure barely changes the width.

## Refs v3 · #03 HW navy contours
Gouache 1.00 + turpentine 35 % · 240 px · 117.5 s

![Refs v3 · #03 HW navy contours](Refs-v3-03-HW-navy-contours.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 69 % → 67 % | 201.0 px | 0.34 | 0.97 | 1423 |
| heavy line | 71 % → 63 % | 206.5 px | 0.34 | 0.89 | 2038 |
| pressure swell | 61 % → 70 % | 230.0 px | 0.32 | 1.14 | 1434 |
| fast wave | 98 % → 82 % | 113.5 px | 0.30 | 0.84 | 6881 |
| slow wave | 99 % → 65 % | 114.5 px | 0.31 | 0.65 | 8458 |
| spiral | 100 % → 66 % | 65.7 px | 0.31 | 0.66 | 8031 |
| loop | 99 % → 78 % | 128.4 px | 0.32 | 0.78 | 4897 |
| tilted | 53 % → 53 % | 148.0 px | 0.31 | 1.00 | 2425 |
| over the wet one | 90 % → 83 % | 103.1 px | 0.31 | 0.92 | 1920 |
| long, no reload | 100 % → 68 % | 44.8 px | 0.30 | 0.68 | 12294 | quarters: 0.00 → 0.00 → 0.00 → 0.00

Numbers say: light vs heavy: width 201.0 → 206.5 px, dark 0.34 → 0.34; pressure barely changes the width.

## Refs v3 · #04 HW grey cloud
Gouache 1.00 + turpentine 30 % · 240 px · 117.0 s

![Refs v3 · #04 HW grey cloud](Refs-v3-04-HW-grey-cloud.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 69 % → 67 % | 201.1 px | 0.17 | 0.97 | 1413 |
| heavy line | 71 % → 63 % | 206.4 px | 0.18 | 0.89 | 1629 |
| pressure swell | 61 % → 70 % | 229.7 px | 0.21 | 1.14 | 1206 |
| fast wave | 98 % → 83 % | 113.5 px | 0.24 | 0.84 | 5194 |
| slow wave | 99 % → 65 % | 114.5 px | 0.21 | 0.66 | 8832 |
| spiral | 100 % → 68 % | 65.8 px | 0.24 | 0.68 | 8366 |
| loop | 99 % → 80 % | 128.4 px | 0.21 | 0.80 | 5668 |
| tilted | 53 % → 53 % | 148.2 px | 0.23 | 1.00 | 2717 |
| over the wet one | 90 % → 83 % | 103.0 px | 0.23 | 0.93 | 1906 |
| long, no reload | 100 % → 69 % | 44.8 px | 0.23 | 0.69 | 12037 | quarters: 0.22 → 0.23 → 0.22 → 0.15

Numbers say: light vs heavy: width 201.1 → 206.4 px, dark 0.17 → 0.18; pressure barely changes the width.

## Refs v3 · #05 HW green in rust loops
Gouache 1.00 + water 15 % · 240 px · 106.6 s

![Refs v3 · #05 HW green in rust loops](Refs-v3-05-HW-green-in-rust-loops.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 70 % → 71 % | 203.7 px | 0.37 | 1.01 | 1287 |
| heavy line | 72 % → 66 % | 210.1 px | 0.37 | 0.91 | 1788 |
| pressure swell | 63 % → 71 % | 236.5 px | 0.34 | 1.13 | 1354 |
| fast wave | 93 % → 93 % | 108.0 px | 0.32 | 0.99 | 3926 |
| slow wave | 97 % → 84 % | 111.7 px | 0.36 | 0.87 | 6935 |
| spiral | 96 % → 84 % | 63.1 px | 0.34 | 0.88 | 6660 |
| loop | 98 % → 93 % | 126.6 px | 0.36 | 0.96 | 3586 |
| tilted | 51 % → 52 % | 143.6 px | 0.33 | 1.00 | 3223 |
| over the wet one | 89 % → 87 % | 104.9 px | 0.33 | 0.97 | 1678 |
| long, no reload | 98 % → 95 % | 44.2 px | 0.35 | 0.96 | 9627 | quarters: 0.00 → 0.00 → 0.00 → 0.00

Numbers say: light vs heavy: width 203.7 → 210.1 px, dark 0.37 → 0.37; pressure barely changes the width.

## Refs v3 · #06 HW scrubbed grey
Gouache 1.00 + turpentine 30 % · 240 px · 113.4 s

![Refs v3 · #06 HW scrubbed grey](Refs-v3-06-HW-scrubbed-grey.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 69 % → 67 % | 201.1 px | 0.17 | 0.97 | 1381 |
| heavy line | 71 % → 63 % | 206.4 px | 0.18 | 0.89 | 1591 |
| pressure swell | 61 % → 70 % | 229.7 px | 0.21 | 1.14 | 1862 |
| fast wave | 98 % → 83 % | 113.5 px | 0.24 | 0.84 | 4574 |
| slow wave | 99 % → 65 % | 114.5 px | 0.21 | 0.66 | 8649 |
| spiral | 100 % → 68 % | 65.8 px | 0.24 | 0.68 | 8109 |
| loop | 99 % → 80 % | 128.4 px | 0.21 | 0.80 | 5454 |
| tilted | 53 % → 53 % | 148.2 px | 0.23 | 1.00 | 2392 |
| over the wet one | 90 % → 83 % | 103.0 px | 0.23 | 0.93 | 1870 |
| long, no reload | 100 % → 69 % | 44.8 px | 0.23 | 0.69 | 11585 | quarters: 0.22 → 0.23 → 0.22 → 0.15

Numbers say: light vs heavy: width 201.1 → 206.4 px, dark 0.17 → 0.18; pressure barely changes the width.

## Refs v3 · #07 HW blue L and zigzag
Gouache 1.00 + turpentine 35 % · 240 px · 112.3 s

![Refs v3 · #07 HW blue L and zigzag](Refs-v3-07-HW-blue-L-and-zigzag.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 69 % → 67 % | 201.0 px | 0.33 | 0.97 | 2246 |
| heavy line | 71 % → 63 % | 206.5 px | 0.34 | 0.89 | 1530 |
| pressure swell | 61 % → 70 % | 230.0 px | 0.31 | 1.14 | 1197 |
| fast wave | 98 % → 82 % | 113.5 px | 0.28 | 0.84 | 4861 |
| slow wave | 99 % → 65 % | 114.5 px | 0.30 | 0.65 | 8807 |
| spiral | 100 % → 66 % | 65.7 px | 0.29 | 0.66 | 8169 |
| loop | 99 % → 78 % | 128.4 px | 0.31 | 0.78 | 3594 |
| tilted | 53 % → 53 % | 148.0 px | 0.30 | 1.00 | 2383 |
| over the wet one | 90 % → 83 % | 103.1 px | 0.30 | 0.92 | 2083 |
| long, no reload | 100 % → 68 % | 44.8 px | 0.29 | 0.68 | 11749 | quarters: 0.00 → 0.00 → 0.00 → 0.00

Numbers say: light vs heavy: width 201.0 → 206.5 px, dark 0.33 → 0.34; pressure barely changes the width.

## Refs v3 · #08 HW lilac crown basket
Gouache 1.00 + turpentine 35 % · 240 px · 110.9 s

![Refs v3 · #08 HW lilac crown basket](Refs-v3-08-HW-lilac-crown-basket.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 69 % → 67 % | 201.0 px | 0.33 | 0.97 | 1771 |
| heavy line | 71 % → 63 % | 206.5 px | 0.33 | 0.89 | 1466 |
| pressure swell | 61 % → 70 % | 230.0 px | 0.31 | 1.14 | 1107 |
| fast wave | 98 % → 82 % | 113.5 px | 0.28 | 0.84 | 4645 |
| slow wave | 99 % → 65 % | 114.5 px | 0.30 | 0.65 | 8091 |
| spiral | 100 % → 66 % | 65.7 px | 0.29 | 0.66 | 8084 |
| loop | 99 % → 78 % | 128.4 px | 0.30 | 0.78 | 4141 |
| tilted | 53 % → 53 % | 148.0 px | 0.30 | 1.00 | 2326 |
| over the wet one | 90 % → 83 % | 103.1 px | 0.30 | 0.92 | 1829 |
| long, no reload | 100 % → 68 % | 44.8 px | 0.28 | 0.68 | 11637 | quarters: 0.00 → 0.00 → 0.00 → 0.00

Numbers say: light vs heavy: width 201.0 → 206.5 px, dark 0.33 → 0.33; pressure barely changes the width.

## Refs v3 · #09 HW white loops
Gouache 1.00 + turpentine 30 % · 240 px · 111.8 s

![Refs v3 · #09 HW white loops](Refs-v3-09-HW-white-loops.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 69 % → 68 % | 201.1 px | 0.27 | 0.98 | 1346 |
| heavy line | 71 % → 63 % | 206.7 px | 0.27 | 0.89 | 1535 |
| pressure swell | 61 % → 70 % | 230.3 px | 0.24 | 1.14 | 1163 |
| fast wave | 98 % → 84 % | 113.5 px | 0.21 | 0.85 | 5260 |
| slow wave | 99 % → 66 % | 114.5 px | 0.23 | 0.66 | 8265 |
| spiral | 100 % → 67 % | 65.8 px | 0.22 | 0.67 | 7805 |
| loop | 99 % → 79 % | 128.4 px | 0.24 | 0.80 | 4197 |
| tilted | 53 % → 53 % | 148.1 px | 0.22 | 1.00 | 2383 |
| over the wet one | 90 % → 83 % | 103.1 px | 0.22 | 0.93 | 2006 |
| long, no reload | 100 % → 69 % | 44.8 px | 0.22 | 0.69 | 11945 | quarters: 0.00 → 0.00 → 0.00 → 0.00

Numbers say: light vs heavy: width 201.1 → 206.7 px, dark 0.27 → 0.27; pressure barely changes the width.

## Refs v3 · #10 HW maroon loops
Gouache 1.00 + turpentine 35 % · 240 px · 137.0 s

![Refs v3 · #10 HW maroon loops](Refs-v3-10-HW-maroon-loops.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 69 % → 67 % | 201.0 px | 0.33 | 0.97 | 1293 |
| heavy line | 71 % → 63 % | 206.6 px | 0.34 | 0.89 | 1670 |
| pressure swell | 61 % → 70 % | 230.2 px | 0.31 | 1.14 | 1092 |
| fast wave | 98 % → 83 % | 113.5 px | 0.28 | 0.85 | 4746 |
| slow wave | 99 % → 65 % | 114.5 px | 0.30 | 0.65 | 8577 |
| spiral | 100 % → 66 % | 65.8 px | 0.29 | 0.66 | 9733 |
| loop | 99 % → 78 % | 128.4 px | 0.31 | 0.78 | 3922 |
| tilted | 53 % → 53 % | 148.0 px | 0.30 | 1.00 | 2446 |
| over the wet one | 90 % → 83 % | 103.1 px | 0.30 | 0.92 | 2386 |
| long, no reload | 100 % → 68 % | 44.8 px | 0.29 | 0.68 | 15894 | quarters: 0.00 → 0.00 → 0.00 → 0.00

Numbers say: light vs heavy: width 201.0 → 206.6 px, dark 0.33 → 0.34; pressure barely changes the width.

## Refs v3 · #11 HW purple balls
Gouache 1.00 + turpentine 35 % · 240 px · 139.4 s

![Refs v3 · #11 HW purple balls](Refs-v3-11-HW-purple-balls.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 69 % → 67 % | 201.0 px | 0.32 | 0.97 | 1343 |
| heavy line | 71 % → 63 % | 206.6 px | 0.32 | 0.89 | 1453 |
| pressure swell | 61 % → 70 % | 230.2 px | 0.29 | 1.14 | 1181 |
| fast wave | 98 % → 83 % | 113.5 px | 0.26 | 0.85 | 5107 |
| slow wave | 99 % → 65 % | 114.5 px | 0.28 | 0.65 | 8198 |
| spiral | 100 % → 66 % | 65.8 px | 0.27 | 0.66 | 9457 |
| loop | 99 % → 78 % | 128.4 px | 0.29 | 0.78 | 4018 |
| tilted | 53 % → 53 % | 148.0 px | 0.28 | 1.00 | 4515 |
| over the wet one | 90 % → 83 % | 103.1 px | 0.28 | 0.92 | 2281 |
| long, no reload | 100 % → 68 % | 44.8 px | 0.27 | 0.68 | 14657 | quarters: 0.00 → 0.00 → 0.00 → 0.00

Numbers say: light vs heavy: width 201.0 → 206.6 px, dark 0.32 → 0.32; pressure barely changes the width.

## Refs v3 · #12 HW black-olive cage
Gouache 1.00 + turpentine 35 % · 240 px · 141.4 s

![Refs v3 · #12 HW black-olive cage](Refs-v3-12-HW-black-olive-cage.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 69 % → 67 % | 201.0 px | 0.33 | 0.97 | 1300 |
| heavy line | 71 % → 63 % | 206.5 px | 0.33 | 0.89 | 1570 |
| pressure swell | 61 % → 70 % | 230.0 px | 0.31 | 1.14 | 1084 |
| fast wave | 98 % → 82 % | 113.5 px | 0.28 | 0.84 | 4793 |
| slow wave | 99 % → 65 % | 114.5 px | 0.30 | 0.65 | 9775 |
| spiral | 100 % → 66 % | 65.7 px | 0.29 | 0.66 | 9325 |
| loop | 99 % → 78 % | 128.4 px | 0.30 | 0.78 | 5251 |
| tilted | 53 % → 53 % | 148.0 px | 0.30 | 1.00 | 2846 |
| over the wet one | 90 % → 83 % | 103.1 px | 0.30 | 0.92 | 2315 |
| long, no reload | 100 % → 68 % | 44.8 px | 0.28 | 0.68 | 15665 | quarters: 0.00 → 0.00 → 0.00 → 0.00

Numbers say: light vs heavy: width 201.0 → 206.5 px, dark 0.33 → 0.33; pressure barely changes the width.

## Refs v3 · #13 HW blue streaky form
Gouache 1.00 + turpentine 35 % · 240 px · 154.6 s

![Refs v3 · #13 HW blue streaky form](Refs-v3-13-HW-blue-streaky-form.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 69 % → 67 % | 201.0 px | 0.34 | 0.97 | 2016 |
| heavy line | 71 % → 63 % | 206.6 px | 0.34 | 0.89 | 3130 |
| pressure swell | 61 % → 70 % | 230.2 px | 0.31 | 1.14 | 1725 |
| fast wave | 98 % → 83 % | 113.5 px | 0.29 | 0.85 | 9412 |
| slow wave | 99 % → 65 % | 114.5 px | 0.31 | 0.65 | 17650 |
| spiral | 100 % → 66 % | 65.8 px | 0.30 | 0.66 | 11196 |
| loop | 99 % → 78 % | 128.4 px | 0.31 | 0.78 | 5135 |
| tilted | 53 % → 53 % | 148.0 px | 0.30 | 1.00 | 2868 |
| over the wet one | 90 % → 83 % | 103.1 px | 0.30 | 0.92 | 2210 |
| long, no reload | 100 % → 68 % | 44.8 px | 0.29 | 0.68 | 13963 | quarters: 0.00 → 0.00 → 0.00 → 0.00

Numbers say: light vs heavy: width 201.0 → 206.6 px, dark 0.34 → 0.34; pressure barely changes the width.

## Refs v3 · #14 HW olive totem
Gouache 1.00 + turpentine 35 % · 240 px · 154.9 s

![Refs v3 · #14 HW olive totem](Refs-v3-14-HW-olive-totem.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 69 % → 67 % | 201.0 px | 0.33 | 0.97 | 2070 |
| heavy line | 71 % → 63 % | 206.6 px | 0.34 | 0.89 | 2961 |
| pressure swell | 61 % → 70 % | 230.2 px | 0.31 | 1.14 | 2544 |
| fast wave | 98 % → 83 % | 113.5 px | 0.28 | 0.85 | 8362 |
| slow wave | 99 % → 65 % | 114.5 px | 0.30 | 0.65 | 16270 |
| spiral | 100 % → 66 % | 65.8 px | 0.29 | 0.66 | 11313 |
| loop | 99 % → 78 % | 128.4 px | 0.31 | 0.78 | 4794 |
| tilted | 53 % → 53 % | 148.0 px | 0.30 | 1.00 | 2895 |
| over the wet one | 90 % → 83 % | 103.1 px | 0.30 | 0.92 | 2117 |
| long, no reload | 100 % → 68 % | 44.8 px | 0.29 | 0.68 | 15000 | quarters: 0.00 → 0.00 → 0.00 → 0.00

Numbers say: light vs heavy: width 201.0 → 206.6 px, dark 0.33 → 0.34; pressure barely changes the width.

## Refs v3 · #15 Ultramarine script
Ink 0.98 · 9 px · 40.5 s

![Refs v3 · #15 Ultramarine script](Refs-v3-15-Ultramarine-script.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 1 % → 5 % | 4.1 px | 0.64 | 3.87 | 111 |
| heavy line | 5 % → 8 % | 15.6 px | 0.69 | 1.50 | 180 |
| pressure swell | 3 % → 6 % | 11.1 px | 0.68 | 1.93 | 109 |
| fast wave | 9 % → 15 % | 10.4 px | 0.71 | 1.65 | 491 |
| slow wave | 8 % → 14 % | 8.8 px | 0.69 | 1.79 | 394 |
| spiral | 11 % → 18 % | 7.5 px | 0.69 | 1.57 | 510 |
| loop | 7 % → 12 % | 9.4 px | 0.69 | 1.71 | 268 |
| tilted | 5 % → 5 % | 13.7 px | 0.71 | 1.09 | 118 |
| over the wet one | 9 % → 14 % | 12.1 px | 0.71 | 1.49 | 122 |
| long, no reload | 18 % → 24 % | 7.9 px | 0.72 | 1.36 | 838 | quarters: 0.30 → 0.20 → 0.15 → 0.13

Numbers say: light vs heavy: width 4.1 → 15.6 px, dark 0.64 → 0.69; wet paint spreads well beyond the stroke.

## Refs v3 · #16 Shrigley strokes
Watercolour 1.00 + water 30 % · 48 px · 35.5 s

![Refs v3 · #16 Shrigley strokes](Refs-v3-16-Shrigley-strokes.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 7 % → 14 % | 18.9 px | 0.41 | 2.20 | 72 |
| heavy line | 13 % → 19 % | 38.6 px | 0.43 | 1.42 | 176 |
| pressure swell | 8 % → 13 % | 30.6 px | 0.48 | 1.60 | 158 |
| fast wave | 29 % → 36 % | 33.7 px | 0.46 | 1.24 | 542 |
| slow wave | 27 % → 35 % | 31.5 px | 0.40 | 1.28 | 596 |
| spiral | 44 % → 51 % | 28.9 px | 0.32 | 1.16 | 598 |
| loop | 23 % → 30 % | 29.6 px | 0.41 | 1.31 | 319 |
| tilted | 15 % → 15 % | 43.0 px | 0.43 | 1.00 | 200 |
| over the wet one | 26 % → 31 % | 28.2 px | 0.43 | 1.20 | 185 |
| long, no reload | 58 % → 64 % | 26.2 px | 0.31 | 1.09 | 921 | quarters: 0.35 → 0.22 → 0.16 → 0.11

Numbers say: light vs heavy: width 18.9 → 38.6 px, dark 0.41 → 0.43; wet paint spreads well beyond the stroke.

## Refs v3 · #17 Krovostok dry brush
Ink 0.93 · Gouache 0.07 · 48 px · 63.1 s

![Refs v3 · #17 Krovostok dry brush](Refs-v3-17-Krovostok-dry-brush.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 15 % → 16 % | 44.9 px | 0.87 | 1.06 | 163 |
| heavy line | 26 % → 26 % | 75.8 px | 0.88 | 1.00 | 322 |
| pressure swell | 17 % → 18 % | 63.4 px | 0.87 | 1.04 | 251 |
| fast wave | 47 % → 48 % | 54.4 px | 0.86 | 1.02 | 932 |
| slow wave | 47 % → 47 % | 54.3 px | 0.87 | 1.01 | 1033 |
| spiral | 61 % → 62 % | 40.5 px | 0.87 | 1.01 | 1087 |
| loop | 40 % → 41 % | 51.6 px | 0.87 | 1.03 | 517 |
| tilted | 14 % → 14 % | 39.8 px | 0.85 | 0.99 | 288 |
| over the wet one | 35 % → 37 % | 58.2 px | 0.85 | 1.04 | 251 |
| long, no reload | 77 % → 78 % | 34.5 px | 0.86 | 1.02 | 3102 | quarters: 0.82 → 0.79 → 0.70 → 0.57

Numbers say: light vs heavy: width 44.9 → 75.8 px, dark 0.87 → 0.88.

## Refs v3 · #18 Twombly blue sticks
Wax 1.00 · 9 px · 10.8 s

![Refs v3 · #18 Twombly blue sticks](Refs-v3-18-Twombly-blue-sticks.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 3 % → 3 % | 7.6 px | 0.58 | 1.00 | 38 |
| heavy line | 4 % → 4 % | 10.2 px | 0.58 | 1.00 | 39 |
| pressure swell | 2 % → 2 % | 8.7 px | 0.56 | 1.00 | 23 |
| fast wave | 8 % → 8 % | 9.7 px | 0.58 | 1.00 | 77 |
| slow wave | 8 % → 8 % | 9.7 px | 0.58 | 1.00 | 76 |
| spiral | 13 % → 13 % | 8.8 px | 0.58 | 1.00 | 131 |
| loop | 7 % → 7 % | 8.7 px | 0.58 | 1.00 | 64 |
| tilted | 3 % → 3 % | 9.4 px | 0.58 | 1.00 | 35 |
| over the wet one | 7 % → 7 % | 9.1 px | 0.58 | 1.00 | 58 |
| long, no reload | 17 % → 17 % | 7.8 px | 0.58 | 1.00 | 320 | quarters: 0.11 → 0.11 → 0.11 → 0.11

Numbers say: light vs heavy: width 7.6 → 10.2 px, dark 0.58 → 0.58; the long stroke does not run out of paint.

## Refs v3 · #19 Guston charcoal hand
Charcoal 1.00 · 14 px · 10.8 s

![Refs v3 · #19 Guston charcoal hand](Refs-v3-19-Guston-charcoal-hand.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 3 % → 3 % | 8.8 px | 0.84 | 1.00 | 32 |
| heavy line | 4 % → 4 % | 12.8 px | 0.84 | 1.00 | 31 |
| pressure swell | 3 % → 3 % | 12.2 px | 0.82 | 1.00 | 17 |
| fast wave | 11 % → 11 % | 12.5 px | 0.84 | 1.00 | 115 |
| slow wave | 10 % → 10 % | 12.1 px | 0.84 | 1.00 | 136 |
| spiral | 16 % → 16 % | 10.5 px | 0.84 | 1.00 | 138 |
| loop | 9 % → 9 % | 11.2 px | 0.84 | 1.00 | 81 |
| tilted | 5 % → 5 % | 12.7 px | 0.84 | 1.00 | 57 |
| over the wet one | 9 % → 9 % | 11.7 px | 0.84 | 1.00 | 31 |
| long, no reload | 18 % → 18 % | 7.9 px | 0.84 | 1.00 | 199 | quarters: 0.17 → 0.17 → 0.17 → 0.17

Numbers say: light vs heavy: width 8.8 → 12.8 px, dark 0.84 → 0.84; the long stroke does not run out of paint.

## Refs v3 · #20 Orange crayon
Wax 1.00 · 17 px · 10.8 s

![Refs v3 · #20 Orange crayon](Refs-v3-20-Orange-crayon.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 4 % → 4 % | 11.0 px | 0.54 | 1.00 | 60 |
| heavy line | 5 % → 5 % | 15.6 px | 0.54 | 1.00 | 38 |
| pressure swell | 4 % → 4 % | 14.2 px | 0.54 | 1.00 | 26 |
| fast wave | 13 % → 13 % | 15.1 px | 0.54 | 1.00 | 90 |
| slow wave | 12 % → 12 % | 14.4 px | 0.54 | 1.00 | 150 |
| spiral | 20 % → 20 % | 13.1 px | 0.54 | 1.00 | 146 |
| loop | 10 % → 10 % | 12.7 px | 0.54 | 1.00 | 80 |
| tilted | 4 % → 4 % | 11.9 px | 0.54 | 1.00 | 55 |
| over the wet one | 9 % → 9 % | 14.1 px | 0.54 | 1.00 | 36 |
| long, no reload | 25 % → 25 % | 11.4 px | 0.54 | 1.00 | 226 | quarters: 0.16 → 0.16 → 0.16 → 0.16

Numbers say: light vs heavy: width 11.0 → 15.6 px, dark 0.54 → 0.54; the long stroke does not run out of paint.

## Refs v3 · #21 Gritty dog contours
Gouache 1.00 + water 15 % · 96 px · 57.7 s

![Refs v3 · #21 Gritty dog contours](Refs-v3-21-Gritty-dog-contours.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 29 % → 28 % | 83.7 px | 0.30 | 0.98 | 346 |
| heavy line | 30 % → 29 % | 87.6 px | 0.31 | 0.95 | 455 |
| pressure swell | 23 % → 24 % | 86.9 px | 0.30 | 1.02 | 320 |
| fast wave | 59 % → 51 % | 68.6 px | 0.32 | 0.86 | 1385 |
| slow wave | 62 % → 47 % | 71.1 px | 0.30 | 0.77 | 1849 |
| spiral | 69 % → 43 % | 45.6 px | 0.29 | 0.62 | 1937 |
| loop | 56 % → 50 % | 72.6 px | 0.29 | 0.89 | 1611 |
| tilted | 23 % → 23 % | 64.5 px | 0.32 | 1.01 | 747 |
| over the wet one | 49 % → 47 % | 71.1 px | 0.32 | 0.96 | 460 |
| long, no reload | 83 % → 57 % | 37.1 px | 0.26 | 0.69 | 2637 | quarters: 0.26 → 0.25 → 0.22 → 0.16

Numbers say: light vs heavy: width 83.7 → 87.6 px, dark 0.30 → 0.31; pressure barely changes the width.

## Refs v3 · #22 Wasilewski brush poster
Ink 0.98 · 24 px · 32.7 s

![Refs v3 · #22 Wasilewski brush poster](Refs-v3-22-Wasilewski-brush-poster.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 8 % → 10 % | 22.8 px | 0.86 | 1.32 | 70 |
| heavy line | 9 % → 11 % | 26.4 px | 0.87 | 1.23 | 128 |
| pressure swell | 7 % → 9 % | 24.7 px | 0.86 | 1.30 | 72 |
| fast wave | 21 % → 25 % | 24.2 px | 0.83 | 1.18 | 232 |
| slow wave | 20 % → 25 % | 23.6 px | 0.85 | 1.23 | 509 |
| spiral | 32 % → 40 % | 21.4 px | 0.87 | 1.24 | 398 |
| loop | 18 % → 22 % | 23.7 px | 0.86 | 1.19 | 214 |
| tilted | 9 % → 10 % | 26.3 px | 0.86 | 1.02 | 112 |
| over the wet one | 18 % → 21 % | 24.3 px | 0.86 | 1.18 | 97 |
| long, no reload | 37 % → 45 % | 16.4 px | 0.86 | 1.22 | 563 | quarters: 0.54 → 0.46 → 0.37 → 0.33

Numbers say: light vs heavy: width 22.8 → 26.4 px, dark 0.86 → 0.87.

## Refs v3 · #23 Report dry white mask
Ink 0.93 · Gouache 0.07 · 64 px · 50.5 s

![Refs v3 · #23 Report dry white mask](Refs-v3-23-Report-dry-white-mask.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 15 % → 17 % | 44.5 px | 0.38 | 1.10 | 167 |
| heavy line | 22 % → 22 % | 63.0 px | 0.39 | 1.02 | 373 |
| pressure swell | 15 % → 17 % | 57.8 px | 0.38 | 1.09 | 310 |
| fast wave | 49 % → 48 % | 56.4 px | 0.33 | 0.99 | 870 |
| slow wave | 47 % → 49 % | 54.6 px | 0.38 | 1.03 | 1254 |
| spiral | 67 % → 62 % | 44.1 px | 0.33 | 0.93 | 1005 |
| loop | 43 % → 44 % | 55.3 px | 0.40 | 1.03 | 489 |
| tilted | 17 % → 17 % | 47.3 px | 0.36 | 0.99 | 303 |
| over the wet one | 35 % → 37 % | 51.4 px | 0.36 | 1.04 | 246 |
| long, no reload | 79 % → 77 % | 35.4 px | 0.33 | 0.98 | 1543 | quarters: 0.00 → 0.00 → 0.00 → 0.00

Numbers say: light vs heavy: width 44.5 → 63.0 px, dark 0.38 → 0.39.

## Refs v3 · #24 Picasso flat oil
Gouache 1.00 + turpentine 30 % · 240 px · 116.3 s

![Refs v3 · #24 Picasso flat oil](Refs-v3-24-Picasso-flat-oil.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 69 % → 67 % | 201.1 px | 0.25 | 0.97 | 1394 |
| heavy line | 71 % → 63 % | 206.4 px | 0.26 | 0.89 | 1559 |
| pressure swell | 61 % → 70 % | 229.7 px | 0.28 | 1.14 | 1253 |
| fast wave | 98 % → 83 % | 113.5 px | 0.31 | 0.84 | 5251 |
| slow wave | 99 % → 65 % | 114.5 px | 0.29 | 0.66 | 9014 |
| spiral | 100 % → 68 % | 65.8 px | 0.31 | 0.68 | 8896 |
| loop | 99 % → 80 % | 128.4 px | 0.28 | 0.80 | 3876 |
| tilted | 53 % → 53 % | 148.2 px | 0.30 | 1.00 | 2977 |
| over the wet one | 90 % → 83 % | 103.0 px | 0.30 | 0.93 | 1984 |
| long, no reload | 100 % → 69 % | 44.8 px | 0.30 | 0.69 | 13376 | quarters: 0.30 → 0.31 → 0.30 → 0.26

Numbers say: light vs heavy: width 201.1 → 206.4 px, dark 0.25 → 0.26; pressure barely changes the width; the long stroke does not run out of paint.

## Refs v3 · #25 Yellow heavy stroke
Impasto 1.00 · 160 px · 43.2 s

![Refs v3 · #25 Yellow heavy stroke](Refs-v3-25-Yellow-heavy-stroke.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 46 % → 43 % | 133.4 px | 0.26 | 0.93 | 676 |
| heavy line | 46 % → 30 % | 134.8 px | 0.25 | 0.65 | 732 |
| pressure swell | 36 % → 35 % | 136.4 px | 0.24 | 0.97 | 540 |
| fast wave | 84 % → 39 % | 97.6 px | 0.21 | 0.46 | 2222 |
| slow wave | 85 % → 33 % | 98.4 px | 0.23 | 0.39 | 4020 |
| spiral | 89 % → 32 % | 58.7 px | 0.21 | 0.36 | 3408 |
| loop | 78 % → 39 % | 100.7 px | 0.24 | 0.50 | 1796 |
| tilted | 34 % → 34 % | 95.5 px | 0.23 | 1.00 | 1231 |
| over the wet one | 69 % → 55 % | 97.7 px | 0.23 | 0.79 | 886 |
| long, no reload | 95 % → 41 % | 42.4 px | 0.23 | 0.44 | 6168 | quarters: 0.00 → 0.00 → 0.00 → 0.02

Numbers say: light vs heavy: width 133.4 → 134.8 px, dark 0.26 → 0.25; pressure barely changes the width; the long stroke does not run out of paint.

## Refs v3 · #26 Ink caricature
Ink 0.98 · 20 px · 27.2 s

![Refs v3 · #26 Ink caricature](Refs-v3-26-Ink-caricature.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 2 % → 6 % | 5.8 px | 0.83 | 3.06 | 54 |
| heavy line | 9 % → 11 % | 25.5 px | 0.87 | 1.24 | 104 |
| pressure swell | 5 % → 7 % | 17.4 px | 0.85 | 1.50 | 64 |
| fast wave | 16 % → 21 % | 18.1 px | 0.86 | 1.34 | 202 |
| slow wave | 13 % → 19 % | 15.5 px | 0.86 | 1.45 | 237 |
| spiral | 22 % → 29 % | 14.6 px | 0.82 | 1.32 | 306 |
| loop | 13 % → 17 % | 16.4 px | 0.87 | 1.37 | 182 |
| tilted | 8 % → 8 % | 22.7 px | 0.85 | 1.03 | 82 |
| over the wet one | 14 % → 18 % | 17.2 px | 0.85 | 1.23 | 76 |
| long, no reload | 32 % → 39 % | 14.5 px | 0.85 | 1.20 | 468 | quarters: 0.47 → 0.39 → 0.33 → 0.29

Numbers say: light vs heavy: width 5.8 → 25.5 px, dark 0.83 → 0.87; wet paint spreads well beyond the stroke.

## Refs v3 · #27 Orange impasto swatch
Impasto 1.00 · 64 px · 18.8 s

![Refs v3 · #27 Orange impasto swatch](Refs-v3-27-Orange-impasto-swatch.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 19 % → 14 % | 56.2 px | 0.31 | 0.73 | 223 |
| heavy line | 20 % → 12 % | 57.6 px | 0.30 | 0.61 | 347 |
| pressure swell | 15 % → 12 % | 56.0 px | 0.33 | 0.78 | 234 |
| fast wave | 44 % → 12 % | 51.3 px | 0.37 | 0.28 | 677 |
| slow wave | 44 % → 13 % | 50.8 px | 0.31 | 0.31 | 1038 |
| spiral | 55 % → 16 % | 36.1 px | 0.34 | 0.29 | 1078 |
| loop | 40 % → 18 % | 51.8 px | 0.32 | 0.44 | 638 |
| tilted | 16 % → 16 % | 43.6 px | 0.35 | 1.00 | 371 |
| over the wet one | 34 % → 25 % | 50.0 px | 0.35 | 0.75 | 284 |
| long, no reload | 64 % → 16 % | 28.6 px | 0.34 | 0.25 | 1379 | quarters: 0.28 → 0.09 → 0.03 → 0.01

Numbers say: light vs heavy: width 56.2 → 57.6 px, dark 0.31 → 0.30; pressure barely changes the width.

## Refs v3 · #28 Miles Davis lines
Ink 0.93 · Gouache 0.07 · 24 px · 35.3 s

![Refs v3 · #28 Miles Davis lines](Refs-v3-28-Miles-Davis-lines.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 4 % → 8 % | 10.7 px | 0.84 | 2.30 | 57 |
| heavy line | 9 % → 12 % | 26.6 px | 0.86 | 1.31 | 129 |
| pressure swell | 5 % → 8 % | 20.4 px | 0.85 | 1.48 | 70 |
| fast wave | 18 % → 24 % | 21.3 px | 0.82 | 1.30 | 184 |
| slow wave | 17 % → 23 % | 20.1 px | 0.86 | 1.34 | 279 |
| spiral | 27 % → 34 % | 17.6 px | 0.84 | 1.26 | 299 |
| loop | 15 % → 20 % | 18.9 px | 0.85 | 1.36 | 153 |
| tilted | 9 % → 10 % | 25.9 px | 0.84 | 1.02 | 103 |
| over the wet one | 16 % → 21 % | 19.8 px | 0.84 | 1.29 | 79 |
| long, no reload | 38 % → 44 % | 17.2 px | 0.84 | 1.16 | 505 | quarters: 0.51 → 0.44 → 0.37 → 0.33

Numbers say: light vs heavy: width 10.7 → 26.6 px, dark 0.84 → 0.86; wet paint spreads well beyond the stroke.

## Refs v3 · #29 Shrigley asterisk
Watercolour 1.00 + water 50 % · 72 px · 53.5 s

![Refs v3 · #29 Shrigley asterisk](Refs-v3-29-Shrigley-asterisk.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 20 % → 24 % | 58.5 px | 0.60 | 1.20 | 159 |
| heavy line | 40 % → 40 % | 115.1 px | 0.62 | 1.00 | 330 |
| pressure swell | 24 % → 26 % | 90.8 px | 0.61 | 1.08 | 270 |
| fast wave | 69 % → 73 % | 79.4 px | 0.61 | 1.06 | 779 |
| slow wave | 65 % → 65 % | 75.0 px | 0.62 | 1.01 | 1252 |
| spiral | 76 % → 76 % | 50.1 px | 0.58 | 1.01 | 1662 |
| loop | 58 % → 58 % | 75.1 px | 0.60 | 1.01 | 696 |
| tilted | 24 % → 24 % | 68.2 px | 0.59 | 1.00 | 384 |
| over the wet one | 53 % → 57 % | 80.5 px | 0.59 | 1.07 | 329 |
| long, no reload | 93 % → 94 % | 41.6 px | 0.55 | 1.01 | 1952 | quarters: 0.56 → 0.55 → 0.53 → 0.46

Numbers say: light vs heavy: width 58.5 → 115.1 px, dark 0.60 → 0.62.

## Refs v3 · #30 Red gouache face
Gouache 1.00 + water 15 % · 80 px · 63.2 s

![Refs v3 · #30 Red gouache face](Refs-v3-30-Red-gouache-face.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 24 % → 23 % | 69.6 px | 0.51 | 0.98 | 252 |
| heavy line | 25 % → 24 % | 72.7 px | 0.51 | 0.94 | 460 |
| pressure swell | 19 % → 19 % | 72.0 px | 0.51 | 0.99 | 245 |
| fast wave | 51 % → 40 % | 58.7 px | 0.55 | 0.79 | 832 |
| slow wave | 54 % → 41 % | 62.2 px | 0.52 | 0.77 | 1399 |
| spiral | 62 % → 41 % | 40.9 px | 0.53 | 0.67 | 1772 |
| loop | 48 % → 42 % | 62.2 px | 0.52 | 0.88 | 1268 |
| tilted | 19 % → 20 % | 54.0 px | 0.51 | 1.01 | 744 |
| over the wet one | 42 % → 40 % | 62.3 px | 0.51 | 0.95 | 429 |
| long, no reload | 76 % → 48 % | 33.9 px | 0.54 | 0.64 | 4005 | quarters: 0.51 → 0.48 → 0.41 → 0.32

Numbers say: light vs heavy: width 69.6 → 72.7 px, dark 0.51 → 0.51; pressure barely changes the width.

## Refs v3 · #31 Warhol blotted line
Ink 0.98 · 6 px · 29.5 s

![Refs v3 · #31 Warhol blotted line](Refs-v3-31-Warhol-blotted-line.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 1 % → 5 % | 3.4 px | 0.80 | 3.98 | 71 |
| heavy line | 4 % → 6 % | 11.8 px | 0.83 | 1.47 | 122 |
| pressure swell | 2 % → 5 % | 8.4 px | 0.81 | 2.22 | 72 |
| fast wave | 7 % → 12 % | 7.8 px | 0.81 | 1.71 | 167 |
| slow wave | 6 % → 11 % | 6.8 px | 0.83 | 1.85 | 238 |
| spiral | 9 % → 13 % | 5.8 px | 0.83 | 1.46 | 560 |
| loop | 6 % → 10 % | 7.1 px | 0.80 | 1.78 | 306 |
| tilted | 4 % → 5 % | 11.6 px | 0.82 | 1.08 | 185 |
| over the wet one | 7 % → 12 % | 9.2 px | 0.82 | 1.60 | 78 |
| long, no reload | 14 % → 18 % | 6.1 px | 0.84 | 1.30 | 479 | quarters: 0.28 → 0.17 → 0.13 → 0.11

Numbers say: light vs heavy: width 3.4 → 11.8 px, dark 0.80 → 0.83; wet paint spreads well beyond the stroke.

## Refs v3 · #32 Thick orange swipes
Gouache 0.85 · Ink 0.15 + turpentine 50 % · 240 px · 159.1 s

![Refs v3 · #32 Thick orange swipes](Refs-v3-32-Thick-orange-swipes.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 71 % → 71 % | 206.0 px | 0.19 | 1.00 | 2107 |
| heavy line | 72 % → 65 % | 209.0 px | 0.19 | 0.91 | 1930 |
| pressure swell | 64 % → 72 % | 240.3 px | 0.22 | 1.12 | 1206 |
| fast wave | 98 % → 89 % | 113.7 px | 0.25 | 0.90 | 5774 |
| slow wave | 99 % → 68 % | 114.3 px | 0.21 | 0.69 | 9652 |
| spiral | 100 % → 74 % | 65.9 px | 0.23 | 0.74 | 11253 |
| loop | 100 % → 87 % | 128.9 px | 0.19 | 0.87 | 5336 |
| tilted | 54 % → 54 % | 149.4 px | 0.23 | 1.00 | 3590 |
| over the wet one | 90 % → 84 % | 102.9 px | 0.23 | 0.93 | 2327 |
| long, no reload | 100 % → 76 % | 44.8 px | 0.22 | 0.76 | 17163 | quarters: 0.24 → 0.23 → 0.19 → 0.10

Numbers say: light vs heavy: width 206.0 → 209.0 px, dark 0.19 → 0.19; pressure barely changes the width.

## Refs v3 · #33 Red wet-in-wet flames
Watercolour 1.00 + water 60 % · 96 px · 77.5 s

![Refs v3 · #33 Red wet-in-wet flames](Refs-v3-33-Red-wet-in-wet-flames.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 30 % → 53 % | 87.2 px | 0.47 | 1.78 | 254 |
| heavy line | 49 % → 59 % | 141.8 px | 0.53 | 1.21 | 390 |
| pressure swell | 30 % → 48 % | 110.9 px | 0.49 | 1.62 | 309 |
| fast wave | 75 % → 87 % | 87.1 px | 0.61 | 1.16 | 1142 |
| slow wave | 78 % → 87 % | 89.8 px | 0.58 | 1.12 | 2162 |
| spiral | 88 % → 98 % | 58.1 px | 0.57 | 1.11 | 2103 |
| loop | 68 % → 83 % | 88.7 px | 0.57 | 1.21 | 921 |
| tilted | 40 % → 42 % | 112.1 px | 0.55 | 1.05 | 781 |
| over the wet one | 72 % → 92 % | 87.8 px | 0.55 | 1.28 | 442 |
| long, no reload | 96 % → 100 % | 42.9 px | 0.61 | 1.04 | 4274 | quarters: 0.67 → 0.65 → 0.63 → 0.53

Numbers say: light vs heavy: width 87.2 → 141.8 px, dark 0.47 → 0.53; wet paint spreads well beyond the stroke.

## Refs v3 · #34 Magenta oil patches
Gouache 1.00 + turpentine 15 % · 96 px · 68.6 s

![Refs v3 · #34 Magenta oil patches](Refs-v3-34-Magenta-oil-patches.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 29 % → 28 % | 83.6 px | 0.42 | 0.98 | 827 |
| heavy line | 30 % → 28 % | 87.3 px | 0.42 | 0.93 | 739 |
| pressure swell | 23 % → 23 % | 86.2 px | 0.44 | 1.00 | 354 |
| fast wave | 65 % → 36 % | 74.6 px | 0.46 | 0.55 | 1380 |
| slow wave | 64 % → 36 % | 73.8 px | 0.44 | 0.56 | 2282 |
| spiral | 77 % → 36 % | 50.7 px | 0.45 | 0.47 | 2937 |
| loop | 58 % → 40 % | 74.6 px | 0.43 | 0.70 | 1250 |
| tilted | 23 % → 23 % | 65.1 px | 0.44 | 1.00 | 807 |
| over the wet one | 48 % → 45 % | 69.9 px | 0.44 | 0.92 | 582 |
| long, no reload | 95 % → 37 % | 42.4 px | 0.45 | 0.40 | 4957 | quarters: 0.44 → 0.42 → 0.37 → 0.33

Numbers say: light vs heavy: width 83.6 → 87.3 px, dark 0.42 → 0.42; pressure barely changes the width.

## Refs v3 · #35 Red band with runs
Watercolour 1.00 + water 75 % · 88 px · 87.0 s

![Refs v3 · #35 Red band with runs](Refs-v3-35-Red-band-with-runs.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 40 % → 57 % | 117.2 px | 0.24 | 1.41 | 462 |
| heavy line | 59 % → 64 % | 170.6 px | 0.35 | 1.10 | 653 |
| pressure swell | 26 % → 40 % | 97.3 px | 0.32 | 1.54 | 514 |
| fast wave | 70 % → 82 % | 81.0 px | 0.43 | 1.17 | 1777 |
| slow wave | 72 % → 81 % | 83.4 px | 0.44 | 1.12 | 1910 |
| spiral | 94 % → 99 % | 62.2 px | 0.19 | 1.05 | 2532 |
| loop | 83 % → 92 % | 106.9 px | 0.39 | 1.12 | 1180 |
| tilted | 45 % → 46 % | 125.8 px | 0.35 | 1.02 | 679 |
| over the wet one | 72 % → 88 % | 75.0 px | 0.35 | 1.23 | 586 |
| long, no reload | 95 % → 100 % | 42.4 px | 0.28 | 1.06 | 3132 | quarters: 0.41 → 0.34 → 0.25 → 0.13

Numbers say: light vs heavy: width 117.2 → 170.6 px, dark 0.24 → 0.35; wet paint spreads well beyond the stroke.

## Refs v3 · #36 Magenta letters flat
Gouache 1.00 + water 15 % · 44 px · 51.1 s

![Refs v3 · #36 Magenta letters flat](Refs-v3-36-Magenta-letters-flat.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 13 % → 13 % | 39.0 px | 0.45 | 0.99 | 145 |
| heavy line | 14 % → 14 % | 40.9 px | 0.46 | 0.99 | 191 |
| pressure swell | 11 % → 11 % | 42.3 px | 0.48 | 1.00 | 149 |
| fast wave | 30 % → 23 % | 34.2 px | 0.51 | 0.79 | 662 |
| slow wave | 31 % → 25 % | 35.7 px | 0.48 | 0.80 | 969 |
| spiral | 47 % → 28 % | 31.2 px | 0.50 | 0.59 | 1344 |
| loop | 28 % → 25 % | 36.9 px | 0.48 | 0.89 | 647 |
| tilted | 11 % → 11 % | 31.3 px | 0.50 | 1.01 | 244 |
| over the wet one | 25 % → 24 % | 38.0 px | 0.50 | 0.95 | 229 |
| long, no reload | 50 % → 28 % | 22.2 px | 0.50 | 0.57 | 1182 | quarters: 0.38 → 0.31 → 0.24 → 0.19

Numbers say: light vs heavy: width 39.0 → 40.9 px, dark 0.45 → 0.46; pressure barely changes the width.

## Refs v3 · #37 Oil still life
Gouache 1.00 + turpentine 30 % · 240 px · 165.0 s

![Refs v3 · #37 Oil still life](Refs-v3-37-Oil-still-life.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 69 % → 67 % | 201.1 px | 0.32 | 0.97 | 2043 |
| heavy line | 71 % → 63 % | 206.4 px | 0.33 | 0.89 | 1919 |
| pressure swell | 61 % → 70 % | 229.7 px | 0.34 | 1.14 | 1912 |
| fast wave | 98 % → 83 % | 113.5 px | 0.37 | 0.84 | 6403 |
| slow wave | 99 % → 65 % | 114.5 px | 0.35 | 0.66 | 11198 |
| spiral | 100 % → 68 % | 65.8 px | 0.37 | 0.68 | 12773 |
| loop | 99 % → 80 % | 128.4 px | 0.35 | 0.80 | 7460 |
| tilted | 53 % → 53 % | 148.2 px | 0.36 | 1.00 | 3531 |
| over the wet one | 90 % → 83 % | 103.0 px | 0.36 | 0.93 | 2458 |
| long, no reload | 100 % → 69 % | 44.8 px | 0.37 | 0.69 | 18183 | quarters: 0.36 → 0.37 → 0.37 → 0.36

Numbers say: light vs heavy: width 201.1 → 206.4 px, dark 0.32 → 0.33; pressure barely changes the width; the long stroke does not run out of paint.

## Refs v3 · #38 Sanguine drawing
Charcoal 0.50 · Pastel 0.50 · 4 px · 12.9 s

![Refs v3 · #38 Sanguine drawing](Refs-v3-38-Sanguine-drawing.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 2 % → 2 % | 5.8 px | 0.65 | 1.00 | 86 |
| heavy line | 2 % → 2 % | 6.8 px | 0.65 | 1.00 | 53 |
| pressure swell | 2 % → 2 % | 5.7 px | 0.63 | 1.00 | 37 |
| fast wave | 6 % → 6 % | 6.5 px | 0.65 | 1.00 | 124 |
| slow wave | 6 % → 6 % | 6.5 px | 0.65 | 1.00 | 101 |
| spiral | 9 % → 9 % | 6.1 px | 0.65 | 1.00 | 133 |
| loop | 5 % → 5 % | 6.1 px | 0.65 | 1.00 | 73 |
| tilted | 3 % → 3 % | 7.0 px | 0.65 | 1.00 | 38 |
| over the wet one | 5 % → 5 % | 6.3 px | 0.65 | 1.00 | 43 |
| long, no reload | 12 % → 12 % | 5.5 px | 0.65 | 1.00 | 197 | quarters: 0.09 → 0.09 → 0.09 → 0.09

Numbers say: light vs heavy: width 5.8 → 6.8 px, dark 0.65 → 0.65; the long stroke does not run out of paint.

## Refs v3 · #39 Thick impasto weave
Impasto 1.00 · 64 px · 24.5 s

![Refs v3 · #39 Thick impasto weave](Refs-v3-39-Thick-impasto-weave.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 19 % → 14 % | 56.2 px | 0.48 | 0.74 | 329 |
| heavy line | 20 % → 12 % | 57.6 px | 0.48 | 0.61 | 372 |
| pressure swell | 15 % → 12 % | 56.0 px | 0.49 | 0.78 | 253 |
| fast wave | 44 % → 12 % | 51.3 px | 0.51 | 0.28 | 773 |
| slow wave | 44 % → 14 % | 50.9 px | 0.49 | 0.31 | 1238 |
| spiral | 55 % → 16 % | 36.2 px | 0.49 | 0.29 | 1178 |
| loop | 40 % → 18 % | 51.9 px | 0.48 | 0.44 | 974 |
| tilted | 16 % → 16 % | 43.6 px | 0.50 | 1.00 | 604 |
| over the wet one | 34 % → 25 % | 50.0 px | 0.50 | 0.75 | 395 |
| long, no reload | 64 % → 16 % | 28.6 px | 0.49 | 0.25 | 1779 | quarters: 0.42 → 0.35 → 0.31 → 0.20

Numbers say: light vs heavy: width 56.2 → 57.6 px, dark 0.48 → 0.48; pressure barely changes the width.

## Refs v3 · #40 Watercolour blooms
Watercolour 1.00 + water 55 % · 96 px · 82.2 s

![Refs v3 · #40 Watercolour blooms](Refs-v3-40-Watercolour-blooms.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 21 % → 40 % | 62.2 px | 0.20 | 1.86 | 264 |
| heavy line | 40 % → 50 % | 117.1 px | 0.22 | 1.25 | 448 |
| pressure swell | 24 % → 39 % | 91.8 px | 0.24 | 1.58 | 367 |
| fast wave | 70 % → 88 % | 81.1 px | 0.26 | 1.25 | 1425 |
| slow wave | 68 % → 82 % | 79.0 px | 0.25 | 1.20 | 2401 |
| spiral | 81 % → 89 % | 53.6 px | 0.23 | 1.09 | 2476 |
| loop | 60 % → 71 % | 77.7 px | 0.26 | 1.18 | 1156 |
| tilted | 30 % → 31 % | 84.6 px | 0.23 | 1.04 | 732 |
| over the wet one | 60 % → 82 % | 82.2 px | 0.23 | 1.37 | 651 |
| long, no reload | 96 % → 99 % | 43.0 px | 0.24 | 1.04 | 5383 | quarters: 0.37 → 0.28 → 0.21 → 0.14

Numbers say: light vs heavy: width 62.2 → 117.1 px, dark 0.20 → 0.22; wet paint spreads well beyond the stroke.

## Refs v3 · #41 Coloured pencil
Charcoal 0.50 · Pastel 0.50 · 3 px · 15.1 s

![Refs v3 · #41 Coloured pencil](Refs-v3-41-Coloured-pencil.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 2 % → 2 % | 5.1 px | 0.44 | 1.00 | 62 |
| heavy line | 2 % → 2 % | 5.9 px | 0.44 | 1.00 | 35 |
| pressure swell | 1 % → 1 % | 4.7 px | 0.42 | 1.00 | 28 |
| fast wave | 5 % → 5 % | 5.6 px | 0.44 | 1.00 | 112 |
| slow wave | 5 % → 5 % | 5.6 px | 0.44 | 1.00 | 84 |
| spiral | 8 % → 8 % | 5.3 px | 0.44 | 1.00 | 238 |
| loop | 4 % → 4 % | 5.3 px | 0.44 | 1.00 | 106 |
| tilted | 2 % → 2 % | 6.2 px | 0.44 | 1.00 | 38 |
| over the wet one | 4 % → 4 % | 5.4 px | 0.44 | 1.00 | 35 |
| long, no reload | 11 % → 11 % | 4.8 px | 0.44 | 1.00 | 259 | quarters: 0.05 → 0.05 → 0.05 → 0.05

Numbers say: light vs heavy: width 5.1 → 5.9 px, dark 0.44 → 0.44; the long stroke does not run out of paint.

## Refs v3 · #42 Pink shaggy pastel
Gouache 1.00 + water 15 % · 80 px · 68.6 s

![Refs v3 · #42 Pink shaggy pastel](Refs-v3-42-Pink-shaggy-pastel.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 24 % → 24 % | 69.9 px | 0.69 | 0.98 | 546 |
| heavy line | 25 % → 24 % | 73.2 px | 0.69 | 0.96 | 359 |
| pressure swell | 19 % → 19 % | 72.7 px | 0.69 | 1.00 | 324 |
| fast wave | 53 % → 44 % | 61.3 px | 0.68 | 0.83 | 1362 |
| slow wave | 54 % → 41 % | 61.9 px | 0.68 | 0.77 | 1791 |
| spiral | 62 % → 38 % | 41.0 px | 0.65 | 0.62 | 1835 |
| loop | 49 % → 43 % | 63.1 px | 0.67 | 0.89 | 928 |
| tilted | 20 % → 20 % | 54.9 px | 0.70 | 1.01 | 573 |
| over the wet one | 42 % → 40 % | 62.0 px | 0.70 | 0.96 | 683 |
| long, no reload | 76 % → 49 % | 34.2 px | 0.66 | 0.65 | 2422 | quarters: 0.63 → 0.60 → 0.51 → 0.40

Numbers say: light vs heavy: width 69.9 → 73.2 px, dark 0.69 → 0.69; pressure barely changes the width.

## Refs v3 · #43 Dragged black blocks
Ink 0.93 · Gouache 0.07 · 128 px · 112.4 s

![Refs v3 · #43 Dragged black blocks](Refs-v3-43-Dragged-black-blocks.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 38 % → 42 % | 109.4 px | 0.87 | 1.12 | 477 |
| heavy line | 41 % → 42 % | 119.9 px | 0.87 | 1.01 | 1184 |
| pressure swell | 30 % → 35 % | 113.5 px | 0.86 | 1.16 | 767 |
| fast wave | 79 % → 85 % | 90.9 px | 0.86 | 1.08 | 2102 |
| slow wave | 77 % → 77 % | 88.9 px | 0.87 | 1.01 | 4286 |
| spiral | 87 % → 88 % | 57.5 px | 0.84 | 1.01 | 3567 |
| loop | 69 % → 70 % | 89.6 px | 0.86 | 1.01 | 1401 |
| tilted | 31 % → 31 % | 85.9 px | 0.85 | 1.00 | 1201 |
| over the wet one | 62 % → 64 % | 87.2 px | 0.85 | 1.04 | 1277 |
| long, no reload | 95 % → 96 % | 42.8 px | 0.87 | 1.01 | 5017 | quarters: 0.87 → 0.87 → 0.86 → 0.80

Numbers say: light vs heavy: width 109.4 → 119.9 px, dark 0.87 → 0.87; pressure barely changes the width; the long stroke does not run out of paint.

## Refs v3 · #44 Blue looping ribbon
Oil 0.84 · Gouache 0.16 + turpentine 10 % · 88 px · 76.2 s

![Refs v3 · #44 Blue looping ribbon](Refs-v3-44-Blue-looping-ribbon.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 27 % → 26 % | 78.3 px | 0.53 | 0.97 | 835 |
| heavy line | 28 % → 26 % | 81.2 px | 0.53 | 0.95 | 1329 |
| pressure swell | 21 % → 20 % | 77.2 px | 0.53 | 0.99 | 409 |
| fast wave | 61 % → 39 % | 70.9 px | 0.60 | 0.63 | 1408 |
| slow wave | 61 % → 42 % | 70.0 px | 0.58 | 0.70 | 2000 |
| spiral | 77 % → 40 % | 50.6 px | 0.64 | 0.53 | 2729 |
| loop | 55 % → 45 % | 71.2 px | 0.57 | 0.82 | 1157 |
| tilted | 22 % → 22 % | 61.8 px | 0.60 | 1.00 | 854 |
| over the wet one | 46 % → 42 % | 66.1 px | 0.60 | 0.92 | 605 |
| long, no reload | 93 % → 40 % | 41.8 px | 0.61 | 0.43 | 3789 | quarters: 0.58 → 0.60 → 0.56 → 0.39

Numbers say: light vs heavy: width 78.3 → 81.2 px, dark 0.53 → 0.53; pressure barely changes the width.

## Refs v3 · #45 Pastel pepper
Pastel 1.00 · 40 px · 17.6 s

![Refs v3 · #45 Pastel pepper](Refs-v3-45-Pastel-pepper.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 7 % → 7 % | 21.5 px | 0.54 | 1.00 | 206 |
| heavy line | 12 % → 12 % | 34.1 px | 0.54 | 1.00 | 160 |
| pressure swell | 8 % → 8 % | 31.2 px | 0.54 | 1.00 | 109 |
| fast wave | 27 % → 27 % | 30.7 px | 0.54 | 1.00 | 436 |
| slow wave | 25 % → 25 % | 28.9 px | 0.54 | 1.00 | 858 |
| spiral | 40 % → 40 % | 26.6 px | 0.54 | 1.00 | 726 |
| loop | 20 % → 20 % | 26.2 px | 0.54 | 1.00 | 352 |
| tilted | 6 % → 6 % | 17.8 px | 0.54 | 1.00 | 253 |
| over the wet one | 16 % → 16 % | 28.0 px | 0.54 | 1.00 | 197 |
| long, no reload | 48 % → 48 % | 21.5 px | 0.54 | 1.00 | 992 | quarters: 0.29 → 0.28 → 0.29 → 0.29

Numbers say: light vs heavy: width 21.5 → 34.1 px, dark 0.54 → 0.54; the long stroke does not run out of paint.

## Refs v3 · #46 Ink lips on wet paper
Watercolour 1.00 + water 65 % · 56 px · 71.1 s

![Refs v3 · #46 Ink lips on wet paper](Refs-v3-46-Ink-lips-on-wet-paper.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 12 % → 29 % | 34.6 px | 0.62 | 2.45 | 130 |
| heavy line | 24 % → 37 % | 69.7 px | 0.64 | 1.55 | 280 |
| pressure swell | 14 % → 27 % | 53.7 px | 0.64 | 1.87 | 179 |
| fast wave | 48 % → 71 % | 55.0 px | 0.65 | 1.50 | 884 |
| slow wave | 45 % → 66 % | 52.1 px | 0.66 | 1.47 | 1481 |
| spiral | 67 % → 78 % | 44.0 px | 0.67 | 1.17 | 2017 |
| loop | 41 % → 58 % | 52.6 px | 0.66 | 1.43 | 535 |
| tilted | 19 % → 20 % | 54.1 px | 0.62 | 1.05 | 397 |
| over the wet one | 39 % → 62 % | 54.5 px | 0.62 | 1.58 | 340 |
| long, no reload | 81 % → 96 % | 36.5 px | 0.67 | 1.18 | 2213 | quarters: 0.72 → 0.72 → 0.68 → 0.59

Numbers say: light vs heavy: width 34.6 → 69.7 px, dark 0.62 → 0.64; wet paint spreads well beyond the stroke.

## Refs v3 · #47 Pink knife slabs
Gouache 1.00 + water 15 % · 240 px · 157.3 s

![Refs v3 · #47 Pink knife slabs](Refs-v3-47-Pink-knife-slabs.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 65 % → 67 % | 189.7 px | 0.34 | 1.02 | 1517 |
| heavy line | 68 % → 64 % | 196.0 px | 0.34 | 0.94 | 3190 |
| pressure swell | 58 % → 67 % | 215.7 px | 0.31 | 1.16 | 1491 |
| fast wave | 94 % → 91 % | 108.4 px | 0.29 | 0.97 | 6078 |
| slow wave | 97 % → 85 % | 111.8 px | 0.33 | 0.88 | 9507 |
| spiral | 96 % → 82 % | 63.5 px | 0.32 | 0.85 | 9750 |
| loop | 98 % → 93 % | 126.4 px | 0.33 | 0.95 | 4833 |
| tilted | 49 % → 49 % | 136.5 px | 0.30 | 1.00 | 2793 |
| over the wet one | 85 % → 85 % | 100.9 px | 0.30 | 1.00 | 2551 |
| long, no reload | 99 % → 94 % | 44.2 px | 0.32 | 0.96 | 16411 | quarters: 0.00 → 0.00 → 0.00 → 0.00

Numbers say: light vs heavy: width 189.7 → 196.0 px, dark 0.34 → 0.34; pressure barely changes the width.

## Refs v3 · #48 Black bands with drips
Watercolour 1.00 + water 35 % · 96 px · 79.2 s

![Refs v3 · #48 Black bands with drips](Refs-v3-48-Black-bands-with-drips.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 38 % → 43 % | 111.7 px | 0.83 | 1.12 | 483 |
| heavy line | 44 % → 47 % | 128.8 px | 0.80 | 1.05 | 476 |
| pressure swell | 26 % → 33 % | 98.2 px | 0.81 | 1.27 | 328 |
| fast wave | 69 % → 75 % | 80.0 px | 0.83 | 1.09 | 1423 |
| slow wave | 71 % → 74 % | 81.8 px | 0.81 | 1.04 | 2578 |
| spiral | 81 % → 85 % | 53.5 px | 0.82 | 1.05 | 2305 |
| loop | 67 % → 72 % | 87.0 px | 0.85 | 1.07 | 1320 |
| tilted | 34 % → 36 % | 95.5 px | 0.83 | 1.04 | 711 |
| over the wet one | 64 % → 70 % | 83.8 px | 0.83 | 1.09 | 498 |
| long, no reload | 79 % → 88 % | 35.5 px | 0.79 | 1.11 | 3243 | quarters: 0.84 → 0.84 → 0.74 → 0.52

Numbers say: light vs heavy: width 111.7 → 128.8 px, dark 0.83 → 0.80.

## Refs v3 · #49 Magenta letters round
Ink 0.93 · Gouache 0.07 · 40 px · 63.1 s

![Refs v3 · #49 Magenta letters round](Refs-v3-49-Magenta-letters-round.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 5 % → 9 % | 14.0 px | 0.50 | 1.87 | 138 |
| heavy line | 14 % → 16 % | 40.3 px | 0.53 | 1.16 | 313 |
| pressure swell | 8 % → 10 % | 28.7 px | 0.55 | 1.30 | 158 |
| fast wave | 28 % → 32 % | 31.8 px | 0.56 | 1.17 | 437 |
| slow wave | 25 % → 30 % | 28.7 px | 0.53 | 1.21 | 550 |
| spiral | 41 % → 47 % | 26.8 px | 0.50 | 1.15 | 820 |
| loop | 22 % → 26 % | 27.9 px | 0.52 | 1.20 | 571 |
| tilted | 14 % → 14 % | 39.6 px | 0.54 | 1.00 | 276 |
| over the wet one | 24 % → 27 % | 27.2 px | 0.54 | 1.13 | 230 |
| long, no reload | 55 % → 60 % | 24.7 px | 0.50 | 1.09 | 1096 | quarters: 0.37 → 0.35 → 0.32 → 0.28

Numbers say: light vs heavy: width 14.0 → 40.3 px, dark 0.50 → 0.53; wet paint spreads well beyond the stroke.

## Refs v3 · #50 Swipes on seaside
Gouache 1.00 + water 15 % · 240 px · 153.0 s

![Refs v3 · #50 Swipes on seaside](Refs-v3-50-Swipes-on-seaside.png)

A light paint: laid on a grey sheet (on white it cannot be seen); **dark** = how far it is from the grey either way.

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| light line | 70 % → 71 % | 203.7 px | 0.29 | 1.01 | 1757 |
| heavy line | 72 % → 66 % | 210.1 px | 0.29 | 0.91 | 2816 |
| pressure swell | 63 % → 71 % | 236.5 px | 0.27 | 1.13 | 2044 |
| fast wave | 93 % → 93 % | 108.0 px | 0.25 | 0.99 | 6941 |
| slow wave | 97 % → 84 % | 111.7 px | 0.29 | 0.87 | 9880 |
| spiral | 96 % → 84 % | 63.1 px | 0.27 | 0.88 | 12511 |
| loop | 98 % → 93 % | 126.6 px | 0.29 | 0.96 | 5096 |
| tilted | 51 % → 52 % | 143.6 px | 0.26 | 1.00 | 3505 |
| over the wet one | 89 % → 87 % | 104.9 px | 0.26 | 0.97 | 2477 |
| long, no reload | 98 % → 95 % | 44.2 px | 0.29 | 0.96 | 15489 | quarters: 0.00 → 0.00 → 0.00 → 0.00

Numbers say: light vs heavy: width 203.7 → 210.1 px, dark 0.29 → 0.29; pressure barely changes the width.

## Refs v3 · #01 HW peach cloud — own sheet
own sheet 800 × 941 · Gouache 1.00 + turpentine 35 % · 240 px · 101.8 s

![Refs v3 · #01 HW peach cloud — own sheet](Refs-v3-01-HW-peach-cloud-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 26 % → 50 % | 129.2 px | 0.16 | 1.93 | 5299 |
| stroke 2 | 41 % → 45 % | 247.9 px | 0.16 | 1.10 | 6045 |
| stroke 3 | 52 % → 39 % | 389.8 px | 0.16 | 0.75 | 10208 |
| stroke 4 | 60 % → 60 % | 512.8 px | 0.18 | 1.00 | 7441 |
| stroke 5 | 74 % → 33 % | 541.5 px | 0.18 | 0.44 | 6740 |
| stroke 6 | 88 % → 26 % | 548.0 px | 0.18 | 0.30 | 7402 |
| stroke 7 | 100 % → 19 % | 465.5 px | 0.21 | 0.19 | 5448 |
| stroke 8 | 7 % → 41 % | 86.1 px | 0.18 | 5.78 | 1201 |
| stroke 9 | 12 % → 40 % | 184.5 px | 0.18 | 3.37 | 1262 |
| stroke 10 | 16 % → 16 % | 253.1 px | 0.18 | 1.00 | 1055 |
| stroke 11 | 19 % → 19 % | 52.8 px | 0.18 | 1.00 | 877 |
| stroke 12 | 25 % → 36 % | 369.7 px | 0.18 | 1.43 | 776 |
| stroke 13 | 34 % → 40 % | 478.5 px | 0.18 | 1.17 | 784 |
| stroke 14 | 39 % → 41 % | 451.5 px | 0.18 | 1.07 | 998 |
| stroke 15 | 10 % → 49 % | 79.7 px | 0.16 | 4.66 | 1059 |
| stroke 16 | 15 % → 47 % | 133.6 px | 0.16 | 3.16 | 799 |
| stroke 17 | 19 % → 45 % | 180.4 px | 0.16 | 2.39 | 754 |
| stroke 18 | 23 % → 43 % | 228.1 px | 0.16 | 1.84 | 837 |
| stroke 19 | 26 % → 40 % | 289.8 px | 0.16 | 1.56 | 1177 |
| stroke 20 | 30 % → 37 % | 352.5 px | 0.16 | 1.25 | 1107 |
| stroke 21 | 33 % → 42 % | 391.7 px | 0.18 | 1.27 | 477 |
| stroke 22 | 33 % → 38 % | 433.8 px | 0.18 | 1.17 | 463 |
| stroke 23 | 32 % → 32 % | 460.9 px | 0.18 | 1.00 | 534 |
| stroke 24 | 34 % → 36 % | 26.5 px | 0.18 | 1.04 | 421 |
| stroke 25 | 39 % → 39 % | 512.5 px | 0.18 | 0.99 | 504 |
| stroke 26 | 44 % → 42 % | 520.1 px | 0.18 | 0.94 | 470 |
| stroke 27 | 24 % → 22 % | 245.9 px | 0.20 | 0.91 | 239 |
| stroke 28 | 26 % → 22 % | 281.3 px | 0.20 | 0.84 | 180 |

Numbers say: wet paint spreads well beyond the stroke.

## Refs v3 · #02 HW cream strokes — own sheet
own sheet 800 × 649 · Gouache 1.00 + turpentine 35 % · 240 px · 96.0 s

![Refs v3 · #02 HW cream strokes — own sheet](Refs-v3-02-HW-cream-strokes-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 26 % → 59 % | 121.7 px | 0.17 | 2.31 | 5627 |
| stroke 2 | 38 % → 49 % | 208.4 px | 0.17 | 1.29 | 6466 |
| stroke 3 | 50 % → 50 % | 308.3 px | 0.17 | 1.00 | 8650 |
| stroke 4 | 65 % → 65 % | 84.6 px | 0.17 | 1.00 | 8166 |
| stroke 5 | 82 % → 82 % | 113.5 px | 0.17 | 1.00 | 6673 |
| stroke 6 | 97 % → 49 % | 525.1 px | 0.17 | 0.50 | 7325 |
| stroke 7 | 100 % → 46 % | 448.7 px | 0.17 | 0.46 | 6307 |
| stroke 8 | 14 % → 56 % | 85.1 px | 0.17 | 4.15 | 1499 |
| stroke 9 | 20 % → 49 % | 169.6 px | 0.17 | 2.43 | 1450 |
| stroke 10 | 29 % → 29 % | 237.9 px | 0.17 | 1.00 | 1042 |
| stroke 11 | 37 % → 37 % | 60.9 px | 0.17 | 1.00 | 1259 |
| stroke 12 | 48 % → 48 % | 84.4 px | 0.17 | 1.00 | 1202 |
| stroke 13 | 55 % → 55 % | 52.4 px | 0.17 | 1.00 | 1098 |
| stroke 14 | 57 % → 49 % | 615.6 px | 0.17 | 0.86 | 825 |
| stroke 15 | 9 % → 53 % | 73.2 px | 0.17 | 5.66 | 977 |
| stroke 16 | 16 % → 47 % | 147.1 px | 0.17 | 2.91 | 902 |
| stroke 17 | 23 % → 23 % | 210.5 px | 0.17 | 1.00 | 1307 |
| stroke 18 | 29 % → 29 % | 52.0 px | 0.17 | 1.00 | 1174 |
| stroke 19 | 35 % → 35 % | 49.3 px | 0.17 | 1.00 | 1025 |
| stroke 20 | 41 % → 41 % | 55.4 px | 0.17 | 1.00 | 1007 |
| stroke 21 | 49 % → 49 % | 72.0 px | 0.17 | 1.00 | 896 |
| stroke 22 | 58 % → 53 % | 498.2 px | 0.17 | 0.92 | 1013 |
| stroke 23 | 50 % → 50 % | 490.4 px | 0.17 | 1.00 | 1048 |
| stroke 24 | 50 % → 50 % | 0.0 px | 0.17 | 1.00 | 846 |
| stroke 25 | 51 % → 46 % | 9.2 px | 0.17 | 0.90 | 1050 |

Numbers say: wet paint spreads well beyond the stroke.

## Refs v3 · #03 HW navy contours — own sheet
own sheet 800 × 601 · Gouache 1.00 + turpentine 35 % · 240 px · 77.7 s

![Refs v3 · #03 HW navy contours — own sheet](Refs-v3-03-HW-navy-contours-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 24 % → 52 % | 113.7 px | 0.42 | 2.15 | 4415 |
| stroke 2 | 36 % → 45 % | 207.4 px | 0.43 | 1.23 | 6261 |
| stroke 3 | 52 % → 52 % | 282.1 px | 0.43 | 1.00 | 7583 |
| stroke 4 | 67 % → 67 % | 81.8 px | 0.43 | 1.00 | 6981 |
| stroke 5 | 84 % → 84 % | 99.7 px | 0.43 | 1.00 | 7202 |
| stroke 6 | 99 % → 45 % | 592.8 px | 0.42 | 0.45 | 6140 |
| stroke 7 | 100 % → 46 % | 483.4 px | 0.39 | 0.46 | 5958 |
| stroke 8 | 4 % → 51 % | 65.7 px | 0.42 | 12.17 | 359 |
| stroke 9 | 6 % → 50 % | 85.5 px | 0.43 | 7.82 | 455 |
| stroke 10 | 9 % → 47 % | 125.6 px | 0.43 | 5.21 | 382 |
| stroke 11 | 17 % → 17 % | 165.7 px | 0.43 | 1.00 | 746 |
| stroke 12 | 23 % → 23 % | 62.5 px | 0.43 | 1.00 | 730 |
| stroke 13 | 29 % → 29 % | 57.5 px | 0.43 | 1.00 | 860 |
| stroke 14 | 31 % → 31 % | 24.2 px | 0.43 | 1.00 | 889 |
| stroke 15 | 37 % → 37 % | 55.7 px | 0.43 | 1.00 | 927 |
| stroke 16 | 44 % → 44 % | 252.5 px | 0.42 | 1.00 | 753 |
| stroke 17 | 47 % → 48 % | 261.3 px | 0.42 | 1.02 | 820 |
| stroke 18 | 44 % → 44 % | 439.1 px | 0.43 | 1.00 | 442 |
| stroke 19 | 44 % → 45 % | 0.0 px | 0.43 | 1.02 | 493 |
| stroke 20 | 48 % → 48 % | 579.0 px | 0.42 | 0.99 | 385 |
| stroke 21 | 50 % → 48 % | 544.3 px | 0.42 | 0.95 | 383 |

Numbers say: wet paint spreads well beyond the stroke.

## Refs v3 · #04 HW grey cloud — own sheet
own sheet 800 × 649 · Gouache 1.00 + turpentine 30 % · 240 px · 114.7 s

![Refs v3 · #04 HW grey cloud — own sheet](Refs-v3-04-HW-grey-cloud-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 23 % → 76 % | 103.1 px | 0.25 | 3.27 | 4068 |
| stroke 2 | 38 % → 63 % | 216.5 px | 0.25 | 1.66 | 6685 |
| stroke 3 | 50 % → 50 % | 321.8 px | 0.25 | 1.00 | 6292 |
| stroke 4 | 67 % → 67 % | 112.2 px | 0.25 | 1.00 | 8248 |
| stroke 5 | 82 % → 82 % | 86.1 px | 0.25 | 1.00 | 7559 |
| stroke 6 | 96 % → 60 % | 572.4 px | 0.25 | 0.63 | 6699 |
| stroke 7 | 100 % → 55 % | 455.4 px | 0.25 | 0.55 | 5801 |
| stroke 8 | 4 % → 4 % | 73.2 px | 0.25 | 1.01 | 523 |
| stroke 9 | 8 % → 8 % | 63.6 px | 0.25 | 1.00 | 420 |
| stroke 10 | 11 % → 61 % | 178.5 px | 0.25 | 5.29 | 337 |
| stroke 11 | 16 % → 61 % | 125.1 px | 0.25 | 3.70 | 1119 |
| stroke 12 | 24 % → 60 % | 164.7 px | 0.25 | 2.53 | 1084 |
| stroke 13 | 34 % → 57 % | 204.9 px | 0.25 | 1.67 | 1198 |
| stroke 14 | 32 % → 32 % | 564.5 px | 0.25 | 1.00 | 506 |
| stroke 15 | 35 % → 60 % | 540.8 px | 0.25 | 1.70 | 716 |
| stroke 16 | 13 % → 71 % | 85.4 px | 0.25 | 5.35 | 1196 |
| stroke 17 | 20 % → 64 % | 143.6 px | 0.25 | 3.22 | 1743 |
| stroke 18 | 25 % → 61 % | 171.5 px | 0.25 | 2.45 | 1576 |
| stroke 19 | 28 % → 28 % | 228.3 px | 0.25 | 1.00 | 1174 |
| stroke 20 | 36 % → 36 % | 58.8 px | 0.25 | 1.00 | 1452 |
| stroke 21 | 44 % → 44 % | 59.4 px | 0.25 | 1.00 | 1413 |
| stroke 22 | 51 % → 51 % | 49.7 px | 0.25 | 1.00 | 1220 |
| stroke 23 | 57 % → 57 % | 51.2 px | 0.25 | 1.00 | 1370 |
| stroke 24 | 60 % → 59 % | 17.7 px | 0.25 | 1.00 | 2067 |
| stroke 25 | 69 % → 69 % | 515.5 px | 0.25 | 1.00 | 1267 |
| stroke 26 | 63 % → 63 % | 491.9 px | 0.25 | 0.99 | 1520 |
| stroke 27 | 60 % → 60 % | 524.4 px | 0.25 | 1.00 | 1060 |
| stroke 28 | 60 % → 60 % | 0.0 px | 0.25 | 1.00 | 1543 |
| stroke 29 | 60 % → 60 % | 0.0 px | 0.25 | 1.00 | 1319 |
| stroke 30 | 60 % → 60 % | 0.0 px | 0.25 | 1.00 | 1221 |
| stroke 31 | 60 % → 59 % | 2.9 px | 0.25 | 0.99 | 698 |
| stroke 32 | 63 % → 61 % | 450.5 px | 0.25 | 0.96 | 651 |

Numbers say: wet paint spreads well beyond the stroke.

## Refs v3 · #05 HW green in rust loops — own sheet
own sheet 800 × 1000 · Gouache 1.00 + water 15 % · 240 px · 117.7 s

![Refs v3 · #05 HW green in rust loops — own sheet](Refs-v3-05-HW-green-in-rust-loops-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 23 % → 42 % | 112.1 px | 0.22 | 1.81 | 5078 |
| stroke 2 | 41 % → 49 % | 267.8 px | 0.17 | 1.20 | 6977 |
| stroke 3 | 52 % → 47 % | 439.3 px | 0.23 | 0.90 | 6582 |
| stroke 4 | 59 % → 44 % | 569.8 px | 0.26 | 0.75 | 9466 |
| stroke 5 | 68 % → 47 % | 560.8 px | 0.25 | 0.68 | 7299 |
| stroke 6 | 86 % → 50 % | 573.3 px | 0.23 | 0.58 | 7560 |
| stroke 7 | 97 % → 46 % | 477.1 px | 0.26 | 0.47 | 6490 |
| stroke 8 | 99 % → 48 % | 523.3 px | 0.26 | 0.48 | 1266 |
| stroke 9 | 99 % → 48 % | 589.1 px | 0.26 | 0.48 | 1093 |
| stroke 10 | 98 % → 46 % | 548.5 px | 0.27 | 0.47 | 1520 |
| stroke 11 | 98 % → 45 % | 479.0 px | 0.27 | 0.46 | 1000 |
| stroke 12 | 5 % → 46 % | 45.6 px | 0.19 | 8.43 | 456 |
| stroke 13 | 10 % → 49 % | 85.1 px | 0.17 | 4.94 | 518 |
| stroke 14 | 13 % → 48 % | 136.3 px | 0.21 | 3.87 | 510 |
| stroke 15 | 15 % → 47 % | 172.0 px | 0.23 | 3.02 | 446 |
| stroke 16 | 17 % → 47 % | 101.0 px | 0.23 | 2.75 | 813 |
| stroke 17 | 19 % → 47 % | 108.3 px | 0.23 | 2.53 | 798 |
| stroke 18 | 22 % → 46 % | 236.0 px | 0.24 | 2.07 | 1354 |
| stroke 19 | 27 % → 45 % | 301.2 px | 0.26 | 1.67 | 1759 |
| stroke 20 | 32 % → 44 % | 373.6 px | 0.26 | 1.36 | 1279 |
| stroke 21 | 37 % → 45 % | 412.0 px | 0.25 | 1.21 | 1364 |
| stroke 22 | 43 % → 46 % | 449.4 px | 0.25 | 1.07 | 1217 |
| stroke 23 | 54 % → 54 % | 269.9 px | 0.24 | 1.00 | 2115 |
| stroke 24 | 63 % → 47 % | 48.2 px | 0.24 | 0.75 | 3047 |

Numbers say: wet paint spreads well beyond the stroke.

## Refs v3 · #06 HW scrubbed grey — own sheet
own sheet 800 × 649 · Gouache 1.00 + turpentine 30 % · 240 px · 116.2 s

![Refs v3 · #06 HW scrubbed grey — own sheet](Refs-v3-06-HW-scrubbed-grey-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 24 % → 75 % | 116.8 px | 0.25 | 3.13 | 4460 |
| stroke 2 | 37 % → 65 % | 201.2 px | 0.25 | 1.77 | 6127 |
| stroke 3 | 51 % → 51 % | 300.8 px | 0.25 | 1.00 | 7381 |
| stroke 4 | 68 % → 68 % | 107.2 px | 0.25 | 1.00 | 6914 |
| stroke 5 | 82 % → 82 % | 83.1 px | 0.25 | 1.00 | 7788 |
| stroke 6 | 97 % → 59 % | 593.8 px | 0.25 | 0.61 | 7055 |
| stroke 7 | 100 % → 55 % | 492.1 px | 0.25 | 0.55 | 5616 |
| stroke 8 | 5 % → 5 % | 73.0 px | 0.25 | 1.00 | 554 |
| stroke 9 | 7 % → 7 % | 47.3 px | 0.25 | 1.00 | 703 |
| stroke 10 | 10 % → 60 % | 172.6 px | 0.25 | 5.86 | 801 |
| stroke 11 | 17 % → 59 % | 119.3 px | 0.25 | 3.50 | 3498 |
| stroke 12 | 27 % → 57 % | 182.5 px | 0.25 | 2.16 | 1316 |
| stroke 13 | 31 % → 56 % | 204.8 px | 0.25 | 1.79 | 1235 |
| stroke 14 | 30 % → 29 % | 593.6 px | 0.25 | 1.00 | 363 |
| stroke 15 | 32 % → 60 % | 554.7 px | 0.25 | 1.87 | 535 |
| stroke 16 | 13 % → 73 % | 78.8 px | 0.25 | 5.80 | 1213 |
| stroke 17 | 21 % → 65 % | 150.6 px | 0.25 | 3.06 | 1472 |
| stroke 18 | 25 % → 61 % | 179.0 px | 0.25 | 2.50 | 1637 |
| stroke 19 | 30 % → 30 % | 214.2 px | 0.25 | 1.00 | 2064 |
| stroke 20 | 37 % → 37 % | 56.9 px | 0.25 | 1.00 | 1520 |
| stroke 21 | 41 % → 41 % | 29.5 px | 0.25 | 1.00 | 1492 |
| stroke 22 | 47 % → 47 % | 48.3 px | 0.25 | 1.00 | 1420 |
| stroke 23 | 56 % → 56 % | 68.4 px | 0.25 | 1.00 | 1436 |
| stroke 24 | 60 % → 60 % | 30.7 px | 0.25 | 1.00 | 1579 |
| stroke 25 | 70 % → 69 % | 511.5 px | 0.25 | 0.99 | 1743 |
| stroke 26 | 64 % → 64 % | 503.9 px | 0.25 | 0.99 | 1846 |
| stroke 27 | 60 % → 60 % | 486.3 px | 0.25 | 1.00 | 1264 |
| stroke 28 | 60 % → 60 % | 0.0 px | 0.25 | 1.00 | 1340 |
| stroke 29 | 60 % → 60 % | 0.0 px | 0.25 | 1.00 | 1466 |
| stroke 30 | 60 % → 60 % | 0.5 px | 0.25 | 1.00 | 1478 |
| stroke 31 | 61 % → 60 % | 5.5 px | 0.25 | 0.98 | 443 |
| stroke 32 | 63 % → 60 % | 446.6 px | 0.25 | 0.95 | 635 |

Numbers say: wet paint spreads well beyond the stroke.

## Refs v3 · #07 HW blue L and zigzag — own sheet
own sheet 800 × 1066 · Gouache 1.00 + turpentine 35 % · 240 px · 110.0 s

![Refs v3 · #07 HW blue L and zigzag — own sheet](Refs-v3-07-HW-blue-L-and-zigzag-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 25 % → 37 % | 115.5 px | 0.16 | 1.51 | 4727 |
| stroke 2 | 44 % → 38 % | 296.7 px | 0.18 | 0.88 | 6666 |
| stroke 3 | 55 % → 37 % | 450.3 px | 0.17 | 0.68 | 6296 |
| stroke 4 | 61 % → 38 % | 547.8 px | 0.19 | 0.63 | 7657 |
| stroke 5 | 69 % → 37 % | 562.6 px | 0.20 | 0.54 | 6298 |
| stroke 6 | 85 % → 35 % | 531.1 px | 0.21 | 0.41 | 6224 |
| stroke 7 | 99 % → 36 % | 488.2 px | 0.22 | 0.36 | 5718 |
| stroke 8 | 12 % → 38 % | 76.9 px | 0.17 | 3.18 | 1329 |
| stroke 9 | 17 % → 38 % | 137.2 px | 0.17 | 2.27 | 2137 |
| stroke 10 | 23 % → 36 % | 203.2 px | 0.18 | 1.54 | 2205 |
| stroke 11 | 26 % → 37 % | 266.9 px | 0.17 | 1.40 | 1508 |
| stroke 12 | 27 % → 38 % | 290.5 px | 0.19 | 1.43 | 1517 |
| stroke 13 | 29 % → 38 % | 299.0 px | 0.19 | 1.31 | 1661 |
| stroke 14 | 31 % → 34 % | 263.3 px | 0.21 | 1.10 | 1612 |
| stroke 15 | 49 % → 39 % | 1689.4 px | 0.18 | 0.80 | 266 |
| stroke 16 | 48 % → 38 % | 1541.7 px | 0.18 | 0.79 | 280 |
| stroke 17 | 50 % → 38 % | 1181.5 px | 0.16 | 0.76 | 347 |
| stroke 18 | 39 % → 39 % | 351.9 px | 0.19 | 0.99 | 902 |
| stroke 19 | 42 % → 37 % | 12.1 px | 0.19 | 0.89 | 1028 |
| stroke 20 | 57 % → 40 % | 571.1 px | 0.18 | 0.70 | 390 |
| stroke 21 | 44 % → 38 % | 1150.1 px | 0.22 | 0.86 | 69 |
| stroke 22 | 44 % → 38 % | 1233.7 px | 0.22 | 0.87 | 100 |
| stroke 23 | 44 % → 38 % | 1381.5 px | 0.22 | 0.85 | 111 |
| stroke 24 | 45 % → 37 % | 1633.4 px | 0.22 | 0.83 | 106 |
| stroke 25 | 46 % → 37 % | 2081.6 px | 0.21 | 0.81 | 75 |
| stroke 26 | 47 % → 37 % | 3015.2 px | 0.21 | 0.80 | 51 |
| stroke 27 | 48 % → 38 % | 5829.6 px | 0.20 | 0.79 | 54 |
| stroke 28 | 35 % → 35 % | 728.5 px | 0.23 | 1.00 | 312 |
| stroke 29 | 39 % → 38 % | 773.0 px | 0.22 | 0.97 | 328 |
| stroke 30 | 40 % → 35 % | 957.8 px | 0.22 | 0.86 | 346 |
| stroke 31 | 43 % → 36 % | 1154.0 px | 0.22 | 0.84 | 189 |
| stroke 32 | 47 % → 38 % | 484.9 px | 0.24 | 0.81 | 293 |
| stroke 33 | 42 % → 34 % | 643.9 px | 0.22 | 0.81 | 225 |

Numbers say: wet paint spreads well beyond the stroke.

## Refs v3 · #08 HW lilac crown basket — own sheet
own sheet 800 × 1000 · Gouache 1.00 + turpentine 35 % · 240 px · 108.4 s

![Refs v3 · #08 HW lilac crown basket — own sheet](Refs-v3-08-HW-lilac-crown-basket-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 25 % → 25 % | 119.5 px | 0.16 | 1.02 | 4828 |
| stroke 2 | 43 % → 32 % | 265.0 px | 0.28 | 0.76 | 6356 |
| stroke 3 | 53 % → 38 % | 379.2 px | 0.35 | 0.72 | 7304 |
| stroke 4 | 61 % → 61 % | 561.6 px | 0.38 | 1.00 | 7232 |
| stroke 5 | 71 % → 39 % | 563.5 px | 0.40 | 0.55 | 6462 |
| stroke 6 | 85 % → 42 % | 569.5 px | 0.44 | 0.50 | 6290 |
| stroke 7 | 99 % → 45 % | 453.7 px | 0.50 | 0.45 | 5572 |
| stroke 8 | 100 % → 38 % | 1114.1 px | 0.38 | 0.39 | 1845 |
| stroke 9 | 99 % → 39 % | 965.9 px | 0.38 | 0.39 | 1177 |
| stroke 10 | 99 % → 41 % | 922.5 px | 0.42 | 0.41 | 1336 |
| stroke 11 | 99 % → 44 % | 610.2 px | 0.51 | 0.45 | 1257 |
| stroke 12 | 3 % → 43 % | 54.6 px | 0.37 | 14.22 | 370 |
| stroke 13 | 5 % → 38 % | 109.0 px | 0.36 | 7.86 | 306 |
| stroke 14 | 7 % → 39 % | 164.6 px | 0.36 | 5.20 | 374 |
| stroke 15 | 9 % → 37 % | 164.1 px | 0.34 | 3.98 | 290 |
| stroke 16 | 13 % → 38 % | 142.8 px | 0.36 | 2.91 | 760 |
| stroke 17 | 15 % → 36 % | 173.0 px | 0.38 | 2.37 | 594 |
| stroke 18 | 18 % → 18 % | 220.7 px | 0.38 | 0.99 | 561 |
| stroke 19 | 22 % → 36 % | 290.3 px | 0.38 | 1.62 | 457 |
| stroke 20 | 26 % → 38 % | 303.0 px | 0.38 | 1.45 | 533 |
| stroke 21 | 30 % → 39 % | 341.1 px | 0.39 | 1.30 | 781 |
| stroke 22 | 34 % → 40 % | 369.3 px | 0.40 | 1.16 | 799 |
| stroke 23 | 39 % → 41 % | 376.9 px | 0.42 | 1.04 | 676 |
| stroke 24 | 45 % → 42 % | 385.6 px | 0.43 | 0.93 | 718 |
| stroke 25 | 51 % → 43 % | 423.2 px | 0.45 | 0.84 | 716 |
| stroke 26 | 45 % → 35 % | 193.2 px | 0.38 | 0.77 | 2138 |
| stroke 27 | 46 % → 36 % | 907.0 px | 0.38 | 0.77 | 295 |
| stroke 28 | 49 % → 38 % | 893.4 px | 0.38 | 0.78 | 329 |
| stroke 29 | 51 % → 39 % | 850.5 px | 0.39 | 0.78 | 255 |
| stroke 30 | 53 % → 41 % | 815.4 px | 0.42 | 0.76 | 342 |

Numbers say: wet paint spreads well beyond the stroke.

## Refs v3 · #09 HW white loops — own sheet
own sheet 800 × 653 · Gouache 1.00 + turpentine 30 % · 240 px · 108.8 s

![Refs v3 · #09 HW white loops — own sheet](Refs-v3-09-HW-white-loops-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 24 % → 60 % | 111.6 px | 0.15 | 2.56 | 5016 |
| stroke 2 | 38 % → 49 % | 215.6 px | 0.15 | 1.28 | 9683 |
| stroke 3 | 51 % → 51 % | 300.6 px | 0.15 | 1.00 | 7688 |
| stroke 4 | 67 % → 67 % | 94.9 px | 0.15 | 1.00 | 9310 |
| stroke 5 | 80 % → 80 % | 78.1 px | 0.15 | 1.00 | 9017 |
| stroke 6 | 96 % → 48 % | 542.5 px | 0.15 | 0.51 | 7609 |
| stroke 7 | 100 % → 48 % | 452.7 px | 0.15 | 0.48 | 6232 |
| stroke 8 | 100 % → 64 % | 2006.3 px | 0.15 | 0.64 | 289 |
| stroke 9 | 100 % → 57 % | 2832.9 px | 0.15 | 0.57 | 200 |
| stroke 10 | 100 % → 50 % | 1269.0 px | 0.15 | 0.51 | 321 |
| stroke 11 | 100 % → 49 % | 1065.7 px | 0.15 | 0.49 | 251 |
| stroke 12 | 100 % → 52 % | 3523.8 px | 0.15 | 0.52 | 135 |
| stroke 13 | 100 % → 48 % | 3808.2 px | 0.15 | 0.48 | 152 |
| stroke 14 | 100 % → 49 % | 4185.8 px | 0.15 | 0.49 | 129 |
| stroke 15 | 9 % → 9 % | 60.1 px | 0.15 | 1.00 | 1575 |
| stroke 16 | 15 % → 15 % | 38.2 px | 0.15 | 1.00 | 1690 |
| stroke 17 | 21 % → 21 % | 42.0 px | 0.15 | 1.00 | 1276 |
| stroke 18 | 28 % → 28 % | 35.7 px | 0.15 | 1.00 | 1800 |
| stroke 19 | 30 % → 30 % | 17.6 px | 0.15 | 1.00 | 1329 |
| stroke 20 | 33 % → 33 % | 22.9 px | 0.15 | 1.00 | 1134 |
| stroke 21 | 33 % → 33 % | 3.3 px | 0.15 | 1.00 | 2032 |
| stroke 22 | 37 % → 37 % | 20.9 px | 0.15 | 1.00 | 3544 |
| stroke 23 | 37 % → 37 % | 4.5 px | 0.15 | 1.00 | 909 |
| stroke 24 | 46 % → 51 % | 400.6 px | 0.15 | 1.11 | 917 |
| stroke 25 | 43 % → 43 % | 370.9 px | 0.15 | 1.00 | 1188 |
| stroke 26 | 43 % → 43 % | 1.5 px | 0.15 | 1.00 | 940 |
| stroke 27 | 45 % → 44 % | 10.0 px | 0.15 | 1.00 | 1071 |
| stroke 28 | 47 % → 46 % | 26.1 px | 0.15 | 0.97 | 920 |

Numbers say: wet paint spreads well beyond the stroke.

## Refs v3 · #10 HW maroon loops — own sheet
own sheet 800 × 1000 · Gouache 1.00 + turpentine 35 % · 240 px · 127.6 s

![Refs v3 · #10 HW maroon loops — own sheet](Refs-v3-10-HW-maroon-loops-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 26 % → 36 % | 129.1 px | 0.37 | 1.37 | 5931 |
| stroke 2 | 44 % → 45 % | 280.0 px | 0.52 | 1.03 | 6636 |
| stroke 3 | 53 % → 50 % | 410.7 px | 0.58 | 0.95 | 9444 |
| stroke 4 | 61 % → 52 % | 543.5 px | 0.62 | 0.86 | 7332 |
| stroke 5 | 73 % → 60 % | 547.5 px | 0.65 | 0.83 | 6290 |
| stroke 6 | 89 % → 65 % | 530.8 px | 0.72 | 0.73 | 6659 |
| stroke 7 | 100 % → 69 % | 478.5 px | 0.76 | 0.69 | 5713 |
| stroke 8 | 3 % → 62 % | 67.1 px | 0.60 | 18.86 | 611 |
| stroke 9 | 6 % → 55 % | 128.6 px | 0.61 | 9.37 | 447 |
| stroke 10 | 8 % → 53 % | 197.9 px | 0.61 | 6.32 | 369 |
| stroke 11 | 12 % → 12 % | 264.1 px | 0.59 | 1.00 | 432 |
| stroke 12 | 13 % → 58 % | 316.1 px | 0.61 | 4.45 | 419 |
| stroke 13 | 13 % → 52 % | 408.9 px | 0.60 | 4.11 | 321 |
| stroke 14 | 14 % → 52 % | 386.3 px | 0.59 | 3.63 | 345 |
| stroke 15 | 17 % → 52 % | 136.9 px | 0.62 | 3.06 | 1173 |
| stroke 16 | 20 % → 52 % | 204.4 px | 0.62 | 2.60 | 789 |
| stroke 17 | 23 % → 52 % | 139.8 px | 0.62 | 2.25 | 1517 |
| stroke 18 | 30 % → 55 % | 178.1 px | 0.62 | 1.84 | 1840 |
| stroke 19 | 34 % → 57 % | 239.6 px | 0.62 | 1.68 | 1554 |
| stroke 20 | 40 % → 59 % | 187.9 px | 0.63 | 1.48 | 1770 |
| stroke 21 | 43 % → 60 % | 218.5 px | 0.65 | 1.39 | 1698 |
| stroke 22 | 47 % → 62 % | 270.9 px | 0.66 | 1.30 | 1343 |
| stroke 23 | 53 % → 63 % | 251.1 px | 0.68 | 1.18 | 1491 |
| stroke 24 | 60 % → 64 % | 194.0 px | 0.71 | 1.08 | 2919 |
| stroke 25 | 58 % → 62 % | 1286.1 px | 0.66 | 1.07 | 330 |
| stroke 26 | 58 % → 62 % | 1642.6 px | 0.66 | 1.06 | 240 |
| stroke 27 | 59 % → 62 % | 1510.4 px | 0.68 | 1.06 | 433 |
| stroke 28 | 63 % → 68 % | 747.1 px | 0.76 | 1.07 | 939 |
| stroke 29 | 69 % → 69 % | 610.0 px | 0.76 | 1.00 | 730 |

Numbers say: wet paint spreads well beyond the stroke.

## Refs v3 · #11 HW purple balls — own sheet
own sheet 800 × 985 · Gouache 1.00 + turpentine 35 % · 240 px · 123.8 s

![Refs v3 · #11 HW purple balls — own sheet](Refs-v3-11-HW-purple-balls-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 24 % → 71 % | 114.3 px | 0.06 | 2.93 | 4850 |
| stroke 2 | 44 % → 73 % | 280.0 px | 0.06 | 1.66 | 7479 |
| stroke 3 | 53 % → 68 % | 388.0 px | 0.09 | 1.28 | 7836 |
| stroke 4 | 60 % → 60 % | 592.5 px | 0.12 | 1.00 | 6870 |
| stroke 5 | 72 % → 60 % | 561.5 px | 0.14 | 0.84 | 6221 |
| stroke 6 | 87 % → 56 % | 591.0 px | 0.16 | 0.64 | 5837 |
| stroke 7 | 99 % → 51 % | 481.1 px | 0.20 | 0.51 | 5359 |
| stroke 8 | 13 % → 72 % | 85.1 px | 0.06 | 5.54 | 1889 |
| stroke 9 | 23 % → 74 % | 166.4 px | 0.06 | 3.21 | 1412 |
| stroke 10 | 28 % → 73 % | 213.0 px | 0.06 | 2.56 | 1211 |
| stroke 11 | 34 % → 70 % | 290.0 px | 0.06 | 2.04 | 1220 |
| stroke 12 | 38 % → 67 % | 402.9 px | 0.09 | 1.76 | 1046 |
| stroke 13 | 41 % → 65 % | 472.5 px | 0.12 | 1.56 | 1031 |
| stroke 14 | 43 % → 65 % | 811.0 px | 0.13 | 1.50 | 765 |
| stroke 15 | 44 % → 63 % | 928.9 px | 0.13 | 1.42 | 816 |
| stroke 16 | 45 % → 45 % | 963.6 px | 0.12 | 1.00 | 965 |
| stroke 17 | 48 % → 60 % | 68.4 px | 0.12 | 1.26 | 704 |
| stroke 18 | 53 % → 63 % | 989.6 px | 0.13 | 1.19 | 816 |
| stroke 19 | 57 % → 65 % | 1039.0 px | 0.13 | 1.14 | 726 |
| stroke 20 | 54 % → 61 % | 1651.7 px | 0.12 | 1.12 | 500 |
| stroke 21 | 53 % → 61 % | 1208.3 px | 0.13 | 1.15 | 718 |
| stroke 22 | 60 % → 64 % | 2132.8 px | 0.13 | 1.08 | 477 |
| stroke 23 | 58 % → 63 % | 1526.8 px | 0.13 | 1.08 | 502 |
| stroke 24 | 80 % → 73 % | 616.0 px | 0.06 | 0.91 | 1015 |
| stroke 25 | 76 % → 70 % | 738.0 px | 0.06 | 0.92 | 1551 |
| stroke 26 | 62 % → 64 % | 730.2 px | 0.12 | 1.03 | 1225 |
| stroke 27 | 58 % → 61 % | 686.7 px | 0.13 | 1.05 | 1317 |
| stroke 28 | 55 % → 58 % | 235.3 px | 0.15 | 1.05 | 2017 |
| stroke 29 | 59 % → 57 % | 251.7 px | 0.16 | 0.97 | 1544 |
| stroke 30 | 63 % → 58 % | 274.7 px | 0.15 | 0.91 | 1820 |

Numbers say: wet paint spreads well beyond the stroke.

## Refs v3 · #12 HW black-olive cage — own sheet
own sheet 800 × 1000 · Gouache 1.00 + turpentine 35 % · 240 px · 101.6 s

![Refs v3 · #12 HW black-olive cage — own sheet](Refs-v3-12-HW-black-olive-cage-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 25 % → 26 % | 118.9 px | 0.18 | 1.06 | 4275 |
| stroke 2 | 42 % → 32 % | 268.5 px | 0.27 | 0.76 | 6866 |
| stroke 3 | 54 % → 54 % | 410.5 px | 0.35 | 1.00 | 6105 |
| stroke 4 | 61 % → 34 % | 532.1 px | 0.37 | 0.57 | 7675 |
| stroke 5 | 70 % → 38 % | 530.9 px | 0.39 | 0.54 | 6393 |
| stroke 6 | 85 % → 40 % | 555.4 px | 0.43 | 0.47 | 8068 |
| stroke 7 | 100 % → 41 % | 517.9 px | 0.50 | 0.41 | 5835 |
| stroke 8 | 100 % → 37 % | 1069.3 px | 0.37 | 0.37 | 992 |
| stroke 9 | 99 % → 37 % | 1029.4 px | 0.38 | 0.38 | 781 |
| stroke 10 | 100 % → 40 % | 888.6 px | 0.42 | 0.40 | 954 |
| stroke 11 | 100 % → 41 % | 600.2 px | 0.50 | 0.41 | 1029 |
| stroke 12 | 3 % → 42 % | 54.6 px | 0.37 | 13.85 | 473 |
| stroke 13 | 5 % → 36 % | 108.6 px | 0.35 | 7.45 | 407 |
| stroke 14 | 7 % → 37 % | 163.8 px | 0.35 | 4.94 | 578 |
| stroke 15 | 9 % → 36 % | 162.9 px | 0.33 | 3.84 | 308 |
| stroke 16 | 13 % → 36 % | 142.1 px | 0.35 | 2.76 | 818 |
| stroke 17 | 15 % → 35 % | 191.4 px | 0.37 | 2.35 | 481 |
| stroke 18 | 18 % → 18 % | 230.4 px | 0.37 | 1.00 | 440 |
| stroke 19 | 21 % → 35 % | 285.6 px | 0.37 | 1.63 | 462 |
| stroke 20 | 26 % → 37 % | 316.0 px | 0.37 | 1.43 | 558 |
| stroke 21 | 30 % → 38 % | 323.3 px | 0.38 | 1.27 | 541 |
| stroke 22 | 34 % → 38 % | 332.1 px | 0.40 | 1.11 | 559 |
| stroke 23 | 37 % → 39 % | 389.5 px | 0.41 | 1.06 | 576 |
| stroke 24 | 42 % → 40 % | 406.7 px | 0.43 | 0.95 | 542 |
| stroke 25 | 48 % → 41 % | 412.9 px | 0.45 | 0.85 | 504 |
| stroke 26 | 43 % → 34 % | 185.4 px | 0.37 | 0.78 | 2584 |
| stroke 27 | 44 % → 34 % | 861.9 px | 0.37 | 0.78 | 267 |
| stroke 28 | 47 % → 37 % | 859.5 px | 0.37 | 0.78 | 268 |
| stroke 29 | 49 % → 38 % | 826.3 px | 0.39 | 0.77 | 218 |
| stroke 30 | 51 % → 39 % | 784.0 px | 0.41 | 0.76 | 259 |

Numbers say: wet paint spreads well beyond the stroke.

## Refs v3 · #13 HW blue streaky form — own sheet
own sheet 800 × 1000 · Gouache 1.00 + turpentine 35 % · 240 px · 138.3 s

![Refs v3 · #13 HW blue streaky form — own sheet](Refs-v3-13-HW-blue-streaky-form-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 29 % → 43 % | 145.4 px | 0.05 | 1.51 | 5299 |
| stroke 2 | 44 % → 44 % | 291.5 px | 0.05 | 1.00 | 5352 |
| stroke 3 | 55 % → 53 % | 414.2 px | 0.06 | 0.97 | 7062 |
| stroke 4 | 61 % → 56 % | 540.8 px | 0.06 | 0.92 | 7643 |
| stroke 5 | 72 % → 67 % | 545.7 px | 0.06 | 0.93 | 9720 |
| stroke 6 | 87 % → 73 % | 572.5 px | 0.06 | 0.84 | 8128 |
| stroke 7 | 100 % → 70 % | 499.8 px | 0.07 | 0.71 | 6496 |
| stroke 8 | 100 % → 61 % | 829.2 px | 0.06 | 0.61 | 645 |
| stroke 9 | 100 % → 61 % | 933.1 px | 0.06 | 0.61 | 694 |
| stroke 10 | 100 % → 53 % | 2697.9 px | 0.05 | 0.53 | 131 |
| stroke 11 | 100 % → 52 % | 2909.4 px | 0.05 | 0.52 | 158 |
| stroke 12 | 100 % → 51 % | 3130.9 px | 0.05 | 0.51 | 150 |
| stroke 13 | 100 % → 49 % | 3323.3 px | 0.05 | 0.49 | 107 |
| stroke 14 | 100 % → 99 % | 3376.8 px | 0.05 | 1.00 | 126 |
| stroke 15 | 99 % → 99 % | 0.0 px | 0.05 | 1.00 | 224 |
| stroke 16 | 99 % → 99 % | 0.0 px | 0.05 | 1.00 | 160 |
| stroke 17 | 100 % → 49 % | 3313.8 px | 0.05 | 0.50 | 127 |
| stroke 18 | 100 % → 52 % | 3034.1 px | 0.05 | 0.52 | 196 |
| stroke 19 | 99 % → 52 % | 2819.5 px | 0.05 | 0.52 | 135 |
| stroke 20 | 99 % → 52 % | 2684.1 px | 0.05 | 0.52 | 152 |
| stroke 21 | 99 % → 48 % | 2256.7 px | 0.05 | 0.49 | 249 |
| stroke 22 | 9 % → 51 % | 84.4 px | 0.05 | 5.38 | 1321 |
| stroke 23 | 17 % → 53 % | 168.4 px | 0.06 | 3.08 | 1195 |
| stroke 24 | 22 % → 54 % | 228.9 px | 0.06 | 2.47 | 1596 |
| stroke 25 | 27 % → 56 % | 296.0 px | 0.06 | 2.05 | 1747 |
| stroke 26 | 36 % → 59 % | 375.2 px | 0.06 | 1.67 | 1562 |
| stroke 27 | 47 % → 66 % | 475.0 px | 0.06 | 1.39 | 1409 |
| stroke 28 | 60 % → 71 % | 532.5 px | 0.06 | 1.19 | 1422 |
| stroke 29 | 62 % → 71 % | 551.2 px | 0.06 | 1.14 | 1490 |
| stroke 30 | 71 % → 72 % | 538.6 px | 0.06 | 1.01 | 1264 |
| stroke 31 | 82 % → 71 % | 508.0 px | 0.07 | 0.86 | 1167 |
| stroke 32 | 60 % → 52 % | 647.8 px | 0.05 | 0.86 | 1789 |
| stroke 33 | 63 % → 55 % | 693.1 px | 0.06 | 0.86 | 1136 |
| stroke 34 | 66 % → 57 % | 860.3 px | 0.06 | 0.86 | 1691 |
| stroke 35 | 76 % → 65 % | 862.1 px | 0.06 | 0.86 | 2034 |
| stroke 36 | 83 % → 72 % | 718.3 px | 0.06 | 0.87 | 1941 |
| stroke 37 | 84 % → 71 % | 684.9 px | 0.06 | 0.85 | 1339 |

Numbers say: wet paint spreads well beyond the stroke.

## Refs v3 · #14 HW olive totem — own sheet
own sheet 800 × 996 · Gouache 1.00 + turpentine 35 % · 240 px · 117.0 s

![Refs v3 · #14 HW olive totem — own sheet](Refs-v3-14-HW-olive-totem-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 27 % → 36 % | 131.8 px | 0.19 | 1.31 | 5352 |
| stroke 2 | 44 % → 43 % | 267.3 px | 0.20 | 0.97 | 5649 |
| stroke 3 | 53 % → 45 % | 398.3 px | 0.20 | 0.86 | 7529 |
| stroke 4 | 60 % → 41 % | 588.1 px | 0.20 | 0.68 | 7860 |
| stroke 5 | 70 % → 46 % | 571.5 px | 0.20 | 0.66 | 7794 |
| stroke 6 | 87 % → 46 % | 538.4 px | 0.20 | 0.53 | 8423 |
| stroke 7 | 99 % → 43 % | 488.9 px | 0.21 | 0.44 | 6960 |
| stroke 8 | 99 % → 45 % | 1028.3 px | 0.20 | 0.45 | 1148 |
| stroke 9 | 99 % → 44 % | 1104.8 px | 0.20 | 0.45 | 1050 |
| stroke 10 | 99 % → 36 % | 3711.3 px | 0.19 | 0.36 | 176 |
| stroke 11 | 99 % → 45 % | 11008.1 px | 0.20 | 0.45 | 96 |
| stroke 12 | 99 % → 44 % | 1253.4 px | 0.20 | 0.45 | 961 |
| stroke 13 | 98 % → 49 % | 958.8 px | 0.20 | 0.49 | 1090 |
| stroke 14 | 98 % → 48 % | 12492.6 px | 0.20 | 0.49 | 144 |
| stroke 15 | 98 % → 43 % | 6740.0 px | 0.21 | 0.44 | 166 |
| stroke 16 | 4 % → 4 % | 71.4 px | 0.20 | 1.00 | 882 |
| stroke 17 | 8 % → 8 % | 60.1 px | 0.20 | 1.00 | 973 |
| stroke 18 | 12 % → 40 % | 59.1 px | 0.20 | 3.35 | 933 |
| stroke 19 | 16 % → 40 % | 239.1 px | 0.20 | 2.54 | 828 |
| stroke 20 | 26 % → 45 % | 228.2 px | 0.20 | 1.74 | 1210 |
| stroke 21 | 27 % → 45 % | 288.8 px | 0.20 | 1.65 | 1334 |
| stroke 22 | 28 % → 44 % | 325.2 px | 0.20 | 1.54 | 1574 |
| stroke 23 | 30 % → 42 % | 359.3 px | 0.20 | 1.41 | 1462 |
| stroke 24 | 38 % → 46 % | 413.8 px | 0.20 | 1.21 | 1041 |
| stroke 25 | 45 % → 48 % | 454.8 px | 0.20 | 1.07 | 1031 |
| stroke 26 | 50 % → 48 % | 507.5 px | 0.20 | 0.95 | 997 |
| stroke 27 | 53 % → 49 % | 1402.7 px | 0.20 | 0.92 | 421 |
| stroke 28 | 52 % → 47 % | 1659.6 px | 0.20 | 0.90 | 245 |

Numbers say: wet paint spreads well beyond the stroke.

## Refs v3 · #15 Ultramarine script — own sheet
own sheet 800 × 1422 · Ink 0.98 · 9 px · 62.8 s

![Refs v3 · #15 Ultramarine script — own sheet](Refs-v3-15-Ultramarine-script-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 32 % → 47 % | 11.7 px | 0.75 | 1.46 | 417 |
| stroke 2 | 33 % → 46 % | 10.1 px | 0.77 | 1.40 | 258 |
| stroke 3 | 29 % → 40 % | 10.9 px | 0.77 | 1.39 | 238 |
| stroke 4 | 35 % → 48 % | 9.8 px | 0.79 | 1.37 | 317 |
| stroke 5 | 33 % → 45 % | 11.7 px | 0.77 | 1.39 | 162 |
| stroke 6 | 33 % → 46 % | 10.2 px | 0.75 | 1.38 | 182 |
| stroke 7 | 28 % → 39 % | 11.0 px | 0.76 | 1.40 | 144 |
| stroke 8 | 25 % → 35 % | 10.6 px | 0.74 | 1.36 | 204 |
| stroke 9 | 31 % → 44 % | 10.7 px | 0.80 | 1.42 | 162 |
| stroke 10 | 26 % → 39 % | 11.0 px | 0.74 | 1.48 | 117 |
| stroke 11 | 26 % → 41 % | 12.1 px | 0.75 | 1.57 | 76 |
| stroke 12 | 29 % → 41 % | 10.4 px | 0.76 | 1.39 | 204 |
| stroke 13 | 24 % → 38 % | 11.1 px | 0.74 | 1.55 | 165 |
| stroke 14 | 23 % → 36 % | 11.2 px | 0.76 | 1.54 | 112 |
| stroke 15 | 27 % → 41 % | 11.4 px | 0.74 | 1.51 | 160 |
| stroke 16 | 25 % → 38 % | 10.8 px | 0.72 | 1.51 | 141 |
| stroke 17 | 27 % → 39 % | 11.5 px | 0.76 | 1.43 | 147 |
| stroke 18 | 26 % → 40 % | 11.7 px | 0.74 | 1.55 | 142 |
| stroke 19 | 26 % → 40 % | 11.3 px | 0.72 | 1.51 | 191 |
| stroke 20 | 24 % → 36 % | 11.5 px | 0.74 | 1.47 | 165 |
| stroke 21 | 23 % → 36 % | 11.2 px | 0.75 | 1.54 | 314 |
| stroke 22 | 29 % → 43 % | 11.1 px | 0.75 | 1.52 | 307 |
| stroke 23 | 25 % → 40 % | 12.6 px | 0.73 | 1.58 | 228 |
| stroke 24 | 29 % → 40 % | 10.6 px | 0.79 | 1.39 | 344 |
| stroke 25 | 32 % → 46 % | 10.2 px | 0.72 | 1.43 | 400 |
| stroke 26 | 33 % → 47 % | 11.6 px | 0.77 | 1.42 | 351 |
| stroke 27 | 29 % → 40 % | 11.1 px | 0.74 | 1.37 | 318 |
| stroke 28 | 32 % → 45 % | 10.5 px | 0.76 | 1.41 | 354 |
| stroke 29 | 33 % → 47 % | 12.0 px | 0.76 | 1.44 | 204 |
| stroke 30 | 27 % → 39 % | 10.2 px | 0.75 | 1.46 | 254 |
| stroke 31 | 26 % → 37 % | 10.6 px | 0.74 | 1.39 | 191 |
| stroke 32 | 30 % → 45 % | 11.1 px | 0.70 | 1.50 | 123 |
| stroke 33 | 27 % → 40 % | 10.1 px | 0.70 | 1.50 | 192 |
| stroke 34 | 31 % → 46 % | 6.4 px | 0.71 | 1.48 | 264 |
| stroke 35 | 31 % → 47 % | 10.0 px | 0.76 | 1.51 | 168 |
| stroke 36 | 27 % → 38 % | 10.2 px | 0.78 | 1.39 | 235 |
| stroke 37 | 22 % → 35 % | 10.6 px | 0.74 | 1.56 | 106 |
| stroke 38 | 28 % → 39 % | 10.3 px | 0.79 | 1.39 | 247 |
| stroke 39 | 27 % → 38 % | 11.4 px | 0.76 | 1.40 | 147 |
| stroke 40 | 22 % → 34 % | 4.1 px | 0.77 | 1.59 | 159 |
| stroke 41 | 29 % → 41 % | 11.0 px | 0.77 | 1.39 | 233 |
| stroke 42 | 26 % → 39 % | 11.7 px | 0.75 | 1.48 | 120 |
| stroke 43 | 26 % → 35 % | 10.5 px | 0.79 | 1.37 | 220 |
| stroke 44 | 32 % → 48 % | 12.1 px | 0.77 | 1.50 | 208 |
| stroke 45 | 29 % → 42 % | 10.5 px | 0.77 | 1.46 | 346 |
| stroke 46 | 29 % → 40 % | 9.9 px | 0.77 | 1.37 | 403 |
| stroke 47 | 27 % → 40 % | 11.2 px | 0.72 | 1.47 | 313 |
| stroke 48 | 30 % → 42 % | 9.9 px | 0.72 | 1.38 | 418 |
| stroke 49 | 26 % → 36 % | 11.2 px | 0.76 | 1.42 | 223 |
| stroke 50 | 26 % → 40 % | 11.2 px | 0.75 | 1.53 | 128 |
| stroke 51 | 22 % → 34 % | 2.9 px | 0.75 | 1.55 | 314 |
| stroke 52 | 26 % → 36 % | 11.2 px | 0.80 | 1.39 | 248 |
| stroke 53 | 27 % → 38 % | 10.4 px | 0.71 | 1.42 | 257 |
| stroke 54 | 32 % → 43 % | 9.9 px | 0.75 | 1.34 | 347 |
| stroke 55 | 25 % → 38 % | 11.0 px | 0.75 | 1.50 | 115 |
| stroke 56 | 38 % → 52 % | 11.2 px | 0.78 | 1.38 | 200 |
| stroke 57 | 30 % → 43 % | 11.4 px | 0.76 | 1.42 | 231 |
| stroke 58 | 33 % → 46 % | 10.3 px | 0.76 | 1.42 | 318 |
| stroke 59 | 26 % → 38 % | 11.1 px | 0.78 | 1.46 | 229 |
| stroke 60 | 28 % → 40 % | 10.5 px | 0.76 | 1.43 | 209 |
| stroke 61 | 25 % → 38 % | 11.8 px | 0.75 | 1.54 | 134 |

Numbers say: wet paint spreads well beyond the stroke.

## Refs v3 · #16 Shrigley strokes — own sheet
own sheet 800 × 1000 · Watercolour 1.00 + water 30 % · 48 px · 40.3 s

![Refs v3 · #16 Shrigley strokes — own sheet](Refs-v3-16-Shrigley-strokes-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 9 % → 51 % | 39.3 px | 0.47 | 5.92 | 170 |
| stroke 2 | 8 % → 38 % | 40.0 px | 0.46 | 4.61 | 150 |
| stroke 3 | 13 % → 47 % | 40.4 px | 0.27 | 3.52 | 129 |
| stroke 4 | 15 % → 44 % | 84.5 px | 0.50 | 2.95 | 124 |
| stroke 5 | 15 % → 40 % | 72.2 px | 0.45 | 2.73 | 242 |
| stroke 6 | 17 % → 48 % | 66.2 px | 0.26 | 2.79 | 155 |
| stroke 7 | 12 % → 39 % | 49.0 px | 0.48 | 3.37 | 88 |
| stroke 8 | 19 % → 50 % | 71.0 px | 0.53 | 2.64 | 170 |
| stroke 9 | 26 % → 43 % | 127.4 px | 0.46 | 1.65 | 216 |
| stroke 10 | 18 % → 43 % | 69.5 px | 0.49 | 2.33 | 178 |
| stroke 11 | 9 % → 31 % | 39.6 px | 0.46 | 3.37 | 150 |
| stroke 12 | 30 % → 46 % | 122.5 px | 0.26 | 1.57 | 82 |
| stroke 13 | 30 % → 56 % | 153.2 px | 0.44 | 1.84 | 111 |
| stroke 14 | 7 % → 44 % | 40.2 px | 0.46 | 6.20 | 89 |
| stroke 15 | 16 % → 46 % | 89.4 px | 0.46 | 2.85 | 149 |
| stroke 16 | 19 % → 46 % | 98.2 px | 0.45 | 2.45 | 199 |
| stroke 17 | 31 % → 53 % | 185.9 px | 0.46 | 1.70 | 106 |
| stroke 18 | 29 % → 47 % | 137.2 px | 0.46 | 1.60 | 293 |
| stroke 19 | 43 % → 51 % | 172.2 px | 0.52 | 1.19 | 289 |
| stroke 20 | 25 % → 44 % | 93.2 px | 0.47 | 1.79 | 366 |
| stroke 21 | 22 % → 36 % | 102.7 px | 0.43 | 1.59 | 169 |
| stroke 22 | 36 % → 47 % | 161.3 px | 0.48 | 1.32 | 247 |
| stroke 23 | 39 % → 51 % | 171.9 px | 0.45 | 1.30 | 184 |
| stroke 24 | 32 % → 44 % | 148.9 px | 0.34 | 1.36 | 214 |
| stroke 25 | 32 % → 47 % | 145.3 px | 0.40 | 1.45 | 326 |
| stroke 26 | 15 % → 27 % | 75.6 px | 0.42 | 1.83 | 85 |
| stroke 27 | 19 % → 29 % | 70.0 px | 0.34 | 1.57 | 215 |
| stroke 28 | 37 % → 43 % | 176.1 px | 0.46 | 1.16 | 165 |
| stroke 29 | 33 % → 39 % | 140.4 px | 0.44 | 1.18 | 225 |
| stroke 30 | 37 % → 45 % | 170.7 px | 0.44 | 1.19 | 191 |

Numbers say: wet paint spreads well beyond the stroke.

## Refs v3 · #17 Krovostok dry brush — own sheet
own sheet 800 × 800 · Ink 0.93 · Gouache 0.07 · 48 px · 34.7 s

![Refs v3 · #17 Krovostok dry brush — own sheet](Refs-v3-17-Krovostok-dry-brush-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 41 % → 53 % | 42.3 px | 0.94 | 1.31 | 2738 |
| stroke 2 | 41 % → 57 % | 42.6 px | 0.94 | 1.37 | 2252 |
| stroke 3 | 55 % → 72 % | 70.3 px | 0.93 | 1.32 | 1703 |
| stroke 4 | 36 % → 53 % | 169.6 px | 0.93 | 1.45 | 171 |
| stroke 5 | 50 % → 65 % | 207.0 px | 0.93 | 1.30 | 216 |
| stroke 6 | 48 % → 72 % | 203.4 px | 0.93 | 1.48 | 184 |
| stroke 7 | 63 % → 69 % | 237.1 px | 0.93 | 1.09 | 228 |
| stroke 8 | 47 % → 47 % | 255.4 px | 0.92 | 1.00 | 71 |
| stroke 9 | 58 % → 58 % | 316.5 px | 0.93 | 1.00 | 69 |
| stroke 10 | 64 % → 65 % | 164.0 px | 0.94 | 1.02 | 280 |
| stroke 11 | 75 % → 77 % | 1097.2 px | 0.94 | 1.02 | 7 |
| stroke 12 | 75 % → 76 % | 1100.5 px | 0.94 | 1.02 | 7 |
| stroke 13 | 87 % → 89 % | 896.5 px | 0.94 | 1.02 | 11 |

## Refs v3 · #18 Twombly blue sticks — own sheet
own sheet 800 × 789 · Wax 1.00 · 9 px · 10.3 s

![Refs v3 · #18 Twombly blue sticks — own sheet](Refs-v3-18-Twombly-blue-sticks-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 16 % → 61 % | 5.9 px | 0.54 | 3.70 | 345 |
| stroke 2 | 26 % → 67 % | 7.1 px | 0.54 | 2.61 | 362 |
| stroke 3 | 20 % → 55 % | 8.4 px | 0.54 | 2.76 | 324 |
| stroke 4 | 29 % → 66 % | 16.2 px | 0.54 | 2.30 | 366 |
| stroke 5 | 41 % → 73 % | 19.3 px | 0.54 | 1.79 | 405 |
| stroke 6 | 39 % → 72 % | 22.5 px | 0.54 | 1.82 | 373 |
| stroke 7 | 43 % → 58 % | 21.9 px | 0.54 | 1.33 | 318 |
| stroke 8 | 46 % → 66 % | 41.8 px | 0.54 | 1.43 | 350 |
| stroke 9 | 42 % → 57 % | 24.7 px | 0.54 | 1.37 | 370 |
| stroke 10 | 47 % → 59 % | 11.0 px | 0.54 | 1.25 | 416 |
| stroke 11 | 59 % → 70 % | 30.5 px | 0.54 | 1.19 | 383 |
| stroke 12 | 59 % → 63 % | 22.3 px | 0.54 | 1.06 | 321 |
| stroke 13 | 56 % → 61 % | 22.5 px | 0.54 | 1.08 | 416 |
| stroke 14 | 66 % → 67 % | 46.0 px | 0.54 | 1.01 | 425 |
| stroke 15 | 75 % → 75 % | 36.6 px | 0.54 | 1.00 | 105 |
| stroke 16 | 13 % → 13 % | 5.8 px | 0.54 | 1.00 | 24 |

Numbers say: wet paint spreads well beyond the stroke.

## Refs v3 · #19 Guston charcoal hand — own sheet
own sheet 800 × 800 · Charcoal 1.00 · 14 px · 5.4 s

![Refs v3 · #19 Guston charcoal hand — own sheet](Refs-v3-19-Guston-charcoal-hand-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 16 % → 40 % | 12.0 px | 0.82 | 2.50 | 96 |
| stroke 2 | 25 % → 40 % | 18.8 px | 0.82 | 1.62 | 105 |
| stroke 3 | 28 % → 42 % | 20.3 px | 0.82 | 1.47 | 67 |
| stroke 4 | 29 % → 32 % | 20.0 px | 0.82 | 1.09 | 69 |
| stroke 5 | 11 % → 14 % | 21.7 px | 0.82 | 1.25 | 126 |
| stroke 6 | 16 % → 16 % | 22.0 px | 0.82 | 1.00 | 54 |
| stroke 7 | 41 % → 53 % | 24.2 px | 0.82 | 1.29 | 67 |
| stroke 8 | 44 % → 52 % | 65.9 px | 0.82 | 1.17 | 10 |
| stroke 9 | 47 % → 57 % | 69.6 px | 0.82 | 1.22 | 4 |
| stroke 10 | 46 % → 52 % | 68.8 px | 0.82 | 1.13 | 4 |
| stroke 11 | 62 % → 64 % | 93.2 px | 0.82 | 1.02 | 13 |
| stroke 12 | 58 % → 65 % | 86.9 px | 0.82 | 1.11 | 6 |
| stroke 13 | 45 % → 51 % | 66.7 px | 0.82 | 1.15 | 10 |
| stroke 14 | 58 % → 60 % | 86.0 px | 0.82 | 1.04 | 4 |
| stroke 15 | 63 % → 70 % | 94.0 px | 0.82 | 1.11 | 5 |
| stroke 16 | 54 % → 61 % | 80.4 px | 0.82 | 1.14 | 6 |
| stroke 17 | 60 % → 60 % | 89.2 px | 0.82 | 1.00 | 4 |
| stroke 18 | 24 % → 24 % | 22.2 px | 0.82 | 1.00 | 45 |
| stroke 19 | 17 % → 17 % | 20.8 px | 0.82 | 1.00 | 13 |
| stroke 20 | 21 % → 21 % | 25.4 px | 0.82 | 1.00 | 8 |

Numbers say: wet paint spreads well beyond the stroke.

## Refs v3 · #20 Orange crayon — own sheet
own sheet 800 × 1243 · Wax 1.00 · 17 px · 22.9 s

![Refs v3 · #20 Orange crayon — own sheet](Refs-v3-20-Orange-crayon-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 13 % → 68 % | 10.8 px | 0.60 | 5.30 | 1815 |
| stroke 2 | 24 % → 65 % | 12.3 px | 0.60 | 2.68 | 1159 |
| stroke 3 | 38 % → 67 % | 22.2 px | 0.60 | 1.76 | 1285 |
| stroke 4 | 41 % → 72 % | 19.3 px | 0.60 | 1.74 | 1172 |
| stroke 5 | 40 % → 67 % | 17.5 px | 0.60 | 1.65 | 1282 |
| stroke 6 | 54 % → 78 % | 9.1 px | 0.60 | 1.44 | 1638 |
| stroke 7 | 59 % → 64 % | 15.1 px | 0.60 | 1.09 | 1410 |
| stroke 8 | 52 % → 67 % | 24.9 px | 0.60 | 1.28 | 1325 |
| stroke 9 | 62 % → 68 % | 33.6 px | 0.60 | 1.10 | 1280 |
| stroke 10 | 66 % → 66 % | 43.6 px | 0.60 | 1.00 | 1439 |
| stroke 11 | 33 % → 38 % | 33.3 px | 0.60 | 1.17 | 102 |
| stroke 12 | 24 % → 30 % | 39.4 px | 0.60 | 1.23 | 104 |
| stroke 13 | 34 % → 42 % | 23.3 px | 0.60 | 1.26 | 106 |
| stroke 14 | 39 % → 39 % | 37.6 px | 0.60 | 1.00 | 178 |
| stroke 15 | 27 % → 27 % | 9.1 px | 0.60 | 1.00 | 171 |
| stroke 16 | 21 % → 28 % | 30.1 px | 0.59 | 1.35 | 227 |
| stroke 17 | 36 % → 36 % | 22.1 px | 0.60 | 1.00 | 120 |
| stroke 18 | 32 % → 32 % | 34.0 px | 0.60 | 1.00 | 126 |
| stroke 19 | 40 % → 40 % | 37.1 px | 0.60 | 1.00 | 128 |
| stroke 20 | 39 % → 39 % | 45.5 px | 0.60 | 1.00 | 192 |

Numbers say: wet paint spreads well beyond the stroke.

## Refs v3 · #21 Gritty dog contours — own sheet
own sheet 800 × 1131 · Gouache 1.00 + water 15 % · 96 px · 48.4 s

![Refs v3 · #21 Gritty dog contours — own sheet](Refs-v3-21-Gritty-dog-contours-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 12 % → 45 % | 85.1 px | 0.15 | 3.79 | 841 |
| stroke 2 | 24 % → 48 % | 176.3 px | 0.14 | 2.01 | 594 |
| stroke 3 | 30 % → 45 % | 229.6 px | 0.14 | 1.53 | 662 |
| stroke 4 | 30 % → 46 % | 237.2 px | 0.14 | 1.57 | 638 |
| stroke 5 | 22 % → 37 % | 162.0 px | 0.13 | 1.71 | 620 |
| stroke 6 | 29 % → 30 % | 162.9 px | 0.11 | 1.04 | 909 |
| stroke 7 | 37 % → 43 % | 151.5 px | 0.16 | 1.17 | 2158 |
| stroke 8 | 29 % → 31 % | 283.1 px | 0.18 | 1.07 | 315 |
| stroke 9 | 39 % → 41 % | 538.7 px | 0.19 | 1.06 | 261 |
| stroke 10 | 37 % → 39 % | 178.2 px | 0.14 | 1.04 | 751 |
| stroke 11 | 39 % → 40 % | 192.8 px | 0.16 | 1.04 | 478 |
| stroke 12 | 63 % → 63 % | 730.6 px | 0.17 | 1.00 | 66 |
| stroke 13 | 60 % → 60 % | 707.9 px | 0.17 | 1.00 | 81 |
| stroke 14 | 72 % → 72 % | 1161.5 px | 0.15 | 1.01 | 54 |
| stroke 15 | 37 % → 37 % | 150.7 px | 0.18 | 1.00 | 300 |
| stroke 16 | 46 % → 47 % | 256.2 px | 0.14 | 1.01 | 233 |
| stroke 17 | 49 % → 48 % | 270.4 px | 0.12 | 1.00 | 256 |

Numbers say: wet paint spreads well beyond the stroke.

## Refs v3 · #22 Wasilewski brush poster — own sheet
own sheet 800 × 1143 · Ink 0.98 · 24 px · 18.6 s

![Refs v3 · #22 Wasilewski brush poster — own sheet](Refs-v3-22-Wasilewski-brush-poster-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 16 % → 33 % | 24.2 px | 0.92 | 1.99 | 699 |
| stroke 2 | 27 % → 38 % | 27.9 px | 0.93 | 1.42 | 142 |
| stroke 3 | 25 % → 33 % | 52.0 px | 0.92 | 1.33 | 115 |
| stroke 4 | 22 % → 29 % | 24.7 px | 0.89 | 1.36 | 451 |
| stroke 5 | 22 % → 26 % | 47.3 px | 0.92 | 1.18 | 72 |
| stroke 6 | 24 % → 28 % | 55.7 px | 0.91 | 1.20 | 303 |
| stroke 7 | 16 % → 19 % | 35.4 px | 0.90 | 1.23 | 53 |
| stroke 8 | 28 % → 33 % | 62.5 px | 0.88 | 1.18 | 71 |

Numbers say: wet paint spreads well beyond the stroke.

## Refs v3 · #23 Report dry white mask — own sheet
own sheet 800 × 1132 · Ink 0.93 · Gouache 0.07 · 64 px · 31.2 s

![Refs v3 · #23 Report dry white mask — own sheet](Refs-v3-23-Report-dry-white-mask-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 14 % → 40 % | 56.6 px | 0.40 | 2.97 | 452 |
| stroke 2 | 21 % → 53 % | 89.8 px | 0.40 | 2.48 | 477 |
| stroke 3 | 35 % → 69 % | 139.6 px | 0.40 | 1.94 | 521 |
| stroke 4 | 37 % → 57 % | 145.3 px | 0.40 | 1.54 | 731 |
| stroke 5 | 42 % → 46 % | 169.8 px | 0.40 | 1.11 | 642 |
| stroke 6 | 34 % → 36 % | 205.6 px | 0.40 | 1.05 | 201 |
| stroke 7 | 57 % → 61 % | 389.3 px | 0.40 | 1.06 | 161 |
| stroke 8 | 54 % → 55 % | 324.8 px | 0.40 | 1.01 | 241 |
| stroke 9 | 37 % → 37 % | 231.6 px | 0.40 | 1.01 | 178 |
| stroke 10 | 71 % → 72 % | 616.6 px | 0.40 | 1.01 | 67 |
| stroke 11 | 69 % → 73 % | 617.9 px | 0.40 | 1.05 | 45 |
| stroke 12 | 67 % → 67 % | 554.3 px | 0.40 | 1.01 | 66 |
| stroke 13 | 28 % → 30 % | 137.2 px | 0.39 | 1.04 | 325 |

Numbers say: wet paint spreads well beyond the stroke.

## Refs v3 · #24 Picasso flat oil — own sheet
own sheet 800 × 1157 · Gouache 1.00 + turpentine 30 % · 240 px · 96.9 s

![Refs v3 · #24 Picasso flat oil — own sheet](Refs-v3-24-Picasso-flat-oil-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 26 % → 12 % | 124.0 px | 0.14 | 0.45 | 6356 |
| stroke 2 | 47 % → 17 % | 311.4 px | 0.16 | 0.36 | 6035 |
| stroke 3 | 56 % → 24 % | 483.1 px | 0.17 | 0.43 | 6404 |
| stroke 4 | 60 % → 30 % | 532.0 px | 0.17 | 0.50 | 7529 |
| stroke 5 | 67 % → 33 % | 531.3 px | 0.17 | 0.50 | 6395 |
| stroke 6 | 84 % → 38 % | 575.0 px | 0.17 | 0.46 | 7614 |
| stroke 7 | 100 % → 48 % | 480.4 px | 0.17 | 0.48 | 4387 |
| stroke 8 | 4 % → 34 % | 71.7 px | 0.17 | 7.95 | 830 |
| stroke 9 | 7 % → 32 % | 144.4 px | 0.17 | 4.35 | 913 |
| stroke 10 | 10 % → 31 % | 274.0 px | 0.17 | 3.19 | 563 |
| stroke 11 | 12 % → 31 % | 313.8 px | 0.17 | 2.50 | 425 |
| stroke 12 | 18 % → 33 % | 318.4 px | 0.17 | 1.87 | 574 |
| stroke 13 | 22 % → 34 % | 314.0 px | 0.16 | 1.54 | 723 |
| stroke 14 | 43 % → 43 % | 280.4 px | 0.17 | 0.98 | 1503 |
| stroke 15 | 54 % → 48 % | 259.4 px | 0.17 | 0.88 | 926 |
| stroke 16 | 31 % → 29 % | 223.2 px | 0.16 | 0.91 | 1077 |
| stroke 17 | 25 % → 20 % | 188.0 px | 0.16 | 0.79 | 1049 |
| stroke 18 | 19 % → 11 % | 256.5 px | 0.15 | 0.59 | 601 |
| stroke 19 | 35 % → 28 % | 337.1 px | 0.16 | 0.80 | 753 |
| stroke 20 | 40 % → 31 % | 314.7 px | 0.17 | 0.79 | 858 |

Numbers say: wet paint spreads well beyond the stroke.

## Refs v3 · #25 Yellow heavy stroke — own sheet
own sheet 800 × 1198 · Impasto 1.00 · 160 px · 11.3 s

![Refs v3 · #25 Yellow heavy stroke — own sheet](Refs-v3-25-Yellow-heavy-stroke-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 15 % → 6 % | 127.2 px | 0.14 | 0.39 | 3763 |

## Refs v3 · #26 Ink caricature — own sheet
own sheet 800 × 1066 · Ink 0.98 · 20 px · 16.2 s

![Refs v3 · #26 Ink caricature — own sheet](Refs-v3-26-Ink-caricature-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 15 % → 25 % | 18.4 px | 0.86 | 1.71 | 215 |
| stroke 2 | 15 % → 23 % | 19.2 px | 0.86 | 1.48 | 166 |
| stroke 3 | 11 % → 15 % | 20.3 px | 0.85 | 1.42 | 98 |
| stroke 4 | 10 % → 14 % | 20.2 px | 0.85 | 1.39 | 134 |
| stroke 5 | 21 % → 27 % | 39.6 px | 0.86 | 1.28 | 104 |
| stroke 6 | 12 % → 41 % | 20.1 px | 0.84 | 3.42 | 55 |
| stroke 7 | 28 % → 54 % | 43.8 px | 0.84 | 1.94 | 51 |
| stroke 8 | 22 % → 50 % | 34.5 px | 0.84 | 2.28 | 51 |
| stroke 9 | 24 % → 48 % | 38.0 px | 0.83 | 2.00 | 47 |
| stroke 10 | 24 % → 42 % | 39.4 px | 0.83 | 1.71 | 60 |
| stroke 11 | 15 % → 41 % | 25.6 px | 0.84 | 2.68 | 55 |
| stroke 12 | 25 % → 46 % | 36.6 px | 0.84 | 1.88 | 68 |
| stroke 13 | 20 % → 47 % | 29.8 px | 0.84 | 2.38 | 58 |
| stroke 14 | 25 % → 34 % | 37.2 px | 0.84 | 1.38 | 51 |
| stroke 15 | 16 % → 19 % | 40.0 px | 0.85 | 1.22 | 225 |

Numbers say: wet paint spreads well beyond the stroke.

## Refs v3 · #27 Orange impasto swatch — own sheet
own sheet 800 × 1000 · Impasto 1.00 · 64 px · 13.9 s

![Refs v3 · #27 Orange impasto swatch — own sheet](Refs-v3-27-Orange-impasto-swatch-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 6 % → 36 % | 62.6 px | 0.35 | 5.89 | 160 |
| stroke 2 | 10 % → 40 % | 83.7 px | 0.35 | 4.05 | 216 |
| stroke 3 | 7 % → 29 % | 59.0 px | 0.34 | 4.36 | 212 |
| stroke 4 | 15 % → 17 % | 146.0 px | 0.36 | 1.08 | 166 |
| stroke 5 | 22 % → 43 % | 210.2 px | 0.34 | 1.99 | 125 |
| stroke 6 | 24 % → 38 % | 209.9 px | 0.34 | 1.63 | 223 |
| stroke 7 | 17 % → 18 % | 164.8 px | 0.33 | 1.04 | 131 |
| stroke 8 | 25 % → 41 % | 227.5 px | 0.36 | 1.65 | 162 |
| stroke 9 | 30 % → 46 % | 267.0 px | 0.35 | 1.51 | 211 |
| stroke 10 | 19 % → 26 % | 191.4 px | 0.35 | 1.36 | 126 |
| stroke 11 | 35 % → 46 % | 266.3 px | 0.35 | 1.31 | 264 |
| stroke 12 | 33 % → 34 % | 357.0 px | 0.34 | 1.01 | 111 |
| stroke 13 | 41 % → 41 % | 352.7 px | 0.35 | 1.00 | 126 |
| stroke 14 | 41 % → 40 % | 410.5 px | 0.34 | 0.98 | 172 |

Numbers say: wet paint spreads well beyond the stroke.

## Refs v3 · #28 Miles Davis lines — own sheet
own sheet 800 × 800 · Ink 0.93 · Gouache 0.07 · 24 px · 20.9 s

![Refs v3 · #28 Miles Davis lines — own sheet](Refs-v3-28-Miles-Davis-lines-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 15 % → 40 % | 21.7 px | 0.85 | 2.60 | 419 |
| stroke 2 | 49 % → 67 % | 65.4 px | 0.86 | 1.35 | 201 |
| stroke 3 | 29 % → 37 % | 32.4 px | 0.85 | 1.30 | 266 |
| stroke 4 | 21 % → 41 % | 31.0 px | 0.83 | 1.95 | 129 |
| stroke 5 | 26 % → 48 % | 38.2 px | 0.85 | 1.86 | 123 |
| stroke 6 | 26 % → 48 % | 34.2 px | 0.84 | 1.84 | 133 |
| stroke 7 | 20 % → 28 % | 37.9 px | 0.84 | 1.37 | 190 |
| stroke 8 | 13 % → 16 % | 20.5 px | 0.81 | 1.27 | 300 |
| stroke 9 | 13 % → 16 % | 22.5 px | 0.85 | 1.23 | 279 |
| stroke 10 | 17 % → 21 % | 34.8 px | 0.82 | 1.29 | 129 |

Numbers say: wet paint spreads well beyond the stroke.

## Refs v3 · #29 Shrigley asterisk — own sheet
own sheet 800 × 1082 · Watercolour 1.00 + water 50 % · 72 px · 25.3 s

![Refs v3 · #29 Shrigley asterisk — own sheet](Refs-v3-29-Shrigley-asterisk-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 23 % → 53 % | 96.6 px | 0.67 | 2.30 | 789 |
| stroke 2 | 20 % → 36 % | 174.7 px | 0.67 | 1.83 | 888 |
| stroke 3 | 37 % → 44 % | 183.2 px | 0.68 | 1.21 | 1146 |
| stroke 4 | 37 % → 37 % | 320.0 px | 0.67 | 1.00 | 1137 |

Numbers say: wet paint spreads well beyond the stroke.

## Refs v3 · #30 Red gouache face — own sheet
own sheet 800 × 1085 · Gouache 1.00 + water 15 % · 80 px · 47.1 s

![Refs v3 · #30 Red gouache face — own sheet](Refs-v3-30-Red-gouache-face-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 15 % → 34 % | 70.0 px | 0.57 | 2.30 | 626 |
| stroke 2 | 24 % → 36 % | 131.4 px | 0.57 | 1.50 | 641 |
| stroke 3 | 21 % → 37 % | 109.7 px | 0.59 | 1.82 | 955 |
| stroke 4 | 25 % → 42 % | 139.5 px | 0.59 | 1.68 | 824 |
| stroke 5 | 26 % → 40 % | 136.4 px | 0.59 | 1.54 | 1112 |
| stroke 6 | 25 % → 41 % | 147.1 px | 0.58 | 1.61 | 1061 |
| stroke 7 | 24 % → 40 % | 139.0 px | 0.58 | 1.65 | 917 |
| stroke 8 | 29 % → 30 % | 131.6 px | 0.58 | 1.06 | 920 |
| stroke 9 | 35 % → 36 % | 168.2 px | 0.58 | 1.05 | 1244 |
| stroke 10 | 33 % → 33 % | 160.6 px | 0.57 | 1.01 | 524 |
| stroke 11 | 46 % → 50 % | 608.6 px | 0.60 | 1.09 | 88 |
| stroke 12 | 42 % → 43 % | 551.0 px | 0.59 | 1.04 | 62 |
| stroke 13 | 62 % → 65 % | 1033.1 px | 0.60 | 1.06 | 64 |
| stroke 14 | 55 % → 57 % | 927.6 px | 0.59 | 1.03 | 55 |
| stroke 15 | 61 % → 62 % | 526.9 px | 0.58 | 1.01 | 136 |
| stroke 16 | 58 % → 57 % | 630.7 px | 0.58 | 0.99 | 90 |
| stroke 17 | 49 % → 49 % | 458.1 px | 0.58 | 1.01 | 62 |
| stroke 18 | 47 % → 48 % | 441.9 px | 0.58 | 1.02 | 51 |

Numbers say: wet paint spreads well beyond the stroke.

## Refs v3 · #31 Warhol blotted line — own sheet
own sheet 800 × 709 · Ink 0.98 · 6 px · 16.8 s

![Refs v3 · #31 Warhol blotted line — own sheet](Refs-v3-31-Warhol-blotted-line-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 2 % → 12 % | 8.0 px | 0.82 | 5.79 | 387 |
| stroke 2 | 5 % → 15 % | 13.6 px | 0.81 | 3.07 | 247 |
| stroke 3 | 22 % → 55 % | 8.2 px | 0.82 | 2.45 | 234 |
| stroke 4 | 24 % → 53 % | 8.6 px | 0.83 | 2.17 | 241 |
| stroke 5 | 54 % → 78 % | 30.6 px | 0.83 | 1.44 | 17 |
| stroke 6 | 52 % → 73 % | 29.5 px | 0.82 | 1.39 | 15 |
| stroke 7 | 51 % → 76 % | 28.9 px | 0.81 | 1.47 | 20 |
| stroke 8 | 52 % → 72 % | 29.0 px | 0.81 | 1.40 | 14 |
| stroke 9 | 48 % → 69 % | 27.3 px | 0.83 | 1.43 | 17 |
| stroke 10 | 49 % → 69 % | 27.5 px | 0.83 | 1.42 | 17 |
| stroke 11 | 47 % → 67 % | 26.6 px | 0.82 | 1.42 | 14 |
| stroke 12 | 47 % → 63 % | 26.4 px | 0.83 | 1.34 | 14 |
| stroke 13 | 48 % → 63 % | 26.8 px | 0.83 | 1.33 | 18 |
| stroke 14 | 45 % → 65 % | 25.6 px | 0.82 | 1.44 | 16 |
| stroke 15 | 44 % → 56 % | 24.6 px | 0.83 | 1.28 | 20 |
| stroke 16 | 43 % → 58 % | 24.1 px | 0.82 | 1.36 | 16 |
| stroke 17 | 40 % → 56 % | 22.4 px | 0.80 | 1.41 | 13 |
| stroke 18 | 40 % → 53 % | 22.7 px | 0.83 | 1.31 | 22 |
| stroke 19 | 35 % → 54 % | 19.7 px | 0.80 | 1.54 | 20 |
| stroke 20 | 33 % → 56 % | 18.8 px | 0.81 | 1.69 | 29 |
| stroke 21 | 27 % → 37 % | 21.5 px | 0.82 | 1.40 | 91 |
| stroke 22 | 23 % → 36 % | 18.5 px | 0.81 | 1.54 | 81 |
| stroke 23 | 20 % → 33 % | 16.2 px | 0.79 | 1.66 | 67 |
| stroke 24 | 16 % → 29 % | 12.8 px | 0.81 | 1.81 | 143 |
| stroke 25 | 14 % → 28 % | 11.5 px | 0.76 | 1.97 | 89 |
| stroke 26 | 17 % → 23 % | 15.5 px | 0.83 | 1.38 | 266 |

Numbers say: wet paint spreads well beyond the stroke.

## Refs v3 · #32 Thick orange swipes — own sheet
own sheet 800 × 800 · Gouache 0.85 · Ink 0.15 + turpentine 50 % · 240 px · 47.3 s

![Refs v3 · #32 Thick orange swipes — own sheet](Refs-v3-32-Thick-orange-swipes-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 23 % → 16 % | 103.2 px | 0.09 | 0.72 | 4368 |
| stroke 2 | 42 % → 19 % | 240.4 px | 0.10 | 0.45 | 6396 |
| stroke 3 | 56 % → 56 % | 403.5 px | 0.10 | 1.00 | 6466 |
| stroke 4 | 72 % → 72 % | 128.8 px | 0.10 | 1.00 | 6619 |
| stroke 5 | 90 % → 19 % | 550.8 px | 0.10 | 0.21 | 6743 |
| stroke 6 | 100 % → 17 % | 462.9 px | 0.11 | 0.17 | 4626 |
| stroke 7 | 7 % → 17 % | 113.3 px | 0.10 | 2.46 | 882 |
| stroke 8 | 12 % → 15 % | 238.0 px | 0.10 | 1.29 | 903 |
| stroke 9 | 19 % → 17 % | 351.8 px | 0.10 | 0.87 | 961 |

Numbers say: wet paint spreads well beyond the stroke.

## Refs v3 · #33 Red wet-in-wet flames — own sheet
own sheet 800 × 1083 · Watercolour 1.00 + water 60 % · 96 px · 43.2 s

![Refs v3 · #33 Red wet-in-wet flames — own sheet](Refs-v3-33-Red-wet-in-wet-flames-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 25 % → 59 % | 102.5 px | 0.38 | 2.34 | 1725 |
| stroke 2 | 29 % → 58 % | 142.0 px | 0.28 | 2.01 | 401 |
| stroke 3 | 31 % → 58 % | 260.5 px | 0.28 | 1.87 | 514 |
| stroke 4 | 37 % → 61 % | 256.7 px | 0.27 | 1.66 | 572 |
| stroke 5 | 38 % → 60 % | 361.1 px | 0.27 | 1.56 | 263 |
| stroke 6 | 37 % → 58 % | 325.2 px | 0.26 | 1.56 | 351 |
| stroke 7 | 35 % → 56 % | 205.9 px | 0.24 | 1.58 | 458 |
| stroke 8 | 41 % → 53 % | 206.3 px | 0.25 | 1.28 | 527 |

Numbers say: wet paint spreads well beyond the stroke.

## Refs v3 · #34 Magenta oil patches — own sheet
own sheet 800 × 1422 · Gouache 1.00 + turpentine 15 % · 96 px · 70.0 s

![Refs v3 · #34 Magenta oil patches — own sheet](Refs-v3-34-Magenta-oil-patches-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 9 % → 57 % | 87.5 px | 0.32 | 6.73 | 340 |
| stroke 2 | 18 % → 38 % | 154.8 px | 0.26 | 2.15 | 422 |
| stroke 3 | 21 % → 61 % | 228.6 px | 0.32 | 2.92 | 350 |
| stroke 4 | 23 % → 42 % | 262.2 px | 0.25 | 1.83 | 360 |
| stroke 5 | 9 % → 53 % | 91.2 px | 0.27 | 6.01 | 165 |
| stroke 6 | 17 % → 67 % | 176.7 px | 0.34 | 3.93 | 172 |
| stroke 7 | 23 % → 57 % | 217.1 px | 0.32 | 2.47 | 438 |
| stroke 8 | 37 % → 55 % | 356.3 px | 0.32 | 1.51 | 636 |
| stroke 9 | 30 % → 56 % | 367.8 px | 0.31 | 1.88 | 403 |
| stroke 10 | 48 % → 66 % | 511.0 px | 0.31 | 1.38 | 420 |
| stroke 11 | 52 % → 69 % | 587.7 px | 0.32 | 1.31 | 356 |
| stroke 12 | 45 % → 53 % | 474.1 px | 0.32 | 1.17 | 543 |
| stroke 13 | 54 % → 64 % | 384.7 px | 0.32 | 1.19 | 539 |
| stroke 14 | 65 % → 68 % | 535.0 px | 0.34 | 1.05 | 702 |
| stroke 15 | 12 % → 32 % | 131.7 px | 0.24 | 2.78 | 398 |
| stroke 16 | 18 % → 36 % | 154.3 px | 0.23 | 1.97 | 364 |
| stroke 17 | 12 % → 48 % | 94.6 px | 0.36 | 3.88 | 385 |
| stroke 18 | 26 % → 41 % | 239.8 px | 0.36 | 1.60 | 344 |
| stroke 19 | 44 % → 49 % | 487.2 px | 0.31 | 1.12 | 374 |
| stroke 20 | 56 % → 56 % | 573.7 px | 0.31 | 1.00 | 439 |
| stroke 21 | 34 % → 53 % | 172.8 px | 0.30 | 1.54 | 456 |
| stroke 22 | 43 % → 52 % | 314.9 px | 0.36 | 1.20 | 521 |
| stroke 23 | 12 % → 53 % | 73.1 px | 0.40 | 4.56 | 316 |
| stroke 24 | 34 % → 69 % | 131.2 px | 0.37 | 2.02 | 415 |
| stroke 25 | 32 % → 47 % | 405.8 px | 0.36 | 1.46 | 274 |
| stroke 26 | 49 % → 57 % | 411.8 px | 0.36 | 1.17 | 382 |
| stroke 27 | 37 % → 38 % | 472.0 px | 0.32 | 1.02 | 440 |
| stroke 28 | 55 % → 54 % | 678.4 px | 0.32 | 0.99 | 381 |
| stroke 29 | 36 % → 45 % | 159.3 px | 0.33 | 1.24 | 251 |
| stroke 30 | 39 % → 40 % | 360.9 px | 0.38 | 1.01 | 459 |
| stroke 31 | 42 % → 45 % | 319.2 px | 0.30 | 1.09 | 441 |
| stroke 32 | 60 % → 60 % | 448.2 px | 0.33 | 0.99 | 603 |

Numbers say: wet paint spreads well beyond the stroke.

## Refs v3 · #35 Red band with runs — own sheet
own sheet 800 × 1191 · Watercolour 1.00 + water 75 % · 88 px · 32.0 s

![Refs v3 · #35 Red band with runs — own sheet](Refs-v3-35-Red-band-with-runs-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 39 % → 47 % | 148.5 px | 0.32 | 1.20 | 1380 |

## Refs v3 · #36 Magenta letters flat — own sheet
own sheet 800 × 1000 · Gouache 1.00 + water 15 % · 44 px · 35.9 s

![Refs v3 · #36 Magenta letters flat — own sheet](Refs-v3-36-Magenta-letters-flat-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 13 % → 17 % | 44.8 px | 0.50 | 1.28 | 225 |
| stroke 2 | 16 % → 24 % | 42.3 px | 0.50 | 1.52 | 158 |
| stroke 3 | 24 % → 33 % | 80.6 px | 0.51 | 1.39 | 154 |
| stroke 4 | 17 % → 26 % | 39.3 px | 0.54 | 1.52 | 1079 |
| stroke 5 | 18 % → 30 % | 61.7 px | 0.52 | 1.64 | 481 |
| stroke 6 | 31 % → 33 % | 191.2 px | 0.52 | 1.05 | 106 |
| stroke 7 | 21 % → 25 % | 47.4 px | 0.51 | 1.18 | 718 |
| stroke 8 | 19 % → 33 % | 69.2 px | 0.54 | 1.80 | 424 |
| stroke 9 | 27 % → 29 % | 123.7 px | 0.54 | 1.08 | 173 |
| stroke 10 | 19 % → 34 % | 63.8 px | 0.52 | 1.81 | 280 |
| stroke 11 | 31 % → 37 % | 189.3 px | 0.53 | 1.18 | 80 |
| stroke 12 | 26 % → 32 % | 58.0 px | 0.52 | 1.25 | 388 |
| stroke 13 | 19 % → 26 % | 74.8 px | 0.53 | 1.40 | 121 |
| stroke 14 | 23 % → 37 % | 95.0 px | 0.52 | 1.63 | 122 |
| stroke 15 | 19 % → 28 % | 65.9 px | 0.51 | 1.47 | 253 |
| stroke 16 | 32 % → 33 % | 196.0 px | 0.50 | 1.05 | 59 |
| stroke 17 | 26 % → 32 % | 58.7 px | 0.52 | 1.22 | 475 |
| stroke 18 | 18 % → 23 % | 72.8 px | 0.51 | 1.30 | 111 |
| stroke 19 | 26 % → 26 % | 90.5 px | 0.51 | 1.02 | 105 |
| stroke 20 | 22 % → 22 % | 75.9 px | 0.52 | 1.03 | 177 |
| stroke 21 | 24 % → 23 % | 61.8 px | 0.52 | 0.97 | 460 |

Numbers say: wet paint spreads well beyond the stroke.

## Refs v3 · #37 Oil still life — own sheet
own sheet 800 × 812 · Gouache 1.00 + turpentine 30 % · 240 px · 62.3 s

![Refs v3 · #37 Oil still life — own sheet](Refs-v3-37-Oil-still-life-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 24 % → 15 % | 110.6 px | 0.31 | 0.60 | 4488 |
| stroke 2 | 41 % → 16 % | 233.3 px | 0.26 | 0.38 | 6508 |
| stroke 3 | 49 % → 15 % | 358.6 px | 0.26 | 0.31 | 6907 |
| stroke 4 | 62 % → 62 % | 493.9 px | 0.26 | 1.00 | 5940 |
| stroke 5 | 77 % → 15 % | 556.3 px | 0.26 | 0.20 | 5177 |
| stroke 6 | 93 % → 18 % | 564.3 px | 0.26 | 0.19 | 4675 |
| stroke 7 | 100 % → 18 % | 466.2 px | 0.26 | 0.18 | 3526 |
| stroke 8 | 3 % → 14 % | 27.0 px | 0.26 | 4.65 | 642 |
| stroke 9 | 5 % → 18 % | 242.2 px | 0.26 | 3.94 | 80 |
| stroke 10 | 4 % → 15 % | 200.3 px | 0.26 | 3.32 | 133 |
| stroke 11 | 9 % → 14 % | 56.0 px | 0.26 | 1.59 | 690 |
| stroke 12 | 11 % → 17 % | 357.4 px | 0.26 | 1.59 | 66 |
| stroke 13 | 10 % → 16 % | 355.4 px | 0.26 | 1.59 | 75 |
| stroke 14 | 10 % → 16 % | 353.9 px | 0.26 | 1.59 | 82 |
| stroke 15 | 9 % → 15 % | 356.2 px | 0.26 | 1.59 | 77 |
| stroke 16 | 10 % → 14 % | 278.3 px | 0.26 | 1.37 | 120 |
| stroke 17 | 13 % → 15 % | 384.5 px | 0.26 | 1.24 | 91 |
| stroke 18 | 15 % → 17 % | 490.2 px | 0.26 | 1.14 | 83 |
| stroke 19 | 17 % → 18 % | 493.2 px | 0.26 | 1.05 | 88 |
| stroke 20 | 15 % → 14 % | 116.4 px | 0.26 | 0.95 | 387 |
| stroke 21 | 16 % → 16 % | 2694.7 px | 0.26 | 0.95 | 24 |
| stroke 22 | 17 % → 16 % | 2695.3 px | 0.26 | 0.95 | 32 |
| stroke 23 | 18 % → 17 % | 2693.2 px | 0.26 | 0.95 | 17 |
| stroke 24 | 23 % → 22 % | 686.3 px | 0.27 | 0.93 | 82 |
| stroke 25 | 21 % → 19 % | 759.3 px | 0.26 | 0.90 | 49 |

Numbers say: wet paint spreads well beyond the stroke.

## Refs v3 · #38 Sanguine drawing — own sheet
own sheet 800 × 1094 · Charcoal 0.50 · Pastel 0.50 · 4 px · 7.4 s

![Refs v3 · #38 Sanguine drawing — own sheet](Refs-v3-38-Sanguine-drawing-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 4 % → 10 % | 6.5 px | 0.61 | 2.86 | 126 |
| stroke 2 | 12 % → 20 % | 6.0 px | 0.61 | 1.68 | 39 |
| stroke 3 | 6 % → 12 % | 7.6 px | 0.61 | 1.84 | 95 |
| stroke 4 | 18 % → 18 % | 13.3 px | 0.61 | 1.00 | 4 |
| stroke 5 | 10 % → 10 % | 7.1 px | 0.61 | 1.00 | 7 |
| stroke 6 | 10 % → 23 % | 6.9 px | 0.61 | 2.33 | 5 |
| stroke 7 | 22 % → 22 % | 15.8 px | 0.61 | 1.00 | 3 |
| stroke 8 | 19 % → 28 % | 13.0 px | 0.61 | 1.47 | 4 |
| stroke 9 | 20 % → 34 % | 15.1 px | 0.61 | 1.66 | 2 |
| stroke 10 | 8 % → 8 % | 6.4 px | 0.61 | 1.00 | 4 |
| stroke 11 | 19 % → 19 % | 14.5 px | 0.61 | 1.00 | 4 |
| stroke 12 | 10 % → 10 % | 7.2 px | 0.60 | 1.00 | 3 |
| stroke 13 | 9 % → 15 % | 6.7 px | 0.61 | 1.66 | 4 |
| stroke 14 | 9 % → 12 % | 6.6 px | 0.61 | 1.40 | 6 |
| stroke 15 | 20 % → 20 % | 14.2 px | 0.61 | 1.00 | 5 |
| stroke 16 | 19 % → 19 % | 14.1 px | 0.61 | 1.00 | 4 |
| stroke 17 | 22 % → 22 % | 14.5 px | 0.61 | 1.00 | 3 |
| stroke 18 | 9 % → 12 % | 6.6 px | 0.60 | 1.37 | 5 |
| stroke 19 | 24 % → 26 % | 18.1 px | 0.61 | 1.08 | 4 |
| stroke 20 | 9 % → 9 % | 6.7 px | 0.61 | 1.00 | 2 |
| stroke 21 | 24 % → 24 % | 17.1 px | 0.61 | 1.00 | 3 |
| stroke 22 | 9 % → 23 % | 6.7 px | 0.61 | 2.40 | 4 |
| stroke 23 | 9 % → 11 % | 6.4 px | 0.61 | 1.29 | 3 |
| stroke 24 | 10 % → 10 % | 7.1 px | 0.61 | 1.00 | 4 |
| stroke 25 | 9 % → 17 % | 6.4 px | 0.61 | 1.94 | 3 |
| stroke 26 | 9 % → 16 % | 6.8 px | 0.61 | 1.78 | 2 |
| stroke 27 | 10 % → 10 % | 6.9 px | 0.61 | 1.00 | 3 |
| stroke 28 | 9 % → 9 % | 7.0 px | 0.61 | 1.00 | 4 |
| stroke 29 | 25 % → 25 % | 18.0 px | 0.61 | 1.00 | 3 |
| stroke 30 | 9 % → 9 % | 6.6 px | 0.61 | 1.00 | 5 |
| stroke 31 | 16 % → 16 % | 11.0 px | 0.61 | 1.00 | 3 |
| stroke 32 | 9 % → 9 % | 6.7 px | 0.61 | 1.00 | 3 |
| stroke 33 | 12 % → 12 % | 8.8 px | 0.61 | 1.00 | 5 |
| stroke 34 | 18 % → 24 % | 14.5 px | 0.61 | 1.30 | 7 |
| stroke 35 | 9 % → 9 % | 6.6 px | 0.61 | 1.00 | 5 |
| stroke 36 | 11 % → 11 % | 8.0 px | 0.61 | 1.00 | 2 |
| stroke 37 | 14 % → 15 % | 10.1 px | 0.61 | 1.10 | 4 |
| stroke 38 | 9 % → 9 % | 6.8 px | 0.61 | 1.00 | 2 |
| stroke 39 | 9 % → 9 % | 6.8 px | 0.61 | 1.00 | 3 |
| stroke 40 | 15 % → 15 % | 10.9 px | 0.61 | 1.00 | 4 |
| stroke 41 | 14 % → 14 % | 10.3 px | 0.61 | 1.00 | 3 |
| stroke 42 | 20 % → 22 % | 15.0 px | 0.61 | 1.10 | 4 |
| stroke 43 | 10 % → 26 % | 6.8 px | 0.61 | 2.76 | 8 |
| stroke 44 | 10 % → 10 % | 6.9 px | 0.61 | 1.00 | 8 |
| stroke 45 | 16 % → 20 % | 12.9 px | 0.61 | 1.22 | 11 |
| stroke 46 | 18 % → 19 % | 13.6 px | 0.61 | 1.07 | 5 |
| stroke 47 | 9 % → 12 % | 6.3 px | 0.61 | 1.41 | 3 |
| stroke 48 | 9 % → 9 % | 6.5 px | 0.61 | 1.00 | 5 |
| stroke 49 | 10 % → 10 % | 7.0 px | 0.61 | 1.00 | 5 |
| stroke 50 | 28 % → 28 % | 20.5 px | 0.61 | 1.00 | 3 |
| stroke 51 | 22 % → 22 % | 15.4 px | 0.61 | 1.00 | 4 |
| stroke 52 | 9 % → 14 % | 6.7 px | 0.61 | 1.48 | 2 |
| stroke 53 | 15 % → 15 % | 12.0 px | 0.61 | 1.00 | 7 |
| stroke 54 | 9 % → 9 % | 6.8 px | 0.61 | 1.00 | 5 |
| stroke 55 | 9 % → 9 % | 6.6 px | 0.61 | 1.00 | 4 |
| stroke 56 | 15 % → 15 % | 10.4 px | 0.61 | 1.00 | 4 |
| stroke 57 | 9 % → 9 % | 6.6 px | 0.61 | 1.00 | 6 |
| stroke 58 | 13 % → 13 % | 9.8 px | 0.61 | 1.00 | 6 |
| stroke 59 | 13 % → 13 % | 9.5 px | 0.60 | 1.00 | 3 |
| stroke 60 | 9 % → 9 % | 6.8 px | 0.61 | 1.00 | 3 |
| stroke 61 | 17 % → 27 % | 12.6 px | 0.61 | 1.55 | 8 |
| stroke 62 | 19 % → 19 % | 13.6 px | 0.61 | 1.00 | 2 |
| stroke 63 | 12 % → 12 % | 9.1 px | 0.61 | 1.00 | 4 |
| stroke 64 | 8 % → 8 % | 16.5 px | 0.61 | 1.00 | 54 |
| stroke 65 | 10 % → 10 % | 6.6 px | 0.61 | 1.00 | 19 |

Numbers say: wet paint spreads well beyond the stroke.

## Refs v3 · #39 Thick impasto weave — own sheet
own sheet 800 × 1067 · Impasto 1.00 · 64 px · 24.9 s

![Refs v3 · #39 Thick impasto weave — own sheet](Refs-v3-39-Thick-impasto-weave-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 14 % → 62 % | 57.9 px | 0.34 | 4.52 | 424 |
| stroke 2 | 19 % → 43 % | 74.6 px | 0.35 | 2.23 | 879 |
| stroke 3 | 19 % → 25 % | 78.6 px | 0.28 | 1.34 | 701 |
| stroke 4 | 38 % → 49 % | 152.1 px | 0.36 | 1.27 | 916 |
| stroke 5 | 20 % → 18 % | 84.7 px | 0.21 | 0.91 | 811 |
| stroke 6 | 37 % → 41 % | 155.3 px | 0.34 | 1.10 | 970 |
| stroke 7 | 28 % → 55 % | 130.7 px | 0.34 | 1.98 | 667 |
| stroke 8 | 23 % → 16 % | 72.3 px | 0.21 | 0.68 | 1041 |
| stroke 9 | 30 % → 22 % | 142.1 px | 0.21 | 0.74 | 666 |
| stroke 10 | 41 % → 33 % | 143.5 px | 0.35 | 0.80 | 815 |
| stroke 11 | 48 % → 52 % | 159.4 px | 0.35 | 1.08 | 901 |
| stroke 12 | 45 % → 27 % | 162.9 px | 0.26 | 0.60 | 666 |
| stroke 13 | 60 % → 47 % | 273.3 px | 0.35 | 0.78 | 445 |
| stroke 14 | 50 % → 30 % | 188.6 px | 0.31 | 0.59 | 786 |
| stroke 15 | 40 % → 21 % | 146.6 px | 0.20 | 0.53 | 437 |
| stroke 16 | 73 % → 43 % | 349.9 px | 0.36 | 0.59 | 480 |
| stroke 17 | 70 % → 66 % | 367.2 px | 0.33 | 0.94 | 505 |
| stroke 18 | 44 % → 24 % | 183.3 px | 0.23 | 0.55 | 673 |

Numbers say: wet paint spreads well beyond the stroke.

## Refs v3 · #40 Watercolour blooms — own sheet
own sheet 800 × 1170 · Watercolour 1.00 + water 55 % · 96 px · 38.6 s

![Refs v3 · #40 Watercolour blooms — own sheet](Refs-v3-40-Watercolour-blooms-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 26 % → 49 % | 93.5 px | 0.25 | 1.85 | 2717 |
| stroke 2 | 25 % → 32 % | 122.5 px | 0.22 | 1.28 | 1182 |
| stroke 3 | 11 % → 27 % | 53.7 px | 0.61 | 2.58 | 253 |
| stroke 4 | 35 % → 46 % | 296.9 px | 0.44 | 1.33 | 130 |

Numbers say: wet paint spreads well beyond the stroke.

## Refs v3 · #41 Coloured pencil — own sheet
own sheet 800 × 1107 · Charcoal 0.50 · Pastel 0.50 · 3 px · 14.4 s

![Refs v3 · #41 Coloured pencil — own sheet](Refs-v3-41-Coloured-pencil-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 18 % → 46 % | 5.0 px | 0.37 | 2.57 | 108 |
| stroke 2 | 22 % → 51 % | 4.9 px | 0.34 | 2.29 | 105 |
| stroke 3 | 20 % → 57 % | 4.8 px | 0.36 | 2.82 | 90 |
| stroke 4 | 17 % → 52 % | 5.0 px | 0.36 | 3.04 | 109 |
| stroke 5 | 22 % → 42 % | 4.9 px | 0.38 | 1.87 | 89 |
| stroke 6 | 17 % → 53 % | 4.8 px | 0.36 | 3.08 | 109 |
| stroke 7 | 21 % → 50 % | 5.0 px | 0.36 | 2.42 | 90 |
| stroke 8 | 14 % → 32 % | 4.8 px | 0.36 | 2.37 | 90 |
| stroke 9 | 25 % → 35 % | 7.3 px | 0.38 | 1.37 | 100 |
| stroke 10 | 15 % → 47 % | 4.9 px | 0.36 | 3.07 | 97 |
| stroke 11 | 18 % → 41 % | 6.0 px | 0.37 | 2.27 | 89 |
| stroke 12 | 14 % → 14 % | 5.1 px | 0.35 | 1.00 | 101 |
| stroke 13 | 21 % → 40 % | 5.1 px | 0.36 | 1.91 | 86 |
| stroke 14 | 18 % → 34 % | 5.7 px | 0.36 | 1.85 | 109 |
| stroke 15 | 43 % → 63 % | 11.1 px | 0.36 | 1.47 | 112 |
| stroke 16 | 45 % → 56 % | 9.0 px | 0.36 | 1.26 | 101 |
| stroke 17 | 18 % → 37 % | 4.8 px | 0.35 | 2.11 | 92 |
| stroke 18 | 33 % → 55 % | 7.3 px | 0.36 | 1.65 | 105 |
| stroke 19 | 25 % → 47 % | 8.2 px | 0.37 | 1.88 | 94 |
| stroke 20 | 15 % → 33 % | 4.9 px | 0.36 | 2.17 | 97 |
| stroke 21 | 15 % → 52 % | 4.9 px | 0.35 | 3.41 | 98 |
| stroke 22 | 32 % → 63 % | 10.4 px | 0.36 | 1.99 | 89 |
| stroke 23 | 43 % → 48 % | 13.8 px | 0.37 | 1.12 | 92 |
| stroke 24 | 37 % → 55 % | 8.9 px | 0.36 | 1.46 | 136 |
| stroke 25 | 27 % → 35 % | 9.6 px | 0.38 | 1.26 | 146 |
| stroke 26 | 18 % → 28 % | 5.0 px | 0.39 | 1.60 | 131 |
| stroke 27 | 21 % → 29 % | 4.6 px | 0.37 | 1.38 | 122 |
| stroke 28 | 17 % → 42 % | 5.1 px | 0.36 | 2.44 | 122 |
| stroke 29 | 28 % → 52 % | 9.4 px | 0.36 | 1.82 | 116 |
| stroke 30 | 36 % → 38 % | 8.8 px | 0.34 | 1.05 | 140 |
| stroke 31 | 47 % → 51 % | 13.2 px | 0.36 | 1.07 | 119 |
| stroke 32 | 45 % → 48 % | 15.8 px | 0.36 | 1.07 | 131 |
| stroke 33 | 32 % → 38 % | 11.0 px | 0.36 | 1.16 | 146 |
| stroke 34 | 41 % → 50 % | 12.9 px | 0.36 | 1.21 | 126 |
| stroke 35 | 18 % → 33 % | 4.7 px | 0.38 | 1.81 | 109 |
| stroke 36 | 22 % → 22 % | 2.6 px | 0.34 | 1.00 | 166 |
| stroke 37 | 61 % → 65 % | 12.1 px | 0.36 | 1.07 | 121 |
| stroke 38 | 45 % → 47 % | 13.6 px | 0.35 | 1.03 | 116 |
| stroke 39 | 29 % → 55 % | 10.0 px | 0.36 | 1.87 | 107 |
| stroke 40 | 20 % → 61 % | 5.0 px | 0.35 | 3.04 | 88 |
| stroke 41 | 53 % → 56 % | 15.4 px | 0.36 | 1.06 | 94 |
| stroke 42 | 37 % → 68 % | 8.6 px | 0.35 | 1.82 | 99 |
| stroke 43 | 15 % → 33 % | 5.0 px | 0.37 | 2.15 | 91 |
| stroke 44 | 40 % → 49 % | 12.5 px | 0.36 | 1.22 | 92 |
| stroke 45 | 33 % → 39 % | 10.1 px | 0.36 | 1.21 | 92 |
| stroke 46 | 51 % → 54 % | 11.8 px | 0.36 | 1.06 | 91 |
| stroke 47 | 19 % → 23 % | 4.9 px | 0.36 | 1.23 | 88 |
| stroke 48 | 46 % → 57 % | 10.5 px | 0.35 | 1.25 | 89 |
| stroke 49 | 24 % → 29 % | 5.0 px | 0.35 | 1.22 | 92 |
| stroke 50 | 45 % → 48 % | 15.4 px | 0.35 | 1.07 | 94 |
| stroke 51 | 32 % → 32 % | 9.5 px | 0.34 | 1.02 | 89 |
| stroke 52 | 29 % → 34 % | 10.0 px | 0.37 | 1.20 | 93 |
| stroke 53 | 23 % → 28 % | 6.8 px | 0.37 | 1.22 | 95 |
| stroke 54 | 30 % → 37 % | 9.2 px | 0.36 | 1.24 | 90 |
| stroke 55 | 23 % → 29 % | 7.3 px | 0.38 | 1.27 | 92 |
| stroke 56 | 58 % → 61 % | 14.6 px | 0.36 | 1.04 | 92 |
| stroke 57 | 37 % → 48 % | 11.5 px | 0.35 | 1.29 | 90 |
| stroke 58 | 48 % → 48 % | 13.6 px | 0.35 | 1.00 | 87 |
| stroke 59 | 35 % → 41 % | 10.4 px | 0.37 | 1.19 | 98 |
| stroke 60 | 54 % → 59 % | 14.1 px | 0.36 | 1.09 | 91 |
| stroke 61 | 30 % → 34 % | 35.0 px | 0.40 | 1.12 | 91 |
| stroke 62 | 48 % → 51 % | 28.5 px | 0.40 | 1.06 | 4 |
| stroke 63 | 41 % → 41 % | 24.7 px | 0.40 | 1.00 | 4 |
| stroke 64 | 34 % → 34 % | 20.3 px | 0.44 | 1.00 | 4 |
| stroke 65 | 43 % → 52 % | 25.6 px | 0.42 | 1.21 | 4 |
| stroke 66 | 37 % → 40 % | 22.5 px | 0.40 | 1.08 | 4 |
| stroke 67 | 34 % → 36 % | 20.5 px | 0.42 | 1.06 | 4 |
| stroke 68 | 28 % → 37 % | 16.8 px | 0.44 | 1.32 | 4 |
| stroke 69 | 38 % → 50 % | 22.5 px | 0.44 | 1.33 | 4 |
| stroke 70 | 35 % → 35 % | 21.0 px | 0.46 | 1.00 | 4 |
| stroke 71 | 38 % → 41 % | 23.1 px | 0.39 | 1.08 | 4 |
| stroke 72 | 32 % → 32 % | 19.4 px | 0.47 | 1.00 | 4 |
| stroke 73 | 40 % → 40 % | 23.7 px | 0.42 | 1.00 | 4 |
| stroke 74 | 27 % → 33 % | 16.7 px | 0.43 | 1.21 | 4 |
| stroke 75 | 28 % → 32 % | 16.7 px | 0.43 | 1.15 | 4 |
| stroke 76 | 33 % → 33 % | 19.9 px | 0.39 | 1.00 | 4 |
| stroke 77 | 40 % → 40 % | 23.9 px | 0.39 | 1.01 | 4 |
| stroke 78 | 33 % → 33 % | 20.1 px | 0.40 | 1.00 | 4 |
| stroke 79 | 32 % → 32 % | 19.3 px | 0.40 | 1.00 | 4 |
| stroke 80 | 40 % → 47 % | 23.7 px | 0.44 | 1.18 | 4 |
| stroke 81 | 35 % → 35 % | 20.9 px | 0.40 | 1.00 | 4 |
| stroke 82 | 38 % → 38 % | 23.0 px | 0.41 | 1.00 | 4 |
| stroke 83 | 47 % → 47 % | 28.3 px | 0.44 | 1.00 | 4 |
| stroke 84 | 39 % → 39 % | 23.3 px | 0.44 | 1.00 | 4 |
| stroke 85 | 34 % → 34 % | 20.5 px | 0.48 | 1.00 | 4 |
| stroke 86 | 51 % → 51 % | 30.7 px | 0.41 | 1.00 | 4 |
| stroke 87 | 39 % → 43 % | 44.7 px | 0.39 | 1.09 | 97 |
| stroke 88 | 49 % → 55 % | 29.3 px | 0.44 | 1.13 | 4 |
| stroke 89 | 38 % → 47 % | 22.8 px | 0.42 | 1.22 | 4 |
| stroke 90 | 38 % → 47 % | 22.8 px | 0.48 | 1.24 | 4 |
| stroke 91 | 40 % → 43 % | 24.0 px | 0.45 | 1.08 | 4 |
| stroke 92 | 32 % → 39 % | 19.4 px | 0.46 | 1.21 | 4 |
| stroke 93 | 42 % → 47 % | 25.0 px | 0.40 | 1.13 | 4 |
| stroke 94 | 43 % → 43 % | 25.5 px | 0.40 | 1.00 | 4 |
| stroke 95 | 50 % → 52 % | 29.8 px | 0.42 | 1.05 | 4 |
| stroke 96 | 47 % → 53 % | 27.9 px | 0.48 | 1.14 | 4 |
| stroke 97 | 46 % → 50 % | 27.6 px | 0.40 | 1.09 | 4 |
| stroke 98 | 46 % → 46 % | 27.3 px | 0.47 | 1.00 | 4 |
| stroke 99 | 58 % → 62 % | 35.3 px | 0.41 | 1.07 | 4 |
| stroke 100 | 38 % → 41 % | 23.4 px | 0.39 | 1.07 | 4 |
| stroke 101 | 42 % → 44 % | 25.2 px | 0.41 | 1.05 | 4 |
| stroke 102 | 52 % → 52 % | 31.3 px | 0.37 | 1.00 | 4 |
| stroke 103 | 42 % → 44 % | 25.4 px | 0.45 | 1.03 | 4 |
| stroke 104 | 38 % → 38 % | 22.5 px | 0.38 | 1.00 | 4 |
| stroke 105 | 33 % → 40 % | 19.6 px | 0.46 | 1.22 | 4 |
| stroke 106 | 48 % → 48 % | 29.2 px | 0.39 | 1.00 | 4 |
| stroke 107 | 50 % → 50 % | 29.9 px | 0.42 | 1.00 | 4 |
| stroke 108 | 49 % → 51 % | 29.6 px | 0.47 | 1.05 | 4 |
| stroke 109 | 53 % → 53 % | 32.5 px | 0.40 | 1.00 | 4 |
| stroke 110 | 41 % → 41 % | 24.7 px | 0.46 | 1.00 | 4 |
| stroke 111 | 48 % → 48 % | 29.0 px | 0.46 | 1.00 | 4 |
| stroke 112 | 51 % → 51 % | 30.8 px | 0.42 | 1.00 | 4 |
| stroke 113 | 37 % → 44 % | 29.3 px | 0.36 | 1.16 | 65 |
| stroke 114 | 38 % → 44 % | 21.6 px | 0.37 | 1.17 | 3 |
| stroke 115 | 39 % → 42 % | 21.8 px | 0.37 | 1.09 | 2 |
| stroke 116 | 42 % → 42 % | 23.5 px | 0.38 | 1.00 | 3 |
| stroke 117 | 45 % → 53 % | 26.2 px | 0.38 | 1.17 | 2 |
| stroke 118 | 30 % → 43 % | 17.0 px | 0.38 | 1.43 | 3 |
| stroke 119 | 39 % → 44 % | 21.9 px | 0.38 | 1.13 | 3 |
| stroke 120 | 49 % → 55 % | 27.7 px | 0.37 | 1.13 | 3 |
| stroke 121 | 40 % → 41 % | 22.6 px | 0.36 | 1.03 | 2 |
| stroke 122 | 40 % → 40 % | 22.6 px | 0.37 | 1.00 | 3 |
| stroke 123 | 40 % → 41 % | 22.5 px | 0.37 | 1.02 | 6 |
| stroke 124 | 40 % → 48 % | 22.5 px | 0.37 | 1.22 | 5 |
| stroke 125 | 42 % → 46 % | 24.0 px | 0.37 | 1.09 | 3 |
| stroke 126 | 37 % → 42 % | 20.9 px | 0.37 | 1.14 | 3 |
| stroke 127 | 36 % → 37 % | 20.6 px | 0.36 | 1.02 | 3 |
| stroke 128 | 39 % → 39 % | 22.3 px | 0.37 | 1.00 | 3 |
| stroke 129 | 38 % → 38 % | 21.8 px | 0.38 | 1.00 | 2 |
| stroke 130 | 32 % → 32 % | 17.9 px | 0.36 | 1.00 | 3 |
| stroke 131 | 52 % → 52 % | 29.2 px | 0.38 | 1.00 | 3 |
| stroke 132 | 46 % → 46 % | 26.2 px | 0.37 | 1.00 | 3 |
| stroke 133 | 49 % → 49 % | 27.5 px | 0.37 | 1.00 | 3 |
| stroke 134 | 36 % → 42 % | 29.0 px | 0.37 | 1.16 | 79 |
| stroke 135 | 30 % → 35 % | 16.9 px | 0.36 | 1.16 | 3 |
| stroke 136 | 30 % → 32 % | 16.8 px | 0.37 | 1.07 | 5 |
| stroke 137 | 52 % → 61 % | 29.3 px | 0.37 | 1.18 | 6 |
| stroke 138 | 42 % → 50 % | 24.0 px | 0.37 | 1.19 | 3 |
| stroke 139 | 41 % → 46 % | 23.3 px | 0.38 | 1.11 | 4 |
| stroke 140 | 67 % → 68 % | 38.2 px | 0.37 | 1.01 | 4 |
| stroke 141 | 44 % → 49 % | 25.4 px | 0.37 | 1.11 | 5 |
| stroke 142 | 48 % → 48 % | 27.3 px | 0.37 | 1.00 | 6 |
| stroke 143 | 40 % → 44 % | 22.6 px | 0.37 | 1.11 | 7 |
| stroke 144 | 46 % → 46 % | 25.9 px | 0.37 | 1.00 | 3 |
| stroke 145 | 26 % → 31 % | 15.0 px | 0.38 | 1.17 | 4 |
| stroke 146 | 36 % → 36 % | 20.2 px | 0.37 | 1.00 | 6 |
| stroke 147 | 25 % → 27 % | 14.3 px | 0.38 | 1.08 | 3 |
| stroke 148 | 55 % → 55 % | 31.8 px | 0.36 | 1.00 | 3 |
| stroke 149 | 57 % → 64 % | 32.5 px | 0.37 | 1.12 | 15 |
| stroke 150 | 46 % → 46 % | 25.8 px | 0.37 | 1.00 | 7 |
| stroke 151 | 41 % → 50 % | 23.1 px | 0.37 | 1.22 | 4 |
| stroke 152 | 32 % → 42 % | 18.1 px | 0.38 | 1.33 | 2 |
| stroke 153 | 69 % → 69 % | 39.2 px | 0.37 | 1.00 | 5 |
| stroke 154 | 54 % → 54 % | 30.7 px | 0.37 | 1.00 | 3 |
| stroke 155 | 39 % → 44 % | 30.7 px | 0.36 | 1.11 | 84 |
| stroke 156 | 56 % → 56 % | 31.5 px | 0.37 | 1.00 | 7 |
| stroke 157 | 54 % → 67 % | 30.5 px | 0.37 | 1.25 | 5 |
| stroke 158 | 31 % → 35 % | 17.7 px | 0.37 | 1.13 | 3 |
| stroke 159 | 46 % → 50 % | 26.3 px | 0.38 | 1.07 | 8 |
| stroke 160 | 59 % → 65 % | 33.4 px | 0.37 | 1.10 | 6 |
| stroke 161 | 54 % → 54 % | 30.6 px | 0.36 | 1.00 | 3 |
| stroke 162 | 50 % → 54 % | 28.5 px | 0.36 | 1.07 | 3 |
| stroke 163 | 46 % → 56 % | 26.3 px | 0.38 | 1.20 | 6 |
| stroke 164 | 54 % → 60 % | 30.5 px | 0.37 | 1.11 | 4 |
| stroke 165 | 48 % → 50 % | 27.3 px | 0.36 | 1.04 | 3 |
| stroke 166 | 47 % → 48 % | 27.2 px | 0.38 | 1.02 | 3 |
| stroke 167 | 40 % → 40 % | 22.9 px | 0.36 | 1.00 | 5 |
| stroke 168 | 48 % → 48 % | 27.2 px | 0.37 | 1.00 | 5 |
| stroke 169 | 42 % → 45 % | 23.5 px | 0.37 | 1.08 | 6 |
| stroke 170 | 47 % → 50 % | 27.4 px | 0.38 | 1.05 | 3 |
| stroke 171 | 52 % → 52 % | 29.3 px | 0.38 | 1.00 | 4 |
| stroke 172 | 60 % → 60 % | 34.1 px | 0.37 | 1.00 | 3 |
| stroke 173 | 51 % → 51 % | 29.1 px | 0.36 | 1.00 | 3 |
| stroke 174 | 70 % → 72 % | 39.8 px | 0.38 | 1.02 | 3 |
| stroke 175 | 67 % → 67 % | 38.2 px | 0.38 | 1.00 | 3 |
| stroke 176 | 36 % → 41 % | 28.6 px | 0.36 | 1.13 | 83 |
| stroke 177 | 56 % → 70 % | 31.4 px | 0.37 | 1.25 | 3 |
| stroke 178 | 56 % → 67 % | 31.9 px | 0.38 | 1.18 | 3 |
| stroke 179 | 35 % → 35 % | 19.8 px | 0.39 | 1.00 | 6 |
| stroke 180 | 46 % → 50 % | 25.8 px | 0.37 | 1.10 | 5 |
| stroke 181 | 55 % → 62 % | 31.1 px | 0.37 | 1.13 | 3 |
| stroke 182 | 49 % → 49 % | 27.6 px | 0.36 | 1.00 | 3 |
| stroke 183 | 56 % → 59 % | 32.0 px | 0.38 | 1.05 | 3 |
| stroke 184 | 33 % → 40 % | 18.7 px | 0.38 | 1.22 | 5 |
| stroke 185 | 25 % → 36 % | 14.4 px | 0.37 | 1.46 | 3 |
| stroke 186 | 62 % → 63 % | 35.1 px | 0.34 | 1.02 | 6 |
| stroke 187 | 30 % → 42 % | 17.0 px | 0.38 | 1.38 | 4 |
| stroke 188 | 21 % → 32 % | 11.7 px | 0.38 | 1.55 | 4 |
| stroke 189 | 55 % → 57 % | 31.3 px | 0.37 | 1.02 | 3 |
| stroke 190 | 26 % → 30 % | 14.9 px | 0.38 | 1.15 | 3 |
| stroke 191 | 39 % → 39 % | 22.7 px | 0.38 | 1.00 | 3 |
| stroke 192 | 25 % → 29 % | 14.5 px | 0.38 | 1.16 | 3 |
| stroke 193 | 44 % → 44 % | 24.7 px | 0.37 | 1.00 | 3 |
| stroke 194 | 34 % → 34 % | 19.1 px | 0.39 | 1.00 | 2 |
| stroke 195 | 37 % → 37 % | 21.1 px | 0.37 | 1.00 | 3 |
| stroke 196 | 66 % → 66 % | 37.6 px | 0.36 | 1.00 | 7 |

Numbers say: wet paint spreads well beyond the stroke.

## Refs v3 · #42 Pink shaggy pastel — own sheet
own sheet 800 × 978 · Gouache 1.00 + water 15 % · 80 px · 54.0 s

![Refs v3 · #42 Pink shaggy pastel — own sheet](Refs-v3-42-Pink-shaggy-pastel-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 32 % → 58 % | 64.3 px | 0.31 | 1.84 | 2690 |
| stroke 2 | 44 % → 48 % | 128.0 px | 0.31 | 1.09 | 920 |
| stroke 3 | 38 % → 52 % | 126.1 px | 0.34 | 1.37 | 1090 |
| stroke 4 | 30 % → 58 % | 103.3 px | 0.34 | 1.89 | 1135 |
| stroke 5 | 39 % → 55 % | 135.1 px | 0.33 | 1.44 | 960 |
| stroke 6 | 39 % → 61 % | 121.4 px | 0.33 | 1.58 | 1109 |
| stroke 7 | 33 % → 57 % | 121.8 px | 0.30 | 1.70 | 970 |
| stroke 8 | 58 % → 44 % | 119.9 px | 0.30 | 0.77 | 913 |
| stroke 9 | 32 % → 60 % | 82.6 px | 0.31 | 1.88 | 1376 |
| stroke 10 | 41 % → 53 % | 157.3 px | 0.32 | 1.29 | 1031 |
| stroke 11 | 35 % → 54 % | 155.0 px | 0.34 | 1.54 | 1011 |
| stroke 12 | 36 % → 54 % | 154.9 px | 0.34 | 1.51 | 1084 |
| stroke 13 | 36 % → 56 % | 139.2 px | 0.33 | 1.56 | 1302 |
| stroke 14 | 38 % → 57 % | 158.7 px | 0.33 | 1.51 | 1256 |
| stroke 15 | 39 % → 51 % | 148.1 px | 0.31 | 1.32 | 1186 |
| stroke 16 | 51 % → 48 % | 142.2 px | 0.30 | 0.95 | 1321 |
| stroke 17 | 63 % → 72 % | 1494.3 px | 0.37 | 1.15 | 18 |
| stroke 18 | 64 % → 73 % | 1875.7 px | 0.37 | 1.14 | 17 |
| stroke 19 | 69 % → 77 % | 1282.7 px | 0.35 | 1.11 | 25 |
| stroke 20 | 63 % → 71 % | 1075.1 px | 0.37 | 1.13 | 28 |
| stroke 21 | 64 % → 71 % | 1651.3 px | 0.37 | 1.11 | 12 |
| stroke 22 | 59 % → 64 % | 865.7 px | 0.35 | 1.07 | 35 |
| stroke 23 | 65 % → 69 % | 1192.1 px | 0.35 | 1.06 | 33 |
| stroke 24 | 70 % → 77 % | 1590.1 px | 0.35 | 1.10 | 24 |
| stroke 25 | 66 % → 69 % | 1602.6 px | 0.35 | 1.05 | 25 |
| stroke 26 | 68 % → 71 % | 1141.0 px | 0.34 | 1.04 | 51 |
| stroke 27 | 69 % → 72 % | 1168.9 px | 0.35 | 1.05 | 12 |
| stroke 28 | 71 % → 78 % | 1632.3 px | 0.35 | 1.09 | 19 |
| stroke 29 | 65 % → 69 % | 1339.1 px | 0.37 | 1.06 | 24 |
| stroke 30 | 71 % → 77 % | 1641.5 px | 0.35 | 1.09 | 17 |
| stroke 31 | 72 % → 77 % | 1356.5 px | 0.35 | 1.07 | 28 |
| stroke 32 | 67 % → 70 % | 1337.4 px | 0.34 | 1.05 | 15 |
| stroke 33 | 71 % → 73 % | 1101.8 px | 0.34 | 1.03 | 28 |
| stroke 34 | 67 % → 70 % | 1179.5 px | 0.35 | 1.04 | 32 |
| stroke 35 | 66 % → 68 % | 1525.9 px | 0.32 | 1.02 | 30 |
| stroke 36 | 66 % → 68 % | 1172.4 px | 0.35 | 1.02 | 34 |
| stroke 37 | 64 % → 67 % | 1190.1 px | 0.35 | 1.05 | 23 |
| stroke 38 | 63 % → 63 % | 1005.5 px | 0.34 | 1.01 | 31 |
| stroke 39 | 62 % → 64 % | 1190.0 px | 0.35 | 1.03 | 19 |
| stroke 40 | 64 % → 68 % | 1179.6 px | 0.37 | 1.07 | 16 |
| stroke 41 | 73 % → 77 % | 1213.8 px | 0.35 | 1.06 | 28 |
| stroke 42 | 70 % → 71 % | 1313.6 px | 0.35 | 1.02 | 12 |
| stroke 43 | 66 % → 69 % | 1547.6 px | 0.34 | 1.05 | 14 |
| stroke 44 | 67 % → 68 % | 1817.0 px | 0.33 | 1.02 | 11 |
| stroke 45 | 74 % → 77 % | 1363.5 px | 0.35 | 1.05 | 28 |
| stroke 46 | 67 % → 70 % | 1358.7 px | 0.37 | 1.05 | 31 |
| stroke 47 | 67 % → 67 % | 1724.0 px | 0.35 | 1.01 | 12 |
| stroke 48 | 66 % → 69 % | 1331.8 px | 0.37 | 1.04 | 26 |
| stroke 49 | 68 % → 68 % | 995.2 px | 0.33 | 1.00 | 23 |
| stroke 50 | 65 % → 64 % | 983.7 px | 0.34 | 1.00 | 30 |
| stroke 51 | 71 % → 75 % | 2038.4 px | 0.35 | 1.05 | 12 |
| stroke 52 | 70 % → 70 % | 1399.6 px | 0.34 | 1.01 | 31 |
| stroke 53 | 65 % → 66 % | 1404.8 px | 0.34 | 1.02 | 28 |
| stroke 54 | 62 % → 63 % | 1133.7 px | 0.34 | 1.02 | 26 |
| stroke 55 | 67 % → 67 % | 1638.3 px | 0.34 | 1.00 | 21 |
| stroke 56 | 74 % → 77 % | 1725.1 px | 0.35 | 1.04 | 23 |
| stroke 57 | 73 % → 74 % | 1088.3 px | 0.33 | 1.02 | 24 |
| stroke 58 | 69 % → 71 % | 1556.8 px | 0.35 | 1.03 | 21 |
| stroke 59 | 75 % → 76 % | 1105.8 px | 0.35 | 1.01 | 36 |
| stroke 60 | 68 % → 68 % | 1018.5 px | 0.32 | 0.99 | 40 |
| stroke 61 | 67 % → 67 % | 969.2 px | 0.35 | 1.01 | 39 |
| stroke 62 | 70 % → 71 % | 1039.2 px | 0.37 | 1.02 | 53 |
| stroke 63 | 72 % → 73 % | 1301.9 px | 0.35 | 1.01 | 21 |
| stroke 64 | 65 % → 66 % | 975.7 px | 0.36 | 1.02 | 39 |
| stroke 65 | 76 % → 77 % | 1251.8 px | 0.34 | 1.01 | 40 |
| stroke 66 | 69 % → 70 % | 2017.4 px | 0.35 | 1.01 | 17 |
| stroke 67 | 69 % → 69 % | 1255.3 px | 0.36 | 0.99 | 21 |
| stroke 68 | 71 % → 69 % | 1113.6 px | 0.33 | 0.97 | 26 |
| stroke 69 | 78 % → 79 % | 1207.0 px | 0.35 | 1.01 | 26 |
| stroke 70 | 71 % → 69 % | 1053.8 px | 0.33 | 0.98 | 32 |
| stroke 71 | 74 % → 74 % | 1119.3 px | 0.34 | 0.99 | 27 |
| stroke 72 | 69 % → 70 % | 1805.8 px | 0.36 | 1.01 | 15 |
| stroke 73 | 71 % → 70 % | 1574.5 px | 0.34 | 0.98 | 18 |
| stroke 74 | 78 % → 78 % | 1206.4 px | 0.36 | 1.01 | 25 |
| stroke 75 | 70 % → 71 % | 1301.3 px | 0.36 | 1.01 | 18 |
| stroke 76 | 75 % → 74 % | 1663.2 px | 0.37 | 0.99 | 14 |
| stroke 77 | 72 % → 72 % | 1369.2 px | 0.36 | 1.00 | 14 |
| stroke 78 | 73 % → 72 % | 1130.3 px | 0.34 | 0.98 | 30 |
| stroke 79 | 68 % → 67 % | 1918.4 px | 0.35 | 0.99 | 12 |
| stroke 80 | 71 % → 69 % | 1593.0 px | 0.34 | 0.98 | 13 |
| stroke 81 | 76 % → 76 % | 1511.3 px | 0.34 | 1.00 | 19 |
| stroke 82 | 71 % → 70 % | 1313.0 px | 0.36 | 0.98 | 19 |
| stroke 83 | 74 % → 74 % | 1465.6 px | 0.33 | 1.00 | 22 |
| stroke 84 | 68 % → 67 % | 1656.3 px | 0.32 | 0.98 | 19 |
| stroke 85 | 69 % → 69 % | 1147.2 px | 0.36 | 1.00 | 26 |
| stroke 86 | 78 % → 78 % | 1524.1 px | 0.35 | 1.00 | 23 |
| stroke 87 | 75 % → 74 % | 441.4 px | 0.37 | 0.99 | 120 |

Numbers say: wet paint spreads well beyond the stroke.

## Refs v3 · #43 Dragged black blocks — own sheet
own sheet 800 × 1114 · Ink 0.93 · Gouache 0.07 · 128 px · 55.5 s

![Refs v3 · #43 Dragged black blocks — own sheet](Refs-v3-43-Dragged-black-blocks-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 17 % → 52 % | 97.7 px | 0.59 | 2.99 | 1046 |
| stroke 2 | 20 % → 50 % | 175.2 px | 0.59 | 2.50 | 1751 |
| stroke 3 | 23 % → 66 % | 203.8 px | 0.58 | 2.87 | 1441 |
| stroke 4 | 33 % → 47 % | 230.9 px | 0.59 | 1.46 | 2771 |
| stroke 5 | 32 % → 62 % | 284.5 px | 0.59 | 1.94 | 1471 |
| stroke 6 | 33 % → 52 % | 194.6 px | 0.59 | 1.60 | 2322 |
| stroke 7 | 46 % → 67 % | 376.6 px | 0.59 | 1.46 | 1778 |
| stroke 8 | 39 % → 50 % | 195.3 px | 0.59 | 1.27 | 2947 |
| stroke 9 | 45 % → 47 % | 291.5 px | 0.58 | 1.03 | 2666 |
| stroke 10 | 53 % → 53 % | 292.9 px | 0.59 | 0.99 | 2462 |

Numbers say: wet paint spreads well beyond the stroke.

## Refs v3 · #44 Blue looping ribbon — own sheet
own sheet 800 × 1203 · Oil 0.84 · Gouache 0.16 + turpentine 10 % · 88 px · 19.7 s

![Refs v3 · #44 Blue looping ribbon — own sheet](Refs-v3-44-Blue-looping-ribbon-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 30 % → 12 % | 48.7 px | 0.67 | 0.40 | 6314 |

## Refs v3 · #45 Pastel pepper — own sheet
own sheet 800 × 800 · Pastel 1.00 · 40 px · 16.2 s

![Refs v3 · #45 Pastel pepper — own sheet](Refs-v3-45-Pastel-pepper-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 14 % → 51 % | 32.8 px | 0.53 | 3.58 | 674 |
| stroke 2 | 20 % → 53 % | 46.5 px | 0.53 | 2.68 | 861 |
| stroke 3 | 27 % → 58 % | 60.9 px | 0.53 | 2.16 | 740 |
| stroke 4 | 35 % → 62 % | 76.1 px | 0.53 | 1.78 | 671 |
| stroke 5 | 44 % → 65 % | 93.9 px | 0.53 | 1.49 | 595 |
| stroke 6 | 53 % → 70 % | 111.8 px | 0.53 | 1.31 | 524 |
| stroke 7 | 63 % → 75 % | 131.6 px | 0.53 | 1.19 | 480 |
| stroke 8 | 74 % → 80 % | 150.6 px | 0.54 | 1.08 | 433 |
| stroke 9 | 27 % → 50 % | 64.5 px | 0.52 | 1.85 | 726 |
| stroke 10 | 32 % → 54 % | 74.9 px | 0.53 | 1.66 | 839 |
| stroke 11 | 40 % → 59 % | 89.2 px | 0.53 | 1.49 | 768 |
| stroke 12 | 47 % → 64 % | 102.5 px | 0.53 | 1.36 | 921 |
| stroke 13 | 54 % → 68 % | 116.4 px | 0.53 | 1.26 | 885 |
| stroke 14 | 62 % → 73 % | 131.8 px | 0.53 | 1.17 | 664 |
| stroke 15 | 69 % → 76 % | 142.8 px | 0.53 | 1.09 | 486 |
| stroke 16 | 77 % → 78 % | 158.0 px | 0.53 | 1.02 | 396 |
| stroke 17 | 66 % → 68 % | 151.5 px | 0.53 | 1.03 | 258 |
| stroke 18 | 48 % → 48 % | 155.6 px | 0.53 | 1.00 | 199 |
| stroke 19 | 48 % → 48 % | 154.3 px | 0.53 | 1.00 | 196 |
| stroke 20 | 31 % → 34 % | 112.5 px | 0.50 | 1.10 | 32 |
| stroke 21 | 9 % → 9 % | 32.3 px | 0.43 | 1.00 | 22 |
| stroke 22 | 79 % → 79 % | 177.3 px | 0.53 | 1.00 | 85 |
| stroke 23 | 63 % → 63 % | 180.3 px | 0.53 | 1.00 | 72 |
| stroke 24 | 42 % → 42 % | 108.1 px | 0.52 | 1.00 | 42 |
| stroke 25 | 78 % → 78 % | 236.1 px | 0.52 | 1.00 | 50 |
| stroke 26 | 59 % → 59 % | 137.5 px | 0.52 | 1.00 | 49 |
| stroke 27 | 57 % → 57 % | 113.9 px | 0.51 | 1.00 | 58 |

Numbers say: wet paint spreads well beyond the stroke.

## Refs v3 · #46 Ink lips on wet paper — own sheet
own sheet 800 × 1047 · Watercolour 1.00 + water 65 % · 56 px · 26.5 s

![Refs v3 · #46 Ink lips on wet paper — own sheet](Refs-v3-46-Ink-lips-on-wet-paper-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 14 % → 22 % | 61.2 px | 0.59 | 1.54 | 305 |
| stroke 2 | 13 % → 21 % | 59.9 px | 0.60 | 1.57 | 262 |

Numbers say: wet paint spreads well beyond the stroke.

## Refs v3 · #47 Pink knife slabs — own sheet
own sheet 800 × 1014 · Gouache 1.00 + water 15 % · 240 px · 50.6 s

![Refs v3 · #47 Pink knife slabs — own sheet](Refs-v3-47-Pink-knife-slabs-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 26 % → 28 % | 127.5 px | 0.08 | 1.10 | 4694 |
| stroke 2 | 45 % → 30 % | 315.5 px | 0.08 | 0.67 | 6790 |
| stroke 3 | 54 % → 31 % | 481.6 px | 0.08 | 0.57 | 9191 |
| stroke 4 | 64 % → 30 % | 451.0 px | 0.08 | 0.47 | 7002 |
| stroke 5 | 82 % → 29 % | 422.8 px | 0.08 | 0.36 | 5285 |
| stroke 6 | 17 % → 31 % | 161.2 px | 0.08 | 1.79 | 218 |
| stroke 7 | 26 % → 32 % | 321.7 px | 0.08 | 1.25 | 190 |
| stroke 8 | 35 % → 32 % | 444.7 px | 0.08 | 0.91 | 188 |
| stroke 9 | 46 % → 31 % | 443.7 px | 0.08 | 0.68 | 168 |

Numbers say: wet paint spreads well beyond the stroke.

## Refs v3 · #48 Black bands with drips — own sheet
own sheet 800 × 1047 · Watercolour 1.00 + water 35 % · 96 px · 37.7 s

![Refs v3 · #48 Black bands with drips — own sheet](Refs-v3-48-Black-bands-with-drips-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 31 % → 52 % | 100.6 px | 0.45 | 1.71 | 1188 |
| stroke 2 | 44 % → 65 % | 189.8 px | 0.44 | 1.46 | 1429 |
| stroke 3 | 48 % → 68 % | 195.9 px | 0.44 | 1.41 | 1389 |
| stroke 4 | 47 % → 68 % | 195.4 px | 0.43 | 1.46 | 2245 |
| stroke 5 | 46 % → 47 % | 187.1 px | 0.43 | 1.03 | 1593 |

Numbers say: wet paint spreads well beyond the stroke.

## Refs v3 · #49 Magenta letters round — own sheet
own sheet 800 × 1000 · Ink 0.93 · Gouache 0.07 · 40 px · 32.9 s

![Refs v3 · #49 Magenta letters round — own sheet](Refs-v3-49-Magenta-letters-round-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 13 % → 19 % | 37.9 px | 0.52 | 1.51 | 172 |
| stroke 2 | 16 % → 27 % | 37.3 px | 0.54 | 1.72 | 181 |
| stroke 3 | 23 % → 35 % | 70.7 px | 0.54 | 1.51 | 174 |
| stroke 4 | 18 % → 31 % | 37.6 px | 0.55 | 1.71 | 380 |
| stroke 5 | 18 % → 33 % | 53.7 px | 0.53 | 1.90 | 250 |
| stroke 6 | 32 % → 38 % | 169.7 px | 0.53 | 1.18 | 41 |
| stroke 7 | 21 % → 29 % | 42.7 px | 0.53 | 1.38 | 361 |
| stroke 8 | 19 % → 37 % | 64.4 px | 0.53 | 1.94 | 283 |
| stroke 9 | 29 % → 33 % | 112.4 px | 0.54 | 1.16 | 117 |
| stroke 10 | 17 % → 36 % | 53.5 px | 0.52 | 2.06 | 309 |
| stroke 11 | 32 % → 39 % | 165.1 px | 0.50 | 1.24 | 52 |
| stroke 12 | 27 % → 38 % | 54.1 px | 0.53 | 1.41 | 358 |
| stroke 13 | 17 % → 27 % | 59.5 px | 0.51 | 1.61 | 100 |
| stroke 14 | 22 % → 40 % | 80.6 px | 0.52 | 1.80 | 100 |
| stroke 15 | 17 % → 29 % | 53.9 px | 0.53 | 1.67 | 215 |
| stroke 16 | 32 % → 37 % | 167.3 px | 0.53 | 1.17 | 67 |
| stroke 17 | 26 % → 36 % | 52.7 px | 0.54 | 1.39 | 330 |
| stroke 18 | 16 % → 25 % | 56.8 px | 0.52 | 1.53 | 84 |
| stroke 19 | 26 % → 30 % | 80.1 px | 0.52 | 1.15 | 86 |
| stroke 20 | 19 % → 22 % | 58.2 px | 0.53 | 1.18 | 99 |
| stroke 21 | 24 % → 27 % | 55.9 px | 0.53 | 1.13 | 268 |

Numbers say: wet paint spreads well beyond the stroke.

## Refs v3 · #50 Swipes on seaside — own sheet
own sheet 800 × 1158 · Gouache 1.00 + water 15 % · 240 px · 87.5 s

![Refs v3 · #50 Swipes on seaside — own sheet](Refs-v3-50-Swipes-on-seaside-own-sheet.png)

| stroke | covered | width | dark | spread | ms |
|---|---|---|---|---|---|
| stroke 1 | 22 % → 7 % | 104.1 px | 0.19 | 0.30 | 6171 |
| stroke 2 | 37 % → 7 % | 227.6 px | 0.19 | 0.19 | 8219 |
| stroke 3 | 51 % → 6 % | 402.2 px | 0.17 | 0.12 | 8143 |
| stroke 4 | 58 % → 7 % | 504.8 px | 0.20 | 0.12 | 7962 |
| stroke 5 | 59 % → 7 % | 548.1 px | 0.20 | 0.11 | 9217 |
| stroke 6 | 59 % → 6 % | 523.5 px | 0.20 | 0.11 | 6721 |
| stroke 7 | 68 % → 6 % | 557.9 px | 0.20 | 0.09 | 6873 |
| stroke 8 | 81 % → 6 % | 571.7 px | 0.21 | 0.07 | 6531 |
| stroke 9 | 90 % → 6 % | 549.6 px | 0.22 | 0.06 | 8243 |
| stroke 10 | 99 % → 5 % | 466.0 px | 0.23 | 0.05 | 4943 |
| stroke 11 | 1 % → 6 % | 49.4 px | 0.17 | 8.30 | 68 |
| stroke 12 | 2 % → 8 % | 109.6 px | 0.19 | 3.90 | 61 |
| stroke 13 | 1 % → 6 % | 47.5 px | 0.20 | 6.40 | 80 |
| stroke 14 | 3 % → 7 % | 170.1 px | 0.18 | 2.62 | 77 |
| stroke 15 | 2 % → 6 % | 103.4 px | 0.22 | 2.80 | 70 |
| stroke 16 | 3 % → 7 % | 299.6 px | 0.20 | 2.23 | 61 |
| stroke 17 | 4 % → 7 % | 200.2 px | 0.19 | 1.56 | 145 |
| stroke 18 | 4 % → 6 % | 320.3 px | 0.17 | 1.69 | 69 |
| stroke 19 | 4 % → 6 % | 277.2 px | 0.20 | 1.44 | 76 |
| stroke 20 | 7 % → 8 % | 397.7 px | 0.20 | 1.22 | 94 |
| stroke 21 | 7 % → 8 % | 529.1 px | 0.20 | 1.07 | 62 |
| stroke 22 | 7 % → 7 % | 466.0 px | 0.19 | 0.97 | 43 |
| stroke 23 | 7 % → 6 % | 313.6 px | 0.21 | 0.96 | 82 |

Numbers say: wet paint spreads well beyond the stroke.

