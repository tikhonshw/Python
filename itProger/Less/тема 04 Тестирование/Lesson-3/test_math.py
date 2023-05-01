import pytest
import math_func

@pytest.mark.parametrize('num1, num2, res', [
    (5, 5, 10),
    ('Hello', 'World', 'HelloWorld')
])
@pytest.mark.add
def test_add(num1, num2, res):
    assert math_func.add(num1, num2) == res
    assert math_func.add() == 5
    assert math_func.add(3) == 7

def test_add():
    assert math_func.mult(4, 5) == 20


@pytest.mark.add
def test_add_strings():
    result = math_func.add('Hello', 'World')
    assert type(result) is str
    assert "hello" not in result

# import unittest
# import math
#
# class TestMath(unittest.TestCase):
#
#     def test_add(self):
#         self.assertEqual(math.add(5, 7), 12)
#         self.assertEqual(math.add(5), 9)
#         self.assertEqual(math.add(), 5)
#
# if __name__ == '__main__':
#     unittest.main()