import pytest
from app.calculator import Calculator


class TestCalc:
    def setup(self):
        self.calc = Calculator

    def test_multyply_caculate_correctly(self):
        assert self.calc.multiply(self, 2, 2) == 4

    def test_multyply_caculation_failed(self):
        assert self.calc.multiply(self, 2, 2) == 5

    def test_adding_caculate_correctly(self):
        assert self.calc.adding(self, 5, 5) == 10

    def test_adding_caculation_failed(self):
        assert self.calc.adding(self, 5, 5) == 12

