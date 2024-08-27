import check_guess as cg
import pytest


def test_guess_correct():
    assert cg.check_guess(50, "50") == "BINGO!!!";


def test_guess_lower():
    assert cg.check_guess(50, "20") == "guess higher";


def test_guess_higher():
    assert cg.check_guess(50, "70") == "guess lower";


def test_guess_str():
    try:
        actual: str = cg.check_guess(50, "forty-two");
        assert False;
    except ValueError as e:
        assert True;


def test_guess_out_of_range():
    with pytest.raises(ValueError) as ex:
        actual: str = cg.check_guess(50, "144");

        assert str(ex.value) == "range of out number";


def test_guess_negative():
    with pytest.raises(ValueError) as ex:
        actual: str = cg.check_guess(50, "-10");

        assert str(ex.value) == "range of out number";
