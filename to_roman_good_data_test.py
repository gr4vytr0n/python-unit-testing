from roman import *

import unittest

class GoodValues(unittest.TestCase):
  known_values = ( (1, 'I'), (2, 'II'), (3, 'III'), (4, 'IV'), (5, 'V'),
    (6, 'VI'), (7, 'VII'), (8, 'VIII'), (9, 'IX'), (10, 'X') )
  
  # test known good values
  def test_to_roman_known_good_values(self):
    '''to_roman should give known result with known input'''
    for integer, numeral in self.known_values:
      result = to_roman(integer)
      self.assertEqual(numeral, result)
