from OutOfRange import OutOfRange

roman_numeral_map = ( ('X', 10), ('IX', 9), ('V', 5), ('IV', 4), ('I', 1) )

def to_roman(n):
  '''convert integer to Roman numeral'''
  result = ''
  for numeral, integer in roman_numeral_map:
    while n >= integer:
      result += numeral
      n -= integer
  return result
