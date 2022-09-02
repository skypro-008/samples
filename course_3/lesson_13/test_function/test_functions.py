from main import get_grade_verbose, get_period
import pytest


class TestGetPeriod:

    def test_get_period_normal(self):

        for i in range(7):
            assert get_period(i) == "ночь"

        for i in range(7,12):
            assert get_period(i) == "утро"

        for i in range(12,18):
            assert get_period(i) == "день"

        for i in range(18,25):
            assert get_period(i) == "вечер"

    def test_get_period_out_of_range(self):

        with pytest.raises(ValueError) as e:
            get_period(-1), f"Wrong type of error {e} or no error"

    def test_get_period_wrong_type(self):

        with pytest.raises(TypeError) as e:
            get_period("1")



