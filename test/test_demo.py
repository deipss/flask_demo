import pytest


class TestClass:
    def test_one(self):
        x = "this"
        assert "h" in x,"error test "

    @pytest.mark.slow
    def test_two(self):
        x = "hello"
        assert hasattr(x, "check"),"error test "

    @pytest.mark.skip(reason="not finished")
    def test_send_http(self):
        pass
if __name__ == '__main__':
    pytest.main(['-s'])