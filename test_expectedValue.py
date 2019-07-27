#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 26 18:53:13 2019

@author: alex
"""

import unittest
import expectedValue

class TestExpValue(unittest.TestCase):
    
    def test_csv(self):
        """
        Test: Inputs to depths and vulnerability
        are csv (comma) files
        """
        pass
    
    def test_loadValues(self):
        """
        Test: All depths are equal to or greater than zero
        """
        values = expectedValue.loadValues()
        self.assertGreaterEqual(values.all(), 0)
    
    def test_loadBounds(self):
        """
        Test: 1. depth intervals, 2. increasing damage amount
        """
        #vcurve = expectedDamage.loadVCurve()
        pass
    
    def test_freqProb(self):
        """
        Test: Frequency probabilities sum to one.
        """
        freq_prob = expectedValue.freqProb()
        self.assertAlmostEqual(sum(freq_prob), 1)
    
    def test_freqValues(self):
        pass
    
    def test_expValues(self):
        pass
        

if __name__=='__main__':
    unittest.main()
