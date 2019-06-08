'''
    测试结果和断言
'''

import unittest

class TestCaseAssert(unittest.TestCase):

    # def test_01_pass(self):
    #     print("123")
    
    # def test_02_error(self):
    #     1/0
    
    # def test_03_fail(self):
    #     assert 1 == 0
    
    # def test_04_assert_pass(self):
    #     assert 1 == 1
    
    def test_05_assert_unittest(self):
        '''
            unittest自带的断言用法
        '''
        a = "123"
        b = "12345"
        # self.assertEqual(a, b)
        # self.assertNotEqual(a, b)

        # self.assertIn(a, b)
        # self.assertNotIn(a, b)

        c = None
        d = ""
        # self.assertIsNone(c)
        # self.assertIsNone(d)

        e = []
        # self.assertIsInstance(a, str)
        # self.assertIsInstance(e, list)
        self.assertNotIsInstance(e, list)






# unittest.main()