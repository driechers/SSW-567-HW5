#!/usr/bin/python3

from classify import classify_triangle

import pytest

def test_invalid_zero():
    """
    Test that an null size triangle returns 'invalid'
    """
    assert 'invalid' == classify_triangle(0,0,0)

def test_inf():
    """
    Test that an invalid triangle with an infinite length returns 'invalid'
    """
    assert 'invalid' == classify_triangle(1,2,float('inf'))

def test_nan():
    """
    Test that an invalid triangle with a not a number length returns 'invalid'
    """
    assert 'invalid' == classify_triangle(1,2,float('nan'))

def test_invalid_scalene():
    """
    Test that an invalid triangle with three different lengths returns 'invalid'
    """
    assert 'invalid' == classify_triangle(1,2,3)

def test_invalid_isosceles():
    """
    Test that an invalid triangle with two equal sides returns 'invalid'
    """
    assert 'invalid' == classify_triangle(1,1,3)

def test_equilateral():
    """
    Test that a triangle with three equal sides returns 'equilateral'
    Note: equilateral triangles are also isosceles
    """
    assert 'equilateral' == classify_triangle(1.2,1.2,1.2)

def test_isosceles():
    """
    Test that a triangle with two equal sides returns 'isosceles'
    """
    assert 'isosceles' == classify_triangle(2,2,3)

def test_scalene():
    """
    Test that a triangle with three differnt sides returns 'scalene'
    """
    assert 'scalene' == classify_triangle(2,3,4)

def test_right():
    """
    Test that a tirangle with a**2 + b**2 = c**2 triangle returns 'right'
    Note: right triangles are also scalene.
    """
    assert 'right' == classify_triangle(3,4,5)

def test_right_order():
    """
    Test that a tirangle with a**2 + b**2 = c**2 triangle return 'right' even when c is not the third parameter
    Note: right triangles are also scalene.
    """
    assert 'right' == classify_triangle(5,3,4)
