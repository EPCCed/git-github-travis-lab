from msc.rot13 import rot13
from msc.rot13 import rot13_char

def test_rot13_char_a():
    assert "Z" == rot13_char("M"), "Unexpected character"
    assert "5" == rot13_char("5"), "Unexpected Non Alpha"
    assert "" == rot13_char(""), "Unexpected Not Null"

def test_rot13():
    assert len("12no889ert") == len(rot13_char("12no889ert")), "Unexpected string length"
    assert " xz " == rot13_char(" xz "), "Expected string with spaces"
