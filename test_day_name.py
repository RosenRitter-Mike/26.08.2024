import day_name;
import pytest;


def test_sunday():
    assert day_name.day_name(1) == "Sunday";


def test_monday():
    assert day_name.day_name(2) == "Monday";


def test_tuesday():
    assert day_name.day_name(3) == "Tuesday";


def test_wednesday():
    assert day_name.day_name(4) == "Wednesday";


def test_thursday():
    assert day_name.day_name(5) == "Thursday";


def test_friday():
    assert day_name.day_name(6) == "Friday";


def test_saturday():
    assert day_name.day_name(7) == "Saturday";

def test_all_days():
    days: list[str] = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"];
    for i in range(1, 8):
        assert day_name.day_name(i) == days[i-1];


def test_no_day():
    with pytest.raises(ValueError) as ex:
        actual: str = day_name.day_name(0);

        assert str(ex.value) == "no such week day";


def test_past_day():
    with pytest.raises(ValueError) as ex:
        actual: str = day_name.day_name(-2);

        assert str(ex.value) == "no such week day";


def test_future_day():
    with pytest.raises(ValueError) as ex:
        actual: str = day_name.day_name(10);

        assert str(ex.value) == "no such week day";


def test_day_str():
    try:
        actual: str = day_name.day_name("Yesterday");
        assert False;
    except TypeError as e:
        assert True;


def test_day_float():
    try:
        actual: str = day_name.day_name(3.02);
        assert False;
    except TypeError as e:
        assert True;