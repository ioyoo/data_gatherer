from ..tools.text_tools import find_in_text


def test_find_in_text():
    try:
        assert find_in_text("hola", "digo hola antes de adios")
    except AssertionError:
        raise AssertionError("Find in text no working correctly")
