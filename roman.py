import re

class OutOfRangeError(ValueError):
  pass

class NotIntegerError(ValueError):
  pass

class InvalidRomanNumeralError(ValueError):
  pass

roman_numeral_map = ( ('X', 10), ('IX', 9), ('V', 5), ('IV', 4), ('I', 1) )

to_roman_table = [ None ]
from_roman_table = {}

def to_roman(n):
  '''convert integer to Roman numeral'''
  if not (0 < n < 11):
    raise OutOfRangeError('number out of range (must not be > 10 or <= 0)')
  if int(n) != n:
    raise NotIntegerError('number must be an integer')

  return to_roman_table[n]


def from_roman(s):
  '''convert Roman numeral to integer'''
  if not isinstance(s, str):
    raise InvalidRomanNumeralError('Input must be a string.')
  if not s:
    raise InvalidRomanNumeralError('Invalid roman numeral: {0}'.format(s))
  if s not in from_roman_table:
    raise InvalidRomanNumeralError('Invalid roman numeral: {0}'.format(s))

  return from_roman_table[s]

def build_lookup_table():
  def to_roman(n):
    result = ''
    for numeral, integer in roman_numeral_map:
      if n >= integer:
        result = numeral
        n -= integer
        break
    if n > 0:
      result += to_roman_table[n]
    return result
  for integer in range(1, 11):
    roman_numeral = to_roman(integer)
    to_roman_table.append(roman_numeral)
    from_roman_table[roman_numeral] = integer

build_lookup_table()
