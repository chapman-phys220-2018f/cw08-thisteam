#!/usr/bin/env python3
# -*- coding: utf-8 -*-

###
# Name: Alley and Royal
# Student ID: 2293544
# Email: busick@chapman.edu
# Course: PHYS220/MATH220/CPSC220 Fall 2018
# Assignment: CW07
###

import numpy as np

def s(T, t, n):
    
    #k values
    array = np.arange(1, n+1)

    def function(k):
        return (((1)/(2*k-1))*np.sin((2*(2*k-1)*np.pi*t)/(T)))
    summation = np.vectorize(function)
    value = (4/np.pi)*np.sum(summation(array))
    return value

def f(T, t):
    if 0 < t < (T/2):
        return 1
    elif t == 0:
        return 0
    elif -(T/2) < t < 0:
        return -1
    else:
        print("Out of range")
        return None
