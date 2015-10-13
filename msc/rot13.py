"""
Rot13

This is an implementation of ROT-13, a substitution cipher. The code
originates from http://en.literateprograms.org/Rot13_(Python).

Licence: CC0 1.0 Universal (CC0 1.0)  Public Domain Dedication,
http://creativecommons.org/publicdomain/zero/1.0/.

For more on ROT-13 substitution cipher, see
https://en.wikipedia.org/wiki/ROT13. 
"""

import sys

"""
Rotate a single character by 13 places. 'a' maps to 'n', 'b' to 'o',
..., 'm' to 'z', 'n' to 'a', ..., 'z' to 'm', similarly for upper-case
characters. Characters not in 'a-zA-Z' are left as-is.

:param ch: character
:type ch: str or unicode
:return: character
:rtype: str or unicode
"""
def rot13_char(ch):
  if not ch.isalpha():
    return ch
  ch_low = ch.lower()
  if ch_low <= 'm':
    dist = 13
  else:
    dist = -13
  return chr(ord(ch) + dist)

"""
Apply ROT-13 substitution cipher to a string.

:param s: string
:type ch: str or unicode
:return: string after ROT-13 substitution
:rtype: str or unicode
"""
def rot13(s):
  return ''.join( rot13_char(ch) for ch in s )

if __name__ == "__main__":
  print(rot13(sys.argv[1]))
