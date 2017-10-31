from msc.rot13 import rot13
from msc.rot13 import rot13_char

def test_rot13():
    assert rot13("a") == "n"
