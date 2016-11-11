from nose.tools import assert_equal
from msc.rot13 import rot13
from msc.rot13 import rot13_char 

def test_rot13_char():

        assert_equal("o", rot13_char("b"))

def test_rot13():

        assert_equal("uryyb", rot13("hello"))
