#!/usr/bin/python3

import sys
import math

def classify_triangle(a, b, c):
    # Make c the largest value
    x = max([a,b,c])
    if x == a:
        a,c = c,a
    if x == b:
        b,c = c,b

    # Determine validity
    if a + b <= c:
        return 'invalid'
    if math.isinf(a) or math.isinf(b) or math.isinf(c):
        return 'invalid'
    if math.isnan(a) or math.isnan(b) or math.isnan(c):
        return 'invalid'

    # Determine if right
    if a**2 + b**2 == c**2:
        return 'right'

    # Determine if eqalateral
    if a == b and b == c:
        return 'equilateral'

    # Determine if isosceles
    if a == b or b == c or a == c:
        return 'isosceles'

    return 'scalene'

if __name__ == '__main__':
    print(classify_triangle(
        float(sys.argv[1]),
        float(sys.argv[2]),
        float(sys.argv[3])))
