import pytest

class Test_math:
    def test_divide_number(self):
        pytest.xfail("need to investigate")
        num = 18
        result = num + num
        assert result == num / num

    @pytest.mark.xfail(reason = "Result add numbers not multiply numbers")
    def test_square_number(self):
        num = 10
        result = num + num
        assert result == num + num

    @pytest.mark.xfail(reason = "result and assert are correct")
    def test_cube_number(self):
        num = 18 
        result = num * num * num
        assert result == num ** 3

    @pytest.mark.xfail(run = False)
    def test_number_square(self):
        num = 18
        result = num * num
        assert result == num **2