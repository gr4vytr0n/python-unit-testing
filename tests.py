from roman import *
import unittest

class KnownValues(unittest.TestCase):
  known_values = ( (1, 'I'), (2, 'II'), (3, 'III'), (4, 'IV'), (5, 'V'),
    (6, 'VI'), (7, 'VII'), (8, 'VIII'), (9, 'IX'), (10, 'X') )
  
  # test known good values
  def test_to_roman_known_values(self):
    '''to_roman should give known result with known input'''
    for integer, numeral in self.known_values:
      result = to_roman(integer)
      self.assertEqual(numeral, result)
  
  # halt and catch fire -- on values greater than 10
  def test_to_roman_out_of_range_values_more(self):
    '''to_roman should fail with input values greater than 10'''
    self.assertRaises(OutOfRangeError, to_roman, 11)

  # halt and catch fire -- on values less than or equal to 0
  def test_to_roman_out_of_range_values_less(self):
    '''to_roman should fail with input values less than or equal to 0'''
    self.assertRaises(OutOfRangeError, to_roman, 0)
    self.assertRaises(OutOfRangeError, to_roman, -5)

  def test_to_roman_non_integer(self):
    '''to_roman should fail with non integer input values'''
    self.assertRaises(NotIntegerError, to_roman, 'string')
    self.assertRaises(NotIntegerError, to_roman, 0.5) 

if __name__ == '__main__':
  unittest.main()
