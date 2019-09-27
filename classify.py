#!/usr/bin/python3
"""
The purpose of this module is to classify a triangle as isoceles, scalene, equalateral or right
"""

import sys
import math


def classify_triangle(a, b, c):
    """
    The purpose of this function is to classify a triangle as
    isoceles, scalene, equalateral or right

    The order of operations do not matter
    Right takes priority over scalene and isocelese

    """
    # Make c the largest value
    max_side = max([a, b, c])
    if max_side == a:
        a, c = c, a
    if max_side == b:
        b, c = c, b

    # Determine validity
    if a + b <= c:
        classification = 'invalid'
    elif math.isinf(a) or math.isinf(b) or math.isinf(c):
        classification = 'invalid'
    elif math.isnan(a) or math.isnan(b) or math.isnan(c):
        classification = 'invalid'

    # Determine if right
    elif a**2 + b**2 == c**2:
        classification = 'right'

    # Determine if eqalateral
    elif a == b and b == c:
        classification = 'equilateral'

    # Determine if isosceles
    elif a == b or b == c or a == c:
        classification = 'isosceles'

    else:
        classification = 'scalene'

    return classification

if __name__ == '__main__':
    print(classify_triangle(
        float(sys.argv[1]),
        float(sys.argv[2]),
        float(sys.argv[3])))
