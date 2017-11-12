from roman import *

import unittest

class BadValues(unittest.TestCase):
  # test known bad values
  # on values greater than 10
  def test_to_roman_out_of_range_values_more(self):
    '''to_roman should fail with input values greater than 10'''
    self.assertRaises(OutOfRangeError, to_roman, 11)

  # on values less than or equal to 0
  def test_to_roman_out_of_range_values_less(self):
    '''to_roman should fail with input values less than or equal to 0'''
    self.assertRaises(OutOfRangeError, to_roman, 0)
    self.assertRaises(OutOfRangeError, to_roman, -5)

  # on values that are non integers
  def test_to_roman_non_integer(self):
    '''to_roman should fail with non integer input values'''
    self.assertRaises(NotIntegerError, to_roman, 'string')
    self.assertRaises(NotIntegerError, to_roman, 0.5) 
