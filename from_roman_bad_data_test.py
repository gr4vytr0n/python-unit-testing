from roman import *

import unittest

class BadValues(unittest.TestCase):
  # test with invalid Roman numerals
  def test_too_many_repeated_characters(self):
    '''expception should be raised when input value contains too many repeating characters'''
    for s in ('MMMM', 'DD', 'CCCC', 'LL', 'XXXX', 'VV', 'IIII'):
      self.assertRaises(InvalidRomanNumeralError, from_roman, s)

  def test_bad_repeated_pairs(self):
    '''expception should be raised when input value contains bad repeated pairs of characters'''
    for s in ('CMCM', 'CDCD', 'XCXC', 'XLXL', 'IXIX', 'IVIV'):
      self.assertRaises(InvalidRomanNumeralError, from_roman, s)

  def test_from_roman_malformed_antecedents(self):
    '''expception should be raised when input value contains a malformed antecedent'''
    for s in ('IIMXCC', 'VX', 'DCM', 'CMM', 'IXIV', 'MCMC', 'XCX', 'IVI', 'LM', 'LD', 'LC'):
      self.assertRaises(InvalidRomanNumeralError, from_roman, s)

  def test_from_roman_empty_string_input_value(self):
    '''expception should be raised when input value is an empty string'''
    self.assertRaises(InvalidRomanNumeralError, from_roman, '')