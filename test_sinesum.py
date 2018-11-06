#!/usr/bin/env python3

"""sinesum.py Test Module

Verify implementation of the Fourier sine series using numpy arrays.
"""

import sinesum
import math

def test_s():
    assert math.isclose((sinesum.s(1/(2*math.pi)),1/(4/math.pi)), math.sin(1))

def test_f():
    assert sinesum.f(1) == 1
    assert sinesum.f(-1) == -1
    assert sinesume.f(0) == 0
