from msc.rot13 import rot13
from msc.rot13 import rot13_char

def test_rot13_char_n():
	assert "n" == rot13("a"), "Unexpected character"


def test_rot13():
        assert "sverzna  fnz" == rot13("fireman sam"), "Unexpected line"


