# 单元测试
import unittest
from math_utils import add, subtract

class TestMath(unittest.TestCase):
    # 测试加法
    def test_add(self):
        self.assertEqual(add(2, 3), 5)

    # 测试减法
    def test_subtract(self):
        self.assertEqual(subtract(5, 2), 3)

if __name__ == '__main__':
    unittest.main()
