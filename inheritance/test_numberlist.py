from hypothesis import *
import hypothesis.strategies as some
import unittest
from number_list import NumberList

class TestNumberList(unittest.TestCase):


    @given(some.lists(some.integers(min_value=-10000,max_value=10000),min_size=2))
    def testGetContainer(self,data:'list[int]'):
        test1 = NumberList(data)
        self.assertEqual(data[1:],test1.get_container())


    @given(some.lists(some.integers(min_value=-10000,max_value=10000),min_size=2))
    def testFindRange(self,data:'list[int]'):

        test1 = NumberList(data)
        self.assertEqual((max(data[1:])-min(data[1:])),test1.findRange())

    @given(some.lists(some.integers(min_value=-10000,max_value=10000),min_size=2))
    def testFindMax(self,data:'list[int]'):
        test1 = NumberList(data)
        test1.findMax()
        self.assertEqual(max(data[1:]),test1.findMax())


    @given(some.lists(some.integers(min_value=-10000,max_value=10000),min_size=2))
    def testFindMin(self,data:'list[int]'):
        test1 = NumberList(data)
        test1.findMin()
        self.assertEqual(min(data[1:]),test1.findMin())
