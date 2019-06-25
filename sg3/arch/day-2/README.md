# Computer Architecture - Day 2

## Bitwise Operations

### Bitwise Operators

| Operation | Bitwise Operator | Boolean Operator |
| :-------: | :--------------: | :--------------: |
|    OR     |       `|`        |       `||`       |
|    AND    |       `&`        |       `&&`       |
|    XOR    |       `^`        |       none       |
|    NOT    |       `~`        |       `!`        |

```
  0b00001001
& 0b00000011
  ----------
  0b00000001

  0b01011001
| 0b00100011
  ----------
  0b01111011

  0b01011001
~ 0b00100011
  ----------
  0b01111010
```

### Shifting

- The right shift operator: `>>`
  - Takes a away the specified number of bits from the right.
- Left shift operator: `<<`
  - Adds the number of specified bits to the right

```
0b1110 >> 1 == 0b0111
0b1110 >> 2 == 0b0011
0b1110 >> 3 == 0b0001

0b1110 << 1 == 0b11100
0b1110 << 2 == 0b111000
0b1110 << 3 == 0b1110000
```

```python
#        vv extract these bits 0b01 == 1
x = 0b01001100
# Shift right to move them to the end
#                                    vv
y = x >> 3 #                 0b00001001

# And mask with 0b11 to filter out all other bits

# With the AND mask, the bits you're interested in "show through"
# where the mask is `1`, and are filtered out where the mask is `0`.
# It's like a stencil.

z = y & 0b11
#   0b00001001
# & 0b00000011
# ------------
#   0b00000001
#           ^^ there's our 0b01!
```

## Using Right Shift to Increment the PC

```C
unsigned char IR = 0b1000010; // 0b1000010 is LDI

// get the number of operands
// add 1 for the instruction itself
int add_to_pc = (IR >> 6) + 1

while (running) {
switch(command) {
    case LDI:
    // LDI stuff
    break;
}
    cpu->pc += add_to_pc;
}
```

### Truth Table Review

#### AND

|  A  |  B  | A AND B |
| :-: | :-: | :-----: |
|  0  |  0  |    0    |
|  0  |  1  |    0    |
|  1  |  0  |    0    |
|  1  |  1  |    1    |

#### OR

|  A  |  B  | A OR B |
| :-: | :-: | :----: |
|  0  |  0  |   0    |
|  0  |  1  |   1    |
|  1  |  0  |   1    |
|  1  |  1  |   1    |

#### XOR

Exclusive-OR means that one or the other must be true, but not both.

|  A  |  B  | A XOR B |
| :-: | :-: | :-----: |
|  0  |  0  |    0    |
|  0  |  1  |    1    |
|  1  |  0  |    1    |
|  1  |  1  |    0    |

#### NOT

|  A  | NOT A |
| :-: | :---: |
|  0  |   1   |
|  1  |   0   |
