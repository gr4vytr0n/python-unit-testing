import roman as rm
import unittest

class KnownValues(unittest.TestCase):
  known_values = ( (1, 'I'), (2, 'II'), (3, 'III'), (4, 'IV'), (5, 'V'),
    (6, 'VI'), (7, 'VII'), (8, 'VIII'), (9, 'IX'), (10, 'X') )
  
  # test known good values
  def test_to_roman_known_values(self):
    '''to_roman should give known result with known input'''
    for integer, numeral in self.known_values:
      result = rm.to_roman(integer)
      self.assertEqual(numeral, result)
  
  # halt and catch fire -- on values greater than 10
  def test_to_roman_out_of_range_values(self):
    '''to_roman should fail with input values greaer than 10'''
    self.assertRaises(rm.OutOfRangeError, rm.to_roman, 11)

if __name__ == '__main__':
  unittest.main()