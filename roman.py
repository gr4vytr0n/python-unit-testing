class OutOfRangeError(ValueError):
  pass

class NotIntegerError(ValueError):
  pass

roman_numeral_map = ( ('X', 10), ('IX', 9), ('V', 5), ('IV', 4), ('I', 1) )

def to_roman(n):
  '''convert integer to Roman numeral'''
  if isinstance(n, int):
    if not (0 < n < 11):
      raise OutOfRangeError('number out of range (must not be > 10 or <= 0)')
  else:
    raise NotIntegerError('number must be an integer')

  result = ''
  for numeral, integer in roman_numeral_map:
    while n >= integer:
      result += numeral
      n -= integer
  return result

def from_roman(n):
  '''convert Roman numeral to integer'''
  pass
