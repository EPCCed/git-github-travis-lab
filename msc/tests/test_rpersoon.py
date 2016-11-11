from nose.tools import assert_equal
from msc.rot13 import *

def test_rot13_char_a():
	assert_equal("n", rot13_char("a"))
