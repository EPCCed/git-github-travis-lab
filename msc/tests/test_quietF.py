from nose.tools import assert_equal
from msc.rot13 import rot13
from msc.rot13 import rot13_char

def test_rot13_char_a():
	assert_equal('n', rot13_char('a'))

def test_rot13_char_4():
	assert_equal('4', rot13_char('4'))

def test_rot13_str_hello():
	assert_equal('uryyb', rot13('hello'))

def test_rot13_char_A():
	assert_equal('N', rot13_char('A'))
