from roman import *

import unittest

class BadValues(unittest.TestCase):
  # test with invalid Roman numerals
  def test_too_many_repeated_characters(self):
    '''test should fail when input value contains too many repeating characters'''
    for s in ('MMMM', 'DD', 'CCCC', 'LL', 'XXXX', 'VV', 'IIII'):
      self.assertRaises(InvalidRomanNumeralError, from_roman, s)
