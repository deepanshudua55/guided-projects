# Theory of Computation - Day 2

Fill out truth tables for the following expressions:

1. `(¬A v B)` (alternate: `(not A or B)`)

```
A     B     result
-------------------
0     0       1
0     1       1
1     0       0
1     1       1
```

2. `¬(A ∧ B) ∧ ¬(¬A v ¬B)` (alternate: `not (A and B) and not (not A or not B)`)

```
A     B     result
-------------------
0     0       ?
0     1       ?
1     0       ?
1     1       ?
```

3. `(A v B) v ( (¬A ∧ C) ∧ ¬(B v C) )` (alternate: `(A or B) or ( (not A and C) and not (B or C) )`)

```
A     B     C     result
-------------------------
0     0     0       ?
0     0     1       ?
0     1     0       ?
0     1     1       ?
1     0     0       ?
1     0     1       ?
1     1     0       ?
1     1     1       ?
```

```
        CARRY SUM
A    B    A + B
------------------
0    0     0 0
0    1     0 1
1    0     0 1
1    1     1 0
```
