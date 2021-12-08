import pytest

from chararray import chararray


def test_chararray() -> None:
    """Tests chararray properties"""
    assert chararray() == chararray()
    assert repr(chararray()) == "chararray()"

    assert chararray("abc") == "abc"
    assert repr(chararray("abc")) == "chararray('abc')"
    assert chararray("abc") == chararray("abc")
    assert chararray("abc") != chararray("abcd")
    assert chararray("abc") < chararray("def")

    assert repr(chararray("abc") + chararray("def")) == "chararray('abcdef')"
    assert chararray("abc") + chararray("def") == chararray("abcdef")

    with pytest.raises(ValueError):
        chararray(123)
    with pytest.raises(ValueError):
        chararray(b"abcd")
    with pytest.raises(ValueError):
        chararray(["abc", "def"])

    assert chararray("abcdefg")[:3] == chararray("abc")
    chars = chararray("abcdefg")
    chars[3:] = "abcd"
    assert chars == chararray("abcabcd")
    with pytest.raises(TypeError):
        chars[3:] = 123
