#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 26 18:22:22 2019

@author: alex
"""

import numpy as np
import csv


# files to be loaded
csvValues = 'values.csv'
csvBounds = 'bounds.csv'


def expectedValue():
    """
    # Expected value is sum of probability times event
    """

    return sum(expValues())

def loadValues():
    """
    
    """
    values = np.genfromtxt(csvValues, delimiter=',', skip_header=1)
    
    return values

def loadBounds():
    """
    
    """
    f = open(csvBounds, 'r')
    reader = csv.reader(f)
    next(reader, None) # skip header in first row
    vdict = {(int(row[0]), int(row[1])) : int(row[2]) for row in reader}

    return vdict

def freqCount():
    """
    # Creates frequency count 
    """
    freq_count = np.histogram(values, bins=len(vdict))

    return freq_count

def freqValues():
    """
    
    """
    freq_count = freqCount()
    # zip the freq_count values with the cost per vulnerability into a tuple
    freq_values = tuple(zip(freq_count[0], vdict.values()))

    return freq_values

def freqProb():
    """
    
    """
    freq_prob = [values_zero/values_total]
    freq_count = freqCount()
    for i in range(10):
        freq_prob.append(freq_count[0][i] / values_total)
        
    return freq_prob

def expValues():
    freq_values = freqValues()

    # Multiply the count per bound with the probability
    exp_values = [((freq_values[i][0] * freq_values[i][1])/(values_zero + values_nonzero)) for i in range(len(freq_values))]

    return exp_values

vdict = loadBounds()
values = loadValues()

values_zero = 2500#input("Number of non-inundated grid points: ")
values_nonzero = len(values)
values_total = values_zero + values_nonzero


exp_value = expectedValue()

print(exp_value)