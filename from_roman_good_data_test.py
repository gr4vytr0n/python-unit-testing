from roman import *

import unittest

class GoodValues(unittest.TestCase):
  known_values = ( (1, 'I'), (2, 'II'), (3, 'III'), (4, 'IV'), (5, 'V'),
    (6, 'VI'), (7, 'VII'), (8, 'VIII'), (9, 'IX'), (10, 'X') )
  
  # test known good values
  def test_from_roman_known_good_values(self):
    '''from_roman should give known result from known input'''
    for integer, numeral in self.known_values:
      result = from_roman(numeral)
      self.assertEqual(integer, result)

  def test_to_roman_into_from_roman(self):
      ''' send know values into to_roman then send returned Roman numerals into from_roman'''
      for integer in range(1, 11):
        numeral = to_roman(integer)
        result = from_roman(numeral)
        self.assertEqual(integer, result)
